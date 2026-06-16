"""Chainlit 问答演示界面(D7 demo)。

启动:
    REPO=click chainlit run app.py        # 需 pip install chainlit
然后浏览器问关于该仓库的问题,会展示工具调用轨迹 + 带 file:line 的答案。

只读、本地运行;对接已 build 的索引与本地 llama-server。
"""

from __future__ import annotations

import json
import os

import chainlit as cl

from qa.agent import QAAgent

REPO = os.environ.get("REPO", "click")


def _display_answer(text: str) -> str:
    """Render only the user-facing Markdown if a final JSON object leaks through."""
    raw = (text or "").strip()
    if raw.startswith("{"):
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            return raw
        if isinstance(obj, dict) and obj.get("action") == "final" and obj.get("answer"):
            return str(obj["answer"]).strip()
    return raw


@cl.on_chat_start
async def start() -> None:
    try:
        agent = QAAgent(REPO)
    except Exception as e:  # 索引不存在 / 服务未起
        await cl.Message(content=f"初始化失败:{e}\n请先 `python -m cli index <repo>` 并启动 llama-server。").send()
        return
    cl.user_session.set("agent", agent)
    files = agent.retriever.meta.get("files", [])
    shown = "\n".join(f"- `{f['path']}`" for f in files[:12])
    more = f"\n- ... 还有 {len(files) - 12} 个文件" if len(files) > 12 else ""
    root = agent.retriever.meta.get("root", "(unknown)")
    await cl.Message(
        content=(
            f"已加载仓库 **{REPO}**(前缀 {len(agent.prefix)} 字符)。\n\n"
            f"**本地源码根目录**: `{root}`\n\n"
            f"**索引文件节选**:\n{shown}{more}\n\n"
            "源码页已隐藏在导航和搜索之外，但 API 详情页的 `来源` 链接仍可跳到真实文件行号；"
            "当前聊天会保留最近几轮问答用于理解追问。"
        )
    ).send()


@cl.on_message
async def on_message(msg: cl.Message) -> None:
    agent: QAAgent = cl.user_session.get("agent")
    if agent is None:
        await cl.Message(content="未初始化,请刷新。").send()
        return

    # 工具循环是阻塞的,放到线程里跑,避免卡住事件循环。
    res = await cl.make_async(agent.ask)(msg.content)

    # 展示工具调用轨迹
    async with cl.Step(name="工具调用轨迹") as step:
        step.output = " → ".join(res.steps) or "(直接作答)"

    await cl.Message(
        content=_display_answer(res.answer)
        + f"\n\n---\n*迭代 {res.iters} 轮 · 前缀复用 cached_tokens={res.last_cached_tokens}*"
    ).send()
