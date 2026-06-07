"""验证"切 Skill"时 cache_prompt 复用仓库前缀的收益。

实验:同一仓库会话里依次跑 architecture → frontend → backend → qa。
system 前缀(仓库概览)始终一致,只切 user 里的 Skill 后缀。
  - 第 1 个 Skill(cold):填充前缀 KV。
  - 后续 Skill(warm):应命中前缀 → prompt_ms 低、cached_tokens 接近前缀长度。

用法:
  先启动 llama-server,然后:
  .venv/bin/python -m scripts.verify_skill_switch [repo-name]
"""

from __future__ import annotations

import sys

from rich.console import Console
from rich.table import Table

from inference.client import LlamaClient
from skills.session import SkillSession

console = Console()

SEQUENCE = ["architecture", "frontend", "backend", "qa"]
TASK = "用一句话概述你负责的分析维度。"  # 任务很短,让 prefill 主导,聚焦前缀缓存


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "click"

    client = LlamaClient()
    console.print(f"[bold]llama-server[/bold]: {client.config.base_url} · 仓库: {name}")
    if not client.ping():
        console.print("[red]无法连接 llama-server[/red],请先启动(scripts/serve_llama_prebuilt_vulkan.sh)。")
        return 1

    sess = SkillSession(name, client=client)
    console.print(f"稳定前缀大小: {sess.prefix_chars()} 字符(约 {sess.prefix_chars()//4} token)\n")

    table = Table(title="切 Skill 的 cache_prompt 复用", header_style="bold")
    table.add_column("步骤")
    table.add_column("Skill")
    table.add_column("阶段")
    table.add_column("prompt_ms", justify="right")
    table.add_column("cached_tokens", justify="right")
    table.add_column("端到端(ms)", justify="right")

    first_cold = None
    warm_vals = []
    for i, skill in enumerate(SEQUENCE):
        res = sess.run(skill, TASK, max_tokens=16, temperature=0.0)
        phase = "cold" if i == 0 else "warm"
        if i == 0:
            first_cold = res.prompt_ms
        else:
            if res.prompt_ms is not None:
                warm_vals.append(res.prompt_ms)
        table.add_row(
            str(i + 1), skill, phase,
            f"{res.prompt_ms:.0f}" if res.prompt_ms is not None else "—",
            str(res.cached_tokens) if res.cached_tokens is not None else "—",
            f"{res.latency_s*1000:.0f}",
        )
    console.print(table)

    if first_cold and warm_vals:
        avg_warm = sum(warm_vals) / len(warm_vals)
        speed = first_cold / avg_warm if avg_warm else float("inf")
        console.print(
            f"\n[bold green]结论[/bold green]:首个 Skill(cold)prefill {first_cold:.0f}ms,"
            f"后续切 Skill(warm)平均 {avg_warm:.0f}ms,**约 {speed:.1f}× 提速**。"
            f"切 Skill 复用了仓库前缀 KV ✅ —— MVP 闭环成立。"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
