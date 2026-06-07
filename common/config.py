"""集中读取运行配置(从环境变量,带合理默认值)。

离线部署时通过环境变量覆盖即可,无需改代码。
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class LlamaConfig:
    base_url: str   # llama-server 的 OpenAI 兼容地址,需带 /v1
    model: str      # 模型名(llama-server 单模型时随意填,占位即可)
    api_key: str    # llama-server 不校验,占位即可

    @staticmethod
    def from_env() -> "LlamaConfig":
        return LlamaConfig(
            base_url=os.environ.get("LLAMA_BASE_URL", "http://127.0.0.1:8080/v1"),
            model=os.environ.get("LLAMA_MODEL", "local-model"),
            api_key=os.environ.get("LLAMA_API_KEY", "sk-no-key-required"),
        )
