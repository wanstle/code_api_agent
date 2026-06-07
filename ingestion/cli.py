"""ingestion 的命令行入口。

用法:
    python -m ingestion.cli analyze <repo-url-or-path> [--out repomap.json]

产出 D1 里程碑要求的:文件树概览 + 函数/类清单。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from common.models import RepoMap
from ingestion.clone import prepare_repo
from ingestion.filetree import scan_files
from ingestion.parse import parse_repo

app = typer.Typer(add_completion=False, help="仓库解析(clone → 文件树 → tree-sitter)")
console = Console()


@app.command()
def analyze(
    source: str = typer.Argument(..., help="git URL 或本地目录路径"),
    out: Optional[Path] = typer.Option(None, "--out", help="把 RepoMap 导出为 JSON"),
    symbols: int = typer.Option(20, "--symbols", help="清单里展示多少个符号示例"),
) -> None:
    """解析一个仓库,打印概览并(可选)导出 JSON。"""
    console.print(f"[bold]准备仓库[/bold]: {source}")
    root = prepare_repo(source)
    console.print(f"  本地路径: {root}")

    console.print("[bold]扫描文件树[/bold] …")
    files = scan_files(root)
    console.print(f"  收录代码文件: {len(files)}")

    console.print("[bold]tree-sitter 解析[/bold] …")
    repo = parse_repo(root, files)

    _print_overview(repo)
    _print_symbol_sample(repo, limit=symbols)

    if out is not None:
        out.write_text(json.dumps(repo.to_dict(), ensure_ascii=False, indent=2), "utf-8")
        console.print(f"\n[green]已导出[/green] RepoMap → {out}")


def _print_overview(repo: RepoMap) -> None:
    console.print(f"\n[bold cyan]仓库概览: {repo.name}[/bold cyan]")
    console.print(
        f"  文件 {repo.num_files} · 符号 {repo.num_symbols} · 代码行 {repo.total_lines}"
    )

    table = Table(title="语言分布", show_header=True, header_style="bold")
    table.add_column("语言")
    table.add_column("文件数", justify="right")
    for lang, n in repo.language_breakdown().items():
        table.add_row(lang, str(n))
    console.print(table)


def _print_symbol_sample(repo: RepoMap, limit: int) -> None:
    table = Table(title=f"函数/类清单(前 {limit} 个)", show_header=True, header_style="bold")
    table.add_column("种类")
    table.add_column("名称")
    table.add_column("位置 (file:line)", style="dim")

    shown = 0
    for fi in repo.files:
        for sym in fi.symbols:
            if shown >= limit:
                break
            qualified = f"{sym.parent}.{sym.name}" if sym.parent else sym.name
            table.add_row(sym.kind, qualified, sym.location())
            shown += 1
        if shown >= limit:
            break
    console.print(table)


if __name__ == "__main__":
    app()
