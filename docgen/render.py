"""Render map-reduce summaries into Android API Reference style MkDocs site.

Features:
  - Material theme + hierarchical sidebar navigation
  - Intra-page TOC with anchor links
  - Post-processing: table alignment, separator dedup, blank-line normalization
  - Custom CSS for professional API Reference appearance
  - Section reorganization for consistent heading hierarchy
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name
from pygments.util import ClassNotFound

from docgen.summarize import DocResult

DOCS_BASE = "docs"


def _safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", name)


def _module_label(path: str) -> str:
    parts = path.replace("\\", "/").split("/")
    return "/".join(parts)


def _clean_nav_label(path: str) -> str:
    """Convert file paths to clean nav labels. Remove .py/.md extensions."""
    parts = path.replace("\\", "/").split("/")
    # Remove file extensions from the last part
    if parts:
        last = parts[-1]
        for ext in [".py", ".md", ".sh"]:
            if last.endswith(ext):
                last = last[: -len(ext)]
                break
        parts[-1] = last
    return "/".join(parts)


def _source_page_name(path: str) -> str:
    return _safe(path) + ".md"


def _source_link(path: str, line: int | None = None) -> str:
    anchor = f"#L{line}" if line else ""
    # API pages live under docs/api/, while source pages live under docs/source/.
    # Use a relative Markdown link so MkDocs can validate it during build.
    return f"../source/{_source_page_name(path)}{anchor}"


def _normalize_source_links(md: str) -> str:
    """Rewrite stale absolute source links that may come from cached API docs."""
    return re.sub(r"\(/source/([^\s)]+?)\.md/#L(\d+)\)", r"(../source/\1.md#L\2)", md)


def _lang_for_source(path: str, default: str = "") -> str:
    ext = Path(path).suffix.lower()
    return {
        ".py": "python", ".js": "javascript", ".jsx": "javascript",
        ".mjs": "javascript", ".cjs": "javascript", ".ts": "typescript",
        ".tsx": "tsx", ".java": "java", ".go": "go", ".rs": "rust",
        ".c": "c", ".h": "cpp", ".cpp": "cpp", ".cc": "cpp",
        ".cxx": "cpp", ".hpp": "cpp", ".hh": "cpp", ".cs": "csharp",
        ".rb": "ruby", ".php": "php", ".kt": "kotlin", ".swift": "swift",
        ".scala": "scala",
    }.get(ext, default)


def _highlight_source_lines(text: str, lang: str) -> list[str]:
    if not text:
        return [""]
    try:
        lexer = get_lexer_by_name(lang) if lang else TextLexer()
    except ClassNotFound:
        lexer = TextLexer()
    formatter = HtmlFormatter(nowrap=True)
    highlighted = highlight(text, lexer, formatter).rstrip("\n")
    return highlighted.splitlines() or [""]


def _render_source_files(doc: DocResult, content_dir: Path) -> None:
    """Render read-only source pages used only as deep-link targets."""
    source_dir = content_dir / "source"
    if source_dir.exists():
        shutil.rmtree(source_dir)
    source_dir.mkdir(parents=True, exist_ok=True)
    repo_root = Path(doc.meta.get("root", ""))
    files = sorted(doc.meta.get("files", []), key=lambda f: f.get("path", ""))

    # Source pages are not a browsable documentation section. They exist so API
    # references can jump to exact source lines, and are excluded from search.

    for f in files:
        rel = f.get("path", "")
        if not rel:
            continue
        abs_path = repo_root / rel
        try:
            lines = abs_path.read_text("utf-8", "replace").splitlines()
        except OSError as e:
            body = f"_无法读取源码: {e}_"
        else:
            lang = _lang_for_source(rel, f.get("lang", ""))
            highlighted_lines = _highlight_source_lines("\n".join(lines), lang)
            code_lines = []
            for i, highlighted_line in enumerate(highlighted_lines, 1):
                code_lines.append(
                    f'<span id="L{i}" class="source-line"><span class="source-line-no">{i}</span>'
                    f'{highlighted_line}</span>'
                )
            body = (
                f'<pre class="source-code highlight" markdown="0"><code class="language-{lang}">'
                + "\n".join(code_lines)
                + "</code></pre>"
            )
        page = [
            "---",
            "search:",
            "  exclude: true",
            "---",
            "",
            f"# `{rel}`",
            "",
            f'<span class="md-source-file"><a href="../architecture.md">Architecture</a></span>',
            "",
            body,
            "",
        ]
        (source_dir / _source_page_name(rel)).write_text("\n".join(page), "utf-8")

# ---------------------------------------------------------------------------
# Markdown post-processing — fixes LLM formatting sloppiness
# ---------------------------------------------------------------------------

def _normalize_markdown(text: str) -> str:
    """Clean up LLM-generated Markdown: align tables, dedup separators,
    collapse excessive blank lines, fix heading spacing, fix inline table labels,
    detect truncated types."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Fix "- **Label**: | col1 | col2 |" — split label from table start
        m = re.match(r"^(\s*-\s*\*\*[^*]+\*\*:\s*)\|\s*(.+)$", line)
        if m:
            out.append(m.group(1).strip())
            line = "| " + m.group(2)

        # Also fix "**Label**: | col1 |" (without the leading dash)
        m = re.match(r"^(\s*\*\*[^*]+\*\*:\s*)\|\s*(.+)$", line)
        if m and not line.strip().startswith("-"):
            out.append(m.group(1).strip())
            line = "| " + m.group(2)

        # Detect table block: line starts with |
        if line.strip().startswith("|"):
            table_block, i = _collect_table_block(lines, i, line)
            aligned = _align_table(table_block)
            out.append(_markdown_table_to_html(aligned))
            continue

        # Detect and fix truncated types like "List[List" or "Dict[str,"
        line = _fix_truncated_types(line)

        # Skip duplicate --- separators
        if line.strip().startswith("---") and line.strip().replace("-", "").strip() == "":
            prev_sep = False
            for j in range(len(out) - 1, -1, -1):
                if out[j].strip():
                    prev_sep = out[j].strip().startswith("---") and out[j].strip().replace("-", "").strip() == ""
                    break
            if prev_sep:
                i += 1
                continue

        out.append(line)
        i += 1

    # Collapse >=3 consecutive blank lines → 2
    collapsed: list[str] = []
    blank_run = 0
    for line in out:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                collapsed.append(line)
        else:
            blank_run = 0
            collapsed.append(line)

    # Ensure exactly one blank line before ##/###/#### headings and --- separators.
    # The --- case is critical: without a blank line before it, CommonMark / Python-Markdown
    # interprets the preceding text as a setext h2 heading (e.g. "**Returns**: None" becomes <h2>).
    final: list[str] = []
    for j, line in enumerate(collapsed):
        stripped = line.strip()
        is_heading = re.match(r"^(#{1,4})\s", stripped)
        is_hr = bool(stripped.startswith("---") and stripped.replace("-", "").strip() == "")
        if is_heading or is_hr:
            while final and final[-1].strip() == "":
                final.pop()
            if final and final[-1].strip():
                final.append("")
        final.append(line)

    return "\n".join(final)


def _fix_truncated_types(line: str) -> str:
    """Detect and annotate obviously truncated type expressions."""
    # Pattern: `List[List` without closing brackets
    # Match generic types that are cut off
    truncated_patterns = [
        (r"`List\[List$", "`List[List[...]]` *(truncated)*"),
        (r"`List\[Dict$", "`List[Dict[...]]` *(truncated)*"),
        (r"`Dict\[str,\s*$", "`Dict[str, ...]` *(truncated)*"),
        (r"`Optional\[$", "`Optional[...]` *(truncated)*"),
        (r"`Union\[$", "`Union[...]` *(truncated)*"),
    ]
    for pattern, replacement in truncated_patterns:
        if re.search(pattern, line):
            line = re.sub(pattern, replacement, line)
    return line


def _collect_table_block(lines: list[str], start: int, first_line: str = "") -> tuple[list[str], int]:
    """Collect consecutive table lines."""
    block = [first_line.strip()] if first_line.strip() else []
    # When first_line is provided, we've already consumed the line at `start`
    i = start + 1 if first_line.strip() else start
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("|"):
            block.append(stripped)
        elif re.match(r"^\|?[\s\-:]+\|[\s\-:|]+$", stripped):
            block.append(stripped)
        else:
            break
        i += 1
    return block, i


