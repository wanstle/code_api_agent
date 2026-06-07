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
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from inference.client import LlamaClient
from indexing.retrieve import Retriever
from skills.base import get as get_skill
from skills.prefix import build_repo_prefix
from qa.tools import RepoTools

MAX_ITERS = 5

_PROTOCOL = (
    "你可以调用只读工具来查证代码。**每步只输出一个 JSON 对象,不要输出任何其它文字**:\n"
    '- 读文件: {"action":"read_file","path":"<相对路径>","start":1,"end":40}\n'
    '- 搜索:   {"action":"grep","pattern":"<正则>"}\n'
    '- 列目录: {"action":"list_dir","path":"<相对路径>"}\n'
    '- 最终答案: {"action":"final","answer":"<答案,关键处带 文件:行号 引用>"}\n'
    "信息足够时立即输出 final。\n"
    "注意:**优先依据源码而非测试文件**;若种子片段主要来自测试或不足以确定答案,"
    "先用 grep/read_file 在源码中确认,再 final。"
)


@dataclass
class AgentResult:
    answer: str
    steps: list[str] = field(default_factory=list)
    iters: int = 0
    last_cached_tokens: Optional[int] = None
    prefix_chars: int = 0


def _extract_json(text: str) -> Optional[dict]:
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidate = m.group(1) if m else None
    if candidate is None:
        i, j = text.find("{"), text.rfind("}")
        candidate = text[i : j + 1] if i != -1 and j > i else None
    if not candidate:
        return None
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        return None


class QAAgent:
    def __init__(self, index_name: str, client: Optional[LlamaClient] = None) -> None:
        self.prefix = build_repo_prefix(index_name)
        self.client = client or LlamaClient()
        self.retriever = Retriever(index_name)
        self.tools = RepoTools(self.retriever.root)

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

            if action in ("read_file", "grep", "list_dir"):
                obs = self.tools.dispatch(action, obj)
                summary = obj.get("path") or obj.get("pattern") or ""
                result.steps.append(f"{action}({summary})")
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": f"工具结果:\n{obs}\n\n请继续(JSON)。"})
            else:
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content": "动作无效,请输出合法 JSON 动作。"})

        # 迭代用尽:强制给出最终答案
        messages.append({"role": "user", "content": "请基于以上信息给出最终答案(纯文本,带 文件:行号 引用)。"})
        res = self.client.chat(messages, max_tokens=600, temperature=0.1, cache_prompt=True)
        result.answer = res.text.strip()
        result.last_cached_tokens = res.cached_tokens
        result.steps.append("final(强制)")
        return result
