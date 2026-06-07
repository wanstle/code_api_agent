# 开发日志 (DEVLOG)

记录每天实际完成的工作、关键决策与偏差。提案见 [README.md](README.md)。

---

## Day 1 — 推理服务 + 解析骨架(2026-06-07)

### 目标(来自 README 时间线)
- 部署 llama.cpp(Vulkan)+ 验证 iGPU 推理与 `cache_prompt` 前缀缓存
- 仓库 clone + 文件树扫描 + tree-sitter 解析骨架
- **里程碑**:能解析仓库出文件树与函数/类清单;LLM 可本地推理

### 环境实况(重要)
- **开发机 ≠ 部署机**:开发机是 **RTX 3090(24GB)+ Intel GPU**,有外网;部署目标才是 **AMD Strix Halo / AI Max+ 395**。
- 开发机:Python 3.10、git、cmake、gcc 齐;**缺** CUDA toolkit(`nvcc`)、Vulkan 的 `glslc`;driver 580(支持 CUDA 13);Vulkan 可枚举到 3090(GPU0)。
- 无 `python3-venv`、sudo 非免密 → 改用 **uv** 建虚拟环境。

### 完成的工作

**1. 项目骨架**
- `requirements.txt`(分 D1/D2/D4 标注),`.gitignore`(排除 `.venv/.cache/models/third_party`)
- uv 建 `.venv` 并装 D1 依赖:GitPython、tree-sitter、tree-sitter-language-pack、openai、typer、rich
- [common/models.py](common/models.py):核心数据结构 `RepoMap / FileInfo / SymbolInfo`(贯穿后续索引与文档生成)
- [common/config.py](common/config.py):从环境变量读 llama-server 配置

**2. Ingestion / 解析层(已实测)**
- [ingestion/clone.py](ingestion/clone.py):本地路径直接用 / git URL 浅克隆;已克隆则复用(契合离线)
- [ingestion/filetree.py](ingestion/filetree.py):文件树扫描 + 扩展名识别语言;忽略 node_modules 等目录、跳过二进制/超大(>1MB)文件
- [ingestion/parse.py](ingestion/parse.py):tree-sitter 抽函数/类/方法,带 parent 类名与起止行
- [ingestion/cli.py](ingestion/cli.py):`python -m ingestion.cli <repo> --out x.json`,rich 表格输出 + 导出 JSON

**3. Inference / 推理层(代码完整)**
- [inference/client.py](inference/client.py):`LlamaClient` 封装 llama-server OpenAI 接口,支持 `cache_prompt`,采集 `prompt_ms` 与 `cached_tokens`
- [scripts/verify_cache_prompt.py](scripts/verify_cache_prompt.py):冷/热/对照三轮验证前缀缓存收益
- 部署脚本:[build_llama.sh](scripts/build_llama.sh)(cuda/vulkan/cpu 源码构建)、[fetch_llama_prebuilt.sh](scripts/fetch_llama_prebuilt.sh)(下预编译二进制)、[serve_llama_cuda.sh](scripts/serve_llama_cuda.sh)/[serve_llama_vulkan.sh](scripts/serve_llama_vulkan.sh)/[serve_llama_prebuilt_vulkan.sh](scripts/serve_llama_prebuilt_vulkan.sh)、[scripts/README.md](scripts/README.md)(部署+模型下载说明)

### 验证结果
- **解析骨架**:在 `pallets/click` 上跑通 —— **61 文件 / 26641 行 / 1838 符号**,正确区分 class/method/function、带 `file:line`。JS/TS/Go/Rust 多语言抽取也验证通过。
- **推理 + cache_prompt(已实测,3090 经 Vulkan)**:
  - 模型 Qwen2.5-Coder-7B-Instruct Q4_K_M,预编译 Vulkan 二进制 `b9548`,`-ngl 99` 全量卸载到 3090(显存占用 ~7.5GB,日志 `Vulkan0 : NVIDIA GeForce RTX 3090`)。
  - `verify_cache_prompt` 结果:

    | 轮次 | 端到端(ms) | prompt_ms(prefill) | cached_tokens |
    |------|-----------:|-------------------:|--------------:|
    | cold | 13241 | 13070 | 0 |
    | warm | 94 | 30 | 3790 |
    | ctrl | 116 | 64 | 3466 |

  - **结论:warm 轮 prefill 比 cold 快约 442×(13070ms→30ms),复用 3790 token**,证明"稳定前缀 + 可切换后缀"机制成立 ✅。
  - 注:cold 轮 13s 偏慢含首次 Vulkan 管线预热;ctrl 轮设计的"不同前缀"其实与前缀共享了前 55 段,所以也命中了缓存 —— 这反而印证了"最长公共前缀"匹配,但作为对照不够干净,D3 正式评测时换成真正无公共前缀的对照。

