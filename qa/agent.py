"""qa Agent:工具循环 + 引用溯源。

协议:每步模型只输出一个 JSON 动作:
  {"action":"search_code","query":"用户意图或符号名","k":5}
  {"action":"find_symbol","name":"函数/类/方法名"}
  {"action":"read_file","path":"src/x.py","start":1,"end":40}
  {"action":"grep","pattern":"def parse_args"}
  {"action":"list_dir","path":"src/click"}
  {"action":"list_docs","path":"."}
  {"action":"read_doc","path":"architecture.md","start":1,"end":80}
  {"action":"final","answer":"...(含 docs:文件:行号 或 文件:行号 引用)"}

system 始终是稳定仓库前缀(跨轮复用 KV);对话逐轮追加,前缀部分持续命中 cache_prompt。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Any

from inference.client import LlamaClient
from indexing.retrieve import Retriever
from skills.base import get as get_skill
from skills.prefix import build_repo_prefix
from qa.tools import RepoTools

MAX_ITERS = 6
DEFAULT_SEED_K = 4
MAX_SEARCH_K = 8
MAX_HISTORY_TURNS = 10
MAX_MEMORY_ITEMS = 10
MAX_MEMORY_ITEMS_PER_TURN = 10
_FINAL_CITATION = re.compile(r"[\w./-]+:\d+")
_FILE_REF = re.compile(r"(?<![\w.-])((?:docs:|docs/)?[\w./-]+):(\d+)(?:-\d+)?")
_CODE_SPAN = re.compile(r"`([^`]{2,120})`")
_DOC_CITATION = re.compile(r"(?<![\w./-])docs:([\w./-]+\.md):(\d+)(?:-\d+)?")
_PATH_CITATION = re.compile(r"(?<![`\w.-])((?:[\w.-]+/)+[\w.-]+\.[A-Za-z0-9]+):(\d+)(?:-\d+)?")
_FOLLOWUP_ITEM_REF = re.compile(r"(?:^|[对把将请看问说讲聊析释明\s])(?:第\s*)?(\d+)\s*(?:[。)、]|点|条|项|[.](?!\d))")
_SECTION_LABEL = re.compile(r"^\s*(?:[-*+]\s*)?([^：:\n]{2,24})[：:]\s*(.*)$")

_PROTOCOL = (
    "你可以调用只读工具来查证代码。每步只输出一个 JSON 对象,不要输出任何其它文字。\n"
    "可用动作:\n"
    '- 语义检索: {"action":"search_code","query":"<要找的行为/符号/路径关键词>","k":5}  ← 默认首选\n'
    '- 定位符号: {"action":"find_symbol","name":"<函数/类/方法名>"}  ← 已知精确名字时使用\n'
    '- 读文件: {"action":"read_file","path":"<相对路径>","start":1,"end":80}  ← 只读相关行附近\n'
    '- 正则搜索: {"action":"grep","pattern":"<精确字符串或正则>"}  ← search_code/find_symbol 不够时才用\n'
    '- 列源码目录: {"action":"list_dir","path":"<相对路径>"}  ← 只在源码路径不清楚时用\n'
    '- 列已生成文档: {"action":"list_docs","path":"."}  ← 用户问文档/架构/模块说明时使用\n'
    '- 读已生成文档: {"action":"read_doc","path":"architecture.md","start":1,"end":120}\n'
    '- 最终答案: {"action":"final","answer":"<Markdown 答案,关键处带 文件:行号 或 docs:文件:行号 引用>"}\n'
    "最终答案格式:\n"
    "- answer 字段里只放给用户看的 Markdown,不要再嵌套 JSON、代码围栏或转义换行。\n"
    "- 优先用 2-5 条短 bullet 或短段落;引用直接写在相关句子后。\n"
    "- 引用必须保持在同一行,写成反引号内的完整短引用,如 `docs:architecture.md:62` 或 `src/pkg/file.py:201`。\n"
    "- 不要把引用写进方括号,不要写成 `[docs\\n.md:62]`、`[src\\n.py:201]` 这类断裂格式。\n"
    "- 若问题是追问,必须先使用\"追问解析\"补全省略主语;如果用户说第 N 条/第 N 点/对 N,就是指上一轮答案的第 N 个条目。\n"
    "- 如果用户问\"上述/前面/刚才的 <某段落名>\",优先使用追问解析中的上一轮命名段落。\n"
    "- 追问解析非空时,只回答解析指向的对象,不要重新展开上一轮所有条目。\n"
    "- 证据仍以文档/源码引用为准。\n"
    "策略约束:\n"
    "1. 先看种子片段;若已有足够证据,直接 final。\n"
    "2. 不要从头顺序翻大文件;先 search_code 或 find_symbol,再 read_file 精确读 40-90 行。\n"
    "3. 不要重复调用同一个工具和同一组参数;换 query 或基于已有结果回答。\n"
    "4. grep 只用于精确标识符/字符串兜底,不要用宽泛词扫全仓库。\n"
    "5. 默认先查已生成文档;如果文档已经足够,直接基于文档回答并给出 `docs:文件:行号` 引用。\n"
    "6. 只有当文档没有覆盖关键细节时,再转去真实源码查证。\n"
    "7. 优先依据非测试源码;关键结论必须带 `文件:行号` 或 `docs:文件:行号` 引用。信息不足要说明不足。"
)


@dataclass
class MemoryTurn:
    question: str
    answer: str
    items: list[str] = field(default_factory=list)
    sections: dict[str, str] = field(default_factory=dict)
    files: list[str] = field(default_factory=list)
    docs: list[str] = field(default_factory=list)
    symbols: list[str] = field(default_factory=list)


@dataclass
class AgentResult:
    answer: str
    steps: list[str] = field(default_factory=list)
    iters: int = 0
    last_cached_tokens: Optional[int] = None
    prefix_chars: int = 0


def _json_dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)


def _tool_key(action: str, obj: dict) -> str:
    relevant = {
        "search_code": ("query", "k"),
        "find_symbol": ("name",),
        "read_file": ("path", "start", "end"),
        "grep": ("pattern",),
        "list_dir": ("path",),
        "list_docs": ("path",),
        "read_doc": ("path", "start", "end"),
    }.get(action, tuple(sorted(obj)))
    return action + ":" + _json_dumps({k: obj.get(k) for k in relevant})


def _as_int(value: Any, default: int, low: int, high: int) -> int:
    try:
        n = int(value)
    except (TypeError, ValueError):
        n = default
    return max(low, min(high, n))


def _has_citation(text: str) -> bool:
    return bool(_FINAL_CITATION.search(text or ""))


def _extract_json(text: str) -> Optional[dict]:
    """取文本里**第一个合法 JSON 对象**。

    模型有时一条响应吐多个 JSON 动作;用 raw_decode 从每个 '{' 处尝试解析,
    成功即返回首个 dict —— 避免"首{到末}"跨多个对象导致解析失败。
    """
    decoder = json.JSONDecoder()
    for i, ch in enumerate(text):
        if ch == "{":
            try:
                obj, _ = decoder.raw_decode(text[i:])
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                return obj
    return None


def _final_answer_from_text(text: str) -> str:
    """Return user-facing Markdown even if the model emitted a final JSON object."""
    raw = (text or "").strip()
    obj = _extract_json(raw)
    if obj and str(obj.get("action", "")).strip() == "final":
        answer = str(obj.get("answer", "")).strip()
        if answer:
            return answer
    return raw


def normalize_answer_citations(text: str) -> str:
    """Stabilize citation rendering for Chainlit/Markdown.

    Tools expose document lines as docs:path.md:line because that is easy for
    the model to copy. User-facing Markdown is less fragile when citations are
    compact inline-code spans. docs/path.md:line also avoids the extra colon
    that small local models often split into broken bracket citations.
    """
    if not text:
        return text

    out = text
    out = re.sub(r"\[\s*(docs:[\w./-]+\.md:\d+(?:-\d+)?)\s*\]", r"\1", out)
    out = re.sub(r"\[\s*([\w./-]+/[^\]\s]+?\.\w+:\d+(?:-\d+)?)\s*\]", r"\1", out)

    placeholders: list[str] = []

    def protect_code(m: re.Match[str]) -> str:
        placeholders.append(m.group(0))
        return f"\x00CODE{len(placeholders) - 1}\x00"

    out = re.sub(r"`[^`]*`", protect_code, out)
    out = _DOC_CITATION.sub(lambda m: f"`docs/{m.group(1)}:{m.group(2)}`", out)
    out = _PATH_CITATION.sub(lambda m: f"`{m.group(1)}:{m.group(2)}`", out)

    for i, span in enumerate(placeholders):
        normalized = span.strip("`")
        doc_match = _DOC_CITATION.fullmatch(normalized)
        path_match = _PATH_CITATION.fullmatch(normalized)
        if doc_match:
            replacement = f"`docs/{doc_match.group(1)}:{doc_match.group(2)}`"
        elif path_match:
            replacement = f"`{path_match.group(1)}:{path_match.group(2)}`"
        else:
            replacement = span
        out = out.replace(f"\x00CODE{i}\x00", replacement)

    return out


def _unique_keep_order(items: list[str], limit: int = MAX_MEMORY_ITEMS) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        item = item.strip()
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
        if len(out) >= limit:
            break
    return out


def _compact_line(text: str, limit: int = 260) -> str:
    compact = re.sub(r"\s+", " ", text or "").strip()
    if len(compact) > limit:
        compact = compact[:limit].rstrip() + "..."
    return compact


def _strip_markdown_prefix(line: str) -> str:
    return re.sub(r"^\s*(?:[-*+]\s+|>\s+)+", "", line).strip()


def _extract_answer_items(answer: str, limit: int = MAX_MEMORY_ITEMS_PER_TURN) -> list[str]:
    """Extract answer-level list items so follow-ups like 'explain 5' bind correctly."""
    if not answer:
        return []

    lines = [ln.rstrip() for ln in answer.splitlines()]
    numbered: dict[int, str] = {}
    current_no: int | None = None

    for raw in lines:
        line = raw.strip()
        if not line or set(line) <= {"-", "*", "_"}:
            current_no = None
            continue
        m = re.match(r"^\s*(?:[-*+]\s*)?(\d{1,2})[.)、]\s+(.+)", raw)
        if m:
            current_no = int(m.group(1))
            if 1 <= current_no <= limit:
                numbered[current_no] = _compact_line(m.group(2))
            continue
        if current_no and current_no in numbered and re.match(r"^\s{2,}\S", raw):
            numbered[current_no] = _compact_line(numbered[current_no] + " " + line)

    if numbered:
        return [numbered[i] for i in sorted(numbered)[:limit]]

    # Many local-model answers are visually separated paragraphs rather than
    # valid Markdown lists. Treat citation-bearing/topical lines as items.
    fallback: list[str] = []
    for raw in lines:
        line = _strip_markdown_prefix(raw)
        if not line or line.startswith("```") or line.startswith("#"):
            continue
        if len(line) < 12:
            continue
        section_match = _SECTION_LABEL.match(line)
        if section_match and section_match.group(2).strip():
            fallback.append(_compact_line(line))
        elif _FINAL_CITATION.search(line):
            fallback.append(_compact_line(line))
        if len(fallback) >= limit:
            break
    return fallback


def _extract_answer_sections(answer: str, limit: int = MAX_MEMORY_ITEMS_PER_TURN) -> dict[str, str]:
    """Extract named answer paragraphs such as '信息不足处: ...'."""
    sections: dict[str, str] = {}
    if not answer:
        return sections

    current_label: str | None = None
    for raw in answer.splitlines():
        line = _strip_markdown_prefix(raw.strip())
        if not line or line.startswith("```") or line.startswith("#"):
            continue
        m = _SECTION_LABEL.match(line)
        if m:
            label = re.sub(r"^[\d.)、\s]+", "", m.group(1)).strip()
            body = m.group(2).strip()
            if 2 <= len(label) <= 24 and not label.startswith(("http", "src/", "docs/")):
                current_label = label
                if label not in sections and len(sections) < limit:
                    sections[label] = _compact_line(body or label)
                elif label in sections and body:
                    sections[label] = _compact_line(sections[label] + " " + body)
                continue
        if current_label and current_label in sections and raw.startswith((" ", "\t", "-", "*")):
            sections[current_label] = _compact_line(sections[current_label] + " " + line)

    return sections


def _section_score(question: str, label: str) -> int:
    q = question or ""
    score = 0
    if label and label in q:
        score += 10
    for token in re.findall(r"[\u4e00-\u9fff]{2,}|[A-Za-z_][A-Za-z0-9_]+", label):
        if token in q:
            score += min(len(token), 6)
    return score


def _followup_item_number(question: str) -> int | None:
    q = question or ""
    for m in _FOLLOWUP_ITEM_REF.finditer(q):
        try:
            n = int(m.group(1))
        except ValueError:
            continue
        if 1 <= n <= MAX_MEMORY_ITEMS_PER_TURN:
            return n
    return None


def _extract_focus(question: str, answer: str) -> tuple[list[str], list[str], list[str]]:
    files: list[str] = []
    docs: list[str] = []
    for m in _FILE_REF.finditer(answer or ""):
        path = m.group(1)
        if path.startswith("docs:"):
            docs.append(path.removeprefix("docs:"))
        elif path.startswith("docs/"):
            docs.append(path.removeprefix("docs/"))
        else:
            files.append(path)

    symbols: list[str] = []
    for text in (question or "", answer or ""):
        for m in _CODE_SPAN.finditer(text):
            val = m.group(1).strip()
            if "/" in val or val.endswith(('.py', '.md', '.ts', '.js')):
                continue
            if re.search(r"[A-Za-z_]", val):
                symbols.append(val)
        for val in re.findall(r"\b[A-Z][A-Za-z0-9_]{2,}\b|\b[a-zA-Z_]\w*\.[a-zA-Z_]\w*\b", text or ""):
            if val.endswith((".py", ".md", ".js", ".ts", ".json", ".toml")):
                continue
            if val not in {"JSON", "Markdown", "API", "LLM", "CPU", "GPU"}:
                symbols.append(val)

    return (
        _unique_keep_order(files),
        _unique_keep_order(docs),
        _unique_keep_order(symbols),
    )


def _memory_turn(question: str, answer: str) -> MemoryTurn:
    files, docs, symbols = _extract_focus(question, answer)
    items = _extract_answer_items(answer)
    sections = _extract_answer_sections(answer)
    return MemoryTurn(question=question, answer=answer, items=items, sections=sections, files=files, docs=docs, symbols=symbols)


def _format_history(history: list[MemoryTurn], max_turns: int = MAX_HISTORY_TURNS) -> str:
    if not history:
        return "[无历史对话]"
    recent = history[-max_turns:]
    lines: list[str] = []
    for i, turn in enumerate(recent, 1):
        answer = turn.answer.strip()
        if len(answer) > 700:
            answer = answer[:700].rstrip() + "..."
        focus = []
        item_text = ""
        if turn.items:
            item_lines = [f"  {n}. {item}" for n, item in enumerate(turn.items, 1)]
            item_text = "\n上一轮条目:\n" + "\n".join(item_lines)
        if turn.sections:
            section_lines = [f"  - {label}: {body}" for label, body in list(turn.sections.items())[:MAX_MEMORY_ITEMS]]
            item_text += "\n上一轮命名段落:\n" + "\n".join(section_lines)
        if turn.symbols:
            focus.append("symbols=" + ", ".join(turn.symbols[:MAX_MEMORY_ITEMS]))
        if turn.files:
            focus.append("files=" + ", ".join(turn.files[:MAX_MEMORY_ITEMS]))
        if turn.docs:
            focus.append("docs=" + ", ".join(turn.docs[:MAX_MEMORY_ITEMS]))
        focus_text = "\n焦点: " + " | ".join(focus) if focus else ""
        lines.append(f"[{i}] 用户: {turn.question.strip()}\n[{i}] 助手摘要: {answer}{item_text}{focus_text}")
    return "\n\n".join(lines)


class QAAgent:
    def __init__(self, index_name: str, client: Optional[LlamaClient] = None) -> None:
        self.prefix = build_repo_prefix(index_name)
        self.client = client or LlamaClient()
        self.retriever = Retriever(index_name)
        docs_root = Path("docs") / index_name / "docs"
        self.docs_root = docs_root if docs_root.exists() else None
        self.tools = RepoTools(self.retriever.root, self.docs_root)
        self.history: list[MemoryTurn] = []
        self.turn_id = 0

    def _format_hits(self, hits, *, max_lines: int = 16) -> str:
        if not hits:
            return "[无检索结果]"
        blocks = []
        for i, h in enumerate(hits, 1):
            sig = f"\nsignature: {h.signature}" if h.signature else ""
            code = "\n".join(h.text.splitlines()[:max_lines])
            blocks.append(
                f"[{i}] {h.kind} {h.name} @ {h.file}:{h.start_line}-{h.end_line} "
                f"source={h.source} score={h.score}{sig}\n```\n{code}\n```"
            )
        return "\n\n".join(blocks)

    def _search_code(self, query: str, k: int = 5) -> str:
        query = (query or "").strip()
        if not query:
            return "[需要 query]"
        hits = self.retriever.retrieve(query, k=_as_int(k, 5, 1, MAX_SEARCH_K))
        return "TOOL_RESULT search_code query=" + repr(query) + "\n" + self._format_hits(hits, max_lines=14)

    def _memory_focus(self, max_turns: int = MAX_HISTORY_TURNS) -> dict[str, list[str]]:
        files: list[str] = []
        docs: list[str] = []
        symbols: list[str] = []
        for turn in self.history[-max_turns:]:
            files.extend(turn.files)
            docs.extend(turn.docs)
            symbols.extend(turn.symbols)
        return {
            "files": _unique_keep_order(files),
            "docs": _unique_keep_order(docs),
            "symbols": _unique_keep_order(symbols),
        }

    def _resolve_followup(self, question: str) -> str:
        if not self.history:
            return ""
        previous = self.history[-1]

        n = _followup_item_number(question)
        if n is not None:
            if 1 <= n <= len(previous.items):
                return f"上一轮第 {n} 条 = {previous.items[n - 1]}"
            return f"用户提到第 {n} 条,但上一轮只记录了 {len(previous.items)} 个条目;需要先澄清或依据上一轮答案判断。"

        best_label = ""
        best_score = 0
        for label in previous.sections:
            score = _section_score(question, label)
            if score > best_score:
                best_label = label
                best_score = score
        if best_label and best_score >= 2:
            return f"上一轮命名段落“{best_label}” = {previous.sections[best_label]}"

        q = question or ""
        if any(word in q for word in ("上述", "前面", "刚才", "上面", "这个", "这些")):
            return "检测到追问指代,但没有匹配到明确编号或命名段落;请结合最近一轮答案,必要时先澄清。"
        return ""

    def _memory_query(self, question: str) -> str:
        focus = self._memory_focus()
        resolved = self._resolve_followup(question)
        parts = [question.strip()]
        if resolved:
            parts.append(resolved)
        if focus["symbols"]:
            parts.append("related symbols: " + " ".join(focus["symbols"][:6]))
        if focus["files"]:
            parts.append("related files: " + " ".join(focus["files"][:4]))
        if focus["docs"]:
            parts.append("related docs: " + " ".join(focus["docs"][:3]))
        return " | ".join(p for p in parts if p)

    def _remember(self, question: str, answer: str) -> None:
        self.history.append(_memory_turn(question, answer))
        if len(self.history) > MAX_HISTORY_TURNS * 2:
            self.history = self.history[-MAX_HISTORY_TURNS * 2:]

    def _debug_prompt(self, *, turn_id: int, question: str, memory_query: str, resolved_followup: str, docs_seed: str, seed: str, history_context: str) -> None:
        focus = self._memory_focus()
        approx_chars = len(self.prefix) + len(docs_seed) + len(seed) + len(history_context) + len(question)
        print(
            "[qa-debug] "
            f"turn_id={turn_id} question={question!r} "
            f"history_turns={len(self.history)} "
            f"prefix_chars={len(self.prefix)} docs_seed_chars={len(docs_seed)} "
            f"source_seed_chars={len(seed)} history_chars={len(history_context)} "
            f"approx_prompt_chars={approx_chars} "
            f"memory_query={memory_query!r} "
            f"resolved_followup={resolved_followup!r} "
            f"focus_symbols={focus['symbols'][:6]} focus_files={focus['files'][:4]} focus_docs={focus['docs'][:3]}",
            flush=True,
        )

    def _docs_overview(self, max_entries: int = 16) -> str:
        if self.docs_root is None:
            return "[未生成文档目录]"
        try:
            entries = sorted(p for p in self.docs_root.iterdir() if not p.name.startswith("."))
        except OSError as e:
            return f"[读取文档目录失败: {e}]"

        lines = [f"docs_root: {self.docs_root}", "pages:"]
        shown = 0
        for entry in entries:
            if entry.is_dir():
                lines.append(f"- {entry.name}/")
            elif entry.suffix.lower() == ".md":
                lines.append(f"- {entry.name}")
            else:
                continue
            shown += 1
            if shown >= max_entries:
                break
        if shown == 0:
            lines.append("[无 Markdown 文档]")
        return "\n".join(lines)

    def _docs_seed(self) -> str:
        if self.docs_root is None:
            return "[未生成文档目录]"
        blocks = ["### 文档索引\n```\n" + self._docs_overview() + "\n```"]
        for rel, end in (("index.md", 40), ("architecture.md", 90), ("api-index.md", 80)):
            if (self.docs_root / rel).exists():
                blocks.append(f"### docs/{rel}\n```\n" + self.tools.read_doc(rel, 1, end) + "\n```")
        return "\n\n".join(blocks)

    def _find_symbol(self, name: str) -> str:
        """查符号索引,直接返回定义位置(file:line),让 agent 精准跳转。"""
        if not name:
            return "[需要 name]"
        rows = self.retriever._si.lookup(name, limit=8)
        if not rows:
            return f"[未找到符号: {name}]"
        lines = [f"TOOL_RESULT find_symbol name={name!r} results={len(rows)}"]
        for r in rows:
            qn = r.get("qualified_name") or ((r["parent"] + "." if r["parent"] else "") + r["name"])
            sig = f" signature={r.get('signature')}" if r.get("signature") else ""
            lines.append(f"{r['kind']} {qn} @ {r['file']}:{r['start_line']}-{r['end_line']}{sig}")
        return "\n".join(lines)

    def ask(self, question: str, k: int = DEFAULT_SEED_K, max_iters: int = MAX_ITERS) -> AgentResult:
        # 文档优先:先给已生成文档索引/核心页,源码种子只作为兜底线索。
        self.turn_id += 1
        turn_id = self.turn_id
        k = _as_int(k, DEFAULT_SEED_K, 0, MAX_SEARCH_K)
        docs_seed = self._docs_seed()
        resolved_followup = self._resolve_followup(question)
        memory_query = self._memory_query(question)
        hits = self.retriever.retrieve(memory_query, k=k) if k else []
        seed = self._format_hits(hits, max_lines=12)
        history_context = _format_history(self.history)
        self._debug_prompt(
            turn_id=turn_id,
            question=question,
            memory_query=memory_query,
            resolved_followup=resolved_followup,
            docs_seed=docs_seed,
            seed=seed,
            history_context=history_context,
        )
        first_user = (
            f"{get_skill('qa').suffix}\n\n{_PROTOCOL}\n\n"
            f"## 本轮 ID\nqa-turn-{turn_id}\n\n"
            f"## 对话历史（用于理解追问,不能替代引用证据）\n{history_context}\n\n"
            f"## 追问解析\n{resolved_followup or '[不是追问或未解析]'}\n\n"
            f"如果追问解析非空,本轮只回答追问解析指向的对象。\n\n"
            f"## 已生成文档优先上下文\n{docs_seed}\n\n"
            f"## 用于本轮检索的记忆增强查询\n{memory_query}\n\n"
            f"## 源码兜底种子片段\n{seed}\n\n## 当前问题\n{question}"
        )
        messages = [
            {"role": "system", "content": self.prefix},
            {"role": "user", "content": first_user},
        ]

        result = AgentResult(answer="", prefix_chars=len(self.prefix))
        seen_tools: set[str] = set()
        for it in range(max_iters):
            res = self.client.chat(messages, max_tokens=700, temperature=0.0, cache_prompt=True)
            result.iters = it + 1
            result.last_cached_tokens = res.cached_tokens
            print(
                f"[qa-debug] iter={it + 1} latency_s={res.latency_s:.2f} "
                f"cached_tokens={res.cached_tokens} prompt_ms={res.prompt_ms} "
                f"response_chars={len(res.text)}",
                flush=True,
            )
            obj = _extract_json(res.text)

            if obj is None:
                text = res.text.strip()
                if _has_citation(text):
                    result.answer = normalize_answer_citations(_final_answer_from_text(text))
                    result.steps.append("final(无 JSON,有引用)")
                    self._remember(question, result.answer)
                    return result
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": "请不要输出散文。只能输出一个 JSON 动作;若要回答,用 {\"action\":\"final\",\"answer\":\"...带 docs:文件:行号 或 文件:行号 引用...\"}。"})
                continue

            action = str(obj.get("action", "")).strip()
            if action == "final":
                answer = normalize_answer_citations(_final_answer_from_text(res.text))
                if _has_citation(answer) or result.iters >= max_iters:
                    result.answer = answer
                    result.steps.append("final")
                    self._remember(question, answer)
                    return result
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": "最终答案缺少 `docs:文件:行号` 或 `文件:行号` 引用。优先读已生成文档;若文档没覆盖关键点,再查真实源码并补上引用。"})
                continue

            if action in ("search_code", "find_symbol", "read_file", "grep", "list_dir", "list_docs", "read_doc"):
                key = _tool_key(action, obj)
                if key in seen_tools:
                    messages.append({"role": "assistant", "content": res.text})
                    messages.append({"role": "user", "content": "你重复调用了同一个工具和参数。请基于已有结果 final,或换一个更具体的 query/path/line 范围。"})
                    result.steps.append(f"repeat({action})")
                    continue
                seen_tools.add(key)

                if action == "search_code":
                    obs = self._search_code(str(obj.get("query", "")), _as_int(obj.get("k"), 5, 1, MAX_SEARCH_K))
                    summary = obj.get("query", "")
                elif action == "find_symbol":
                    obs = self._find_symbol(str(obj.get("name", "")))
                    summary = obj.get("name", "")
                else:
                    obs = self.tools.dispatch(action, obj)
                    summary = obj.get("path") or obj.get("pattern") or ""

                result.steps.append(f"{action}({summary})")
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": f"工具结果:\n{obs}\n\n请继续输出一个 JSON 动作。若已生成文档已经足够,就直接 final 并给出 docs:文件:行号;否则再查源码。"})
            else:
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": "动作无效。请输出 search_code/find_symbol/read_file/grep/list_dir/list_docs/read_doc/final 之一的 JSON。"})

        # 迭代用尽:强制给出最终答案(仍要求带引用)
        messages.append({"role": "user", "content":
            "已达查证上限。请基于以上信息给出最终答案,**关键结论必须带 `docs:文件:行号` 或 `文件:行号` 引用**;"
            "信息不足处如实说明,不要编造。"})
        res = self.client.chat(messages, max_tokens=700, temperature=0.0, cache_prompt=True)
        print(
            f"[qa-debug] final_force latency_s={res.latency_s:.2f} "
            f"cached_tokens={res.cached_tokens} prompt_ms={res.prompt_ms} "
            f"response_chars={len(res.text)}",
            flush=True,
        )
        result.answer = normalize_answer_citations(_final_answer_from_text(res.text))
        result.last_cached_tokens = res.cached_tokens
        result.steps.append("final(强制)")
        self._remember(question, result.answer)
        return result
