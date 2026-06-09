# 部署到 AMD 395 机器(aup-SHC2-395-3)— 操作记录

目标机:**AMD RYZEN AI MAX+ 395 / Radeon 8060S(gfx1151)**,统一内存,Linux x86-64。
原则:**一步一步、保守、可回退**。每步记录命令与结果。

## 前置勘察(只读,已完成 2026-06-09)
- 硬件:gfx1151 ✓、`/dev/dri/renderD128` ✓、Vulkan 加载器 `libvulkan.so.1` + RADV(mesa 25.0.7)✓、**ROCm 7.1.1** 已装 ✓、无 nvidia-smi。
- 内存:实测 **62Gi**(注:提案假设 128G;另有一台 90G 的机器待连)。
- 网络:github ✓ / pypi ✓ / astral.sh ✓ / **huggingface.co ✗(000)** / **hf-mirror.com ✓** / modelscope ✓;GitHub release 资产实测可下(33MB)。
- 现成:`python3 3.12` + `python3 -m venv` 可用、pip3/cmake 在;无 uv、无 llama/ollama、无旧模型。
- 结论:全部可在线获取(模型走 hf-mirror);推理首选 **Vulkan**,备选 ROCm。

## 部署步骤(逐步勾选)
- [ ] **S1** 拷代码 + 建 venv + 装依赖(无模型下载)
- [ ] **S2** 验证导入 + tree-sitter 解析
- [ ] **S3** 取 llama.cpp Vulkan 预编译二进制,验证**能否枚举到 iGPU(关键未知)**
- [ ] **S4** 下小模型(0.5B,走 hf-mirror)+ 起 llama-server + 推理冒烟
- [ ] **S5** 全链路:clone click → 建索引(fastembed 走镜像)→ 跑一次问答

---

## 执行记录

### S1 — 拷代码 + venv + 依赖 ✅(2026-06-09)
- `rsync` 代码到 `~/api_doc`(排除 venv/cache/models/third_party/git;含 docs)。
- 坑:`python3 -m venv` 缺 ensurepip(同开发机)→ 改用 **uv**(`curl astral.sh | sh`,uv 0.11.19)。
- `uv venv --python 3.12` + `uv pip install` 核心依赖:GitPython / tree-sitter / tree-sitter-language-pack / openai / typer / rich / fastembed / chromadb。
- 坑:首次安装下载久,SSH 300s 超时被杀 → 改 **远端 nohup 后台跑 + 完成标记**,uv 缓存命中后秒完成。
- 坑:**NFS 家目录首次导入大库慢**(onnxruntime/chromadb),import 检查要给足超时(>120s);第二次因 pyc 缓存而快。
- 结果:核心依赖导入 OK,onnxruntime 为 CPU 版。demo UI(gradio/chainlit/mkdocs)暂未装。

### S2 — tree-sitter 解析 ✅(2026-06-09)
`python -m ingestion.cli ~/api_doc/ingestion` 正常:5 文件 / 26 符号,签名+位置正确。tree-sitter-language-pack 预编译绑定在 AMD x86-64 上工作。

### S3 — Vulkan 二进制 + iGPU 枚举 ✅(关键!2026-06-09)
- `scripts/fetch_llama_prebuilt.sh vulkan` 从 GitHub 下载 b9548(~33MB)成功。
- `llama-server --version` OK。
- **`llama-cli --list-devices` 枚举到:`Vulkan0: AMD Radeon Graphics (RADV GFX1151) (97503 MiB, 97288 MiB free)`**
- → **预编译 Vulkan 二进制在 gfx1151 上可用**,推理路径打通(最大未知解除)。
- ⚠️ 内存观察:Vulkan 报告 ~95GB 可用,而 `free` 是 62G 系统内存 —— 疑似 BIOS UMA/GTT 配置或即用户所说"90G"机,待确认。坑:远端 heredoc 里 echo 含中文括号 `(` 会触发 bash 语法错,避免。

### S4 — 下模型 + 起 server + 推理冒烟 ✅(2026-06-09)
- 走 **hf-mirror** 下 Qwen2.5-0.5B-Instruct Q4(469MB)成功 → 镜像方案验证可行。
- `MODEL=... PORT=8080 serve_llama_prebuilt_vulkan.sh` 启动;日志确认 `Vulkan0: RADV GFX1151` 加载模型。
- 推理冒烟:输入 "Reply with exactly: hello from amd" → 输出 **"Hello from AMD!"**,prompt_ms≈610。**AMD 卡推理链路打通。**

### S5 — 全链路 clone+索引+问答 ✅(管道)/ ⚠️(模型太小)(2026-06-09)
- `HF_ENDPOINT=https://hf-mirror.com cli index github.com/pallets/click`:clone + 解析 + **fastembed(走镜像)编码 1768 块** + 双索引,全部成功。
- `cli ask click "..."`:检索→agent→输出全程无报错,**管道连通**。
- ⚠️ 但 0.5B 模型太弱,跟不上 JSON 工具协议(吐出模板占位"文件:行号")。**真实问答质量需 7B/14B**;0.5B 仅用于验证链路。

---

## 部署结论(2026-06-09)
**整套代码在 AMD RYZEN AI MAX+ 395 / Radeon 8060S(gfx1151)上端到端跑通**:解析、索引(fastembed CPU)、Vulkan 推理、检索+agent 问答全部 OK,**代码零修改**。模型与依赖全部经 hf-mirror/GitHub/pypi 在线获取。
- 推理路径:**Vulkan(已验证)**,ROCm 7.1.1 备选。
- 待办:① 确认最终部署机内存(62G/95G/90G);② 如需可视化 demo,补装 gradio。

### S6 — 真模型实测 Qwen3-Coder-30B-A3B(MoE)✅(2026-06-09)
- 模型源:`unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF`,单文件 `Q4_K_M`(**18.56GB**),走 hf-mirror 后台可续下载(~33MB/s)。
- **内存实测**(这台 62G 系统 / GTT 97G):加载后 **Vulkan 剩余 97288→78636 MiB,正好降 ~18.6GB**;`free` 仍 **59Gi 可用 / 37Gi free**。→ **60G 装 30B-A3B 很宽裕**(占 ~18.6G,余 ~78G Vulkan/59G 系统),可开到 256k 上下文(实测设 8192)。
- **质量实测**:用它跑 `cli ask`,正确跟随 JSON 工具协议(read_file→find_symbol→read_file→final),答案准确带引用(Option @ core.py:2805、_OptionParser、_Option @ parser.py:127)。比 0.5B 天壤之别 → **30B-A3B 是这卡的合适主力模型**。
- 已停 server 释放内存。
- 🔎 发现一个 agent 小瑕疵:模型有时在一条响应里**输出多个 JSON 动作**,`_extract_json`(取首{到末})会解析失败而回退"直接作答"(本次最终答案仍正确)。改进:取**第一个合法 JSON 对象**即可。待修。
