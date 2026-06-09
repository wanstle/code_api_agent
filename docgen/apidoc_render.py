"""把 API 抽取结果渲染成 Markdown 页(每模块一页),含「内部调用」小节 + 链接。"""

from __future__ import annotations

import re

from docgen.apidoc import APIEntry

_EXT_LANG = {
    ".py": "python", ".js": "javascript", ".jsx": "javascript", ".ts": "typescript",
    ".tsx": "tsx", ".go": "go", ".rs": "rust", ".java": "java", ".c": "c",
    ".cpp": "cpp", ".rb": "ruby", ".php": "php", ".cs": "csharp",
}
_SOURCE_LABEL = {"none": "待生成"}   # ai 来源不再加标注(现在描述均为 AI 生成)


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


def render_module_md(module: str, entries: list[APIEntry], by_key: dict[str, APIEntry]) -> str:
    out = [f"# API 参考:`{module}`", ""]
    current_file = None
    for e in entries:
        s = e.symbol
        if s.file != current_file:
            out.append(f"\n## `{s.file}`\n")
            current_file = s.file

        kind_label = {"class": "class", "method": "method", "function": "func"}.get(s.kind, s.kind)
        out.append(f'<a id="{_anchor(s)}"></a>')
        out.append(f"### `{s.qualified_name()}` · {kind_label}")
        if s.decorators:
            out.append("装饰器: " + " ".join(f"`{d}`" for d in s.decorators))
        out.append(f"```{_lang(s.file)}\n{s.signature}\n```")
        if e.body_md:
            out.append("\n" + e.body_md)
        callees = _callees_md(e, by_key)
        if callees:
            out.append("\n" + callees)
        label = _SOURCE_LABEL.get(e.doc_source)
        out.append(f"\n*来源: `{s.location()}`*" if not label
                   else f"\n*来源: `{s.location()}` · {label}*")
        out.append("\n---")
    return "\n".join(out)


def render_all(by_module: dict[str, list[APIEntry]], by_key: dict[str, APIEntry]) -> dict[str, str]:
    return {mod: render_module_md(mod, entries, by_key) for mod, entries in by_module.items() if entries}
