# RepoAgent —— 大型仓库代码分析与文档生成 Agent

> 项目提案 (Proposal) · v0.1 · 2026-06-07
> 目标：7 天内交付一个可离线部署、面向大型 GitHub 仓库的代码分析 Agent，能自动解读仓库、生成文档，并支持用户对仓库提问。

---

## 1. 工作目标 (Goals)

### 1.1 总目标
构建一个**离线部署**的代码分析 Agent，输入一个大型 GitHub 仓库，输出：
1. **仓库解读**：架构概览、模块划分、技术栈、关键调用链与依赖关系。
2. **文档生成**：自动产出结构化文档（README / 架构文档 / 模块文档 / API 文档）。
3. **问答 (Q&A)**：用户可针对该仓库自然语言提问，Agent 基于检索 + 代码理解给出带引用（文件:行号）的答案。

### 1.2 关键约束 (Constraints)
| 维度 | 约束 |
|------|------|
| 部署 | **完全离线**，集群内运行，无外网/无外部 API |
| 硬件 | **AMD Ryzen AI Max+ 395 (Strix Halo)** · 128G LPDDR5X **统一内存** (CPU + iGPU 共享) · iGPU Radeon 8060S (RDNA 3.5 / gfx1151) · 内存带宽 ~256 GB/s · NPU XDNA 2 (~50 TOPS) |
| 模型 | 开源权重模型（本地推理），不依赖闭源 API |
| 切换机制 | 采用 **context switch + KV cache** 切换 skill，实现不同分析能力（前端 / 后端 / 基础设施 等） |
| 规模 | 面向"大型"仓库（数千～数万文件，远超单次上下文窗口） |
| 工期 | **7 天** |

### 1.3 成功标准 (Definition of Done)
- 能对一个 ≥ 5万行代码的真实仓库（如一个中型开源项目）完成端到端分析并产出文档。
- 问答答案可溯源（给出 `file:line` 引用），事实正确率在抽样评测中达标。
- Skill 切换通过 KV cache 复用共享前缀，切换延迟显著低于"重新构建上下文"。
- 单次仓库分析在目标硬件上可在可接受时间内完成（分钟级到小时级，视仓库规模）。

---

## 2. 工作分类 (Work Breakdown)

工作从**两个正交维度**拆分：按"分析能力 (Skill)"和按"工程模块 (Component)"。

### 2.1 按分析能力划分（Skill 维度 —— 决定切换什么）
Skill 分**两类**,都共享同一份"仓库概览前缀"（被 KV cache 缓存），仅切换后缀指令:
- **模板型 Skill**(`architecture` / `frontend` / `backend` / ...)：= 专用系统提示词 + 检索过滤策略 + 输出模板,**不带工具**,用于文档生成(map-reduce 摘要)。
- **agent 型 Skill**(`qa`)：= 专用提示词 + **工具集**(检索/读文件/grep)的循环,用于问答。

> 即:只有 `qa` 是 agent(会调工具),其余是"喂上下文→出文档"的模板器,实现上简单得多。

| Skill | 关注点 | 典型产物 |
|-------|--------|----------|
| `architecture` (通用架构) | 顶层结构、模块边界、技术栈 | 架构总览文档、模块地图 |
| `frontend` | UI 组件、路由、状态管理、构建链 | 前端模块文档、组件清单 |
| `backend` | 服务/接口、数据模型、业务逻辑、调用链 | 后端模块文档、API 文档 |
| `data` (可选) | 数据流、Schema、ETL、存储 | 数据流文档 |
| `infra` (可选) | CI/CD、容器、部署、配置 | 部署/运维文档 |
| `qa` | 基于以上索引的检索增强问答 | 带引用的回答 |

> Skill 之间是**可插拔模块**，先实现 `architecture` + `frontend` + `backend` + `qa` 四个，其余为可选增量。

