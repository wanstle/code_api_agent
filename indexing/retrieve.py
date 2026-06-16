"""检索接口:向量检索 + 符号检索的混合。

这是 D2 的核心交付物,也是 D5 问答 Agent 的"种子上下文"来源。
  - 向量检索:语义相似(回答"哪段代码在做 X")。
  - 符号检索:精确命中(回答"X 函数/类在哪"),对查询里的标识符做精确/前缀匹配。
  - 规则重排:路径/符号 token 命中加分,测试文件降权,符号命中优先。
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
_WORD = re.compile(r"[A-Za-z][A-Za-z0-9_]{1,}")
_CAMEL_SPLIT = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_SNIPPET_MAX_LINES = 80
VECTOR_CANDIDATE_MULTIPLIER = 4

_STOPWORDS = {
    "the", "and", "for", "are", "from", "how", "does", "what", "where", "which",
    "with", "this", "that", "into", "out", "value", "values", "code", "file",
    "files", "function", "class", "method", "read", "reading", "write", "get",
    "set", "use", "using", "via", "all", "any", "can", "you", "your", "its",
    "show", "tell", "about", "implemented", "defined", "definition",
}
_KIND_WORDS = {"class", "function", "method", "func"}


def _is_codeish(token: str) -> bool:
    return "_" in token or "." in token or "/" in token or any(c.isupper() for c in token)


def _is_test_file(path: str) -> bool:
    p = path.lower()
    return p.startswith(("test", "tests/")) or "/test" in p or "test_" in p


def _split_identifier(token: str) -> list[str]:
    pieces: list[str] = []
    for part in re.split(r"[_./:-]+", token):
        if not part:
            continue
        pieces.extend(x for x in _CAMEL_SPLIT.split(part) if x)
    return pieces


def _stem_term(term: str) -> str:
    for suffix in ("ing", "es", "s"):
        if term.endswith(suffix) and len(term) > len(suffix) + 3:
            return term[: -len(suffix)]
    return term


def _query_terms(query: str) -> set[str]:
    terms: set[str] = set()
    for raw in _WORD.findall(query):
        low = raw.lower()
        if low in _STOPWORDS or len(low) < 3:
            continue
        terms.add(low)
        terms.add(_stem_term(low))
        for piece in _split_identifier(raw):
            plow = piece.lower()
            if plow not in _STOPWORDS and len(plow) >= 3:
                terms.add(plow)
                terms.add(_stem_term(plow))
    for raw in re.findall(r"[A-Za-z0-9_./-]+", query):
        if "/" in raw or "." in raw or "_" in raw:
            terms.add(raw.lower().strip("`'\""))
    return terms


def _expanded_query(query: str) -> str:
    extras: list[str] = []
    lowered = query.lower()
    for tok in _IDENT.findall(query):
        parts = _split_identifier(tok)
        if len(parts) > 1:
            extras.append(" ".join(parts))
            extras.append("_".join(p.lower() for p in parts))
    if ("parse" in lowered or "parses" in lowered or "parsing" in lowered) and (
        "argument" in lowered or "option" in lowered or "command line" in lowered
    ):
        extras.extend(["parse_args", "parser", "option_parser", "OptionParser", "_OptionParser"])
    if not extras:
        return query
    return query + "\n" + " ".join(dict.fromkeys(extras))


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
    signature: str = ""

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
        expanded = _expanded_query(query)
        terms = _query_terms(expanded)
        symbol_hits = self._symbol_search(expanded, limit=max(8, k))
        vector_hits = self._vector_search(expanded, k=max(k, k * VECTOR_CANDIDATE_MULTIPLIER))
        return self._merge(symbol_hits, vector_hits, k, terms)

    def _symbol_search(self, query: str, limit: int) -> list[CodeSnippet]:
        out: list[CodeSnippet] = []
        seen: set[tuple] = set()
        tokens = list(dict.fromkeys(_IDENT.findall(query)))
        dotted = re.findall(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+", query)
        for token in dict.fromkeys(dotted + tokens):
            codeish = _is_codeish(token)
            if not codeish and token.lower() in _STOPWORDS:
                continue
            for row in self._si.lookup(token, limit=5, allow_prefix=codeish):
                key = (row["file"], row["start_line"])
                if key in seen:
                    continue
                seen.add(key)
                name = row.get("qualified_name") or (
                    f"{row['parent']}.{row['name']}" if row.get("parent") else row["name"]
                )
                out.append(
                    CodeSnippet(
                        file=row["file"],
                        start_line=row["start_line"],
                        end_line=row["end_line"],
                        name=name,
                        kind=row["kind"],
                        score=1.0,
                        source="symbol",
                        text=self._read_slice(row["file"], row["start_line"], row["end_line"]),
                        signature=row.get("signature") or "",
                    )
                )
                if len(out) >= limit:
                    return out
        return out

    def _vector_search(self, query: str, k: int) -> list[CodeSnippet]:
        qv = self._embedder.embed_one(query)
        rows = self._vs.query(qv, k=k)
        return [
            CodeSnippet(
                file=r["file"],
                start_line=r["start_line"],
                end_line=r["end_line"],
                name=r.get("qualified_name") or r["name"],
                kind=r["kind"],
                score=round(r["score"], 4),
                source="vector",
                text=r["text"],
                signature=r.get("signature") or "",
            )
            for r in rows
        ]

    def _merge(self, symbol_hits, vector_hits, k, terms: set[str]) -> list[CodeSnippet]:
        out: list[CodeSnippet] = []
        seen: set[tuple] = set()
        candidates = symbol_hits + vector_hits
        ranked = sorted(candidates, key=lambda s: self._rank_key(s, terms))
        for s in ranked:
            if self._overlaps(seen, s):
                continue
            seen.add((s.file, s.start_line, s.end_line))
            out.append(s)
            if len(out) >= k:
                break
        return out

    def _rank_key(self, s: CodeSnippet, terms: set[str]) -> tuple:
        bonus = self._term_bonus(s, terms)
        source_bonus = 0.20 if s.source == "symbol" else 0.0
        kind_bonus = 0.08 if s.kind in ("function", "method", "class") else 0.0
        test_penalty = 0.35 if _is_test_file(s.file) else 0.0
        adjusted = s.score + bonus + source_bonus + kind_bonus - test_penalty
        return (_is_test_file(s.file), -adjusted, 0 if s.source == "symbol" else 1, s.file, s.start_line)

    @staticmethod
    def _term_bonus(s: CodeSnippet, terms: set[str]) -> float:
        if not terms:
            return 0.0
        hay_name = s.name.lower()
        hay_path = s.file.lower()
        hay_sig = s.signature.lower()
        bonus = 0.0
        for t in terms:
            if not t or t in _KIND_WORDS:
                continue
            if t == hay_name or hay_name.endswith("." + t):
                bonus += 0.35
            elif t in hay_name:
                bonus += 0.18
            if t in hay_path:
                bonus += 0.12
            if hay_sig and t in hay_sig:
                bonus += 0.08
        return min(bonus, 0.9)

    @staticmethod
    def _overlaps(seen: set[tuple], s: CodeSnippet) -> bool:
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
