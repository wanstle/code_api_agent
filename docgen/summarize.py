"""层次化 map-reduce 摘要。

复用 SkillSession:system 是稳定仓库前缀(跨所有调用复用 KV),
每次 map/reduce 的具体内容放 user 消息。
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

from indexing.builder import index_dir_for
from skills.session import SkillSession

MAX_MODULES = 12
MAX_FILES_PER_MODULE = 15
MAX_SYMBOLS_PER_FILE = 10


@dataclass
class DocResult:
    name: str
    modules: dict[str, str] = field(default_factory=dict)        # module -> 摘要
    module_skills: dict[str, str] = field(default_factory=dict)  # module -> 所用 skill
    architecture: str = ""                                      # 仓库整体架构文档
    meta: dict = field(default_factory=dict)


def _module_of(path: str) -> str:
    parts = path.split("/")
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]


# 关键字 → skill 的目录路由(完整版:前后端各用对应 skill 分析)
_FRONTEND_KW = ("frontend", "client", "webapp", "/web", "/ui", "components", "views", "pages")
_BACKEND_KW = ("backend", "server", "/api", "service", "controllers", "routes", "models")


def _skill_for_module(module: str) -> str:
    m = module.lower()
    if any(k in m for k in _FRONTEND_KW):
        return "frontend"
    if any(k in m for k in _BACKEND_KW):
        return "backend"
    return "architecture"


def _load(index_name: str):
    idir = index_dir_for(index_name)
    meta = json.loads((idir / "meta.json").read_text("utf-8"))
    conn = sqlite3.connect(str(idir / "symbols.db"))
    conn.row_factory = sqlite3.Row
    top: dict[str, list[str]] = {}
    for r in conn.execute(
        "SELECT file, name FROM symbols WHERE parent IS NULL "
        "ORDER BY file, CASE kind WHEN 'class' THEN 0 ELSE 1 END, start_line"
    ):
        top.setdefault(r["file"], []).append(r["name"])
    conn.close()
    return meta, top


def _group_modules(meta, top) -> list[tuple[str, list[dict]]]:
    groups: dict[str, list[dict]] = {}
    for f in meta.get("files", []):
        groups.setdefault(_module_of(f["path"]), []).append(f)
    # 按模块总符号数排序,取前 N
    ranked = sorted(
        groups.items(),
        key=lambda kv: -sum(f["symbols"] for f in kv[1]),
    )
    return ranked[:MAX_MODULES]


def _module_context(files: list[dict], top: dict[str, list[str]]) -> str:
    lines = []
    for f in sorted(files, key=lambda d: -d["symbols"])[:MAX_FILES_PER_MODULE]:
        syms = ", ".join(top.get(f["path"], [])[:MAX_SYMBOLS_PER_FILE])
        lines.append(f"- {f['path']} ({f['symbols']} 符号): {syms}")
    return "\n".join(lines)


def generate(index_name: str, progress=print) -> DocResult:
    meta, top = _load(index_name)
    modules = _group_modules(meta, top)
    session = SkillSession(index_name)
    out = DocResult(name=index_name, meta=meta)

    # --- map:逐模块摘要(按目录路由到 frontend/backend/architecture skill)---
    for mod, files in modules:
        ctx = _module_context(files, top)
        task = (
            f"以下是模块 `{mod}` 的文件与关键符号:\n{ctx}\n\n"
            f"请用 4-6 行 Markdown 总结该模块的职责、关键组件、对外提供的能力。"
        )
        skill = _skill_for_module(mod)          # ← 完整版:前后端各用对应 skill
        res = session.run(skill, task, max_tokens=400, temperature=0.2)
        out.modules[mod] = res.text.strip()
        out.module_skills[mod] = skill
        progress(f"  [map] 模块摘要: {mod}  (skill={skill}, cached_tokens={res.cached_tokens})")

    # --- reduce:汇总成整体架构文档 ---
    digest = "\n".join(f"### {m}\n{s}" for m, s in out.modules.items())
    task = (
        f"以下是本仓库各模块的摘要:\n\n{digest}\n\n"
        f"请据此产出仓库的**整体架构文档**:1) 一段总体介绍;2) 模块划分与职责表;"
        f"3) 关键组件关系/数据流;4) 技术栈。用结构化 Markdown。"
    )
    res = session.run("architecture", task, max_tokens=900, temperature=0.2)
    out.architecture = res.text.strip()
    progress(f"  [reduce] 架构文档完成  (cached_tokens={res.cached_tokens})")
    return out
