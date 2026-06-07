"""检索接口:向量检索 + 符号检索的混合。

这是 D2 的核心交付物,也是 D5 问答 Agent 的"种子上下文"来源。
  - 向量检索:语义相似(回答"哪段代码在做 X")。
  - 符号检索:精确命中(回答"X 函数/类在哪"),对查询里的标识符做精确/前缀匹配。
两路结果合并去重:符号精确命中优先(高置信),再补语义结果。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path

from indexing.builder import index_dir_for
from indexing.embed import Embedder
from indexing.symbol_index import SymbolIndex
from indexing.vector_store import VectorStore

_IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
_SNIPPET_MAX_LINES = 60

# 自然语言常见词,避免把它们当符号名去前缀匹配(如 "from" 误命中 from_bytes)。
_STOPWORDS = {
    "the", "and", "for", "are", "from", "how", "does", "what", "where", "which",
    "with", "this", "that", "into", "out", "value", "values", "code", "file",
    "files", "function", "class", "method", "read", "reading", "write", "get",
    "set", "use", "using", "via", "all", "any", "can", "you", "your", "its",
}


def _is_codeish(token: str) -> bool:
    """像标识符的 token:含下划线或大写(CamelCase/snake_case)。"""
    return "_" in token or any(c.isupper() for c in token)


def _is_test_file(path: str) -> bool:
    p = path.lower()
    return p.startswith(("test", "tests/")) or "/test" in p or "test_" in p


@dataclass
class CodeSnippet:
    file: str
    start_line: int
    end_line: int
    name: str
    kind: str
    score: float
    source: str        # "symbol" | "vector"
    text: str

    def location(self) -> str:
        return f"{self.file}:{self.start_line}"

    def to_dict(self) -> dict:
        return asdict(self)


class Retriever:
    def __init__(self, name: str) -> None:
        idir = index_dir_for(name)
        meta_path = idir / "meta.json"
        if not meta_path.exists():
            raise FileNotFoundError(f"未找到索引: {idir}(先运行 build)")
        self.meta = json.loads(meta_path.read_text("utf-8"))
        self.root = Path(self.meta["root"])
        self._embedder = Embedder(self.meta.get("embed_model"))
        self._vs = VectorStore(str(idir / "chroma"))
        self._si = SymbolIndex(str(idir / "symbols.db"))

    def retrieve(self, query: str, k: int = 8) -> list[CodeSnippet]:
        symbol_hits = self._symbol_search(query, limit=max(3, k // 2))
        vector_hits = self._vector_search(query, k=k)
        return self._merge(symbol_hits, vector_hits, k)

    # --- 符号检索 ---
    def _symbol_search(self, query: str, limit: int) -> list[CodeSnippet]:
        out: list[CodeSnippet] = []
        seen: set[tuple] = set()
        for token in dict.fromkeys(_IDENT.findall(query)):  # 去重保序
            codeish = _is_codeish(token)
            # 普通英文词:跳过停用词,且只做精确匹配(不前缀),避免噪声。
            if not codeish and token.lower() in _STOPWORDS:
                continue
            for row in self._si.lookup(token, limit=3, allow_prefix=codeish):
                key = (row["file"], row["start_line"])
                if key in seen:
                    continue
                seen.add(key)
                out.append(
                    CodeSnippet(
                        file=row["file"],
                        start_line=row["start_line"],
                        end_line=row["end_line"],
                        name=(f"{row['parent']}.{row['name']}" if row["parent"] else row["name"]),
                        kind=row["kind"],
                        score=1.0,  # 精确命中,给满分
                        source="symbol",
                        text=self._read_slice(row["file"], row["start_line"], row["end_line"]),
                    )
                )
                if len(out) >= limit:
                    return out
        return out

    # --- 向量检索 ---
    def _vector_search(self, query: str, k: int) -> list[CodeSnippet]:
        qv = self._embedder.embed_one(query)
        rows = self._vs.query(qv, k=k)
        return [
            CodeSnippet(
                file=r["file"],
                start_line=r["start_line"],
                end_line=r["end_line"],
                name=r["name"],
                kind=r["kind"],
                score=round(r["score"], 4),
                source="vector",
                text=r["text"],
            )
            for r in rows
        ]

    def _merge(self, symbol_hits, vector_hits, k) -> list[CodeSnippet]:
        out: list[CodeSnippet] = []
        seen: set[tuple] = set()
        # 排序键:源码优先于测试;其次相似度;符号精确命中略优于向量。
        candidates = sorted(
            symbol_hits + vector_hits,
            key=lambda s: (_is_test_file(s.file), -s.score, 0 if s.source == "symbol" else 1),
        )
        for s in candidates:
            if self._overlaps(seen, s):
                continue
            seen.add((s.file, s.start_line, s.end_line))
            out.append(s)
            if len(out) >= k:
                break
        return out

    @staticmethod
    def _overlaps(seen: set[tuple], s: CodeSnippet) -> bool:
        # 同文件、行区间有重叠则视为重复(避免符号命中与其所在 chunk 重复展示)。
        for (f, a, b) in seen:
            if f == s.file and not (s.end_line < a or s.start_line > b):
                return True
        return False

    def _read_slice(self, file: str, start: int, end: int) -> str:
        try:
            lines = (self.root / file).read_text("utf-8", "replace").splitlines()
        except OSError:
            return ""
        end = min(end, start + _SNIPPET_MAX_LINES - 1, len(lines))
        return "\n".join(lines[start - 1 : end])
