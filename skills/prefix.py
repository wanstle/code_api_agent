"""构建"仓库概览"稳定前缀。

要点(对应 README 3.3):
  - 内容是**压缩概览**(技术栈 + 关键文件与符号 + 通用规则),不是全量代码。
  - **token 级稳定**:同一索引每次构建出完全一致的文本,cache_prompt 才能命中。
    因此所有取数都做确定性排序,且按预算截断。
  - 控制在约 2k–8k token:用字符数近似(~4 char/token)做上限。
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from indexing.builder import index_dir_for

# 字符预算(~4 char/token → ~6000 char ≈ 1.5k token,稳妥落在预算内)
MAX_PREFIX_CHARS = 6000
TOP_FILES = 30
TOP_SYMBOLS_PER_FILE = 8


def build_repo_prefix(index_name: str) -> str:
    idir = index_dir_for(index_name)
    meta = json.loads((idir / "meta.json").read_text("utf-8"))
    top_syms = _top_symbols_by_file(str(idir / "symbols.db"))

    lines: list[str] = []
    lines.append(f'你正在分析名为 "{meta["name"]}" 的代码仓库。以下是仓库概览(稳定上下文)。')
    lines.append("")
    lines.append(f"规模:{meta['num_files']} 文件 / {meta['num_symbols']} 符号。")

    # 技术栈
    langs = meta.get("languages", {})
    if langs:
        stack = ", ".join(f"{k}:{v}" for k, v in langs.items())
        lines.append(f"技术栈(语言:文件数):{stack}")
    lines.append("")

    # 关键文件与符号(源码优先于测试,其次按符号数;确定性排序后截断)
    lines.append("## 关键文件与符号(源码优先,节选)")
    budget = MAX_PREFIX_CHARS - sum(len(x) + 1 for x in lines) - 200  # 预留尾部规则
    files_ranked = sorted(
        meta.get("files", []),
        key=lambda f: (_is_test(f["path"]), -f["symbols"]),
    )
    for f in files_ranked[:TOP_FILES]:
        if f["symbols"] == 0:
            continue
        syms = top_syms.get(f["path"], [])[:TOP_SYMBOLS_PER_FILE]
        sym_str = ", ".join(syms)
        row = f"- {f['path']} ({f['lang']}, {f['symbols']} 符号): {sym_str}"
        if budget - len(row) < 0:
            lines.append("- …(更多文件略)")
            break
        lines.append(row)
        budget -= len(row) + 1

    # 通用规则(固定文本)
    lines.append("")
    lines.append("## 通用规则")
    lines.append("- 回答须基于上述仓库结构与随后提供的代码片段,不要臆测不存在的代码。")
    lines.append("- 涉及具体代码时,给出 `文件:行号` 形式的引用。")

    return "\n".join(lines)


def _is_test(path: str) -> bool:
    p = path.lower()
    return p.startswith(("test", "tests/")) or "/test" in p or "test_" in p


def _top_symbols_by_file(db_path: str) -> dict[str, list[str]]:
    """每个文件的代表性符号(类优先,其次顶层函数),确定性排序。"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        # 类与顶层函数优先(parent 为空),按文件、种类、行号稳定排序
        "SELECT file, name, kind, parent FROM symbols "
        "ORDER BY file, (parent IS NOT NULL), "
        "CASE kind WHEN 'class' THEN 0 ELSE 1 END, start_line"
    ).fetchall()
    conn.close()

    out: dict[str, list[str]] = {}
    for r in rows:
        if r["parent"]:  # 概览里只列顶层符号,方法不展开
            continue
        out.setdefault(r["file"], []).append(r["name"])
    return out
