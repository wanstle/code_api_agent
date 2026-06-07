"""E. Doc Generation / 文档生成:层次化 map-reduce 摘要 → Markdown / MkDocs。

map:   按模块(目录)生成模块摘要(文件 + 关键符号 → 一段说明)
reduce:汇总各模块摘要 → 仓库整体架构文档
注:map 阶段每模块内容不同,cache_prompt 仅复用稳定的 system 前缀(仓库概览),
    per-module 内容仍需 prefill —— 符合 README 3.3 对收益边界的标定。
"""
