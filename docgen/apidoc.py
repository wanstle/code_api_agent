"""API 参考生成(调用链驱动)。

流程(对应需求):
  ① 静态建调用图(callgraph,无 LLM)。
  ② 对每个函数,用显式栈沿调用图收集底层被调函数(签名)作为上下文。
  ③ AI 读"本函数源码 + 底层被调函数签名"生成描述(**不使用作者 docstring**)。
  ④ 记录直接被调,供渲染「内部调用」小节 + 链接。
签名仍逐字 copy 自代码(不经 LLM)。范围:公开 + 私有,跳过测试目录。
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path

from common.gpu import check_memory, MemoryLowError
from common.models import RepoMap, SymbolInfo
from indexing.builder import index_dir_for
from indexing.callgraph import CallGraph
from ingestion.filetree import scan_files
from ingestion.parse import parse_repo
from skills.session import SkillSession

MAX_BODY_LINES = 40
MAX_CLOSURE = 12            # 喂给 LLM 的底层被调函数数量上限
CLOSURE_DEPTH = 2
DEFAULT_MAX_LLM = 60
MIN_FREE_MEM_MIB = 3000    # 空闲内存(显存/统一内存)低于此值就提前停止,防 OOM
SAVE_EVERY = 15            # 每生成多少个就存一次缓存(防崩溃丢进度)
CHECK_EVERY = 5            # 每隔几个符号查一次内存(降低 nvidia-smi 调用开销)


def _is_test(path: str) -> bool:
    p = path.lower()
    return p.startswith(("test", "tests/")) or "/test" in p or "test_" in p


def _module_of(path: str) -> str:
    parts = path.split("/")
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]


@dataclass
class APIEntry:
    symbol: SymbolInfo
    body_md: str                              # AI 生成的描述(不含签名)
    doc_source: str                           # "ai" | "none"
    callee_keys: list[str] = field(default_factory=list)   # 直接库内被调(file:line)


@dataclass
class GenResult:
    by_module: dict[str, list[APIEntry]]
    by_key: dict[str, APIEntry]
    generated: int
    reused: int
    pending: int
    status: str       # "done"(全覆盖) | "budget"(预算用尽) | "lowmem"(内存不足中止) | "error"


def _reparse(index_name: str) -> RepoMap:
    meta = json.loads((index_dir_for(index_name) / "meta.json").read_text("utf-8"))
    root = Path(meta["root"])
    return parse_repo(root, scan_files(root))


def _body_source(root: Path, s: SymbolInfo, max_lines: int = MAX_BODY_LINES) -> str:
    try:
        lines = (root / s.file).read_text("utf-8", "replace").splitlines()
    except OSError:
        return ""
    end = min(s.end_line, s.start_line + max_lines - 1, len(lines))
    return "\n".join(lines[s.start_line - 1 : end])


def generate_api(
    index_name: str, max_llm: int = DEFAULT_MAX_LLM, progress=print
) -> GenResult:
    """生成一批 API 描述(抽取优先 + 调用链上下文),返回 GenResult。"""
    repo = _reparse(index_name)
    root = Path(repo.root)
    cg = CallGraph(repo)
    session = SkillSession(index_name)

    # 持久化缓存:已生成的符号存盘复用,本次只补未生成的(可多次运行直到全覆盖)
    cache_path = index_dir_for(index_name) / "apidoc_cache.json"
    cache: dict = json.loads(cache_path.read_text("utf-8")) if cache_path.exists() else {}

    # 收集非测试符号,按模块分组(源码优先于 examples 用 LLM 预算)
    modules: dict[str, list[SymbolInfo]] = {}
    methods_by_class: dict[tuple[str, str], list[SymbolInfo]] = {}
    for fi in repo.files:
        if _is_test(fi.path):
            continue
        for s in fi.symbols:
            modules.setdefault(_module_of(fi.path), []).append(s)
            if s.parent:  # 方法:登记到所属类
                methods_by_class.setdefault((fi.path, s.parent), []).append(s)
    ordered = sorted(modules.items(), key=lambda kv: ("example" in kv[0].lower(), kv[0]))

    def _save() -> None:
        cache_path.write_text(json.dumps(cache, ensure_ascii=False), "utf-8")

    llm_used = 0
    reused = 0
    abort_reason = None    # None | "lowmem" | "error"
    since_save = 0
    seen = 0
    by_module: dict[str, list[APIEntry]] = {}
    by_key: dict[str, APIEntry] = {}
    for mod, syms in ordered:
        entries: list[APIEntry] = []
        for s in syms:
            key = cg.key_of(s)
            callee_keys = cg.callees(key)
            fp = _fingerprint(s)
            cached = cache.get(key)
            if cached and cached.get("hash") == fp:
                entry = APIEntry(s, cached["desc"], cached["src"], callee_keys)  # 复用,不调 LLM
                reused += 1
            elif (abort_reason is None) and llm_used < max_llm:
                try:
                    seen += 1
                    if seen % CHECK_EVERY == 0:
                        check_memory(MIN_FREE_MEM_MIB)   # 内存看门狗:不足则在调 LLM 前就停
                    if s.kind == "class":
                        desc = _describe_class(session, s, methods_by_class.get((s.file, s.name), []))
                    else:
                        desc = _describe(session, cg, root, s, key)
                except MemoryLowError as e:
                    progress(f"  ⚠ {e};已保存进度,提前停止")
                    _save(); abort_reason = "lowmem"
                    entry = APIEntry(s, "", "none", callee_keys)
                except Exception as e:  # 服务崩溃/连接中断等
                    progress(f"  ⚠ 生成失败:{type(e).__name__}: {e};已保存进度,提前停止")
                    _save(); abort_reason = "error"
                    entry = APIEntry(s, "", "none", callee_keys)
                else:
                    entry = APIEntry(s, desc, "ai", callee_keys)
                    cache[key] = {"hash": fp, "desc": desc, "src": "ai"}
                    llm_used += 1
                    since_save += 1
                    if since_save >= SAVE_EVERY:   # 增量存盘,崩溃最多丢 SAVE_EVERY 个
                        _save(); since_save = 0
            else:
                entry = APIEntry(s, "", "none", callee_keys)  # 预算用尽或已中止
            entries.append(entry)
            by_key[key] = entry
        by_module[mod] = entries
        progress(f"  模块 {mod}: {len(entries)} 符号(本次新生成 {llm_used}/{max_llm}, 复用 {reused})")

    _save()
    total = sum(len(v) for v in by_module.values())
    pending = total - reused - llm_used
    if abort_reason:
        status = abort_reason
    elif pending == 0:
        status = "done"
    else:
        status = "budget"
    tail = {"done": "(已全覆盖)", "budget": "(再运行一批可续)",
            "lowmem": "(内存不足提前停,重启释放后可续)", "error": "(服务异常,已保存进度)"}[status]
    progress(f"API:{total} 符号 · 复用 {reused} · 新生成 {llm_used} · 待生成 {pending}{tail}")
    return GenResult(by_module, by_key, llm_used, reused, pending, status)


def _fingerprint(s: SymbolInfo) -> str:
    """符号指纹:签名或 kind 变了才需要重新生成。"""
    return hashlib.md5(f"{s.kind}\n{s.signature}".encode("utf-8")).hexdigest()


def _describe(session: SkillSession, cg: CallGraph, root: Path, s: SymbolInfo, key: str) -> str:
    body = _body_source(root, s)
    closure = cg.closure(key, max_depth=CLOSURE_DEPTH)[:MAX_CLOSURE]
    ctx_lines = []
    for ck in closure:
        cs = cg.symbol(ck)
        if cs:
            ctx_lines.append(f"- {cs.qualified_name()}{_short_sig(cs)}")
    closure_ctx = "\n".join(ctx_lines) if ctx_lines else "(无库内调用)"

    task = (
        f"为以下 {s.kind} 写 API 文档(只依据代码,不要复述代码,不要重复签名):\n"
        f"名称: {s.qualified_name()}\n签名:\n```\n{s.signature}\n```\n"
        f"函数体:\n```\n{body}\n```\n"
        f"它(递归)调用到的库内函数,供你理解其底层行为:\n{closure_ctx}\n\n"
        f"请输出:第一行一句话用途;随后 **Parameters** / **Returns** / **Raises**(若有)。"
    )
    return session.run("apidoc", task, max_tokens=320, temperature=0.2).text.strip()


def _describe_class(session: SkillSession, s: SymbolInfo, methods: list[SymbolInfo]) -> str:
    method_lines = [f"- {m.name}{_short_sig(m)}" for m in methods[:25]]
    methods_ctx = "\n".join(method_lines) if method_lines else "(无方法)"
    task = (
        f"为以下 class 写 API 文档(只依据代码,不要复述代码):\n"
        f"名称: {s.qualified_name()}\n签名:\n```\n{s.signature}\n```\n"
        f"它的方法:\n{methods_ctx}\n\n"
        f"请输出:第一行一句话说明这个类代表什么、承担什么职责;"
        f"随后用 Markdown 简述它的关键方法与典型用法。"
    )
    return session.run("apidoc", task, max_tokens=320, temperature=0.2).text.strip()


def _short_sig(s: SymbolInfo) -> str:
    """取签名里括号部分,简短表示。"""
    sig = s.signature
    i = sig.find("(")
    return sig[i:] if i != -1 else ""
