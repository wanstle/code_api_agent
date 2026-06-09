"""可视化 Demo:一个 Gradio 应用,两个标签页。

  📖 文档浏览:浏览已生成的架构总览 / 模块 / API 参考(静态 markdown,无需服务)。
  💬 仓库问答:对仓库提问,展示工具调用轨迹 + 带 file:line 引用的答案(需 llama-server)。

启动:  .venv/bin/python demo.py        (或 scripts/run_demo.sh 一键起服务+界面)
"""

from __future__ import annotations

from pathlib import Path

import gradio as gr

DOCS_BASE = Path("docs")
_agents: dict = {}   # repo -> QAAgent(惰性创建并缓存)


# ---------------- 文档浏览 ----------------
def list_repos() -> list[str]:
    if not DOCS_BASE.exists():
        return []
    return sorted(p.name for p in DOCS_BASE.iterdir() if (p / "index.md").exists())


def _heading(md_path: Path) -> str:
    try:
        for line in md_path.read_text("utf-8").splitlines():
            if line.startswith("#"):
                return line.lstrip("#").strip()
    except OSError:
        pass
    return md_path.stem


def list_pages(repo: str) -> list[tuple[str, str]]:
    """返回 [(显示标签, 相对 docs/<repo> 的路径)],分组:架构 / 模块 / API。"""
    root = DOCS_BASE / repo
    pages: list[tuple[str, str]] = []
    if (root / "index.md").exists():
        pages.append(("📐 架构总览", "index.md"))
    for sub, icon in (("modules", "📦 模块"), ("api", "🔧 API")):
        d = root / sub
        if d.is_dir():
            for f in sorted(d.glob("*.md")):
                pages.append((f"{icon}: {_heading(f)}", f"{sub}/{f.name}"))
    return pages


def render_page(repo: str, rel: str) -> str:
    if not repo or not rel:
        return "_请选择页面_"
    p = DOCS_BASE / repo / rel
    try:
        return p.read_text("utf-8")
    except OSError:
        return f"_无法读取 {p}_"


def on_repo_change(repo: str):
    pages = list_pages(repo)
    choices = [(label, rel) for label, rel in pages]
    first = choices[0][1] if choices else None
    return gr.update(choices=choices, value=first), render_page(repo, first) if first else ""


# ---------------- 问答 ----------------
def _get_agent(repo: str):
    if repo not in _agents:
        from qa.agent import QAAgent
        _agents[repo] = QAAgent(repo)
    return _agents[repo]


def respond(message: str, history: list, repo: str):
    history = history or []
    if not message.strip():
        return "", history
    history.append({"role": "user", "content": message})
    try:
        agent = _get_agent(repo)
        res = agent.ask(message)
        traj = " → ".join(res.steps) or "(直接作答)"
        content = res.answer + f"\n\n---\n🛠️ *工具轨迹: {traj}*"
    except Exception as e:
        content = (f"⚠️ 出错:{type(e).__name__}: {e}\n\n"
                   f"请确认已启动 llama-server(scripts/serve_llama_prebuilt_vulkan.sh)"
                   f"且已对该仓库建索引。")
    history.append({"role": "assistant", "content": content})
    return "", history


# ---------------- 界面 ----------------
def build() -> gr.Blocks:
    repos = list_repos()
    default_repo = repos[0] if repos else None
    init_pages = list_pages(default_repo) if default_repo else []
    init_rel = init_pages[0][1] if init_pages else None

    with gr.Blocks(title="RepoLens — 仓库分析 Demo") as demo:
        gr.Markdown("# 🔎 RepoLens —— 大型仓库分析 Demo\n离线 · 代码解读 / API 文档 / 问答")

        with gr.Tabs():
            # 文档浏览
            with gr.Tab("📖 文档浏览"):
                with gr.Row():
                    repo_dd = gr.Dropdown(repos, value=default_repo, label="仓库", scale=1)
                    page_dd = gr.Dropdown(
                        [(l, r) for l, r in init_pages], value=init_rel, label="页面", scale=3
                    )
                doc_md = gr.Markdown(render_page(default_repo, init_rel) if init_rel else "_无文档_")
                repo_dd.change(on_repo_change, repo_dd, [page_dd, doc_md])
                page_dd.change(render_page, [repo_dd, page_dd], doc_md)

            # 问答
            with gr.Tab("💬 仓库问答"):
                qa_repo = gr.Dropdown(repos, value=default_repo, label="提问的仓库")
                chatbot = gr.Chatbot(height=460, label="问答(带 file:line 引用)")
                msg = gr.Textbox(placeholder="例如:Where is the Option class defined and what does parse_args do?",
                                 label="问题", submit_btn=True)
                gr.Examples(
                    ["Where is the Option class defined?",
                     "How does it parse command line options into parameter values?",
                     "What does the ProgressBar.update() method do?"],
                    inputs=msg,
                )
                msg.submit(respond, [msg, chatbot, qa_repo], [msg, chatbot])
    return demo


if __name__ == "__main__":
    build().launch(server_name="0.0.0.0", server_port=7860, theme=gr.themes.Soft())
