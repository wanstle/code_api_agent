"""D. Skill 框架:稳定前缀(仓库概览)+ 可切换后缀(各 Skill 指令)。

核心:稳定前缀放 system(跨 Skill 不变)→ llama.cpp cache_prompt 命中;
Skill 后缀 + 任务放 user(每次变)。切 Skill 不动 system 前缀,KV 被复用。
"""
