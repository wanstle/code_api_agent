# API 参考:`scrapy`

## `scrapy/addons.py`

<a id="sym-scrapy_addons.py-18"></a>

### `AddonManager` · class
```python
class AddonManager
```

AddonManager 类负责管理 Scrapy 扩展插件的加载与配置。

### 方法

- **`__init__(self, crawler: Crawler) -> None`**  
  初始化 AddonManager 实例，并传入一个 Crawler 对象用于后续的扩展管理。

- **`load_settings(self, settings: Settings) -> None`**  
  从给定的 Settings 对象中加载扩展相关的设置。

- **`load_pre_crawler_settings(cls, settings: BaseSettings) -> None`**  
  类方法，用于在爬虫启动前加载扩展所需的预设设置。

*来源: `scrapy/addons.py:18`*

---
<a id="sym-scrapy_addons.py-21"></a>

### `AddonManager.__init__` · method
```python
def __init__(self, crawler: Crawler) -> None
```

初始化 AddonManager 实例，关联爬虫实例并初始化插件列表。

**Parameters**
- `crawler`: Crawler - 用于关联的爬虫实例。

**Returns**
- `None`

**Raises**
- `(unknown)`

*来源: `scrapy/addons.py:21`*

---
<a id="sym-scrapy_addons.py-25"></a>

### `AddonManager.load_settings` · method
```python
def load_settings(self, settings: Settings) -> None
```

从设置对象加载插件和配置并应用它们。

**Parameters**
- `settings` (Settings): 用于读取插件配置的设置对象

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/addons.py:25`*

---
<a id="sym-scrapy_addons.py-58"></a>

### `AddonManager.load_pre_crawler_settings` · method
装饰器: `@classmethod`
```python
def load_pre_crawler_settings(cls, settings: BaseSettings) -> None
```

更新爬虫早期设置，加载 `ADDONS` 中配置的插件并调用其 `update_pre_crawler_settings` 方法。

**Parameters**

- `settings` (BaseSettings): 用于读取早期插件配置的设置对象。

**Returns**

- `None`

**Raises**

- (unknown)

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/addons.py:58`*

---

## `scrapy/cmdline.py`

<a id="sym-scrapy_cmdline.py-28"></a>

### `ScrapyArgumentParser` · class
```python
class ScrapyArgumentParser(argparse.ArgumentParser)
```

ScrapyArgumentParser 是一个继承自 argparse.ArgumentParser 的类，用于解析命令行参数，通常在 Scrapy 项目的命令行工具中使用。

### 方法

- **_parse_optional(self, arg_string: str) -> tuple[argparse.Action | None, str, str | None] | None**
  - 解析可选参数字符串。
  - 参数:
    - `arg_string`: 要解析的参数字符串。
  - 返回值:
    - 如果 `arg_string` 是一个可选参数，则返回一个包含 `Action` 对象、参数名和参数值的元组；否则返回 `None`。
  - 该方法用于处理命令行中以 `-` 或 `--` 开头的参数。

*来源: `scrapy/cmdline.py:28`*

---
<a id="sym-scrapy_cmdline.py-29"></a>

### `ScrapyArgumentParser._parse_optional` · method
```python
def _parse_optional(
        self, arg_string: str
    ) -> tuple[argparse.Action | None, str, str | None] | None
```

解析可选参数字符串，处理特殊格式如 `-:json`。

**Parameters**

- `arg_string` (str): 待解析的命令行参数字符串。

**Returns**

- `tuple[argparse.Action | None, str, str | None] | None`: 如果参数以 `-:` 开头则返回 `None`，否则返回父类解析结果。

**Raises**

- (unknown)

*来源: `scrapy/cmdline.py:29`*

---
<a id="sym-scrapy_cmdline.py-40"></a>

### `_iter_command_classes` · func
```python
def _iter_command_classes(module_name: str) -> Iterable[type[ScrapyCommand]]
```

递归遍历模块以查找所有继承自 `ScrapyCommand` 的命令类。

**Parameters**

- `module_name`: str - 要遍历的模块名称。

**Returns**

- `Iterable[type[ScrapyCommand]]` - 所有找到的命令类的迭代器。

**Raises**

- (unknown)

