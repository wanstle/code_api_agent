"""skills 的命令行入口(D3 MVP 闭环的对外操作)。

    python -m skills.cli ask <repo-name> "登录接口在哪、前端怎么调?"   # qa + 检索
    python -m skills.cli run <repo-name> architecture "生成架构总览"     # 跑任意 Skill
    python -m skills.cli prefix <repo-name>                              # 查看稳定前缀
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from indexing.retrieve import Retriever
from skills.session import SkillSession

app = typer.Typer(add_completion=False, help="Skill 框架:切换分析能力 + 问答")
console = Console()

_SNIPPET_LINES = 30


def _format_context(hits) -> str:
    blocks = []
    for h in hits:
        body = "\n".join(h.text.splitlines()[:_SNIPPET_LINES])
        blocks.append(f"### {h.name}  ({h.location()})\n```\n{body}\n```")
    return "\n\n".join(blocks)


@app.command()
def ask(
    name: str = typer.Argument(..., help="仓库名"),
    question: str = typer.Argument(..., help="问题"),
    k: int = typer.Option(6, "--k", help="检索 top-k 作为种子上下文"),
) -> None:
    """问答:D2 检索拿种子片段 → qa Skill 回答(带引用)。"""
    hits = Retriever(name).retrieve(question, k=k)
    context = _format_context(hits)
    console.print(f"[dim]检索到 {len(hits)} 段片段作为上下文[/dim]")

    sess = SkillSession(name)
    res = sess.run("qa", question, context=context, max_tokens=512)

    console.print(Panel(Markdown(res.text), title="回答", title_align="left"))
    console.print(
        f"[dim]前缀 {sess.prefix_chars()} 字符 · prompt_ms={res.prompt_ms} · "
        f"cached_tokens={res.cached_tokens} · 端到端 {res.latency_s*1000:.0f}ms[/dim]"
    )
    console.print("[dim]来源:[/dim] " + ", ".join(h.location() for h in hits))


@app.command()
def run(
    name: str = typer.Argument(..., help="仓库名"),
    skill: str = typer.Argument(..., help="skill 名:architecture/frontend/backend/qa"),
    task: str = typer.Argument("生成该部分的分析文档", help="任务描述"),
) -> None:
    """运行指定 Skill(模板型文档生成)。"""
    sess = SkillSession(name)
    res = sess.run(skill, task, max_tokens=700)
    console.print(Panel(Markdown(res.text), title=f"Skill: {skill}", title_align="left"))
    console.print(
        f"[dim]prompt_ms={res.prompt_ms} · cached_tokens={res.cached_tokens} · "
        f"端到端 {res.latency_s*1000:.0f}ms[/dim]"
    )


@app.command()
def prefix(name: str = typer.Argument(..., help="仓库名")) -> None:
    """打印该仓库的稳定前缀(供检查 token 稳定性/大小)。"""
    from skills.prefix import build_repo_prefix

    p = build_repo_prefix(name)
    console.print(p)
    console.print(f"\n[dim]前缀长度: {len(p)} 字符(约 {len(p)//4} token)[/dim]")


if __name__ == "__main__":
    app()