def _align_table(block: list[str]) -> list[str]:
    """Parse Markdown table, fix column count mismatches, align columns.

    Strategy:
    1. Detect expected column count from the separator row (the one with ---).
    2. For data rows that have too many | (because of inline code/dquotes
       containing |), merge the excess cells back into the last valid column.
    3. Rebuild with aligned widths.
    """
    if not block:
        return block

    # ── phase 1: split each line into raw cells ──────────────────────────
    def _raw_split(line: str) -> list[str]:
        """Split on | but protect content inside backtick spans."""
        inner = line.strip().strip("|")
        cols: list[str] = []
        current: list[str] = []
        in_bt = False
        for ch in inner:
            if ch == "`":
                in_bt = not in_bt
                current.append(ch)
            elif ch == "|" and not in_bt:
                cols.append("".join(current).strip())
                current = []
            else:
                current.append(ch)
        cols.append("".join(current).strip())
        return cols

    raw_rows = [_raw_split(line) for line in block]
    if not raw_rows:
        return block

    # ── phase 2: detect expected column count from separator ─────────────
    def _is_sep_row(row: list[str]) -> bool:
        return all(
            re.match(r"^[\-:\s]+$", c) or c == ""
            for c in row
        )

    expected_cols = max(len(r) for r in raw_rows)  # fallback
    for row in raw_rows:
        if _is_sep_row(row):
            expected_cols = sum(1 for c in row if c.strip() != "")
            break

    # ── phase 3: normalize every row to expected_cols ────────────────────
    def _normalize_row(row: list[str], target: int, is_sep: bool) -> list[str]:
        """Merge overflow cells back into the last meaningful column."""
        non_empty = [c for c in row if c.strip() != ""]
        if is_sep:
            # Separator: keep only dashes entries, pad/trim to target
            result = [c for c in row if c.strip() != ""]
            while len(result) < target:
                result.append("---")
            return result[:target]

        if len(row) <= target:
            while len(row) < target:
                row.append("")
            return row

        # Too many columns — merge extras into the last non-empty column.
        # Join with \| so the Markdown parser treats the merged result as
        # one cell and renders literal | characters.
        keep = row[:target - 1]
        merged = " \\| ".join(row[target - 1:])
        keep.append(merged)
        return keep

    normalized = []
    for row in raw_rows:
        is_sep = _is_sep_row(row)
        normalized.append(_normalize_row(row, expected_cols, is_sep))

    rows = normalized
    ncols = expected_cols

    # ── phase 4: compute widths ──────────────────────────────────────────
    widths = [0] * ncols
    for row in rows:
        for ci in range(min(len(row), ncols)):
            widths[ci] = max(widths[ci], len(row[ci]))
    widths = [max(w, 3) for w in widths]

    # ── phase 5: find separator row index ────────────────────────────────
    sep_idx = None
    for ri, row in enumerate(rows):
        if _is_sep_row(row):
            sep_idx = ri
            break

    # ── phase 6: rebuild aligned table ───────────────────────────────────
    aligned: list[str] = []
    for ri, row in enumerate(rows):
        cells: list[str] = []
        for ci in range(ncols):
            cell = row[ci] if ci < len(row) else ""
            if ri == sep_idx:
                raw = cell.strip()
                if raw.startswith(":") and raw.endswith(":"):
                    cells.append(":" + "-" * max(widths[ci] - 2, 1) + ":")
                elif raw.startswith(":"):
                    cells.append(":" + "-" * max(widths[ci] - 1, 1))
                elif raw.endswith(":"):
                    cells.append("-" * max(widths[ci] - 1, 1) + ":")
                else:
                    cells.append("-" * widths[ci])
            else:
                cells.append(cell.ljust(widths[ci]))
        aligned.append("| " + " | ".join(cells) + " |")

    return aligned


# ---------------------------------------------------------------------------
# Markdown table → styled HTML table conversion
# ---------------------------------------------------------------------------

def _markdown_table_to_html(block: list[str]) -> str:
    """Convert an aligned Markdown table block into a styled HTML table.

    The block should already be aligned by _align_table().  Produces a
    ``<div class="api-table-container">`` wrapping a ``<table>`` with
    ``<thead>`` / ``<tbody>``, code spans wrapped in ``<code>``, and
    cells that contain ``\\|`` un-escaped back to literal ``|``.

    Falls back to raw Markdown when the block can't be parsed.
    """
    if not block:
        return ""

    # ── phase 1: split aligned rows into cells ──────────────────────────
    rows: list[list[str]] = []
    for line in block:
        line = line.strip().strip("|")
        # Protect escaped pipes before splitting
        line = line.replace("\\|", "\x00ESCPIPE\x00")
        cells: list[str] = []
        for c in line.split("|"):
            # Restore escaped pipes then un-escape
            c = c.strip().replace("\x00ESCPIPE\x00", "|")
            cells.append(c)
        rows.append(cells)

    if len(rows) < 2:
        return "\n".join(block)

    # ── phase 2: locate header, separator, data ─────────────────────────
    def _is_sep(cells: list[str]) -> bool:
        return all(re.match(r"^[\-:\s]+$", c) for c in cells)

    sep_idx: int | None = None
    for ri, row in enumerate(rows):
        if _is_sep(row):
            sep_idx = ri
            break

    if sep_idx is None or sep_idx == 0:
        return "\n".join(block)          # no separator → give up

    header_cells = rows[0]
    data_rows = rows[sep_idx + 1 :]
    ncols = len(header_cells)

    # Guess table type from header text
    header_text = " ".join(header_cells).lower()
    has_type_col = any(w in header_text for w in ("type", "类型"))
    has_desc_col = any(w in header_text for w in ("description", "描述", "说明"))
    has_sig_col = any(w in header_text for w in ("method", "signature", "方法", "签名"))
    has_param_col = any(w in header_text for w in ("parameter", "参数"))

    if has_param_col or (has_type_col and has_desc_col):
        table_class = "api-fields-table"
    elif has_sig_col or (len(header_cells) == 2 and not has_type_col):
        table_class = "api-methods-table"
    else:
        table_class = "api-simple-table"

    # ── phase 3: render HTML ────────────────────────────────────────────
    def _render_cell(cell: str, col_idx: int) -> str:
        """Render a single cell, converting `` `code` `` → ``<code>``."""
        # Process backtick-wrapped spans
        result: list[str] = []
        in_bt = False
        buf: list[str] = []
        i = 0
        while i < len(cell):
            ch = cell[i]
            if ch == "`":
                if in_bt:
                    # close code span
                    if buf:
                        result.append(f"<code>{''.join(buf)}</code>")
                        buf = []
                    in_bt = False
                else:
                    # flush text before code
                    if buf:
                        result.append("".join(buf))
                        buf = []
                    in_bt = True
            else:
                buf.append(ch)
            i += 1
        if buf:
            result.append("".join(buf))

        inner = "".join(result)
        if not inner.strip():
            inner = "&nbsp;"
        return inner

    html: list[str] = []
    html.append(f'<div class="api-table-container {table_class}" markdown="0">')
    html.append("<table>")

    # thead
    html.append("<thead>")
    html.append("<tr>")
    for ci, cell in enumerate(header_cells):
        clean = cell.replace("`", "")
        html.append(f"<th>{clean}</th>")
    html.append("</tr>")
    html.append("</thead>")

    # tbody
    html.append("<tbody>")
    for row in data_rows:
        html.append("<tr>")
        for ci in range(ncols):
            raw = row[ci] if ci < len(row) else ""
            inner = _render_cell(raw, ci)
            html.append(f"<td>{inner}</td>")
        html.append("</tr>")
    html.append("</tbody>")

    html.append("</table>")
    html.append("</div>")
    return "\n".join(html)


# ---------------------------------------------------------------------------
# Heading localization — force Chinese section headings (LLM stubbornness fallback)
# ---------------------------------------------------------------------------

# Map of English headings → Chinese headings for consistent localization.
# Applied as a post-processing step because smaller LLMs (e.g., Qwen2.5-Coder-7B)
# often revert to English section headings despite explicit Chinese instructions.
_HEADING_LOCALIZATION_MAP: list[tuple[str, str]] = [
    # H2 module-level headings
    ("## Quick Summary", "## 快速概览"),
    ("## Class Reference", "## 类参考"),
    ("## Function Reference", "## 函数参考"),
    ("## Module Overview", "## 模块概述"),
    # H4 sub-headings
    ("#### Fields", "#### 字段"),
    ("#### Constructor", "#### 构造方法"),
    ("#### Methods", "#### 方法"),
    # Bold inline labels (standalone on a line)
    ("**Fields**", "**字段**"),
    ("**Methods**", "**方法**"),
    ("**Summary**", "**概述**"),
]


def _localize_headings(text: str) -> str:
    """Replace stubborn English section headings with Chinese equivalents."""
    for en, cn in _HEADING_LOCALIZATION_MAP:
        # Only replace when the English text is at the start of a line (heading context)
        text = text.replace("\n" + en + "\n", "\n" + cn + "\n")
        # Also handle first-line case (text starts with heading)
        if text.startswith(en + "\n"):
            text = cn + text[len(en):]
    return text


# ---------------------------------------------------------------------------
# Section reorganization — enforce consistent heading hierarchy
# ---------------------------------------------------------------------------


