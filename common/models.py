"""贯穿各模块的核心数据结构。

D1 只用到 FileInfo / SymbolInfo / RepoMap;后续 D2 的索引、D4 的文档生成
都会复用这些结构,所以放在 common 里统一定义。
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class SymbolInfo:
    """一个代码符号(函数/类/方法)。"""

    name: str
    kind: str          # "function" | "class" | "method" | ...
    file: str          # 相对仓库根的路径
    start_line: int    # 1-based
    end_line: int
    parent: Optional[str] = None   # 所属类名(方法时填)
    # --- API doc 用:确定性抽取,不经 LLM ---
    signature: str = ""                          # 逐字签名(节点起点→body 之间的源码)
    docstring: Optional[str] = None              # 已有 docstring / JSDoc(逐字,作者权威文档)
    decorators: list[str] = field(default_factory=list)  # 装饰器(如 @property)
    calls: list[str] = field(default_factory=list)       # 函数体里调用到的名字(原始,未解析)

    @property
    def is_private(self) -> bool:
        return self.name.startswith("_")

    def qualified_name(self) -> str:
        return f"{self.parent}.{self.name}" if self.parent else self.name

    def location(self) -> str:
        """返回 file:line 形式的引用,贯穿全项目的溯源格式。"""
        return f"{self.file}:{self.start_line}"


@dataclass
class FileInfo:
    """一个被纳入分析的文件。"""

    path: str          # 相对仓库根
    language: str      # 语言标识(tree-sitter 名),无法识别为 "unknown"
    size_bytes: int
    lines: int
    symbols: list[SymbolInfo] = field(default_factory=list)


@dataclass
class RepoMap:
    """一次仓库解析的产物:文件树 + 全量符号。

    这是 D1 的核心交付物,也是后续"共享前缀(仓库概览)"和索引的输入。
    """

    root: str                       # 本地路径
    name: str                       # 仓库名
    files: list[FileInfo] = field(default_factory=list)

    # --- 便捷统计 ---
    @property
    def num_files(self) -> int:
        return len(self.files)

    @property
    def num_symbols(self) -> int:
        return sum(len(f.symbols) for f in self.files)

    @property
    def total_lines(self) -> int:
        return sum(f.lines for f in self.files)

    def language_breakdown(self) -> dict[str, int]:
        """各语言文件数,用于技术栈概览。"""
        out: dict[str, int] = {}
        for f in self.files:
            out[f.language] = out.get(f.language, 0) + 1
        return dict(sorted(out.items(), key=lambda kv: -kv[1]))

    def to_dict(self) -> dict:
        return asdict(self)
