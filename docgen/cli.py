"""docgen 命令行入口。

    python -m docgen.cli gen <repo-name>
然后:  mkdocs serve -f docs/<repo>/mkdocs.yml   （需 pip install mkdocs-material）
"""

from __future__ import annotations

import typer
from rich.console import Console

from docgen.render import render
from docgen.summarize import generate

app = typer.Typer(add_completion=False, help="文档生成:map-reduce 摘要 → MkDocs")
console = Console()


@app.command()
def gen(name: str = typer.Argument(..., help="仓库名(已 build 过索引)")) -> None:
    console.print(f"[bold]生成文档[/bold]: {name}")
    doc = generate(name, progress=lambda m: console.print(m))
    out = render(doc)
    console.print(f"[green]文档已生成[/green] → {out}")
    console.print(f"预览: [bold]mkdocs serve -f {out}/mkdocs.yml[/bold]  (需 mkdocs-material)")


if __name__ == "__main__":
    app()
