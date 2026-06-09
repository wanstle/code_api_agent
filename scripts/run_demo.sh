#!/usr/bin/env bash
# 一键启动可视化 Demo:llama-server(问答用)+ Gradio 界面(文档浏览 + 问答)。
# 文档浏览不依赖服务;问答需要 server。
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# 1) 起 llama-server(脚本自带单实例守护)
echo "启动 llama-server …"
PORT="${LLAMA_PORT:-8080}" nohup scripts/serve_llama_prebuilt_vulkan.sh > .cache/llama_server.log 2>&1 &
for i in $(seq 1 90); do
  curl -s "http://127.0.0.1:${LLAMA_PORT:-8080}/health" 2>/dev/null | grep -q '"status":"ok"' && { echo "server ready"; break; }
  sleep 1
done

# 2) 起 Gradio 界面
echo "启动 Gradio Demo → http://localhost:7860"
exec .venv/bin/python demo.py
