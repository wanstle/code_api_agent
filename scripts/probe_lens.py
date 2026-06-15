"""探针:只让 LLM 为每个模块生成"分析视角(lens)",不生成文档。

目的:验证 30B 能否产出**模块特异**的指引(而非通用套话)。
- 输入:稳定仓库前缀(system) + 该模块的文件/符号/部分源码(user)
- 输出:JSON 约束的 {role, focus[], sections[]}(顺便验证防循环)
用法: .venv/bin/python -m scripts.probe_lens [repo-name] [模块数]
"""

from __future__ import annotations

import sys

from inference.client import LlamaClient
from skills.prefix import build_repo_prefix
from docgen.summarize import _load, _group_modules, _module_context

CTX_CAP = 2500   # 截断单模块上下文,控制输入预算

_META = (
    "你是文档系统的「分析视角设计器」。下面给出本仓库某个模块的文件、符号和部分源码。\n"
    "请为**这个模块**设计一份专属的文档分析视角,要求**具体到该模块本身**,"
    "能体现它和别的模块的差异,不要写放之四海皆准的套话。\n"
    "**只输出一个 JSON 对象**,字段如下(中文填写):\n"
    '{"role": "一句话说明该模块在本仓库中的角色与定位", '
    '"focus": ["该模块文档应重点讲清的 3-5 个具体点"], '
    '"sections": ["建议的输出小节名,3-5 个"]}'
)


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "click"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    client = LlamaClient()
    if not client.ping():
        print("llama-server 不可达,请先启动。")
        return 1

    prefix = build_repo_prefix(name)
    meta, top, detail, snippets = _load(name)
    modules = _group_modules(meta, top)[:n]
    print(f"仓库={name} · 前缀 {len(prefix)} 字符 · 探测 {len(modules)} 个模块\n")

    for mod, files in modules:
        ctx = _module_context(files, top, detail, snippets)[:CTX_CAP]
        user = _META + f"\n\n模块: {mod}\n{ctx}"
        res = client.chat(
            [{"role": "system", "content": prefix}, {"role": "user", "content": user}],
            max_tokens=350, temperature=0.3,
            response_format={"type": "json_object"},   # 约束为合法 JSON,防循环
        )
        print("=" * 72)
        print(f"模块: {mod}")
        print(res.text.strip())
        print(f"[cached_tokens={res.cached_tokens} · 输出 {len(res.text)} 字符]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
