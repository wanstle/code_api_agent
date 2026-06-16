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

其他选择如 `Qwen/Qwen3-Coder-Next-GGUF` 也是不错的选择。

但是注意`/home/`是NFS，因此可以考虑

```bash
mkdir -p /tmp/qwen3-next
cp models/Qwen3-Coder-Next-GGUF/Qwen3-Coder-Next-Q4_K_M/*.gguf /tmp/qwen3-next/
```


## 1. 启动本地 LLM

如果没有正在运行的 `llama-server`，先启动模型服务：

```bash
MODEL=/home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf \
PORT=8080 CTX=131072 SLOTS=1 \
scripts/serve_llama_prebuilt_vulkan.sh
```

确认服务健康：

```bash
curl http://127.0.0.1:8080/health
```

返回 `{"status":"ok"}` 即可继续。

### 使用多分片 GGUF 模型

如果模型目录里是 llama.cpp 的 GGUF 分片，例如：

```text
models/Qwen3-Coder-Next-GGUF/Qwen3-Coder-Next-Q4_K_M/
  Qwen3-Coder-Next-Q4_K_M-00001-of-00004.gguf
  Qwen3-Coder-Next-Q4_K_M-00002-of-00004.gguf
  Qwen3-Coder-Next-Q4_K_M-00003-of-00004.gguf
  Qwen3-Coder-Next-Q4_K_M-00004-of-00004.gguf
```

启动时只需要把 `MODEL` 指向第一个分片，llama.cpp 会自动读取同目录下后续分片：

```bash
MODEL=/home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-Next-GGUF/Qwen3-Coder-Next-Q4_K_M/Qwen3-Coder-Next-Q4_K_M-00001-of-00004.gguf \
PORT=8080 CTX=131072 SLOTS=1 \
scripts/serve_llama_prebuilt_vulkan.sh

MODEL=/tmp/qwen3-next/Qwen3-Coder-Next-Q4_K_M-00001-of-00004.gguf \
PORT=8080 CTX=131072 SLOTS=1 \
scripts/serve_llama_prebuilt_vulkan.sh
```

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

推荐流程是先生成模块提纲 lens，再带着 lens 生成文档：

```bash
python -m cli lens <repo-name>
python -m cli doc <repo-name> --use-lens --complete --nav-subfolders
```

`cli doc` 默认会生成三层内容：

- `Architecture`：仓库整体视角，回答项目分层、关键流程和模块关系。
- `Modules`：模块导览，比 Architecture 更具体，但仍保持高屋建瓴；主要写模块职责、边界、关键入口、工作方式和阅读建议。
- `Detailed API`：逐符号细节，写签名、参数、返回值、异常、行为和源码定位。

`--nav-subfolders` 会让左侧导航按一级子目录分组，并支持手动展开/收起；如果想改回扁平列表，可以加 `--no-nav-subfolders`。

`lens` 会写入：

```text
.cache/index/<repo-name>/lenses.json
```

你可以在生成文档前人工编辑 `lenses.json`。如果某个模块由人工确认过，把对应条目的 `source` 改成 `"human"`；后续 `python -m cli lens <repo-name>` 默认会保留已有内容，只有加 `--force` 才会覆盖。`python -m cli doc <repo-name> --use-lens` 只会注入 `source` 为 `"ai"` 或 `"human"` 的提纲。

一般情况下，调整 Module / Detailed API 的 prompt 后不需要重新生成 lens；lens 只是模块级分析视角，不缓存 Detailed API 的逐符号描述。只有当你觉得模块视角本身不准、模块职责划分不清，或源码变化很大时，才需要重新跑：

```bash
python -m cli lens <repo-name> --force
```

如果 `llama-server` 已经手动启动，推荐使用外部 server 模式：

```bash
python -m cli doc <repo-name> --use-lens --complete --nav-subfolders
```

如果希望 CLI 自动启动并停止模型服务，使用 managed 模式：

```bash
python -m cli lens <repo-name> --managed \
  --model /home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf \
  --ctx 131072

python -m cli doc <repo-name> --use-lens \
  --managed \
  --complete \
  --nav-subfolders \
  --model /home/sht8/xiaojx/code_api_agent/models/Qwen3-Coder-30B-A3B-Instruct-GGUF/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf \
  --ctx 131072
```

文档生成是可续跑的。Detailed API 的逐符号描述会写入：

```text
.cache/index/<repo-name>/apidoc_cache.json
```

如果中途停止，重新运行同一条 `cli doc` 命令会复用缓存继续补齐。

如果只想让新的 Detailed API prompt 作用到已经生成过的符号，删除 API 描述缓存后重跑：

```bash
rm -f .cache/index/<repo-name>/apidoc_cache.json
python -m cli doc <repo-name> --use-lens --complete --nav-subfolders
```

如果想完全重新生成站点文件，也可以同时删除旧文档目录：

```bash
rm -f .cache/index/<repo-name>/apidoc_cache.json
rm -rf docs/<repo-name>
python -m cli doc <repo-name> --use-lens --complete --nav-subfolders
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
- `Modules`：模块级文档
- `Detailed API`：逐模块 API 细项页

源码页面仍会生成为 API `来源` 链接的跳转目标，但不会出现在导航或站内搜索中。

## 5. 在文档内使用 LLM 问答窗口

文档站的 `LLM Chat` 页面会嵌入本地 Chainlit UI。先在另一个终端启动问答 UI：

```bash
REPO=<repo-name> chainlit run app.py --host 127.0.0.1 --port 8001
```

然后打开文档站：

```text
http://127.0.0.1:8000/
```

进入导航里的 `LLM Chat`，即可在文档内提问；API 详情页中的 `来源` 链接可跳到对应源码行。

也可以直接访问 Chainlit：

```text
http://127.0.0.1:8001/
```

命令行问答仍然可用：

```bash
python -m cli ask <repo-name> "question here"
```


### 文档生成中途停止

`cli doc` 的 API 细项阶段按批次生成，默认可续跑。中途停止后直接重跑同一条命令即可。