### 2.2 按工程模块划分（Component 维度 —— 决定要建什么）
| 模块 | 职责 |
|------|------|
| **A. Ingestion / 解析层** | clone 仓库、文件树扫描、语言识别、tree-sitter AST 解析、**import/依赖关系图**(从 import 语句直接抽取;精确调用图列为可选增量) |
| **B. Indexing / 索引层** | 代码感知分块 + **向量索引**(语义检索)；**符号索引**(精确符号定位，函数/类/文件结构) —— 后者直接由 tree-sitter 解析结果存入 SQLite，是"免费副产品" |
| **C. Inference / 推理服务层** | 本地 LLM 推理（llama.cpp / Vulkan，用 iGPU）、**前缀 KV cache**；embedding 单独跑 CPU(fastembed) |
| **D. Skill 框架** | Skill 定义/注册、context switch 调度、前缀复用 |
| **E. Doc Generation / 文档生成** | 层次化摘要（文件→模块→仓库）、map-reduce、模板渲染 |
| **F. Q&A Agent** | 工具调用循环（检索/读文件/grep）、引用溯源 |
| **G. Serving / 编排** | API/CLI 入口、任务编排、缓存与产物管理 |

---

## 3. 实施方法和计划 (Approach)

### 3.1 总体架构

```
                 ┌─────────────────────────────────────────────┐
   GitHub Repo → │  A. Ingestion: clone → 文件树 → tree-sitter   │
                 │     AST → import/依赖图                         │
                 └───────────────────┬─────────────────────────┘
                                     │  代码块 + 符号 + 结构
                 ┌───────────────────▼─────────────────────────┐
                 │  B. Indexing: 代码感知分块                      │
                 │     ├─ 向量索引 (embeddings + Chroma) 语义检索  │
                 │     └─ 符号索引 (SQLite, tree-sitter 副产品)    │
                 └───────────────────┬─────────────────────────┘
                                     │  检索接口
   ┌─────────────────────────────────▼───────────────────────────┐
   │  共享上下文前缀 (仓库概览 + 文件地图)  ←── KV cache 缓存          │
   │  ───────────────────────────────────────────────────────────│
   │   D. Skill 框架 (context switch)                              │
   │   ┌──────────┬──────────┬──────────┬──────────┐             │
   │   │architect.│ frontend │ backend  │   qa     │  ← 可插拔后缀 │
   │   └──────────┴──────────┴──────────┴──────────┘             │
   └───────────────────┬───────────────────┬──────────────────────┘
                        │                   │
        ┌───────────────▼──────┐   ┌────────▼─────────────┐
        │ E. 文档生成 (map-     │   │ F. Q&A Agent          │
        │   reduce 层次摘要)     │   │   (工具循环 + 引用)    │
        └──────────────────────┘   └──────────────────────┘
                   │                          │
                   └──────────► G. Serving (CLI / API) ◄──┘

        全程运行于 C. 本地推理服务 (llama.cpp/Vulkan + embedding model)
```

### 3.2 核心技术选型（已按 AMD Strix Halo 平台调整）

> ⚠️ **平台前提**：硬件是 AMD APU(非 NVIDIA)。vLLM 的高效路径依赖 CUDA / 数据中心级 ROCm(MI300 等)，在 Radeon 8060S(gfx1151)上**不是可行路径**。本项目改用对 Strix Halo 支持最成熟的 **llama.cpp**。

