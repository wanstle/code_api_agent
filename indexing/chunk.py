"""代码感知分块。

原则(对应 README:按函数/类边界切,而非按行硬切):
  - 每个顶层符号(class / 顶层 function,parent 为 None)→ 一个 chunk,自带完整语义。
  - 符号之间未覆盖的"模块级代码"(import、常量等)→ 按行窗口聚成 chunk。
  - 没抽到符号的文件 → 整文件按行窗口切,避免内容丢失。
  - 过大的符号 → 再按行窗口拆分,控制单 chunk 体积。
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import OrderedDict
from pathlib import Path

from common.models import RepoMap

MAX_CHUNK_LINES = 200   # 单 chunk 上限,超过则按窗口拆
WINDOW_LINES = 80       # 模块级 / 无符号文件的窗口大小
MIN_CHUNK_CHARS = 8     # 过滤空白 chunk


@dataclass
class CodeChunk:
    id: str            # "file:start-end"
    file: str
    language: str
    kind: str          # "class" | "function" | "module"
    name: str          # 符号名,或 "<module>"
    start_line: int    # 1-based
    end_line: int
    text: str

    def embed_text(self) -> str:
        """送进 embedding 的文本:加一行轻量头,提升检索命中。"""
        return f"# {self.language} {self.kind} {self.name} — {self.file}\n{self.text}"


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

    # 顶层符号(parent 为 None);按起始行排序。
    top = sorted(
        [s for s in fi.symbols if s.parent is None and 1 <= s.start_line <= n],
        key=lambda s: s.start_line,
    )

    if not top:
        # 无符号文件:整文件窗口切。
        out.extend(_window_chunks(path, language, lines, 1, n, name="<module>"))
        return out

    covered_until = 0  # 已处理到的行号(1-based,闭区间)
    for s in top:
        # 符号之前未覆盖的模块级代码。
        if s.start_line - 1 > covered_until:
            out.extend(
                _window_chunks(
                    path, language, lines, covered_until + 1, s.start_line - 1, name="<module>"
                )
            )
        end = min(max(s.end_line, s.start_line), n)
        out.extend(_emit_symbol(path, language, lines, s.kind, s.name, s.start_line, end))
        covered_until = max(covered_until, end)

    # 末尾剩余的模块级代码。
    if covered_until < n:
        out.extend(_window_chunks(path, language, lines, covered_until + 1, n, name="<module>"))

    return out


def _emit_symbol(path, language, lines, kind, name, start, end) -> list[CodeChunk]:
    if end - start + 1 <= MAX_CHUNK_LINES:
        c = _make(path, language, kind, name, start, end, lines)
        return [c] if c else []
    # 过大符号:按窗口拆,名字沿用符号名。
    return _window_chunks(path, language, lines, start, end, name=name, kind=kind)


def _window_chunks(path, language, lines, start, end, name, kind="module") -> list[CodeChunk]:
    out: list[CodeChunk] = []
    i = start
    while i <= end:
        j = min(i + WINDOW_LINES - 1, end)
        c = _make(path, language, kind, name, i, j, lines)
        if c:
            out.append(c)
        i = j + 1
    return out


def _make(path, language, kind, name, start, end, lines) -> CodeChunk | None:
    text = "\n".join(lines[start - 1 : end]).strip("\n")
    if len(text.strip()) < MIN_CHUNK_CHARS:
        return None
    return CodeChunk(
        id=f"{path}:{start}-{end}",
        file=path,
        language=language,
        kind=kind,
        name=name,
        start_line=start,
        end_line=end,
        text=text,
    )
