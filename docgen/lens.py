"""模块分析视角(lens)生成 —— "LLM 自己生成 prompt"的第一环。

只负责:为每个模块生成一份结构化的分析视角 {role, focus[], sections[]},
持久化到 .cache/index/<repo>/lenses.json,供人工 review/编辑;
**不生成文档**(那是下一步,会读取这里的 lens)。

护栏:
  - JSON 约束输出(response_format=json_object)+ 校验 + 1 次重试 + 兜底,防循环/失控。
  - 增量缓存:已存在的模块不重算;--force 才覆盖(保护人工修改)。
  - 内存看门狗:低内存提前停、写盘保进度。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

from common.gpu import check_memory, MemoryLowError
from inference.client import LlamaClient
from indexing.builder import index_dir_for
from skills.prefix import build_repo_prefix
from docgen.summarize import _load, _group_modules, _module_context

CTX_CAP = 2500            # 单模块上下文字符上限(控制输入预算)
MIN_FREE_MEM_MIB = 3000   # 内存看门狗阈值
MAX_FOCUS = 6
MAX_SECTIONS = 6

_META = (
    "你是文档系统的「分析视角设计器」。下面给出本仓库某个模块的文件、符号和部分源码。\n"
    "请为**这个模块**设计一份专属的文档分析视角,具体到该模块本身、能体现差异,不要套话。\n"
    "**保守原则(重要)**:你看到的很可能只是该模块的**部分文件**(按符号数采样),不是全部。\n"
    "- role 用「包含/涉及/提供……等」描述**你实际观察到的**内容;"
    "**禁止**下「该模块就是/主要用于 X」这类以偏概全的结论。\n"
    "- 拿不准的领域用「等」带过或留空;宁可说少一点,也不要硬下定论或猜测未见到的部分。\n"
    "- 若只看到少数文件却推断整体用途,请在 role 末尾注明「(基于部分文件推断)」。\n"
    "**精确性原则(让据此生成的文档更准)**:\n"
    "- focus 的每一条都要**引用上面真实出现的符号名**(类/函数名),指向具体、可核对的对象;"
    "不要写无法对应到代码的抽象关注点。\n"
    "- focus 指向那些**最该被精确文档化**的关键符号(公开接口、核心类),而非边角。\n"
    "- 不要让后续文档臆测代码里看不到的参数/返回/异常/行为。\n"
    "**只输出一个 JSON 对象**,字段如下(中文填写):\n"
    '{"role": "一句话:基于观察到的内容,说明该模块涉及/包含什么", '
    '"focus": ["该模块文档应重点讲清的 3-5 个具体点(基于已见内容)"], '
    '"sections": ["建议的输出小节名,3-5 个"]}'
)


@dataclass
class Lens:
    module: str
    role: str
    focus: list[str] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)
    source: str = "ai"          # "ai" | "human" | "fallback"


def lenses_path(index_name: str) -> Path:
    return index_dir_for(index_name) / "lenses.json"


def load_lenses(index_name: str) -> dict[str, Lens]:
    p = lenses_path(index_name)
    if not p.exists():
        return {}
    raw = json.loads(p.read_text("utf-8"))
    return {m: Lens(**d) for m, d in raw.items()}


def _save(index_name: str, lenses: dict[str, Lens]) -> None:
    p = lenses_path(index_name)
    p.write_text(
        json.dumps({m: asdict(l) for m, l in lenses.items()}, ensure_ascii=False, indent=2),
        "utf-8",
    )


def _first_json(text: str) -> Optional[dict]:
    """取文本里第一个合法 JSON 对象(容多 JSON / 代码围栏)。"""
    dec = json.JSONDecoder()
    for i, ch in enumerate(text):
        if ch == "{":
            try:
                obj, _ = dec.raw_decode(text[i:])
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                return obj
    return None


def _to_lens(module: str, text: str) -> Optional[Lens]:
    obj = _first_json(text)
    if not obj or not isinstance(obj.get("role"), str) or not obj["role"].strip():
        return None
    focus = [str(x).strip() for x in obj.get("focus", []) if str(x).strip()][:MAX_FOCUS]
    sections = [str(x).strip() for x in obj.get("sections", []) if str(x).strip()][:MAX_SECTIONS]
    if not focus:
        return None
    return Lens(module=module, role=obj["role"].strip(), focus=focus, sections=sections, source="ai")


def generate_lenses(
    index_name: str, max_llm: int = 50, force: bool = False, progress=print
) -> dict[str, Lens]:
    """为各模块生成 lens(增量缓存)。返回 module -> Lens。"""
    client = LlamaClient()
    prefix = build_repo_prefix(index_name)
    meta, top, detail, snippets = _load(index_name)
    modules = _group_modules(meta, top)

    lenses = load_lenses(index_name)     # 已有的(含人工编辑)默认保留
    generated = reused = 0

    for mod, files in modules:
        if mod in lenses and not force:
            reused += 1
            continue
        # 0 符号模块:没有可依据的代码,不让 LLM 凭文件名瞎猜 → 标低置信、留待人工
        if sum(f.get("symbols", 0) for f in files) == 0:
            lenses[mod] = Lens(mod, "(该模块无可提取符号,跳过自动生成,建议人工补充)",
                               [], [], "low-signal")
            _save(index_name, lenses)
            progress(f"  lens: {mod}  (跳过:0 符号,标低置信)")
            continue
        if generated >= max_llm:
            continue
        try:
            check_memory(MIN_FREE_MEM_MIB)
        except MemoryLowError as e:
            progress(f"  ⚠ {e};已保存进度,提前停止")
            break

        ctx = _module_context(files, top, detail, snippets)[:CTX_CAP]
        cover = (f"模块 {mod}(该模块共 {len(files)} 个文件;"
                 f"以下仅展示其中符号数最高的若干个,可能不代表全部)")
        user = _META + f"\n\n{cover}\n{ctx}"
        msgs = [{"role": "system", "content": prefix}, {"role": "user", "content": user}]

        lens = None
        for _ in range(2):   # 1 次重试
            res = client.chat(msgs, max_tokens=350, temperature=0.3,
                              response_format={"type": "json_object"}, cache_prompt=True)
            lens = _to_lens(mod, res.text)
            if lens:
                break
        if lens is None:     # 兜底:标记待人工补
            lens = Lens(module=mod, role="(生成失败,待人工填写)", focus=[], sections=[], source="fallback")

        lenses[mod] = lens
        generated += 1
        _save(index_name, lenses)   # 增量存盘
        progress(f"  lens: {mod}  (source={lens.source}, focus={len(lens.focus)})")

    _save(index_name, lenses)
    progress(f"完成:{len(lenses)} 个模块 · 新生成 {generated} · 复用/保留 {reused} → {lenses_path(index_name)}")
    return lenses
