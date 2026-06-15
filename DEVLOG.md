# DEVLOG — 动态 lens + 确定性事实 + AMD 多机部署

> 本阶段记录(2026-06)。提案/快速开始见 [README.md](README.md)。
> 主线:把固定的 frontend/backend skill 换成**按仓库动态生成的"分析视角(lens)"**,
> 并用**确定性抽取的事实**锁住文档精度;在 AMD Strix Halo 集群上离线验证。

## 一、部署与基础设施(AMD Strix Halo)

- **机器**:`aup-SHC2-395-2` / `395-3`,均为 AMD RYZEN AI MAX+ 395 / Radeon 8060S(gfx1151)。
  **共享同一 NFS home**,故代码/venv/模型/索引一处生效。
  - 395-3:系统内存 ~62G;395-2:**GPU VRAM 96G / 系统内存仅 30G**(BIOS UMA 划分相反)。
- **取数路径**(集群网络):github 网页 ✓ / pypi ✓ / **HF 直连 ✗**,但 **hf-mirror.com ✓**、release CDN ✓;
  **codeload(源码 tarball/git)✗** → 源码用"**dev 机下载 → scp 到集群**"。
- **推理**:`Qwen3-Coder-30B-A3B` Q4_K_M(~18.6G,进 VRAM),llama.cpp 预编译 **Vulkan** 二进制;
  bounded 配置 `--ctx 8192 --parallel 1`,内存有界。
- **内存看门狗** [common/gpu.py](common/gpu.py):跨平台,采集 **GPU(nvidia-smi / AMD sysfs vram+gtt)与系统内存(/proc/meminfo)**,
  取**最紧值**——在 395-2 上正确盯住 30G 系统内存(而非被 96G 显存误导)。实测加载 30B 后系统仍 ~28G 可用,安全。

## 二、动态 lens(替换固定 FE/BE skill)

- [docgen/lens.py](docgen/lens.py):为每个模块用 **JSON 约束输出**生成 `{role, focus[], sections[]}`,
  持久化到 `.cache/index/<repo>/lenses.json`(**可人工编辑**,`--force` 才覆盖)。
- **保守化**(防以偏概全):告知 LLM 只看到部分文件、role 用「涉及/包含…等(基于部分文件推断)」、
  约束经 `_lens_block` 传导到文档生成(覆盖 base prompt 的笃定语气)。
- **0 符号模块跳过**:标 `low-signal`、不调 LLM、不注入文档(避免靠文件名瞎猜)。

## 三、确定性事实优先(精度)

- [ingestion/parse.py](ingestion/parse.py):确定性抽取 **签名 / 调用 / 真实 raise**(走 AST,不经 LLM)。
- **raises 注入** [summarize.py](docgen/summarize.py):把"真实 raise 清单"作为权威事实注入 doc + 约束"Raises 只能来自此清单" → **假 Raises 根治**。
- **签名**:prompt 约束"照抄"**不可靠**(LLM 用先验硬加类型);改为**靠 [apidoc.py](docgen/apidoc.py) 逐字渲染**(LLM 不经手签名)。
- **关键认知**:prompt 能管「省略类」事实(raises:要不要写),**管不住「覆盖强先验类」**(签名:用我给的别用你脑里的)——后者必须程序直接写进产物。
- [ingestion/filetree.py](ingestion/filetree.py):`.h → cpp`(C++ 头文件;cpp 语法也能解析 C 头),修复 C++ 仓库头文件解析。

## 四、跨仓库验证结论(lens 的适用面)

| 仓库 | 语言/规模 | lens 效果 | 说明 |
|------|-----------|-----------|------|
| **click** | Python,小 | 边际 | base prompt 已够好,lens 提升不明显 |
| **ceres-solver** | C++,大 | 救不了 | 瓶颈在**抽取**:模板/trait/宏噪声 + 大模块采样偏差,非 prompt 能解 |
| **scrapy** | Python,复杂 | **有正收益** | 模块功能多样 → lens 区分度高、准确;文档**覆盖更全 + 更不编造**(TypedDict 默认值标 `(unknown)` 而非假 `None`,补齐 H2 类) |

→ **lens 适用于:复杂、且抽取干净(Python)的仓库。** 简单库边际、噪声大的 C++ 被抽取拖累。

## 五、当前架构(事实 vs LLM 分工)

```
解析(程序,确定性)→ 签名 / 调用 / raise / 符号层级   ← 事实,不会错
        │ 喂为权威事实 + 约束
LLM 只判断语义:模块 lens(干嘛的)、函数描述;签名走 apidoc 逐字渲染,Raises 受事实约束
```

## 六、待办 / 下一步杠杆
- **C++ 抽取降噪**:过滤 `std::` 特化 / trait 辅助 / 宏 / 外部 typedef,优先项目命名空间符号 —— ceres 文档质量的真正杠杆。
- **大模块采样**:`internal/ceres`(499 文件)只取 top-8,代表性不足;需更好的采样/再分组。
- **apidoc 全覆盖成本**:大仓库符号多(scrapy 6520),逐符号生成需分批/挑公开接口。
- `--use-lens` 默认是否打开(scrapy 上验证有益;click 上边际)。
