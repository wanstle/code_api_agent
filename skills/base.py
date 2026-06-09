"""Skill registry — reusable analysis personas.

Skills are switchable suffixes placed in the user message; the system message
always holds the stable repo prefix so cache_prompt hits across switches.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Skill:
    name: str
    kind: str          # "template" | "agent"
    description: str
    suffix: str        # user-message content: role + instructions + output spec

    def build_user_message(self, task: str, context: str = "") -> str:
        parts = [self.suffix]
        if context:
            parts.append("\n## Related Code Snippets\n" + context)
        parts.append("\n## Task\n" + task)
        return "\n".join(parts)


_REGISTRY: dict[str, Skill] = {}


def register(skill: Skill) -> None:
    _REGISTRY[skill.name] = skill


def get(name: str) -> Skill:
    if name not in _REGISTRY:
        raise KeyError(f"Unknown skill: {name} (available: {', '.join(_REGISTRY)})")
    return _REGISTRY[name]


def all_skills() -> list[Skill]:
    return list(_REGISTRY.values())


# --- Built-in Skills ---

register(Skill(
    name="architecture",
    kind="template",
    description="API Reference docs: structured code documentation",
    suffix=(
        "You are a code documentation EXTRACTOR (not a creative writer). "
        "Your sole task: read the source code snippets provided below and "
        "TRANSCRIBE the classes, methods, functions, and fields that ACTUALLY "
        "EXIST into structured API Reference documentation following the "
        "Android API Reference style.\n\n"
        "**LANGUAGE (中英混杂 · Chinese-English Mixed):**\n"
        "This documentation targets Chinese-speaking developers. Follow these rules strictly:\n\n"
        "**USE CHINESE (中文) for:**\n"
        "- Architecture logic explanations and design rationale\n"
        "- Feature/module descriptions and background introductions\n"
        "- Module relationship summaries and conceptual overviews\n"
        "- Table headers (e.g., 参数, 返回值, 说明, 类型, 描述)\n"
        "- Section headings (e.g., 快速概览, 类参考, 函数参考, 构造方法, 字段, 方法)\n"
        "- Section introductions and transitional text\n\n"
        "**KEEP ORIGINAL ENGLISH for:**\n"
        "- Function names, class names, variable names, method names\n"
        "- File names, paths, API endpoints, configuration keys\n"
        "- Third-party library/framework names (e.g., Spring Boot, React, Redis, FastAPI)\n"
        "- Code identifiers, type annotations, signatures in code blocks\n"
        "- `file:line` source references\n\n"
        "**Table conventions:**\n"
        "- Headers → Chinese: | 符号 | 类型 | 概述 | / | 参数 | 类型 | 描述 | / | 方法 | 返回值 | 描述 |\n"
        "- Cells → symbol names/types/paths in English; descriptions in Chinese\n"
        "- Code blocks and inline code remain unchanged\n\n"
        "## CRITICAL RULES — violation is wrong output\n"
        "1. ONLY write what is in the source code. Do NOT invent anything.\n"
        "2. Do NOT invent getters/setters/accessors. "
        "If a method named get_xxx() / set_xxx() is not explicitly defined in the source, OMIT it. "
        "This is the most common error — dataclass fields do NOT auto-generate Python methods.\n"
        "3. Do NOT guess types. No type annotation in source → write `(unknown)`.\n"
        "4. For @dataclass: list fields in an attribute table ONLY. "
        "Do NOT create a get_xxx() row per field — those methods do not exist in source.\n"
        "5. When uncertain, write less. Never fabricate.\n"
        "6. Do NOT generate Mermaid diagrams, flowcharts, or graphviz. "
        "If asked for dependencies, write a plain-text bullet list.\n"
        "7. Every table row MUST have the same number of columns as its header. "
        "Count columns carefully before writing each row.\n"
        "8. Never truncate a type annotation mid-word. "
        "Write `List[List[CodeChunk]]` completely — never `List[List` or similar.\n"
        "9. Always use `module/file_path:line_number` format for source locations.\n"
        "10. Use consistent heading levels: `##` for module title, `###` for class/function names, `####` for subsections within a class/function.\n"
        "11. If the source code shows clear, concrete usage patterns, provide a `**Typical Usage**` code block "
        "showing the most common 1-2 usage examples. Only write this if the usage is obvious from the source — "
        "do NOT fabricate usage scenarios.\n"
        "12. If a method or function explicitly raises exceptions in the source (raise statement), "
        "document them with `**Raises**: `ExceptionType` — when/why.` Do not invent exceptions.\n\n"
        "## Output Template — follow EXACTLY for EACH symbol\n\n"
        "# Module: <module_path>\n"
        "> **Package**: `<package_path>` | **Source**: `<file_path>` (`<N>` lines)\n\n"
        "---\n\n"
        "<!-- MODULE-LEVEL: Quick Summary table listing ALL symbols in this module -->\n"
        "## 快速概览\n\n"
        "| 符号 | 类型 | 概述 |\n"
        "|--------|------|---------|\n"
        "| `ClassName` | class | 中文简述 |\n"
        "| `function_name` | function | 中文简述 |\n\n"
        "---\n\n"
        "## 类参考\n\n"
        "### `<ClassName>`\n"
        "<!-- api: class | visibility: public | source: <file_path>:<line> -->\n\n"
        "> **Summary**: <one-line purpose of the class>\n\n"
        "<!-- If the source shows clear usage patterns, add a Typical Usage block: -->\n"
        "**Typical Usage**:\n"
        "```python\n"
        "# Show the most common way to instantiate and use this class\n"
        "obj = ClassName(arg1, arg2)\n"
        "result = obj.method_name()\n"
        "```\n\n"
        "<!-- If @dataclass, add: `dataclass` badge -->\n"
        "**Type**: `<class>` | **Module**: `<module_path>`\n\n"
        "<!-- If it has a base class: -->\n"
        "**Inheritance**: `ClassName` → `BaseClassName`\n\n"
        "<!-- If there are known subclasses from the codebase: -->\n"
        "**Known Subclasses**: `SubClassA`, `SubClassB`\n\n"
        "<!-- FOR @dataclass: Field table -->\n"
        "#### 字段\n\n"
        "| 名称 | 类型 | 默认值 | 描述 |\n"
        "|------|------|---------|-------------|\n"
        "| `field_name` | `FieldType` | `default_value` | 用途说明 |\n\n"
        "<!-- FOR regular class: Constructor -->\n"
        "#### 构造方法\n\n"
        "```python\n"
        "ClassName(param: Type, ...)\n"
        "```\n\n"
        "| 参数 | 类型 | 描述 |\n"
        "|-----------|------|-------------|\n"
        "| `param` | `Type` | Description |\n\n"
        "<!-- Methods explicitly defined in source (NOT inherited, NOT auto-generated) -->\n"
        "#### 方法\n\n"
        "| 方法 | 返回值 | 描述 |\n"
        "|--------|---------|-------------|\n"
        "| `method_name(param: Type)` | `ReturnType` | 中文简述 |\n\n"
        "<!-- For each method with complex logic, optionally expand: -->\n"
        "##### `method_name`\n\n"
        "```python\n"
        "method_name(param: Type) -> ReturnType\n"
        "```\n\n"
        "| 参数 | 类型 | 描述 |\n"
        "|-----------|------|-------------|\n"
        "| `param` | `Type` | Description |\n\n"
        "**Returns**: `ReturnType` — what it returns\n\n"
        "<!-- If the method raises exceptions in source: -->\n"
        "**Raises**: `ValueError` — when `param` is negative.\n\n"
        "<!-- If deprecated: -->\n"
        "> ⚠️ **Deprecated**: Use `replacement` instead.\n\n"
        "<!-- Cross-references -->\n"
        "**See Also**: `RelatedClass`, `related_function`\n\n"
        "---\n\n"
        "## 函数参考\n\n"
        "### `function_name`\n"
        "<!-- api: function | source: <file_path>:<line> -->\n\n"
        "> **Summary**: <one-line purpose>\n\n"
        "<!-- If the source shows clear usage: -->\n"
        "**Typical Usage**:\n"
        "```python\n"
        "# Show the most common way to call this function\n"
        "result = function_name(arg1, arg2)\n"
        "```\n\n"
        "**Module**: `<module_path>`\n\n"
        "```python\n"
        "def function_name(param: Type, ...) -> ReturnType\n"
        "```\n\n"
        "| 参数 | 类型 | 描述 |\n"
        "|-----------|------|-------------|\n"
        "| `param` | `Type` | Description |\n\n"
        "**Returns**: `ReturnType` — description\n\n"
        "<!-- If the function raises exceptions in source: -->\n"
        "**Raises**: `ValueError` — when input is invalid.\n\n"
        "<!-- If deprecated: -->\n"
        "> ⚠️ **Deprecated**: Use `replacement` instead.\n\n"
        "**See Also**: `RelatedClass`, `related_function`\n\n"
        "---\n\n"
        "REMEMBER:\n"
        "- If it is NOT explicitly in the source code, do NOT write it.\n"
        "- An empty Methods table is better than invented methods.\n"
        "- Every table row MUST have exactly the same number of columns as its header.\n"
        "- Never truncate types. Type annotations must be complete.\n"
        "- Always include `file:line` location references.\n"
        "- Typical Usage examples must be based on REAL usage patterns from the source — NEVER fabricate scenarios.\n"
        "- Raises must ONLY list exceptions that are explicitly raised in the source code."
    ),
))

register(Skill(
    name="frontend",
    kind="template",
    description="Frontend analysis: UI components, routing, state management, build chain",
    suffix=(
        "You are a frontend architecture analyst. Focus on: UI component structure, "
        "routing, state management, data fetching, and build chain. If the repo has no "
        "frontend code, state that directly. Output concise Markdown."
    ),
))

register(Skill(
    name="backend",
    kind="template",
    description="Backend analysis: services, data models, business logic, call chains",
    suffix=(
        "You are a backend architecture analyst. Focus on: services and interfaces, "
        "data models, core business logic, and key call chains. If the repo has no "
        "backend code, state that directly. Output concise Markdown."
    ),
))

register(Skill(
    name="qa",
    kind="agent",
    description="Code Q&A: answer based on retrieved snippets with file:line references",
    suffix=(
        "You are a code Q&A assistant. Answer questions based ONLY on the code snippets "
        "provided above. Give file:line references for key conclusions. If the snippets "
        "are insufficient, say so explicitly — do not fabricate."
    ),
))