### 关键决策 / 踩坑
1. **vLLM → llama.cpp**:目标是 AMD APU,vLLM 不可行;统一走 llama.cpp,业务代码只依赖 OpenAI 兼容接口,后端可换。
2. **tree-sitter-language-pack 的绑定是非标准的**:`parse()` 收 str、`root_node()`/`kind()`/`child_count()`/`start_position().row`/`start_byte()` 全是方法(标准 `tree_sitter` 是 `.type`/`.children`/`.start_point`)。已据此适配 [parse.py](ingestion/parse.py)。
3. **CUDA 不可行的替代**:Linux 官方 release **无 CUDA 预编译**,且装 CUDA toolkit 需 sudo(非免密)。改用**预编译 Vulkan 二进制在 3090 上跑** —— 免编译、免 sudo,且 Vulkan 正是 Strix Halo 部署后端,更具代表性。

### 与计划的偏差
- README 中 D1 写"LLM 在 Radeon 8060S 上推理"是**目标机**的事;开发机上用 **3090(Vulkan)** 做等价验证。
- Go 的 struct 命名、Rust impl 去重为已知小瑕疵,留作后续优化,不影响骨架。

### D1 状态:✅ 完成(解析骨架 + 推理 + cache_prompt 均已实测通过)

### 交接到 D2
- D2:代码感知分块 + fastembed(CPU)embedding + Chroma 向量索引 + tree-sitter→SQLite 符号索引
- 复现推理测试:`scripts/fetch_llama_prebuilt.sh vulkan` → 放好 GGUF → `scripts/serve_llama_prebuilt_vulkan.sh` → `.venv/bin/python -m scripts.verify_cache_prompt`
- D3 正式评测时:把 `verify_cache_prompt` 的对照前缀换成真正无公共前缀的版本

---

## Day 2 — 索引层(2026-06-07)

### 目标(README 时间线)
代码感知分块 + fastembed(CPU)embedding + Chroma 向量索引 + tree-sitter→SQLite 符号索引 + 检索接口。**里程碑**:能对任意问题返回 top-k 相关代码片段。

### 完成的工作(全部实测)
- 装 D2 依赖:`fastembed` 0.8.0(ONNX/CPU)、`chromadb` 1.5.9(注:它把 typer 降到 0.25.1,已确认两个 CLI 仍正常)
- [indexing/chunk.py](indexing/chunk.py):**代码感知分块** —— 按顶层符号(class/function)切,符号间的模块级代码按行窗口聚合,无符号文件整文件窗口切,过大符号再拆。click → 1768 chunks
- [indexing/embed.py](indexing/embed.py):fastembed 封装(默认 `BAAI/bge-small-en-v1.5`,384 维,CPU)
- [indexing/vector_store.py](indexing/vector_store.py):Chroma 封装(cosine,自带向量传入,不用内置 EF,分批写)
- [indexing/symbol_index.py](indexing/symbol_index.py):SQLite 符号索引,精确/前缀按名查找(`allow_prefix` 控制)
- [indexing/builder.py](indexing/builder.py):一键构建(clone→解析→分块→向量化→双索引→meta.json),落 `.cache/index/<repo>/`
- [indexing/retrieve.py](indexing/retrieve.py):**混合检索**(符号精确命中优先 + 向量语义补充,按行区间重叠去重)
- [indexing/cli.py](indexing/cli.py):`build <repo>` / `query <repo-name> "问题" --k`