| 组件 | 选型 | 理由 |
|------|------|------|
| 推理引擎 | **llama.cpp**(`llama-server`)，**Vulkan 后端**首选；ROCm(gfx1151)作为备选 | Vulkan 后端在 Radeon 8060S 上最稳定可用；支持 GGUF 量化、`cache_prompt` 前缀 KV 复用、多 slot —— 即"KV cache / context switch"的落地手段 |
| 主模型(分两档) | **交互问答**：Qwen2.5-Coder-7B / 14B-Instruct (GGUF Q4_K_M～Q5_K_M)，求响应速度；**离线文档生成**：32B 起,内存允许可上 70B(Q4 ~40G)，求质量 | 统一内存 128G 装得下大模型,**瓶颈是带宽 ~256 GB/s**:模型越大 token/s 越低。**离线文档生成不追求速度**(后台批跑、可慢),因此放最大可行模型换最高质量;问答需要交互响应,用 7/14B |
| Embedding | **fastembed**(ONNX, **跑 CPU**)，模型用 bge-small / nomic-embed-text | **全机只有一块 iGPU,要留给 LLM**;embedding 是一次性索引开销,放 CPU 即可,避免和 LLM 抢卡,也省去 PyTorch 重依赖 |
| AST 解析 | **tree-sitter**（`tree-sitter-language-pack`，预编译 wheel 免编译） | 语言无关、精确到函数/类边界，便于代码感知分块 |
| 向量库 | **Chroma**(底层 SQLite，自带持久化) | 本地、轻量、`Client()` 一行起、无需起服务;比裸 FAISS 省去自己管持久化 |
| Agent 编排 | 轻量自研循环 (Python，调 `llama-server` 的 OpenAI 兼容接口) | 7 天工期下避免重框架，掌控提示与工具调用 |

> 关于 NPU(XDNA 2)：当前 Linux 下用 NPU 做 LLM 推理的工具链(Ryzen AI / Lemonade)仍不成熟，本项目**以 iGPU(llama.cpp Vulkan)为主**，不依赖 NPU。

### 3.3 KV cache / context switch 落地方式（项目核心机制）

这是本项目区别于普通 RAG 的关键。思路：**把"重而稳定"的部分做成可缓存前缀，把"轻而多变"的 Skill 指令做成可切换后缀。**

```
[ 系统前缀: 仓库概览 + 文件地图 + 通用规则 ]   ← 长、跨 Skill 不变 → KV cache 命中
[ Skill 后缀: 该 Skill 的角色/输出模板 ]        ← 短、随 Skill 切换 → 仅此段重算
[ 当次任务 / 用户问题 + 检索片段 ]              ← 每次不同
```

**前缀里装什么、多大(关键)**：大仓库的**全量代码塞不进前缀**(否则就不存在"超出上下文窗口"这个前提了)。所以前缀是一份**压缩概览** —— 文件树骨架 + 各模块一两句摘要 + 技术栈,**控制在约 2k～8k token**(由 `--ctx-size` 和模型上下文上限约束),具体代码靠后面的检索片段按需带入,不进可复用前缀。

- **机制**：用 **llama.cpp `llama-server` 的 prompt 缓存**。请求带 `cache_prompt: true` 时，server 会复用与缓存中**最长公共前缀**匹配的 KV，未变的前缀不重新 prefill。所有 Skill 请求共用同一段逐 token 一致的前缀，切换 Skill 时只对后缀做增量 prefill —— 这就是"context switch + KV cache"在本平台的工程实现。(可配合多 slot:把同一仓库的会话固定到同一 slot，提升前缀命中。)
- **要点**：① 前缀必须 **token 级稳定**（同样的文本、同样的顺序、同样的分词），任何变化都会使缓存失效；② Skill 专属内容全部放在前缀之后；③ 检索片段放最后，避免污染可复用前缀；④ 用足够大的 `--ctx-size` 容纳"前缀 + 各 Skill 后缀 + 检索片段"。
- **收益边界(诚实标定)**：前缀缓存**不是处处变快**——
  - ✅ **真正受益**：对**同一仓库的多轮问答**、以及**多个 Skill 复用同一份概览前缀**(切 Skill 只重算短后缀)。这是带宽受限的 Strix Halo 上最值的省法。
  - ⚠️ **受益有限**：文档生成的 **map 阶段(逐文件摘要)每次文件内容都不同**,能复用的只有"概览+Skill 指令"那一小段,真正的 per-file prefill 省不掉。所以**别指望前缀缓存让文档生成变快**——那一档本就走"离线慢跑"。
