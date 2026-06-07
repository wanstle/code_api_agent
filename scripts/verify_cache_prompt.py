"""验证 llama-server 的 cache_prompt 前缀缓存是否真的省下 prefill。

实验设计(对应项目核心机制"稳定前缀 + 可切换后缀"):
  - 构造一段长而稳定的「前缀」(放在 system 里,模拟"仓库概览")。
  - Round 1 (cold) :前缀 + 后缀A,cache_prompt=True → 填充缓存。
  - Round 2 (warm) :同一前缀 + 后缀B(模拟切 Skill)→ 应命中前缀 KV。
  - Round 3 (ctrl) :换一段不同前缀 → 不应命中,作为对照。

判据:Round 2 的服务端 prompt_ms 应显著低于 Round 1/3;cached_tokens 应接近前缀长度。
若服务端未返回 timings,则退回比较端到端时延。

用法:
  先启动 llama-server(见 scripts/serve_llama_*.sh),然后:
  .venv/bin/python -m scripts.verify_cache_prompt
"""

from __future__ import annotations

import sys

from rich.console import Console
from rich.table import Table

from inference.client import ChatResult, LlamaClient

console = Console()


def _build_prefix(repeat: int = 60) -> str:
    """造一段长而稳定的前缀(约数千 token),模拟仓库概览。"""
    para = (
        "本仓库是一个示例工程。以下是其文件地图与模块摘要的占位文本,"
        "用于测试前缀缓存:模块A负责解析,模块B负责索引,模块C负责推理,"
        "模块D负责技能切换,模块E负责文档生成,模块F负责问答。"
    )
    return "仓库概览(稳定前缀):\n" + "\n".join(f"{i}. {para}" for i in range(repeat))


def _row(name: str, r: ChatResult) -> list[str]:
    pm = r.prompt_ms
    ct = r.cached_tokens
    return [
        name,
        f"{r.latency_s*1000:.0f}",
        f"{pm:.0f}" if pm is not None else "—",
        str(ct) if ct is not None else "—",
        (r.text[:24] + "…") if len(r.text) > 24 else r.text,
    ]


def main() -> int:
    client = LlamaClient()
    console.print(f"[bold]目标 llama-server[/bold]: {client.config.base_url}")

    if not client.ping():
        console.print(
            "[red]无法连接 llama-server。[/red]请先启动它(见 "
            "scripts/serve_llama_cuda.sh 或 serve_llama_vulkan.sh),"
            "或用 LLAMA_BASE_URL 指定地址。"
        )
        return 1

    prefix = _build_prefix()
    prefix2 = _build_prefix(repeat=55) + "\n(这是一段不同的前缀,用于对照)"

    msgs = lambda pfx, suffix: [
        {"role": "system", "content": pfx},
        {"role": "user", "content": suffix},
    ]

    console.print("Round 1 (cold)  …")
    r1 = client.chat(msgs(prefix, "用一句话说明模块A的职责。"), max_tokens=32)
    console.print("Round 2 (warm)  …")
    r2 = client.chat(msgs(prefix, "用一句话说明模块B的职责。"), max_tokens=32)
    console.print("Round 3 (ctrl)  …")
    r3 = client.chat(msgs(prefix2, "用一句话说明模块C的职责。"), max_tokens=32)

    table = Table(title="cache_prompt 前缀缓存验证", header_style="bold")
    table.add_column("轮次")
    table.add_column("端到端(ms)", justify="right")
    table.add_column("prompt_ms(prefill)", justify="right")
    table.add_column("cached_tokens", justify="right")
    table.add_column("输出片段", style="dim")
    table.add_row(*_row("1 cold", r1))
    table.add_row(*_row("2 warm", r2))
    table.add_row(*_row("3 ctrl", r3))
    console.print(table)

    # 给个直观结论
    if r1.prompt_ms and r2.prompt_ms:
        speedup = r1.prompt_ms / r2.prompt_ms if r2.prompt_ms else float("inf")
        console.print(
            f"\n[bold green]结论[/bold green]:warm 轮 prefill 比 cold 轮快 "
            f"约 [bold]{speedup:.1f}×[/bold]({r1.prompt_ms:.0f}ms → {r2.prompt_ms:.0f}ms)"
            f"。说明前缀 KV 被复用 ✅"
        )
    else:
        console.print(
            "\n[yellow]服务端未返回 timings[/yellow],改看端到端时延:"
            f"cold {r1.latency_s*1000:.0f}ms vs warm {r2.latency_s*1000:.0f}ms。"
            "(建议升级 llama.cpp 以获得 timings 字段)"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
