#!/usr/bin/env bash
# 下载 llama.cpp 官方预编译二进制(免编译)。
#   scripts/fetch_llama_prebuilt.sh vulkan   # 默认,适配 3090(Vulkan) 与 Strix Halo
#   scripts/fetch_llama_prebuilt.sh cpu
#   scripts/fetch_llama_prebuilt.sh rocm     # 部署机若走 ROCm 可选
#
# 注:Linux 官方 release 不提供 CUDA 预编译;3090 走 Vulkan 即可,
# 且 Vulkan 正是部署目标 Strix Halo 的后端,更具代表性。
set -euo pipefail

BACKEND="${1:-vulkan}"
VER="${LLAMA_VER:-b9548}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/third_party/llama_prebuilt"

case "$BACKEND" in
  vulkan) ASSET="llama-${VER}-bin-ubuntu-vulkan-x64.tar.gz" ;;
  cpu)    ASSET="llama-${VER}-bin-ubuntu-x64.tar.gz" ;;
  rocm)   ASSET="llama-${VER}-bin-ubuntu-rocm-7.2-x64.tar.gz" ;;
  *) echo "未知后端: $BACKEND (vulkan|cpu|rocm)" >&2; exit 1 ;;
esac

mkdir -p "$DEST"
URL="https://github.com/ggml-org/llama.cpp/releases/download/${VER}/${ASSET}"
echo "下载 $URL"
curl -sL -o "$DEST/$ASSET" "$URL"
tar xzf "$DEST/$ASSET" -C "$DEST"
echo "完成 → $(ls -d "$DEST"/llama-*/llama-server)"