- **"context switch"指什么(避免歧义)**：本项目走的是 **(a) 前缀复用**(共享前缀 + 切后缀),不是为每个 Skill 保存/恢复整段 KV 快照。若日后想要"按 Skill 秒切回上次状态",可选 llama.cpp 的 **slot save/restore**(把某 slot 的 KV 存盘再载回)作为 (b) 方案,但 MVP 不做。

### 3.4 关键流程

**(1) 文档生成 —— 层次化 map-reduce 摘要**
解决"仓库远大于上下文窗口"的问题：
```
文件级摘要 (map) → 模块级摘要 (reduce 同目录/同包) → 仓库级架构摘要 (reduce)
```
- 各层用对应模板型 Skill 生成,再渲染成 Markdown。
- **注意**:最顶层的"仓库级架构摘要"产出的就是 `architecture` 文档 —— `architecture` Skill 不是独立的一遍分析,而是 map-reduce 的**顶层 reduce**,二者是同一产物。

**(2) 问答 —— 检索增强 + Agent 工具循环**
```
用户问题 → 向量检索 + 符号检索 → 取 top-k 代码片段 (种子上下文)
        → qa Skill 在工具循环中按需 read_file / grep_symbol / list_dir (补充检索)
        → 生成带 file:line 引用的答案
```
- **检索是混合式**:先一次性预检索 top-k 作为**种子上下文**(快、保底),再让 agent 在循环里**按需补充**(精确定位、跟踪引用)。不是二选一。

### 3.5 风险与对策
| 风险 | 对策 |
|------|------|
| 大仓库分析耗时 | 增量处理、按模块分批、量化模型、可配置只分析子目录 |
| **带宽受限(~256 GB/s)导致大模型生成慢** | 交互问答用 7B/14B(Q4_K_M)；32B 仅用于离线批量文档生成(可后台慢跑);严控生成长度 |
| ROCm 对 gfx1151 支持不稳 | **默认走 llama.cpp Vulkan 后端**(对 Strix Halo 最稳),ROCm 仅作可选加速备选 |
| 前缀缓存频繁失效 | 严格隔离"稳定前缀"与"可变后缀"，`cache_prompt`+固定 slot，做缓存命中率监控 |
| 多语言解析覆盖不全 | tree-sitter 优先覆盖目标语言；无 grammar 时回退到基于正则/启发式分块 |
| 7 天工期紧张 | 先打通"窄而深"的端到端 MVP（单语言仓库 + 4 个 Skill），再横向扩展 |

---

## 4. 时间线 (7-Day Timeline)

> 原则：**Day 1–3 打通端到端最小闭环 (MVP)，Day 4–6 做深做宽，Day 7 收尾。** 每天结束有可演示的产出。

| Day | 主题 | 主要任务 | 当日产出 (里程碑) |
|-----|------|----------|-------------------|
| **D1** | 推理服务 + 解析骨架 | 编译/部署 llama.cpp(Vulkan)离线服务,验证 iGPU 推理 + `cache_prompt` 前缀缓存可用;仓库 clone + 文件树扫描 + tree-sitter 解析骨架 | LLM 在 Radeon 8060S 上可本地推理；能解析一个仓库出文件树与函数/类清单 |
| **D2** | 索引层 | 代码感知分块；fastembed(CPU) + Chroma 向量索引；tree-sitter→SQLite 符号索引；检索接口 | 能对任意问题返回 top-k 相关代码片段 |
| **D3** | Skill 框架 + KV cache | Skill 注册机制；稳定前缀 / 可切换后缀设计；接入 llama.cpp `cache_prompt` 前缀缓存；验证切换收益 | **MVP 闭环**：可切换 Skill，缓存命中率/切换延迟有数据 |
| **D4** | 文档生成 | 层次化 map-reduce 摘要；`architecture` + `frontend` + `backend` 三个 Skill；模板渲染 | 能对真实仓库自动产出架构 + 前后端模块文档 |
| **D5** | 问答 Agent | `qa` Skill；工具循环 (read_file/grep/list)；引用溯源 | 可对仓库提问并得到带 `file:line` 的答案 |
| **D6** | 集成 + 评测 + 调优 | 端到端跑一个真实大型仓库；抽样评测文档质量与问答正确率；性能/内存调优 | 评测报告 + 调优后的稳定版本 |
| **D7** | 收尾 | CLI/API 入口完善、文档、demo 录制、缓冲修 bug | **可交付版本 + 演示** |