**内部调用(库内):**
- [`walk_modules_iter`](scrapy_utils.md#sym-scrapy_utils_misc.py-93)

*来源: `scrapy/cmdline.py:40`*

---
<a id="sym-scrapy_cmdline.py-54"></a>

### `_get_commands_from_module` · func
```python
def _get_commands_from_module(module: str, inproject: bool) -> dict[str, ScrapyCommand]
```

从模块中提取命令类，根据是否在项目中过滤并实例化命令。

**Parameters**
- `module` (str): 模块路径，用于查找命令类。
- `inproject` (bool): 是否仅返回需要项目配置的命令。

**Returns**
- `dict[str, ScrapyCommand]`: 命令名称到命令实例的映射。

**Raises**
- (unknown)

**内部调用(库内):**
- [`_iter_command_classes`](scrapy.md#sym-scrapy_cmdline.py-40) — 递归遍历模块以查找所有继承自 `ScrapyCommand` 的命令类。

*来源: `scrapy/cmdline.py:54`*

---
<a id="sym-scrapy_cmdline.py-63"></a>

### `_get_commands_from_entry_points` · func
```python
def _get_commands_from_entry_points(
    inproject: bool, group: str = "scrapy.commands"
) -> dict[str, ScrapyCommand]
```

从入口点加载命令类并返回命令字典。

**Parameters**
- `inproject` (bool): 是否在项目中查找命令。
- `group` (str): 入口点组名称，默认为 `"scrapy.commands"`。

**Returns**
- `dict[str, ScrapyCommand]`: 命令名称到命令实例的映射。

**Raises**
- `ValueError`: 当入口点加载的不是类时抛出。

*来源: `scrapy/cmdline.py:63`*

---
<a id="sym-scrapy_cmdline.py-76"></a>

### `_get_commands_dict` · func
```python
def _get_commands_dict(
    settings: BaseSettings, inproject: bool
) -> dict[str, ScrapyCommand]
```

从模块和入口点加载命令并返回命令字典。

**Parameters**
- `settings`: BaseSettings - 配置设置对象
- `inproject`: bool - 是否在项目中运行

**Returns**
- dict[str, ScrapyCommand] - 命令名称到命令类的映射字典

**Raises**
- (unknown)

**内部调用(库内):**
- [`_get_commands_from_module`](scrapy.md#sym-scrapy_cmdline.py-54) — 从模块中提取命令类，根据是否在项目中过滤并实例化命令。
- [`_get_commands_from_entry_points`](scrapy.md#sym-scrapy_cmdline.py-63) — 从入口点加载命令类并返回命令字典。

*来源: `scrapy/cmdline.py:76`*

---
<a id="sym-scrapy_cmdline.py-87"></a>

### `_get_project_only_cmds` · func
```python
def _get_project_only_cmds(settings: BaseSettings) -> set[str]
```

根据提供的代码，此函数用于获取仅在项目中定义的命令集合。

**Parameters**
- `settings`: 配置设置对象，用于获取命令字典。

**Returns**
- 一个字符串集合，包含仅在项目中定义的命令名称。

**Raises**
- (unknown)

**内部调用(库内):**
- [`_get_commands_dict`](scrapy.md#sym-scrapy_cmdline.py-76) — 从模块和入口点加载命令并返回命令字典。

*来源: `scrapy/cmdline.py:87`*

---
<a id="sym-scrapy_cmdline.py-93"></a>

### `_pop_command_name` · func
```python
def _pop_command_name(argv: list[str]) -> str | None
```

从命令行参数列表中提取并移除第一个非选项参数作为命令名称。

**Parameters**

- `argv`: 命令行参数列表。

**Returns**

- 如果存在非选项参数，则返回该参数并从列表中移除；否则返回 `None`。

*来源: `scrapy/cmdline.py:93`*

---
<a id="sym-scrapy_cmdline.py-100"></a>

### `_print_header` · func
```python
def _print_header(settings: BaseSettings, inproject: bool) -> None
```

打印 Scrapy 版本信息，根据是否处于项目中显示活动项目名称或提示无活动项目。

**Parameters**
- `settings` (BaseSettings): 配置设置对象，用于获取 BOT_NAME。
- `inproject` (bool): 指示当前是否处于 Scrapy 项目中。

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `scrapy/cmdline.py:100`*

---
<a id="sym-scrapy_cmdline.py-109"></a>

### `_print_commands` · func
```python
def _print_commands(settings: BaseSettings, inproject: bool) -> None
```

打印可用的 Scrapy 命令列表及其简短描述。

**Parameters**
- `settings` (BaseSettings): 配置设置对象。
- `inproject` (bool): 是否在项目目录中运行。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`_print_header`](scrapy.md#sym-scrapy_cmdline.py-100) — 打印 Scrapy 版本信息，根据是否处于项目中显示活动项目名称或提示无活动项目。
- [`_get_commands_dict`](scrapy.md#sym-scrapy_cmdline.py-76) — 从模块和入口点加载命令并返回命令字典。

*来源: `scrapy/cmdline.py:109`*

---
<a id="sym-scrapy_cmdline.py-131"></a>

### `_print_unknown_command_msg` · func
```python
def _print_unknown_command_msg(
    settings: BaseSettings, cmdname: str, inproject: bool
) -> None
```

打印未知命令的提示信息。

**Parameters**
- `settings`: BaseSettings - 配置设置对象
- `cmdname`: str - 未知命令名称
- `inproject`: bool - 是否在项目内部执行

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`_get_project_only_cmds`](scrapy.md#sym-scrapy_cmdline.py-87) — 根据提供的代码，此函数用于获取仅在项目中定义的命令集合。

*来源: `scrapy/cmdline.py:131`*

---
<a id="sym-scrapy_cmdline.py-145"></a>

### `_print_unknown_command` · func
```python
def _print_unknown_command(
    settings: BaseSettings, cmdname: str, inproject: bool
) -> None
```

打印未知命令的相关信息和提示。

**Parameters**
- `settings`: BaseSettings - 配置设置对象
- `cmdname`: str - 未知命令名称
- `inproject`: bool - 是否在项目中

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`_print_header`](scrapy.md#sym-scrapy_cmdline.py-100) — 打印 Scrapy 版本信息，根据是否处于项目中显示活动项目名称或提示无活动项目。
- [`_print_unknown_command_msg`](scrapy.md#sym-scrapy_cmdline.py-131) — 打印未知命令的提示信息。

*来源: `scrapy/cmdline.py:145`*

---
<a id="sym-scrapy_cmdline.py-153"></a>

### `_run_print_help` · func
```python
def _run_print_help(
    parser: argparse.ArgumentParser,
    func: Callable[_P, None],
    *a: _P.args,
    **kw: _P.kwargs,
) -> None
```

打印帮助信息并处理命令行参数错误。

**Parameters**
- `parser`: argparse.ArgumentParser - 命令行参数解析器
- `func`: Callable[_P, None] - 执行的函数
- `*a`: _P.args - 传递给 func 的位置参数
- `**kw`: _P.kwargs - 传递给 func 的关键字参数

**Raises**
- `UsageError` - 当命令行参数使用错误时抛出
- `SystemExit` - 当需要退出程序时抛出

**Returns**
- `None`

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`Shell.print_help`](scrapy.md#sym-scrapy_shell.py-269)

*来源: `scrapy/cmdline.py:153`*

---
<a id="sym-scrapy_cmdline.py-169"></a>

### `execute` · func
```python
def execute(argv: list[str] | None = None, settings: Settings | None = None) -> None
```

执行 Scrapy 命令行工具的主函数，解析命令行参数并运行相应的命令。

**Parameters**
- `argv`: 命令行参数列表，若为 `None` 则使用 `sys.argv`。
- `settings`: 项目设置对象，若为 `None` 则使用默认项目设置。

**Returns**
- `None`

**Raises**
- `SystemExit`: 当命令不存在或无命令时退出程序。

**内部调用(库内):**
- [`get_project_settings`](scrapy_utils.md#sym-scrapy_utils_project.py-66)
- [`inside_project`](scrapy_utils.md#sym-scrapy_utils_project.py-16)
- [`_get_commands_dict`](scrapy.md#sym-scrapy_cmdline.py-76) — 从模块和入口点加载命令并返回命令字典。
- [`_pop_command_name`](scrapy.md#sym-scrapy_cmdline.py-93) — 从命令行参数列表中提取并移除第一个非选项参数作为命令名称。
- [`_print_commands`](scrapy.md#sym-scrapy_cmdline.py-109) — 打印可用的 Scrapy 命令列表及其简短描述。
- [`_print_unknown_command`](scrapy.md#sym-scrapy_cmdline.py-145) — 打印未知命令的相关信息和提示。
- [`ScrapyArgumentParser`](scrapy.md#sym-scrapy_cmdline.py-28) — ScrapyArgumentParser 是一个继承自 argparse.ArgumentParser 的类，用于解析命令行参数，通常在 Scrapy 项目的命
- [`BaseSettings.setdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-535)
- [`_run_print_help`](scrapy.md#sym-scrapy_cmdline.py-153) — 打印帮助信息并处理命令行参数错误。
- [`AsyncCrawlerProcess`](scrapy.md#sym-scrapy_crawler.py-796) — `AsyncCrawlerProcess` 是一个异步爬虫进程管理器，负责启动和管理异步爬虫的执行流程。
- [`CrawlerProcess`](scrapy.md#sym-scrapy_crawler.py-720) — `CrawlerProcess` 类用于启动和管理一个独立的爬虫进程，它继承自 `CrawlerProcessBase` 和 `CrawlerRunner`，负

*来源: `scrapy/cmdline.py:169`*

---
<a id="sym-scrapy_cmdline.py-218"></a>

### `_run_command` · func
```python
def _run_command(cmd: ScrapyCommand, args: list[str], opts: argparse.Namespace) -> None
```

运行命令并根据是否启用性能分析来选择执行路径。

**Parameters**
- `cmd`: ScrapyCommand - 要运行的命令实例
- `args`: list[str] - 命令行参数列表
- `opts`: argparse.Namespace - 命令行选项命名空间

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`_run_command_profiled`](scrapy.md#sym-scrapy_cmdline.py-225) — 运行命令并使用 cProfile 进行性能分析。

*来源: `scrapy/cmdline.py:218`*

---
<a id="sym-scrapy_cmdline.py-225"></a>

### `_run_command_profiled` · func
```python
def _run_command_profiled(
    cmd: ScrapyCommand, args: list[str], opts: argparse.Namespace
) -> None
```

运行命令并使用 cProfile 进行性能分析。

**Parameters**
- `cmd`: ScrapyCommand - 要运行的命令对象
- `args`: list[str] - 命令行参数列表
- `opts`: argparse.Namespace - 命令行选项对象

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `scrapy/cmdline.py:225`*

---

## `scrapy/crawler.py`

<a id="sym-scrapy_crawler.py-57"></a>

### `Crawler` · class
```python
class Crawler
```

`Crawler` 类代表一个爬虫实例，负责管理爬虫的生命周期、配置、组件和执行引擎。

### 关键方法与典型用法

- `__init__(self, spidercls: type[Spider], settings: dict[str, Any] | Settings | None = None, init_reactor: bool = False)`  
  初始化爬虫实例，传入爬虫类、设置和是否初始化 reactor。

- `_update_root_log_handler(self) -> None`  
  更新根日志处理器。

- `_apply_settings(self) -> None`  
  应用设置。

- `_apply_reactorless_default_settings(self) -> None`  
  应用无 reactor 的默认设置。

- `crawl(self, *args: Any, **kwargs: Any) -> Generator[Deferred[Any], Any, None]`  
  启动爬虫，返回一个 Deferred 生成器。

- `crawl_async(self, *args: Any, **kwargs: Any) -> None`  
  异步启动爬虫。

- `_create_spider(self, *args: Any, **kwargs: Any) -> Spider`  
  创建爬虫实例。

- `_create_engine(self) -> ExecutionEngine`  
  创建执行引擎。

- `stop(self) -> Deferred[None]`  
  停止爬虫，返回一个 Deferred。

- `stop_async(self) -> None`  
  异步停止爬虫。

- `_get_component(component_class: type[_T], components: Iterable[Any]) -> _

*来源: `scrapy/crawler.py:57`*

---
<a id="sym-scrapy_crawler.py-58"></a>

### `Crawler.__init__` · method
```python
def __init__(
        self,
        spidercls: type[Spider],
        settings: dict[str, Any] | Settings | None = None,
        init_reactor: bool = False,
    )
```

初始化一个 Crawler 实例，用于管理爬虫的生命周期和组件。

**Parameters**
- `spidercls`: 要使用的 Spider 类。
- `settings`: 用于配置爬虫的设置，可以是字典或 Settings 对象。
- `init_reactor`: 是否在爬虫启动时初始化 Reactor。

**Returns**
- (unknown)

**Raises**
- `ValueError`: 当 spidercls 是 Spider 实例而非类时抛出。

**内部调用(库内):**
- [`Settings`](scrapy_settings.md#sym-scrapy_settings___init__.py-690)
- [`Crawler._update_root_log_handler`](scrapy.md#sym-scrapy_crawler.py-89) — 更新 Scrapy 根日志处理器以匹配当前设置。
- [`AddonManager`](scrapy.md#sym-scrapy_addons.py-18) — AddonManager 类负责管理 Scrapy 扩展插件的加载与配置。
- [`SignalManager`](scrapy.md#sym-scrapy_signalmanager.py-14)

*来源: `scrapy/crawler.py:58`*

---
<a id="sym-scrapy_crawler.py-89"></a>

### `Crawler._update_root_log_handler` · method
```python
def _update_root_log_handler(self) -> None
```

更新 Scrapy 根日志处理器以匹配当前设置。

**Parameters**
- `self`: Crawler 实例

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`get_scrapy_root_handler`](scrapy_utils.md#sym-scrapy_utils_log.py-160)
- [`install_scrapy_root_handler`](scrapy_utils.md#sym-scrapy_utils_log.py-140)

*来源: `scrapy/crawler.py:89`*

---
<a id="sym-scrapy_crawler.py-94"></a>

### `Crawler._apply_settings` · method
```python
def _apply_settings(self) -> None
```

应用爬虫设置并初始化相关组件。

**Parameters**
- `self`: Crawler 实例

**Returns**
- `None`

**Raises**
- `RuntimeError`: 当启用 Twisted reactor 但未安装时抛出。

**内部调用(库内):**
- [`AddonManager.load_settings`](scrapy.md#sym-scrapy_addons.py-25) — 从设置对象加载插件和配置并应用它们。
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`install_reactor`](scrapy_utils.md#sym-scrapy_utils_reactor.py-114)
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)
- [`verify_installed_reactor`](scrapy_utils.md#sym-scrapy_utils_reactor.py-169)
- [`is_asyncio_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-220)
- [`verify_installed_asyncio_event_loop`](scrapy_utils.md#sym-scrapy_utils_reactor.py-189)
- [`log_reactor_info`](scrapy_utils.md#sym-scrapy_utils_log.py-199)
- [`Crawler._apply_reactorless_default_settings`](scrapy.md#sym-scrapy_crawler.py-154) — 设置某些配置默认值，当不使用 Twisted 反应器时。
- [`BaseSettings.freeze`](scrapy_settings.md#sym-scrapy_settings___init__.py-624)
- [`overridden_settings`](scrapy_settings.md#sym-scrapy_settings___init__.py-722)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)

*来源: `scrapy/crawler.py:94`*

---
<a id="sym-scrapy_crawler.py-154"></a>

### `Crawler._apply_reactorless_default_settings` · method
```python
def _apply_reactorless_default_settings(self) -> None
```

设置某些配置默认值，当不使用 Twisted 反应器时。

**Parameters**
- `self` - Crawler 实例

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:154`*

---
<a id="sym-scrapy_crawler.py-172"></a>

### `Crawler.crawl` · method
装饰器: `@inlineCallbacks`
```python
def crawl(self, *args: Any, **kwargs: Any) -> Generator[Deferred[Any], Any, None]
```

启动爬虫以爬取数据，返回一个在爬取完成后触发的 deferred 对象。

**Parameters**

- `*args` - 传递给爬虫类构造函数的位置参数。
- `**kwargs` - 传递给爬虫类构造函数的关键字参数。

**Raises**

- `RuntimeError` - 如果爬虫已经在运行中，或者在同一个实例上调用了多次 `Crawler.crawl()`。

**内部调用(库内):**
- [`Crawler._create_spider`](scrapy.md#sym-scrapy_crawler.py-230) — 创建并返回一个 spider 实例。
- [`Crawler._apply_settings`](scrapy.md#sym-scrapy_crawler.py-94) — 应用爬虫设置并初始化相关组件。
- [`Crawler._update_root_log_handler`](scrapy.md#sym-scrapy_crawler.py-89) — 更新 Scrapy 根日志处理器以匹配当前设置。
- [`Crawler._create_engine`](scrapy.md#sym-scrapy_crawler.py-233) — 创建并返回一个 ExecutionEngine 实例用于执行爬虫引擎。
- [`ExecutionEngine.start_async`](scrapy_core.md#sym-scrapy_core_engine.py-176)
- [`ExecutionEngine.close_async`](scrapy_core.md#sym-scrapy_core_engine.py-249)

*来源: `scrapy/crawler.py:172`*

---
<a id="sym-scrapy_crawler.py-200"></a>

### `Crawler.crawl_async` · method
```python
async def crawl_async(self, *args: Any, **kwargs: Any) -> None
```

启动爬虫并异步执行，仅可调用一次。

**Parameters**
- `*args: Any` - 传递给爬虫类的参数。
- `**kwargs: Any` - 传递给爬虫类的关键字参数。

**Raises**
- `RuntimeError` - 当爬虫已在运行或已调用过 `crawl_async` 时抛出。

**内部调用(库内):**
- [`Crawler._create_spider`](scrapy.md#sym-scrapy_crawler.py-230) — 创建并返回一个 spider 实例。
- [`Crawler._apply_settings`](scrapy.md#sym-scrapy_crawler.py-94) — 应用爬虫设置并初始化相关组件。
- [`Crawler._update_root_log_handler`](scrapy.md#sym-scrapy_crawler.py-89) — 更新 Scrapy 根日志处理器以匹配当前设置。
- [`Crawler._create_engine`](scrapy.md#sym-scrapy_crawler.py-233) — 创建并返回一个 ExecutionEngine 实例用于执行爬虫引擎。
- [`ExecutionEngine.start_async`](scrapy_core.md#sym-scrapy_core_engine.py-176)
- [`ExecutionEngine.close_async`](scrapy_core.md#sym-scrapy_core_engine.py-249)

*来源: `scrapy/crawler.py:200`*

---
<a id="sym-scrapy_crawler.py-230"></a>

### `Crawler._create_spider` · method
```python
def _create_spider(self, *args: Any, **kwargs: Any) -> Spider
```

创建并返回一个 spider 实例。

**Parameters**
- `*args`: 传递给 spider 类构造函数的位置参数。
- `**kwargs`: 传递给 spider 类构造函数的关键字参数。

**Returns**
- `Spider`: 由 `self.spidercls` 创建的 spider 实例。

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:230`*

---
<a id="sym-scrapy_crawler.py-233"></a>

### `Crawler._create_engine` · method
```python
def _create_engine(self) -> ExecutionEngine
```

创建并返回一个 ExecutionEngine 实例用于执行爬虫引擎。

**Parameters**
- `self` - Crawler 类的实例

**Returns**
- `ExecutionEngine` - 用于执行爬虫任务的引擎实例

**Raises**
- (unknown)

**内部调用(库内):**
- [`ExecutionEngine`](scrapy_core.md#sym-scrapy_core_engine.py-102)
- [`Crawler.stop_async`](scrapy.md#sym-scrapy_crawler.py-246) — Crawler.stop_async 方法用于异步启动爬虫的优雅停止过程。

*来源: `scrapy/crawler.py:233`*

---
<a id="sym-scrapy_crawler.py-236"></a>

### `Crawler.stop` · method
```python
def stop(self) -> Deferred[None]
```

Crawler.stop 方法用于启动爬虫的优雅停止过程，并在爬虫停止时返回一个已触发的 deferred 对象。

**Parameters**
- `self` - Crawler 实例

**Returns**
- `Deferred[None]` - 当爬虫停止时触发的 deferred 对象

**Raises**
- `ScrapyDeprecationWarning` - 当调用此方法时会发出的弃用警告

**内部调用(库内):**
- [`Crawler.stop_async`](scrapy.md#sym-scrapy_crawler.py-246) — Crawler.stop_async 方法用于异步启动爬虫的优雅停止过程。

*来源: `scrapy/crawler.py:236`*

---
<a id="sym-scrapy_crawler.py-246"></a>

### `Crawler.stop_async` · method
```python
async def stop_async(self) -> None
```

Crawler.stop_async 方法用于异步启动爬虫的优雅停止过程。

**Parameters**
- `self` - Crawler 实例

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:246`*

---
<a id="sym-scrapy_crawler.py-258"></a>

### `Crawler._get_component` · method
装饰器: `@staticmethod`
```python
def _get_component(
        component_class: type[_T], components: Iterable[Any]
    ) -> _T | None
```

从组件列表中获取指定类型的第一个组件实例。

**Parameters**
- `component_class`: 要查找的组件类型。
- `components`: 组件实例的可迭代对象。

**Returns**
- 如果找到匹配的组件，则返回该组件实例；否则返回 `None`。

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:258`*

---
<a id="sym-scrapy_crawler.py-266"></a>

### `Crawler.get_addon` · method
```python
def get_addon(self, cls: type[_T]) -> _T | None
```

返回指定类或其子类的运行时附加组件实例，若未找到则返回 None。

**Parameters**
- `cls`: 要查找的附加组件类或其子类

**Returns**
- `cls` 类的实例或其子类的实例，如果未找到则返回 None

**Raises**
- (unknown)

**内部调用(库内):**
- [`Crawler._get_component`](scrapy.md#sym-scrapy_crawler.py-258) — 从组件列表中获取指定类型的第一个组件实例。

*来源: `scrapy/crawler.py:266`*

---
<a id="sym-scrapy_crawler.py-274"></a>

### `Crawler.get_downloader_middleware` · method
```python
def get_downloader_middleware(self, cls: type[_T]) -> _T | None
```

获取指定类或其子类的下载中间件实例。

**Parameters**
- `cls`: 下载中间件的类类型

**Returns**
- 指定类或其子类的下载中间件实例，如果未找到则返回 `None`

**Raises**
- `RuntimeError`: 如果爬虫引擎尚未创建，则抛出此异常

**内部调用(库内):**
- [`Crawler._get_component`](scrapy.md#sym-scrapy_crawler.py-258) — 从组件列表中获取指定类型的第一个组件实例。

*来源: `scrapy/crawler.py:274`*

---
<a id="sym-scrapy_crawler.py-291"></a>

### `Crawler.get_extension` · method
```python
def get_extension(self, cls: type[_T]) -> _T | None
```

返回指定类或其子类的扩展运行时实例，若未找到则返回 None。

**Parameters**
- `cls`: 扩展类或其子类

**Returns**
- 指定类的扩展实例或 None

**Raises**
- `RuntimeError`: 当扩展管理器尚未创建时抛出

**内部调用(库内):**
- [`Crawler._get_component`](scrapy.md#sym-scrapy_crawler.py-258) — 从组件列表中获取指定类型的第一个组件实例。

*来源: `scrapy/crawler.py:291`*

---
<a id="sym-scrapy_crawler.py-309"></a>

### `Crawler.get_item_pipeline` · method
```python
def get_item_pipeline(self, cls: type[_T]) -> _T | None
```

返回指定类或其子类的运行时实例，如果未找到则返回 None。

**Parameters**
- `cls`: 要查找的项目管道类。

**Returns**
- 指定类或其子类的运行时实例，如果未找到则返回 None。

**Raises**
- `RuntimeError`: 如果爬虫引擎尚未创建，则抛出此异常。

**内部调用(库内):**
- [`Crawler._get_component`](scrapy.md#sym-scrapy_crawler.py-258) — 从组件列表中获取指定类型的第一个组件实例。

*来源: `scrapy/crawler.py:309`*

---
<a id="sym-scrapy_crawler.py-326"></a>

### `Crawler.get_spider_middleware` · method
```python
def get_spider_middleware(self, cls: type[_T]) -> _T | None
```

返回指定类或其子类的爬虫中间件实例，若未找到则返回 None。

**Parameters**
- `cls`: 要查找的中间件类。

**Returns**
- 指定类或其子类的中间件实例，若未找到则返回 None。

**Raises**
- `RuntimeError`: 如果爬虫引擎尚未创建。

**内部调用(库内):**
- [`Crawler._get_component`](scrapy.md#sym-scrapy_crawler.py-258) — 从组件列表中获取指定类型的第一个组件实例。

*来源: `scrapy/crawler.py:326`*

---
<a id="sym-scrapy_crawler.py-344"></a>

### `CrawlerRunnerBase` · class
```python
class CrawlerRunnerBase(ABC)
```

`CrawlerRunnerBase` 是一个抽象基类，用于管理爬虫的创建与运行流程，为异步和同步爬虫运行器提供通用接口。

### 方法说明

- **`__init__(self, settings: dict[str, Any] | Settings | None = None)`**  
  初始化爬虫运行器，可传入配置项 `settings`。

- **`crawlers(self) -> set[Crawler]`**  
  返回当前运行器中所有已创建的爬虫实例集合。

- **`create_crawler(self, crawler_or_spidercls: type[Spider] | str | Crawler) -> Crawler`**  
  根据爬虫类、爬虫名称或已有的爬虫实例创建一个新的爬虫实例。

- **`_create_crawler(self, spidercls: str | type[Spider]) -> Crawler`**  
  内部方法，用于根据爬虫类或名称创建爬虫实例。

- **`crawl(self, crawler_or_spidercls: type[Spider] | str | Crawler, *args: Any, **kwargs: Any) -> Awaitable[None]`**  
  异步启动一个爬虫，可传入爬虫类、名称或实例，并支持传入额外参数。

*来源: `scrapy/crawler.py:344`*

---
<a id="sym-scrapy_crawler.py-345"></a>

### `CrawlerRunnerBase.__init__` · method
```python
def __init__(self, settings: dict[str, Any] | Settings | None = None)
```

初始化 CrawlerRunnerBase 实例，设置配置、爬虫加载器等必要组件。

**Parameters**
- `settings`: 配置信息，可以是字典、Settings 对象或 None。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`Settings`](scrapy_settings.md#sym-scrapy_settings___init__.py-690)
- [`AddonManager.load_pre_crawler_settings`](scrapy.md#sym-scrapy_addons.py-58) — 更新爬虫早期设置，加载 `ADDONS` 中配置的插件并调用其 `update_pre_crawler_settings` 方法。
- [`get_spider_loader`](scrapy.md#sym-scrapy_spiderloader.py-25)

*来源: `scrapy/crawler.py:345`*

---
<a id="sym-scrapy_crawler.py-355"></a>

### `CrawlerRunnerBase.crawlers` · method
装饰器: `@property`
```python
def crawlers(self) -> set[Crawler]
```

返回由该类启动并管理的爬虫集合。

**Returns**
- `set[Crawler]` - 由该类启动并管理的爬虫集合。

*来源: `scrapy/crawler.py:355`*

---
<a id="sym-scrapy_crawler.py-360"></a>

### `CrawlerRunnerBase.create_crawler` · method
```python
def create_crawler(
        self, crawler_or_spidercls: type[Spider] | str | Crawler
    ) -> Crawler
```

创建并返回一个 `scrapy.crawler.Crawler` 对象。

**Parameters**
- `crawler_or_spidercls`: 可以是 Spider 类、Crawler 对象或 Spider 名称（字符串）。如果传入的是 Spider 对象，则会抛出异常。

**Returns**
- `Crawler`: 返回一个 `Crawler` 实例。

**Raises**
- `ValueError`: 当传入的参数是 `Spider` 实例时抛出。

**内部调用(库内):**
- [`CrawlerRunnerBase._create_crawler`](scrapy.md#sym-scrapy_crawler.py-382) — 创建一个爬虫实例。

*来源: `scrapy/crawler.py:360`*

---
<a id="sym-scrapy_crawler.py-382"></a>

### `CrawlerRunnerBase._create_crawler` · method
```python
def _create_crawler(self, spidercls: str | type[Spider]) -> Crawler
```

创建一个爬虫实例。

**Parameters**
- `spidercls`: 爬虫类或爬虫类的名称。

**Returns**
- `Crawler`: 返回一个爬虫实例。

**Raises**
- (unknown)

**内部调用(库内):**
- [`Crawler`](scrapy.md#sym-scrapy_crawler.py-57) — `Crawler` 类代表一个爬虫实例，负责管理爬虫的生命周期、配置、组件和执行引擎。

*来源: `scrapy/crawler.py:382`*

---
<a id="sym-scrapy_crawler.py-388"></a>

### `CrawlerRunnerBase.crawl` · method
装饰器: `@abstractmethod`
```python
def crawl(
        self,
        crawler_or_spidercls: type[Spider] | str | Crawler,
        *args: Any,
        **kwargs: Any,
    ) -> Awaitable[None]
```

CrawlerRunnerBase.crawl 用于创建并爬取爬虫实例。

**Parameters**
- `crawler_or_spidercls`: 爬虫类、爬虫实例或爬虫名称
- `*args`: 传递给爬虫的参数
- `**kwargs`: 传递给爬虫的关键词参数

**Returns**
- `Awaitable[None]`: 一个等待对象，表示爬虫的执行

**Raises**
- `NotImplementedError`: 当前方法未被实现

*来源: `scrapy/crawler.py:388`*

---
<a id="sym-scrapy_crawler.py-397"></a>

### `CrawlerRunner` · class
```python
class CrawlerRunner(CrawlerRunnerBase)
```

`CrawlerRunner` 是一个用于运行爬虫的类，负责管理爬虫的启动、执行和停止流程。

### 方法说明

- **`__init__(self, settings: dict[str, Any] | Settings | None = None)`**  
  初始化 `CrawlerRunner` 实例，可传入配置项 `settings`。

- **`crawl(self, crawler_or_spidercls: type[Spider] | str | Crawler, *args: Any, **kwargs: Any) -> Deferred[None]`**  
  启动一个爬虫，可以传入爬虫类、爬虫名称或已有的 `Crawler` 实例。

- **`_crawl(self, crawler: Crawler, *args: Any, **kwargs: Any) -> Generator[Deferred[Any], Any, None]`**  
  内部方法，用于执行爬虫的运行逻辑，返回一个生成器对象。

- **`stop(self) -> Deferred[Any]`**  
  停止所有正在运行的爬虫任务。

- **`join(self) -> Generator[Deferred[Any], Any, None]`**  
  等待所有爬虫任务完成，返回一个生成器对象。

*来源: `scrapy/crawler.py:397`*

---
<a id="sym-scrapy_crawler.py-413"></a>

### `CrawlerRunner.__init__` · method
```python
def __init__(self, settings: dict[str, Any] | Settings | None = None)
```

CrawlerRunner 的初始化方法，用于设置运行时配置并验证 Twisted Reactor 的启用状态。

**Parameters**
- `settings`: 可选的配置字典或 Settings 对象，用于初始化爬虫运行器。

**Raises**
- `RuntimeError`: 当配置中禁用了 TWISTED_REACTOR_ENABLED 时抛出。

*来源: `scrapy/crawler.py:413`*

---
<a id="sym-scrapy_crawler.py-421"></a>

### `CrawlerRunner.crawl` · method
```python
def crawl(
        self,
        crawler_or_spidercls: type[Spider] | str | Crawler,
        *args: Any,
        **kwargs: Any,
    ) -> Deferred[None]
```

启动一个爬虫进行爬取。

**Parameters**
- `crawler_or_spidercls`: 已创建的爬虫实例、爬虫类或项目内的爬虫名称
- `args`: 用于初始化爬虫的参数
- `kwargs`: 用于初始化爬虫的关键词参数

**Returns**
- 一个在爬取完成后触发的 deferred 对象

**Raises**
- `ValueError`: 当 `crawler_or_spidercls` 参数是爬虫对象时抛出

**内部调用(库内):**
- [`CrawlerRunnerBase.create_crawler`](scrapy.md#sym-scrapy_crawler.py-360) — 创建并返回一个 `scrapy.crawler.Crawler` 对象。
- [`CrawlerRunner._crawl`](scrapy.md#sym-scrapy_crawler.py-457) — 递归调用爬虫进行抓取，管理爬虫生命周期和异常状态。

*来源: `scrapy/crawler.py:421`*

---
<a id="sym-scrapy_crawler.py-457"></a>

### `CrawlerRunner._crawl` · method
装饰器: `@inlineCallbacks`
```python
def _crawl(
        self, crawler: Crawler, *args: Any, **kwargs: Any
    ) -> Generator[Deferred[Any], Any, None]
```

递归调用爬虫进行抓取，管理爬虫生命周期和异常状态。

**Parameters**
- `crawler` (Crawler): 要运行的爬虫实例。
- `*args` (Any): 传递给爬虫的参数。
- `**kwargs` (Any): 传递给爬虫的关键词参数。

**Returns**
- `Generator[Deferred[Any], Any, None]`: 一个生成器，用于异步处理爬虫任务。

**Raises**
- `Exception`: 如果在爬取过程中发生异常，则会重新抛出。

**内部调用(库内):**
- [`CrawlerRunner.crawl`](scrapy.md#sym-scrapy_crawler.py-421) — 启动一个爬虫进行爬取。

*来源: `scrapy/crawler.py:457`*

---
<a id="sym-scrapy_crawler.py-474"></a>

### `CrawlerRunner.stop` · method
```python
def stop(self) -> Deferred[Any]
```

停止所有正在运行的爬取任务。

**Parameters**
- `self` - CrawlerRunner 实例

**Returns**
- `Deferred[Any]` - 在所有爬取任务结束时触发的 deferred 对象

**Raises**
- (unknown)

**内部调用(库内):**
- [`Crawler.stop_async`](scrapy.md#sym-scrapy_crawler.py-246) — Crawler.stop_async 方法用于异步启动爬虫的优雅停止过程。

*来源: `scrapy/crawler.py:474`*

---
<a id="sym-scrapy_crawler.py-483"></a>

### `CrawlerRunner.join` · method
装饰器: `@inlineCallbacks`
```python
def join(self) -> Generator[Deferred[Any], Any, None]
```

等待所有管理的爬虫执行完成。

**Returns**
- `Generator[Deferred[Any], Any, None]`: 一个生成器，返回一个在所有爬虫执行完成后被触发的 deferred 对象。

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:483`*

---
<a id="sym-scrapy_crawler.py-494"></a>

### `AsyncCrawlerRunner` · class
```python
class AsyncCrawlerRunner(CrawlerRunnerBase)
```

`AsyncCrawlerRunner` 是一个用于异步运行爬虫的类，负责管理爬虫的启动、执行和停止。

### 方法说明

- **`__init__(self, settings: dict[str, Any] | Settings | None = None)`**  
  初始化 `AsyncCrawlerRunner` 实例，可传入配置项。

- **`crawl(self, crawler_or_spidercls: type[Spider] | str | Crawler, *args: Any, **kwargs: Any) -> asyncio.Task[None]`**  
  启动一个爬虫任务，返回一个 `asyncio.Task` 对象。

- **`_crawl_and_track(self, crawler: Crawler, *args: Any, **kwargs: Any) -> None`**  
  内部方法，用于跟踪爬虫任务的执行。

- **`_done(self, task: asyncio.Task[None], crawler: Crawler) -> None`**  
  内部方法，处理爬虫任务完成后的逻辑。

- **`_crawl(self, crawler: Crawler, *args: Any, **kwargs: Any) -> asyncio.Task[None]`**  
  内部方法，执行爬虫任务并返回一个 `asyncio.Task`。

- **`stop(self) -> None`**  
  停止所有正在运行的爬虫任务。

- **`join(self) -> None`**  
  等待所有爬虫任务完成。

*来源: `scrapy/crawler.py:494`*

---
<a id="sym-scrapy_crawler.py-517"></a>

### `AsyncCrawlerRunner.__init__` · method
```python
def __init__(self, settings: dict[str, Any] | Settings | None = None)
```

初始化 AsyncCrawlerRunner 实例，设置配置并初始化活跃任务集合。

**Parameters**
- `settings`: 配置字典、Settings 对象或 None。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:517`*

---
<a id="sym-scrapy_crawler.py-521"></a>

### `AsyncCrawlerRunner.crawl` · method
```python
def crawl(
        self,
        crawler_or_spidercls: type[Spider] | str | Crawler,
        *args: Any,
        **kwargs: Any,
    ) -> asyncio.Task[None]
```

运行一个爬虫，并返回一个在爬取完成后完成的异步任务。

**Parameters**:
- `crawler_or_spidercls`: 已经创建的爬虫实例、爬虫类或项目内的爬虫名称。
- `*args`: 用于初始化爬虫的参数。
- `**kwargs`: 用于初始化爬虫的关键词参数。

**Returns**:
- 一个 `asyncio.Task[None]` 对象，当爬取完成后该任务将完成。

**Raises**:
- `ValueError`: 如果 `crawler_or_spidercls` 参数是一个 spider 对象而不是 spider 类或 Crawler 对象。
- `RuntimeError`: 如果启用了 Twisted Reactor 但未安装 Twisted 或 asyncio 的 reactor。

**内部调用(库内):**
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)
- [`is_asyncio_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-220)
- [`CrawlerRunnerBase.create_crawler`](scrapy.md#sym-scrapy_crawler.py-360) — 创建并返回一个 `scrapy.crawler.Crawler` 对象。
- [`AsyncCrawlerRunner._crawl`](scrapy.md#sym-scrapy_crawler.py-586) — 异步爬取任务的启动与跟踪。

*来源: `scrapy/crawler.py:521`*

---
<a id="sym-scrapy_crawler.py-572"></a>

### `AsyncCrawlerRunner._crawl_and_track` · method
```python
async def _crawl_and_track(
        self, crawler: Crawler, *args: Any, **kwargs: Any
    ) -> None
```

异步爬取并跟踪爬虫执行状态。

**Parameters**
- `crawler` (Crawler): 要爬取的爬虫实例。
- `*args` (Any): 传递给爬虫的参数。
- `**kwargs` (Any): 传递给爬虫的关键字参数。

**Returns**
- (None): 无返回值。

**Raises**
- (Exception): 如果爬取过程中发生异常，则设置 `bootstrap_failed` 标志并重新抛出异常。

**内部调用(库内):**
- [`Crawler.crawl_async`](scrapy.md#sym-scrapy_crawler.py-200) — 启动爬虫并异步执行，仅可调用一次。

*来源: `scrapy/crawler.py:572`*

---
<a id="sym-scrapy_crawler.py-581"></a>

### `AsyncCrawlerRunner._done` · method
```python
def _done(self, task: asyncio.Task[None], crawler: Crawler) -> None
```

处理异步爬虫任务完成后的清理和状态更新。

**Parameters**
- `task`: asyncio.Task[None] - 已完成的异步任务
- `crawler`: Crawler - 对应的爬虫实例

**Returns**
- `None`

**Raises**
- `(unknown)`

*来源: `scrapy/crawler.py:581`*

---
<a id="sym-scrapy_crawler.py-586"></a>

### `AsyncCrawlerRunner._crawl` · method
```python
def _crawl(self, crawler: Crawler, *args: Any, **kwargs: Any) -> asyncio.Task[None]
```

异步爬取任务的启动与跟踪。

**Parameters**
- `crawler`: Crawler - 要启动爬取的爬虫实例。
- `*args`: Any - 传递给爬虫的参数。
- `**kwargs`: Any - 传递给爬虫的关键字参数。

**Returns**
- `asyncio.Task[None]` - 表示异步爬取任务的 `Task` 对象。

**Raises**
- (unknown)

**内部调用(库内):**
- [`AsyncCrawlerRunner._crawl_and_track`](scrapy.md#sym-scrapy_crawler.py-572) — 异步爬取并跟踪爬虫执行状态。

*来源: `scrapy/crawler.py:586`*

---
<a id="sym-scrapy_crawler.py-598"></a>

### `AsyncCrawlerRunner.stop` · method
```python
async def stop(self) -> None
```

停止所有正在运行的爬取任务，并等待它们全部结束。

**Parameters**
- `self` - AsyncCrawlerRunner 实例

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`CallLaterOnce.wait`](scrapy_utils.md#sym-scrapy_utils_reactor.py-86)
- [`Crawler.stop_async`](scrapy.md#sym-scrapy_crawler.py-246) — Crawler.stop_async 方法用于异步启动爬虫的优雅停止过程。

*来源: `scrapy/crawler.py:598`*

---
<a id="sym-scrapy_crawler.py-609"></a>

### `AsyncCrawlerRunner.join` · method
```python
async def join(self) -> None
```

等待所有管理的爬虫执行完成。

**Parameters**
- `self` - AsyncCrawlerRunner 实例

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`CallLaterOnce.wait`](scrapy_utils.md#sym-scrapy_utils_reactor.py-86)

*来源: `scrapy/crawler.py:609`*

---
<a id="sym-scrapy_crawler.py-618"></a>

### `CrawlerProcessBase` · class
```python
class CrawlerProcessBase(CrawlerRunnerBase)
```

`CrawlerProcessBase` 是一个用于运行爬虫进程的基类，负责管理爬虫的启动、停止和信号处理。

### 方法说明

- **`__init__(self, settings: dict[str, Any] | Settings | None = None, install_root_handler: bool = True)`**  
  初始化爬虫进程，可传入配置项和是否安装根日志处理器。

- **`start(self, stop_after_crawl: bool = True, install_signal_handlers: bool = True) -> None`**  
  启动爬虫进程，可以选择是否在爬取结束后自动停止，并控制是否安装信号处理器。

- **`_signal_shutdown(self, signum: int, _: Any) -> None`**  
  处理关闭信号（如 SIGTERM），用于优雅地关闭爬虫进程。

- **`_signal_kill(self, signum: int, _: Any) -> None`**  
  处理终止信号（如 SIGKILL），用于强制关闭爬虫进程。

- **`_log_shutdown(signum: int) -> None`**  
  记录关闭信号的日志信息。

- **`_log_kill(signum: int) -> None`**  
  记录终止信号的日志信息。

- **`_setup_reactor(self, install_signal_handlers: bool) -> None`**  
  设置反应器（reactor）并可选择是否安装信号处理器。

- **`_stop_dfd(self) -> Deferred[Any]`**

*来源: `scrapy/crawler.py:618`*

---
<a id="sym-scrapy_crawler.py-619"></a>

### `CrawlerProcessBase.__init__` · method
```python
def __init__(
        self,
        settings: dict[str, Any] | Settings | None = None,
        install_root_handler: bool = True,
    )
```

初始化 CrawlerProcessBase 实例，配置日志记录并记录 Scrapy 信息。

**Parameters**
- `settings` (dict[str, Any] | Settings | None): 配置设置，可为字典、Settings 对象或 None。
- `install_root_handler` (bool): 是否安装根处理器，默认为 True。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`configure_logging`](scrapy_utils.md#sym-scrapy_utils_log.py-91)
- [`log_scrapy_info`](scrapy_utils.md#sym-scrapy_utils_log.py-187)

*来源: `scrapy/crawler.py:619`*

---
<a id="sym-scrapy_crawler.py-629"></a>

### `CrawlerProcessBase.start` · method
装饰器: `@abstractmethod`
```python
def start(
        self, stop_after_crawl: bool = True, install_signal_handlers: bool = True
    ) -> None
```

CrawlerProcessBase.start 用于启动爬虫进程。

**Parameters**:
- `stop_after_crawl` (bool): 是否在爬虫完成后自动停止，默认为 True。
- `install_signal_handlers` (bool): 是否安装信号处理器，默认为 True。

**Returns**:
- (unknown)

**Raises**:
- (unknown)

*来源: `scrapy/crawler.py:629`*

---
<a id="sym-scrapy_crawler.py-634"></a>

### `CrawlerProcessBase._signal_shutdown` · method
```python
def _signal_shutdown(self, signum: int, _: Any) -> None
```

CrawlerProcessBase._signal_shutdown 用于处理信号关闭请求。

**Parameters**
- `signum`: int - 信号编号
- `_`: Any - 未使用的参数

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`install_shutdown_handlers`](scrapy_utils.md#sym-scrapy_utils_ossignal.py-21)
- [`CrawlerProcessBase._log_shutdown`](scrapy.md#sym-scrapy_crawler.py-649) — 记录关闭信号的日志信息。

*来源: `scrapy/crawler.py:634`*

---
<a id="sym-scrapy_crawler.py-641"></a>

### `CrawlerProcessBase._signal_kill` · method
```python
def _signal_kill(self, signum: int, _: Any) -> None
```

处理信号以终止爬虫进程。

**Parameters**
- `signum`: 信号编号
- `_`: 任意类型参数，未使用

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`install_shutdown_handlers`](scrapy_utils.md#sym-scrapy_utils_ossignal.py-21)
- [`CrawlerProcessBase._log_kill`](scrapy.md#sym-scrapy_crawler.py-657) — 在接收到两次信号时记录强制关闭的日志。

*来源: `scrapy/crawler.py:641`*

---
<a id="sym-scrapy_crawler.py-649"></a>

### `CrawlerProcessBase._log_shutdown` · method
装饰器: `@staticmethod`
```python
def _log_shutdown(signum: int) -> None
```

记录关闭信号的日志信息。

**Parameters**
- `signum`: int - 信号编号

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/crawler.py:649`*

---
<a id="sym-scrapy_crawler.py-657"></a>

### `CrawlerProcessBase._log_kill` · method
装饰器: `@staticmethod`
```python
def _log_kill(signum: int) -> None
```

在接收到两次信号时记录强制关闭的日志。

**Parameters**
- `signum`: int - 信号编号

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/crawler.py:657`*

---
<a id="sym-scrapy_crawler.py-663"></a>

### `CrawlerProcessBase._setup_reactor` · method
```python
def _setup_reactor(self, install_signal_handlers: bool) -> None
```

设置 Twisted 反应器并配置 DNS 解析器和线程池。

**Parameters**
- `install_signal_handlers` (bool): 是否安装信号处理器。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/crawler.py:663`*

---
<a id="sym-scrapy_crawler.py-702"></a>

### `CrawlerProcessBase._stop_dfd` · method
装饰器: `@abstractmethod`
```python
def _stop_dfd(self) -> Deferred[Any]
```

停止爬虫进程的延迟对象，由子类实现。

**Parameters**
- 无

**Returns**
- `Deferred[Any]`: 表示停止操作的延迟对象

**Raises**
- `NotImplementedError`: 当前方法未被实现，必须在子类中重写

*来源: `scrapy/crawler.py:702`*

---
<a id="sym-scrapy_crawler.py-706"></a>

### `CrawlerProcessBase._graceful_stop_reactor` · method
装饰器: `@inlineCallbacks`
```python
def _graceful_stop_reactor(self) -> Generator[Deferred[Any], Any, None]
```

停止 Reactor 的优雅过程。

**Parameters**

- `self` - `CrawlerProcessBase` 实例

**Returns**

- `Generator[Deferred[Any], Any, None]` - 一个生成器，用于异步执行停止操作

**Raises**

- (unknown)

**内部调用(库内):**
- [`CrawlerProcessBase._stop_dfd`](scrapy.md#sym-scrapy_crawler.py-702) — 停止爬虫进程的延迟对象，由子类实现。
- [`CrawlerProcessBase._stop_reactor`](scrapy.md#sym-scrapy_crawler.py-712) — 停止 Twisted 反应器。

*来源: `scrapy/crawler.py:706`*

---
<a id="sym-scrapy_crawler.py-712"></a>

### `CrawlerProcessBase._stop_reactor` · method
```python
def _stop_reactor(self, _: Any = None) -> None
```

停止 Twisted 反应器。

**Parameters**
- `_`: 任意类型，未使用。

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`Crawler.stop`](scrapy.md#sym-scrapy_crawler.py-236) — Crawler.stop 方法用于启动爬虫的优雅停止过程，并在爬虫停止时返回一个已触发的 deferred 对象。

*来源: `scrapy/crawler.py:712`*

---
<a id="sym-scrapy_crawler.py-720"></a>

### `CrawlerProcess` · class
```python
class CrawlerProcess(CrawlerProcessBase, CrawlerRunner)
```

`CrawlerProcess` 类用于启动和管理一个独立的爬虫进程，它继承自 `CrawlerProcessBase` 和 `CrawlerRunner`，负责运行爬虫并处理其生命周期。

### 方法说明

- **`__init__(self, settings: dict[str, Any] | Settings | None = None, install_root_handler: bool = True)`**
  - 初始化爬虫进程，可传入配置项 `settings` 和是否安装根日志处理器 `install_root_handler`。
  - 文件: `scrapy/crawler.py:20`

- **`_create_crawler(self, spidercls: type[Spider] | str) -> Crawler`**
  - 根据给定的爬虫类或名称创建一个 `Crawler` 实例。
  - 文件: `scrapy/crawler.py:35`

- **`_stop_dfd(self) -> Deferred[Any]`**
  - 返回一个 `Deferred` 对象，用于停止爬虫进程。
  - 文件: `scrapy/crawler.py:40`

- **`start(self, stop_after_crawl: bool = True, install_signal_handlers: bool = True) -> None`**
  - 启动爬虫进程，可以选择在爬取结束后是否停止，并是否安装信号处理器。
  - 文件: `scrapy/crawler.py:45`

*来源: `scrapy/crawler.py:720`*

---
<a id="sym-scrapy_crawler.py-747"></a>

### `CrawlerProcess.__init__` · method
```python
def __init__(
        self,
        settings: dict[str, Any] | Settings | None = None,
        install_root_handler: bool = True,
    )
```

CrawlerProcess 初始化方法，用于创建并配置爬虫进程实例。

**Parameters**
- `settings`: 配置项字典或 Settings 对象，用于初始化爬虫设置。
- `install_root_handler`: 布尔值，指定是否安装根日志处理器。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/crawler.py:747`*

---
<a id="sym-scrapy_crawler.py-756"></a>

### `CrawlerProcess._create_crawler` · method
```python
def _create_crawler(self, spidercls: type[Spider] | str) -> Crawler
```

创建一个用于爬取的 Crawler 实例。

**Parameters**
- `spidercls`: 爬虫类或爬虫类名字符串

**Returns**
- `Crawler`: 用于爬取的爬虫实例

**Raises**
- (unknown)

**内部调用(库内):**
- [`Crawler`](scrapy.md#sym-scrapy_crawler.py-57) — `Crawler` 类代表一个爬虫实例，负责管理爬虫的生命周期、配置、组件和执行引擎。

*来源: `scrapy/crawler.py:756`*

---
<a id="sym-scrapy_crawler.py-763"></a>

### `CrawlerProcess._stop_dfd` · method
```python
def _stop_dfd(self) -> Deferred[Any]
```

停止爬虫进程的异步操作。

**Parameters**
- `self` - CrawlerProcess 实例

**Returns**
- `Deferred[Any]` - 表示停止操作完成的延迟对象

**Raises**
- (unknown)

**内部调用(库内):**
- [`Crawler.stop`](scrapy.md#sym-scrapy_crawler.py-236) — Crawler.stop 方法用于启动爬虫的优雅停止过程，并在爬虫停止时返回一个已触发的 deferred 对象。

*来源: `scrapy/crawler.py:763`*

---
<a id="sym-scrapy_crawler.py-766"></a>

### `CrawlerProcess.start` · method
```python
def start(
        self, stop_after_crawl: bool = True, install_signal_handlers: bool = True
    ) -> None
```

启动爬虫进程并运行 Twisted reactor，可选择在爬虫完成后停止 reactor 并安装信号处理器。

**Parameters**:
- `stop_after_crawl` (bool): 在爬虫完成后是否停止 reactor，默认为 True。
- `install_signal_handlers` (bool): 是否安装操作系统的信号处理器，默认为 True。

**Returns**:
- (unknown)

**Raises**:
- (unknown)

**内部调用(库内):**
- [`CrawlerProcessBase._setup_reactor`](scrapy.md#sym-scrapy_crawler.py-663) — 设置 Twisted 反应器并配置 DNS 解析器和线程池。

*来源: `scrapy/crawler.py:766`*

---
<a id="sym-scrapy_crawler.py-796"></a>

### `AsyncCrawlerProcess` · class
```python
class AsyncCrawlerProcess(CrawlerProcessBase, AsyncCrawlerRunner)
```

`AsyncCrawlerProcess` 是一个异步爬虫进程管理器，负责启动和管理异步爬虫的执行流程。

### 关键方法说明

- `__init__(self, settings: dict[str, Any] | Settings | None = None, install_root_handler: bool = True)`  
  初始化异步爬虫进程，可传入配置项和是否安装根日志处理器。

- `start(self, stop_after_crawl: bool = True, install_signal_handlers: bool = True) -> None`  
  启动异步爬虫进程，可以选择是否在爬取结束后停止，并安装信号处理器。

- `_start_asyncio(self, stop_after_crawl: bool, install_signal_handlers: bool) -> None`  
  启动 asyncio 事件循环以运行爬虫任务。

- `_run_loop(self, install_signal_handlers: bool) -> None`  
  运行事件循环，处理爬虫任务。

- `_close_loop(self) -> None`  
  关闭事件循环。

- `_cancel_all_tasks(loop: asyncio.AbstractEventLoop) -> None`  
  取消事件循环中所有待处理的任务。

- `_signal_shutdown_reactorless(self, signum: int, _: Any) -> None`  
  处理关闭信号，用于非 Reactor 环境下的优雅关闭。

- `_create_shutdown_task(self) -> None`  
  创建关闭任务。

- `_shutdown_graceful_reactorless(self) -> None`  
  在非 Reactor

*来源: `scrapy/crawler.py:796`*

---
<a id="sym-scrapy_crawler.py-828"></a>

### `AsyncCrawlerProcess.__init__` · method
```python
def __init__(
        self,
        settings: dict[str, Any] | Settings | None = None,
        install_root_handler: bool = True,
    )
```

AsyncCrawlerProcess 的初始化方法，用于设置异步爬虫进程的配置和事件循环。

**Parameters**
- `settings` (dict[str, Any] | Settings | None): 配置设置，可以是字典、Settings 对象或 None。
- `install_root_handler` (bool): 是否安装根日志处理器，默认为 True。

**Returns**
- (unknown)

**Raises**
- `RuntimeError`: 当 `TWISTED_REACTOR_ENABLED` 为 False 但已安装 Twisted 反应器时抛出。

**内部调用(库内):**
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)
- [`set_asyncio_event_loop`](scrapy_utils.md#sym-scrapy_utils_reactor.py-136)
- [`install_reactor_import_hook`](scrapy_utils.md#sym-scrapy_utils_reactorless.py-50)
- [`verify_installed_reactor`](scrapy_utils.md#sym-scrapy_utils_reactor.py-169)
- [`verify_installed_asyncio_event_loop`](scrapy_utils.md#sym-scrapy_utils_reactor.py-189)
- [`install_reactor`](scrapy_utils.md#sym-scrapy_utils_reactor.py-114)

*来源: `scrapy/crawler.py:828`*

---
<a id="sym-scrapy_crawler.py-861"></a>

### `AsyncCrawlerProcess._stop_dfd` · method
```python
def _stop_dfd(self) -> Deferred[Any]
```

停止异步爬虫进程并返回一个 Deferred 对象。

**Parameters**
- `self` - AsyncCrawlerProcess 实例

**Returns**
- `Deferred[Any]` - 表示停止操作的 Deferred 对象

**Raises**
- (unknown)

**内部调用(库内):**
- [`Crawler.stop`](scrapy.md#sym-scrapy_crawler.py-236) — Crawler.stop 方法用于启动爬虫的优雅停止过程，并在爬虫停止时返回一个已触发的 deferred 对象。

*来源: `scrapy/crawler.py:861`*

---
<a id="sym-scrapy_crawler.py-864"></a>

### `AsyncCrawlerProcess.start` · method
```python
def start(
        self, stop_after_crawl: bool = True, install_signal_handlers: bool = True
    ) -> None
```

启动异步爬虫进程，根据配置选择使用 asyncio 或 Twisted 运行时。

**Parameters**

- `stop_after_crawl` (bool): 在所有爬虫完成后是否停止运行时，默认为 True。
- `install_signal_handlers` (bool): 是否安装操作系统信号处理器，默认为 True。

**Returns**

- (unknown)

**Raises**

- (unknown)

**内部调用(库内):**
- [`AsyncCrawlerProcess._start_asyncio`](scrapy.md#sym-scrapy_crawler.py-891) — 启动异步事件循环以运行爬虫，支持在爬取完成后停止或持续运行，并处理信号量关闭。
- [`AsyncCrawlerProcess._start_twisted`](scrapy.md#sym-scrapy_crawler.py-1039) — 启动 Twisted 事件循环并可选择在爬取结束后停止，同时设置信号处理器。

*来源: `scrapy/crawler.py:864`*

---
<a id="sym-scrapy_crawler.py-891"></a>

### `AsyncCrawlerProcess._start_asyncio` · method
```python
def _start_asyncio(
        self, stop_after_crawl: bool, install_signal_handlers: bool
    ) -> None
```

启动异步事件循环以运行爬虫，支持在爬取完成后停止或持续运行，并处理信号量关闭。

**Parameters**
- `stop_after_crawl` (bool): 爬取完成后是否停止事件循环。
- `install_signal_handlers` (bool): 是否安装信号处理器以响应中断。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`AsyncCrawlerProcess._run_loop`](scrapy.md#sym-scrapy_crawler.py-961) — 运行异步爬虫进程的主循环，可选择是否安装信号处理器。
- [`AsyncCrawlerProcess._close_loop`](scrapy.md#sym-scrapy_crawler.py-969) — 关闭异步事件循环并清理相关资源。

*来源: `scrapy/crawler.py:891`*

---
<a id="sym-scrapy_crawler.py-961"></a>

### `AsyncCrawlerProcess._run_loop` · method
```python
def _run_loop(self, install_signal_handlers: bool) -> None
```

运行异步爬虫进程的主循环，可选择是否安装信号处理器。

**Parameters**
- `install_signal_handlers` (bool): 是否安装信号处理器。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`install_shutdown_handlers`](scrapy_utils.md#sym-scrapy_utils_ossignal.py-21)

*来源: `scrapy/crawler.py:961`*

---
<a id="sym-scrapy_crawler.py-969"></a>

### `AsyncCrawlerProcess._close_loop` · method
```python
def _close_loop(self) -> None
```

关闭异步事件循环并清理相关资源。

**Parameters**
- `self`: AsyncCrawlerProcess 实例

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`AsyncCrawlerProcess._cancel_all_tasks`](scrapy.md#sym-scrapy_crawler.py-984) — 取消所有 asyncio 任务并在关闭时处理未处理的异常。

*来源: `scrapy/crawler.py:969`*

---
<a id="sym-scrapy_crawler.py-984"></a>

### `AsyncCrawlerProcess._cancel_all_tasks` · method
装饰器: `@staticmethod`
```python
def _cancel_all_tasks(loop: asyncio.AbstractEventLoop) -> None
```

取消所有 asyncio 任务并在关闭时处理未处理的异常。

**Parameters**
- `loop` (asyncio.AbstractEventLoop): 要取消所有任务的事件循环。

**Returns**
- `None`

**Raises**
- `(unknown)`

*来源: `scrapy/crawler.py:984`*

---
<a id="sym-scrapy_crawler.py-1007"></a>

### `AsyncCrawlerProcess._signal_shutdown_reactorless` · method
```python
def _signal_shutdown_reactorless(self, signum: int, _: Any) -> None
```

处理信号以关闭异步爬虫进程。

**Parameters**
- `signum`: 信号编号
- `_`: 任意参数，未使用

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`install_shutdown_handlers`](scrapy_utils.md#sym-scrapy_utils_ossignal.py-21)
- [`CrawlerProcessBase._log_shutdown`](scrapy.md#sym-scrapy_crawler.py-649) — 记录关闭信号的日志信息。

*来源: `scrapy/crawler.py:1007`*

---
<a id="sym-scrapy_crawler.py-1015"></a>

### `AsyncCrawlerProcess._create_shutdown_task` · method
```python
def _create_shutdown_task(self) -> None
```

创建一个关闭任务以优雅地停止异步爬虫进程。

**Parameters**
- `self` - AsyncCrawlerProcess 实例

**Returns**
- `None`

**Raises**
- `RuntimeError` - 当无法创建任务时抛出，此时协程会被关闭。

**内部调用(库内):**
- [`AsyncCrawlerProcess._shutdown_graceful_reactorless`](scrapy.md#sym-scrapy_crawler.py-1023) — 优雅关闭爬虫进程，等待当前任务完成并取消主任务。

*来源: `scrapy/crawler.py:1015`*

---
<a id="sym-scrapy_crawler.py-1023"></a>

### `AsyncCrawlerProcess._shutdown_graceful_reactorless` · method
```python
async def _shutdown_graceful_reactorless(self) -> None
```

优雅关闭爬虫进程，等待当前任务完成并取消主任务。

**Parameters**
- `self` - AsyncCrawlerProcess 实例

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`Crawler.stop`](scrapy.md#sym-scrapy_crawler.py-236) — Crawler.stop 方法用于启动爬虫的优雅停止过程，并在爬虫停止时返回一个已触发的 deferred 对象。

*来源: `scrapy/crawler.py:1023`*

---
<a id="sym-scrapy_crawler.py-1031"></a>

### `AsyncCrawlerProcess._signal_kill_reactorless` · method
```python
def _signal_kill_reactorless(self, signum: int, _: Any) -> None
```

处理信号以终止异步爬虫进程，不使用反应器。

**Parameters**
- `signum`: 信号编号
- `_`: 任意参数，用于信号处理接口，未被使用

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`install_shutdown_handlers`](scrapy_utils.md#sym-scrapy_utils_ossignal.py-21)
- [`CrawlerProcessBase._log_kill`](scrapy.md#sym-scrapy_crawler.py-657) — 在接收到两次信号时记录强制关闭的日志。

*来源: `scrapy/crawler.py:1031`*

---
<a id="sym-scrapy_crawler.py-1039"></a>

### `AsyncCrawlerProcess._start_twisted` · method
```python
def _start_twisted(
        self, stop_after_crawl: bool, install_signal_handlers: bool
    ) -> None
```

启动 Twisted 事件循环并可选择在爬取结束后停止，同时设置信号处理器。

**Parameters**
- `stop_after_crawl` (bool): 是否在爬取结束后自动停止事件循环。
- `install_signal_handlers` (bool): 是否安装信号处理器。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`CrawlerProcessBase._setup_reactor`](scrapy.md#sym-scrapy_crawler.py-663) — 设置 Twisted 反应器并配置 DNS 解析器和线程池。

*来源: `scrapy/crawler.py:1039`*

---

## `scrapy/dupefilters.py`

<a id="sym-scrapy_dupefilters.py-27"></a>

### `BaseDupeFilter` · class
```python
class BaseDupeFilter
```

`BaseDupeFilter` 是一个用于去重请求的基类，负责判断请求是否已经处理过，以避免重复抓取。

### 方法说明

- `from_crawler(cls, crawler: Crawler) -> Self`  
  从爬虫实例中创建并初始化去重过滤器的类方法。

- `request_seen(self, request: Request) -> bool`  
  检查给定的请求是否已经处理过，返回布尔值表示是否已见过该请求。

- `open(self) -> Deferred[None] | None`  
  打开去重过滤器，通常用于初始化资源，可能返回一个延迟对象或 `None`。

- `close(self, reason: str) -> Deferred[None] | None`  
  关闭去重过滤器，通常用于清理资源，可能返回一个延迟对象或 `None`。

- `log(self, request: Request, spider: Spider) -> None`  
  记录请求的日志信息，通常用于调试或监控重复请求。

*来源: `scrapy/dupefilters.py:27`*

---
<a id="sym-scrapy_dupefilters.py-32"></a>

### `BaseDupeFilter.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

从爬虫实例创建去重过滤器的类方法。

**Parameters**
- `crawler` (Crawler): 爬虫实例，用于配置去重过滤器。

**Returns**
- `Self`: 新创建的去重过滤器实例。

**Raises**
- (unknown)

*来源: `scrapy/dupefilters.py:32`*

---
<a id="sym-scrapy_dupefilters.py-35"></a>

### `BaseDupeFilter.request_seen` · method
```python
def request_seen(self, request: Request) -> bool
```

检查请求是否已见过，用于去重。

**Parameters**
- `request`: Request - 要检查的请求对象

**Returns**
- `bool` - 如果请求已见过则返回 True，否则返回 False

**Raises**
- (unknown)

*来源: `scrapy/dupefilters.py:35`*

---
<a id="sym-scrapy_dupefilters.py-38"></a>

### `BaseDupeFilter.open` · method
```python
def open(self) -> Deferred[None] | None
```

初始化去重过滤器实例。

**Parameters**
- `self` - BaseDupeFilter 类的实例。

**Returns**
- `Deferred[None] | None` - 异步操作的延迟对象或 None。

**Raises**
- (unknown)

*来源: `scrapy/dupefilters.py:38`*

---
<a id="sym-scrapy_dupefilters.py-41"></a>

### `BaseDupeFilter.close` · method
```python
def close(self, reason: str) -> Deferred[None] | None
```

关闭去重过滤器，执行清理操作。

**Parameters**
- `reason`: str - 关闭原因

**Returns**
- `Deferred[None] | None` - 异步关闭操作的延迟结果或 None

**Raises**
- (unknown)

*来源: `scrapy/dupefilters.py:41`*

---
<a id="sym-scrapy_dupefilters.py-44"></a>

### `BaseDupeFilter.log` · method
```python
def log(self, request: Request, spider: Spider) -> None
```

用途:记录一个请求被去重过滤的日志信息。

**Parameters**
- `request`: Request - 被过滤的请求对象。
- `spider`: Spider - 发起请求的爬虫对象。

**Returns**
- `None`

**Raises**
- `ScrapyDeprecationWarning` - 调用此方法时会发出弃用警告。

*来源: `scrapy/dupefilters.py:44`*

---
<a id="sym-scrapy_dupefilters.py-53"></a>

### `RFPDupeFilter` · class
```python
class RFPDupeFilter(BaseDupeFilter)
```

RFPDupeFilter 是一个基于请求指纹的重复过滤器，用于在爬虫中识别和过滤重复的请求。

### 方法说明

- `__init__(self, path: str | None = None, debug: bool = False, *, fingerprinter: RequestFingerprinterProtocol | None = None) -> None`  
  初始化一个 RFPDupeFilter 实例，可指定存储路径、调试模式以及请求指纹生成器。

- `from_crawler(cls, crawler: Crawler) -> Self`  
  从爬虫实例创建并返回一个 RFPDupeFilter 实例，通常用于爬虫框架内部初始化。

- `request_seen(self, request: Request) -> bool`  
  检查请求是否已经处理过，如果已处理则返回 True，否则返回 False。

- `request_fingerprint(self, request: Request) -> str`  
  根据请求生成一个指纹字符串，用于标识请求的唯一性。

- `close(self, reason: str) -> None`  
  关闭过滤器，通常用于清理资源或保存状态。

- `log(self, request: Request, spider: Spider) -> None`  
  记录请求日志，通常在调试模式下使用，记录重复请求的详细信息。

*来源: `scrapy/dupefilters.py:53`*

---
<a id="sym-scrapy_dupefilters.py-72"></a>

### `RFPDupeFilter.__init__` · method
```python
def __init__(
        self,
        path: str | None = None,
        debug: bool = False,
        *,
        fingerprinter: RequestFingerprinterProtocol | None = None,
    ) -> None
```

RFPDupeFilter.__init__ 用于初始化重复请求过滤器，管理请求指纹集合并可选地从文件中加载已见请求。

**Parameters**
- `path`: str | None = None - 用于存储已见请求的文件路径。
- `debug`: bool = False - 是否启用调试模式。
- `fingerprinter`: RequestFingerprinterProtocol | None = None - 用于生成请求指纹的协议实现。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/dupefilters.py:72`*

---
<a id="sym-scrapy_dupefilters.py-97"></a>

### `RFPDupeFilter.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

从爬虫实例创建 RFPDupeFilter 实例。

**Parameters**
- `crawler` (Crawler): 爬虫实例，用于获取设置和指纹生成器。

**Returns**
- `Self`: 新创建的 RFPDupeFilter 实例。

**Raises**
- (unknown)

**内部调用(库内):**
- [`job_dir`](scrapy_utils.md#sym-scrapy_utils_job.py-10)

*来源: `scrapy/dupefilters.py:97`*

---
<a id="sym-scrapy_dupefilters.py-106"></a>

### `RFPDupeFilter.request_seen` · method
```python
def request_seen(self, request: Request) -> bool
```

检查请求是否已见过，若未见过则记录该请求的指纹。

**Parameters**
- `request`: Request - 要检查的请求对象

**Returns**
- `bool` - 如果请求已见过则返回 True，否则返回 False 并记录该请求

**Raises**
- (unknown)

**内部调用(库内):**
- [`RFPDupeFilter.request_fingerprint`](scrapy.md#sym-scrapy_dupefilters.py-115) — 计算指定请求的唯一指纹字符串。

*来源: `scrapy/dupefilters.py:106`*

---
<a id="sym-scrapy_dupefilters.py-115"></a>

### `RFPDupeFilter.request_fingerprint` · method
```python
def request_fingerprint(self, request: Request) -> str
```

计算指定请求的唯一指纹字符串。

**Parameters**
- `request` (Request): 要计算指纹的请求对象。

**Returns**
- `str`: 表示请求唯一标识的十六进制字符串。

*来源: `scrapy/dupefilters.py:115`*

---
<a id="sym-scrapy_dupefilters.py-119"></a>

### `RFPDupeFilter.close` · method
```python
def close(self, reason: str) -> None
```

关闭去重过滤器并关闭相关文件。

**Parameters**
- `reason`: 关闭原因字符串。

**Returns**
- `None`

**Raises**
- `(unknown)`

*来源: `scrapy/dupefilters.py:119`*

---
<a id="sym-scrapy_dupefilters.py-123"></a>

### `RFPDupeFilter.log` · method
```python
def log(self, request: Request, spider: Spider) -> None
```

记录重复请求的日志。

**Parameters**
- `request`: Request - 被过滤的请求对象。
- `spider`: Spider - 发起请求的爬虫对象。

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`referer_str`](scrapy_utils.md#sym-scrapy_utils_request.py-150)

*来源: `scrapy/dupefilters.py:123`*

---

## `scrapy/exceptions.py`

<a id="sym-scrapy_exceptions.py-18"></a>

### `NotConfigured` · class
```python
class NotConfigured(Exception)
```

`NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。

该类继承自 `Exception`，没有额外的方法或属性。它主要用于框架内部，在遇到未配置的组件时抛出此异常，以提示用户或框架需要进行相应的配置。

典型用法是在配置检查阶段，当某个必需的配置项缺失时，抛出该异常以通知调用方配置不完整。例如：

```python
if not self.settings.get('SOME_REQUIRED_SETTING'):
    raise NotConfigured
```

(unknown)

*来源: `scrapy/exceptions.py:18`*

---
<a id="sym-scrapy_exceptions.py-22"></a>

### `_InvalidOutput` · class
```python
class _InvalidOutput(TypeError)
```

这个类 `_InvalidOutput` 是一个类型错误的子类，用于表示爬虫输出数据无效的情况。

```markdown

## _InvalidOutput

- **继承**: `TypeError`
- **职责**: 表示在爬虫处理过程中遇到的无效输出数据错误。
- **用法**: 当爬虫在处理请求或响应时发现输出不符合预期格式或类型时抛出此异常。
- **相关文件**: `scrapy/exceptions.py:行号` (注：实际行号未提供，但该类定义在 `scrapy/exceptions.py` 中)
```

*来源: `scrapy/exceptions.py:22`*

---
<a id="sym-scrapy_exceptions.py-32"></a>

### `IgnoreRequest` · class
```python
class IgnoreRequest(Exception)
```

`IgnoreRequest` 异常类用于指示爬虫应忽略某个请求，通常在请求中间件中抛出以阻止请求继续处理。

该类继承自 `Exception`，没有额外定义方法，因此其行为完全由异常机制决定。在爬虫流程中，当某个请求需要被跳过时，可以通过抛出此异常来实现。典型的使用场景是在 `SpiderMiddleware` 的 `process_request` 方法中，根据特定条件决定是否忽略该请求。

*来源: `scrapy/exceptions.py:32`*

---
<a id="sym-scrapy_exceptions.py-36"></a>

### `DontCloseSpider` · class
```python
class DontCloseSpider(Exception)
```

这个类代表一个异常，用于指示爬虫在遇到该异常时不应被关闭。

```markdown

## DontCloseSpider

- **继承自**: `Exception`
- **职责**: 当爬虫遇到此异常时，不会被关闭。
- **方法**: 无
```

*来源: `scrapy/exceptions.py:36`*

---
<a id="sym-scrapy_exceptions.py-40"></a>

### `CloseSpider` · class
```python
class CloseSpider(Exception)
```

`CloseSpider` 异常类用于在爬虫运行过程中主动触发爬虫关闭操作。

### 方法

- `__init__(self, reason: str = "cancelled")`  
  初始化 `CloseSpider` 异常实例，可选地指定关闭原因。

*来源: `scrapy/exceptions.py:40`*

---
<a id="sym-scrapy_exceptions.py-43"></a>

### `CloseSpider.__init__` · method
```python
def __init__(self, reason: str = "cancelled")
```

用途:初始化 CloseSpider 异常对象，设置关闭原因。

**Parameters**
- `reason`: str - 关闭爬虫的原因，默认为 "cancelled"

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exceptions.py:43`*

---
<a id="sym-scrapy_exceptions.py-48"></a>

### `StopDownload` · class
```python
class StopDownload(Exception)
```

`StopDownload` 异常类用于指示下载过程中应停止下载操作。

### 方法

- `__init__(self, *, fail: bool = True)`  
  初始化方法，接受一个可选的关键字参数 `fail`，默认值为 `True`。当 `fail` 为 `True` 时，表示下载失败；为 `False` 时，表示下载被正常中断。

*来源: `scrapy/exceptions.py:48`*

---
<a id="sym-scrapy_exceptions.py-57"></a>

### `StopDownload.__init__` · method
```python
def __init__(self, *, fail: bool = True)
```

StopDownload.__init__ 用于初始化 StopDownload 异常实例，设置是否失败标志。

**Parameters**
- `fail` (bool): 指定是否应引发失败，默认为 True。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exceptions.py:57`*

---
<a id="sym-scrapy_exceptions.py-62"></a>

### `DownloadConnectionRefusedError` · class
```python
class DownloadConnectionRefusedError(Exception)
```

`DownloadConnectionRefusedError` 类代表在下载过程中连接被拒绝时抛出的异常，用于处理网络连接失败的错误情况。

该异常类继承自 Python 内置的 `Exception` 类，没有额外定义的方法或属性。它通常在下载器尝试建立连接但被目标服务器拒绝时触发，属于 `scrapy.exceptions` 模块中定义的异常体系的一部分。

```python
class DownloadConnectionRefusedError(Exception)
```

- **职责**: 表示下载过程中因连接被拒绝而引发的错误。
- **使用场景**: 当网络请求由于目标主机拒绝连接而失败时，Scrapy 会抛出此异常以通知上层逻辑。

*来源: `scrapy/exceptions.py:62`*

---
<a id="sym-scrapy_exceptions.py-66"></a>

### `CannotResolveHostError` · class
```python
class CannotResolveHostError(Exception)
```

CannotResolveHostError 类用于表示在爬取过程中无法解析主机名的错误，通常由网络请求失败引发。

该类继承自 `Exception`，没有额外定义方法，因此其行为完全由父类 `Exception` 提供。它主要用于异常处理场景中，当爬虫遇到无法解析目标主机地址的情况时抛出此异常。

*来源: `scrapy/exceptions.py:66`*

---
<a id="sym-scrapy_exceptions.py-70"></a>

### `DownloadTimeoutError` · class
```python
class DownloadTimeoutError(Exception)
```

`DownloadTimeoutError` 类代表在下载过程中发生超时错误的异常类型，用于标识网络请求因超时而失败的情况。

该异常类继承自 Python 内置的 `Exception` 类，没有额外定义方法或属性。它通常在下载器（Downloader）检测到请求超过设定的超时时间时被抛出，以通知上层代码发生了超时错误。

典型用法是捕获此异常来处理因超时导致的下载失败情况，例如在自定义的下载中间件或爬虫逻辑中进行重试或记录日志等操作。

文件:scrapy/exceptions.py:行号 22

*来源: `scrapy/exceptions.py:70`*

---
<a id="sym-scrapy_exceptions.py-74"></a>

### `DownloadCancelledError` · class
```python
class DownloadCancelledError(Exception)
```

`DownloadCancelledError` 异常用于表示下载过程中被取消的情况。

该异常类没有定义任何特殊方法，直接继承自 Python 的 `Exception` 类，用于在下载任务被取消时抛出，以便上层代码能够捕获并处理此类异常。

```python
class DownloadCancelledError(Exception)
```

- **职责**: 标识下载操作因外部干预或内部逻辑而被取消。
- **用法**: 当下载过程中的某个条件满足时（例如用户主动取消、超时、资源不可用等），可以抛出此异常以中断后续处理流程。通常在 `scrapy/core/downloader` 相关模块中使用。

*来源: `scrapy/exceptions.py:74`*

---
<a id="sym-scrapy_exceptions.py-78"></a>

### `DownloadFailedError` · class
```python
class DownloadFailedError(Exception)
```

`DownloadFailedError` 是一个异常类，用于表示下载失败时抛出的错误。

该类继承自 `Exception`，没有额外定义方法，因此其行为完全由基类 `Exception` 提供。它通常在爬虫下载过程中发生错误时被抛出，以通知调用者下载操作未能成功完成。

(无方法)

*来源: `scrapy/exceptions.py:78`*

---
<a id="sym-scrapy_exceptions.py-82"></a>

### `ResponseDataLossError` · class
```python
class ResponseDataLossError(Exception)
```

`ResponseDataLossError` 类用于表示在请求响应过程中发生数据丢失的异常情况。

该类继承自 `Exception`，没有定义任何额外的方法，因此它仅作为一个异常类型存在，用于标识和抛出响应数据丢失相关的错误。

```python
class ResponseDataLossError(Exception)
```

- **职责**: 标识在 HTTP 响应处理期间发生的潜在数据丢失问题。
- **用法**: 当爬虫在处理响应时检测到数据可能丢失（例如，由于网络中断或协议错误），会抛出此异常。

*来源: `scrapy/exceptions.py:82`*

---
<a id="sym-scrapy_exceptions.py-86"></a>

### `UnsupportedURLSchemeError` · class
```python
class UnsupportedURLSchemeError(Exception)
```

`UnsupportedURLSchemeError` 异常类用于表示请求的 URL 使用了不支持的协议方案。

该异常类继承自 Python 内置的 `Exception` 类，没有定义额外的方法或属性。它通常在爬虫处理过程中遇到不被支持的 URL 协议（如 `ftp`、`mailto` 等）时抛出，以指示当前实现无法处理此类请求。

```python
class UnsupportedURLSchemeError(Exception)
```

- **职责**: 当请求的 URL 使用了 Scrapy 当前不支持的协议时，抛出此异常。
- **用法**: 一般由内部组件在检测到不支持的 URL 协议时自动抛出，开发者通常无需直接实例化该异常。

*来源: `scrapy/exceptions.py:86`*

---
<a id="sym-scrapy_exceptions.py-93"></a>

### `DropItem` · class
```python
class DropItem(Exception)
```

`DropItem` 异常类用于在数据处理流程中指示应丢弃某个项目（Item）。

### 方法

- `__init__(self, message: str, log_level: str | None = None)`
  - 初始化方法，接受一个错误信息字符串和可选的日志级别。
  - 当需要丢弃项目时抛出此异常，通常在管道（Pipeline）中使用。

*来源: `scrapy/exceptions.py:93`*

---
<a id="sym-scrapy_exceptions.py-96"></a>

### `DropItem.__init__` · method
```python
def __init__(self, message: str, log_level: str | None = None)
```

用于初始化 DropItem 异常实例，设置错误信息和日志级别。

**Parameters**
- `message`: str - 错误信息。
- `log_level`: str | None - 日志级别，可选。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exceptions.py:96`*

---
<a id="sym-scrapy_exceptions.py-101"></a>

### `NotSupported` · class
```python
class NotSupported(Exception)
```

`NotSupported` 类代表一个异常，用于表示某些功能或操作不被支持。

该类继承自 `Exception`，没有定义任何额外的方法或属性，因此它仅作为一个标记异常使用，表明某个操作或功能当前不可用或未实现。

```python
class NotSupported(Exception):
    pass
```

- **职责**: 作为异常基类，用于指示特定操作或功能不被支持。
- **用法**: 当代码遇到不支持的功能时抛出此异常，以明确告知调用者该操作无法执行。

*来源: `scrapy/exceptions.py:101`*

---
<a id="sym-scrapy_exceptions.py-108"></a>

### `UsageError` · class
```python
class UsageError(Exception)
```

`UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。

### 方法

- `__init__(self, *a: Any, **kw: Any)`  
  初始化方法，接受任意位置和关键字参数，用于创建 `UsageError` 异常实例。

*来源: `scrapy/exceptions.py:108`*

---
<a id="sym-scrapy_exceptions.py-111"></a>

### `UsageError.__init__` · method
```python
def __init__(self, *a: Any, **kw: Any)
```

UsageError.__init__ 用于初始化 UsageError 异常实例，支持控制是否打印帮助信息。

**Parameters**
- `*a`: 传递给父类构造函数的位置参数。
- `**kw`: 传递给父类构造函数的关键字参数，其中 `print_help` 用于控制是否打印帮助信息，默认为 `True`。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exceptions.py:111`*

---
<a id="sym-scrapy_exceptions.py-116"></a>

### `ScrapyDeprecationWarning` · class
```python
class ScrapyDeprecationWarning(Warning)
```

`ScrapyDeprecationWarning` 类代表 Scrapy 中用于发出弃用警告的自定义警告类，用于标记将来可能移除或更改的功能。

该类继承自 Python 内置的 `Warning` 类，没有额外的方法或属性。它通常用于在代码中发出弃用通知，提醒开发者某些功能即将被移除或更改，以便及时更新代码以避免未来的问题。

典型用法是通过 `warnings.warn()` 函数配合该类来发出警告信息，例如：

```python
import warnings
warnings.warn("此功能已被弃用", ScrapyDeprecationWarning)
```

(unknown)

*来源: `scrapy/exceptions.py:116`*

---
<a id="sym-scrapy_exceptions.py-122"></a>

### `ContractFail` · class
```python
class ContractFail(AssertionError)
```

`ContractFail` 类代表一个契约失败的异常，继承自 `AssertionError`，用于在契约检查失败时抛出。

该类没有定义任何方法，仅作为异常类型使用，通常在契约编程（contract programming）中用于表示契约条件未被满足的情况。

```python
class ContractFail(AssertionError)
```

- 继承自 `AssertionError`，用于标识契约检查失败。
- 无额外方法。

*来源: `scrapy/exceptions.py:122`*

---

## `scrapy/exporters.py`

<a id="sym-scrapy_exporters.py-39"></a>

### `BaseItemExporter` · class
```python
class BaseItemExporter(ABC)
```

`BaseItemExporter` 是一个抽象基类，用于定义数据导出器的通用接口，负责将爬取到的项（item）序列化为特定格式。

### 方法说明

- `__init__(self, *, dont_fail: bool = False, **kwargs: Any)`  
  初始化导出器实例，可选择是否在遇到错误时停止导出。

- `_configure(self, options: dict[str, Any], dont_fail: bool = False) -> None`  
  根据配置选项设置导出器的行为，通常在导出开始前调用。

- `export_item(self, item: Any) -> None`  
  导出单个项，将项数据写入输出流。

- `serialize_field(self, field: Mapping[str, Any] | Field, name: str, value: Any) -> Any`  
  序列化项中的单个字段，返回序列化后的值。

- `start_exporting(self) -> None`  
  开始导出过程，通常用于初始化输出流或准备导出环境。

- `finish_exporting(self) -> None`  
  完成导出过程，通常用于关闭输出流或清理资源。

- `_get_serialized_fields(self, item: Any, default_value: Any = None, include_empty: bool | None = None) -> Iterable[tuple[str, Any]]`  
  获取项中所有已序列化的字段，返回字段名与值的元组迭代器。

*来源: `scrapy/exporters.py:39`*

---
<a id="sym-scrapy_exporters.py-40"></a>

### `BaseItemExporter.__init__` · method
```python
def __init__(self, *, dont_fail: bool = False, **kwargs: Any)
```

初始化 BaseItemExporter 实例并配置导出选项。

**Parameters**
- `dont_fail` (bool): 如果为 True，在配置过程中遇到错误时不会抛出异常。
- `**kwargs` (Any): 传递给 `_configure` 方法的额外关键字参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter._configure`](scrapy.md#sym-scrapy_exporters.py-44) — 配置导出器以从选项字典中弹出参数。

*来源: `scrapy/exporters.py:40`*

---
<a id="sym-scrapy_exporters.py-44"></a>

### `BaseItemExporter._configure` · method
```python
def _configure(self, options: dict[str, Any], dont_fail: bool = False) -> None
```

配置导出器以从选项字典中弹出参数。

**Parameters**
- `options` (dict[str, Any]): 包含导出器配置选项的字典。
- `dont_fail` (bool): 如果为 `True`，则在遇到意外选项时不抛出异常。

**Returns**
- `None`

**Raises**
- `TypeError`: 当 `dont_fail` 为 `False` 且存在意外选项时抛出。

*来源: `scrapy/exporters.py:44`*

---
<a id="sym-scrapy_exporters.py-59"></a>

### `BaseItemExporter.export_item` · method
装饰器: `@abstractmethod`
```python
def export_item(self, item: Any) -> None
```

BaseItemExporter.export_item 用于导出单个项，但未实现具体功能。

**Parameters**
- `item` (Any): 要导出的项。

**Raises**
- `NotImplementedError`: 当前方法未被实现。

*来源: `scrapy/exporters.py:59`*

---
<a id="sym-scrapy_exporters.py-62"></a>

### `BaseItemExporter.serialize_field` · method
```python
def serialize_field(
        self, field: Mapping[str, Any] | Field, name: str, value: Any
    ) -> Any
```

序列化字段值，使用字段定义的序列化器或默认身份函数。

**Parameters**
- `field`: 字段的映射或 `Field` 对象，包含可选的 `serializer` 键。
- `name`: 字段名称。
- `value`: 要序列化的值。

**Returns**
- 序列化后的值。

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:62`*

---
<a id="sym-scrapy_exporters.py-68"></a>

### `BaseItemExporter.start_exporting` · method
```python
def start_exporting(self) -> None
```

启动项导出过程，通常用于初始化导出会话。

**Parameters**
- 无

**Returns**
- 无

**Raises**
- 无

*来源: `scrapy/exporters.py:68`*

---
<a id="sym-scrapy_exporters.py-71"></a>

### `BaseItemExporter.finish_exporting` · method
```python
def finish_exporting(self) -> None
```

结束数据导出过程，执行清理或收尾操作。

**Parameters**
- 无

**Returns**
- 无

**Raises**
- 无

*来源: `scrapy/exporters.py:71`*

---
<a id="sym-scrapy_exporters.py-74"></a>

### `BaseItemExporter._get_serialized_fields` · method
```python
def _get_serialized_fields(
        self, item: Any, default_value: Any = None, include_empty: bool | None = None
    ) -> Iterable[tuple[str, Any]]
```

返回要导出的字段及其序列化值的迭代器。

**Parameters**
- `item` (Any): 要序列化的项。
- `default_value` (Any): 当字段不存在时使用的默认值。
- `include_empty` (bool | None): 是否包含空字段。

**Returns**
- `Iterable[tuple[str, Any]]`: 包含字段名和其序列化值的元组迭代器。

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter.serialize_field`](scrapy.md#sym-scrapy_exporters.py-62) — 序列化字段值，使用字段定义的序列化器或默认身份函数。

*来源: `scrapy/exporters.py:74`*

---
<a id="sym-scrapy_exporters.py-113"></a>

### `JsonLinesItemExporter` · class
```python
class JsonLinesItemExporter(BaseItemExporter)
```

`JsonLinesItemExporter` 类用于将爬取的项（item）以 JSON Lines 格式写入文件。

### 方法

- `__init__(self, file: BytesIO, **kwargs: Any)`  
  初始化一个 `JsonLinesItemExporter` 实例，指定输出文件和可选的配置参数。

- `export_item(self, item: Any) -> None`  
  将单个项（item）以 JSON Lines 格式写入到初始化时指定的文件中。

*来源: `scrapy/exporters.py:113`*

---
<a id="sym-scrapy_exporters.py-114"></a>

### `JsonLinesItemExporter.__init__` · method
```python
def __init__(self, file: BytesIO, **kwargs: Any)
```

JsonLinesItemExporter 的构造函数，用于初始化 JSON Lines 导出器实例。

**Parameters**
- `file` (BytesIO): 用于写入导出数据的文件对象。
- `**kwargs` (Any): 传递给父类构造函数的额外关键字参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`ScrapyJSONEncoder`](scrapy_utils.md#sym-scrapy_utils_serialize.py-12)

*来源: `scrapy/exporters.py:114`*

---
<a id="sym-scrapy_exporters.py-120"></a>

### `JsonLinesItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将项以 JSON Lines 格式写入文件。

**Parameters**
- `item` (Any): 要导出的项。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/exporters.py:120`*

---
<a id="sym-scrapy_exporters.py-126"></a>

### `JsonItemExporter` · class
```python
class JsonItemExporter(BaseItemExporter)
```

`JsonItemExporter` 类用于将爬虫项（item）以 JSON 格式导出到文件中。

### 方法说明

- **`__init__(self, file: BytesIO, **kwargs: Any)`**  
  初始化 `JsonItemExporter` 实例，指定输出文件和相关配置参数。

- **`_beautify_newline(self) -> None`**  
  内部方法，用于在输出中添加美化换行。

- **`_add_comma_after_first(self) -> None`**  
  内部方法，用于在第一个项之后添加逗号，以支持 JSON 数组格式。

- **`start_exporting(self) -> None`**  
  开始导出过程，初始化输出格式。

- **`finish_exporting(self) -> None`**  
  完成导出过程，关闭或清理输出资源。

- **`export_item(self, item: Any) -> None`**  
  导出单个项，将其写入到输出文件中。

*来源: `scrapy/exporters.py:126`*

---
<a id="sym-scrapy_exporters.py-127"></a>

### `JsonItemExporter.__init__` · method
```python
def __init__(self, file: BytesIO, **kwargs: Any)
```

JsonItemExporter.__init__ 用于初始化 JSON 导出器实例，设置文件输出流和 JSON 编码参数。

**Parameters**
- `file` (BytesIO): 用于写入 JSON 数据的字节流。
- `**kwargs` (Any): 传递给基础类和 JSON 编码器的额外关键字参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`ScrapyJSONEncoder`](scrapy_utils.md#sym-scrapy_utils_serialize.py-12)

*来源: `scrapy/exporters.py:127`*

---
<a id="sym-scrapy_exporters.py-141"></a>

### `JsonItemExporter._beautify_newline` · method
```python
def _beautify_newline(self) -> None
```

将换行符写入文件以美化输出格式。

**Parameters**
- `self` - JsonItemExporter 类的实例

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:141`*

---
<a id="sym-scrapy_exporters.py-145"></a>

### `JsonItemExporter._add_comma_after_first` · method
```python
def _add_comma_after_first(self) -> None
```

用途: 在 JSON 输出中为第一个之后的项目添加逗号分隔符。

**Parameters**
- `self` - JsonItemExporter 实例

**Returns**
- `None`

**Raises**
- (unknown)

**内部调用(库内):**
- [`JsonItemExporter._beautify_newline`](scrapy.md#sym-scrapy_exporters.py-141) — 将换行符写入文件以美化输出格式。

*来源: `scrapy/exporters.py:145`*

---
<a id="sym-scrapy_exporters.py-152"></a>

### `JsonItemExporter.start_exporting` · method
```python
def start_exporting(self) -> None
```

开始导出 JSON 格式的数据，写入起始的 JSON 数组符号。

**Parameters**
- 无

**Returns**
- 无

**Raises**
- 无

**内部调用(库内):**
- [`JsonItemExporter._beautify_newline`](scrapy.md#sym-scrapy_exporters.py-141) — 将换行符写入文件以美化输出格式。

*来源: `scrapy/exporters.py:152`*

---
<a id="sym-scrapy_exporters.py-156"></a>

### `JsonItemExporter.finish_exporting` · method
```python
def finish_exporting(self) -> None
```

结束 JSON 导出，写入结束括号。

**Parameters**
- 无

**Returns**
- 无

**Raises**
- 无

**内部调用(库内):**
- [`JsonItemExporter._beautify_newline`](scrapy.md#sym-scrapy_exporters.py-141) — 将换行符写入文件以美化输出格式。

*来源: `scrapy/exporters.py:156`*

---
<a id="sym-scrapy_exporters.py-160"></a>

### `JsonItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将项目导出为 JSON 格式数据。

**Parameters**
- `item`: 要导出的项目对象。

**Returns**
- `None`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`JsonItemExporter._add_comma_after_first`](scrapy.md#sym-scrapy_exporters.py-145) — 用途: 在 JSON 输出中为第一个之后的项目添加逗号分隔符。

*来源: `scrapy/exporters.py:160`*

---
<a id="sym-scrapy_exporters.py-167"></a>

### `XmlItemExporter` · class
```python
class XmlItemExporter(BaseItemExporter)
```

XmlItemExporter 类用于将爬取的项（item）以 XML 格式导出到文件中。

### 关键方法

- `__init__(self, file: BytesIO, **kwargs: Any)`  
  初始化 XmlItemExporter 实例，指定输出文件。

- `_beautify_newline(self, new_item: bool = False) -> None`  
  在 XML 输出中处理换行符，用于美化格式。

- `_beautify_indent(self, depth: int = 1) -> None`  
  根据缩进层级调整 XML 输出的缩进。

- `start_exporting(self) -> None`  
  开始导出过程，初始化 XML 根元素。

- `export_item(self, item: Any) -> None`  
  导出单个项，将其转换为 XML 格式并写入文件。

- `finish_exporting(self) -> None`  
  完成导出过程，关闭 XML 文档。

- `_export_xml_field(self, name: str, serialized_value: Any, depth: int) -> None`  
  将项的字段序列化为 XML 格式，并写入输出文件。

*来源: `scrapy/exporters.py:167`*

---
<a id="sym-scrapy_exporters.py-168"></a>

### `XmlItemExporter.__init__` · method
```python
def __init__(self, file: BytesIO, **kwargs: Any)
```

XmlItemExporter 用于将项目导出为 XML 格式。

**Parameters**
- `file` (BytesIO): 用于写入 XML 数据的文件对象。
- `**kwargs` (Any): 其他传递给基类的关键词参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:168`*

---
<a id="sym-scrapy_exporters.py-176"></a>

### `XmlItemExporter._beautify_newline` · method
```python
def _beautify_newline(self, new_item: bool = False) -> None
```

XmlItemExporter._beautify_newline 方法用于在 XML 输出中根据缩进设置和参数控制添加换行符。

**Parameters**
- `new_item` (bool): 指示是否为新项目，用于决定是否添加换行符。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:176`*

---
<a id="sym-scrapy_exporters.py-180"></a>

### `XmlItemExporter._beautify_indent` · method
```python
def _beautify_indent(self, depth: int = 1) -> None
```

设置缩进以美化 XML 输出。

**Parameters**
- `depth` (int): 缩进的深度，默认为 1。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:180`*

---
<a id="sym-scrapy_exporters.py-184"></a>

### `XmlItemExporter.start_exporting` · method
```python
def start_exporting(self) -> None
```

XmlItemExporter.start_exporting 方法用于启动 XML 导出过程，初始化 XML 文档结构。

**Parameters**
- 无

**Returns**
- `None`

**Raises**
- 无

**内部调用(库内):**
- [`XmlItemExporter._beautify_newline`](scrapy.md#sym-scrapy_exporters.py-176) — XmlItemExporter._beautify_newline 方法用于在 XML 输出中根据缩进设置和参数控制添加换行符。

*来源: `scrapy/exporters.py:184`*

---
<a id="sym-scrapy_exporters.py-189"></a>

### `XmlItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将项导出为 XML 格式。

**Parameters**
- `item` (Any): 要导出的项。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

**内部调用(库内):**
- [`XmlItemExporter._beautify_indent`](scrapy.md#sym-scrapy_exporters.py-180) — 设置缩进以美化 XML 输出。
- [`XmlItemExporter._beautify_newline`](scrapy.md#sym-scrapy_exporters.py-176) — XmlItemExporter._beautify_newline 方法用于在 XML 输出中根据缩进设置和参数控制添加换行符。
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。
- [`XmlItemExporter._export_xml_field`](scrapy.md#sym-scrapy_exporters.py-203) — 递归导出 XML 字段并处理嵌套结构和列表。

*来源: `scrapy/exporters.py:189`*

---
<a id="sym-scrapy_exporters.py-199"></a>

### `XmlItemExporter.finish_exporting` · method
```python
def finish_exporting(self) -> None
```

结束 XML 导出过程，关闭根元素和文档。

**Parameters**
- 无

**Returns**
- 无

**Raises**
- 无

*来源: `scrapy/exporters.py:199`*

---
<a id="sym-scrapy_exporters.py-203"></a>

### `XmlItemExporter._export_xml_field` · method
```python
def _export_xml_field(self, name: str, serialized_value: Any, depth: int) -> None
```

递归导出 XML 字段并处理嵌套结构和列表。

**Parameters**
- `name` (str): 字段名称
- `serialized_value` (Any): 序列化后的字段值
- `depth` (int): 当前缩进层级

**Returns**
- (None): 无返回值

**Raises**
- (unknown)

**内部调用(库内):**
- [`XmlItemExporter._beautify_indent`](scrapy.md#sym-scrapy_exporters.py-180) — 设置缩进以美化 XML 输出。
- [`XmlItemExporter._beautify_newline`](scrapy.md#sym-scrapy_exporters.py-176) — XmlItemExporter._beautify_newline 方法用于在 XML 输出中根据缩进设置和参数控制添加换行符。
- [`is_listlike`](scrapy_utils.md#sym-scrapy_utils_python.py-35)

*来源: `scrapy/exporters.py:203`*

---
<a id="sym-scrapy_exporters.py-224"></a>

### `CsvItemExporter` · class
```python
class CsvItemExporter(BaseItemExporter)
```

`CsvItemExporter` 类用于将爬取项（Item）以 CSV 格式导出到文件中。

### 方法说明

- `__init__(self, file: BytesIO, include_headers_line: bool = True, join_multivalued: str = ",", errors: str | None = None, **kwargs: Any)`  
  初始化一个 `CsvItemExporter` 实例，指定输出文件、是否包含表头、多值字段的连接符等参数。

- `serialize_field(self, field: Mapping[str, Any] | Field, name: str, value: Any) -> Any`  
  序列化单个字段的值，用于转换字段内容以适应 CSV 格式。

- `_join_if_needed(self, value: Any) -> Any`  
  如果字段值是列表或可迭代对象，根据配置的连接符将其连接成字符串。

- `export_item(self, item: Any) -> None`  
  将单个项写入输出文件。

- `finish_exporting(self) -> None`  
  完成导出过程，通常用于执行清理操作。

- `_build_row(self, values: Iterable[Any]) -> Iterable[Any]`  
  构建一行数据，将字段值转换为适合 CSV 格式的列表。

- `_write_headers_and_set_fields_to_export(self, item: Any) -> None`  
  写入表头并设置待导出的字段列表，仅在首次调用时执行。

*来源: `scrapy/exporters.py:224`*

---
<a id="sym-scrapy_exporters.py-225"></a>

### `CsvItemExporter.__init__` · method
```python
def __init__(
        self,
        file: BytesIO,
        include_headers_line: bool = True,
        join_multivalued: str = ",",
        errors: str | None = None,
        **kwargs: Any,
    )
```

初始化 `CsvItemExporter` 实例，设置文件输出流、编码、是否包含表头行及多值连接符等参数。

**Parameters**
- `file` (BytesIO): 用于写入 CSV 数据的文件对象。
- `include_headers_line` (bool): 是否在输出中包含表头行，默认为 `True`。
- `join_multivalued` (str): 多值字段的连接符，默认为 `","`。
- `errors` (str | None): 编码错误处理方式，默认为 `None`。
- `**kwargs` (Any): 其他传递给基类的参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:225`*

---
<a id="sym-scrapy_exporters.py-249"></a>

### `CsvItemExporter.serialize_field` · method
```python
def serialize_field(
        self, field: Mapping[str, Any] | Field, name: str, value: Any
    ) -> Any
```

将字段值序列化为适合导出的格式。

**Parameters**
- `field`: 字段的映射或 Field 对象，包含序列化信息。
- `name`: 字段名称。
- `value`: 要序列化的字段值。

**Returns**
- 序列化后的字段值。

*来源: `scrapy/exporters.py:249`*

---
<a id="sym-scrapy_exporters.py-255"></a>

### `CsvItemExporter._join_if_needed` · method
```python
def _join_if_needed(self, value: Any) -> Any
```

将多值列表或元组连接为单个字符串，若无法连接则返回原值。

**Parameters**
- `value` (Any): 要处理的值，若为列表或元组则尝试连接。

**Returns**
- `Any`: 连接后的字符串或原始值。

**Raises**
- `(unknown)`

*来源: `scrapy/exporters.py:255`*

---
<a id="sym-scrapy_exporters.py-263"></a>

### `CsvItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将单个 Item 以 CSV 格式写入输出流。

**Parameters**
- `item` (Any): 要导出的 Item 对象。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

**内部调用(库内):**
- [`CsvItemExporter._write_headers_and_set_fields_to_export`](scrapy.md#sym-scrapy_exporters.py-282) — 写入 CSV 头部行并设置要导出的字段。
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。
- [`CsvItemExporter._build_row`](scrapy.md#sym-scrapy_exporters.py-275) — 将值序列转换为指定编码的 Unicode 字符串序列。

*来源: `scrapy/exporters.py:263`*

---
<a id="sym-scrapy_exporters.py-272"></a>

### `CsvItemExporter.finish_exporting` · method
```python
def finish_exporting(self) -> None
```

结束数据导出过程，分离流以避免关闭包装的文件。

**Parameters**
- 无

**Returns**
- 无

**Raises**
- 无

*来源: `scrapy/exporters.py:272`*

---
<a id="sym-scrapy_exporters.py-275"></a>

### `CsvItemExporter._build_row` · method
```python
def _build_row(self, values: Iterable[Any]) -> Iterable[Any]
```

将值序列转换为指定编码的 Unicode 字符串序列。

**Parameters**

- `values` – 要转换的值序列。

**Returns**

- 转换后的值序列。

**Raises**

- `(unknown)`

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/exporters.py:275`*

---
<a id="sym-scrapy_exporters.py-282"></a>

### `CsvItemExporter._write_headers_and_set_fields_to_export` · method
```python
def _write_headers_and_set_fields_to_export(self, item: Any) -> None
```

写入 CSV 头部行并设置要导出的字段。

**Parameters**
- `item`: 要从中提取字段名的项。

**Returns**
- `(unknown)`

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`CsvItemExporter._build_row`](scrapy.md#sym-scrapy_exporters.py-275) — 将值序列转换为指定编码的 Unicode 字符串序列。

*来源: `scrapy/exporters.py:282`*

---
<a id="sym-scrapy_exporters.py-297"></a>

### `PickleItemExporter` · class
```python
class PickleItemExporter(BaseItemExporter)
```

PickleItemExporter 类用于将爬取项以 Python 的 pickle 格式序列化并写入文件。

### 方法

- `__init__(self, file: BytesIO, protocol: int = 4, **kwargs: Any)`  
  初始化一个 `PickleItemExporter` 实例，指定输出文件和 pickle 协议版本。

- `export_item(self, item: Any) -> None`  
  将单个爬取项序列化并写入到初始化时指定的文件中。

*来源: `scrapy/exporters.py:297`*

---
<a id="sym-scrapy_exporters.py-298"></a>

### `PickleItemExporter.__init__` · method
```python
def __init__(self, file: BytesIO, protocol: int = 4, **kwargs: Any)
```

PickleItemExporter 的构造函数，用于初始化文件和协议版本。

**Parameters**
- `file` (BytesIO): 用于写入序列化数据的字节流。
- `protocol` (int): Python 对象序列化协议版本，默认为 4。
- `**kwargs` (Any): 其他传递给父类构造函数的参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:298`*

---
<a id="sym-scrapy_exporters.py-303"></a>

### `PickleItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将项以 pickle 格式写入文件。

**Parameters**
- `item` (Any): 要导出的项。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。

*来源: `scrapy/exporters.py:303`*

---
<a id="sym-scrapy_exporters.py-308"></a>

### `MarshalItemExporter` · class
```python
class MarshalItemExporter(BaseItemExporter)
```

`MarshalItemExporter` 类用于将数据项以 Python 的 `marshal` 模块支持的格式序列化并导出到文件中。

### 方法

- **`__init__(self, file: BytesIO, **kwargs: Any)`**  
  初始化导出器实例，指定用于写入序列化数据的文件对象。

- **`export_item(self, item: Any) -> None`**  
  将单个数据项序列化并写入到初始化时指定的文件中。

*来源: `scrapy/exporters.py:308`*

---
<a id="sym-scrapy_exporters.py-317"></a>

### `MarshalItemExporter.__init__` · method
```python
def __init__(self, file: BytesIO, **kwargs: Any)
```

MarshalItemExporter.__init__ 用于初始化一个用于导出项到二进制流的导出器实例。

**Parameters**
- `file` (BytesIO): 用于写入导出数据的二进制流。
- `**kwargs` (Any): 传递给父类构造函数的额外关键字参数。

**Returns**
(unknown)

**Raises**
(unknown)

*来源: `scrapy/exporters.py:317`*

---
<a id="sym-scrapy_exporters.py-321"></a>

### `MarshalItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将项导出为 marshal 格式到文件。

**Parameters**
- `item` (Any): 要导出的项。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。

*来源: `scrapy/exporters.py:321`*

---
<a id="sym-scrapy_exporters.py-325"></a>

### `PprintItemExporter` · class
```python
class PprintItemExporter(BaseItemExporter)
```

`PprintItemExporter` 类用于将项目以格式化的方式导出到文件中，通常用于调试或日志记录。

### 方法

- `__init__(self, file: BytesIO, **kwargs: Any)`  
  初始化一个 `PprintItemExporter` 实例，指定输出文件和可选的配置参数。

- `export_item(self, item: Any) -> None`  
  将单个项目导出到初始化时指定的文件中。

*来源: `scrapy/exporters.py:325`*

---
<a id="sym-scrapy_exporters.py-326"></a>

### `PprintItemExporter.__init__` · method
```python
def __init__(self, file: BytesIO, **kwargs: Any)
```

PprintItemExporter 的初始化方法，用于设置输出文件和额外的关键字参数。

**Parameters**
- `file` (BytesIO): 用于输出的字节流对象。
- `**kwargs` (Any): 其他传递给父类构造函数的参数。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:326`*

---
<a id="sym-scrapy_exporters.py-330"></a>

### `PprintItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> None
```

将项以格式化的形式写入文件。

**Parameters**
- `item` (Any): 要导出的项。

**Returns**
- (None): 无返回值。

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)

*来源: `scrapy/exporters.py:330`*

---
<a id="sym-scrapy_exporters.py-335"></a>

### `PythonItemExporter` · class
```python
class PythonItemExporter(BaseItemExporter)
```

PythonItemExporter 是一个用于将爬虫项（Item）序列化为 Python 原生数据结构的导出器。

### 方法说明

- `export_item(self, item: Any) -> dict[str | bytes, Any]`  
  将单个项导出为字典格式，返回项的键值对序列化结果。

- `serialize_field(self, field: Mapping[str, Any] | Field, name: str, value: Any) -> Any`  
  序列化项中的单个字段，返回该字段的序列化值。

- `_serialize_value(self, value: Any) -> Any`  
  内部方法，用于序列化字段值，处理复杂数据类型。

- `_serialize_item(self, item: Any) -> Iterable[tuple[str | bytes, Any]]`  
  内部方法，将项序列化为键值对的迭代器。

- `_configure(self, options: dict[str, Any], dont_fail: bool = False) -> None`  
  配置导出器的选项，若 `dont_fail` 为 True，则在配置失败时不抛出异常。

*来源: `scrapy/exporters.py:335`*

---
<a id="sym-scrapy_exporters.py-345"></a>

### `PythonItemExporter._configure` · method
```python
def _configure(self, options: dict[str, Any], dont_fail: bool = False) -> None
```

配置 `PythonItemExporter` 的导出选项，并设置默认编码为 `utf-8`。

**Parameters**
- `options` (dict[str, Any]): 导出选项字典。
- `dont_fail` (bool): 配置失败时是否抛出异常，默认为 `False`。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `scrapy/exporters.py:345`*

---
<a id="sym-scrapy_exporters.py-350"></a>

### `PythonItemExporter.serialize_field` · method
```python
def serialize_field(
        self, field: Mapping[str, Any] | Field, name: str, value: Any
    ) -> Any
```

将字段值序列化为适当的格式。

**Parameters**
- `field`: 字段的映射或 Field 对象，包含序列化信息。
- `name`: 字段名称。
- `value`: 要序列化的字段值。

**Returns**
- 序列化后的字段值。

*来源: `scrapy/exporters.py:350`*

---
<a id="sym-scrapy_exporters.py-358"></a>

### `PythonItemExporter._serialize_value` · method
```python
def _serialize_value(self, value: Any) -> Any
```

序列化项值，处理 Item、字符串、列表等类型的值。

**Parameters**

- `value` (Any): 待序列化的值。

**Returns**

- `Any`: 序列化后的值。

**内部调用(库内):**
- [`PythonItemExporter.export_item`](scrapy.md#sym-scrapy_exporters.py-373) — 将项目序列化为字典格式。
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)
- [`PythonItemExporter._serialize_item`](scrapy.md#sym-scrapy_exporters.py-369) — 序列化项的键值对，递归处理值。
- [`is_listlike`](scrapy_utils.md#sym-scrapy_utils_python.py-35)

*来源: `scrapy/exporters.py:358`*

---
<a id="sym-scrapy_exporters.py-369"></a>

### `PythonItemExporter._serialize_item` · method
```python
def _serialize_item(self, item: Any) -> Iterable[tuple[str | bytes, Any]]
```

序列化项的键值对，递归处理值。

**Parameters**
- `item`: 要序列化的项。

**Returns**
- 键值对的迭代器，其中键是字符串或字节，值是序列化后的值。

**内部调用(库内):**
- [`PythonItemExporter._serialize_value`](scrapy.md#sym-scrapy_exporters.py-358) — 序列化项值，处理 Item、字符串、列表等类型的值。

*来源: `scrapy/exporters.py:369`*

---
<a id="sym-scrapy_exporters.py-373"></a>

### `PythonItemExporter.export_item` · method
```python
def export_item(self, item: Any) -> dict[str | bytes, Any]
```

将项目序列化为字典格式。

**Parameters**
- `item`: 要序列化的项目对象。

**Returns**
- `dict[str | bytes, Any]`: 序列化后的键值对字典。

**Raises**
- (unknown)

**内部调用(库内):**
- [`BaseItemExporter._get_serialized_fields`](scrapy.md#sym-scrapy_exporters.py-74) — 返回要导出的字段及其序列化值的迭代器。

*来源: `scrapy/exporters.py:373`*

---

## `scrapy/extension.py`

<a id="sym-scrapy_extension.py-18"></a>

### `ExtensionManager` · class
```python
class ExtensionManager(MiddlewareManager)
```

ExtensionManager 是 Scrapy 中用于管理扩展（Extensions）的类，负责加载、初始化和协调各个扩展的生命周期。

### 方法

- **_get_mwlist_from_settings(cls, settings: Settings) -> list[Any]**  
  从设置中获取扩展列表。该方法根据配置的设置来确定应加载哪些扩展，并返回一个包含扩展实例的列表。  
  `scrapy/extensions/__init__.py:25`

*来源: `scrapy/extension.py:18`*

---
<a id="sym-scrapy_extension.py-22"></a>

### `ExtensionManager._get_mwlist_from_settings` · method
装饰器: `@classmethod`
```python
def _get_mwlist_from_settings(cls, settings: Settings) -> list[Any]
```

从设置中获取扩展组件列表。

**Parameters**
- `settings`: 配置设置对象

**Returns**
- 扩展组件优先级字典转换后的列表

**Raises**
- (unknown)

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`BaseSettings.get_component_priority_dict_with_base`](scrapy_settings.md#sym-scrapy_settings___init__.py-338)

*来源: `scrapy/extension.py:22`*

---

## `scrapy/interfaces.py`

<a id="sym-scrapy_interfaces.py-6"></a>

### `ISpiderLoader` · class
```python
class ISpiderLoader(Interface)
```

`ISpiderLoader` 是一个接口，用于定义爬虫加载器的行为，负责从配置、名称、请求等不同来源加载和管理爬虫实例。

### 方法说明

- **`from_settings(settings)`**  
  根据给定的设置创建一个 `ISpiderLoader` 实例。  
  `文件:scrapy/spiderloader.py:20`

- **`load(spider_name)`**  
  根据爬虫名称加载并返回一个爬虫实例。  
  `文件:scrapy/spiderloader.py:20`

- **`list()`**  
  返回所有可用爬虫的名称列表。  
  `文件:scrapy/spiderloader.py:20`

- **`find_by_request(request)`**  
  根据请求查找并返回匹配的爬虫类。  
  `文件:scrapy/spiderloader.py:20`

*来源: `scrapy/interfaces.py:6`*

---
<a id="sym-scrapy_interfaces.py-7"></a>

### `ISpiderLoader.from_settings` · method
```python
def from_settings(settings)
```

根据提供的代码，为 `ISpiderLoader.from_settings` 方法生成 API 文档。

---

**根据给定的 settings 返回一个类的实例**

**Parameters**
- `settings` (Settings): 配置设置对象

**Returns**
- `ISpiderLoader` 的实例

**Raises**
- (unknown)

*来源: `scrapy/interfaces.py:7`*

---
<a id="sym-scrapy_interfaces.py-10"></a>

### `ISpiderLoader.load` · method
```python
def load(spider_name)
```

根据提供的 `scrapy/spiderloader.py` 文件中的 `SpiderLoader` 类的 `load` 方法，以下是其 API 文档：

---

**用途**: 根据给定的爬虫名称返回对应的 Spider 类。

**Parameters**:
- `spider_name` (str): 爬虫的名称。

**Returns**:
- `Spider`: 与指定名称对应的 Spider 类。

**Raises**:
- `KeyError`: 如果未找到指定名称的爬虫。

---

*来源: `scrapy/interfaces.py:10`*

---
<a id="sym-scrapy_interfaces.py-14"></a>

### `ISpiderLoader.list` · method
```python
def list()
```

返回项目中所有蜘蛛的名称列表。

**Parameters**
- 无

**Returns**
- `list`: 蜘蛛名称列表

**Raises**
- 无

*来源: `scrapy/interfaces.py:14`*

---
<a id="sym-scrapy_interfaces.py-18"></a>

### `ISpiderLoader.find_by_request` · method
```python
def find_by_request(request)
```

根据提供的代码，为 `ISpiderLoader.find_by_request` 方法生成 API 文档。

---

根据提供的代码，为 `ISpiderLoader.find_by_request` 方法生成 API 文档。

---

**用途**: 返回能够处理给定请求的爬虫名称列表。

**Parameters**:
- `request`: 要查找可处理该请求的爬虫的请求对象。

**Returns**:
- `list`: 包含能够处理该请求的爬虫名称的列表。

**Raises**:
- (unknown)

*来源: `scrapy/interfaces.py:18`*

---

## `scrapy/item.py`

<a id="sym-scrapy_item.py-24"></a>

### `Field` · class
```python
class Field(dict[str, Any])
```

Field 类用于定义和存储爬虫数据项（Item）中的字段信息，它继承自字典类型，允许以键值对的形式存储字段的元数据。

该类没有定义任何方法，其行为完全依赖于其父类 dict 的功能，通常用于在 Item 类中作为字段的占位符或配置容器。

*来源: `scrapy/item.py:24`*

---
<a id="sym-scrapy_item.py-28"></a>

### `ItemMeta` · class
```python
class ItemMeta(ABCMeta)
```

`ItemMeta` 是一个元类，用于定义 `Item` 类的创建行为，负责处理 `Item` 子类的构建与属性注册。

### 方法

- **`__new__(mcs, class_name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> ItemMeta`**  
  创建一个新的 `Item` 类。该方法在类创建时被调用，用于设置类的属性和行为，包括处理字段定义、继承关系等。  
  文件: `scrapy/item.py:line`

*来源: `scrapy/item.py:28`*

---
<a id="sym-scrapy_item.py-34"></a>

### `ItemMeta.__new__` · method
```python
def __new__(
        mcs, class_name: str, bases: tuple[type, ...], attrs: dict[str, Any]
    ) -> ItemMeta
```

创建一个新的 ItemMeta 类型，用于定义数据项结构。

**Parameters**
- `mcs`: 元类本身
- `class_name`: 要创建的类名
- `bases`: 基类元组
- `attrs`: 类属性字典

**Returns**
- `ItemMeta`: 新创建的元类实例

**Raises**
- (unknown)

*来源: `scrapy/item.py:34`*

---
<a id="sym-scrapy_item.py-57"></a>

### `Item` · class
```python
class Item(MutableMapping[str, Any], object_ref, metaclass=ItemMeta)
```

`Item` 类代表一个可变的键值映射结构，用于存储和管理爬取数据的字段与值，是 Scrapy 中定义数据结构的核心类。

### 方法说明

- `__init__(self, *args: Any, **kwargs: Any)`  
  初始化一个 `Item` 实例，支持传入关键字参数或位置参数来设置初始字段。

- `__getitem__(self, key: str) -> Any`  
  获取指定字段的值，如果字段不存在则抛出 `KeyError`。

- `__setitem__(self, key: str, value: Any) -> None`  
  设置指定字段的值。

- `__delitem__(self, key: str) -> None`  
  删除指定字段。

- `__getattr__(self, name: str) -> NoReturn`  
  当访问不存在的属性时抛出异常，防止意外访问。

- `__setattr__(self, name: str, value: Any) -> None`  
  设置对象属性，用于控制字段的赋值行为。

- `__len__(self) -> int`  
  返回 `Item` 中字段的数量。

- `__iter__(self) -> Iterator[str]`  
  返回字段名的迭代器。

- `keys(self) -> KeysView[str]`  
  返回字段名的视图对象。

- `__repr__(self) -> str`  
  返回该 `Item` 的字符串表示形式，通常用于调试。

- `copy(self) -> Self

*来源: `scrapy/item.py:57`*

---
<a id="sym-scrapy_item.py-85"></a>

### `Item.__init__` · method
```python
def __init__(self, *args: Any, **kwargs: Any)
```

初始化 Item 实例并设置其值。

**Parameters**
- `*args: Any` - 位置参数，用于初始化项的值。
- `**kwargs: Any` - 关键字参数，用于初始化项的值。

**Returns**
- `None`

**Raises**
- (unknown)

*来源: `scrapy/item.py:85`*

---
<a id="sym-scrapy_item.py-91"></a>

### `Item.__getitem__` · method
```python
def __getitem__(self, key: str) -> Any
```

获取项目中指定键的值。

**Parameters**
- `key` (str): 要获取的值的键名。

**Returns**
- `Any`: 与键关联的值。

*来源: `scrapy/item.py:91`*

---
<a id="sym-scrapy_item.py-94"></a>

### `Item.__setitem__` · method
```python
def __setitem__(self, key: str, value: Any) -> None
```

设置项目中指定键的值，若键不存在于字段定义中则抛出异常。

**Parameters**
- `key` (str): 要设置的字段名
- `value` (Any): 要设置的值

**Raises**
- `KeyError`: 当字段名不在预定义字段中时抛出

*来源: `scrapy/item.py:94`*

---
<a id="sym-scrapy_item.py-100"></a>

### `Item.__delitem__` · method
```python
def __delitem__(self, key: str) -> None
```

删除 Item 中指定键的值。

**Parameters**
- `key`: 要删除的键，类型为 `str`。

**Returns**
- `None`

**Raises**
- `(unknown)`

*来源: `scrapy/item.py:100`*

---
<a id="sym-scrapy_item.py-103"></a>

### `Item.__getattr__` · method
```python
def __getattr__(self, name: str) -> NoReturn
```

当访问不存在的字段时，抛出异常提示使用 `item[field]` 形式访问。

**Parameters**
- `name`: str - 要访问的字段名称

**Raises**
- `AttributeError` - 当字段不存在时抛出异常，若字段存在于 `self.fields` 中，则提示使用 `item[field]` 形式访问；否则直接抛出字段名称对应的异常。

*来源: `scrapy/item.py:103`*

---
<a id="sym-scrapy_item.py-108"></a>

### `Item.__setattr__` · method
```python
def __setattr__(self, name: str, value: Any) -> None
```

设置项目字段时应使用 `item[field] = value` 语法，而非直接赋值属性。

**Parameters**
- `name`: str - 属性名称
- `value`: Any - 属性值

**Raises**
- `AttributeError` - 当尝试设置非下划线开头的属性时抛出，提示使用 `item[field] = value` 语法。

*来源: `scrapy/item.py:108`*

---
<a id="sym-scrapy_item.py-113"></a>

### `Item.__len__` · method
```python
def __len__(self) -> int
```

计算并返回 Item 中值的数量。

**Returns**
- `int`: Item 中 `_values` 的长度。

*来源: `scrapy/item.py:113`*

---
<a id="sym-scrapy_item.py-116"></a>

### `Item.__iter__` · method
```python
def __iter__(self) -> Iterator[str]
```

返回 Item 中所有值的迭代器。

**Returns**
- `Iterator[str]`: 包含 Item 所有值的迭代器。

*来源: `scrapy/item.py:116`*

---
<a id="sym-scrapy_item.py-121"></a>

### `Item.keys` · method
```python
def keys(self) -> KeysView[str]
```

返回 Item 中所有键的视图。

**Returns**
  - `KeysView[str]`: 包含所有键的视图对象。

*来源: `scrapy/item.py:121`*

---
<a id="sym-scrapy_item.py-124"></a>

### `Item.__repr__` · method
```python
def __repr__(self) -> str
```

用于返回 Item 对象的字符串表示，便于调试和日志记录。

**Parameters**

- `self` - Item 实例

**Returns**

- `str` - 格式化后的字典形式字符串表示

**Raises**

- (unknown)

**内部调用(库内):**
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)

*来源: `scrapy/item.py:124`*

---
<a id="sym-scrapy_item.py-127"></a>

### `Item.copy` · method
```python
def copy(self) -> Self
```

创建当前 Item 的一个浅层副本。

**Returns**
  - `Self`: 当前 Item 类型的一个新实例，其数据与原实例相同。

*来源: `scrapy/item.py:127`*

---
<a id="sym-scrapy_item.py-130"></a>

### `Item.deepcopy` · method
```python
def deepcopy(self) -> Self
```

返回此 item 的深拷贝。

**Returns**
  - `Self`: 此 item 的深拷贝对象。

*来源: `scrapy/item.py:130`*

---

## `scrapy/link.py`

<a id="sym-scrapy_link.py-9"></a>

### `Link` · class
```python
class Link
```

`Link` 类用于表示一个链接，包含 URL、文本、片段和是否nofollow等属性。

### 方法

- `__init__(self, url: str, text: str = "", fragment: str = "", nofollow: bool = False)`  
  初始化一个 Link 实例，需要提供 URL，其他参数为可选。

- `__eq__(self, other: object) -> bool`  
  比较两个 Link 实例是否相等。

- `__hash__(self) -> int`  
  返回 Link 实例的哈希值，使其可以作为字典的键或存入集合。

- `__repr__(self) -> str`  
  返回 Link 实例的字符串表示形式，用于调试和日志输出。

*来源: `scrapy/link.py:9`*

---
<a id="sym-scrapy_link.py-29"></a>

### `Link.__init__` · method
```python
def __init__(
        self, url: str, text: str = "", fragment: str = "", nofollow: bool = False
    )
```

初始化一个 Link 对象，用于表示链接信息。

**Parameters**
- `url: str` - 链接的 URL 地址。
- `text: str` - 链接的文本内容，默认为空字符串。
- `fragment: str` - 链接的片段标识符，默认为空字符串。
- `nofollow: bool` - 是否设置为 nofollow 属性，默认为 False。

**Raises**
- `TypeError` - 如果 url 不是字符串类型。

*来源: `scrapy/link.py:29`*

---
<a id="sym-scrapy_link.py-40"></a>

### `Link.__eq__` · method
```python
def __eq__(self, other: object) -> bool
```

比较两个 Link 对象是否相等。

**Parameters**
- `other` (object): 另一个要比较的 Link 对象。

**Returns**
- `bool`: 如果两个 Link 对象的 url、text、fragment 和 nofollow 属性都相等，则返回 True；否则返回 False。如果 other 不是 Link 类型，则返回 NotImplemented。

**Raises**
- (unknown)

*来源: `scrapy/link.py:40`*

---
<a id="sym-scrapy_link.py-50"></a>

### `Link.__hash__` · method
```python
def __hash__(self) -> int
```

计算 Link 对象的哈希值，用于唯一标识该对象。

**Returns**
- `int`: 返回 Link 对象的哈希值。

*来源: `scrapy/link.py:50`*

---
<a id="sym-scrapy_link.py-55"></a>

### `Link.__repr__` · method
```python
def __repr__(self) -> str
```

用于返回 Link 对象的字符串表示形式，便于调试和日志记录。

**Returns**
- `str`: 包含链接 URL、文本、片段和 nofollow 属性的字符串表示。

*来源: `scrapy/link.py:55`*

---

## `scrapy/logformatter.py`

<a id="sym-scrapy_logformatter.py-31"></a>

### `LogFormatterResult` · class
```python
class LogFormatterResult(TypedDict)
```

`LogFormatterResult` 类型用于定义日志格式化结果的结构，通常在日志记录过程中用于描述日志条目的格式化内容。

该类型继承自 `TypedDict`，因此它是一个类型提示结构，用于描述一个字典对象的键和值的类型。它不包含任何方法，仅用于类型检查和代码提示，以确保日志格式化函数返回的结构符合预期。在 Scrapy 中，它可能被用于定义日志记录器返回的格式化结果，以便在日志处理流程中保持一致的结构。

由于该类没有方法，因此无需进一步说明其典型用法。

*来源: `scrapy/logformatter.py:31`*

---
<a id="sym-scrapy_logformatter.py-37"></a>

### `LogFormatter` · class
```python
class LogFormatter
```

`LogFormatter` 类用于定义爬虫过程中各类日志事件的格式化方式。

### 方法说明

- **crawled**
  - 签名: `crawled(self, request: Request, response: Response, spider: Spider) -> LogFormatterResult`
  - 说明: 当成功抓取一个请求时调用，用于格式化该事件的日志。

- **scraped**
  - 签名: `scraped(self, item: Any, response: Response | Failure | None, spider: Spider) -> LogFormatterResult`
  - 说明: 当成功抓取并处理一个数据项时调用，用于格式化该事件的日志。

- **dropped**
  - 签名: `dropped(self, item: Any, exception: BaseException, response: Response | Failure | None, spider: Spider) -> LogFormatterResult`
  - 说明: 当一个数据项被丢弃时调用，用于格式化该事件的日志。

- **item_error**
  - 签名: `item_error(self, item: Any, exception: BaseException, response: Response | Failure | None, spider: Spider) -> LogFormatterResult`
  - 说明: 当处理数据项时发生错误时调用，用于格式化该事件的日志。

- **spider_error**
  - 签名: `spider_error(self, failure: Failure, request: Request, response: Response | Failure, spider: Spider) ->

*来源: `scrapy/logformatter.py:37`*

---
<a id="sym-scrapy_logformatter.py-75"></a>

### `LogFormatter.crawled` · method
```python
def crawled(
        self, request: Request, response: Response, spider: Spider
    ) -> LogFormatterResult
```

记录爬取网页时的日志信息。

**Parameters**
- `request` (Request): 发送的请求对象。
- `response` (Response): 响应对象。
- `spider` (Spider): 爬虫实例。

**Returns**
- `LogFormatterResult`: 包含日志级别、消息和参数的字典，用于记录爬取日志。

**Raises**
- (unknown)

**内部调用(库内):**
- [`referer_str`](scrapy_utils.md#sym-scrapy_utils_request.py-150)

*来源: `scrapy/logformatter.py:75`*

---
<a id="sym-scrapy_logformatter.py-95"></a>

### `LogFormatter.scraped` · method
```python
def scraped(
        self, item: Any, response: Response | Failure | None, spider: Spider
    ) -> LogFormatterResult
```

记录爬虫抓取到项时的日志消息。

**Parameters**
- `item` (Any): 被抓取的项。
- `response` (Response | Failure | None): 相应对象、失败对象或 None。
- `spider` (Spider): 触发此操作的爬虫实例。

**Returns**
- `LogFormatterResult`: 包含日志级别、消息和参数的字典。

**Raises**
- (unknown)

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/logformatter.py:95`*

---
<a id="sym-scrapy_logformatter.py-115"></a>

### `LogFormatter.dropped` · method
```python
def dropped(
        self,
        item: Any,
        exception: BaseException,
        response: Response | Failure | None,
        spider: Spider,
    ) -> LogFormatterResult
```

记录项目在通过项目管道时被丢弃的日志消息。

**Parameters**
- `item` (Any): 被丢弃的项目。
- `exception` (BaseException): 导致项目被丢弃的异常。
- `response` (Response | Failure | None): 导致项目被丢弃的响应或失败对象。
- `spider` (Spider): 执行此操作的爬虫实例。

**Returns**
- `LogFormatterResult`: 包含日志级别、消息和参数的字典。

**Raises**
- (unknown)

*来源: `scrapy/logformatter.py:115`*

---
<a id="sym-scrapy_logformatter.py-136"></a>

### `LogFormatter.item_error` · method
```python
def item_error(
        self,
        item: Any,
        exception: BaseException,
        response: Response | Failure | None,
        spider: Spider,
    ) -> LogFormatterResult
```

记录项目在通过项目管道时引发错误的日志消息。

**Parameters**
- `item` (Any): 引发错误的项目。
- `exception` (BaseException): 抛出的异常。
- `response` (Response | Failure | None): 相应的响应或失败对象，可能为 None。
- `spider` (Spider): 处理该项目的爬虫。

**Returns**
- `LogFormatterResult`: 包含日志级别、消息和参数的字典。

**Raises**
- (unknown)

*来源: `scrapy/logformatter.py:136`*

---
<a id="sym-scrapy_logformatter.py-154"></a>

### `LogFormatter.spider_error` · method
```python
def spider_error(
        self,
        failure: Failure,
        request: Request,
        response: Response | Failure,
        spider: Spider,
    ) -> LogFormatterResult
```

记录爬虫错误信息的日志。

**Parameters**
- `failure` (`Failure`): 异常失败对象。
- `request` (`Request`): 导致错误的请求。
- `response` (`Response` | `Failure`): 响应或失败对象。
- `spider` (`Spider`): 爬虫实例。

**Returns**
- `LogFormatterResult`: 日志格式化结果，包含日志级别、消息和参数。

**Raises**
- (unknown)

**内部调用(库内):**
- [`referer_str`](scrapy_utils.md#sym-scrapy_utils_request.py-150)

*来源: `scrapy/logformatter.py:154`*

---
<a id="sym-scrapy_logformatter.py-171"></a>

### `LogFormatter.download_error` · method
```python
def download_error(
        self,
        failure: Failure,
        request: Request,
        spider: Spider,
        errmsg: str | None = None,
    ) -> LogFormatterResult
```

记录爬虫在下载过程中发生的错误信息。

**Parameters**
- `failure` (`Failure`): 下载失败的异常对象。
- `request` (`Request`): 发生错误的请求对象。
- `spider` (`Spider`): 触发该错误的爬虫实例。
- `errmsg` (`str | None`, optional): 错误信息字符串，若提供则使用长格式消息。

**Returns**
- `LogFormatterResult`: 包含日志级别、消息和参数的字典，用于记录下载错误。

**Raises**
- (unknown)

*来源: `scrapy/logformatter.py:171`*

---
<a id="sym-scrapy_logformatter.py-194"></a>

### `LogFormatter.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

从爬虫实例创建日志格式化器。

**Parameters**
- `crawler`: Crawler - 爬虫实例

**Returns**
- `Self` - 日志格式化器实例

**Raises**
- (unknown)

*来源: `scrapy/logformatter.py:194`*

---

## `scrapy/mail.py`

<a id="sym-scrapy_mail.py-49"></a>

### `_to_bytes_or_none` · func
```python
def _to_bytes_or_none(text: str | bytes | None) -> bytes | None
```

将字符串或字节转换为字节，若输入为 None 则返回 None。

**Parameters**
- `text: str | bytes | None` - 要转换的文本

**Returns**
- `bytes | None` - 转换后的字节数据或 None

**Raises**
- `(unknown)`

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/mail.py:49`*

---
<a id="sym-scrapy_mail.py-63"></a>

### `MailSender` · class
```python
class MailSender
```

*来源: `scrapy/mail.py:63` · 待生成*

---
<a id="sym-scrapy_mail.py-64"></a>

### `MailSender.__init__` · method
```python
def __init__(
        self,
        smtphost: str = "localhost",
        mailfrom: str = "scrapy@localhost",
        smtpuser: str | None = None,
        smtppass: str | None = None,
        smtpport: int = 25,
        smtptls: bool = False,
        smtpssl: bool = False,
        debug: bool = False,
    )
```

**内部调用(库内):**
- [`is_reactorless`](scrapy_utils.md#sym-scrapy_utils_reactorless.py-16)
- [`_to_bytes_or_none`](scrapy.md#sym-scrapy_mail.py-49) — 将字符串或字节转换为字节，若输入为 None 则返回 None。

*来源: `scrapy/mail.py:64` · 待生成*

---
<a id="sym-scrapy_mail.py-87"></a>

### `MailSender.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/mail.py:87` · 待生成*

---
<a id="sym-scrapy_mail.py-99"></a>

### `MailSender.send` · method
```python
def send(
        self,
        to: str | list[str],
        subject: str,
        body: str,
        cc: str | list[str] | None = None,
        attachs: Sequence[tuple[str, str, IO[Any]]] = (),
        mimetype: str = "text/plain",
        charset: str | None = None,
        _callback: Callable[..., None] | None = None,
    ) -> Deferred[None] | None
```

**内部调用(库内):**
- [`MailSender._sendmail`](scrapy.md#sym-scrapy_mail.py-204)

*来源: `scrapy/mail.py:99` · 待生成*

---
<a id="sym-scrapy_mail.py-167"></a>

### `MailSender._sent_ok` · method
```python
def _sent_ok(
        self, result: Any, to: list[str], cc: list[str], subject: str, nattachs: int
    ) -> None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/mail.py:167` · 待生成*

---
<a id="sym-scrapy_mail.py-181"></a>

### `MailSender._sent_failed` · method
```python
def _sent_failed(
        self,
        failure: Failure,
        to: list[str],
        cc: list[str],
        subject: str,
        nattachs: int,
    ) -> Failure
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/mail.py:181` · 待生成*

---
<a id="sym-scrapy_mail.py-204"></a>

### `MailSender._sendmail` · method
```python
def _sendmail(self, to_addrs: list[str], msg: bytes) -> Deferred[Any]
```

**内部调用(库内):**
- [`MailSender._create_sender_factory`](scrapy.md#sym-scrapy_mail.py-221)

*来源: `scrapy/mail.py:204` · 待生成*

---
<a id="sym-scrapy_mail.py-221"></a>

### `MailSender._create_sender_factory` · method
```python
def _create_sender_factory(
        self, to_addrs: list[str], msg: IO[bytes], d: Deferred[Any]
    ) -> ESMTPSenderFactory
```

*来源: `scrapy/mail.py:221` · 待生成*

---

## `scrapy/middleware.py`

<a id="sym-scrapy_middleware.py-35"></a>

### `MiddlewareManager` · class
```python
class MiddlewareManager(ABC)
```

*来源: `scrapy/middleware.py:35` · 待生成*

---
<a id="sym-scrapy_middleware.py-41"></a>

### `MiddlewareManager.__init__` · method
```python
def __init__(self, *middlewares: Any, crawler: Crawler | None = None) -> None
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`MiddlewareManager._add_middleware`](scrapy.md#sym-scrapy_middleware.py-116)

*来源: `scrapy/middleware.py:41` · 待生成*

---
<a id="sym-scrapy_middleware.py-59"></a>

### `MiddlewareManager._spider` · method
装饰器: `@property`
```python
def _spider(self) -> Spider
```

*来源: `scrapy/middleware.py:59` · 待生成*

---
<a id="sym-scrapy_middleware.py-70"></a>

### `MiddlewareManager._set_compat_spider` · method
```python
def _set_compat_spider(self, spider: Spider | None) -> None
```

*来源: `scrapy/middleware.py:70` · 待生成*

---
<a id="sym-scrapy_middleware.py-84"></a>

### `MiddlewareManager._get_mwlist_from_settings` · method
装饰器: `@classmethod` `@abstractmethod`
```python
def _get_mwlist_from_settings(cls, settings: Settings) -> list[Any]
```

*来源: `scrapy/middleware.py:84` · 待生成*

---
<a id="sym-scrapy_middleware.py-88"></a>

### `MiddlewareManager.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`MiddlewareManager._get_mwlist_from_settings`](scrapy.md#sym-scrapy_middleware.py-84)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)

*来源: `scrapy/middleware.py:88` · 待生成*

---
<a id="sym-scrapy_middleware.py-116"></a>

### `MiddlewareManager._add_middleware` · method
```python
def _add_middleware(self, mw: Any) -> None
```

*来源: `scrapy/middleware.py:116` · 待生成*

---
<a id="sym-scrapy_middleware.py-119"></a>

### `MiddlewareManager._check_mw_method_spider_arg` · method
```python
def _check_mw_method_spider_arg(self, method: Callable[..., Any]) -> None
```

**内部调用(库内):**
- [`argument_is_required`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-203)

*来源: `scrapy/middleware.py:119` · 待生成*

---
<a id="sym-scrapy_middleware.py-131"></a>

### `MiddlewareManager._process_chain` · method
```python
async def _process_chain(
        self,
        methodname: str,
        obj: _T,
        *args: Any,
        add_spider: bool = False,
        always_add_spider: bool = False,
        warn_deferred: bool = False,
    ) -> _T
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/middleware.py:131` · 待生成*

---
<a id="sym-scrapy_middleware.py-155"></a>

### `MiddlewareManager.open_spider` · method
```python
def open_spider(self, spider: Spider) -> Deferred[list[None]]
```

*来源: `scrapy/middleware.py:155` · 待生成*

---
<a id="sym-scrapy_middleware.py-161"></a>

### `MiddlewareManager.close_spider` · method
```python
def close_spider(self, spider: Spider) -> Deferred[list[None]]
```

*来源: `scrapy/middleware.py:161` · 待生成*

---

## `scrapy/pqueues.py`

<a id="sym-scrapy_pqueues.py-22"></a>

### `_path_safe` · func
```python
def _path_safe(text: str) -> str
```

*来源: `scrapy/pqueues.py:22` · 待生成*

---
<a id="sym-scrapy_pqueues.py-40"></a>

### `QueueProtocol` · class
```python
class QueueProtocol(Protocol)
```

*来源: `scrapy/pqueues.py:40` · 待生成*

---
<a id="sym-scrapy_pqueues.py-43"></a>

### `QueueProtocol.push` · method
```python
def push(self, request: Request) -> None
```

*来源: `scrapy/pqueues.py:43` · 待生成*

---
<a id="sym-scrapy_pqueues.py-45"></a>

### `QueueProtocol.pop` · method
```python
def pop(self) -> Request | None
```

*来源: `scrapy/pqueues.py:45` · 待生成*

---
<a id="sym-scrapy_pqueues.py-47"></a>

### `QueueProtocol.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/pqueues.py:47` · 待生成*

---
<a id="sym-scrapy_pqueues.py-49"></a>

### `QueueProtocol.__len__` · method
```python
def __len__(self) -> int
```

*来源: `scrapy/pqueues.py:49` · 待生成*

---
<a id="sym-scrapy_pqueues.py-52"></a>

### `ScrapyPriorityQueue` · class
```python
class ScrapyPriorityQueue
```

*来源: `scrapy/pqueues.py:52` · 待生成*

---
<a id="sym-scrapy_pqueues.py-101"></a>

### `ScrapyPriorityQueue.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls,
        crawler: Crawler,
        downstream_queue_cls: type[QueueProtocol],
        key: str,
        startprios: Iterable[int] = (),
        *,
        start_queue_cls: type[QueueProtocol] | None = None,
    ) -> Self
```

*来源: `scrapy/pqueues.py:101` · 待生成*

---
<a id="sym-scrapy_pqueues.py-118"></a>

### `ScrapyPriorityQueue.__init__` · method
```python
def __init__(
        self,
        crawler: Crawler,
        downstream_queue_cls: type[QueueProtocol],
        key: str,
        startprios: Iterable[int] = (),
        *,
        start_queue_cls: type[QueueProtocol] | None = None,
    )
```

**内部调用(库内):**
- [`ScrapyPriorityQueue.init_prios`](scrapy.md#sym-scrapy_pqueues.py-136)

*来源: `scrapy/pqueues.py:118` · 待生成*

---
<a id="sym-scrapy_pqueues.py-136"></a>

### `ScrapyPriorityQueue.init_prios` · method
```python
def init_prios(self, startprios: Iterable[int]) -> None
```

**内部调用(库内):**
- [`ScrapyPriorityQueue.qfactory`](scrapy.md#sym-scrapy_pqueues.py-151)
- [`ScrapyPriorityQueue._sqfactory`](scrapy.md#sym-scrapy_pqueues.py-158)

*来源: `scrapy/pqueues.py:136` · 待生成*

---
<a id="sym-scrapy_pqueues.py-151"></a>

### `ScrapyPriorityQueue.qfactory` · method
```python
def qfactory(self, key: int) -> QueueProtocol
```

*来源: `scrapy/pqueues.py:151` · 待生成*

---
<a id="sym-scrapy_pqueues.py-158"></a>

### `ScrapyPriorityQueue._sqfactory` · method
```python
def _sqfactory(self, key: int) -> QueueProtocol
```

*来源: `scrapy/pqueues.py:158` · 待生成*

---
<a id="sym-scrapy_pqueues.py-166"></a>

### `ScrapyPriorityQueue.priority` · method
```python
def priority(self, request: Request) -> int
```

*来源: `scrapy/pqueues.py:166` · 待生成*

---
<a id="sym-scrapy_pqueues.py-169"></a>

### `ScrapyPriorityQueue.push` · method
```python
def push(self, request: Request) -> None
```

**内部调用(库内):**
- [`ScrapyPriorityQueue.priority`](scrapy.md#sym-scrapy_pqueues.py-166)
- [`ScrapyPriorityQueue._sqfactory`](scrapy.md#sym-scrapy_pqueues.py-158)
- [`ScrapyPriorityQueue.qfactory`](scrapy.md#sym-scrapy_pqueues.py-151)

*来源: `scrapy/pqueues.py:169` · 待生成*

---
<a id="sym-scrapy_pqueues.py-184"></a>

### `ScrapyPriorityQueue.pop` · method
```python
def pop(self) -> Request | None
```

**内部调用(库内):**
- [`ScrapyPriorityQueue._update_curprio`](scrapy.md#sym-scrapy_pqueues.py-214)

*来源: `scrapy/pqueues.py:184` · 待生成*

---
<a id="sym-scrapy_pqueues.py-214"></a>

### `ScrapyPriorityQueue._update_curprio` · method
```python
def _update_curprio(self) -> None
```

*来源: `scrapy/pqueues.py:214` · 待生成*

---
<a id="sym-scrapy_pqueues.py-223"></a>

### `ScrapyPriorityQueue.peek` · method
```python
def peek(self) -> Request | None
```

*来源: `scrapy/pqueues.py:223` · 待生成*

---
<a id="sym-scrapy_pqueues.py-239"></a>

### `ScrapyPriorityQueue.close` · method
```python
def close(self) -> list[int]
```

*来源: `scrapy/pqueues.py:239` · 待生成*

---
<a id="sym-scrapy_pqueues.py-247"></a>

### `ScrapyPriorityQueue.__len__` · method
```python
def __len__(self) -> int
```

*来源: `scrapy/pqueues.py:247` · 待生成*

---
<a id="sym-scrapy_pqueues.py-259"></a>

### `DownloaderInterface` · class
```python
class DownloaderInterface
```

*来源: `scrapy/pqueues.py:259` · 待生成*

---
<a id="sym-scrapy_pqueues.py-260"></a>

### `DownloaderInterface.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/pqueues.py:260` · 待生成*

---
<a id="sym-scrapy_pqueues.py-264"></a>

### `DownloaderInterface.stats` · method
```python
def stats(self, possible_slots: Iterable[str]) -> list[tuple[int, str]]
```

**内部调用(库内):**
- [`DownloaderInterface._active_downloads`](scrapy.md#sym-scrapy_pqueues.py-270)

*来源: `scrapy/pqueues.py:264` · 待生成*

---
<a id="sym-scrapy_pqueues.py-267"></a>

### `DownloaderInterface.get_slot_key` · method
```python
def get_slot_key(self, request: Request) -> str
```

*来源: `scrapy/pqueues.py:267` · 待生成*

---
<a id="sym-scrapy_pqueues.py-270"></a>

### `DownloaderInterface._active_downloads` · method
```python
def _active_downloads(self, slot: str) -> int
```

*来源: `scrapy/pqueues.py:270` · 待生成*

---
<a id="sym-scrapy_pqueues.py-277"></a>

### `DownloaderAwarePriorityQueue` · class
```python
class DownloaderAwarePriorityQueue
```

*来源: `scrapy/pqueues.py:277` · 待生成*

---
<a id="sym-scrapy_pqueues.py-304"></a>

### `DownloaderAwarePriorityQueue.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls,
        crawler: Crawler,
        downstream_queue_cls: type[QueueProtocol],
        key: str,
        startprios: dict[str, Iterable[int]] | None = None,
        *,
        start_queue_cls: type[QueueProtocol] | None = None,
    ) -> Self
```

*来源: `scrapy/pqueues.py:304` · 待生成*

---
<a id="sym-scrapy_pqueues.py-321"></a>

### `DownloaderAwarePriorityQueue.__init__` · method
```python
def __init__(
        self,
        crawler: Crawler,
        downstream_queue_cls: type[QueueProtocol],
        key: str,
        slot_startprios: dict[str, Iterable[int]] | None = None,
        *,
        start_queue_cls: type[QueueProtocol] | None = None,
    )
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`DownloaderInterface`](scrapy.md#sym-scrapy_pqueues.py-259)
- [`DownloaderAwarePriorityQueue.pqfactory`](scrapy.md#sym-scrapy_pqueues.py-385)

*来源: `scrapy/pqueues.py:321` · 待生成*

---
<a id="sym-scrapy_pqueues.py-358"></a>

### `DownloaderAwarePriorityQueue._next_slot` · method
```python
def _next_slot(self, stats: list[tuple[int, str]], *, update_state: bool) -> str
```

*来源: `scrapy/pqueues.py:358` · 待生成*

---
<a id="sym-scrapy_pqueues.py-385"></a>

### `DownloaderAwarePriorityQueue.pqfactory` · method
```python
def pqfactory(
        self, slot: str, startprios: Iterable[int] = ()
    ) -> ScrapyPriorityQueue
```

**内部调用(库内):**
- [`ScrapyPriorityQueue`](scrapy.md#sym-scrapy_pqueues.py-52)
- [`_path_safe`](scrapy.md#sym-scrapy_pqueues.py-22)

*来源: `scrapy/pqueues.py:385` · 待生成*

---
<a id="sym-scrapy_pqueues.py-396"></a>

### `DownloaderAwarePriorityQueue.pop` · method
```python
def pop(self) -> Request | None
```

**内部调用(库内):**
- [`DownloaderInterface.stats`](scrapy.md#sym-scrapy_pqueues.py-264)
- [`DownloaderAwarePriorityQueue._next_slot`](scrapy.md#sym-scrapy_pqueues.py-358)

*来源: `scrapy/pqueues.py:396` · 待生成*

---
<a id="sym-scrapy_pqueues.py-409"></a>

### `DownloaderAwarePriorityQueue.push` · method
```python
def push(self, request: Request) -> None
```

**内部调用(库内):**
- [`DownloaderInterface.get_slot_key`](scrapy.md#sym-scrapy_pqueues.py-267)
- [`DownloaderAwarePriorityQueue.pqfactory`](scrapy.md#sym-scrapy_pqueues.py-385)

*来源: `scrapy/pqueues.py:409` · 待生成*

---
<a id="sym-scrapy_pqueues.py-416"></a>

### `DownloaderAwarePriorityQueue.peek` · method
```python
def peek(self) -> Request | None
```

**内部调用(库内):**
- [`DownloaderInterface.stats`](scrapy.md#sym-scrapy_pqueues.py-264)
- [`DownloaderAwarePriorityQueue._next_slot`](scrapy.md#sym-scrapy_pqueues.py-358)

*来源: `scrapy/pqueues.py:416` · 待生成*

---
<a id="sym-scrapy_pqueues.py-430"></a>

### `DownloaderAwarePriorityQueue.close` · method
```python
def close(self) -> dict[str, list[int]]
```

*来源: `scrapy/pqueues.py:430` · 待生成*

---
<a id="sym-scrapy_pqueues.py-435"></a>

### `DownloaderAwarePriorityQueue.__len__` · method
```python
def __len__(self) -> int
```

*来源: `scrapy/pqueues.py:435` · 待生成*

---
<a id="sym-scrapy_pqueues.py-438"></a>

### `DownloaderAwarePriorityQueue.__contains__` · method
```python
def __contains__(self, slot: str) -> bool
```

*来源: `scrapy/pqueues.py:438` · 待生成*

---

## `scrapy/resolver.py`

<a id="sym-scrapy_resolver.py-33"></a>

### `CachingThreadedResolver` · class
装饰器: `@implementer(IResolverSimple)`
```python
class CachingThreadedResolver(ThreadedResolver)
```

*来源: `scrapy/resolver.py:33` · 待生成*

---
<a id="sym-scrapy_resolver.py-38"></a>

### `CachingThreadedResolver.__init__` · method
```python
def __init__(self, reactor: ReactorBase, cache_size: int, timeout: float)
```

*来源: `scrapy/resolver.py:38` · 待生成*

---
<a id="sym-scrapy_resolver.py-44"></a>

### `CachingThreadedResolver.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, reactor: ReactorBase) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/resolver.py:44` · 待生成*

---
<a id="sym-scrapy_resolver.py-51"></a>

### `CachingThreadedResolver.install_on_reactor` · method
```python
def install_on_reactor(self) -> None
```

*来源: `scrapy/resolver.py:51` · 待生成*

---
<a id="sym-scrapy_resolver.py-54"></a>

### `CachingThreadedResolver.getHostByName` · method
```python
def getHostByName(self, name: str, timeout: Sequence[int] = ()) -> Deferred[str]
```

*来源: `scrapy/resolver.py:54` · 待生成*

---
<a id="sym-scrapy_resolver.py-68"></a>

### `CachingThreadedResolver._cache_result` · method
```python
def _cache_result(self, result: Any, name: str) -> Any
```

*来源: `scrapy/resolver.py:68` · 待生成*

---
<a id="sym-scrapy_resolver.py-74"></a>

### `HostResolution` · class
装饰器: `@implementer(IHostResolution)`
```python
class HostResolution
```

*来源: `scrapy/resolver.py:74` · 待生成*

---
<a id="sym-scrapy_resolver.py-75"></a>

### `HostResolution.__init__` · method
```python
def __init__(self, name: str)
```

*来源: `scrapy/resolver.py:75` · 待生成*

---
<a id="sym-scrapy_resolver.py-78"></a>

### `HostResolution.cancel` · method
```python
def cancel(self) -> None
```

*来源: `scrapy/resolver.py:78` · 待生成*

---
<a id="sym-scrapy_resolver.py-83"></a>

### `_CachingResolutionReceiver` · class
装饰器: `@provider(IResolutionReceiver)`
```python
class _CachingResolutionReceiver
```

*来源: `scrapy/resolver.py:83` · 待生成*

---
<a id="sym-scrapy_resolver.py-84"></a>

### `_CachingResolutionReceiver.__init__` · method
```python
def __init__(self, resolutionReceiver: IResolutionReceiver, hostName: str)
```

*来源: `scrapy/resolver.py:84` · 待生成*

---
<a id="sym-scrapy_resolver.py-89"></a>

### `_CachingResolutionReceiver.resolutionBegan` · method
```python
def resolutionBegan(self, resolution: IHostResolution) -> None
```

*来源: `scrapy/resolver.py:89` · 待生成*

---
<a id="sym-scrapy_resolver.py-93"></a>

### `_CachingResolutionReceiver.addressResolved` · method
```python
def addressResolved(self, address: IAddress) -> None
```

*来源: `scrapy/resolver.py:93` · 待生成*

---
<a id="sym-scrapy_resolver.py-97"></a>

### `_CachingResolutionReceiver.resolutionComplete` · method
```python
def resolutionComplete(self) -> None
```

*来源: `scrapy/resolver.py:97` · 待生成*

---
<a id="sym-scrapy_resolver.py-104"></a>

### `CachingHostnameResolver` · class
装饰器: `@implementer(IHostnameResolver)`
```python
class CachingHostnameResolver
```

*来源: `scrapy/resolver.py:104` · 待生成*

---
<a id="sym-scrapy_resolver.py-110"></a>

### `CachingHostnameResolver.__init__` · method
```python
def __init__(self, reactor: ReactorBase, cache_size: int)
```

*来源: `scrapy/resolver.py:110` · 待生成*

---
<a id="sym-scrapy_resolver.py-116"></a>

### `CachingHostnameResolver.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, reactor: ReactorBase) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/resolver.py:116` · 待生成*

---
<a id="sym-scrapy_resolver.py-123"></a>

### `CachingHostnameResolver.install_on_reactor` · method
```python
def install_on_reactor(self) -> None
```

*来源: `scrapy/resolver.py:123` · 待生成*

---
<a id="sym-scrapy_resolver.py-126"></a>

### `CachingHostnameResolver.resolveHostName` · method
```python
def resolveHostName(
        self,
        resolutionReceiver: IResolutionReceiver,
        hostName: str,
        portNumber: int = 0,
        addressTypes: Sequence[type[IAddress]] | None = None,
        transportSemantics: str = "TCP",
    ) -> IHostResolution
```

**内部调用(库内):**
- [`_CachingResolutionReceiver`](scrapy.md#sym-scrapy_resolver.py-83)
- [`_CachingResolutionReceiver.resolutionBegan`](scrapy.md#sym-scrapy_resolver.py-89)
- [`HostResolution`](scrapy.md#sym-scrapy_resolver.py-74)
- [`_CachingResolutionReceiver.addressResolved`](scrapy.md#sym-scrapy_resolver.py-93)
- [`_CachingResolutionReceiver.resolutionComplete`](scrapy.md#sym-scrapy_resolver.py-97)

*来源: `scrapy/resolver.py:126` · 待生成*

---

## `scrapy/responsetypes.py`

<a id="sym-scrapy_responsetypes.py-21"></a>

### `ResponseTypes` · class
```python
class ResponseTypes
```

*来源: `scrapy/responsetypes.py:21` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-39"></a>

### `ResponseTypes.__init__` · method
```python
def __init__(self) -> None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/responsetypes.py:39` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-51"></a>

### `ResponseTypes.from_mimetype` · method
```python
def from_mimetype(self, mimetype: str) -> type[Response]
```

*来源: `scrapy/responsetypes.py:51` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-60"></a>

### `ResponseTypes.from_content_type` · method
```python
def from_content_type(
        self, content_type: str | bytes, content_encoding: bytes | None = None
    ) -> type[Response]
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)
- [`ResponseTypes.from_mimetype`](scrapy.md#sym-scrapy_responsetypes.py-51)

*来源: `scrapy/responsetypes.py:60` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-72"></a>

### `ResponseTypes.from_content_disposition` · method
```python
def from_content_disposition(
        self, content_disposition: str | bytes
    ) -> type[Response]
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)
- [`ResponseTypes.from_filename`](scrapy.md#sym-scrapy_responsetypes.py-99)

*来源: `scrapy/responsetypes.py:72` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-86"></a>

### `ResponseTypes.from_headers` · method
```python
def from_headers(self, headers: Mapping[bytes, bytes]) -> type[Response]
```

**内部调用(库内):**
- [`ResponseTypes.from_content_type`](scrapy.md#sym-scrapy_responsetypes.py-60)
- [`ResponseTypes.from_content_disposition`](scrapy.md#sym-scrapy_responsetypes.py-72)

*来源: `scrapy/responsetypes.py:86` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-99"></a>

### `ResponseTypes.from_filename` · method
```python
def from_filename(self, filename: str) -> type[Response]
```

**内部调用(库内):**
- [`ResponseTypes.from_mimetype`](scrapy.md#sym-scrapy_responsetypes.py-51)

*来源: `scrapy/responsetypes.py:99` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-106"></a>

### `ResponseTypes.from_body` · method
```python
def from_body(self, body: bytes) -> type[Response]
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`binary_is_text`](scrapy_utils.md#sym-scrapy_utils_python.py-166)
- [`ResponseTypes.from_mimetype`](scrapy.md#sym-scrapy_responsetypes.py-51)

*来源: `scrapy/responsetypes.py:106` · 待生成*

---
<a id="sym-scrapy_responsetypes.py-124"></a>

### `ResponseTypes.from_args` · method
```python
def from_args(
        self,
        headers: Mapping[bytes, bytes] | None = None,
        url: str | None = None,
        filename: str | None = None,
        body: bytes | None = None,
    ) -> type[Response]
```

**内部调用(库内):**
- [`ResponseTypes.from_headers`](scrapy.md#sym-scrapy_responsetypes.py-86)
- [`ResponseTypes.from_filename`](scrapy.md#sym-scrapy_responsetypes.py-99)
- [`ResponseTypes.from_body`](scrapy.md#sym-scrapy_responsetypes.py-106)

*来源: `scrapy/responsetypes.py:124` · 待生成*

---

## `scrapy/robotstxt.py`

<a id="sym-scrapy_robotstxt.py-24"></a>

### `decode_robotstxt` · func
```python
def decode_robotstxt(
    robotstxt_body: bytes, spider: Spider | None, to_native_str_type: bool = False
) -> str
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/robotstxt.py:24` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-45"></a>

### `RobotParser` · class
```python
class RobotParser(metaclass=ABCMeta)
```

*来源: `scrapy/robotstxt.py:45` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-48"></a>

### `RobotParser.from_crawler` · method
装饰器: `@classmethod` `@abstractmethod`
```python
def from_crawler(cls, crawler: Crawler, robotstxt_body: bytes) -> Self
```

*来源: `scrapy/robotstxt.py:48` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-60"></a>

### `RobotParser.allowed` · method
装饰器: `@abstractmethod`
```python
def allowed(self, url: str | bytes, user_agent: str | bytes) -> bool
```

*来源: `scrapy/robotstxt.py:60` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-71"></a>

### `PythonRobotParser` · class
```python
class PythonRobotParser(RobotParser)
```

*来源: `scrapy/robotstxt.py:71` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-72"></a>

### `PythonRobotParser.__init__` · method
```python
def __init__(self, robotstxt_body: bytes, spider: Spider | None)
```

**内部调用(库内):**
- [`decode_robotstxt`](scrapy.md#sym-scrapy_robotstxt.py-24)

*来源: `scrapy/robotstxt.py:72` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-79"></a>

### `PythonRobotParser.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, robotstxt_body: bytes) -> Self
```

*来源: `scrapy/robotstxt.py:79` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-83"></a>

### `PythonRobotParser.allowed` · method
```python
def allowed(self, url: str | bytes, user_agent: str | bytes) -> bool
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/robotstxt.py:83` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-89"></a>

### `RerpRobotParser` · class
```python
class RerpRobotParser(RobotParser)
```

*来源: `scrapy/robotstxt.py:89` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-90"></a>

### `RerpRobotParser.__init__` · method
```python
def __init__(self, robotstxt_body: bytes, spider: Spider | None)
```

**内部调用(库内):**
- [`decode_robotstxt`](scrapy.md#sym-scrapy_robotstxt.py-24)

*来源: `scrapy/robotstxt.py:90` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-99"></a>

### `RerpRobotParser.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, robotstxt_body: bytes) -> Self
```

*来源: `scrapy/robotstxt.py:99` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-103"></a>

### `RerpRobotParser.allowed` · method
```python
def allowed(self, url: str | bytes, user_agent: str | bytes) -> bool
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/robotstxt.py:103` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-109"></a>

### `ProtegoRobotParser` · class
```python
class ProtegoRobotParser(RobotParser)
```

*来源: `scrapy/robotstxt.py:109` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-110"></a>

### `ProtegoRobotParser.__init__` · method
```python
def __init__(self, robotstxt_body: bytes, spider: Spider | None)
```

**内部调用(库内):**
- [`decode_robotstxt`](scrapy.md#sym-scrapy_robotstxt.py-24)

*来源: `scrapy/robotstxt.py:110` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-116"></a>

### `ProtegoRobotParser.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, robotstxt_body: bytes) -> Self
```

*来源: `scrapy/robotstxt.py:116` · 待生成*

---
<a id="sym-scrapy_robotstxt.py-120"></a>

### `ProtegoRobotParser.allowed` · method
```python
def allowed(self, url: str | bytes, user_agent: str | bytes) -> bool
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/robotstxt.py:120` · 待生成*

---

## `scrapy/shell.py`

<a id="sym-scrapy_shell.py-94"></a>

### `Shell` · class
```python
class Shell
```

*来源: `scrapy/shell.py:94` · 待生成*

---
<a id="sym-scrapy_shell.py-97"></a>

### `Shell.__init__` · method
```python
def __init__(
        self,
        crawler: Crawler,
        update_vars: Callable[[dict[str, Any]], None] | None = None,
        code: str | None = None,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
    )
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/shell.py:97` · 待生成*

---
<a id="sym-scrapy_shell.py-130"></a>

### `Shell.inthread` · method
装饰器: `@property`
```python
def inthread(self) -> bool
```

*来源: `scrapy/shell.py:130` · 待生成*

---
<a id="sym-scrapy_shell.py-139"></a>

### `Shell.fetch_available` · method
装饰器: `@property`
```python
def fetch_available(self) -> bool
```

*来源: `scrapy/shell.py:139` · 待生成*

---
<a id="sym-scrapy_shell.py-143"></a>

### `Shell.start` · method
```python
def start(
        self,
        url: str | None = None,
        request: Request | None = None,
        response: Response | None = None,
        spider: Spider | None = None,
        redirect: bool = True,
    ) -> None
```

**内部调用(库内):**
- [`Shell.fetch`](scrapy.md#sym-scrapy_shell.py-210)
- [`Shell.populate_vars`](scrapy.md#sym-scrapy_shell.py-248)
- [`get_config`](scrapy_utils.md#sym-scrapy_utils_conf.py-104)
- [`start_python_console`](scrapy_utils.md#sym-scrapy_utils_console.py-122)

*来源: `scrapy/shell.py:143` · 待生成*

---
<a id="sym-scrapy_shell.py-188"></a>

### `Shell._schedule` · method
```python
async def _schedule(self, request: Request, spider: Spider | None) -> Response
```

**内部调用(库内):**
- [`Shell._open_spider`](scrapy.md#sym-scrapy_shell.py-201)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`_request_deferred`](scrapy.md#sym-scrapy_shell.py-313)

*来源: `scrapy/shell.py:188` · 待生成*

---
<a id="sym-scrapy_shell.py-201"></a>

### `Shell._open_spider` · method
```python
async def _open_spider(self, spider: Spider | None) -> None
```

**内部调用(库内):**
- [`Crawler._create_spider`](scrapy.md#sym-scrapy_crawler.py-230) — 创建并返回一个 spider 实例。

*来源: `scrapy/shell.py:201` · 待生成*

---
<a id="sym-scrapy_shell.py-210"></a>

### `Shell.fetch` · method
```python
def fetch(
        self,
        request_or_url: Request | str,
        spider: Spider | None = None,
        redirect: bool = True,
        **kwargs: Any,
    ) -> None
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)
- [`SequenceExclude`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-189)
- [`deferred_f_from_coro_f`](scrapy_utils.md#sym-scrapy_utils_defer.py-406)
- [`Shell._schedule`](scrapy.md#sym-scrapy_shell.py-188)
- [`Shell.populate_vars`](scrapy.md#sym-scrapy_shell.py-248)

*来源: `scrapy/shell.py:210` · 待生成*

---
<a id="sym-scrapy_shell.py-248"></a>

### `Shell.populate_vars` · method
```python
def populate_vars(
        self,
        response: Response | None = None,
        request: Request | None = None,
        spider: Spider | None = None,
    ) -> None
```

**内部调用(库内):**
- [`Command.update_vars`](scrapy_commands.md#sym-scrapy_commands_shell.py-62)
- [`Shell.get_help`](scrapy.md#sym-scrapy_shell.py-272)

*来源: `scrapy/shell.py:248` · 待生成*

---
<a id="sym-scrapy_shell.py-269"></a>

### `Shell.print_help` · method
```python
def print_help(self) -> None
```

**内部调用(库内):**
- [`Shell.get_help`](scrapy.md#sym-scrapy_shell.py-272)

*来源: `scrapy/shell.py:269` · 待生成*

---
<a id="sym-scrapy_shell.py-272"></a>

### `Shell.get_help` · method
```python
def get_help(self) -> str
```

**内部调用(库内):**
- [`Shell._is_relevant`](scrapy.md#sym-scrapy_shell.py-296)

*来源: `scrapy/shell.py:272` · 待生成*

---
<a id="sym-scrapy_shell.py-296"></a>

### `Shell._is_relevant` · method
```python
def _is_relevant(self, value: Any) -> bool
```

*来源: `scrapy/shell.py:296` · 待生成*

---
<a id="sym-scrapy_shell.py-300"></a>

### `inspect_response` · func
```python
def inspect_response(response: Response, spider: Spider) -> None
```

**内部调用(库内):**
- [`Shell.start`](scrapy.md#sym-scrapy_shell.py-143)
- [`Shell`](scrapy.md#sym-scrapy_shell.py-94)

*来源: `scrapy/shell.py:300` · 待生成*

---
<a id="sym-scrapy_shell.py-313"></a>

### `_request_deferred` · func
```python
def _request_deferred(request: Request) -> Deferred[Any]
```

*来源: `scrapy/shell.py:313` · 待生成*

---
<a id="sym-scrapy_shell.py-327"></a>

### `_restore_callbacks` · func
```python
def _restore_callbacks(result: Any) -> Any
```

*来源: `scrapy/shell.py:327` · 待生成*

---

## `scrapy/signalmanager.py`

<a id="sym-scrapy_signalmanager.py-14"></a>

### `SignalManager` · class
```python
class SignalManager
```

*来源: `scrapy/signalmanager.py:14` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-15"></a>

### `SignalManager.__init__` · method
```python
def __init__(self, sender: Any = dispatcher.Anonymous)
```

*来源: `scrapy/signalmanager.py:15` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-18"></a>

### `SignalManager.connect` · method
```python
def connect(self, receiver: Any, signal: Any, **kwargs: Any) -> None
```

*来源: `scrapy/signalmanager.py:18` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-35"></a>

### `SignalManager.disconnect` · method
```python
def disconnect(self, receiver: Any, signal: Any, **kwargs: Any) -> None
```

*来源: `scrapy/signalmanager.py:35` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-44"></a>

### `SignalManager.send_catch_log` · method
```python
def send_catch_log(self, signal: Any, **kwargs: Any) -> list[tuple[Any, Any]]
```

*来源: `scrapy/signalmanager.py:44` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-54"></a>

### `SignalManager.send_catch_log_deferred` · method
```python
def send_catch_log_deferred(
        self, signal: Any, **kwargs: Any
    ) -> Deferred[list[tuple[Any, Any]]]
```

**内部调用(库内):**
- [`_send_catch_log_deferred`](scrapy_utils.md#sym-scrapy_utils_signal.py-98)

*来源: `scrapy/signalmanager.py:54` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-75"></a>

### `SignalManager.send_catch_log_async` · method
```python
async def send_catch_log_async(
        self, signal: Any, **kwargs: Any
    ) -> list[tuple[Any, Any]]
```

*来源: `scrapy/signalmanager.py:75` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-94"></a>

### `SignalManager.disconnect_all` · method
```python
def disconnect_all(self, signal: Any, **kwargs: Any) -> None
```

*来源: `scrapy/signalmanager.py:94` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-104"></a>

### `SignalManager.wait_for` · method
```python
async def wait_for(self, signal: Any) -> None
```

**内部调用(库内):**
- [`SignalManager.disconnect`](scrapy.md#sym-scrapy_signalmanager.py-35)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)
- [`SignalManager.connect`](scrapy.md#sym-scrapy_signalmanager.py-18)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/signalmanager.py:104` · 待生成*

---
<a id="sym-scrapy_signalmanager.py-111"></a>

### `SignalManager.handle` · method
```python
def handle() -> None
```

**内部调用(库内):**
- [`SignalManager.disconnect`](scrapy.md#sym-scrapy_signalmanager.py-35)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/signalmanager.py:111` · 待生成*

---

## `scrapy/spiderloader.py`

<a id="sym-scrapy_spiderloader.py-25"></a>

### `get_spider_loader` · func
```python
def get_spider_loader(settings: BaseSettings) -> SpiderLoaderProtocol
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`SpiderLoaderProtocol.from_settings`](scrapy.md#sym-scrapy_spiderloader.py-35)
- [`BaseSettings.frozencopy`](scrapy_settings.md#sym-scrapy_settings___init__.py-634)

*来源: `scrapy/spiderloader.py:25` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-33"></a>

### `SpiderLoaderProtocol` · class
```python
class SpiderLoaderProtocol(Protocol)
```

*来源: `scrapy/spiderloader.py:33` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-35"></a>

### `SpiderLoaderProtocol.from_settings` · method
装饰器: `@classmethod`
```python
def from_settings(cls, settings: BaseSettings) -> Self
```

*来源: `scrapy/spiderloader.py:35` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-38"></a>

### `SpiderLoaderProtocol.load` · method
```python
def load(self, spider_name: str) -> type[Spider]
```

*来源: `scrapy/spiderloader.py:38` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-42"></a>

### `SpiderLoaderProtocol.list` · method
```python
def list(self) -> list[str]
```

*来源: `scrapy/spiderloader.py:42` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-46"></a>

### `SpiderLoaderProtocol.find_by_request` · method
```python
def find_by_request(self, request: Request) -> __builtins__.list[str]
```

*来源: `scrapy/spiderloader.py:46` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-51"></a>

### `SpiderLoader` · class
装饰器: `@implementer(ISpiderLoader)`
```python
class SpiderLoader
```

*来源: `scrapy/spiderloader.py:51` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-57"></a>

### `SpiderLoader.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`SpiderLoader._load_all_spiders`](scrapy.md#sym-scrapy_spiderloader.py-89)

*来源: `scrapy/spiderloader.py:57` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-64"></a>

### `SpiderLoader._check_name_duplicates` · method
```python
def _check_name_duplicates(self) -> None
```

*来源: `scrapy/spiderloader.py:64` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-84"></a>

### `SpiderLoader._load_spiders` · method
```python
def _load_spiders(self, module: ModuleType) -> None
```

**内部调用(库内):**
- [`iter_spider_classes`](scrapy_utils.md#sym-scrapy_utils_spider.py-50)

*来源: `scrapy/spiderloader.py:84` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-89"></a>

### `SpiderLoader._load_all_spiders` · method
```python
def _load_all_spiders(self) -> None
```

**内部调用(库内):**
- [`walk_modules_iter`](scrapy_utils.md#sym-scrapy_utils_misc.py-93)
- [`SpiderLoader._load_spiders`](scrapy.md#sym-scrapy_spiderloader.py-84)
- [`SpiderLoader._check_name_duplicates`](scrapy.md#sym-scrapy_spiderloader.py-64)

*来源: `scrapy/spiderloader.py:89` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-108"></a>

### `SpiderLoader.from_settings` · method
装饰器: `@classmethod`
```python
def from_settings(cls, settings: BaseSettings) -> Self
```

*来源: `scrapy/spiderloader.py:108` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-111"></a>

### `SpiderLoader.load` · method
```python
def load(self, spider_name: str) -> type[Spider]
```

*来源: `scrapy/spiderloader.py:111` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-121"></a>

### `SpiderLoader.find_by_request` · method
```python
def find_by_request(self, request: Request) -> list[str]
```

*来源: `scrapy/spiderloader.py:121` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-129"></a>

### `SpiderLoader.list` · method
```python
def list(self) -> list[str]
```

*来源: `scrapy/spiderloader.py:129` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-137"></a>

### `DummySpiderLoader` · class
装饰器: `@implementer(ISpiderLoader)`
```python
class DummySpiderLoader
```

*来源: `scrapy/spiderloader.py:137` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-141"></a>

### `DummySpiderLoader.from_settings` · method
装饰器: `@classmethod`
```python
def from_settings(cls, settings: BaseSettings) -> Self
```

*来源: `scrapy/spiderloader.py:141` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-144"></a>

### `DummySpiderLoader.load` · method
```python
def load(self, spider_name: str) -> type[Spider]
```

*来源: `scrapy/spiderloader.py:144` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-147"></a>

### `DummySpiderLoader.list` · method
```python
def list(self) -> list[str]
```

*来源: `scrapy/spiderloader.py:147` · 待生成*

---
<a id="sym-scrapy_spiderloader.py-150"></a>

### `DummySpiderLoader.find_by_request` · method
```python
def find_by_request(self, request: Request) -> __builtins__.list[str]
```

*来源: `scrapy/spiderloader.py:150` · 待生成*

---

## `scrapy/squeues.py`

<a id="sym-scrapy_squeues.py-27"></a>

### `_with_mkdir` · func
```python
def _with_mkdir(queue_class: type[queue.BaseQueue]) -> type[queue.BaseQueue]
```

**内部调用(库内):**
- [`DirectoriesCreated.__init__`](scrapy.md#sym-scrapy_squeues.py-29)

*来源: `scrapy/squeues.py:27` · 待生成*

---
<a id="sym-scrapy_squeues.py-28"></a>

### `DirectoriesCreated` · class
```python
class DirectoriesCreated(queue_class)
```

*来源: `scrapy/squeues.py:28` · 待生成*

---
<a id="sym-scrapy_squeues.py-29"></a>

### `DirectoriesCreated.__init__` · method
```python
def __init__(self, path: str | PathLike[str], *args: Any, **kwargs: Any)
```

*来源: `scrapy/squeues.py:29` · 待生成*

---
<a id="sym-scrapy_squeues.py-38"></a>

### `_serializable_queue` · func
```python
def _serializable_queue(
    queue_class: type[queue.BaseQueue],
    serialize: Callable[[Any], bytes],
    deserialize: Callable[[bytes], Any],
) -> type[queue.BaseQueue]
```

**内部调用(库内):**
- [`SerializableQueue.push`](scrapy.md#sym-scrapy_squeues.py-44)
- [`SerializableQueue.peek`](scrapy.md#sym-scrapy_squeues.py-54)

*来源: `scrapy/squeues.py:38` · 待生成*

---
<a id="sym-scrapy_squeues.py-43"></a>

### `SerializableQueue` · class
```python
class SerializableQueue(queue_class)
```

*来源: `scrapy/squeues.py:43` · 待生成*

---
<a id="sym-scrapy_squeues.py-44"></a>

### `SerializableQueue.push` · method
```python
def push(self, obj: Any) -> None
```

*来源: `scrapy/squeues.py:44` · 待生成*

---
<a id="sym-scrapy_squeues.py-48"></a>

### `SerializableQueue.pop` · method
```python
def pop(self) -> Any | None
```

*来源: `scrapy/squeues.py:48` · 待生成*

---
<a id="sym-scrapy_squeues.py-54"></a>

### `SerializableQueue.peek` · method
```python
def peek(self) -> Any | None
```

*来源: `scrapy/squeues.py:54` · 待生成*

---
<a id="sym-scrapy_squeues.py-74"></a>

### `_scrapy_serialization_queue` · func
```python
def _scrapy_serialization_queue(
    queue_class: type[queue.BaseQueue],
) -> type[queue.BaseQueue]
```

**内部调用(库内):**
- [`DirectoriesCreated.__init__`](scrapy.md#sym-scrapy_squeues.py-29)
- [`Request.to_dict`](scrapy_http.md#sym-scrapy_http_request___init__.py-384)
- [`SerializableQueue.push`](scrapy.md#sym-scrapy_squeues.py-44)
- [`request_from_dict`](scrapy_utils.md#sym-scrapy_utils_request.py-158)
- [`SerializableQueue.peek`](scrapy.md#sym-scrapy_squeues.py-54)

*来源: `scrapy/squeues.py:74` · 待生成*

---
<a id="sym-scrapy_squeues.py-77"></a>

### `ScrapyRequestQueue` · class
```python
class ScrapyRequestQueue(queue_class)
```

*来源: `scrapy/squeues.py:77` · 待生成*

---
<a id="sym-scrapy_squeues.py-78"></a>

### `ScrapyRequestQueue.__init__` · method
```python
def __init__(self, crawler: Crawler, key: str)
```

*来源: `scrapy/squeues.py:78` · 待生成*

---
<a id="sym-scrapy_squeues.py-83"></a>

### `ScrapyRequestQueue.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
            cls, crawler: Crawler, key: str, *args: Any, **kwargs: Any
        ) -> Self
```

*来源: `scrapy/squeues.py:83` · 待生成*

---
<a id="sym-scrapy_squeues.py-88"></a>

### `ScrapyRequestQueue.push` · method
```python
def push(self, request: Request) -> None
```

**内部调用(库内):**
- [`Request.to_dict`](scrapy_http.md#sym-scrapy_http_request___init__.py-384)

*来源: `scrapy/squeues.py:88` · 待生成*

---
<a id="sym-scrapy_squeues.py-92"></a>

### `ScrapyRequestQueue.pop` · method
```python
def pop(self) -> Request | None
```

**内部调用(库内):**
- [`request_from_dict`](scrapy_utils.md#sym-scrapy_utils_request.py-158)

*来源: `scrapy/squeues.py:92` · 待生成*

---
<a id="sym-scrapy_squeues.py-98"></a>

### `ScrapyRequestQueue.peek` · method
```python
def peek(self) -> Request | None
```

**内部调用(库内):**
- [`request_from_dict`](scrapy_utils.md#sym-scrapy_utils_request.py-158)

*来源: `scrapy/squeues.py:98` · 待生成*

---
<a id="sym-scrapy_squeues.py-113"></a>

### `_scrapy_non_serialization_queue` · func
```python
def _scrapy_non_serialization_queue(
    queue_class: type[queue.BaseQueue],
) -> type[queue.BaseQueue]
```

**内部调用(库内):**
- [`SerializableQueue.peek`](scrapy.md#sym-scrapy_squeues.py-54)

*来源: `scrapy/squeues.py:113` · 待生成*

---
<a id="sym-scrapy_squeues.py-116"></a>

### `ScrapyRequestQueue` · class
```python
class ScrapyRequestQueue(queue_class)
```

*来源: `scrapy/squeues.py:116` · 待生成*

---
<a id="sym-scrapy_squeues.py-118"></a>

### `ScrapyRequestQueue.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self
```

*来源: `scrapy/squeues.py:118` · 待生成*

---
<a id="sym-scrapy_squeues.py-121"></a>

### `ScrapyRequestQueue.peek` · method
```python
def peek(self) -> Any | None
```

**内部调用(库内):**
- [`ScrapyRequestQueue.peek`](scrapy.md#sym-scrapy_squeues.py-98)

*来源: `scrapy/squeues.py:121` · 待生成*

---
<a id="sym-scrapy_squeues.py-139"></a>

### `_pickle_serialize` · func
```python
def _pickle_serialize(obj: Any) -> bytes
```

*来源: `scrapy/squeues.py:139` · 待生成*

---

## `scrapy/statscollectors.py`

<a id="sym-scrapy_statscollectors.py-24"></a>

### `StatsCollector` · class
```python
class StatsCollector
```

*来源: `scrapy/statscollectors.py:24` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-25"></a>

### `StatsCollector.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/statscollectors.py:25` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-30"></a>

### `StatsCollector.__getattribute__` · method
```python
def __getattribute__(self, name: str) -> Any
```

*来源: `scrapy/statscollectors.py:30` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-57"></a>

### `StatsCollector.get_value` · method
```python
def get_value(
        self, key: str, default: Any = None, spider: Spider | None = None
    ) -> Any
```

*来源: `scrapy/statscollectors.py:57` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-62"></a>

### `StatsCollector.get_stats` · method
```python
def get_stats(self, spider: Spider | None = None) -> StatsT
```

*来源: `scrapy/statscollectors.py:62` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-65"></a>

### `StatsCollector.set_value` · method
```python
def set_value(self, key: str, value: Any, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:65` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-68"></a>

### `StatsCollector.set_stats` · method
```python
def set_stats(self, stats: StatsT, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:68` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-71"></a>

### `StatsCollector.inc_value` · method
```python
def inc_value(
        self, key: str, count: int = 1, start: int = 0, spider: Spider | None = None
    ) -> None
```

*来源: `scrapy/statscollectors.py:71` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-77"></a>

### `StatsCollector.max_value` · method
```python
def max_value(self, key: str, value: Any, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:77` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-80"></a>

### `StatsCollector.min_value` · method
```python
def min_value(self, key: str, value: Any, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:80` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-83"></a>

### `StatsCollector.clear_stats` · method
```python
def clear_stats(self, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:83` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-86"></a>

### `StatsCollector.open_spider` · method
```python
def open_spider(self, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:86` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-89"></a>

### `StatsCollector.close_spider` · method
```python
def close_spider(
        self, spider: Spider | None = None, reason: str | None = None
    ) -> None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)
- [`StatsCollector._persist_stats`](scrapy.md#sym-scrapy_statscollectors.py-99)

*来源: `scrapy/statscollectors.py:89` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-99"></a>

### `StatsCollector._persist_stats` · method
```python
def _persist_stats(self, stats: StatsT) -> None
```

*来源: `scrapy/statscollectors.py:99` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-103"></a>

### `MemoryStatsCollector` · class
```python
class MemoryStatsCollector(StatsCollector)
```

*来源: `scrapy/statscollectors.py:103` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-104"></a>

### `MemoryStatsCollector.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/statscollectors.py:104` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-108"></a>

### `MemoryStatsCollector._persist_stats` · method
```python
def _persist_stats(self, stats: StatsT) -> None
```

*来源: `scrapy/statscollectors.py:108` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-113"></a>

### `DummyStatsCollector` · class
```python
class DummyStatsCollector(StatsCollector)
```

*来源: `scrapy/statscollectors.py:113` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-114"></a>

### `DummyStatsCollector.get_value` · method
```python
def get_value(
        self, key: str, default: Any = None, spider: Spider | None = None
    ) -> Any
```

*来源: `scrapy/statscollectors.py:114` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-119"></a>

### `DummyStatsCollector.set_value` · method
```python
def set_value(self, key: str, value: Any, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:119` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-122"></a>

### `DummyStatsCollector.set_stats` · method
```python
def set_stats(self, stats: StatsT, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:122` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-125"></a>

### `DummyStatsCollector.inc_value` · method
```python
def inc_value(
        self, key: str, count: int = 1, start: int = 0, spider: Spider | None = None
    ) -> None
```

*来源: `scrapy/statscollectors.py:125` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-130"></a>

### `DummyStatsCollector.max_value` · method
```python
def max_value(self, key: str, value: Any, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:130` · 待生成*

---
<a id="sym-scrapy_statscollectors.py-133"></a>

### `DummyStatsCollector.min_value` · method
```python
def min_value(self, key: str, value: Any, spider: Spider | None = None) -> None
```

*来源: `scrapy/statscollectors.py:133` · 待生成*

---