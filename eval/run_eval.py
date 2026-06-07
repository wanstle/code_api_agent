"""端到端评测:对一组已知答案的问题跑 qa Agent,检查答案是否引对了文件。

判据(轻量、可自动化):答案文本或工具轨迹中是否出现期望的文件名子串。
用法:
  .venv/bin/python -m eval.run_eval [repo-name]
"""

from __future__ import annotations

import sys
import time

from rich.console import Console
from rich.table import Table

from inference.client import LlamaClient
from qa.agent import QAAgent

console = Console()

# (问题, 期望出现的文件子串之一)
CASES_CLICK = [
    ("Where is the Option class defined?", ["core.py"]),
    ("Which file parses command line arguments into options?", ["parser.py", "core.py"]),
    ("How is a progress bar implemented?", ["termui.py"]),
    ("Where are the exception classes defined?", ["exceptions.py"]),
    ("Where is shell completion implemented?", ["shell_completion.py"]),
]


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "click"
    if not LlamaClient().ping():
        console.print("[red]llama-server 不可达[/red],先启动服务。")
        return 1

    agent = QAAgent(name)
    table = Table(title=f"qa Agent 评测 · {name}", header_style="bold")
    table.add_column("问题")
    table.add_column("期望文件")
    table.add_column("结果", justify="center")
    table.add_column("轮", justify="right")
    table.add_column("耗时(s)", justify="right")

    passed = 0
    for q, expects in CASES_CLICK:
        t0 = time.perf_counter()
        res = agent.ask(q, k=4, max_iters=5)
        dt = time.perf_counter() - t0
        haystack = (res.answer + " " + " ".join(res.steps)).lower()
        ok = any(e.lower() in haystack for e in expects)
        passed += ok
        table.add_row(
            q[:42], "/".join(expects),
            "[green]✓[/green]" if ok else "[red]✗[/red]",
            str(res.iters), f"{dt:.1f}",
        )
    console.print(table)
    console.print(f"\n[bold]通过率: {passed}/{len(CASES_CLICK)} = {passed/len(CASES_CLICK)*100:.0f}%[/bold]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
