# API 参考:`docs/_ext`

## `docs/_ext/scrapydocs.py`

<a id="sym-docs__ext_scrapydocs.py-13"></a>

### `SettingData` · class
```python
class SettingData(TypedDict)
```

`SettingData` 类型用于定义 Scrapy 设置数据的结构，它是一个 `TypedDict`，用于描述设置项的键值对结构。

```markdown

## SettingData

`SettingData` 是一个 `TypedDict`，用于定义 Scrapy 设置项的结构，表示设置项的键值对结构。

### 用法

- 通常用于类型提示，以确保设置数据符合预期的结构。
- 作为 `Settings` 类的内部数据结构，用于存储和管理配置项。
```

*来源: `docs/_ext/scrapydocs.py:13`*

---
<a id="sym-docs__ext_scrapydocs.py-19"></a>

### `SettingslistNode` · class
```python
class SettingslistNode(General, Element)
```

`SettingslistNode` 类代表一个用于处理设置列表的节点，通常用于配置或管理一系列设置项。

该类继承自 `General` 和 `Element`，但未定义任何方法。因此，其行为和用法完全依赖于其父类提供的功能。典型的使用场景是作为设置系统中的一个节点元素，参与设置的组织与管理。

由于没有具体方法，无法进一步描述其关键方法与典型用法。

*来源: `docs/_ext/scrapydocs.py:19`*

---
<a id="sym-docs__ext_scrapydocs.py-23"></a>

### `SettingsListDirective` · class
```python
class SettingsListDirective(Directive)
```

这个类用于处理 Scrapy 配置列表指令，通常在命令行中用于展示或管理配置项。

### 方法

- **run(self) -> Sequence[Node]**  
  执行指令并返回一个包含节点的序列，这些节点代表了配置列表的输出内容。

*来源: `docs/_ext/scrapydocs.py:23`*

---
<a id="sym-docs__ext_scrapydocs.py-24"></a>

### `SettingsListDirective.run` · method
```python
def run(self) -> Sequence[Node]
```

用途:执行 SettingsListDirective 并返回包含一个 SettingslistNode 的序列。

**Returns**
- `Sequence[Node]`: 包含一个 SettingslistNode 的序列。

