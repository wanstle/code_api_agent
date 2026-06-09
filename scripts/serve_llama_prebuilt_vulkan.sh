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

# 安全:启动前杀掉残留的 llama-server,避免多实例叠加把显存占满。
if pgrep -x llama-server >/dev/null 2>&1; then
  echo "发现残留 llama-server,先清理…" >&2
  pkill -x llama-server 2>/dev/null || true
  sleep 2
fi

# 默认 1 个并行槽(顺序批量足够,KV 显存更省;需要并发再调 SLOTS)。
exec env LD_LIBRARY_PATH="$DIR" "$DIR/llama-server" \
  -m "$MODEL" \
  -c "${CTX:-8192}" \
  -ngl 99 \
  --host 0.0.0.0 --port "${PORT:-8080}" \
  --parallel "${SLOTS:-1}" \
  --metrics
