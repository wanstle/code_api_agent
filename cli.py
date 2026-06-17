"""RepoLens 统一命令行入口(G. Serving / 编排)。

    python -m cli index <repo-url-or-path>      # 解析 + 建索引(D1+D2)
    python -m cli lens  <repo-name>             # 生成模块分析视角 lenses.json
    python -m cli doc   <repo-name> --use-lens  # 带 lens 生成 MkDocs 文档(D4)
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
def doc(
    name: str = typer.Argument(..., help="仓库名(已 index)"),
    api: bool = typer.Option(True, "--api/--no-api", help="是否生成 API 参考"),
    max_llm: int = typer.Option(60, "--max-llm", help="每批 LLM 补描述的调用上限"),
    complete: bool = typer.Option(False, "--complete", help="分批跑到全覆盖(外部 server,带缓存可续)"),
    managed: bool = typer.Option(False, "--managed", help="自管 llama-server:内存高则自动写盘+重启释放+续跑,直到全覆盖"),
    port: int = typer.Option(8080, "--port", help="受管 server 端口"),
    model: str = typer.Option(None, "--model", help="受管 server 用的 GGUF 路径(默认走脚本默认)"),
    ctx: int = typer.Option(8192, "--ctx", help="上下文长度(越小 KV 越省,内存越安全)"),
    use_lens: bool = typer.Option(False, "--use-lens", help="模块文档注入各模块 lens(需先 cli lens 生成)"),
    modules_only: bool = typer.Option(False, "--modules-only", help="重新生成 Architecture/Modules,保留现有 Detailed API,跳过 API LLM 生成"),
    nav_subfolders: bool = typer.Option(True, "--nav-subfolders/--no-nav-subfolders", help="左侧导航是否按一级子目录分组;开启后可手动展开/收起各 subfolder"),
) -> None:
    """生成文档站(MkDocs):架构总览(map-reduce)+ API 参考(抽取优先)。

    API 参考带持久化缓存(增量存盘)。安全闭环(--managed):内存逼近阈值时
    先写盘保存进度 → 重启 server 释放内存 → 自动续下一轮,直到全覆盖。
    """
    from docgen.render import render
    from docgen.summarize import generate

    server = None
    if managed:
        import os
        from inference.server import LlamaServer
        env = {"CTX": str(ctx), "SLOTS": "1"}   # 保守:单槽 + 受控上下文,内存有界
        if model:
            env["MODEL"] = model
        # 让客户端命中受管 server 的端口
        os.environ["LLAMA_BASE_URL"] = f"http://127.0.0.1:{port}/v1"
        server = LlamaServer(port=port, env=env)
        console.print(f"[dim]启动受管 llama-server(ctx={ctx}, slots=1)…[/dim]")
        server.start()

    try:
        doc_result = generate(
            name,
            progress=lambda m: console.print(m),
            use_lens=use_lens,
        )

        api_pages = None
        if api and not modules_only:
            from docgen.apidoc import generate_api
            from docgen.apidoc_render import render_all

            loop = complete or managed
            prev_pending = None
            res = None
            while True:
                res = generate_api(name, max_llm=max_llm, progress=lambda m: console.print(m))
                if res.pending == 0 or not loop:
                    break
                if prev_pending is not None and res.pending >= prev_pending:
                    console.print("[yellow]本批待生成数未下降,停止续跑以避免重复生成。已保存进度,稍后可重试。[/yellow]")
                    break
                prev_pending = res.pending
                if managed and res.status in ("lowmem", "error"):
                    console.print(f"[yellow]触发 {res.status}:写盘已完成,重启 server 释放内存后续跑(还剩 {res.pending})…[/yellow]")
                    server.restart()
                else:
                    console.print(f"[dim]还剩 {res.pending},继续下一批…[/dim]")
            api_pages = render_all(res.by_module, res.by_key)

        out = render(
            doc_result,
            api_pages=api_pages,
            nav_subfolders=nav_subfolders,
            preserve_existing_api=modules_only,
        )
        console.print(f"[green]文档[/green] → {out} · 预览: mkdocs serve -f {out}/mkdocs.yml")
    finally:
        if server is not None:
            console.print("[dim]停止受管 server,释放内存。[/dim]")
            server.stop()


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


def _print_lenses(lenses: dict) -> None:
    if not lenses:
        console.print("[yellow]还没有 lenses(先生成)。[/yellow]")
        return
    for mod, l in lenses.items():
        tag = {"ai": "AI", "human": "人工", "fallback": "待补", "low-signal": "低信号"}.get(l.source, l.source)
        console.print(f"\n[bold cyan]{mod}[/bold cyan]  [dim]({tag})[/dim]")
        console.print(f"  [bold]role[/bold]: {l.role}")
        if l.focus:
            console.print("  [bold]focus[/bold]:")
            for f in l.focus:
                console.print(f"    • {f}")
        if l.sections:
            console.print(f"  [bold]sections[/bold]: {' · '.join(l.sections)}")


@app.command()
def lens(
    name: str = typer.Argument(..., help="仓库名(已 index)"),
    show: bool = typer.Option(False, "--show", help="只展示已有 lenses,不生成"),
    force: bool = typer.Option(False, "--force", help="重新生成(会覆盖人工修改)"),
    max_llm: int = typer.Option(50, "--max-llm", help="本次生成上限"),
    managed: bool = typer.Option(False, "--managed", help="自管 llama-server(内存安全)"),
    model: str = typer.Option(None, "--model", help="受管 server 的 GGUF 路径"),
    ctx: int = typer.Option(8192, "--ctx"),
    port: int = typer.Option(8080, "--port"),
) -> None:
    """生成/查看模块分析视角(lens)→ 写入 lenses.json 供人工 review/编辑(不生成文档)。"""
    from docgen.lens import generate_lenses, load_lenses, lenses_path

    if show:
        _print_lenses(load_lenses(name))
        return

    server = None
    if managed:
        import os
        from inference.server import LlamaServer
        env = {"CTX": str(ctx), "SLOTS": "1"}
        if model:
            env["MODEL"] = model
        os.environ["LLAMA_BASE_URL"] = f"http://127.0.0.1:{port}/v1"
        server = LlamaServer(port=port, env=env)
        console.print(f"[dim]启动受管 llama-server(ctx={ctx}, slots=1)…[/dim]")
        server.start()
    try:
        lenses = generate_lenses(name, max_llm=max_llm, force=force, progress=lambda m: console.print(m))
        _print_lenses(lenses)
        console.print(f"\n[green]可编辑[/green]: .cache/index/{name}/lenses.json  "
                      f"(改完直接用于后续文档生成;重跑默认保留你的修改,除非 --force)")
    finally:
        if server is not None:
            console.print("[dim]停止受管 server。[/dim]")
            server.stop()


@app.command("retrieval-eval")
def retrieval_eval(
    name: str = typer.Argument(..., help="仓库名(已 index)"),
    cases: str = typer.Option(None, "--cases", help="JSON case 文件; click 可省略使用内置样例"),
    k: int = typer.Option(5, "--k", help="每题检索 top-k"),
) -> None:
    """不调用 LLM 的检索质量评测。"""
    from rich.table import Table
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
