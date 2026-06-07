"""文件树扫描 + 语言识别。

职责:遍历仓库,跳过无意义目录/二进制/超大文件,按扩展名识别语言,
统计行数。产出 FileInfo 列表(此时 symbols 还是空,由 parse.py 填充)。
"""

from __future__ import annotations

import os
from pathlib import Path

from common.models import FileInfo

# 扩展名 → tree-sitter 语言名。只列 D1 关注的主流语言;
# 其余代码文件仍会被收录(language="unknown"),只是暂不抽符号。
EXT_LANG: dict[str, str] = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".mjs": "javascript",
    ".cjs": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".java": "java",
    ".go": "go",
    ".rs": "rust",
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".hpp": "cpp",
    ".hh": "cpp",
    ".cs": "csharp",
    ".rb": "ruby",
    ".php": "php",
    ".kt": "kotlin",
    ".swift": "swift",
    ".scala": "scala",
}

# 直接整目录跳过。
IGNORE_DIRS: set[str] = {
    ".git", ".hg", ".svn",
    "node_modules", "bower_components", "vendor",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".venv", "venv", "env", ".env",
    "dist", "build", "out", ".next", ".nuxt", "target",
    ".idea", ".vscode", ".cache",
    "coverage", ".gradle",
}

MAX_FILE_BYTES = 1_000_000   # >1MB 的单文件多半是生成物/数据,跳过


def scan_files(repo_root: Path) -> list[FileInfo]:
    """遍历仓库,返回 FileInfo 列表(symbols 留空)。"""
    repo_root = Path(repo_root).resolve()
    out: list[FileInfo] = []

    for dirpath, dirnames, filenames in os.walk(repo_root):
        # 原地裁剪要遍历的子目录(os.walk 的标准做法)。
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]

        for fn in filenames:
            ext = Path(fn).suffix.lower()
            if ext not in EXT_LANG:
                continue  # D1 只收录已知代码文件,降低噪声

            abs_path = Path(dirpath) / fn
            try:
                size = abs_path.stat().st_size
            except OSError:
                continue
            if size > MAX_FILE_BYTES or size == 0:
                continue
            if _is_binary(abs_path):
                continue

            rel = str(abs_path.relative_to(repo_root))
            out.append(
                FileInfo(
                    path=rel,
                    language=EXT_LANG[ext],
                    size_bytes=size,
                    lines=_count_lines(abs_path),
                )
            )

    out.sort(key=lambda f: f.path)
    return out


def _count_lines(path: Path) -> int:
    try:
        with open(path, "rb") as f:
            return sum(1 for _ in f)
    except OSError:
        return 0


def _is_binary(path: Path, sniff: int = 2048) -> bool:
    """简单判定:前若干字节里出现 NUL 即视为二进制。"""
    try:
        with open(path, "rb") as f:
            chunk = f.read(sniff)
        return b"\x00" in chunk
    except OSError:
        return True
