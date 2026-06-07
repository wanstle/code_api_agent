# 推理服务部署说明(llama.cpp）

业务代码只依赖 llama-server 的 **OpenAI 兼容接口**,因此开发机(CUDA/CPU)与部署机(Vulkan)
切换后端时,Python 侧一行不用改。

## 1. 构建 llama.cpp

```bash
# 开发机(RTX 3090):需先装 CUDA toolkit(nvcc)
scripts/build_llama.sh cuda

# 部署机(AMD Strix Halo / AI Max+ 395):需 Vulkan loader + glslc(shaderc)
scripts/build_llama.sh vulkan

# 任何机器都能用的兜底(慢,仅冒烟测试)
scripts/build_llama.sh cpu
```

各后端的额外依赖:
- **cuda**:CUDA toolkit(`nvcc`)。本开发机当前只有驱动(`nvidia-smi` 可用)缺 toolkit。
- **vulkan**:Vulkan 头文件(本机已有 `/usr/include/vulkan`)+ `glslc`(本机缺,装 `glslang-tools`/`shaderc`)。
- **cpu**:仅需 cmake + gcc(本机已具备)。

## 2. 下载模型(GGUF)

放到 `./models/` 下。开发机有外网,可用 huggingface 拉取:

```bash
pip install -U "huggingface_hub[cli]"
# 问答交互档(7B,~4.5GB)
huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF \
  qwen2.5-coder-7b-instruct-q4_k_m.gguf --local-dir ./models
# 冒烟测试用的超小模型(0.5B,~0.4GB)
huggingface-cli download Qwen/Qwen2.5-0.5B-Instruct-GGUF \
  qwen2.5-0.5b-instruct-q4_k_m.gguf --local-dir ./models
```

> 离线部署机:在有网机器上下好 GGUF,拷贝到部署机的 `./models/` 即可。

## 3. 启动服务

```bash
# 开发机
MODEL=./models/qwen2.5-coder-7b-instruct-q4_k_m.gguf scripts/serve_llama_cuda.sh
# 部署机
MODEL=./models/qwen2.5-coder-14b-instruct-q4_k_m.gguf scripts/serve_llama_vulkan.sh
```

可用环境变量:`PORT`(默认 8080)、`CTX`(默认 16384)、`SLOTS`(并行槽,默认 2)、`MODEL`。

## 4. 验证 KV cache(cache_prompt)

```bash
# 默认连 http://127.0.0.1:8080/v1,可用 LLAMA_BASE_URL 覆盖
.venv/bin/python -m scripts.verify_cache_prompt
```

预期:warm 轮的 `prompt_ms`(prefill)显著低于 cold 轮,`cached_tokens` 接近前缀长度,
证明"稳定前缀 + 可切换后缀"的复用机制成立。