### 验证结果(click 仓库)
- 构建:1768 chunks 向量化 + 1838 符号入库
- 检索质量:
  - 语义查询 "how does it parse command line options and arguments" → 命中 `Command.parse_args` / `Group.parse_args`(正确答案)
  - 符号查询 "Option" → 精确命中 `class Option`(core.py:2805)
  - 纯语义 "how to show a progress bar while iterating" → 向量命中 `progressbar`(termui.py,score 0.82)

### 关键决策 / 调优
- **embedding 放 CPU**:把唯一的 iGPU 留给 LLM(索引是一次性开销),fastembed 也避免拉 PyTorch 重依赖。
- **混合检索去噪**:初版把自然语言里的普通词(如 "from")当符号前缀匹配,误命中 `from_bytes`。加了停用词表 + "仅对 code-ish token(含 `_`/大写)做前缀匹配",显著降噪。

### 已知小问题(留给 D3 调优)
- 自然语言查询里若某词恰好精确等于某方法名(如 "show"→`*.show`),符号精确命中可能挤占语义结果的排名。D3 做排序/权重调优时处理。

### D2 状态:✅ 完成(混合检索达标,top-k 相关片段可返回)

### 交接到 D3
- D3:Skill 框架 + 稳定前缀/可切换后缀 + 接入 `cache_prompt`,把 D2 检索结果作为问答种子上下文。

---

## Day 3 — Skill 框架 + KV cache(2026-06-07)

### 目标(README 时间线)
Skill 注册机制 + 稳定前缀/可切换后缀设计 + 接入 `cache_prompt` + 验证切换收益。**里程碑:MVP 闭环 —— 可切换 Skill,缓存命中率/切换延迟有数据。**

### 核心设计(对应 README 3.3)
**稳定前缀(仓库概览)放 system,跨 Skill 完全不变 → cache_prompt 命中;Skill 后缀 + 检索片段 + 任务放 user,每次切换。** 切 Skill 不动 system,前缀 KV 被复用。

### 完成的工作(全部实测)
- [indexing/builder.py](indexing/builder.py):meta 增加 `languages` + 紧凑 `files` 清单(供前缀构建)
- [skills/prefix.py](skills/prefix.py):**稳定前缀构建器** —— 压缩概览(技术栈 + 源码优先的关键文件与符号 + 通用规则),确定性排序、字符预算截断(~6000 char)保证 token 稳定
- [skills/base.py](skills/base.py):Skill 抽象 + 注册表;内置 4 个 Skill(模板型 `architecture`/`frontend`/`backend` + agent 型 `qa`),后缀放 user 消息
- [skills/session.py](skills/session.py):`SkillSession` —— 全程固定 system 前缀,切 Skill 只换 user,接 `cache_prompt`
- [skills/cli.py](skills/cli.py):`ask`(qa + D2 检索种子上下文)/ `run`(任意 Skill)/ `prefix`(查看前缀)
- [scripts/verify_skill_switch.py](scripts/verify_skill_switch.py):切 Skill 缓存复用验证

### 验证结果(click,3090/Vulkan,Qwen2.5-Coder-7B)
- **切 Skill 缓存复用**(稳定前缀 3662 字符 ≈ 915 token):

  | 步骤 | Skill | 阶段 | prompt_ms | cached_tokens |
  |------|-------|------|----------:|--------------:|
  | 1 | architecture | cold | 359 | 0 |
  | 2 | frontend | warm | 34 | 1168 |
  | 3 | backend | warm | 35 | 1168 |
  | 4 | qa | warm | 65 | 1168 |

  **结论:cold 359ms → warm 平均 45ms,约 8× 提速**,warm 轮复用 1168 个前缀 token(整段仓库概览)✅

- **MVP 端到端闭环**:`ask click "How does click parse command line options..."` → 检索 5 段 → qa skill 输出准确解释(正确点到 `src/click/core.py` 的 Command/Group、`parser.py` 的 OptionParser),带 file:line 来源,cached_tokens=1218。
- **模板型 Skill**:`run click architecture` 产出连贯架构总览(正确识别各模块),cached_tokens=1168。

### MVP 闭环达成
**parse(D1)→ index(D2)→ 检索 → 切 Skill(前缀缓存复用)→ 带引用回答** 全链路打通,且切换延迟/缓存命中有实测数据。