**内部调用(库内):**
- [`SettingslistNode`](docs__ext.md#sym-docs__ext_scrapydocs.py-19) — `SettingslistNode` 类代表一个用于处理设置列表的节点，通常用于配置或管理一系列设置项。

*来源: `docs/_ext/scrapydocs.py:24`*

---
<a id="sym-docs__ext_scrapydocs.py-28"></a>

### `is_setting_index` · func
```python
def is_setting_index(node: Node) -> bool
```

判断给定的节点是否为设置索引条目。

**Parameters**
- `node`: Node - 待检查的节点对象

**Returns**
- `bool` - 如果节点是设置索引条目则返回 True，否则返回 False

**Raises**
- (unknown)

*来源: `docs/_ext/scrapydocs.py:28`*

---
<a id="sym-docs__ext_scrapydocs.py-37"></a>

### `get_setting_name_and_refid` · func
```python
def get_setting_name_and_refid(node: Node) -> tuple[str, str]
```

从指令索引节点中提取设置名称和引用 ID。

**Parameters**
- `node`: Node - 包含设置条目的指令索引节点

**Returns**
- `tuple[str, str]` - 设置名称和引用 ID 的元组

**Raises**
- `(unknown)`

*来源: `docs/_ext/scrapydocs.py:37`*

---
<a id="sym-docs__ext_scrapydocs.py-43"></a>

### `collect_scrapy_settings_refs` · func
```python
def collect_scrapy_settings_refs(app: Sphinx, doctree: document) -> None
```

收集 Scrapy 配置项引用信息。

**Parameters**
- `app`: Sphinx 应用实例
- `doctree`: 文档树对象

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`get_setting_name_and_refid`](docs__ext.md#sym-docs__ext_scrapydocs.py-37) — 从指令索引节点中提取设置名称和引用 ID。
- [`SettingData`](docs__ext.md#sym-docs__ext_scrapydocs.py-13) — `SettingData` 类型用于定义 Scrapy 设置数据的结构，它是一个 `TypedDict`，用于描述设置项的键值对结构。

*来源: `docs/_ext/scrapydocs.py:43`*

---
<a id="sym-docs__ext_scrapydocs.py-62"></a>

### `make_setting_element` · func
```python
def make_setting_element(
    setting_data: SettingData, app: Sphinx, fromdocname: str
) -> Any
```

创建一个设置元素，用于文档生成中的设置列表。

**Parameters**
- `setting_data`: SettingData - 包含设置信息的字典，包括文档名称、引用ID和设置名称。
- `app`: Sphinx - Sphinx 应用程序对象，用于构建文档。
- `fromdocname`: str - 当前文档的名称。

**Returns**
- Any - 返回一个列表项节点，包含指向设置文档的引用。

*来源: `docs/_ext/scrapydocs.py:62`*

---
<a id="sym-docs__ext_scrapydocs.py-80"></a>

### `make_setting_markdown_item` · func
```python
def make_setting_markdown_item(
    setting_data: SettingData, app: Sphinx, fromdocname: str
) -> str
```

生成设置项的 Markdown 链接项。

**Parameters**
- `setting_data`: SettingData 类型，包含设置项的文档名称、引用ID和名称。
- `app`: Sphinx 类型，Sphinx 应用程序实例。
- `fromdocname`: str 类型，当前文档名称。

**Returns**
- str 类型，表示设置项的 Markdown 链接格式。

*来源: `docs/_ext/scrapydocs.py:80`*

---
<a id="sym-docs__ext_scrapydocs.py-91"></a>

### `_iter_sorted_settings` · func
```python
def _iter_sorted_settings(env: Any, fromdocname: str) -> list[SettingData]
```

对 `scrapy_all_settings` 列表按设置名称排序，并过滤掉与指定文档名称相同的设置项。

**Parameters**
- `env`: 包含 `scrapy_all_settings` 属性的对象。
- `fromdocname`: 用于过滤设置项的文档名称。

**Returns**
- 按设置名称排序且已过滤的设置项列表。

**Raises**
- `(unknown)`

*来源: `docs/_ext/scrapydocs.py:91`*

---
<a id="sym-docs__ext_scrapydocs.py-99"></a>

### `replace_settingslist_nodes` · func
```python
def replace_settingslist_nodes(
    app: Sphinx, doctree: document, fromdocname: str
) -> None
```

将文档树中的 `SettingslistNode` 节点替换为包含排序后设置项的列表。

**Parameters**
- `app`: Sphinx 应用实例
- `doctree`: 文档树
- `fromdocname`: 来源文档名称

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`make_setting_element`](docs__ext.md#sym-docs__ext_scrapydocs.py-62) — 创建一个设置元素，用于文档生成中的设置列表。
- [`_iter_sorted_settings`](docs__ext.md#sym-docs__ext_scrapydocs.py-91) — 对 `scrapy_all_settings` 列表按设置名称排序，并过滤掉与指定文档名称相同的设置项。

*来源: `docs/_ext/scrapydocs.py:99`*

---
<a id="sym-docs__ext_scrapydocs.py-115"></a>

### `visit_settingslist_node_markdown` · func
```python
def visit_settingslist_node_markdown(translator: Any, _node: Node) -> None
```

将设置列表节点转换为 Markdown 格式并添加到翻译器中，然后跳过该节点。

**Parameters**

- `translator` (Any): 文档翻译器对象。
- `_node` (Node): 要处理的节点对象。

**Returns**

- (None): 此函数不返回任何值。

**Raises**

- `nodes.SkipNode`: 处理完成后抛出以跳过当前节点。

**内部调用(库内):**
- [`make_setting_markdown_item`](docs__ext.md#sym-docs__ext_scrapydocs.py-80) — 生成设置项的 Markdown 链接项。
- [`_iter_sorted_settings`](docs__ext.md#sym-docs__ext_scrapydocs.py-91) — 对 `scrapy_all_settings` 列表按设置名称排序，并过滤掉与指定文档名称相同的设置项。

*来源: `docs/_ext/scrapydocs.py:115`*

---
<a id="sym-docs__ext_scrapydocs.py-128"></a>

### `depart_settingslist_node_markdown` · func
```python
def depart_settingslist_node_markdown(_translator: Any, _node: Node) -> None
```

此函数用于处理设置列表节点的 Markdown 输出，目前为空实现。

**Parameters**
- `_translator`: 任意类型，用于翻译器对象。
- `_node`: 任意类型，表示节点对象。

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `docs/_ext/scrapydocs.py:128`*

---
<a id="sym-docs__ext_scrapydocs.py-132"></a>

### `source_role` · func
```python
def source_role(
    name, rawtext, text: str, lineno, inliner, options=None, content=None
) -> tuple[list[Any], list[Any]]
```

该函数用于创建一个指向 GitHub 源码链接的参考节点。

**Parameters**
- `name`: 角色名称
- `rawtext`: 原始文本
- `text`: 要显示的文本内容
- `lineno`: 行号
- `inliner`: 内联处理程序
- `options`: 可选参数字典
- `content`: 内容列表

**Returns**
- 返回一个包含参考节点的列表和一个空列表的元组

**Raises**
- (unknown)

*来源: `docs/_ext/scrapydocs.py:132`*

---
<a id="sym-docs__ext_scrapydocs.py-140"></a>

### `issue_role` · func
```python
def issue_role(
    name, rawtext, text: str, lineno, inliner, options=None, content=None
) -> tuple[list[Any], list[Any]]
```

处理 issue 角色引用，生成指向 GitHub issue 的链接。

**Parameters**
- `name` (str): 角色名称
- `rawtext` (str): 原始文本
- `text` (str): issue 编号
- `lineno` (int): 行号
- `inliner` (Any): 内联处理器
- `options` (dict, optional): 选项
- `content` (list, optional): 内容

**Returns**
- `tuple[list[Any], list[Any]]`: 包含节点和错误信息的元组，其中节点是生成的链接，错误信息列表为空。

**Raises**
- (unknown)

*来源: `docs/_ext/scrapydocs.py:140`*

---
<a id="sym-docs__ext_scrapydocs.py-148"></a>

### `commit_role` · func
```python
def commit_role(
    name, rawtext, text: str, lineno, inliner, options=None, content=None
) -> tuple[list[Any], list[Any]]
```

用途: `commit_role` 函数用于创建一个指向 GitHub 提交记录的超链接引用节点。

**Parameters**
- `name`: 角色名称
- `rawtext`: 原始文本
- `text`: 提交哈希值
- `lineno`: 行号
- `inliner`: 内联处理器
- `options`: 选项字典（可选）
- `content`: 内容列表（可选）

**Returns**
- 返回一个包含引用节点和空列表的元组，格式为 `tuple[list[Any], list[Any]]`。

**Raises**
- (unknown)

*来源: `docs/_ext/scrapydocs.py:148`*

---
<a id="sym-docs__ext_scrapydocs.py-156"></a>

### `rev_role` · func
```python
def rev_role(
    name, rawtext, text: str, lineno, inliner, options=None, content=None
) -> tuple[list[Any], list[Any]]
```

将修订版本号转换为指向 Mercurial 变更集链接的引用节点。

**Parameters**
- `name`: 角色名称
- `rawtext`: 原始文本
- `text`: 修订版本号字符串
- `lineno`: 行号
- `inliner`: 内联处理器
- `options`: 可选参数字典
- `content`: 内容列表

**Returns**
- 包含引用节点的列表和空列表的元组

**Raises**
- (unknown)

*来源: `docs/_ext/scrapydocs.py:156`*

---
<a id="sym-docs__ext_scrapydocs.py-164"></a>

### `setup` · func
```python
def setup(app: Sphinx) -> dict[str, Any]
```

设置 Sphinx 应用以支持 Scrapy 文档中的自定义角色和指令。

**Parameters**

- `app`: Sphinx 应用实例

**Returns**

- 包含 `parallel_read_safe` 键的字典，值为 `True`

*来源: `docs/_ext/scrapydocs.py:164`*

---

## `docs/_ext/scrapyfixautodoc.py`

<a id="sym-docs__ext_scrapyfixautodoc.py-12"></a>

### `maybe_skip_member` · func
```python
def maybe_skip_member(app: Sphinx, what, name: str, obj, skip: bool, options) -> bool
```

跳过特定成员的自动文档生成。

**Parameters**
- `app`: Sphinx 应用实例
- `what`: 成员类型
- `name`: 成员名称
- `obj`: 成员对象
- `skip`: 是否跳过
- `options`: 选项

**Returns**
- `bool`: 是否跳过该成员

**Raises**
- (unknown)

*来源: `docs/_ext/scrapyfixautodoc.py:12`*

---
<a id="sym-docs__ext_scrapyfixautodoc.py-19"></a>

### `setup` · func
```python
def setup(app: Sphinx) -> dict[str, Any]
```

配置 Sphinx 应用以跳过某些成员，并返回并行读取安全标志。

**Parameters**

- `app`: Sphinx 应用实例。

**Returns**

- 包含 `parallel_read_safe` 标志的字典。

*来源: `docs/_ext/scrapyfixautodoc.py:19`*

---