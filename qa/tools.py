"""Agent 可调用的只读代码工具(限制在仓库根目录内,防越权)。"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

MAX_GREP_RESULTS = 20
MAX_READ_LINES = 90
MAX_LIST_ENTRIES = 120
MAX_GREP_FILE_BYTES = 1_000_000
MAX_DOC_LINES = 140

_SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".cache",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "target",
    "third_party",
    "vendor",
    "models",
}
_SKIP_SUFFIXES = {
    ".7z", ".bin", ".bmp", ".bz2", ".ckpt", ".dll", ".dylib", ".gif",
    ".gguf", ".gz", ".ico", ".jpeg", ".jpg", ".lock", ".mp4", ".onnx",
    ".pdf", ".png", ".pt", ".pth", ".pyc", ".safetensors", ".so", ".tar",
    ".webp", ".zip",
}


def _as_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


class RepoTools:
    def __init__(self, root: str | Path, docs_root: str | Path | None = None) -> None:
        self.root = Path(root).resolve()
        self.docs_root = Path(docs_root).resolve() if docs_root else None

    # --- 路径安全:确保不逃出仓库根 ---
    def _safe(self, rel: str) -> Path | None:
        rel = rel or "."
        p = (self.root / rel).resolve()
        try:
            p.relative_to(self.root)
        except ValueError:
            return None
        return p


    def _safe_doc(self, rel: str) -> Path | None:
        if self.docs_root is None:
            return None
        rel = rel or "."
        p = (self.docs_root / rel).resolve()
        try:
            p.relative_to(self.docs_root)
        except ValueError:
            return None
        return p

    def read_file(self, path: str, start: int = 1, end: int | None = None) -> str:
        p = self._safe(path)
        if p is None or not p.is_file():
            return f"[错误] 文件不存在或越权: {path}"
        try:
            lines = p.read_text("utf-8", "replace").splitlines()
        except OSError as e:
            return f"[错误] 读取失败: {e}"
        if not lines:
            return f"{path}: [空文件]"

        start = max(1, start)
        if start > len(lines):
            return f"[错误] 起始行超出文件长度: {path}:{start} > {len(lines)}"
        requested_end = end or (start + MAX_READ_LINES - 1)
        end = min(max(start, requested_end), start + MAX_READ_LINES - 1, len(lines))
        chosen = lines[start - 1 : end]
        body = "\n".join(f"{path}:{start + i}: {ln}" for i, ln in enumerate(chosen))
        return (
            f"TOOL_RESULT read_file path={path} lines={start}-{end}/{len(lines)}\n"
            f"{body}"
        )

    def grep(self, pattern: str, max_results: int = MAX_GREP_RESULTS) -> str:
        if not pattern:
            return "[错误] grep 需要 pattern"
        try:
            rx = re.compile(pattern)
        except re.error as e:
            return f"[错误] 正则无效: {e}"
        hits: list[str] = []
        skipped = 0
        for dirpath, dirnames, filenames in os.walk(self.root):
            dirnames[:] = [d for d in dirnames if d not in _SKIP_DIRS and not d.startswith(".")]
            for fn in filenames:
                fp = Path(dirpath) / fn
                if fp.suffix.lower() in _SKIP_SUFFIXES:
                    skipped += 1
                    continue
                try:
                    if fp.stat().st_size > MAX_GREP_FILE_BYTES:
                        skipped += 1
                        continue
                    for i, line in enumerate(fp.read_text("utf-8", "replace").splitlines(), 1):
                        if rx.search(line):
                            rel = fp.relative_to(self.root)
                            hits.append(f"{rel}:{i}: {line.strip()[:180]}")
                            if len(hits) >= max_results:
                                return (
                                    f"TOOL_RESULT grep pattern={pattern!r} results={len(hits)} truncated=true\n"
                                    + "\n".join(hits)
                                )
                except (OSError, UnicodeDecodeError):
                    skipped += 1
                    continue
        if not hits:
            return f"TOOL_RESULT grep pattern={pattern!r} results=0 skipped={skipped}\n[无匹配]"
        return f"TOOL_RESULT grep pattern={pattern!r} results={len(hits)} skipped={skipped}\n" + "\n".join(hits)

    def list_dir(self, path: str = ".") -> str:
        p = self._safe(path)
        if p is None or not p.is_dir():
            return f"[错误] 目录不存在或越权: {path}"
        entries = []
        for e in sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
            if e.name.startswith(".") or e.name in _SKIP_DIRS:
                continue
            entries.append(e.name + ("/" if e.is_dir() else ""))
            if len(entries) >= MAX_LIST_ENTRIES:
                return (
                    f"TOOL_RESULT list_dir path={path or '.'} entries={len(entries)} truncated=true\n"
                    + "\n".join(entries)
                )
        if not entries:
            return f"TOOL_RESULT list_dir path={path or '.'} entries=0\n[空目录]"
        return f"TOOL_RESULT list_dir path={path or '.'} entries={len(entries)}\n" + "\n".join(entries)


    def list_docs(self, path: str = ".") -> str:
        p = self._safe_doc(path)
        if p is None:
            return "[错误] 未找到已生成文档目录;请先运行 `python -m cli doc <repo>`"
        if not p.is_dir():
            return f"[错误] 文档目录不存在或越权: {path}"
        entries = []
        for e in sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
            if e.name.startswith("."):
                continue
            if e.is_dir() or e.suffix.lower() == ".md":
                entries.append(e.name + ("/" if e.is_dir() else ""))
            if len(entries) >= MAX_LIST_ENTRIES:
                return (
                    f"TOOL_RESULT list_docs path={path or '.'} entries={len(entries)} truncated=true\n"
                    + "\n".join(entries)
                )
        if not entries:
            return f"TOOL_RESULT list_docs path={path or '.'} entries=0\n[空目录]"
        return f"TOOL_RESULT list_docs path={path or '.'} entries={len(entries)}\n" + "\n".join(entries)

    def read_doc(self, path: str, start: int = 1, end: int | None = None) -> str:
        p = self._safe_doc(path)
        if p is None:
            return "[错误] 未找到已生成文档目录;请先运行 `python -m cli doc <repo>`"
        if not p.is_file() or p.suffix.lower() != ".md":
            return f"[错误] 文档文件不存在、不是 Markdown 或越权: {path}"
        try:
            lines = p.read_text("utf-8", "replace").splitlines()
        except OSError as e:
            return f"[错误] 读取文档失败: {e}"
        if not lines:
            return f"{path}: [空文档]"
        start = max(1, start)
        if start > len(lines):
            return f"[错误] 起始行超出文档长度: {path}:{start} > {len(lines)}"
        requested_end = end or (start + MAX_DOC_LINES - 1)
        end = min(max(start, requested_end), start + MAX_DOC_LINES - 1, len(lines))
        chosen = lines[start - 1 : end]
        body = "\n".join(f"docs:{path}:{start + i}: {ln}" for i, ln in enumerate(chosen))
        return (
            f"TOOL_RESULT read_doc path={path} lines={start}-{end}/{len(lines)}\n"
            f"{body}"
        )

    def dispatch(self, action: str, args: dict) -> str:
        if action == "read_file":
            return self.read_file(
                str(args.get("path", "")),
                _as_int(args.get("start"), 1),
                _as_int(args.get("end"), 0) or None,
            )
        if action == "grep":
            return self.grep(str(args.get("pattern", "")))
        if action == "list_dir":
            return self.list_dir(str(args.get("path", ".")))
        if action == "list_docs":
            return self.list_docs(str(args.get("path", ".")))
        if action == "read_doc":
            return self.read_doc(
                str(args.get("path", "")),
                _as_int(args.get("start"), 1),
                _as_int(args.get("end"), 0) or None,
            )
        return f"[错误] 未知工具: {action}"
