"""indexing 的命令行入口。

用法:
    python -m indexing.cli build <repo-url-or-path>
    python -m indexing.cli query <repo-name> "如何解析命令行参数?"  [--k 8]
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel

from indexing.builder import build_index
from indexing.retrieve import Retriever

app = typer.Typer(add_completion=False, help="索引层:构建索引 / 检索代码片段")
console = Console()


@app.command()
def build(source: str = typer.Argument(..., help="git URL 或本地目录")) -> None:
    """对仓库构建向量索引 + 符号索引。"""
    build_index(source, progress=lambda m: console.print(f"  {m}"))


@app.command()
def query(
    name: str = typer.Argument(..., help="仓库名(build 时的目录名)"),
    question: str = typer.Argument(..., help="自然语言问题或符号名"),
    k: int = typer.Option(8, "--k", help="返回 top-k"),
) -> None:
    """检索 top-k 相关代码片段。"""
    r = Retriever(name)
    hits = r.retrieve(question, k=k)
    console.print(f"[bold]查询[/bold]: {question}  ([dim]{len(hits)} 命中[/dim])\n")
    for i, h in enumerate(hits, 1):
        head = f"[{i}] {h.kind} [bold]{h.name}[/bold]  {h.location()}  " \
               f"[dim]({h.source}, score={h.score})[/dim]"
        body = "\n".join(h.text.splitlines()[:18])
        console.print(Panel(body, title=head, title_align="left"))


if __name__ == "__main__":
    app()
