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
def doc(
    name: str = typer.Argument(..., help="仓库名(已 index)"),
    api: bool = typer.Option(True, "--api/--no-api", help="是否生成 API 参考"),
    max_llm: int = typer.Option(60, "--max-llm", help="每批 LLM 补描述的调用上限"),
    complete: bool = typer.Option(False, "--complete", help="分批跑到全覆盖(外部 server,带缓存可续)"),
    managed: bool = typer.Option(False, "--managed", help="自管 llama-server:内存高则自动写盘+重启释放+续跑,直到全覆盖"),
    port: int = typer.Option(8080, "--port", help="受管 server 端口"),
    model: str = typer.Option(None, "--model", help="受管 server 用的 GGUF 路径(默认走脚本默认)"),
    ctx: int = typer.Option(8192, "--ctx", help="上下文长度(越小 KV 越省,内存越安全)"),
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
        doc_result = generate(name, progress=lambda m: console.print(m))

        api_pages = None
        if api:
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

        out = render(doc_result, api_pages=api_pages)
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


if __name__ == "__main__":
    app()
