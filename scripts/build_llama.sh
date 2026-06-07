#!/usr/bin/env bash
# 构建 llama.cpp。用法:
#   scripts/build_llama.sh cuda      # 开发机(RTX 3090)
#   scripts/build_llama.sh vulkan    # 部署机(AMD Strix Halo / AI Max+ 395)
#
# 产物在 ./third_party/llama.cpp/build/bin/llama-server
set -euo pipefail

BACKEND="${1:-vulkan}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/third_party/llama.cpp"

mkdir -p "$ROOT/third_party"
if [ ! -d "$SRC" ]; then
  git clone --depth 1 https://github.com/ggml-org/llama.cpp "$SRC"
fi
cd "$SRC"

case "$BACKEND" in
  cuda)
    # 开发机:需已装 CUDA toolkit(nvcc)。
    cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release
    ;;
  vulkan)
    # 部署机 Strix Halo:走 Vulkan(对 gfx1151 最稳)。需 Vulkan SDK / loader + glslc。
    cmake -B build -DGGML_VULKAN=ON -DCMAKE_BUILD_TYPE=Release
    ;;
  cpu)
    cmake -B build -DCMAKE_BUILD_TYPE=Release
    ;;
  *)
    echo "未知后端: $BACKEND (可选 cuda|vulkan|cpu)" >&2
    exit 1
    ;;
esac

cmake --build build --config Release -j --target llama-server llama-cli
echo "完成 → $SRC/build/bin/llama-server"
