"""SkillSession:在同一仓库上下文里切换 Skill。

整个会话期间 system 前缀(仓库概览)保持**完全一致**,只切换 user 里的
Skill 后缀与任务 —— 这正是 cache_prompt 复用前缀 KV 的前提。
"""

from __future__ import annotations

from typing import Optional

from inference.client import ChatResult, LlamaClient
from skills.base import Skill, get
from skills.prefix import build_repo_prefix


class SkillSession:
    def __init__(self, index_name: str, client: Optional[LlamaClient] = None) -> None:
        self.index_name = index_name
        self.prefix = build_repo_prefix(index_name)   # 构建一次,全程复用
        self.client = client or LlamaClient()

    def run(
        self,
        skill_name: str,
        task: str,
        context: str = "",
        *,
        max_tokens: int = 512,
        temperature: float = 0.2,
    ) -> ChatResult:
        skill: Skill = get(skill_name)
        messages = [
            {"role": "system", "content": self.prefix},          # 稳定前缀 → 缓存命中
            {"role": "user", "content": skill.build_user_message(task, context)},  # 可切换后缀
        ]
        return self.client.chat(
            messages,
            max_tokens=max_tokens,
            temperature=temperature,
            cache_prompt=True,
        )

    def prefix_chars(self) -> int:
        return len(self.prefix)
