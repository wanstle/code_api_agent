"""tree-sitter 解析:从源码抽取函数/类/方法符号。

做法:对每个文件按其语言拿到 parser,遍历语法树,挑出"函数/类"类型的节点,
取其名字与起止行。方法(类内函数)会带上 parent 类名。

刻意保持简单:不写每语言的 .scm 查询,而是用一张
{语言 -> {节点类型 -> 符号种类}} 的映射 + 通用取名逻辑覆盖主流语言。
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from tree_sitter_language_pack import get_parser

from common.models import FileInfo, RepoMap, SymbolInfo

# 每语言:语法树节点类型 → 符号种类("function"/"class")。
# "function" 若处于某个 class 之内,会自动改记为 "method"。
LANG_NODE_TYPES: dict[str, dict[str, str]] = {
    "python": {"function_definition": "function", "class_definition": "class"},
    "javascript": {
        "function_declaration": "function",
        "method_definition": "method",
        "class_declaration": "class",
    },
    "typescript": {
        "function_declaration": "function",
        "method_definition": "method",
        "class_declaration": "class",
        "interface_declaration": "class",
    },
    "tsx": {
        "function_declaration": "function",
        "method_definition": "method",
        "class_declaration": "class",
        "interface_declaration": "class",
    },
    "java": {
        "method_declaration": "method",
        "constructor_declaration": "method",
        "class_declaration": "class",
        "interface_declaration": "class",
    },
    "go": {
        "function_declaration": "function",
        "method_declaration": "method",
        "type_declaration": "class",  # 近似:struct/interface 都在 type 下
    },
    "rust": {
        "function_item": "function",
        "struct_item": "class",
        "enum_item": "class",
        "trait_item": "class",
        "impl_item": "class",
    },
    "c": {"function_definition": "function", "struct_specifier": "class"},
    "cpp": {
        "function_definition": "function",
        "class_specifier": "class",
        "struct_specifier": "class",
    },
    "csharp": {
        "method_declaration": "method",
        "class_declaration": "class",
        "interface_declaration": "class",
        "struct_declaration": "class",
    },
    "ruby": {"method": "method", "class": "class", "module": "class"},
    "php": {
        "function_definition": "function",
        "method_declaration": "method",
        "class_declaration": "class",
    },
}

# 解析失败/不支持的语言会被记下,便于评估覆盖率。
_parser_cache: dict[str, object] = {}


def _get_parser(language: str):
    if language not in _parser_cache:
        _parser_cache[language] = get_parser(language)
    return _parser_cache[language]


def parse_repo(repo_root: Path, files: list[FileInfo]) -> RepoMap:
    """对 scan_files 得到的文件逐个抽符号,填回 FileInfo.symbols。"""
    repo_root = Path(repo_root).resolve()
    for fi in files:
        types = LANG_NODE_TYPES.get(fi.language)
        if not types:
            continue  # 暂不支持抽符号的语言,跳过(文件本身仍在树里)
        try:
            raw = (repo_root / fi.path).read_bytes()
            fi.symbols = _extract_symbols(raw, fi.language, fi.path, types)
        except Exception:
            # 单文件解析失败不应中断整仓;留空符号即可。
            fi.symbols = []

    return RepoMap(root=str(repo_root), name=repo_root.name, files=files)


def _extract_symbols(
    raw: bytes, language: str, rel_path: str, types: dict[str, str]
) -> list[SymbolInfo]:
    # 注:tree-sitter-language-pack 的绑定 parse() 收 str,且按 UTF-8 计算
    # byte 偏移。为让 start_byte/end_byte 与切片一致,统一用 text 的 UTF-8 编码做参照。
    text = raw.decode("utf-8", "replace")
    ref = text.encode("utf-8")

    parser = _get_parser(language)
    root = parser.parse(text).root_node()
    symbols: list[SymbolInfo] = []

    def visit(node, parent_class: Optional[str]) -> None:
        kind = types.get(node.kind())
        cur_class = parent_class
        if kind:
            name = _node_name(node, ref)
            if name:
                effective = kind
                if kind == "function" and parent_class is not None:
                    effective = "method"
                symbols.append(
                    SymbolInfo(
                        name=name,
                        kind=effective,
                        file=rel_path,
                        start_line=node.start_position().row + 1,
                        end_line=node.end_position().row + 1,
                        parent=parent_class,
                    )
                )
                if kind == "class":
                    cur_class = name
        for i in range(node.child_count()):
            visit(node.child(i), cur_class)

    visit(root, None)
    return symbols


def _node_name(node, ref: bytes) -> Optional[str]:
    """取符号名:优先 name 字段,退而求其次找标识符子节点。"""
    name_node = node.child_by_field_name("name")
    if name_node is not None:
        return ref[name_node.start_byte() : name_node.end_byte()].decode("utf-8", "replace")

    for i in range(node.child_count()):
        child = node.child(i)
        if child.kind() in ("identifier", "type_identifier", "constant", "name"):
            return ref[child.start_byte() : child.end_byte()].decode("utf-8", "replace")
    return None
