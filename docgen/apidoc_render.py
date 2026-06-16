"""把 API 抽取结果渲染成 Markdown 页(每模块一页),含「内部调用」小节 + 链接。"""

from __future__ import annotations

import re

from docgen.apidoc import APIEntry

_EXT_LANG = {
    ".py": "python", ".js": "javascript", ".jsx": "javascript", ".ts": "typescript",
    ".tsx": "tsx", ".go": "go", ".rs": "rust", ".java": "java", ".c": "c",
    ".cpp": "cpp", ".rb": "ruby", ".php": "php", ".cs": "csharp",
}


def _safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", name)


def _module_of(path: str) -> str:
    parts = path.split("/")
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]


def _lang(path: str) -> str:
    for ext, lang in _EXT_LANG.items():
        if path.endswith(ext):
            return lang
    return ""


def _anchor(sym) -> str:
    return f"sym-{_safe(sym.file)}-{sym.start_line}"


def _source_page_name(path: str) -> str:
    return _safe(path) + ".md"


def _source_link(sym) -> str:
    return f"../source/{_source_page_name(sym.file)}#L{sym.start_line}"


def _purpose(entry: APIEntry) -> str:
    """取描述的第一行作为一句话用途。"""
    if not entry.body_md:
        return ""
    for line in entry.body_md.splitlines():
        t = line.strip().lstrip("#").strip()
        if t:
            return t[:80]
    return ""


def _callees_md(entry: APIEntry, by_key: dict[str, APIEntry]) -> str:
    rows = []
    for ck in entry.callee_keys:
        ce = by_key.get(ck)
        if ce is None:  # 被调在测试目录或未纳入,跳过
            continue
        sym = ce.symbol
        link = f"{_safe(_module_of(sym.file))}.md#{_anchor(sym)}"
        purpose = _purpose(ce)
        rows.append(f"- [`{sym.qualified_name()}`]({link})" + (f" — {purpose}" if purpose else ""))
    if not rows:
        return ""
    return "**内部调用(库内):**\n" + "\n".join(rows)


def _symbol_level(kind: str) -> str:
    # Keep symbols below toc_depth=2 so large method lists do not flood sidebars.
    return "####"


def _normalize_body_md(md: str) -> str:
    if not md:
        return ""
    text = md.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"^(\*\*(?:Parameters|Returns|Raises)\*\*)\s{2,}$", r"\1", text, flags=re.M)
    return text


def render_module_md(module: str, entries: list[APIEntry], by_key: dict[str, APIEntry]) -> str:
    out = [
        f"# API 参考: `{module}`",
        "",
        "!!! note \"阅读提示\"",
        "    本页是 Detailed API：保留签名、参数、返回值、内部调用和源码定位。左侧导航只列模块页面；页面内文件目录保留到文件级，避免方法列表挤满导航。",
        "",
    ]
    pending: list[APIEntry] = []
    current_file = None
    for e in entries:
        if e.doc_source == "none" and not e.body_md:
            pending.append(e)
            continue

        s = e.symbol
        if s.file != current_file:
            out.append(f"\n## `{s.file}`\n")
            current_file = s.file

        kind_label = {"class": "class", "method": "method", "function": "func"}.get(s.kind, s.kind)
        heading = _symbol_level(s.kind)
        out.append(f'<a id="{_anchor(s)}"></a>')
        out.append(f'{heading} `{s.qualified_name()}` <span class="api-kind">{kind_label}</span>')
        out.append(
            f'<div class="api-symbol-meta" markdown="1">'
            f'**Source**: [`{s.location()}`]({_source_link(s)})'
            f' &nbsp;|&nbsp; **Kind**: `{kind_label}`'
            f'</div>'
        )
        if s.decorators:
            out.append("装饰器: " + " ".join(f"`{d}`" for d in s.decorators))
        out.append(f"```{_lang(s.file)}\n{s.signature}\n```")
        body = _normalize_body_md(e.body_md)
        if body:
            out.append("\n" + body)
        callees = _callees_md(e, by_key)
        if callees:
            out.append("\n" + callees)
        out.append("\n---")

    if pending:
        out.append("\n## 待补全文档\n")
        out.append(
            "> 这些符号已从源码中抽取出签名，但本轮 LLM 预算尚未覆盖。"
            "使用 `python -m cli doc <name> --api --complete` 可续跑补齐。\n"
        )
        out.append('??? note "待生成符号清单"')
        out.append("")
        out.append("    | 符号 | 类型 | 来源 | 签名 |")
        out.append("    |---|---|---|---|")
        for e in pending:
            s = e.symbol
            kind_label = {"class": "class", "method": "method", "function": "func"}.get(s.kind, s.kind)
            sig = s.signature.replace("|", "\\|").replace("`", "")
            out.append(f"    | `{s.qualified_name()}` | {kind_label} | `{s.location()}` | `{sig}` |")

    return "\n".join(out)


def render_all(by_module: dict[str, list[APIEntry]], by_key: dict[str, APIEntry]) -> dict[str, str]:
    return {mod: render_module_md(mod, entries, by_key) for mod, entries in by_module.items() if entries}
