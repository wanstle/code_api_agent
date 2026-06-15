"""只读:打印生成 lens 时,LLM 实际收到的输入(不调用模型)。"""
from __future__ import annotations
import sys
from skills.prefix import build_repo_prefix
from docgen.summarize import _load, _group_modules, _module_context, _module_of

name = sys.argv[1] if len(sys.argv) > 1 else "click"
target = sys.argv[2] if len(sys.argv) > 2 else "examples/aliases"

pfx = build_repo_prefix(name)
meta, top, detail, snippets = _load(name)
files = [f for f in meta["files"] if _module_of(f["path"]) == target]
ctx = _module_context(files, top, detail, snippets)

print(f"========== 系统消息=仓库概览前缀(共 {len(pfx)} 字符,节选前 700)==========")
print(pfx[:700])
print(f"\n========== 用户消息=模块 [{target}] 的上下文(共 {len(ctx)} 字符,lens 实际用前 2500;此处展示前 1900)==========")
print(ctx[:1900])