### 关键点 / 调优
- **前缀 token 稳定性**是 cache_prompt 命中的前提:所有取数确定性排序 + 预算截断,保证同一索引每次生成完全一致的前缀文本。
- 前缀概览**源码优先于测试文件**(初版测试文件按符号数排在最前,是噪声),已修正排序键 `(_is_test, -symbols)`。

### D3 状态:✅ 完成(MVP 闭环成立,切换收益与缓存命中有数据)

### 交接到 D4
- D4:层次化 map-reduce 文档生成(文件→模块→仓库),用 `architecture`/`frontend`/`backend` 三个模板型 Skill 产出文档;注意 map 阶段每文件内容不同,前缀缓存收益有限(符合 README 3.3 标定)。

---

## Day 4 — 文档生成(2026-06-07)

### 完成(全部实测,click)
- [docgen/summarize.py](docgen/summarize.py):**map-reduce 摘要** —— map 按模块(目录)生成摘要,reduce 汇总成整体架构文档;复用 `SkillSession`,system 仓库前缀跨所有调用复用 KV
- [docgen/render.py](docgen/render.py):渲染成 **MkDocs** 文档站(index.md + modules/*.md + mkdocs.yml)
- [docgen/cli.py](docgen/cli.py)
- **实测**:click → 12 个模块摘要 + 架构文档;map 阶段 warm 调用 cached_tokens≈1239(稳定前缀复用,印证 README 3.3:前缀复用、per-module 内容仍需 prefill);`mkdocs build` 成功产出 HTML 站点。
- 文档质量:架构总览准确(模块职责表 + 组件关系),`src/click` 模块摘要正确点出 core/types/exceptions/parser 等。

## Day 5 — qa Agent 工具循环(2026-06-07)

### 完成(全部实测)
- [qa/tools.py](qa/tools.py):只读工具 `read_file`/`grep`/`list_dir`,路径限制在仓库根内防越权
- [qa/agent.py](qa/agent.py):**ReAct 式 JSON 动作循环** —— 预检索种子上下文 + agent 按需调工具补充;system 固定仓库前缀,多轮对话前缀持续命中 cache_prompt
- [qa/cli.py](qa/cli.py)
- **实测**:问 "Where is the Option class defined and its parsing flow" → agent 自主 read_file(core.py)→ read_file(parser.py)→ final,带 file:line 引用,3 轮,cached_tokens 累积到 2947。

## Day 6 — 集成 + 评测 + 调优(2026-06-07)

### 完成
- [eval/run_eval.py](eval/run_eval.py):对一组已知答案的问题跑 qa Agent,检查是否引对文件,算通过率
- **调优**:初版评测 4/5。失败项 "exception classes" 因种子检索把**测试文件**的异常类排前、agent 直接采信。两处修:① [retrieve.py](indexing/retrieve.py) 合并排序加入 `源码优先于测试` 的键;② agent 提示"优先源码、不确定先 grep 查证"。**复测 5/5 = 100%**。

## Day 7 — 统一 CLI + 演示 + 收尾(2026-06-07)

### 完成
- [cli.py](cli.py):**统一入口** `index` / `doc` / `ask` / `skill`(对接 llama-server,后端无关)
- [app.py](app.py):**Chainlit 问答演示**(展示工具调用轨迹 + 引用 + 前缀复用),import 验证通过
- 演示依赖:`mkdocs-material` 9.7.6(已用真实 build 验证)、`chainlit` 2.11.1
- 收尾:requirements 转正、README 加"快速开始"、本 DEVLOG 补全

### 7 天 MVP 状态:✅ 全链路打通并实测
parse(D1)→ index(D2)→ Skill+KV cache(D3)→ 文档生成(D4)→ qa Agent(D5)→ 评测调优(D6)→ 统一 CLI + 演示(D7)。
- 推理实测:3090/Vulkan,Qwen2.5-Coder-7B;cache_prompt 单轮 442×、切 Skill 8× 提速。
- 问答评测:click 5/5。
- 文档:click 自动生成 MkDocs 站点。
- **注**:目标机 AMD Strix Halo 的实机验证待部署时进行(开发机用 3090/Vulkan 等价验证,后端一致)。
