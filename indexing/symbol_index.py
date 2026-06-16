"""符号索引(SQLite)。

直接把 D1 tree-sitter 抽出的符号落库,提供"按名字/限定名/签名精确定位"的能力。
这是向量检索之外的互补手段:用户问"X 函数在哪",符号索引能精确命中,
而不依赖语义相似度。
"""

from __future__ import annotations

import sqlite3
from threading import RLock
from pathlib import Path

from common.models import RepoMap


class SymbolIndex:
    def __init__(self, db_path: str) -> None:
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.db_path = db_path
        self._lock = RLock()
        self._conn = sqlite3.connect(db_path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        with self._lock:
            self._conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS symbols (
                    name             TEXT NOT NULL,
                    name_lower       TEXT NOT NULL,
                    qualified_name   TEXT NOT NULL DEFAULT '',
                    qualified_lower  TEXT NOT NULL DEFAULT '',
                    kind             TEXT NOT NULL,
                    file             TEXT NOT NULL,
                    module           TEXT NOT NULL DEFAULT '',
                    start_line       INTEGER NOT NULL,
                    end_line         INTEGER NOT NULL,
                    parent           TEXT,
                    signature        TEXT NOT NULL DEFAULT '',
                    docstring        TEXT
                );
                """
            )
            self._ensure_columns()
            self._conn.executescript(
                """
                CREATE INDEX IF NOT EXISTS idx_name_lower ON symbols(name_lower);
                CREATE INDEX IF NOT EXISTS idx_qualified_lower ON symbols(qualified_lower);
                CREATE INDEX IF NOT EXISTS idx_file ON symbols(file);
                CREATE INDEX IF NOT EXISTS idx_module ON symbols(module);
                """
            )
            self._conn.commit()

    def _ensure_columns(self) -> None:
        existing = {
            r["name"] for r in self._conn.execute("PRAGMA table_info(symbols)").fetchall()
        }
        columns = {
            "qualified_name": "TEXT NOT NULL DEFAULT ''",
            "qualified_lower": "TEXT NOT NULL DEFAULT ''",
            "module": "TEXT NOT NULL DEFAULT ''",
            "signature": "TEXT NOT NULL DEFAULT ''",
            "docstring": "TEXT",
        }
        for name, spec in columns.items():
            if name not in existing:
                self._conn.execute(f"ALTER TABLE symbols ADD COLUMN {name} {spec}")

    def build(self, repo: RepoMap) -> int:
        """清空并重建符号表,返回写入条数。"""
        rows = []
        for fi in repo.files:
            module = _module_of(fi.path)
            for s in fi.symbols:
                qual = s.qualified_name()
                rows.append((
                    s.name,
                    s.name.lower(),
                    qual,
                    qual.lower(),
                    s.kind,
                    s.file,
                    module,
                    s.start_line,
                    s.end_line,
                    s.parent,
                    s.signature,
                    s.docstring,
                ))
        with self._lock:
            self._conn.execute("DELETE FROM symbols")
            self._conn.executemany(
                "INSERT INTO symbols("
                "name,name_lower,qualified_name,qualified_lower,kind,file,module,"
                "start_line,end_line,parent,signature,docstring) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                rows,
            )
            self._conn.commit()
        return len(rows)

    def lookup(self, name: str, limit: int = 10, allow_prefix: bool = True) -> list[dict]:
        """先精确匹配 name/qualified_name;allow_prefix 时再用前缀补足。"""
        nl = name.lower().strip()
        if not nl:
            return []
        with self._lock:
            exact = self._conn.execute(
                "SELECT * FROM symbols WHERE name_lower = ? OR qualified_lower = ? "
                "ORDER BY CASE WHEN qualified_lower = ? THEN 0 ELSE 1 END, file, start_line LIMIT ?",
                (nl, nl, nl, limit),
            ).fetchall()
            results = [dict(r) for r in exact]
            if allow_prefix and len(results) < limit:
                seen = {(r["file"], r["start_line"]) for r in results}
                prefix = self._conn.execute(
                    "SELECT * FROM symbols WHERE "
                    "(name_lower LIKE ? OR qualified_lower LIKE ?) "
                    "AND name_lower != ? AND qualified_lower != ? "
                    "ORDER BY file, start_line LIMIT ?",
                    (nl + "%", nl + "%", nl, nl, limit - len(results)),
                ).fetchall()
                for r in prefix:
                    d = dict(r)
                    if (d["file"], d["start_line"]) not in seen:
                        results.append(d)
        return results

    def count(self) -> int:
        with self._lock:
            return self._conn.execute("SELECT COUNT(*) FROM symbols").fetchone()[0]

    def close(self) -> None:
        with self._lock:
            self._conn.close()


def _module_of(path: str) -> str:
    parts = path.replace("\\", "/").split("/")
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]
