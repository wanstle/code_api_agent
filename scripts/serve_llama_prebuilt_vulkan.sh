#!/usr/bin/env bash
# 用"预编译 Vulkan 二进制"启动 llama-server(免编译,免 CUDA toolkit)。
# 开发机(RTX 3090 经 Vulkan)和部署机(Strix Halo iGPU)都能用同一份二进制路径逻辑。
#
# 二进制由 scripts/fetch_llama_prebuilt.sh 下载到 third_party/llama_prebuilt/<ver>/。
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$(ls -d "$ROOT"/third_party/llama_prebuilt/llama-* 2>/dev/null | head -1 || true)"
if [ -z "$DIR" ]; then
  echo "未找到预编译二进制,请先运行 scripts/fetch_llama_prebuilt.sh" >&2
  exit 1
fi
MODEL="${MODEL:-$ROOT/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf}"

exec env LD_LIBRARY_PATH="$DIR" "$DIR/llama-server" \
  -m "$MODEL" \
  -c "${CTX:-16384}" \
  -ngl 99 \
  --host 0.0.0.0 --port "${PORT:-8080}" \
  --parallel "${SLOTS:-2}" \
  --metrics
