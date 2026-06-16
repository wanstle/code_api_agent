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
MAX_HISTORY_TURNS = 4
_FINAL_CITATION = re.compile(r"[\w./-]+:\d+")

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
    "- 若问题是追问,结合对话历史补全省略主语,但证据仍以文档/源码引用为准。\n"
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


def _format_history(history: list[dict[str, str]], max_turns: int = MAX_HISTORY_TURNS) -> str:
    if not history:
        return "[无历史对话]"
    recent = history[-max_turns:]
    lines: list[str] = []
    for i, turn in enumerate(recent, 1):
        q = turn.get("question", "").strip()
        a = turn.get("answer", "").strip()
        if len(a) > 900:
            a = a[:900].rstrip() + "..."
        lines.append(f"[{i}] 用户: {q}\n[{i}] 助手: {a}")
    return "\n\n".join(lines)


class QAAgent:
    def __init__(self, index_name: str, client: Optional[LlamaClient] = None) -> None:
        self.prefix = build_repo_prefix(index_name)
        self.client = client or LlamaClient()
        self.retriever = Retriever(index_name)
        docs_root = Path("docs") / index_name / "docs"
        self.docs_root = docs_root if docs_root.exists() else None
        self.tools = RepoTools(self.retriever.root, self.docs_root)
        self.history: list[dict[str, str]] = []

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
        k = _as_int(k, DEFAULT_SEED_K, 0, MAX_SEARCH_K)
        docs_seed = self._docs_seed()
        hits = self.retriever.retrieve(question, k=k) if k else []
        seed = self._format_hits(hits, max_lines=12)
        history_context = _format_history(self.history)
        first_user = (
            f"{get_skill('qa').suffix}\n\n{_PROTOCOL}\n\n"
            f"## 对话历史（用于理解追问,不能替代引用证据）\n{history_context}\n\n"
            f"## 已生成文档优先上下文\n{docs_seed}\n\n"
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
            obj = _extract_json(res.text)

            if obj is None:
                text = res.text.strip()
                if _has_citation(text):
                    result.answer = _final_answer_from_text(text)
                    result.steps.append("final(无 JSON,有引用)")
                    self.history.append({"question": question, "answer": result.answer})
                    return result
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": "请不要输出散文。只能输出一个 JSON 动作;若要回答,用 {\"action\":\"final\",\"answer\":\"...带 docs:文件:行号 或 文件:行号 引用...\"}。"})
                continue

            action = str(obj.get("action", "")).strip()
            if action == "final":
                answer = _final_answer_from_text(res.text)
                if _has_citation(answer) or result.iters >= max_iters:
                    result.answer = answer
                    result.steps.append("final")
                    self.history.append({"question": question, "answer": answer})
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
        result.answer = _final_answer_from_text(res.text)
        result.last_cached_tokens = res.cached_tokens
        result.steps.append("final(强制)")
        self.history.append({"question": question, "answer": result.answer})
        return result
