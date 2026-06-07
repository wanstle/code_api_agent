"""LLM 客户端:封装 llama-server 的 OpenAI 兼容接口。

只暴露一个 chat() 方法,返回文本 + 时延 + 服务端 timings(若有)。
timings 用于 D3 验证 KV cache(cache_prompt)是否真的省下了 prefill。
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Optional

from openai import OpenAI

from common.config import LlamaConfig


@dataclass
class ChatResult:
    text: str
    latency_s: float                 # 客户端测得的端到端时延
    timings: Optional[dict] = None   # llama-server 返回的 timings(prompt_ms 等)
    usage: Optional[dict] = None
    raw: Optional[dict] = None

    @property
    def prompt_ms(self) -> Optional[float]:
        """服务端 prefill 耗时(ms)。能直接反映前缀缓存是否命中。"""
        if self.timings:
            return self.timings.get("prompt_ms")
        return None

    @property
    def cached_tokens(self) -> Optional[int]:
        """被缓存复用的 token 数(llama-server 在 timings/usage 里给)。"""
        if self.timings and "cache_n" in self.timings:
            return self.timings.get("cache_n")
        if self.usage:
            # OpenAI 风格:prompt_tokens_details.cached_tokens
            details = self.usage.get("prompt_tokens_details") or {}
            return details.get("cached_tokens")
        return None


class LlamaClient:
    def __init__(self, config: Optional[LlamaConfig] = None) -> None:
        self.config = config or LlamaConfig.from_env()
        self._client = OpenAI(base_url=self.config.base_url, api_key=self.config.api_key)

    def chat(
        self,
        messages: list[dict[str, str]],
        *,
        max_tokens: int = 256,
        temperature: float = 0.0,
        cache_prompt: bool = True,
        **extra: Any,
    ) -> ChatResult:
        """发一轮对话。

        cache_prompt=True 让 llama-server 复用最长公共前缀的 KV(项目核心机制)。
        """
        extra_body = {"cache_prompt": cache_prompt, **extra}

        t0 = time.perf_counter()
        # with_raw_response 拿原始 JSON,以便读取 llama-server 的非标准字段 timings。
        raw_resp = self._client.chat.completions.with_raw_response.create(
            model=self.config.model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            extra_body=extra_body,
        )
        latency = time.perf_counter() - t0

        data = raw_resp.parse().to_dict()
        text = ""
        if data.get("choices"):
            text = data["choices"][0].get("message", {}).get("content", "") or ""

        return ChatResult(
            text=text,
            latency_s=latency,
            timings=data.get("timings"),
            usage=data.get("usage"),
            raw=data,
        )

    def ping(self) -> bool:
        """轻量探活:返回 True 表示 llama-server 可达且能出 token。"""
        try:
            r = self.chat([{"role": "user", "content": "ping"}], max_tokens=1)
            return isinstance(r.text, str)
        except Exception:
            return False
