"""把 map-reduce 摘要渲染成 MkDocs 文档站。

产出:
  docs/<repo>/index.md          # 架构总览 + 规模
  docs/<repo>/modules/<m>.md    # 各模块摘要
  docs/<repo>/mkdocs.yml        # 直接 `mkdocs serve -f <此文件>` 即可预览
"""

from __future__ import annotations

import re
from pathlib import Path

from docgen.summarize import DocResult

DOCS_BASE = "docs"


def _safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", name)


def render(doc: DocResult, base: str = DOCS_BASE, api_pages: dict | None = None) -> Path:
    root = Path(base) / doc.name
    (root / "modules").mkdir(parents=True, exist_ok=True)

    # index.md
    langs = ", ".join(f"{k}({v})" for k, v in doc.meta.get("languages", {}).items())
    index = [
        f"# {doc.name}",
        "",
        f"> 自动生成的仓库文档 · {doc.meta.get('num_files', '?')} 文件 / "
        f"{doc.meta.get('num_symbols', '?')} 符号 · 技术栈:{langs}",
        "",
        "## 架构总览",
        "",
        doc.architecture or "(未生成)",
    ]
    (root / "index.md").write_text("\n".join(index), "utf-8")

    # 各模块
    nav_modules = []
    for mod, summary in doc.modules.items():
        fn = _safe(mod) + ".md"
        skill = doc.module_skills.get(mod, "architecture")
        header = f"# {mod}\n\n> 🔎 分析视角:`{skill}` skill\n\n{summary}\n"
        (root / "modules" / fn).write_text(header, "utf-8")
        nav_modules.append((mod, f"modules/{fn}"))

    # API 参考页(可选)
    nav_api = []
    if api_pages:
        (root / "api").mkdir(parents=True, exist_ok=True)
        for mod, md in api_pages.items():
            fn = _safe(mod) + ".md"
            (root / "api" / fn).write_text(md, "utf-8")
            nav_api.append((mod, f"api/{fn}"))

    # mkdocs.yml
    nav_lines = ["nav:", "  - 架构总览: index.md", "  - 模块:"]
    for mod, path in nav_modules:
        nav_lines.append(f"      - {mod}: {path}")
    if nav_api:
        nav_lines.append("  - API 参考:")
        for mod, path in nav_api:
            nav_lines.append(f"      - {mod}: {path}")
    mkdocs_yml = [
        f"site_name: {doc.name} 代码文档",
        "theme:",
        "  name: material",
        "docs_dir: .",
        "\n".join(nav_lines),
    ]
    (root / "mkdocs.yml").write_text("\n".join(mkdocs_yml) + "\n", "utf-8")
    return root
