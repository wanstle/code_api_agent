#!/usr/bin/env bash
# 部署机(AMD Strix Halo / AI Max+ 395, 128GB 统一内存)启动 llama-server。
# 统一内存大:文档生成档可上 32B 甚至 70B(Q4);瓶颈是带宽 ~256 GB/s,故大模型只用于离线慢跑。
#
# 模型放在 ./models/ 下,用 MODEL 覆盖。问答用 7B/14B,文档生成用 32B+。
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/third_party/llama.cpp/build/bin/llama-server"
MODEL="${MODEL:-$ROOT/models/qwen2.5-coder-14b-instruct-q4_k_m.gguf}"

# -ngl 99:统一内存下把所有层交给 iGPU(Radeon 8060S)。
exec "$BIN" \
  -m "$MODEL" \
  -c "${CTX:-16384}" \
  -ngl 99 \
  --host 0.0.0.0 --port "${PORT:-8080}" \
  --parallel "${SLOTS:-2}" \
  --metrics