def _plain_inline(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = text.replace("**", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _strip_markdown_code(text: str) -> str:
    return re.sub(r"`([^`]+)`", r"\1", text or "")


def _split_overview_sentences(lines: list[str]) -> list[str]:
    blob = "\n".join(lines)
    blob = re.sub(r"<div[^>]*>|</div>", "\n", blob)
    blob = re.sub(r"^>\s*", "", blob, flags=re.M)
    blob = re.sub(r"\*\*(角色定位|职责边界|协作关系)\*\*\s*[：:]", r"\n\1：", blob)
    raw_parts = re.split(r"(?<=[。！？])\s+|\n+", blob)
    parts: list[str] = []
    for part in raw_parts:
        item = _plain_inline(part)
        if not item:
            continue
        if re.match(r"^(Package|Source|Module)\s*[:：]", item, re.I):
            continue
        if len(item) < 8:
            continue
        parts.append(item)
    return parts


def _overview_bullets(lines: list[str]) -> list[str]:
    parts = _split_overview_sentences(lines)
    role = next((p for p in parts if "角色定位" in p), "")
    boundary = next((p for p in parts if "职责边界" in p), "")
    collaboration = next((p for p in parts if "协作关系" in p or "依赖" in p or "被" in p), "")
    if not role and len(parts) == 1:
        role = parts[0]

    used: set[str] = set()
    bullets: list[tuple[str, str]] = []
    for label, val in (("角色定位", role), ("职责边界", boundary), ("协作关系", collaboration)):
        if val:
            val = re.sub(rf"^\s*{label}\s*[：:]\s*", "", val)
            bullets.append((label, val))
            used.add(val)

    for part in parts:
        if len(bullets) >= 3:
            break
        if part in used:
            continue
        label = ("角色定位" if not bullets else "职责边界" if len(bullets) == 1 else "协作关系")
        bullets.append((label, part))
        used.add(part)

    if not bullets:
        return [f"- **角色定位**：本模块 `{_strip_markdown_code('')}` 提供该目录下的代码组织入口。"]
    return [f"- **{label}**：{text}" for label, text in bullets[:3]]


def _extract_symbol_cards(lines: list[str], limit: int = 12) -> list[dict[str, str]]:
    cards: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_code = False

    def flush() -> None:
        nonlocal current
        if current and current.get("name"):
            cards.append(current)
        current = None

    for raw in lines:
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^###\s+`?([^`\n]+?)`?\s*$", line)
        if m:
            flush()
            current = {"name": _strip_markdown_code(m.group(1)).strip(), "kind": "", "summary": "", "source": ""}
            continue
        if current is None:
            continue
        summary = re.match(r"^>\s*\*\*(?:Summary|概述)\*\*\s*[：:]\s*(.+)$", line, re.I)
        if summary:
            current["summary"] = _plain_inline(summary.group(1))
            continue
        source = re.match(r"^\*\*Source\*\*\s*[：:]\s*(.+)$", line, re.I)
        if source:
            current["source"] = _plain_inline(source.group(1))
            continue
        type_m = re.search(r"\*\*(?:Type|类型)\*\*\s*[：:]\s*`?([^`|]+)`?", line, re.I)
        if type_m:
            current["kind"] = _plain_inline(type_m.group(1))
        module_m = re.search(r"\*\*(?:Module|模块)\*\*\s*[：:]\s*`?([^`|]+)`?", line, re.I)
        if module_m and not current.get("source"):
            current["source"] = _plain_inline(module_m.group(1))
        if not current.get("source"):
            ref = re.search(r"([\w./-]+\.py(?::\d+)?)", line)
            if ref:
                current["source"] = ref.group(1)
    flush()

    out: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for card in cards:
        key = (card.get("name", ""), card.get("source", ""))
        if key in seen:
            continue
        seen.add(key)
        out.append(card)
        if len(out) >= limit:
            break
    return out


def _render_symbol_index(cards: list[dict[str, str]], module_path: str) -> list[str]:
    if not cards:
        return ["_未提取到稳定的入口符号；详细符号请查看 Detailed API。_"]
    rows = [
        '<div class="api-table-container api-module-symbols" markdown="0">',
        '<table>',
        '<thead><tr><th>入口</th><th>类型</th><th>职责</th><th>位置</th></tr></thead>',
        '<tbody>',
    ]
    for card in cards:
        name = card.get("name", "")
        kind = card.get("kind", "") or ("class" if name[:1].isupper() else "function")
        summary = card.get("summary", "") or "该入口的详细行为见 Detailed API。"
        source = card.get("source", "") or module_path
        rows.append(
            "<tr>"
            f"<td><code>{name}</code></td>"
            f"<td>{kind}</td>"
            f"<td>{summary}</td>"
            f"<td><code>{source}</code></td>"
            "</tr>"
        )
    rows.extend(['</tbody>', '</table>', '</div>'])
    return rows


def _render_module_guide(text: str, module_path: str) -> str:
    """Render module pages as high-level guides, leaving details to api/ pages."""
    lines = text.splitlines()
    overview: list[str] = []
    symbol_lines: list[str] = []
    meta_lines: list[str] = []
    current = "overview"

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            continue
        meta_m = re.match(r"^(?:>\s*)?\*\*Package\*\*:\s*(.+?)\s*\|\s*\*\*Source\*\*:\s*(.+)$", stripped)
        if meta_m:
            meta_lines.append(
                f'<div class="api-module-meta"><strong>Package</strong>: {meta_m.group(1).strip()}'
                f' &nbsp;|&nbsp; <strong>Source</strong>: {meta_m.group(2).strip()}</div>'
            )
            continue
        if re.match(r"^##\s+(关键入口|快速概览|类参考|函数参考|Class Reference|Function Reference|Quick Summary)", stripped, re.I):
            current = "symbols"
            continue
        if re.match(r"^##\s+(模块概述|Module Overview)", stripped, re.I):
            current = "overview"
            continue
        if current == "overview":
            overview.append(raw)
        else:
            symbol_lines.append(raw)

    cards = _extract_symbol_cards(symbol_lines, limit=14)
    result: list[str] = ["## 模块导览", ""]
    result.extend(meta_lines)
    if meta_lines:
        result.append("")
    result.append('<div class="api-module-overview" markdown="1">')
    result.extend(_overview_bullets(overview))
    result.append('</div>')
    result.append("")
    result.append("## 关键入口")
    result.append("")
    result.extend(_render_symbol_index(cards, module_path))
    result.append("")
    result.append("!!! note \"详细 API\"")
    result.append("    本页只保留模块职责与入口索引；参数、返回值、构造方法和方法表请查看左侧 Detailed API。")
    return "\n".join(result)


def _reorganize_sections(text: str, module_path: str) -> str:
    """Reorganize LLM output into a clean, consistent structure.

    Enforces:
      ## 模块概述
      ## 类参考 (if classes exist)
      ## 函数参考 (if top-level functions exist)

    Intelligently detects section marker headings (e.g. "## 类参考")
    vs content headings (e.g. "### MyClass") and preserves the latter.
    """
    lines = text.splitlines()

    # First pass: classify each line into a section bucket
    sections: dict[str, list[str]] = {
        "quick_summary": [],
        "overview": [],
        "classes": [],
        "functions": [],
        "other": [],
    }
    current_section = "overview"

    # Patterns that indicate a section-level heading (not a symbol heading)
    SECTION_MARKER_PATTERNS = [
        # H2 section markers
        (re.compile(r"^##\s+(quick\s*summary|快速概览|摘要|速览|概览表)", re.I), "quick_summary"),
        (re.compile(r"^##\s+(module\s*overview|模块概述|module:?\s*\S)", re.I), "overview"),
        (re.compile(r"^##\s+(class(?:es)?\s*reference|类参考|类\s*$|classes?\s*$)", re.I), "classes"),
        (re.compile(r"^##\s+(function(?:s)?\s*reference|函数参考|顶层函数|top.?level\s+functions?|functions?\s*$)", re.I), "functions"),
        # H3 section markers (less common but possible)
        (re.compile(r"^###\s+(quick\s*summary|快速概览|摘要|速览|概览表)$", re.I), "quick_summary"),
        (re.compile(r"^###\s+(module\s*overview|模块概述)", re.I), "overview"),
        (re.compile(r"^###\s+(class(?:es)?\s*reference|类参考|类\s*$)$", re.I), "classes"),
        (re.compile(r"^###\s+(function(?:s)?\s*reference|函数参考|顶层函数|top.?level\s+functions?|functions?\s*$)$", re.I), "functions"),
    ]

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check for H1 heading - treat as module title, convert to overview
        h1_match = re.match(r"^#\s+(.+)$", stripped)
        if h1_match:
            title = h1_match.group(1)
            # Check if this is "Module: X" style title — keep as overview info
            if not re.match(r"^(?:module|class|function)(?:\s|:)", title, re.I):
                sections["overview"].append(f"**Module**: `{module_path}`")
            i += 1
            continue

        # Check for H2/H3 section markers
        h_match = re.match(r"^(#{2,3})\s+(.+)$", stripped)
        if h_match:
            heading = h_match.group(2)
            heading_lower = heading.lower().strip().strip("`")

            is_marker = False
            for pattern, target_section in SECTION_MARKER_PATTERNS:
                if pattern.match(stripped):
                    current_section = target_section
                    is_marker = True
                    break

            if is_marker:
                i += 1
                # Skip blank lines right after section marker
                while i < len(lines) and lines[i].strip() == "":
                    i += 1
                continue

            # Not a section marker — classify by naming convention
            # Clean heading: remove backtick-quoted annotations
            clean_heading = re.sub(r"`[^`]*`", "", heading).strip()
            if clean_heading:
                # Class-like: starts with uppercase
                if clean_heading[0].isupper():
                    current_section = "classes"
                # Function-like: starts with lowercase or underscore
                elif clean_heading[0].islower() or clean_heading.startswith("_"):
                    # But don't reclassify if it looks like a method signature (has parens)
                    current_section = "functions"

        sections[current_section].append(line)
        i += 1

    # Build clean output
    result: list[str] = []

    # Quick Summary (if LLM produced one)
    summary_lines = [l for l in sections["quick_summary"] if l.strip()]
    # Filter out empty stubs
    summary_lines = _filter_metadata_lines(summary_lines)
    if summary_lines:
        result.append("## 快速概览")
        result.append("")
        result.extend(summary_lines)
        result.append("")

    # Module Overview
    overview_lines = [l for l in sections["overview"] if l.strip()]
    result.append("## 模块概述")
    result.append("")
    if overview_lines:
        meta_lines: list[str] = []
        content_lines: list[str] = []
        for line in overview_lines:
            # Convert blockquote metadata line to compact styled HTML
            meta_m = re.match(
                r"^>\s*\*\*Package\*\*:\s*(.+?)\s*\|\s*\*\*Source\*\*:\s*(.+)$",
                line,
            )
            if meta_m:
                pkg = meta_m.group(1).strip()
                src = meta_m.group(2).strip()
                meta_lines.append(
                    f'<div class="api-module-meta">'
                    f'<strong>Package</strong>: {pkg}'
                    f' &nbsp;|&nbsp; '
                    f'<strong>Source</strong>: {src}'
                    f'</div>'
                )
            else:
                content_lines.append(line)

        # Emit metadata bar(s) first
        for ml in meta_lines:
            result.append(ml)
            result.append("")

        # Strip all standalone --- separator lines from overview prose
        # (the overview is a prose section — horizontal rules don't belong here)
        content_lines = [
            l for l in content_lines
            if not re.match(r"^-{3,}\s*$", l.strip())
        ]

        # Remove redundant **Module**: ... stubs when real content exists
        real_content = [
            l for l in content_lines
            if not re.match(r"^\s*\*\*Module\*\*:\s*`[^`]+`\s*$", l.strip())
        ]
        if real_content:
            content_lines = real_content

        if content_lines:
            result.append('<div class="api-module-overview" markdown="1">')
            result.extend(content_lines)
            result.append('</div>')
            result.append("")
    else:
        result.append(f"**Module**: `{module_path}`")
    result.append("")

    # Class Reference
    class_lines = [l for l in sections["classes"] if l.strip()]
    # Filter out lines that are just "**Files**:" or "**文件列表**:" with empty content
    class_lines = _filter_metadata_lines(class_lines)
    class_lines = _dedup_heading_sections(class_lines)
    if class_lines:
        result.append("---")
        result.append("")
        result.append("## 类参考")
        result.append("")
        result.extend(class_lines)
        result.append("")

    # Function Reference
    func_lines = [l for l in sections["functions"] if l.strip()]
    func_lines = _filter_metadata_lines(func_lines)
    func_lines = _dedup_heading_sections(func_lines)
    if func_lines:
        result.append("---")
        result.append("")
        result.append("## 函数参考")
        result.append("")
        result.extend(func_lines)
        result.append("")

    # Other sections
    other_lines = [l for l in sections["other"] if l.strip()]
    other_lines = _filter_metadata_lines(other_lines)
    if other_lines:
        result.append("---")
        result.append("")
        result.extend(other_lines)
        result.append("")

    return "\n".join(result)


def _filter_metadata_lines(lines: list[str]) -> list[str]:
    """Remove empty metadata stubs like '**Files**:' with no value."""
    result: list[str] = []
    skip_next = False
    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue
        stripped = line.strip()
        # Skip standalone metadata keys with no value
        m = re.match(r"^\*\*(Files|文件列表|职责|Responsibility|所属文件)\*\*:\s*$", stripped)
        if m:
            # If next line is another metadata key or empty, skip both
            if i + 1 < len(lines):
                next_stripped = lines[i + 1].strip()
                if next_stripped == "" or re.match(r"^\*\*", next_stripped):
                    skip_next = next_stripped == ""
                    continue
        result.append(line)
    return result


def _dedup_heading_sections(lines: list[str]) -> list[str]:
    """Remove duplicate headings within a section while preserving content.

    Uses a content-based approach: if two H3 headings have the exact same text
    within a close range, it's likely a duplicate — preserve the first occurrence.
    """
    seen: set[str] = set()
    result: list[str] = []
    skip_until_next_heading = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r"^(#{2,4})\s+(.+)$", stripped)
        if m:
            heading_key = m.group(2).lower().strip().replace("`", "").strip()
            if heading_key in seen:
                # Duplicate heading — skip this and all content until next heading
                skip_until_next_heading = True
                continue
            seen.add(heading_key)
            skip_until_next_heading = False
            result.append(line)
        elif skip_until_next_heading:
            # Skip content of duplicate section
            continue
        else:
            result.append(line)

    return result


# ---------------------------------------------------------------------------
# Architecture text cleanup
# ---------------------------------------------------------------------------

def _clean_architecture(text: str) -> str:
    """Clean up the architecture/reduce output from LLM.

    - Strip broken Mermaid diagrams and graphviz code blocks
    - Remove repetitive diagram fragments
    - Normalize formatting
    - Fix common LLM artifacts
    """
    # Remove Mermaid code blocks (usually broken/incomplete)
    text = re.sub(
        r"```mermaid\s*\n.*?```",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Remove graphviz/dot code blocks
    text = re.sub(
        r"```(?:dot|graphviz|graph)\s*\n.*?```",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Remove stray unmatched ``` fences
    # (Find orphan ``` that aren't part of a proper pair)
    lines = text.splitlines()
    cleaned: list[str] = []
    in_code_block = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            if in_code_block:
                cleaned.append(line)
            else:
                # Closing fence
                if cleaned and cleaned[-1].strip().startswith("```"):
                    # Proper open/close — keep both
                    cleaned.append(line)
                else:
                    # Orphan closing — skip it
                    pass
            continue
        # Skip overly long diagram-like lines
        if len(stripped) > 300 and any(
            kw in stripped.lower()
            for kw in ["-->", "graph", "flowchart", "subgraph", "digraph"]
        ):
            continue
        # Strip arrow-based diagram fragments like "A --> B[...]"
        if re.match(r"^\s*\w+\s*(-->|-->\||->)\s*", stripped) and len(stripped) > 80:
            continue
        cleaned.append(line)

    # Re-process to remove any remaining code blocks with Mermaid-like content
    result: list[str] = []
    skip_block = False
    for line in cleaned:
        stripped = line.strip()
        if stripped.startswith("```"):
            # Check if the next non-empty line looks like diagram content
            skip_block = False
            result.append(line)
            continue
        if skip_block:
            if stripped.startswith("```"):
                skip_block = False
            continue
        result.append(line)

    # Collapse multiple blank lines
    final: list[str] = []
    blank_count = 0
    for line in result:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                final.append(line)
        else:
            blank_count = 0
            final.append(line)

    return "\n".join(final)


# ---------------------------------------------------------------------------
# Custom CSS generation — Android API Reference style
# ---------------------------------------------------------------------------

EXTRA_CSS = """\
/* ================================================================
   Android API Reference Style — Custom Stylesheet
   ================================================================ */

/* --- Design Tokens --- */
:root {
  --md-primary-fg-color: #1a73e8;
  --md-primary-fg-color--light: #4da3ff;
  --md-primary-fg-color--dark: #1557b0;
  --md-accent-fg-color: #ff6d00;
  --api-public-color: #1b8a3d;
  --api-protected-color: #e37400;
  --api-private-color: #c5221f;
  --api-deprecated-color: #80868b;
  --api-code-bg: #f1f3f4;
  --api-table-stripe: #f8f9fa;
  --api-table-hover: #e8f0fe;
  --api-border-color: #dadce0;
  --api-heading-color: #202124;
  --api-text-color: #3c4043;
  --api-table-header-bg: #1a73e8;
  --api-table-header-text: #ffffff;
}

[data-md-color-scheme="slate"] {
  --api-code-bg: #2d2d2d;
  --api-table-stripe: #1e1e1e;
  --api-table-hover: #253045;
  --api-border-color: #404040;
  --api-heading-color: #e8eaed;
  --api-text-color: #bdc1c6;
  --md-primary-fg-color: #8ab4f8;
  --md-primary-fg-color--light: #aecbfa;
  --md-primary-fg-color--dark: #669df6;
  --api-table-header-bg: #1a3a5c;
  --api-table-header-text: #e8eaed;
}

/* --- Body & General --- */
.md-typeset {
  font-size: 0.75rem;
  line-height: 1.6;
  color: var(--api-text-color);
}

.md-typeset h1 {
  font-size: 1.8rem;
  font-weight: 400;
  color: var(--api-heading-color);
  border-bottom: 1px solid var(--api-border-color);
  padding-bottom: 0.3em;
  margin-bottom: 0.5em;
}

.md-typeset h2 {
  font-size: 1.4rem;
  font-weight: 400;
  color: var(--api-heading-color);
  border-bottom: 1px solid var(--api-border-color);
  padding-bottom: 0.2em;
  margin-top: 1.5em;
}

.md-typeset h3 {
  font-size: 1.15rem;
  font-weight: 500;
  color: var(--api-heading-color);
  margin-top: 1.2em;
  padding: 0.3em 0;
}

.md-typeset h4 {
  font-size: 1rem;
  font-weight: 500;
  color: var(--api-text-color);
}

/* --- Module metadata bar --- */
.api-module-meta {
  font-size: 0.65rem;
  color: #80868b;
  background: var(--api-table-stripe);
  border-left: 3px solid var(--api-border-color);
  border-radius: 0 4px 4px 0;
  padding: 5px 12px;
  margin: 0 0 8px 0;
  line-height: 1.4;
}

.api-module-meta strong {
  color: #5b5b5b;
  font-weight: 600;
}

[data-md-color-scheme="slate"] .api-module-meta {
  color: #9aa0a6;
  background: #1e1e1e;
}

[data-md-color-scheme="slate"] .api-module-meta strong {
  color: #bdc1c6;
}

/* --- Detailed API symbols --- */
.api-kind {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 600;
  color: var(--md-default-fg-color--light);
  background: var(--api-table-stripe);
  border: 1px solid var(--api-border-color);
  border-radius: 4px;
  padding: 0.05rem 0.35rem;
  vertical-align: middle;
}

.api-symbol-meta {
  font-size: 0.68rem;
  color: var(--md-default-fg-color--light);
  margin: -0.2rem 0 0.45rem 0;
}

.api-symbol-meta p {
  margin: 0;
}

.md-typeset h4 code {
  white-space: normal;
  word-break: break-word;
}

/* --- Module guide symbol index --- */
.api-module-symbols table {
  table-layout: fixed;
  width: 100%;
}

.api-module-symbols th:nth-child(1),
.api-module-symbols td:nth-child(1) { width: 22%; }
.api-module-symbols th:nth-child(2),
.api-module-symbols td:nth-child(2) { width: 12%; }
.api-module-symbols th:nth-child(3),
.api-module-symbols td:nth-child(3) { width: 46%; }
.api-module-symbols th:nth-child(4),
.api-module-symbols td:nth-child(4) { width: 20%; }

.api-module-symbols td {
  vertical-align: top;
  word-break: break-word;
}

.api-module-symbols code {
  white-space: normal;
  word-break: break-word;
}

/* --- Module overview prose --- */
.api-module-overview {
  font-size: 0.7rem;
  line-height: 1.55;
  color: #5b5b5b;
  margin: 4px 0 12px 0;
}

.api-module-overview p {
  margin: 0.3em 0;
}

.api-module-overview h3 {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--api-heading-color);
  margin-top: 0.6em;
  margin-bottom: 0.2em;
  padding: 0;
}

.api-module-overview h4 {
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--api-heading-color);
}

.api-module-overview ul,
.api-module-overview ol {
  font-size: 0.7rem;
  margin: 0.3em 0;
  padding-left: 1.5em;
}

.api-module-overview li {
  margin: 0.15em 0;
}

.api-module-overview code {
  font-size: 0.72rem;
}

.api-module-overview strong {
  color: var(--api-heading-color);
  font-weight: 600;
}

[data-md-color-scheme="slate"] .api-module-overview {
  color: #9aa0a6;
}

[data-md-color-scheme="slate"] .api-module-overview strong {
  color: #e8eaed;
}

/* --- Compact blockquotes --- */
.md-typeset blockquote {
  font-size: 0.7rem;
  color: #80868b;
  border-left: 2px solid var(--api-border-color);
  padding: 4px 12px;
  margin: 4px 0 8px 0;
}

/* ================================================================
   API Table Containers — Android Reference-style polished tables
   ================================================================ */

.api-table-container {
  margin: 16px 0 24px 0;
  overflow-x: auto;
}

.api-table-container table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border: 1px solid var(--api-border-color);
  border-radius: 8px;
  overflow: hidden;
  font-size: 0.75rem;
  line-height: 1.5;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
}

/* --- Header --- */
.api-table-container thead th {
  background: var(--api-table-header-bg);
  color: var(--api-table-header-text);
  font-weight: 500;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  padding: 10px 16px;
  text-align: left;
  border: none;
  white-space: nowrap;
}

/* --- Body cells --- */
.api-table-container tbody td {
  padding: 8px 16px;
  border-bottom: 1px solid var(--api-border-color);
  vertical-align: top;
  color: var(--api-text-color);
}

.api-table-container tbody tr:last-child td {
  border-bottom: none;
}

/* --- Row striping --- */
.api-table-container tbody tr:nth-child(even) td {
  background: var(--api-table-stripe);
}

/* --- Row hover --- */
.api-table-container tbody tr:hover td {
  background: var(--api-table-hover);
  transition: background 0.15s ease;
}

/* --- Code in tables --- */
.api-table-container td code {
  font-family: "Roboto Mono", "Fira Code", "Consolas", monospace;
  font-size: 0.78rem;
  background: transparent;
  border: none;
  padding: 0;
  color: var(--md-primary-fg-color);
}

/* ================================================================
   Field / Parameter tables  (Name | Type | Description)
   ================================================================ */
.api-fields-table tbody td:first-child {
  white-space: nowrap;
  font-weight: 500;
}

.api-fields-table tbody td:nth-child(2) {
  white-space: nowrap;
  font-family: "Roboto Mono", "Fira Code", "Consolas", monospace;
  font-size: 0.75rem;
  color: #5b5b5b;
}

[data-md-color-scheme="slate"] .api-fields-table tbody td:nth-child(2) {
  color: #a0a0a0;
}

/* --- Returns row in parameter tables --- */
.api-returns-row td {
  border-top: 1px solid var(--api-border-color) !important;
  font-size: 0.72rem;
}

.api-returns-row td:first-child strong {
  color: var(--md-accent-fg-color);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.api-returns-row td:nth-child(2) code {
  color: var(--md-accent-fg-color);
  font-weight: 500;
}

[data-md-color-scheme="slate"] .api-returns-row td:nth-child(2) code {
  color: #f2b845;
}

/* --- Returns inline fallback (no surrounding table) --- */
.api-returns {
  font-size: 0.72rem;
  color: var(--api-text-color);
  margin: 4px 0 8px 0;
}

.api-returns strong {
  color: var(--md-accent-fg-color);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.api-returns code {
  color: var(--md-accent-fg-color);
  font-weight: 500;
  background: transparent;
  border: none;
  padding: 0;
}

[data-md-color-scheme="slate"] .api-returns code {
  color: #f2b845;
}

/* ================================================================
   Method tables  (Method | Description)
   ================================================================ */
.api-methods-table tbody td:first-child {
  font-family: "Roboto Mono", "Fira Code", "Consolas", monospace;
  font-size: 0.78rem;
  white-space: nowrap;
}

.api-methods-table tbody td:first-child code {
  color: var(--api-heading-color);
}

/* ================================================================
   API Index tables
   ================================================================ */
.api-index-table tbody td:first-child {
  white-space: nowrap;
}

.api-index-name code {
  font-weight: 500;
}

/* ================================================================
   Simple / generic API tables
   ================================================================ */
.api-simple-table tbody td:first-child {
  white-space: nowrap;
}

/* --- Signature Block --- */
.api-signature {
  background: var(--api-code-bg);
  border: 1px solid var(--api-border-color);
  border-radius: 4px;
  padding: 12px 16px;
  margin: 12px 0;
  font-family: "Roboto Mono", "Fira Code", "Consolas", monospace;
  font-size: 0.85rem;
  overflow-x: auto;
}

/* --- Code blocks --- */
.md-typeset code {
  font-family: "Roboto Mono", "Fira Code", "Consolas", monospace;
  font-size: 0.8rem;
  background: var(--api-code-bg);
  border: 1px solid var(--api-border-color);
  border-radius: 3px;
  padding: 1px 5px;
  word-break: keep-all;
}

.md-typeset pre {
  border: 1px solid var(--api-border-color);
  border-radius: 6px;
}

.md-typeset pre > code {
  border: none;
  border-radius: 0;
  padding: 12px 16px;
}

/* --- Accessibility badges (public/private/protected) --- */
.api-badge {
  display: inline-block;
  padding: 1px 8px;
  border-radius: 3px;
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-right: 6px;
  vertical-align: middle;
}

.api-badge--public {
  background: #e6f4ea;
  color: var(--api-public-color);
  border: 1px solid #ceead6;
}

.api-badge--protected {
  background: #fef7e0;
  color: var(--api-protected-color);
  border: 1px solid #feefc3;
}

.api-badge--private {
  background: #fce8e6;
  color: var(--api-private-color);
  border: 1px solid #f5c6c2;
}

[data-md-color-scheme="slate"] .api-badge--public {
  background: #1a3522;
  color: #5bb974;
  border-color: #2d5a3a;
}

[data-md-color-scheme="slate"] .api-badge--protected {
  background: #3a2e10;
  color: #f2b845;
  border-color: #5a4a1a;
}

[data-md-color-scheme="slate"] .api-badge--private {
  background: #3a1a1a;
  color: #e86562;
  border-color: #5a2a2a;
}

/* --- Deprecated notice --- */
.api-deprecated {
  background: #fef7e0;
  border-left: 4px solid #f2b845;
  padding: 10px 16px;
  margin: 12px 0;
  border-radius: 0 4px 4px 0;
  font-size: 0.8rem;
}

.api-deprecated strong {
  color: var(--api-protected-color);
}

[data-md-color-scheme="slate"] .api-deprecated {
  background: #3a2e10;
  border-left-color: #f2b845;
}

/* --- Since / Version tag --- */
.api-since {
  display: inline-block;
  background: var(--api-code-bg);
  border: 1px solid var(--api-border-color);
  border-radius: 3px;
  padding: 1px 8px;
  font-size: 0.7rem;
  color: var(--api-text-color);
  margin-left: 8px;
}

/* --- Breadcrumb / Navigation --- */
.md-typeset .nav-link {
  font-size: 0.8rem;
  color: var(--md-primary-fg-color);
  text-decoration: none;
}

.md-typeset .nav-link:hover {
  text-decoration: underline;
}

/* --- Search highlight --- */
.md-search-result__article {
  font-size: 0.75rem;
}

/* --- Scrollbar --- */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--api-border-color);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #9aa0a6;
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .md-typeset h1 { font-size: 1.4rem; }
  .md-typeset h2 { font-size: 1.15rem; }
  .md-typeset h3 { font-size: 1rem; }

  .api-table-container table { font-size: 0.7rem; }
  .api-table-container thead th,
  .api-table-container tbody td { padding: 6px 10px; }
}

/* --- Summary block (blockquote with special styling) --- */
.md-typeset blockquote.api-summary {
  border-left: 4px solid var(--md-primary-fg-color);
  background: var(--api-table-stripe);
  padding: 8px 16px;
  margin: 12px 0;
  border-radius: 0 4px 4px 0;
  font-size: 0.85rem;
}

.md-typeset blockquote.api-summary p {
  margin: 0;
}

/* --- Inheritance tree --- */
.api-inheritance {
  background: var(--api-code-bg);
  border: 1px solid var(--api-border-color);
  border-radius: 6px;
  padding: 10px 16px;
  margin: 10px 0;
  font-family: "Roboto Mono", "Fira Code", "Consolas", monospace;
  font-size: 0.82rem;
}

.api-inheritance a {
  color: var(--md-primary-fg-color);
  text-decoration: none;
}

.api-inheritance a:hover {
  text-decoration: underline;
}

/* --- See Also cross-references --- */
.api-see-also {
  background: var(--api-code-bg);
  border: 1px solid var(--api-border-color);
  border-radius: 4px;
  padding: 8px 14px;
  margin: 12px 0;
  font-size: 0.78rem;
}

.api-see-also strong {
  color: var(--api-text-color);
}

.api-see-also code {
  font-size: 0.78rem;
}

/* --- Section separators --- */
.md-typeset hr.api-section-divider {
  border: none;
  border-top: 1px solid var(--api-border-color);
  margin: 24px 0;
}

/* --- Typical Usage example block --- */
.api-usage-block {
  background: var(--api-code-bg);
  border: 1px solid var(--api-border-color);
  border-left: 4px solid var(--md-accent-fg-color);
  border-radius: 0 6px 6px 0;
  margin: 12px 0;
}

.api-usage-block pre {
  margin: 0;
  border: none;
  border-radius: 0;
}

.api-usage-block pre > code {
  border: none;
  padding: 12px 16px;
}

/* --- Raises / Exceptions block --- */
.api-raises {
  background: #fef7e0;
  border: 1px solid #feefc3;
  border-left: 4px solid #f2b845;
  border-radius: 0 4px 4px 0;
  padding: 8px 14px;
  margin: 10px 0;
  font-size: 0.8rem;
}

.api-raises code {
  font-weight: 600;
  color: var(--api-protected-color);
  background: transparent;
  border: none;
  padding: 0;
}

[data-md-color-scheme="slate"] .api-raises {
  background: #3a2e10;
  border-color: #5a4a1a;
}

[data-md-color-scheme="slate"] .api-raises code {
  color: #f2b845;
}

/* --- Call-chain cards (数据流与典型调用链) --- */
.api-callchain {
  margin: 16px 0;
  padding: 14px 18px;
  border-left: 3px solid var(--md-accent-fg-color);
  background: var(--md-code-bg-color);
  border-radius: 0 6px 6px 0;
}

.api-callchain-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 3px 0;
  font-size: 0.82rem;
  line-height: 1.6;
}

.api-callchain-label {
  flex-shrink: 0;
  min-width: 48px;
  font-weight: 700;
  color: var(--md-accent-fg-color);
  font-size: 0.76rem;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.api-callchain-content {
  color: var(--md-typeset-color);
}

.api-callchain-content code {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--md-accent-fg-color);
  background: transparent;
  border: none;
  padding: 0;
}

[data-md-color-scheme="slate"] .api-callchain {
  border-left-color: #f2b845;
}

[data-md-color-scheme="slate"] .api-callchain-label {
  color: #f2b845;
}

[data-md-color-scheme="slate"] .api-callchain-content code {
  color: #f2b845;
}



/* --- Source browser --- */
.source-code {
  border: 1px solid var(--api-border-color);
  border-radius: 8px;
  overflow: auto;
  background: var(--api-code-bg);
  padding: 0;
}

.source-code code {
  display: block;
  padding: 10px 0;
}

.source-line {
  display: block;
  min-height: 1.35em;
  padding: 0 16px 0 0;
  white-space: pre;
}

.source-line {
  scroll-margin-top: 5rem;
}

.source-line:target {
  background: rgba(242, 184, 69, 0.20);
  box-shadow: inset 4px 0 0 #f2b845;
}

[data-md-color-scheme="slate"] .source-line:target {
  background: rgba(242, 184, 69, 0.16);
}

.source-line-no {
  display: inline-block;
  width: 4.5em;
  margin-right: 1em;
  padding-right: 0.8em;
  color: #80868b;
  text-align: right;
  user-select: none;
  border-right: 1px solid var(--api-border-color);
}

/* --- Embedded LLM chat page --- */
.llm-chat-shell {
  width: 100%;
  min-height: 760px;
  border: 1px solid var(--api-border-color);
  border-radius: 8px;
  overflow: hidden;
  background: var(--md-default-bg-color);
}

.llm-chat-shell iframe {
  display: block;
  width: 100%;
  height: 760px;
  border: 0;
}

/* --- Print styles --- */
@media print {
  .md-header, .md-footer, .md-sidebar, .md-tabs { display: none !important; }
  .md-main__inner { max-width: 100% !important; }
  .md-typeset { font-size: 10pt; }
}
"""


# ---------------------------------------------------------------------------
# Index generation
# ---------------------------------------------------------------------------

def _entries_from_api_pages(api_pages: dict[str, str] | None) -> list[tuple[str, str, str, str]]:
    """Extract symbols from deterministic Detailed API pages.

    Returns tuples of (name, module, kind, anchor). This is more reliable than
    scraping LLM-generated module summaries because Detailed API pages are
    driven by symbols.db.
    """
    if not api_pages:
        return []
    entries: list[tuple[str, str, str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for mod, md in api_pages.items():
        current_anchor = ""
        for line in md.splitlines():
            m_anchor = re.match(r'<a id="([^"]+)"></a>', line.strip())
            if m_anchor:
                current_anchor = m_anchor.group(1)
                continue
            m = re.match(r"^###\s+`([^`]+)`\s+·\s+(\w+)", line.strip())
            if not m or not current_anchor:
                continue
            qual_name, kind = m.groups()
            name = qual_name.split(".")[-1]
            key = (name, mod, current_anchor)
            if key in seen:
                continue
            seen.add(key)
            entries.append((name, mod, kind, current_anchor))
    return entries


def _entries_from_module_summaries(doc: DocResult) -> list[tuple[str, str, str, str]]:
    """Fallback symbol extraction from module pages when Detailed API is disabled."""
    entries: list[tuple[str, str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    non_symbol = re.compile(
        r"^(module|class|function|overview|包|项目|架构|模块|类|函数|文件列表|职责|顶层|"
        r"模块概述|类参考|函数参考|快速概览|构造方法|字段|方法|参数|返回值|说明|"
        r"summary|description|parameters|returns?|see also|constructor|fields|methods|"
        r"inheritance|type|source|package|quick summary|typical usage|raises)$",
        re.IGNORECASE,
    )
    for mod, summary in doc.modules.items():
        for line in summary.splitlines():
            m = re.match(r"^(?:#{2,4})\s+(?:`([^`]+)`|([A-Za-z_][A-Za-z0-9_]*))", line)
            if not m:
                continue
            name = (m.group(1) or m.group(2)).strip("`")
            if non_symbol.match(name) or not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
                continue
            key = (name, mod)
            if key in seen:
                continue
            seen.add(key)
            kind = "class" if name[:1].isupper() else "func"
            entries.append((name, mod, kind, name.lower().replace(".", "")))
    return entries


def _generate_api_index(
    doc: DocResult, modules_order: list[str], api_pages: dict[str, str] | None = None
) -> str:
    """Generate the API quick-reference page from deterministic API pages first."""
    api_entries = _entries_from_api_pages(api_pages)
    using_api_pages = bool(api_entries)
    if not api_entries:
        api_entries = _entries_from_module_summaries(doc)

    class_entries = [e for e in api_entries if e[2] == "class"]
    func_entries = [e for e in api_entries if e[2] != "class"]
    class_entries.sort(key=lambda x: (x[0].lower(), x[1].lower()))
    func_entries.sort(key=lambda x: (x[0].lower(), x[1].lower()))

    def _render_index_table(title: str, col1: str, col2: str, entries: list[tuple[str, str, str, str]]) -> list[str]:
        if not entries:
            return []
        link_root = "api" if using_api_pages else "modules"
        html_lines = [
            f"## {title}",
            "",
            '<div class="api-table-container api-index-table" markdown="0">',
            "<table>",
            f"<thead><tr><th>{col1}</th><th>{col2}</th></tr></thead>",
            "<tbody>",
        ]
        for name, mod, _kind, anchor in entries:
            fn = _safe(mod)
            mod_label = _clean_nav_label(mod)
            html_lines.append(
                f'<tr>'
                f'<td class="api-index-name"><code><a href="/{link_root}/{fn}/#{anchor}">{name}</a></code></td>'
                f'<td><a href="/{link_root}/{fn}/">{mod_label}</a></td>'
                f'</tr>'
            )
        html_lines.extend(["</tbody>", "</table>", "</div>"])
        return html_lines

    quick_lines = [
        "# API Quick Reference",
        "",
        "Jump to any class or function in the API reference.",
        "",
    ]
    if class_entries:
        quick_lines.extend(_render_index_table("Classes", "Class", "Module", class_entries))
        quick_lines.append("")
    if func_entries:
        quick_lines.extend(_render_index_table("Functions", "Function", "Module", func_entries))
    return "\n".join(quick_lines)


# ---------------------------------------------------------------------------
# Architecture section extraction
# ---------------------------------------------------------------------------

def _extract_architecture_sections(text: str) -> dict[str, str]:
    """Parse the architecture/reduce output into logical sections.

    Returns dict with keys: overview, modules, api, deps, other
    """
    sections: dict[str, str] = {
        "overview": "",
        "modules": "",
        "api": "",
        "deps": "",
        "dataflow": "",
        "other": "",
    }

    if not text.strip():
        return sections

    lines = text.splitlines()
    current_section = "overview"

    # Heuristic patterns to detect section boundaries
    SECTION_PATTERNS = [
        # Numbered section: "## 1. Project Overview", "## 2. Module Index", etc.
        (re.compile(r"^#+\s*\d+\.\s*(?:.*?(?:项目|包|Project|Package)\s*)?(?:概览|Overview)", re.I), "overview"),
        (re.compile(r"^#+\s*\d+\.\s*(?:.*?(?:模块|Module)\s*)?(?:索引|表|Index|Table)", re.I), "modules"),
        (re.compile(r"^#+\s*\d+\.\s*(?:.*?(?:核心|Core|Key|Quick|API)\s*)?(?:API|导航|Navigation)", re.I), "api"),
        (re.compile(r"^#+\s*\d+\.\s*(?:.*?(?:模块|Module)\s*)?(?:依赖|关系|Dependenc)", re.I), "deps"),
        (re.compile(r"^#+\s*\d+\.\s*(?:.*?(?:数据流|调用链|Data\s*Flow|Workflow|Call\s*Chain))", re.I), "dataflow"),
        # Non-numbered variants
        (re.compile(r"^#+\s*(?:项目|包|Project|Package)\s*(?:概览|Overview)", re.I), "overview"),
        (re.compile(r"^#+\s*(?:模块|Module)\s*(?:索引|表|Index|Table)", re.I), "modules"),
        (re.compile(r"^#+\s*(?:核心|Core|Key|Quick|API)\s*(?:API|导航|Navigation)", re.I), "api"),
        (re.compile(r"^#+\s*(?:模块|Module)\s*(?:依赖|关系|Dependenc)", re.I), "deps"),
        (re.compile(r"^#+\s*(?:数据流|调用链|Data\s*Flow|Workflow|Call\s*Chain)", re.I), "dataflow"),
    ]

    section_lines: dict[str, list[str]] = {k: [] for k in sections}

    for line in lines:
        matched = False
        for pattern, target in SECTION_PATTERNS:
            if pattern.match(line.strip()):
                current_section = target
                matched = True
                break
        if not matched:
            section_lines[current_section].append(line)

    # Merge back
    for key in sections:
        text_block = "\n".join(section_lines[key]).strip()
        # Clean up leading/trailing reference-style text
        text_block = re.sub(r"^[-*]+\s*\n", "", text_block)
        sections[key] = text_block

    return sections


# ---------------------------------------------------------------------------
# Dataflow section formatter
# ---------------------------------------------------------------------------

def _format_dataflow_section(text: str) -> str:
    """Transform flat bullet list into row-based call-chain cards.

    The LLM generates groups like::

        - **触发**: description
        - **流程**: ``code → code``
        - **数据流**: description
        - **产出**: description

    Each group becomes a ``<div class="api-callchain">`` card where every
    field (触发/流程/数据流/产出) is a labelled row — no bullet points.
    """
    if not text.strip():
        return text

    # Split into call-chain groups
    groups = re.split(r'\n\s*\n', text.strip())

    # Pattern:  - **label**: content  (content may contain inline `code`)
    BULLET_RE = re.compile(
        r'^[-\*]\s+\*\*([^*]+)\*\*\s*:\s*(.*)$'
    )

    def _codefy(s: str) -> str:
        """Replace ``...`` with <code>...</code>."""
        return re.sub(r'`([^`]+)`', r'<code>\1</code>', s)

    cards: list[str] = []
    for g in groups:
        g = g.strip()
        if not g:
            continue

        rows: list[str] = []
        for line in g.splitlines():
            line = line.strip()
            m = BULLET_RE.match(line)
            if m:
                label = m.group(1).strip()
                content = _codefy(m.group(2).strip())
                rows.append(
                    f'<div class="api-callchain-row">'
                    f'<span class="api-callchain-label">{label}</span>'
                    f'<span class="api-callchain-content">{content}</span>'
                    f'</div>'
                )

        if rows:
            cards.append(
                f'<div class="api-callchain" markdown="0">\n'
                + '\n'.join(rows)
                + '\n</div>'
            )

    return '\n\n'.join(cards)


# ---------------------------------------------------------------------------
# Returns → table row post-processing
# ---------------------------------------------------------------------------

def _merge_returns_into_tables(text: str) -> str:
    """Merge standalone ``**Returns**:`` lines into the preceding parameter table.

    Converts::

        </tbody></table></div>
        **Returns**: ``int`` — description

    into a ``<tr class="api-returns-row">`` inserted before ``</tbody>``, and
    removes the original bold-text line so it no longer looks like a separate
    mini-section heading.

    Handles backtick-quoted types, plain-word types, and optional em-dash
    descriptions.  Does nothing when no Returns line follows a table.
    """
    pattern = re.compile(
        r'(<tbody>\s*)'
        r'(.*?)'
        r'(\s*</tbody>\s*</table>\s*</div>)'
        r'\s*\n\s*\*\*Returns\*\*:\s*'
        r'(?:`([^`\n]+)`|([^—–\n]+))'
        r'(?:\s*[—–-]\s*([^\n]+?))?'
        r'[ \t]*\n',
        re.DOTALL,
    )

    def _build_row(m: re.Match) -> str:
        before = m.group(1)
        existing_rows = m.group(2)
        after = m.group(3)
        ret_type = m.group(4) or m.group(5) or "(unknown)"
        ret_desc = (m.group(6) or "").strip()
        desc_html = ret_desc if ret_desc else "&nbsp;"
        row = (
            f'<tr class="api-returns-row">'
            f'<td><strong>Returns</strong></td>'
            f'<td><code>{ret_type}</code></td>'
            f'<td>{desc_html}</td>'
            f'</tr>'
        )
        # Preserve the trailing newline so the next element
        # (Typical-Usage / See-Also / next heading) stays on its own line
        return before + existing_rows + row + after + "\n"

    result = pattern.sub(_build_row, text)

    # Second pass: catch Returns lines that are NOT preceded by a table.
    # Functions with no parameters may have no parameter table at all,
    # so the primary regex above won't match them.  Wrap these in a
    # compact styled div instead.
    fallback = re.compile(
        r'\*\*Returns\*\*:\s*'
        r'(?:`([^`\n]+)`|([^—–\n]+))'
        r'(?:\s*[—–-]\s*([^\n]+?))?'
        r'[ \t]*\n',
    )

    def _build_fallback(m: re.Match) -> str:
        ret_type = m.group(1) or m.group(2) or "(unknown)"
        ret_desc = (m.group(3) or "").strip()
        if ret_desc:
            return (
                f'<div class="api-returns" markdown="0">'
                f'<strong>Returns</strong>: <code>{ret_type}</code>'
                f' &mdash; {ret_desc}'
                f'</div>\n'
            )
        else:
            return (
                f'<div class="api-returns" markdown="0">'
                f'<strong>Returns</strong>: <code>{ret_type}</code>'
                f'</div>\n'
            )

    result = fallback.sub(_build_fallback, result)

    # Re-ensure blank lines before --- separators that may have lost
    # their leading blank line when Returns was removed (and the
    # original blank line was stripped by _reorganize_sections).
    # Match --- that is NOT preceded by a blank line.
    result = re.sub(r'(^|[^\n])\n(-{3,}\s*\n)', r'\1\n\n\2', result)

    return result


# ---------------------------------------------------------------------------
# Main render
# ---------------------------------------------------------------------------

def render(
    doc: DocResult,
    base: str = DOCS_BASE,
    api_pages: dict[str, str] | None = None,
    nav_subfolders: bool = True,
) -> Path:
    root = Path(base) / doc.name
    content_dir = root / "docs"
    modules_dir = content_dir / "modules"
    api_dir = content_dir / "api"
    stylesheets_dir = content_dir / "stylesheets"
    modules_dir.mkdir(parents=True, exist_ok=True)
    api_dir.mkdir(parents=True, exist_ok=True)
    stylesheets_dir.mkdir(parents=True, exist_ok=True)

    # --- Generate custom CSS ---
    (stylesheets_dir / "extra.css").write_text(EXTRA_CSS, "utf-8")
    _render_source_files(doc, content_dir)

    # --- Module pages (with TOC + navigation) ---
    modules_order: list[str] = []
    for mod, summary in doc.modules.items():
        fn = _safe(mod) + ".md"
        modules_order.append(mod)

        # Normalize the LLM output
        cleaned = _normalize_markdown(summary)

        # Render module pages as high-level guides. Detailed signatures,
        # parameters, returns, constructors and method tables live under api/.
        localized = _localize_headings(cleaned)
        reorganized = _render_module_guide(localized, mod)

        mod_label = _clean_nav_label(mod)

        page = [
            f"# {mod_label}",
            "",
            f'<span class="md-source-file"><a href="../architecture.md">Architecture</a></span>',
            "",
            "---",
            "",
        ]

        page.append(reorganized)
        page.append("")
        page.append("---")
        page.append(
            f'<span class="md-source-file"><a href="../architecture.md">Architecture</a></span>'
        )

        (modules_dir / fn).write_text("\n".join(page), "utf-8")

    api_order: list[str] = []
    if api_pages:
        for mod, md in api_pages.items():
            fn = _safe(mod) + ".md"
            api_order.append(mod)
            api_md = _normalize_source_links(_normalize_markdown(md))
            (api_dir / fn).write_text(api_md, "utf-8")

    # API quick-reference is intentionally not generated as a public page.
    old_api_index = content_dir / "api-index.md"
    if old_api_index.exists():
        old_api_index.unlink()

    # --- architecture.md ---
    arch_raw = _clean_architecture(doc.architecture or "")
    arch_clean = _normalize_markdown(arch_raw)

    # Extract sections from architecture for better organization
    arch_sections = _extract_architecture_sections(arch_clean)

    arch_lines = [
        f"# Architecture: {doc.name}",
        "",
        "---",
        "",
    ]

    # --- 阅读指南 (Reading Guide) — auto-generated based on module roles ---
    arch_lines.append("## 阅读指南")
    arch_lines.append("")
    arch_lines.append("如果你是初次接触本项目，建议按以下顺序阅读文档：")
    arch_lines.append("")

    # Categorize modules by heuristic analysis of their descriptions
    entry_modules: list[tuple[str, str, str]] = []
    infra_modules: list[tuple[str, str, str]] = []
    core_modules: list[tuple[str, str, str]] = []
    aux_modules: list[tuple[str, str, str]] = []

    for mod in modules_order:
        mod_summary = doc.modules.get(mod, "")
        # Extract the first meaningful description sentence
        desc = ""
        for line in mod_summary.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith("|") and not stripped.startswith(">"):
                # Skip metadata lines
                if stripped.startswith("**Package") or stripped.startswith("**Source") or stripped.startswith("**Module"):
                    continue
                if len(stripped) > 10:
                    desc = stripped[:120]
                    break

        label = _clean_nav_label(mod)
        fn = _safe(mod)
        item = (label, fn, desc)

        # Heuristic categorization
        mod_lower = mod.lower()
        desc_lower = desc.lower()
        if any(kw in mod_lower for kw in ["cli", "app.py"]) or any(kw in desc_lower for kw in ["命令行", "入口", "cli"]):
            entry_modules.append(item)
        # 辅助类(测试/示例/脚本)先扣除:test 模块描述里常出现"配置/设置"等词,
        # 若先判基础设施会被误并入基础设施层,故必须排在 infra 之前。
        elif any(kw in mod_lower for kw in ["eval", "scripts", "test", "example", "benchmark"]) or any(kw in desc_lower for kw in ["评估", "脚本", "测试", "示例", "基准"]):
            aux_modules.append(item)
        elif any(kw in mod_lower for kw in ["common", "inference", "ingestion", "util", "config"]) or any(kw in desc_lower for kw in ["配置", "模型", "客户端", "推理", "解析", "工具", "基础设施", "通用"]):
            infra_modules.append(item)
        else:
            core_modules.append(item)

    step = 1
    # 1. Architecture (this page)
    arch_lines.append(f"**{step}. 先读本页** — 了解项目整体结构、模块职责划分和典型调用链。")
    arch_lines.append("")
    step += 1

    # 2. Infrastructure modules
    if infra_modules:
        names = "、".join(f"[{l}](modules/{f}.md)" for l, f, _ in infra_modules)
        arch_lines.append(f"**{step}. 基础设施层** — {names}")
        arch_lines.append("")
        arch_lines.append("这些模块提供项目的基础能力与通用工具，被其他模块广泛依赖。先理解它们，后续模块更容易读懂。")
        arch_lines.append("")
        step += 1

    # 3. Core business modules
    if core_modules:
        names = "、".join(f"[{l}](modules/{f}.md)" for l, f, _ in core_modules)
        arch_lines.append(f"**{step}. 核心业务层** — {names}")
        arch_lines.append("")
        arch_lines.append("这些模块实现项目的核心业务逻辑，是项目的主体所在。")
        arch_lines.append("")
        step += 1

    # 4. Entry modules
    if entry_modules:
        names = "、".join(f"[{l}](modules/{f}.md)" for l, f, _ in entry_modules)
        arch_lines.append(f"**{step}. 入口层** — {names}")
        arch_lines.append("")
        arch_lines.append("这些模块是用户交互的入口，它们编排调用核心业务层和基础设施层来完成具体任务。阅读时可以对照调用链理解模块间的协作关系。")
        arch_lines.append("")
        step += 1

    # 5. Auxiliary modules
    if aux_modules:
        names = "、".join(f"[{l}](modules/{f}.md)" for l, f, _ in aux_modules)
        arch_lines.append(f"**{step}. 辅助工具** — {names}")
        arch_lines.append("")
        arch_lines.append("这些模块提供评估、测试和实用脚本，通常在了解核心功能后按需查阅。")
        arch_lines.append("")

    arch_lines.append("---")
    arch_lines.append("")

    if arch_sections.get("overview"):
        arch_lines.append("## 项目概述")
        arch_lines.append("")
        # Strip numbered heading that duplicates our section title
        overview_text = re.sub(
            r"^#+\s*\d+\.\s*(?:项目|Project|Package)\s*(?:概述|Overview)\s*\n+",
            "",
            arch_sections["overview"],
            flags=re.IGNORECASE,
        ).strip()
        arch_lines.append(overview_text)
        arch_lines.append("")

    if arch_sections.get("dataflow"):
        arch_lines.append("---")
        arch_lines.append("")
        arch_lines.append("## 数据流与典型调用链")
        arch_lines.append("")
        arch_lines.append(_format_dataflow_section(arch_sections["dataflow"]))
        arch_lines.append("")

    if arch_sections.get("modules"):
        arch_lines.append("---")
        arch_lines.append("")
        arch_lines.append("## 模块索引")
        arch_lines.append("")
        arch_lines.append(arch_sections["modules"])
        arch_lines.append("")

    if arch_sections.get("api"):
        arch_lines.append("---")
        arch_lines.append("")
        arch_lines.append("## 核心 API 速览")
        arch_lines.append("")
        arch_lines.append(arch_sections["api"])
        arch_lines.append("")

    if arch_sections.get("deps"):
        arch_lines.append("---")
        arch_lines.append("")
        arch_lines.append("## 模块依赖关系")
        arch_lines.append("")
        arch_lines.append(arch_sections["deps"])
        arch_lines.append("")

    if arch_sections.get("other"):
        arch_lines.append("---")
        arch_lines.append("")
        arch_lines.append(arch_sections["other"])
        arch_lines.append("")

    arch_md = "\n".join(arch_lines)
    # Force Chinese section headings (LLM stubbornness fallback)
    arch_md = _localize_headings(arch_md)
    (content_dir / "architecture.md").write_text(arch_md, "utf-8")

    # --- index.md: 首页(根路由 /),重定向到架构总览,避免 mkdocs 在 / 上 404 ---
    (content_dir / "index.md").write_text(
        '<meta http-equiv="refresh" content="0; url=./architecture/">\n\n'
        f"# {doc.name} — API 文档\n\n"
        "正在进入[架构总览](architecture.md)…如果没有自动跳转，请点击该链接。\n",
        "utf-8",
    )

    # --- chat.md: embed the local Chainlit QA UI inside the generated docs site ---
    chat_md = f"""# LLM Chat

<div class="llm-chat-shell">
  <iframe src="http://127.0.0.1:8001" title="RepoAgent LLM Chat" loading="lazy"></iframe>
</div>

!!! note "Local service required"
    Start the QA UI before using this page:

    ```bash
    REPO={doc.name} .venv/bin/chainlit run app.py --host 127.0.0.1 --port 8001
    ```

    The generated documentation can run on `http://127.0.0.1:8000`, while this embedded chat connects to Chainlit on `8001`.
"""
    (content_dir / "chat.md").write_text(chat_md, "utf-8")

    # --- mkdocs.yml ---
    def _nav_lines(section: str, mods: list[str], root: str) -> list[str]:
        lines: list[str] = [f"  - {section}:"]
        if not nav_subfolders:
            for mod in sorted(mods, key=str.lower):
                lines.append(f"      - {_clean_nav_label(mod)}: {root}/{_safe(mod)}.md")
            return lines

        groups: dict[str, list[tuple[str, str]]] = {}
        root_items: list[tuple[str, str]] = []
        for mod in mods:
            label = _clean_nav_label(mod)
            path = f"{root}/{_safe(mod)}.md"
            parts = mod.replace("\\", "/").split("/")
            if len(parts) > 1:
                groups.setdefault(parts[0], []).append((label, path))
            else:
                root_items.append((label, path))

        for group in sorted(groups):
            lines.append(f"      - {group}:")
            for label, path in sorted(groups[group], key=lambda x: x[0].lower()):
                lines.append(f"          - {label}: {path}")
        for label, path in sorted(root_items, key=lambda x: x[0].lower()):
            lines.append(f"      - {label}: {path}")
        return lines

    nav_module_lines = _nav_lines("Modules", modules_order, "modules")

    mkdocs_yml = [
        "site_name: " + doc.name + " API Reference",
        "site_description: Auto-generated code API reference",
        "repo_url: https://github.com/user/" + doc.name,
        "edit_uri: ''",
        "",
        "theme:",
        "  name: material",
        "  custom_dir: ''",
        "  language: en",
        "  features:",
        "    - navigation.instant",
        "    - navigation.instant.prefetch",
        "    - navigation.tracking",
        "    - navigation.tabs",
        "    - navigation.tabs.sticky",
        "    - navigation.sections",
        "    - navigation.top",
        "    - navigation.path",
        "    - toc.follow",
        "    - search.suggest",
        "    - search.highlight",
        "    - search.share",
        "    - content.code.copy",
        "    - content.code.annotate",
        "    - content.tabs.link",
        "  palette:",
        "    - scheme: default",
        "      primary: custom",
        "      accent: custom",
        "      toggle:",
        "        icon: material/brightness-7",
        "        name: Switch to dark mode",
        "    - scheme: slate",
        "      primary: custom",
        "      accent: custom",
        "      toggle:",
        "        icon: material/brightness-4",
        "        name: Switch to light mode",
        "  font:",
        "    text: Roboto",
        "    code: Roboto Mono",
        "  icon:",
        "    logo: material/home",
        "",
        "extra_css:",
        "  - stylesheets/extra.css",
        "",
        "extra:",
        "  homepage: architecture.md",
        "",
        "markdown_extensions:",
        "  - pymdownx.highlight:",
        "      anchor_linenums: true",
        "      line_spans: __span",
        "      pygments_lang_class: true",
        "  - pymdownx.inlinehilite",
        "  - pymdownx.snippets",
        "  - pymdownx.superfences",
        "  - pymdownx.details",
        "  - attr_list",
        "  - md_in_html",
        "  - pymdownx.emoji:",
        "      emoji_index: !!python/name:material.extensions.emoji.twemoji",
        "      emoji_generator: !!python/name:material.extensions.emoji.to_svg",
        "  - pymdownx.tabbed:",
        "      alternate_style: true",
        "  - admonition",
        "  - footnotes",
        "  - toc:",
        "      permalink: true",
        "      toc_depth: 2",
        "",
        "plugins:",
        "  - search:",
        "      separator: '[\\s\\-\\_\\.\\/]+'",
        "",
        "docs_dir: docs",
        "not_in_nav: |",
        "  index.md",
        "  source/**/*.md",
        "nav:",
        "  - Architecture: architecture.md",
        "  - LLM Chat: chat.md",
    ]
    mkdocs_yml.extend(nav_module_lines)
    if api_order:
        mkdocs_yml.extend(_nav_lines("Detailed API", api_order, "api"))

    (root / "mkdocs.yml").write_text("\n".join(mkdocs_yml) + "\n", "utf-8")
    return root