**关键里程碑**
- 🏁 **D3 末**：端到端 MVP（解析→索引→Skill 切换）跑通。
- 🏁 **D5 末**：文档生成 + 问答两大功能均可用。
- 🏁 **D7 末**：在真实大型仓库上完成验收，可演示交付。

**缓冲与降级策略**：若进度落后，按优先级砍可选项 —— 先保 `architecture` + `qa`，前后端 Skill 次之，`data`/`infra` Skill 最后；模型可从 32B 降到 14B/7B 换取吞吐与工期。

> 实施进度与每日实测见 [DEVLOG.md](DEVLOG.md)。7 天 MVP 已全链路打通(开发机 3090/Vulkan 实测;目标机 Strix Halo 待部署验证)。

---

## 5. 快速开始 (Quickstart)

```bash
# 0) 装依赖(本项目用 uv 管理虚拟环境)
uv venv --python 3.10 .venv
uv pip install --python .venv/bin/python -r requirements.txt

# 1) 起推理服务(开发机 3090 走 Vulkan 预编译二进制;部署机 Strix Halo 同样 Vulkan)
scripts/fetch_llama_prebuilt.sh vulkan          # 下预编译二进制(免编译)
#   把 GGUF 放到 ./models/,然后:
scripts/serve_llama_prebuilt_vulkan.sh          # 起 llama-server(:8080)

# 2) 解析 + 建索引(D1+D2)
.venv/bin/python -m cli index https://github.com/pallets/click

# 3) 生成文档(D4) → MkDocs 站点
.venv/bin/python -m cli doc click
mkdocs serve -f docs/click/mkdocs.yml           # 浏览器查看文档站

# 4) 问答(D5,带 file:line 引用)
.venv/bin/python -m cli ask click "How does it parse command line options?"

# 5) 演示界面(可选)
REPO=click chainlit run app.py                  # Chainlit 问答 UI

# 验证脚本
.venv/bin/python -m scripts.verify_cache_prompt    # KV cache 收益
.venv/bin/python -m scripts.verify_skill_switch click  # 切 Skill 缓存复用
.venv/bin/python -m eval.run_eval click            # 问答评测通过率
```

---

## 附：目录结构（实际）
```
api_doc/
├── README.md              # 本提案
├── DEVLOG.md              # 每日实施日志(含实测数据)
├── cli.py                 # G. 统一 CLI 入口(index/doc/ask/skill)
├── app.py                 # G. Chainlit 问答演示
├── common/                # 共享数据结构(RepoMap/FileInfo/SymbolInfo)+ 配置
├── ingestion/             # A. clone / 文件树 / tree-sitter 解析
├── indexing/              # B. 分块 / 向量索引(Chroma) / 符号索引(SQLite) / 检索
├── inference/             # C. llama-server(OpenAI 接口)客户端封装
├── skills/                # D. 稳定前缀 + architecture/frontend/backend/qa
├── docgen/                # E. map-reduce 摘要 + MkDocs 渲染
├── qa/                    # F. 问答 Agent 工具循环
├── scripts/               # llama.cpp 构建/启动 + 验证脚本
└── eval/                  # 评测脚本
```
