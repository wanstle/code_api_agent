"""qa Agent 命令行入口。

    python -m qa.cli <repo-name> "用户登录的接口在哪、前端怎么调?"
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from qa.agent import DEFAULT_SEED_K, MAX_ITERS, QAAgent

app = typer.Typer(add_completion=False, help="qa Agent:工具循环问答")
console = Console()


@app.command()
def ask(
    name: str = typer.Argument(..., help="仓库名"),
    question: str = typer.Argument(..., help="问题"),
    k: int = typer.Option(DEFAULT_SEED_K, "--k"),
    max_iters: int = typer.Option(MAX_ITERS, "--max-iters"),
) -> None:
    agent = QAAgent(name)
    res = agent.ask(question, k=k, max_iters=max_iters)
    console.print(f"[dim]工具调用轨迹:[/dim] {' → '.join(res.steps)}")
    console.print(Panel(Markdown(res.answer), title="回答", title_align="left"))
    console.print(
        f"[dim]迭代 {res.iters} 轮 · 前缀 {res.prefix_chars} 字符 · "
        f"last cached_tokens={res.last_cached_tokens}[/dim]"
    )


if __name__ == "__main__":
    app()
