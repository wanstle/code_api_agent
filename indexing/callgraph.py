"""静态调用图:把函数体里抽到的"调用名"解析成库内符号,并支持闭包收集。

解析是近似的(动态分派/同名/import 别名做不到 100%),用
"同文件 → 同类 → 全局唯一"的优先级尽量准;解析不到的(外部/标准库/歧义)忽略。
"""

from __future__ import annotations

from common.models import RepoMap, SymbolInfo

# 这些名字是内建/常见 stdlib 方法,直接不当库内调用(降噪;近似,无法穷尽)
_BUILTINS = {
    # 内建函数
    "len", "str", "int", "float", "bool", "list", "dict", "set", "tuple", "frozenset",
    "isinstance", "issubclass", "type", "print", "range", "enumerate", "zip", "map",
    "filter", "open", "super", "cast", "getattr", "setattr", "hasattr", "delattr",
    "repr", "sorted", "reversed", "any", "all", "min", "max", "sum", "abs", "iter", "next",
    "vars", "dir", "id", "hash", "ord", "chr", "bytes", "bytearray", "callable",
    # 常见 dict/list/set/str 方法(易误配)
    "join", "append", "extend", "insert", "remove", "pop", "popitem", "clear",
    "items", "keys", "values", "get", "update", "copy", "add", "discard", "index",
    "count", "split", "rsplit", "splitlines", "strip", "lstrip", "rstrip",
    "startswith", "endswith", "lower", "upper", "title", "capitalize", "replace",
    "format", "encode", "decode", "find", "rfind", "ljust", "rjust", "zfill",
    # 常见 IO/通用方法
    "read", "readline", "readlines", "write", "writelines", "flush", "close",
    "seek", "tell", "send", "recv", "setdefault",
}


def _key(s: SymbolInfo) -> str:
    return f"{s.file}:{s.start_line}"


class CallGraph:
    def __init__(self, repo: RepoMap) -> None:
        self._by_key: dict[str, SymbolInfo] = {}
        self._by_name: dict[str, list[SymbolInfo]] = {}
        for fi in repo.files:
            for s in fi.symbols:
                self._by_key[_key(s)] = s
                if s.kind in ("function", "method", "class"):
                    self._by_name.setdefault(s.name, []).append(s)
        # caller_key -> [callee_key](已解析、去重、去自环)
        self._edges: dict[str, list[str]] = {}
        for s in self._by_key.values():
            self._edges[_key(s)] = self._resolve_edges(s)

    def _resolve_edges(self, caller: SymbolInfo) -> list[str]:
        out: list[str] = []
        seen: set[str] = set()
        for name in caller.calls:
            if name in _BUILTINS:
                continue
            target = self._resolve(caller, name)
            if target is None:
                continue
            k = _key(target)
            if k != _key(caller) and k not in seen:
                seen.add(k)
                out.append(k)
        return out

    def _resolve(self, caller: SymbolInfo, name: str) -> SymbolInfo | None:
        cands = self._by_name.get(name)
        if not cands:
            return None
        same_file = [c for c in cands if c.file == caller.file]
        if len(same_file) == 1:
            return same_file[0]
        if same_file:
            same_class = [c for c in same_file if c.parent == caller.parent]
            return (same_class or same_file)[0]
        if len(cands) == 1:
            return cands[0]
        return None  # 跨文件歧义,宁可不连也不连错

    # --- 查询接口 ---
    def symbol(self, key: str) -> SymbolInfo | None:
        return self._by_key.get(key)

    def key_of(self, s: SymbolInfo) -> str:
        return _key(s)

    def callees(self, key: str) -> list[str]:
        """直接库内被调(一层)。"""
        return self._edges.get(key, [])

    def closure(self, key: str, max_depth: int = 2) -> list[str]:
        """用显式栈沿调用图收集被调函数(深度≤max_depth,去重防环)。"""
        visited: set[str] = {key}
        result: list[str] = []
        stack: list[tuple[str, int]] = [(c, 1) for c in self.callees(key)]
        while stack:
            k, depth = stack.pop(0)  # 广度优先,层次更自然
            if k in visited:
                continue
            visited.add(k)
            result.append(k)
            if depth < max_depth:
                for c in self.callees(k):
                    if c not in visited:
                        stack.append((c, depth + 1))
        return result
