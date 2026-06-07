"""符号索引(SQLite)。

直接把 D1 tree-sitter 抽出的符号落库,提供"按名字精确/前缀定位"的能力 ——
这是向量检索之外的互补手段:用户问"X 函数在哪",符号索引能精确命中,
而不依赖语义相似度。是 tree-sitter 解析的免费副产品。
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from common.models import RepoMap


class SymbolIndex:
    def __init__(self, db_path: str) -> None:
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.db_path = db_path
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self._conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS symbols (
                name        TEXT NOT NULL,
                name_lower  TEXT NOT NULL,
                kind        TEXT NOT NULL,
                file        TEXT NOT NULL,
                start_line  INTEGER NOT NULL,
                end_line    INTEGER NOT NULL,
                parent      TEXT
            );
            CREATE INDEX IF NOT EXISTS idx_name_lower ON symbols(name_lower);
            CREATE INDEX IF NOT EXISTS idx_file ON symbols(file);
            """
        )
        self._conn.commit()

    def build(self, repo: RepoMap) -> int:
        """清空并重建符号表,返回写入条数。"""
        self._conn.execute("DELETE FROM symbols")
        rows = [
            (s.name, s.name.lower(), s.kind, s.file, s.start_line, s.end_line, s.parent)
            for fi in repo.files
            for s in fi.symbols
        ]
        self._conn.executemany(
            "INSERT INTO symbols(name,name_lower,kind,file,start_line,end_line,parent) "
            "VALUES (?,?,?,?,?,?,?)",
            rows,
        )
        self._conn.commit()
        return len(rows)

    def lookup(self, name: str, limit: int = 10, allow_prefix: bool = True) -> list[dict]:
        """先精确(忽略大小写)匹配;allow_prefix 时不足再用前缀匹配补足。"""
        nl = name.lower()
        exact = self._conn.execute(
            "SELECT * FROM symbols WHERE name_lower = ? LIMIT ?", (nl, limit)
        ).fetchall()
        results = [dict(r) for r in exact]
        if allow_prefix and len(results) < limit:
            seen = {(r["file"], r["start_line"]) for r in results}
            prefix = self._conn.execute(
                "SELECT * FROM symbols WHERE name_lower LIKE ? AND name_lower != ? LIMIT ?",
                (nl + "%", nl, limit - len(results)),
            ).fetchall()
            for r in prefix:
                d = dict(r)
                if (d["file"], d["start_line"]) not in seen:
                    results.append(d)
        return results

    def count(self) -> int:
        return self._conn.execute("SELECT COUNT(*) FROM symbols").fetchone()[0]

    def close(self) -> None:
        self._conn.close()
