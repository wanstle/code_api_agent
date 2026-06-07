"""C. Inference / 推理服务层:对接 llama-server 的 OpenAI 兼容接口。

设计要点:业务代码只依赖"OpenAI 兼容接口",与后端无关 ——
开发机用 CUDA 版 llama.cpp、部署机用 Vulkan 版,这一层代码一行不改。
"""
