"""代码感知分块。

原则(对应 README:按函数/类边界切,而非按行硬切):
  - 顶层 function → 一个 chunk。
  - class → 一个轻量 class/header chunk + 每个 method 独立 chunk,避免大类把语义糊成一团。
  - 符号之间未覆盖的"模块级代码"(import、常量等)→ 按行窗口聚成 chunk。
  - 没抽到符号的文件 → 整文件按行窗口切,避免内容丢失。
  - 过大的符号 → 再按行窗口拆分,控制单 chunk 体积。
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import OrderedDict
from pathlib import Path

from common.models import RepoMap, SymbolInfo

MAX_CHUNK_LINES = 200   # 单 chunk 上限,超过则按窗口拆
WINDOW_LINES = 80       # 模块级 / 无符号文件的窗口大小
MIN_CHUNK_CHARS = 8     # 过滤空白 chunk
CLASS_HEADER_MAX_LINES = 80


@dataclass
class CodeChunk:
    id: str            # "file:start-end:name"
    file: str
    language: str
    kind: str          # "class" | "function" | "method" | "module" | "class_body"
    name: str          # 符号名,或 "<module>"
    start_line: int    # 1-based
    end_line: int
    text: str
    parent: str = ""
    signature: str = ""
    docstring: str = ""

    def qualified_name(self) -> str:
        return f"{self.parent}.{self.name}" if self.parent else self.name

    def embed_text(self) -> str:
        """送进 embedding 的文本:加结构化头,提升符号/路径/签名命中。"""
        header = [
            f"# {self.language} {self.kind} {self.qualified_name()} — {self.file}",
        ]
        if self.signature:
            header.append(f"signature: {self.signature}")
        if self.docstring:
            first = " ".join(self.docstring.split())[:240]
            if first:
                header.append(f"docstring: {first}")
        return "\n".join(header) + "\n" + self.text


def chunk_repo(repo: RepoMap) -> list[CodeChunk]:
    root = Path(repo.root)
    chunks: list[CodeChunk] = []
    for fi in repo.files:
        try:
            lines = (root / fi.path).read_text("utf-8", "replace").splitlines()
        except OSError:
            continue
        chunks.extend(_chunk_file(fi.path, fi.language, lines, fi))
    return list(OrderedDict((c.id, c) for c in chunks).values())


def _chunk_file(path: str, language: str, lines: list[str], fi) -> list[CodeChunk]:
    n = len(lines)
    out: list[CodeChunk] = []

    top = sorted(
        [s for s in fi.symbols if s.parent is None and 1 <= s.start_line <= n],
        key=lambda s: s.start_line,
    )

    if not top:
        out.extend(_window_chunks(path, language, lines, 1, n, name="<module>"))
        return out

    by_parent: dict[str, list[SymbolInfo]] = {}
    for s in fi.symbols:
        if s.parent:
            by_parent.setdefault(s.parent, []).append(s)
    for methods in by_parent.values():
        methods.sort(key=lambda s: s.start_line)

    covered_until = 0
    for s in top:
        if s.start_line - 1 > covered_until:
            out.extend(
                _window_chunks(path, language, lines, covered_until + 1, s.start_line - 1, name="<module>")
            )
        end = min(max(s.end_line, s.start_line), n)
        if s.kind == "class":
            out.extend(_emit_class(path, language, lines, s, end, by_parent.get(s.name, [])))
        else:
            out.extend(_emit_symbol(path, language, lines, s, end))
        covered_until = max(covered_until, end)

    if covered_until < n:
        out.extend(_window_chunks(path, language, lines, covered_until + 1, n, name="<module>"))

    return out


def _emit_class(path: str, language: str, lines: list[str], cls: SymbolInfo, end: int,
                methods: list[SymbolInfo]) -> list[CodeChunk]:
    methods = [m for m in methods if cls.start_line <= m.start_line <= end]
    if not methods:
        return _emit_symbol(path, language, lines, cls, end)

    out: list[CodeChunk] = []
    first_method = methods[0].start_line
    header_end = min(end, max(cls.start_line, first_method - 1), cls.start_line + CLASS_HEADER_MAX_LINES - 1)
    header = _make(path, language, "class", cls.name, cls.start_line, header_end, lines,
                   parent="", signature=cls.signature, docstring=cls.docstring or "")
    if header:
        out.append(header)

    covered = header_end
    for m in methods:
        if m.start_line - 1 > covered:
            out.extend(_window_chunks(path, language, lines, covered + 1, m.start_line - 1,
                                      name=f"{cls.name}.<body>", kind="class_body", parent=cls.name))
        m_end = min(max(m.end_line, m.start_line), end)
        out.extend(_emit_symbol(path, language, lines, m, m_end))
        covered = max(covered, m_end)

    if covered < end:
        out.extend(_window_chunks(path, language, lines, covered + 1, end,
                                  name=f"{cls.name}.<body>", kind="class_body", parent=cls.name))
    return out


def _emit_symbol(path: str, language: str, lines: list[str], sym: SymbolInfo, end: int) -> list[CodeChunk]:
    if end - sym.start_line + 1 <= MAX_CHUNK_LINES:
        c = _make(path, language, sym.kind, sym.name, sym.start_line, end, lines,
                  parent=sym.parent or "", signature=sym.signature, docstring=sym.docstring or "")
        return [c] if c else []
    return _window_chunks(path, language, lines, sym.start_line, end, name=sym.name, kind=sym.kind,
                          parent=sym.parent or "", signature=sym.signature, docstring=sym.docstring or "")


def _window_chunks(path, language, lines, start, end, name, kind="module", parent="",
                   signature="", docstring="") -> list[CodeChunk]:
    out: list[CodeChunk] = []
    i = start
    while i <= end:
        j = min(i + WINDOW_LINES - 1, end)
        c = _make(path, language, kind, name, i, j, lines, parent=parent,
                  signature=signature, docstring=docstring)
        if c:
            out.append(c)
        i = j + 1
    return out


def _make(path, language, kind, name, start, end, lines, parent="", signature="",
          docstring="") -> CodeChunk | None:
    text = "\n".join(lines[start - 1 : end]).strip("\n")
    if len(text.strip()) < MIN_CHUNK_CHARS and not signature:
        return None
    safe_name = name.replace(" ", "_").replace("/", "_")
    return CodeChunk(
        id=f"{path}:{start}-{end}:{kind}:{safe_name}",
        file=path,
        language=language,
        kind=kind,
        name=name,
        start_line=start,
        end_line=end,
        text=text,
        parent=parent,
        signature=signature,
        docstring=docstring,
    )
