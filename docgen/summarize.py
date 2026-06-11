"""层次化 map-reduce 摘要（增强版：带源码片段）。

复用 SkillSession:system 是稳定仓库前缀(跨所有调用复用 KV),
每次 map/reduce 的具体内容放 user 消息。

关键改进: map 阶段喂入每个符号的真实源码片段(按行号精确截取),
LLM 能读到实际方法签名/参数/返回值,不再凭空编造 API。
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

from indexing.builder import index_dir_for
from skills.session import SkillSession

MAX_MODULES = 12
MAX_FILES_PER_MODULE = 8
MAX_SYMBOLS_PER_FILE = 3           # 每文件最多展示的符号数
MAX_SYMBOL_SNIPPET_LINES = 18      # 单个符号截取的源码最大行数
MAX_MODULE_CONTEXT_CHARS = 10000  # 适配 8k ctx: prefix + rules + module material
MAX_REDUCE_DIGEST_CHARS = 12000


@dataclass
class DocResult:
    name: str
    modules: dict[str, str] = field(default_factory=dict)   # module -> 摘要
    architecture: str = ""                                  # 仓库整体架构文档
    meta: dict = field(default_factory=dict)


def _module_of(path: str) -> str:
    parts = path.replace("\\", "/").split("/")
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]


def _load(index_name: str):
    """从索引加载元数据、符号清单 与 源码片段。

    Returns:
        meta:     meta.json 内容
        top:      每个文件 → 顶层符号名列表
        detail:   每个文件 → [{name, kind, line}, ...]
        snippets: 每个文件 → [(name, kind, line, code_text), ...]
    """
    idir = index_dir_for(index_name)
    meta = json.loads((idir / "meta.json").read_text("utf-8"))
    repo_root = Path(meta["root"])

    conn = sqlite3.connect(str(idir / "symbols.db"))
    conn.row_factory = sqlite3.Row
    top: dict[str, list[str]] = {}
    detail: dict[str, list[dict]] = {}
    snippets: dict[str, list[tuple]] = {}

    rows = conn.execute(
        "SELECT file, name, kind, start_line, end_line, parent FROM symbols "
        "WHERE parent IS NULL "
        "ORDER BY file, CASE kind WHEN 'class' THEN 0 ELSE 1 END, start_line"
    ).fetchall()

    for r in rows:
        fpath = r["file"]
        top.setdefault(fpath, []).append(r["name"])
        detail.setdefault(fpath, []).append({
            "name": r["name"], "kind": r["kind"], "line": r["start_line"],
        })

        # 读取该符号的真实源码
        try:
            src_lines = (repo_root / fpath).read_text("utf-8", "replace").splitlines()
        except OSError:
            src_lines = []

        start = max(0, r["start_line"] - 1)
        end = min(len(src_lines), r["end_line"])
        if end - start > MAX_SYMBOL_SNIPPET_LINES:
            end = start + MAX_SYMBOL_SNIPPET_LINES
        code = "\n".join(src_lines[start:end]) if src_lines else "(源码不可用)"

        snippets.setdefault(fpath, []).append(
            (r["name"], r["kind"], r["start_line"], code)
        )

    conn.close()
    return meta, top, detail, snippets


def _group_modules(meta, top) -> list[tuple[str, list[dict]]]:
    groups: dict[str, list[dict]] = {}
    for f in meta.get("files", []):
        groups.setdefault(_module_of(f["path"]), []).append(f)
    ranked = sorted(
        groups.items(),
        key=lambda kv: -sum(f["symbols"] for f in kv[1]),
    )
    return ranked[:MAX_MODULES]


def _module_context(
    files: list[dict],
    top: dict[str, list[str]],
    detail: dict[str, list[dict]],
    snippets: dict[str, list[tuple]],
) -> str:
    """构建模块上下文:文件清单 + 每文件的符号及其真实源码。"""
    lines = []
    for f in sorted(files, key=lambda d: -d["symbols"])[:MAX_FILES_PER_MODULE]:
        path = f["path"]
        syms = detail.get(path, [])
        code_snippets = snippets.get(path, [])

        # 分类展示
        classes = [(s["name"], s["line"]) for s in syms if s["kind"] == "class"]
        funcs = [(s["name"], s["line"]) for s in syms if s["kind"] != "class"]

        parts = []
        if classes:
            parts.append("类: " + ", ".join(f"{n}(:{l})" for n, l in classes))
        if funcs:
            parts.append("函数: " + ", ".join(f"{n}(:{l})" for n, l in funcs))
        sym_str = "; ".join(parts) if parts else "(无顶层符号)"

        lines.append(
            f"### {path} ({f['lang']}, {f['symbols']} 符号, {f['lines']} 行)\n"
            f"符号清单: {sym_str}\n"
        )

        # 贴出实际源码（按种类分组）
        if code_snippets:
            lines.append("**源码片段**:")
            for name, kind, line, code in code_snippets[:MAX_SYMBOLS_PER_FILE]:
                lines.append(
                    f"\n`{kind} {name}` ({path}:{line}):\n"
                    f"```{f['lang']}\n{code}\n```\n"
                )

    text = "\n".join(lines)
    if len(text) > MAX_MODULE_CONTEXT_CHARS:
        text = text[:MAX_MODULE_CONTEXT_CHARS] + "\n\n[模块上下文已按 8k ctx 预算截断]"
    return text


def generate(index_name: str, progress=print) -> DocResult:
    meta, top, detail, snippets = _load(index_name)
    modules = _group_modules(meta, top)
    session = SkillSession(index_name)
    out = DocResult(name=index_name, meta=meta)

    # --- map: 逐模块 API 参考文档（带真实源码） ---
    for mod, files in modules:
        ctx = _module_context(files, top, detail, snippets)
        task = (
            f"Below is the **real source code** for module `{mod}`. "
            f"Your task is to **EXTRACT** (not create) structured API Reference documentation.\n"
            f"**LANGUAGE (中英混杂 · Chinese-English Mixed):**\n"
            f"- **USE CHINESE (中文) for**: architecture logic explanations, feature descriptions, "
            f"background introductions, module relationship summaries, table headers (参数/类型/描述/返回值), section headings.\n"
            f"- **KEEP ENGLISH for**: function/class/variable/method names, file names, paths, "
            f"API endpoints, config keys, third-party library/framework names, code identifiers, signatures.\n"
            f"- Code blocks, inline code, and `file:line` references remain unchanged.\n"
            f"- **SECTION HEADINGS (## / ###) MUST be in Chinese**: 快速概览, 类参考, 函数参考, 模块概述, 字段, 构造方法, 方法.\n"
            f"  Do NOT use English headings like Quick Summary, Class Reference, Function Reference, Module Overview, Fields, Constructor, Methods.\n\n"
            f"{ctx}\n\n"
            f"## Extraction Rules (follow exactly — violations are errors)\n"
            f"### General Rules\n"
            f"1. Only write what actually exists in the source code. Do not invent, infer, or guess.\n"
            f"2. Mark uncertain content as `(unknown)`. When in doubt, leave it out.\n"
            f"3. Copy type annotations in full, never truncate. `List[List[CodeChunk]]` must not become `List[List`.\n"
            f"4. NO Mermaid diagrams, flowcharts, or graphviz. Use plain-text lists for dependencies.\n"
            f"5. Every table row MUST have the same number of columns as its header. Count after writing each table.\n"
            f"6. Use `file:line` format for source locations.\n"
            f"7. If the source shows clear, typical usage patterns, show a `**Typical Usage**:` + Python code block (1-2 lines).\n"
            f"8. If the source has explicit `raise` statements, document them with `**Raises**: ExceptionType — reason`.\n\n"
            f"### For each class (including @dataclass)\n"
            f"1. Use `### ClassName` heading with `**Source**: file:line` below.\n"
            f"2. Write a one-line description with `> **Summary**:`.\n"
            f"3. Mark `**Type**:` (class / dataclass / enum).\n"
            f"4. If the source shows inheritance, mark `**Inheritance**: ClassName → BaseClass`.\n"
            f"5. For @dataclass: use `#### 字段` subheading + table (名称 | 类型 | 默认值 | 描述).\n"
            f"   **NEVER invent get_xxx() methods for dataclass fields** — Python dataclasses do NOT auto-generate them.\n"
            f"6. For regular classes: use `#### 构造方法` subheading + parameter table.\n"
            f"7. Use `#### 方法` subheading + table (方法 | 返回值 | 描述).\n"
            f"   Only list methods explicitly defined with `def` in the source — no inherited or auto-generated methods.\n"
            f"8. For methods with complex logic worth expanding: use `##### method_name` + parameter table + Returns.\n\n"
            f"### For each top-level function\n"
            f"1. Use `### function_name` heading with `**Source**: file:line` below.\n"
            f"2. Write a one-line description with `> **Summary**:`.\n"
            f"3. Show the full signature in a code block: `def function_name(param: Type, ...) -> ReturnType`.\n"
            f"4. List parameters in a table (参数 | 类型 | 描述).\n"
            f"5. Mark **Returns**: `ReturnType` — description.\n\n"
            f"### Module Structure Requirements\n"
            f"- First: `## 快速概览` table listing all symbols (符号 | 类型 | 概述).\n"
            f"- Second: `## 模块概述` section with 2-3 substantive sentences (in Chinese) that clearly answer:\n"
            f"  * **角色定位**: What role does this module play? (e.g., \"本模块是项目的 CLI 入口层，负责…\"、\"本模块是核心推理引擎，处于架构的中间层…\")\n"
            f"  * **职责边界**: What does it own vs delegate? What capability does it expose to other modules?\n"
            f"  * **协作关系**: Who calls it (upstream)? What does it depend on (downstream)? Use specific module names.\n"
            f"  * Use active, role-oriented language: \"负责…\" \"提供…\" \"作为…层…\" \"被 X 模块调用…\"\n"
            f"  * This section MUST contain real explanatory content — do NOT write only package/source metadata\n"
            f"    like 'Package: X | Source: Y (N lines)'. Write actual prose about the module's role.\n"
            f"- If the module has classes: `## 类参考`, all classes with `###` headings.\n"
            f"- If the module has top-level functions: `## 函数参考`, all functions with `###` headings.\n"
            f"- Separate each symbol with `---`.\n"
            f"- Mark inheritance relationships in the Inheritance field.\n"
            f"- For related symbols, add `**See Also**: ...` cross-references on the last line.\n\n"
            f"### Typical Usage\n"
            f"- If the source shows clear, typical usage patterns, place a `**Typical Usage**:` + Python code block after Summary.\n"
            f"- Examples MUST be based on real usage patterns from the source — never fabricate.\n"
            f"- Only give 1-2 core examples, keep them short.\n"
            f"- If usage is not obvious from the source snippets, omit Typical Usage.\n\n"
            f"### Raises\n"
            f"- If the source has explicit `raise` statements, note `**Raises**: ExceptionType — trigger condition` in the method details.\n"
            f"- NEVER invent Raises entries for methods that don't throw exceptions.\n"
            f"- If a method may raise multiple exceptions, put each on its own line."
        )
        res = session.run("architecture", task, max_tokens=1200, temperature=0.2)
        out.modules[mod] = res.text.strip()
        progress(f"  [map] 模块: {mod}  (cached_tokens={res.cached_tokens})")

    # --- reduce: synthesize Architecture overview ---
    digest_lines = []
    for m, s in out.modules.items():
        # Limit each module summary to avoid exceeding token budget
        truncated = "\n".join(s.splitlines()[:30])
        digest_lines.append(f"## Module: {m}\n{truncated}\n")
    digest = "\n".join(digest_lines)
    if len(digest) > MAX_REDUCE_DIGEST_CHARS:
        digest = digest[:MAX_REDUCE_DIGEST_CHARS] + "\n\n[模块摘要已按上下文预算截断]"
    task = (
        f"Below are the API Reference document summaries for each module in this repository.\n"
        f"**LANGUAGE (中英混杂 · Chinese-English Mixed): Use Chinese for descriptions/explanations, keep English for all code identifiers.**\n\n"
        f"**IMPORTANT: ALL section headings (## / ### level) MUST be in Chinese.**\n\n"
        f"{digest}\n\n"
        f"Produce the **API Reference Overview** for this repository, following this structure:\n\n"
        f"## 1. 项目概述\n"
        f"- One-line project description, tech stack, overall scale (file count / symbol count) — in Chinese.\n"
        f"- Additionally, describe the project's layered architecture in 2-3 sentences:\n"
        f"  which modules form the entry/CLI layer, which form the core business logic layer,\n"
        f"  and which form the infrastructure/shared layer.\n\n"
        f"## 2. 数据流与典型调用链\n"
        f"**This is the most important section for understanding how the project works.**\n"
        f"Describe 2-4 typical end-to-end workflows in Chinese. Use real function/method names:\n\n"
        f"### 调用链 1: [workflow name]\n"
        f"- **触发**: [what starts this flow]\n"
        f"- **流程**: `entry.func()` → `core.method()` → `infra.util()`\n"
        f"- **数据流**: [what data passes between steps]\n"
        f"- **产出**: [what the user gets back]\n\n"
        f"## 3. 模块索引\n"
        f"| 模块 | 描述 | 核心类 | 核心函数 |\n"
        f"|--------|-------------|-------------|---------------|\n"
        f"- Module descriptions MUST reflect the module's ROLE, not just list its first class.\n"
        f"- Example of GOOD: \"CLI 入口模块，提供命令行接口用于索引、文档生成和问答\"\n"
        f"- Example of BAD: \"代码片段对象\" (this describes a class, not the module)\n\n"
        f"## 4. 核心 API 速览\n"
        f"Select the 5-10 most important public classes/functions:\n"
        f"| 符号 | 类型 | 模块 | 签名 | 描述 |\n"
        f"|--------|------|--------|-----------|-------------|\n\n"
        f"## 5. 模块依赖关系\n"
        f"**NO Mermaid/flowchart/graphviz. Plain-text structured list only.**\n"
        f"- For EACH module, list what it depends on AND what depends on it.\n"
        f"- Use this format: `module_a` → `module_b, module_c` (原因: 调用其 XXX 功能)\n\n"
        f"## Output Requirements\n"
        f"- Use structured Markdown tables. Reference symbols with `ModuleName (file:line)` format.\n"
        f"- Descriptions, summaries, and explanations should be in Chinese. Code identifiers, signatures, and file paths must remain in original English."
    )
    res = session.run("architecture", task, max_tokens=3000, temperature=0.4)
    out.architecture = res.text.strip()
    progress(f"  [reduce] API Reference 总览完成  (cached_tokens={res.cached_tokens})")
    return out
