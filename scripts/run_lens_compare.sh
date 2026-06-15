#!/usr/bin/env bash
# 在部署机上:起 30B server → 生成 lenses → 跑 lens-vs-fixed 对比。
# 用法: run_lens_compare.sh <repo-name> <comma-separated-modules>
# 留下 server 运行(调用方测完自行 pkill);写 .lenscmp.done 标记。
set -uo pipefail
ROOT="$HOME/api_doc"; cd "$ROOT"
REPO="${1:?repo}"; MODS="${2:?modules}"
rm -f .lenscmp.done

export PATH="$HOME/.local/bin:$PATH"
export MODEL="$ROOT/models/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf"
export PORT=8080 CTX=8192 SLOTS=1 HF_ENDPOINT=https://hf-mirror.com

bash scripts/serve_llama_prebuilt_vulkan.sh > .cache/llama_server.log 2>&1 &
for i in $(seq 1 150); do
  curl -s http://127.0.0.1:8080/health 2>/dev/null | grep -q ok && break; sleep 2
done

echo "[1/2] 生成 lenses …"
.venv/bin/python -m cli lens "$REPO" > .cache/run_lens.log 2>&1
echo "[2/2] lens-vs-fixed 对比 …"
.venv/bin/python -m scripts.compare_lens_doc "$REPO" "$MODS" > .cache/run_cmp.log 2>&1

echo OK > .lenscmp.done
echo "完成。"
