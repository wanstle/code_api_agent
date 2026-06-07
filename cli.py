"""RepoLens 统一命令行入口(G. Serving / 编排)。

    python -m cli index <repo-url-or-path>      # 解析 + 建索引(D1+D2)
    python -m cli doc   <repo-name>             # 生成 MkDocs 文档(D4)
    python -m cli ask   <repo-name> "问题"      # qa Agent 工具循环问答(D5)
    python -m cli skill <repo-name> <skill> [任务]   # 跑指定 Skill(D3)

所有子命令对接 llama-server 的 OpenAI 接口(开发机 CUDA/Vulkan、部署机 Vulkan 通用)。
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

app = typer.Typer(add_completion=False, help="RepoLens:大型仓库分析 / 文档生成 / 问答")
console = Console()


@app.command()
def index(source: str = typer.Argument(..., help="git URL 或本地目录")) -> None:
    """解析仓库并构建向量+符号索引。"""
    from indexing.builder import build_index

    build_index(source, progress=lambda m: console.print(f"  {m}"))


@app.command()
def doc(name: str = typer.Argument(..., help="仓库名(已 index)")) -> None:
    """map-reduce 生成文档站(MkDocs)。"""
    from docgen.render import render
    from docgen.summarize import generate

    out = render(generate(name, progress=lambda m: console.print(m)))
    console.print(f"[green]文档[/green] → {out} · 预览: mkdocs serve -f {out}/mkdocs.yml")


@app.command()
def ask(
    name: str = typer.Argument(..., help="仓库名"),
    question: str = typer.Argument(..., help="问题"),
    k: int = typer.Option(5, "--k"),
) -> None:
    """qa Agent 工具循环问答(带 file:line 引用)。"""
    from qa.agent import QAAgent

    res = QAAgent(name).ask(question, k=k)
    console.print(f"[dim]轨迹:[/dim] {' → '.join(res.steps)}")
    console.print(Panel(Markdown(res.answer), title="回答", title_align="left"))


@app.command()
def skill(
    name: str = typer.Argument(..., help="仓库名"),
    skill_name: str = typer.Argument(..., help="architecture/frontend/backend/qa"),
    task: str = typer.Argument("生成该部分的分析", help="任务"),
) -> None:
    """运行指定 Skill。"""
    from skills.session import SkillSession

    res = SkillSession(name).run(skill_name, task, max_tokens=700)
    console.print(Panel(Markdown(res.text), title=f"Skill: {skill_name}", title_align="left"))


if __name__ == "__main__":
    app()
