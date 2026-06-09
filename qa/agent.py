"""qa Agent:工具循环 + 引用溯源。

协议:每步模型只输出一个 JSON 动作:
  {"action":"read_file","path":"src/x.py","start":1,"end":40}
  {"action":"grep","pattern":"def parse_args"}
  {"action":"list_dir","path":"src/click"}
  {"action":"final","answer":"...(含 文件:行号 引用)"}

system 始终是稳定仓库前缀(跨轮复用 KV);对话逐轮追加,前缀部分持续命中 cache_prompt。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from inference.client import LlamaClient
from indexing.retrieve import Retriever
from skills.base import get as get_skill
from skills.prefix import build_repo_prefix
from qa.tools import RepoTools

MAX_ITERS = 8

_PROTOCOL = (
    "你可以调用只读工具来查证代码。**每步只输出一个 JSON 对象,不要输出任何其它文字**:\n"
    '- 定位符号: {"action":"find_symbol","name":"<函数/类/方法名>"}  ← 优先用它直接跳到定义\n'
    '- 读文件: {"action":"read_file","path":"<相对路径>","start":1,"end":60}\n'
    '- 搜索:   {"action":"grep","pattern":"<正则>"}\n'
    '- 列目录: {"action":"list_dir","path":"<相对路径>"}\n'
    '- 最终答案: {"action":"final","answer":"<答案,关键处带 文件:行号 引用>"}\n'
    "高效策略:**先用 find_symbol 拿到目标的 文件:行号,再 read_file 精确读那几行**,"
    "不要从头顺序翻大文件。信息足够立即 final。\n"
    "注意:优先依据源码而非测试文件;答案关键结论必须带 `文件:行号` 引用。"
)


@dataclass
class AgentResult:
    answer: str
    steps: list[str] = field(default_factory=list)
    iters: int = 0
    last_cached_tokens: Optional[int] = None
    prefix_chars: int = 0


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


class QAAgent:
    def __init__(self, index_name: str, client: Optional[LlamaClient] = None) -> None:
        self.prefix = build_repo_prefix(index_name)
        self.client = client or LlamaClient()
        self.retriever = Retriever(index_name)
        self.tools = RepoTools(self.retriever.root)

    def _find_symbol(self, name: str) -> str:
        """查符号索引,直接返回定义位置(file:line),让 agent 精准跳转。"""
        if not name:
            return "[需要 name]"
        rows = self.retriever._si.lookup(name, limit=8)
        if not rows:
            return f"[未找到符号: {name}]"
        return "\n".join(
            f"{r['kind']} {(r['parent'] + '.' if r['parent'] else '') + r['name']}"
            f" @ {r['file']}:{r['start_line']}-{r['end_line']}"
            for r in rows
        )

    def ask(self, question: str, k: int = 5, max_iters: int = MAX_ITERS) -> AgentResult:
        # 预检索种子上下文(混合式:先给种子,再让 agent 补充)
        hits = self.retriever.retrieve(question, k=k)
        seed = "\n\n".join(
            f"### {h.name} ({h.location()})\n```\n" + "\n".join(h.text.splitlines()[:20]) + "\n```"
            for h in hits
        )
        first_user = (
            f"{get_skill('qa').suffix}\n\n{_PROTOCOL}\n\n"
            f"## 种子代码片段\n{seed}\n\n## 问题\n{question}"
        )
        messages = [
            {"role": "system", "content": self.prefix},
            {"role": "user", "content": first_user},
        ]

        result = AgentResult(answer="", prefix_chars=len(self.prefix))
        for it in range(max_iters):
            res = self.client.chat(messages, max_tokens=600, temperature=0.1, cache_prompt=True)
            result.iters = it + 1
            result.last_cached_tokens = res.cached_tokens
            obj = _extract_json(res.text)

            if obj is None:  # 没有合法 JSON,当作最终答案
                result.answer = res.text.strip()
                result.steps.append("final(无 JSON,直接作答)")
                return result

            action = obj.get("action")
            if action == "final":
                result.answer = str(obj.get("answer", "")).strip() or res.text.strip()
                result.steps.append("final")
                return result

            if action == "find_symbol":
                obs = self._find_symbol(obj.get("name", ""))
                result.steps.append(f'find_symbol({obj.get("name", "")})')
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": f"符号定位结果:\n{obs}\n\n请继续(JSON)。"})
            elif action in ("read_file", "grep", "list_dir"):
                obs = self.tools.dispatch(action, obj)
                summary = obj.get("path") or obj.get("pattern") or ""
                result.steps.append(f"{action}({summary})")
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": f"工具结果:\n{obs}\n\n请继续(JSON)。"})
            else:
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": "动作无效,请输出合法 JSON 动作。"})

        # 迭代用尽:强制给出最终答案(仍要求带引用)
        messages.append({"role": "user", "content":
            "已达查证上限。请基于以上信息给出最终答案,**关键结论必须带 `文件:行号` 引用**;"
            "信息不足处如实说明,不要编造。"})
        res = self.client.chat(messages, max_tokens=600, temperature=0.1, cache_prompt=True)
        result.answer = res.text.strip()
        result.last_cached_tokens = res.cached_tokens
        result.steps.append("final(强制)")
        return result
