"""Skill 抽象 + 注册表。

Skill 分两类(见 README 2.1):
  - 模板型(architecture/frontend/backend):喂上下文 → 出文档,无工具。
  - agent 型(qa):带工具循环(D5 实现);D3 先把它当"基于检索片段回答"的模板用。

关键:Skill 的内容是**可切换后缀**,放进 user 消息;system 始终是稳定仓库前缀,
这样切 Skill 不破坏 cache_prompt 的前缀复用。
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Skill:
    name: str
    kind: str          # "template" | "agent"
    description: str
    suffix: str        # 放入 user 消息的"角色 + 指令 + 输出要求"

    def build_user_message(self, task: str, context: str = "") -> str:
        """组装 user 消息:Skill 后缀 + 检索片段 + 当次任务。"""
        parts = [self.suffix]
        if context:
            parts.append("\n## 相关代码片段\n" + context)
        parts.append("\n## 任务\n" + task)
        return "\n".join(parts)


_REGISTRY: dict[str, Skill] = {}


def register(skill: Skill) -> None:
    _REGISTRY[skill.name] = skill


def get(name: str) -> Skill:
    if name not in _REGISTRY:
        raise KeyError(f"未注册的 Skill: {name}(可用: {', '.join(_REGISTRY)})")
    return _REGISTRY[name]


def all_skills() -> list[Skill]:
    return list(_REGISTRY.values())


# --- 内置 Skill ---
register(Skill(
    name="architecture",
    kind="template",
    description="整体架构:模块划分、技术栈、关键组件关系",
    suffix=(
        "你是资深软件架构师。基于仓库概览,产出该仓库的**架构总览**:"
        "1) 顶层模块划分与职责;2) 技术栈;3) 关键组件之间的关系与数据流。"
        "用简洁的 Markdown,分小节;不确定处明确说明,不要编造。"
    ),
))

register(Skill(
    name="frontend",
    kind="template",
    description="前端分析:UI 组件、路由、状态管理、构建链",
    suffix=(
        "你是前端架构分析师。聚焦前端部分:UI 组件结构、路由、状态管理、"
        "数据获取与构建链。若该仓库没有前端代码,直接说明。输出简洁 Markdown。"
    ),
))

register(Skill(
    name="backend",
    kind="template",
    description="后端分析:服务/接口、数据模型、业务逻辑、调用链",
    suffix=(
        "你是后端架构分析师。聚焦后端部分:服务与接口、数据模型、核心业务逻辑、"
        "关键调用链。若该仓库没有后端代码,直接说明。输出简洁 Markdown。"
    ),
))

register(Skill(
    name="qa",
    kind="agent",
    description="代码问答:基于检索片段回答,带 file:line 引用",
    suffix=(
        "你是代码问答助手。**只依据上面提供的代码片段**回答用户问题,"
        "在关键结论处给出 `文件:行号` 引用。若片段不足以回答,明确说"
        "“依据现有片段无法确定”,不要编造。"
    ),
))
