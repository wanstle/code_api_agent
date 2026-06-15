# RepoAgent AMD Deployment Guide

RepoAgent 是一个本地代码分析与文档生成工具。当前 workspace 已按 AMD Ryzen AI Max+ 395 / Radeon 8060S 的 Vulkan 路径部署，推理使用本地 `llama-server`，模型默认使用：

```text
models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf
```

主要流程是：

```text
GitHub 仓库 -> 建索引 -> 生成 MkDocs 文档 -> 在文档站内打开 LLM Chat 问答
```

## 0. 环境设置

重新打开 shell，或手动加载 uv 所在路径后，创建并同步虚拟环境：

```bash
uv venv --python 3.10 .venv
source .venv/bin/activate
uv sync
```

后续命令默认在已激活 `.venv` 的 shell 里执行，因此可以直接使用 `python -m cli ...`。如果不激活环境，也可以把 `python` 写成 `.venv/bin/python`。

### 准备 llama.cpp Vulkan 预编译运行时

本项目默认使用 llama.cpp 的 Vulkan 后端。运行下面的脚本会下载并解压预编译包到 `third_party/llama_prebuilt/`：

```bash
scripts/fetch_llama_prebuilt.sh vulkan
```

完成后应能看到类似目录：

```text
third_party/llama_prebuilt/llama-b9548/llama-server
third_party/llama_prebuilt/llama-b9548/llama-cli
```

验证 AMD iGPU 是否被 Vulkan 后端识别：

```bash
third_party/llama_prebuilt/llama-b9548/llama-cli --list-devices
```

在 Ryzen AI Max+ 395 / Radeon 8060S 上，期望看到类似：

```text
Vulkan0: AMD Radeon Graphics (RADV GFX1151)
```

如果想换 llama.cpp release 版本，可以设置 `LLAMA_VER`：

```bash
LLAMA_VER=b9548 scripts/fetch_llama_prebuilt.sh vulkan
```

### 下载默认 GGUF 模型

使用项目脚本下载默认模型：

```bash
HF_ENDPOINT=https://hf-mirror.com \
LOCAL_DIR=./models/Qwen3-Coder-30B-A3B-Instruct-GGUF \
GGUF_PATTERN='*Q4_K_M*.gguf' \
python scripts/download_model.py
```

默认模型来源是：

```text
unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF
```

下载完成后应有：

```text
models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf
```

可以检查文件：

```bash
ls -lh models/Qwen3-Coder-30B-A3B-Instruct-GGUF/
```


## 1. 启动本地 LLM

如果没有正在运行的 `llama-server`，先启动模型服务：

```bash
MODEL=/home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf \
PORT=8080 CTX=262144 SLOTS=1 \
scripts/serve_llama_prebuilt_vulkan.sh
```

确认服务健康：

```bash
curl http://127.0.0.1:8080/health
```

返回 `{"status":"ok"}` 即可继续。

## 2. 建索引

对 GitHub 仓库建索引：

```bash
HF_ENDPOINT=https://hf-mirror.com python -m cli index https://github.com/OWNER/REPO
```

索引名通常等于仓库名。上例生成的索引是：

```text
.cache/index/<repo-name>/
```

## 3. 生成或重新生成文档

推荐流程是先生成模块提纲 lens,再带着 lens 生成文档：

```bash
python -m cli lens <repo-name>
python -m cli doc <repo-name> --use-lens
```

`lens` 会写入：

```text
.cache/index/<repo-name>/lenses.json
```

你可以在生成文档前人工编辑 `lenses.json`。如果某个模块由人工确认过,把对应条目的 `source` 改成 `"human"`；后续 `python -m cli lens <repo-name>` 默认会保留已有内容,只有加 `--force` 才会覆盖。`python -m cli doc <repo-name> --use-lens` 只会注入 `source` 为 `"ai"` 或 `"human"` 的提纲。

如果 `llama-server` 已经手动启动，推荐使用外部 server 模式：

```bash
python -m cli doc <repo-name> --use-lens
```

如果希望 CLI 自动启动并停止模型服务，使用 managed 模式：

```bash
python -m cli lens <repo-name> --managed \
  --model /home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf \
  --ctx 8192

python -m cli doc <repo-name> --use-lens \
  --managed \
  --model /home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf \
  --ctx 8192
```

文档生成是可续跑的。API 细项会写入：

```text
.cache/index/<repo-name>/apidoc_cache.json
```

如果中途停止，重新运行同一条 `cli doc` 命令会复用缓存继续补齐。

如果你想完全重新生成文档和 API 描述，先删除旧缓存和旧文档：

```bash
rm -f .cache/index/<repo-name>/apidoc_cache.json
rm -rf docs/<repo-name>
python -m cli doc <repo-name> --use-lens --api --complete
```

注意：不要删除 `.cache/index/<repo-name>/meta.json`、`symbols.db` 或 `chroma/`，除非你也准备重新执行 `cli index`。

## 4. 预览文档站

生成完成后启动 MkDocs：

```bash
mkdocs serve -f docs/<repo-name>/mkdocs.yml --dev-addr 127.0.0.1:8000
```

浏览器打开：

```text
http://127.0.0.1:8000/
```

文档站包含：

- `Architecture`：整体架构和模块索引
- `LLM Chat`：嵌入式问答窗口
- `API Quick Ref`：API 快速索引
- `Modules`：模块级文档
- `Detailed API`：逐模块 API 细项页

## 5. 在文档内使用 LLM 问答窗口

文档站的 `LLM Chat` 页面会嵌入本地 Chainlit UI。先在另一个终端启动问答 UI：

```bash
REPO=<repo-name> chainlit run app.py --host 127.0.0.1 --port 8001
```

然后打开文档站：

```text
http://127.0.0.1:8000/
```

进入导航里的 `LLM Chat`，即可在文档内提问。

也可以直接访问 Chainlit：

```text
http://127.0.0.1:8001/
```

命令行问答仍然可用：

```bash
python -m cli ask <repo-name> "question here"
```

## 6. 常见问题

### repo 名称写错

如果出现：

```text
FileNotFoundError: .cache/index/<name>/meta.json
```

先查看真实索引名：

```bash
find .cache/index -maxdepth 2 -name meta.json -print
```

### context 超限

如果出现：

```text
request (...) exceeds the available context size (8192 tokens)
```

说明某次文档生成请求太长。当前代码已经对模块上下文做了截断，优先继续使用 `--ctx 8192`。如果仍频繁超限，可以改用更大的 CTX 重新启动 server，例如 `CTX=16384`，但显存/GTT 占用会增加。

### 文档生成中途停止

`cli doc` 的 API 细项阶段按批次生成，默认可续跑。中途停止后直接重跑同一条命令即可。


