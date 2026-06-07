#!/usr/bin/env bash
# 开发机(RTX 3090, 24GB)启动 llama-server。
# 24GB 显存:7B/14B(Q4_K_M)可全量 offload;问答交互档用这个。
#
# 模型放在 ./models/ 下,用 MODEL 环境变量覆盖路径。
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/third_party/llama.cpp/build/bin/llama-server"
MODEL="${MODEL:-$ROOT/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf}"

exec "$BIN" \
  -m "$MODEL" \
  -c "${CTX:-16384}" \
  -ngl 99 \
  --host 0.0.0.0 --port "${PORT:-8080}" \
  --parallel "${SLOTS:-2}" \
  --metrics
