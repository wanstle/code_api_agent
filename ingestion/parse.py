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
                        signature=_signature(node, ref),
                        docstring=_docstring(node, ref, language),
                        decorators=_decorators(node, ref),
                        calls=_calls(node, ref) if effective in ("function", "method") else [],
                        raises=_raises(node, ref) if effective in ("function", "method") else [],
                    )
                )
                if kind == "class":
                    cur_class = name
        for i in range(node.child_count()):
            visit(node.child(i), cur_class)

    visit(root, None)
    return symbols


def _decode(ref: bytes, a: int, b: int) -> str:
    return ref[a:b].decode("utf-8", "replace")


def _signature(node, ref: bytes) -> str:
    """逐字签名:节点起点 → body 起点 之间的源码(语言无关)。

    去掉尾部的块起始符(`:` / `{`),多行签名原样保留。
    """
    body = node.child_by_field_name("body")
    if body is not None:
        sig = _decode(ref, node.start_byte(), body.start_byte())
    else:
        # 无 body 字段(接口/结构体/类型等):取节点首行
        whole = _decode(ref, node.start_byte(), node.end_byte())
        sig = whole.splitlines()[0] if whole else ""
    sig = sig.strip()
    # 去掉从 body 第一行泄漏进来的行注释(Python '#' / C 系 '//'),仅当注释出现在参数表 ')' 之后,
    # 以免误伤默认值里的 '#'(如 color="#fff")
    for cmt in ("#", "//"):
        i = sig.find(cmt)
        if i != -1 and ")" in sig[:i]:
            sig = sig[:i].strip()
    while sig.endswith((":", "{", "=", "(")):
        sig = sig[:-1].strip()
    return sig


def _docstring(node, ref: bytes, language: str) -> Optional[str]:
    """已有文档:Python 取 body 首个字符串字面量;类 C 语言取前导 /** */ 注释。"""
    if language in ("python",):
        return _python_docstring(node, ref)
    return _preceding_jsdoc(node, ref)


def _python_docstring(node, ref: bytes) -> Optional[str]:
    body = node.child_by_field_name("body")
    if body is None or body.named_child_count() == 0:
        return None
    first = body.named_child(0)
    # 文档串可能直接是 string 节点,或包在 expression_statement 里(取决于 grammar 版本)
    s = None
    if first.kind() == "string":
        s = first
    elif first.kind() == "expression_statement" and first.named_child_count() > 0:
        cand = first.named_child(0)
        if cand.kind() == "string":
            s = cand
    if s is None:
        return None
    return _clean_pystring(_decode(ref, s.start_byte(), s.end_byte()))


def _preceding_jsdoc(node, ref: bytes) -> Optional[str]:
    """JS/TS/Java 等:取紧邻在符号前的 /** ... */ 块注释。"""
    parent = node.parent()
    if parent is None:
        return None
    prev = None
    for i in range(parent.child_count()):
        ch = parent.child(i)
        if ch.start_byte() == node.start_byte() and ch.end_byte() == node.end_byte():
            break
        prev = ch
    if prev is not None and prev.kind() in ("comment", "block_comment"):
        txt = _decode(ref, prev.start_byte(), prev.end_byte())
        if txt.lstrip().startswith("/**"):
            return _clean_jsdoc(txt)
    return None


def _decorators(node, ref: bytes) -> list[str]:
    """Python 装饰器:父节点为 decorated_definition 时收集其 decorator 子节点。"""
    parent = node.parent()
    if parent is None or parent.kind() != "decorated_definition":
        return []
    out = []
    for i in range(parent.child_count()):
        ch = parent.child(i)
        if ch.kind() == "decorator":
            out.append(_decode(ref, ch.start_byte(), ch.end_byte()).strip())
    return out


# 各语言里"函数调用"节点的 kind(用于抽调用名)
_CALL_KINDS = {
    "call", "call_expression", "method_invocation",
    "function_call_expression", "member_call_expression", "scoped_call_expression",
}
_ID_KINDS = {"identifier", "field_identifier", "property_identifier", "type_identifier"}


def _calls(node, ref: bytes) -> list[str]:
    """抽取函数体内调用到的名字(取被调表达式里最后一个标识符)。

    例:foo() → foo;self.parse_args() → parse_args;a.b.c() → c。
    只取名字、不解析归属;库内解析交给 callgraph(用符号表)。
    """
    body = node.child_by_field_name("body")
    if body is None:
        return []
    names: list[str] = []
    seen: set[str] = set()

    def walk(n) -> None:
        if n.kind() in _CALL_KINDS:
            callee = (
                n.child_by_field_name("function")
                or n.child_by_field_name("name")
                or (n.named_child(0) if n.named_child_count() > 0 else None)
            )
            nm = _last_identifier(callee, ref) if callee is not None else None
            if nm and nm not in seen:
                seen.add(nm)
                names.append(nm)
        for i in range(n.child_count()):
            walk(n.child(i))

    walk(body)
    return names


# raise/throw 语句节点(各语言)
_RAISE_KINDS = {"raise_statement", "throw_statement", "throw_expression"}


def _raises(node, ref: bytes) -> list[str]:
    """确定性抽取:函数体里真正 raise/throw 的异常类型名。

    只取真实抛出的异常类型(`raise ValueError(...)`→ValueError;`raise Err`→Err),
    不碰被 except 捕获的、也不碰消息里的标识符。
    """
    body = node.child_by_field_name("body")
    if body is None:
        return []
    out: list[str] = []
    seen: set[str] = set()

    def walk(n) -> None:
        if n.kind() in _RAISE_KINDS:
            exc = n.named_child(0) if n.named_child_count() > 0 else None
            name = None
            if exc is not None:
                if exc.kind() in ("call", "call_expression"):
                    callee = (exc.child_by_field_name("function")
                              or exc.child_by_field_name("name")
                              or (exc.named_child(0) if exc.named_child_count() > 0 else None))
                    name = _last_identifier(callee, ref) if callee is not None else None
                else:
                    name = _last_identifier(exc, ref)
            if name and name not in seen:
                seen.add(name)
                out.append(name)
        for i in range(n.child_count()):
            walk(n.child(i))

    walk(body)
    return out


def _last_identifier(node, ref: bytes) -> Optional[str]:
    """返回子树里最后出现的标识符文本(用于从 a.b.c 里取 c)。"""
    found = [None]

    def walk(n) -> None:
        if n.kind() in _ID_KINDS:
            found[0] = _decode(ref, n.start_byte(), n.end_byte())
        for i in range(n.child_count()):
            walk(n.child(i))

    walk(node)
    return found[0]


def _clean_pystring(raw: str) -> str:
    s = raw.strip()
    # 去掉字符串前缀 r/b/f/u(可组合)
    while s and s[0] in "rRbBfFuU" and len(s) > 1 and s[1] in "rRbBfFuU\"'":
        s = s[1:]
    for q in ('"""', "'''", '"', "'"):
        if s.startswith(q) and s.endswith(q) and len(s) >= 2 * len(q):
            s = s[len(q) : -len(q)]
            break
    return s.strip()


def _clean_jsdoc(raw: str) -> str:
    s = raw.strip()
    if s.startswith("/**"):
        s = s[3:]
    if s.endswith("*/"):
        s = s[:-2]
    lines = [ln.strip().lstrip("*").strip() for ln in s.splitlines()]
    return "\n".join(ln for ln in lines if ln).strip()


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
