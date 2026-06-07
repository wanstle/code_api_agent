"""Agent 可调用的只读代码工具(限制在仓库根目录内,防越权)。"""

from __future__ import annotations

import os
import re
from pathlib import Path

MAX_GREP_RESULTS = 30
MAX_READ_LINES = 120


class RepoTools:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root).resolve()

    # --- 路径安全:确保不逃出仓库根 ---
    def _safe(self, rel: str) -> Path | None:
        p = (self.root / rel).resolve()
        try:
            p.relative_to(self.root)
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
        start = max(1, start)
        end = min(end or (start + MAX_READ_LINES - 1), start + MAX_READ_LINES - 1, len(lines))
        chosen = lines[start - 1 : end]
        body = "\n".join(f"{start + i:>5}  {ln}" for i, ln in enumerate(chosen))
        return f"{path} (行 {start}-{end}/{len(lines)}):\n{body}"

    def grep(self, pattern: str, max_results: int = MAX_GREP_RESULTS) -> str:
        try:
            rx = re.compile(pattern)
        except re.error as e:
            return f"[错误] 正则无效: {e}"
        hits: list[str] = []
        for dirpath, dirnames, filenames in os.walk(self.root):
            dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "node_modules"]
            for fn in filenames:
                fp = Path(dirpath) / fn
                try:
                    for i, line in enumerate(fp.read_text("utf-8", "replace").splitlines(), 1):
                        if rx.search(line):
                            rel = fp.relative_to(self.root)
                            hits.append(f"{rel}:{i}: {line.strip()[:160]}")
                            if len(hits) >= max_results:
                                return "\n".join(hits) + f"\n[已截断,最多 {max_results} 条]"
                except (OSError, UnicodeDecodeError):
                    continue
        return "\n".join(hits) if hits else "[无匹配]"

    def list_dir(self, path: str = ".") -> str:
        p = self._safe(path)
        if p is None or not p.is_dir():
            return f"[错误] 目录不存在或越权: {path}"
        entries = []
        for e in sorted(p.iterdir()):
            if e.name.startswith("."):
                continue
            entries.append(e.name + ("/" if e.is_dir() else ""))
        return "\n".join(entries) if entries else "[空目录]"

    def dispatch(self, action: str, args: dict) -> str:
        if action == "read_file":
            return self.read_file(args.get("path", ""), int(args.get("start", 1)),
                                  int(args["end"]) if args.get("end") else None)
        if action == "grep":
            return self.grep(args.get("pattern", ""))
        if action == "list_dir":
            return self.list_dir(args.get("path", "."))
        return f"[错误] 未知工具: {action}"
