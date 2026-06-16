"""indexing 的命令行入口。

用法:
    python -m indexing.cli build <repo-url-or-path>
    python -m indexing.cli query <repo-name> "如何解析命令行参数?"  [--k 8]
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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


@app.command("eval")
def eval_retrieval(
    name: str = typer.Argument(..., help="仓库名(build 时的目录名)"),
    cases: str = typer.Option(None, "--cases", help="JSON case 文件; click 可省略使用内置样例"),
    k: int = typer.Option(5, "--k", help="每题检索 top-k"),
) -> None:
    """不调用 LLM 的 retrieval eval:检查 expected file/symbol 是否进入 top-k。"""
    from indexing.eval_retrieval import run_retrieval_eval

    res = run_retrieval_eval(name, cases_path=cases, k=k)
    table = Table(title=f"Retrieval Eval · {name} · top-{k}")
    table.add_column("Query")
    table.add_column("File", justify="center")
    table.add_column("Symbol", justify="center")
    table.add_column("Top hit")
    for row in res["cases"]:
        top = row["top"][0] if row["top"] else {}
        top_label = f"{top.get('name', '')} @ {top.get('file', '')}:{top.get('start_line', '')}"
        table.add_row(
            row["query"][:48],
            "[green]OK[/green]" if row["file_ok"] else "[red]MISS[/red]",
            "[green]OK[/green]" if row["symbol_ok"] else "[red]MISS[/red]",
            top_label[:72],
        )
    console.print(table)
    console.print(
        f"file_hit_rate={res['file_hit_rate']:.0%} "
        f"symbol_hit_rate={res['symbol_hit_rate']:.0%} ({res['total']} cases)"
    )


if __name__ == "__main__":
    app()
