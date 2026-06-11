"""Download the GGUF model used by llama.cpp.

Defaults are chosen for the AMD/Vulkan path in this repo:
  - mirror: https://hf-mirror.com
  - repo:   unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF
  - files:  *Q4_K_M*.gguf

Override with environment variables when needed:
  HF_ENDPOINT=https://hf-mirror.com
  GGUF_PATTERN='*Q4_K_M*.gguf'
  LOCAL_DIR='./models/Qwen3-Coder-30B-A3B-Instruct-GGUF'
"""

import os

os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

from huggingface_hub import logging, snapshot_download

REPO_ID = "unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF"
LOCAL_DIR = os.environ.get("LOCAL_DIR", "../models/Qwen3-Coder-30B-A3B-Instruct-GGUF")
GGUF_PATTERN = os.environ.get("GGUF_PATTERN", "*Q4_K_M*.gguf")
MAX_WORKERS = int(os.environ.get("HF_MAX_WORKERS", "8"))

logging.set_verbosity_info()

snapshot_download(
    repo_id=REPO_ID,
    local_dir=LOCAL_DIR,
    local_dir_use_symlinks=False,
    allow_patterns=[
        GGUF_PATTERN,
        "README.md",
        "config.json",
        "tokenizer.json",
        "tokenizer_config.json",
        "generation_config.json",
        "chat_template.jinja",
    ],
    max_workers=MAX_WORKERS,
)

print(f"Downloaded {REPO_ID} ({GGUF_PATTERN}) to {LOCAL_DIR}")
