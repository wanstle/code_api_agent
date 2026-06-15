# API 参考:`scrapy/commands`

## `scrapy/commands/__init__.py`

<a id="sym-scrapy_commands___init__.py-27"></a>

### `ScrapyCommand` · class
```python
class ScrapyCommand(ABC)
```

*来源: `scrapy/commands/__init__.py:27` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-37"></a>

### `ScrapyCommand.__init__` · method
```python
def __init__(self) -> None
```

*来源: `scrapy/commands/__init__.py:37` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-40"></a>

### `ScrapyCommand.set_crawler` · method
```python
def set_crawler(self, crawler: Crawler) -> None
```

*来源: `scrapy/commands/__init__.py:40` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-50"></a>

### `ScrapyCommand.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/__init__.py:50` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-57"></a>

### `ScrapyCommand.short_desc` · method
装饰器: `@abstractmethod`
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/__init__.py:57` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-63"></a>

### `ScrapyCommand.long_desc` · method
```python
def long_desc(self) -> str
```

**内部调用(库内):**
- [`ScrapyCommand.short_desc`](scrapy_commands.md#sym-scrapy_commands___init__.py-57)

*来源: `scrapy/commands/__init__.py:63` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-70"></a>

### `ScrapyCommand.help` · method
```python
def help(self) -> str
```

**内部调用(库内):**
- [`ScrapyCommand.long_desc`](scrapy_commands.md#sym-scrapy_commands___init__.py-63)

*来源: `scrapy/commands/__init__.py:70` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-77"></a>

### `ScrapyCommand.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/__init__.py:77` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-113"></a>

### `ScrapyCommand.process_options` · method
```python
def process_options(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`BaseSettings.setdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-535)
- [`arglist_to_dict`](scrapy_utils.md#sym-scrapy_utils_conf.py-66)
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。

*来源: `scrapy/commands/__init__.py:113` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-142"></a>

### `ScrapyCommand.run` · method
装饰器: `@abstractmethod`
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

*来源: `scrapy/commands/__init__.py:142` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-149"></a>

### `BaseRunSpiderCommand` · class
```python
class BaseRunSpiderCommand(ScrapyCommand)
```

*来源: `scrapy/commands/__init__.py:149` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-154"></a>

### `BaseRunSpiderCommand.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/__init__.py:154` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-181"></a>

### `BaseRunSpiderCommand.process_options` · method
```python
def process_options(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`arglist_to_dict`](scrapy_utils.md#sym-scrapy_utils_conf.py-66)
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。
- [`feed_process_params_from_cli`](scrapy_utils.md#sym-scrapy_utils_conf.py-144)

*来源: `scrapy/commands/__init__.py:181` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-199"></a>

### `ScrapyHelpFormatter` · class
```python
class ScrapyHelpFormatter(argparse.HelpFormatter)
```

*来源: `scrapy/commands/__init__.py:199` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-204"></a>

### `ScrapyHelpFormatter.__init__` · method
```python
def __init__(
        self,
        prog: str,
        indent_increment: int = 2,
        max_help_position: int = 24,
        width: int | None = None,
    )
```

*来源: `scrapy/commands/__init__.py:204` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-218"></a>

### `ScrapyHelpFormatter._join_parts` · method
```python
def _join_parts(self, part_strings: Iterable[str]) -> str
```

**内部调用(库内):**
- [`ScrapyHelpFormatter.format_part_strings`](scrapy_commands.md#sym-scrapy_commands___init__.py-223)

*来源: `scrapy/commands/__init__.py:218` · 待生成*

---
<a id="sym-scrapy_commands___init__.py-223"></a>

### `ScrapyHelpFormatter.format_part_strings` · method
```python
def format_part_strings(self, part_strings: list[str]) -> list[str]
```

*来源: `scrapy/commands/__init__.py:223` · 待生成*

---

## `scrapy/commands/bench.py`

<a id="sym-scrapy_commands_bench.py-20"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/bench.py:20` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-27"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/bench.py:27` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-30"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`_BenchServer`](scrapy_commands.md#sym-scrapy_commands_bench.py-37)
- [`_BenchSpider.start`](scrapy_commands.md#sym-scrapy_commands_bench.py-61)

*来源: `scrapy/commands/bench.py:30` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-37"></a>

### `_BenchServer` · class
```python
class _BenchServer
```

*来源: `scrapy/commands/bench.py:37` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-38"></a>

### `_BenchServer.__enter__` · method
```python
def __enter__(self) -> None
```

*来源: `scrapy/commands/bench.py:38` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-46"></a>

### `_BenchServer.__exit__` · method
```python
def __exit__(self, exc_type, exc_value, traceback) -> None
```

**内部调用(库内):**
- [`CallLaterOnce.wait`](scrapy_utils.md#sym-scrapy_utils_reactor.py-86)

*来源: `scrapy/commands/bench.py:46` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-52"></a>

### `_BenchSpider` · class
```python
class _BenchSpider(scrapy.Spider)
```

*来源: `scrapy/commands/bench.py:52` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-61"></a>

### `_BenchSpider.start` · method
```python
async def start(self) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/commands/bench.py:61` · 待生成*

---
<a id="sym-scrapy_commands_bench.py-66"></a>

### `_BenchSpider.parse` · method
```python
def parse(self, response: Response) -> Any
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/commands/bench.py:66` · 待生成*

---

## `scrapy/commands/check.py`

<a id="sym-scrapy_commands_check.py-16"></a>

### `TextTestResult` · class
```python
class TextTestResult(_TextTestResult)
```

*来源: `scrapy/commands/check.py:16` · 待生成*

---
<a id="sym-scrapy_commands_check.py-17"></a>

### `TextTestResult.printSummary` · method
```python
def printSummary(self, start: float, stop: float) -> None
```

*来源: `scrapy/commands/check.py:17` · 待生成*

---
<a id="sym-scrapy_commands_check.py-45"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/check.py:45` · 待生成*

---
<a id="sym-scrapy_commands_check.py-49"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/check.py:49` · 待生成*

---
<a id="sym-scrapy_commands_check.py-52"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/check.py:52` · 待生成*

---
<a id="sym-scrapy_commands_check.py-55"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/check.py:55` · 待生成*

---
<a id="sym-scrapy_commands_check.py-73"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`BaseSettings.get_component_priority_dict_with_base`](scrapy_settings.md#sym-scrapy_settings___init__.py-338)
- [`ContractsManager`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-92)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`TextTestResult`](scrapy_commands.md#sym-scrapy_commands_check.py-16)
- [`ContractsManager.from_spider`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-125)
- [`set_environ`](scrapy_utils.md#sym-scrapy_utils_misc.py-222)
- [`ContractsManager.tested_methods_from_spidercls`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-99)
- [`Command.start`](scrapy_commands.md#sym-scrapy_commands_check.py-89)
- [`TextTestResult.printSummary`](scrapy_commands.md#sym-scrapy_commands_check.py-17)

*来源: `scrapy/commands/check.py:73` · 待生成*

---
<a id="sym-scrapy_commands_check.py-89"></a>

### `Command.start` · method
```python
async def start(self: Spider) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`ContractsManager.from_spider`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-125)

*来源: `scrapy/commands/check.py:89` · 待生成*

---

## `scrapy/commands/crawl.py`

<a id="sym-scrapy_commands_crawl.py-12"></a>

### `Command` · class
```python
class Command(BaseRunSpiderCommand)
```

*来源: `scrapy/commands/crawl.py:12` · 待生成*

---
<a id="sym-scrapy_commands_crawl.py-15"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/crawl.py:15` · 待生成*

---
<a id="sym-scrapy_commands_crawl.py-18"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/crawl.py:18` · 待生成*

---
<a id="sym-scrapy_commands_crawl.py-21"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。

*来源: `scrapy/commands/crawl.py:21` · 待生成*

---

## `scrapy/commands/edit.py`

<a id="sym-scrapy_commands_edit.py-11"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/edit.py:11` · 待生成*

---
<a id="sym-scrapy_commands_edit.py-16"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/edit.py:16` · 待生成*

---
<a id="sym-scrapy_commands_edit.py-19"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/edit.py:19` · 待生成*

---
<a id="sym-scrapy_commands_edit.py-22"></a>

### `Command.long_desc` · method
```python
def long_desc(self) -> str
```

*来源: `scrapy/commands/edit.py:22` · 待生成*

---
<a id="sym-scrapy_commands_edit.py-28"></a>

### `Command._err` · method
```python
def _err(self, msg: str) -> None
```

*来源: `scrapy/commands/edit.py:28` · 待生成*

---
<a id="sym-scrapy_commands_edit.py-32"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`get_spider_loader`](scrapy.md#sym-scrapy_spiderloader.py-25)
- [`Command._err`](scrapy_commands.md#sym-scrapy_commands_edit.py-28)

*来源: `scrapy/commands/edit.py:32` · 待生成*

---

## `scrapy/commands/fetch.py`

<a id="sym-scrapy_commands_fetch.py-22"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/fetch.py:22` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-23"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/fetch.py:23` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-26"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/fetch.py:26` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-29"></a>

### `Command.long_desc` · method
```python
def long_desc(self) -> str
```

*来源: `scrapy/commands/fetch.py:29` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-35"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: ArgumentParser) -> None
```

*来源: `scrapy/commands/fetch.py:35` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-52"></a>

### `Command._print_headers` · method
```python
def _print_headers(self, headers: dict[bytes, list[bytes]], prefix: bytes) -> None
```

**内部调用(库内):**
- [`Command._print_bytes`](scrapy_commands.md#sym-scrapy_commands_fetch.py-66)

*来源: `scrapy/commands/fetch.py:52` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-57"></a>

### `Command._print_response` · method
```python
def _print_response(self, response: Response, opts: Namespace) -> None
```

**内部调用(库内):**
- [`Command._print_headers`](scrapy_commands.md#sym-scrapy_commands_fetch.py-52)
- [`Command._print_bytes`](scrapy_commands.md#sym-scrapy_commands_fetch.py-66)

*来源: `scrapy/commands/fetch.py:57` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-66"></a>

### `Command._print_bytes` · method
```python
def _print_bytes(self, bytes_: bytes) -> None
```

*来源: `scrapy/commands/fetch.py:66` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-69"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: Namespace) -> None
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)
- [`SequenceExclude`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-189)
- [`Command.start`](scrapy_commands.md#sym-scrapy_commands_fetch.py-93)

*来源: `scrapy/commands/fetch.py:69` · 待生成*

---
<a id="sym-scrapy_commands_fetch.py-93"></a>

### `Command.start` · method
```python
async def start(self: Spider) -> AsyncIterator[Any]
```

*来源: `scrapy/commands/fetch.py:93` · 待生成*

---

## `scrapy/commands/genspider.py`

<a id="sym-scrapy_commands_genspider.py-21"></a>

### `sanitize_module_name` · func
```python
def sanitize_module_name(module_name: str) -> str
```

*来源: `scrapy/commands/genspider.py:21` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-32"></a>

### `extract_domain` · func
```python
def extract_domain(url: str) -> str
```

*来源: `scrapy/commands/genspider.py:32` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-40"></a>

### `verify_url_scheme` · func
```python
def verify_url_scheme(url: str) -> str
```

*来源: `scrapy/commands/genspider.py:40` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-48"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/genspider.py:48` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-52"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/genspider.py:52` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-55"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/genspider.py:55` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-58"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/genspider.py:58` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-95"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`Command._list_templates`](scrapy_commands.md#sym-scrapy_commands_genspider.py-182)
- [`Command._find_template`](scrapy_commands.md#sym-scrapy_commands_genspider.py-172)
- [`verify_url_scheme`](scrapy_commands.md#sym-scrapy_commands_genspider.py-40)
- [`sanitize_module_name`](scrapy_commands.md#sym-scrapy_commands_genspider.py-21)
- [`Command._spider_exists`](scrapy_commands.md#sym-scrapy_commands_genspider.py-192)
- [`Command._genspider`](scrapy_commands.md#sym-scrapy_commands_genspider.py-144)

*来源: `scrapy/commands/genspider.py:95` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-125"></a>

### `Command._generate_template_variables` · method
```python
def _generate_template_variables(
        self,
        module: str,
        name: str,
        url: str,
        template_name: str,
    ) -> dict[str, Any]
```

**内部调用(库内):**
- [`string_camelcase`](scrapy_utils.md#sym-scrapy_utils_template.py-31)
- [`extract_domain`](scrapy_commands.md#sym-scrapy_commands_genspider.py-32)

*来源: `scrapy/commands/genspider.py:125` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-144"></a>

### `Command._genspider` · method
```python
def _genspider(
        self,
        module: str,
        name: str,
        url: str,
        template_name: str,
        template_file: str | os.PathLike[str],
    ) -> None
```

**内部调用(库内):**
- [`Command._generate_template_variables`](scrapy_commands.md#sym-scrapy_commands_genspider.py-125)
- [`render_templatefile`](scrapy_utils.md#sym-scrapy_utils_template.py-14)

*来源: `scrapy/commands/genspider.py:144` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-172"></a>

### `Command._find_template` · method
```python
def _find_template(self, template: str) -> Path | None
```

*来源: `scrapy/commands/genspider.py:172` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-182"></a>

### `Command._list_templates` · method
```python
def _list_templates(self) -> None
```

*来源: `scrapy/commands/genspider.py:182` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-192"></a>

### `Command._spider_exists` · method
```python
def _spider_exists(self, name: str) -> bool
```

**内部调用(库内):**
- [`get_spider_loader`](scrapy.md#sym-scrapy_spiderloader.py-25)

*来源: `scrapy/commands/genspider.py:192` · 待生成*

---
<a id="sym-scrapy_commands_genspider.py-227"></a>

### `Command.templates_dir` · method
装饰器: `@property`
```python
def templates_dir(self) -> str
```

*来源: `scrapy/commands/genspider.py:227` · 待生成*

---

## `scrapy/commands/list.py`

<a id="sym-scrapy_commands_list.py-12"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/list.py:12` · 待生成*

---
<a id="sym-scrapy_commands_list.py-17"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/list.py:17` · 待生成*

---
<a id="sym-scrapy_commands_list.py-20"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`get_spider_loader`](scrapy.md#sym-scrapy_spiderloader.py-25)

*来源: `scrapy/commands/list.py:20` · 待生成*

---

## `scrapy/commands/parse.py`

<a id="sym-scrapy_commands_parse.py-38"></a>

### `Command` · class
```python
class Command(BaseRunSpiderCommand)
```

*来源: `scrapy/commands/parse.py:38` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-48"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/parse.py:48` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-51"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/parse.py:51` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-54"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/parse.py:54` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-124"></a>

### `Command.max_level` · method
装饰器: `@property`
```python
def max_level(self) -> int
```

*来源: `scrapy/commands/parse.py:124` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-132"></a>

### `Command.handle_exception` · method
```python
def handle_exception(self, _failure: Failure) -> None
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)

*来源: `scrapy/commands/parse.py:132` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-139"></a>

### `Command.iterate_spider_output` · method
装饰器: `@overload`
```python
def iterate_spider_output(
        self, result: AsyncGenerator[_T] | Coroutine[Any, Any, _T]
    ) -> Deferred[_T]
```

*来源: `scrapy/commands/parse.py:139` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-144"></a>

### `Command.iterate_spider_output` · method
装饰器: `@overload`
```python
def iterate_spider_output(self, result: _T) -> Iterable[Any]
```

*来源: `scrapy/commands/parse.py:144` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-146"></a>

### `Command.iterate_spider_output` · method
```python
def iterate_spider_output(self, result: Any) -> Iterable[Any] | Deferred[Any]
```

**内部调用(库内):**
- [`collect_asyncgen`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-9)
- [`aiter_errback`](scrapy_utils.md#sym-scrapy_utils_defer.py-364)

*来源: `scrapy/commands/parse.py:146` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-158"></a>

### `Command.add_items` · method
```python
def add_items(self, lvl: int, new_items: list[Any]) -> None
```

*来源: `scrapy/commands/parse.py:158` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-162"></a>

### `Command.add_requests` · method
```python
def add_requests(self, lvl: int, new_reqs: list[Request]) -> None
```

*来源: `scrapy/commands/parse.py:162` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-166"></a>

### `Command.print_items` · method
```python
def print_items(self, lvl: int | None = None, colour: bool = True) -> None
```

**内部调用(库内):**
- [`pprint`](scrapy_utils.md#sym-scrapy_utils_display.py-50)

*来源: `scrapy/commands/parse.py:166` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-175"></a>

### `Command.print_requests` · method
```python
def print_requests(self, lvl: int | None = None, colour: bool = True) -> None
```

**内部调用(库内):**
- [`pprint`](scrapy_utils.md#sym-scrapy_utils_display.py-50)

*来源: `scrapy/commands/parse.py:175` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-186"></a>

### `Command.print_results` · method
```python
def print_results(self, opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`Command.print_items`](scrapy_commands.md#sym-scrapy_commands_parse.py-166)
- [`Command.print_requests`](scrapy_commands.md#sym-scrapy_commands_parse.py-175)

*来源: `scrapy/commands/parse.py:186` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-203"></a>

### `Command._get_items_and_requests` · method
```python
def _get_items_and_requests(
        self,
        spider_output: Iterable[Any],
        opts: argparse.Namespace,
        depth: int,
        spider: Spider,
        callback: CallbackT,
    ) -> tuple[list[Any], list[Request], argparse.Namespace, int, Spider, CallbackT]
```

*来源: `scrapy/commands/parse.py:203` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-219"></a>

### `Command.run_callback` · method
```python
def run_callback(
        self,
        response: Response,
        callback: CallbackT,
        cb_kwargs: dict[str, Any] | None = None,
    ) -> Deferred[Any]
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/commands/parse.py:219` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-230"></a>

### `Command.get_callback_from_rules` · method
```python
def get_callback_from_rules(
        self, spider: Spider, response: Response
    ) -> CallbackT | str | None
```

**内部调用(库内):**
- [`LxmlLinkExtractor.matches`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-237)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/commands/parse.py:230` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-245"></a>

### `Command.set_spidercls` · method
```python
def set_spidercls(self, url: str, opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)
- [`Command.prepare_request`](scrapy_commands.md#sym-scrapy_commands_parse.py-340)

*来源: `scrapy/commands/parse.py:245` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-260"></a>

### `Command.start` · method
```python
async def start(spider: Spider) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`Command.prepare_request`](scrapy_commands.md#sym-scrapy_commands_parse.py-340)
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/commands/parse.py:260` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-266"></a>

### `Command.start_parsing` · method
```python
def start_parsing(self, url: str, opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`Command.start`](scrapy_commands.md#sym-scrapy_commands_parse.py-260)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/commands/parse.py:266` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-276"></a>

### `Command.scraped_data` · method
```python
def scraped_data(
        self,
        args: tuple[
            list[Any], list[Request], argparse.Namespace, int, Spider, CallbackT
        ],
    ) -> list[Any]
```

**内部调用(库内):**
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`Command.add_items`](scrapy_commands.md#sym-scrapy_commands_parse.py-158)
- [`Command.add_requests`](scrapy_commands.md#sym-scrapy_commands_parse.py-162)

*来源: `scrapy/commands/parse.py:276` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-305"></a>

### `Command._get_callback` · method
```python
def _get_callback(
        self,
        *,
        spider: Spider,
        opts: argparse.Namespace,
        response: Response | None = None,
    ) -> CallbackT
```

**内部调用(库内):**
- [`Command.get_callback_from_rules`](scrapy_commands.md#sym-scrapy_commands_parse.py-230)

*来源: `scrapy/commands/parse.py:305` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-340"></a>

### `Command.prepare_request` · method
```python
def prepare_request(
        self, spider: Spider, request: Request, opts: argparse.Namespace
    ) -> Request
```

**内部调用(库内):**
- [`Command._get_callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-305)
- [`Command.run_callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-219)

*来源: `scrapy/commands/parse.py:340` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-343"></a>

### `Command.callback` · method
```python
def callback(response: Response, **cb_kwargs: Any) -> Deferred[list[Any]]
```

**内部调用(库内):**
- [`Command._get_callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-305)
- [`Command.run_callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-219)

*来源: `scrapy/commands/parse.py:343` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-374"></a>

### `Command.process_options` · method
```python
def process_options(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`Command.process_request_meta`](scrapy_commands.md#sym-scrapy_commands_parse.py-380)
- [`Command.process_request_cb_kwargs`](scrapy_commands.md#sym-scrapy_commands_parse.py-391)

*来源: `scrapy/commands/parse.py:374` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-380"></a>

### `Command.process_request_meta` · method
```python
def process_request_meta(self, opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。

*来源: `scrapy/commands/parse.py:380` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-391"></a>

### `Command.process_request_cb_kwargs` · method
```python
def process_request_cb_kwargs(self, opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。

*来源: `scrapy/commands/parse.py:391` · 待生成*

---
<a id="sym-scrapy_commands_parse.py-402"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`Command.set_spidercls`](scrapy_commands.md#sym-scrapy_commands_parse.py-245)
- [`Command.start_parsing`](scrapy_commands.md#sym-scrapy_commands_parse.py-266)
- [`Command.print_results`](scrapy_commands.md#sym-scrapy_commands_parse.py-186)

*来源: `scrapy/commands/parse.py:402` · 待生成*

---

## `scrapy/commands/runspider.py`

<a id="sym-scrapy_commands_runspider.py-19"></a>

### `_import_file` · func
```python
def _import_file(filepath: str | PathLike[str]) -> ModuleType
```

*来源: `scrapy/commands/runspider.py:19` · 待生成*

---
<a id="sym-scrapy_commands_runspider.py-32"></a>

### `Command` · class
```python
class Command(BaseRunSpiderCommand)
```

*来源: `scrapy/commands/runspider.py:32` · 待生成*

---
<a id="sym-scrapy_commands_runspider.py-37"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/runspider.py:37` · 待生成*

---
<a id="sym-scrapy_commands_runspider.py-40"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/runspider.py:40` · 待生成*

---
<a id="sym-scrapy_commands_runspider.py-43"></a>

### `Command.long_desc` · method
```python
def long_desc(self) -> str
```

*来源: `scrapy/commands/runspider.py:43` · 待生成*

---
<a id="sym-scrapy_commands_runspider.py-46"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。
- [`_import_file`](scrapy_commands.md#sym-scrapy_commands_runspider.py-19)
- [`iter_spider_classes`](scrapy_utils.md#sym-scrapy_utils_spider.py-50)

*来源: `scrapy/commands/runspider.py:46` · 待生成*

---

## `scrapy/commands/settings.py`

<a id="sym-scrapy_commands_settings.py-9"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/settings.py:9` · 待生成*

---
<a id="sym-scrapy_commands_settings.py-13"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/settings.py:13` · 待生成*

---
<a id="sym-scrapy_commands_settings.py-16"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/settings.py:16` · 待生成*

---
<a id="sym-scrapy_commands_settings.py-19"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/settings.py:19` · 待生成*

---
<a id="sym-scrapy_commands_settings.py-49"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`BaseSettings.copy_to_dict`](scrapy_settings.md#sym-scrapy_settings___init__.py-656)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/commands/settings.py:49` · 待生成*

---

## `scrapy/commands/shell.py`

<a id="sym-scrapy_commands_shell.py-27"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/shell.py:27` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-34"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/shell.py:34` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-37"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/shell.py:37` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-40"></a>

### `Command.long_desc` · method
```python
def long_desc(self) -> str
```

*来源: `scrapy/commands/shell.py:40` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-46"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: ArgumentParser) -> None
```

*来源: `scrapy/commands/shell.py:46` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-62"></a>

### `Command.update_vars` · method
```python
def update_vars(self, vars: dict[str, Any]) -> None
```

*来源: `scrapy/commands/shell.py:62` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-67"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: Namespace) -> None
```

**内部调用(库内):**
- [`guess_scheme`](scrapy_utils.md#sym-scrapy_utils_url.py-100)
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)
- [`Crawler._apply_settings`](scrapy.md#sym-scrapy_crawler.py-94) — 应用爬虫设置并初始化相关组件。
- [`Command._init_with_reactor`](scrapy_commands.md#sym-scrapy_commands_shell.py-97)
- [`Command._init_without_reactor`](scrapy_commands.md#sym-scrapy_commands_shell.py-103)
- [`Command._get_reactorless_loop`](scrapy_commands.md#sym-scrapy_commands_shell.py-120)
- [`Shell`](scrapy.md#sym-scrapy_shell.py-94)

*来源: `scrapy/commands/shell.py:67` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-97"></a>

### `Command._init_with_reactor` · method
```python
def _init_with_reactor(self, crawler: Crawler) -> None
```

**内部调用(库内):**
- [`Crawler._create_engine`](scrapy.md#sym-scrapy_crawler.py-233) — 创建并返回一个 ExecutionEngine 实例用于执行爬虫引擎。
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`ExecutionEngine.start_async`](scrapy_core.md#sym-scrapy_core_engine.py-176)
- [`Command._start_crawler_thread`](scrapy_commands.md#sym-scrapy_commands_shell.py-127)

*来源: `scrapy/commands/shell.py:97` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-103"></a>

### `Command._init_without_reactor` · method
```python
def _init_without_reactor(self, crawler: Crawler) -> None
```

**内部调用(库内):**
- [`Command._get_reactorless_loop`](scrapy_commands.md#sym-scrapy_commands_shell.py-120)
- [`Command._start_crawler_thread`](scrapy_commands.md#sym-scrapy_commands_shell.py-127)
- [`Crawler._create_engine`](scrapy.md#sym-scrapy_crawler.py-233) — 创建并返回一个 ExecutionEngine 实例用于执行爬虫引擎。
- [`ExecutionEngine.start_async`](scrapy_core.md#sym-scrapy_core_engine.py-176)
- [`Command._init_engine`](scrapy_commands.md#sym-scrapy_commands_shell.py-108)

*来源: `scrapy/commands/shell.py:103` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-108"></a>

### `Command._init_engine` · method
```python
async def _init_engine() -> None
```

**内部调用(库内):**
- [`Crawler._create_engine`](scrapy.md#sym-scrapy_crawler.py-233) — 创建并返回一个 ExecutionEngine 实例用于执行爬虫引擎。
- [`ExecutionEngine.start_async`](scrapy_core.md#sym-scrapy_core_engine.py-176)

*来源: `scrapy/commands/shell.py:108` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-120"></a>

### `Command._get_reactorless_loop` · method
```python
def _get_reactorless_loop(self) -> asyncio.AbstractEventLoop
```

*来源: `scrapy/commands/shell.py:120` · 待生成*

---
<a id="sym-scrapy_commands_shell.py-127"></a>

### `Command._start_crawler_thread` · method
```python
def _start_crawler_thread(self) -> None
```

*来源: `scrapy/commands/shell.py:127` · 待生成*

---

## `scrapy/commands/startproject.py`

<a id="sym-scrapy_commands_startproject.py-30"></a>

### `_make_writable` · func
```python
def _make_writable(path: Path) -> None
```

*来源: `scrapy/commands/startproject.py:30` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-35"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/startproject.py:35` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-39"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/startproject.py:39` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-42"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/startproject.py:42` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-45"></a>

### `Command._is_valid_name` · method
```python
def _is_valid_name(self, project_name: str) -> bool
```

**内部调用(库内):**
- [`ReactorImportHook.find_spec`](scrapy_utils.md#sym-scrapy_utils_reactorless.py-36)
- [`Command._module_exists`](scrapy_commands.md#sym-scrapy_commands_startproject.py-46)

*来源: `scrapy/commands/startproject.py:45` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-46"></a>

### `Command._module_exists` · method
```python
def _module_exists(module_name: str) -> bool
```

**内部调用(库内):**
- [`ReactorImportHook.find_spec`](scrapy_utils.md#sym-scrapy_utils_reactorless.py-36)

*来源: `scrapy/commands/startproject.py:46` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-61"></a>

### `Command._copytree` · method
```python
def _copytree(self, src: Path, dst: Path) -> None
```

**内部调用(库内):**
- [`_make_writable`](scrapy_commands.md#sym-scrapy_commands_startproject.py-30)

*来源: `scrapy/commands/startproject.py:61` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-92"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`Command._is_valid_name`](scrapy_commands.md#sym-scrapy_commands_startproject.py-45)
- [`Command._copytree`](scrapy_commands.md#sym-scrapy_commands_startproject.py-61)
- [`render_templatefile`](scrapy_utils.md#sym-scrapy_utils_template.py-14)
- [`string_camelcase`](scrapy_utils.md#sym-scrapy_utils_template.py-31)

*来源: `scrapy/commands/startproject.py:92` · 待生成*

---
<a id="sym-scrapy_commands_startproject.py-134"></a>

### `Command.templates_dir` · method
装饰器: `@property`
```python
def templates_dir(self) -> str
```

*来源: `scrapy/commands/startproject.py:134` · 待生成*

---

## `scrapy/commands/version.py`

<a id="sym-scrapy_commands_version.py-9"></a>

### `Command` · class
```python
class Command(ScrapyCommand)
```

*来源: `scrapy/commands/version.py:9` · 待生成*

---
<a id="sym-scrapy_commands_version.py-13"></a>

### `Command.syntax` · method
```python
def syntax(self) -> str
```

*来源: `scrapy/commands/version.py:13` · 待生成*

---
<a id="sym-scrapy_commands_version.py-16"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/version.py:16` · 待生成*

---
<a id="sym-scrapy_commands_version.py-19"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/version.py:19` · 待生成*

---
<a id="sym-scrapy_commands_version.py-29"></a>

### `Command.run` · method
```python
def run(self, args: list[str], opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`get_versions`](scrapy_utils.md#sym-scrapy_utils_versions.py-28)

*来源: `scrapy/commands/version.py:29` · 待生成*

---

## `scrapy/commands/view.py`

<a id="sym-scrapy_commands_view.py-11"></a>

### `Command` · class
```python
class Command(fetch.Command)
```

*来源: `scrapy/commands/view.py:11` · 待生成*

---
<a id="sym-scrapy_commands_view.py-12"></a>

### `Command.short_desc` · method
```python
def short_desc(self) -> str
```

*来源: `scrapy/commands/view.py:12` · 待生成*

---
<a id="sym-scrapy_commands_view.py-15"></a>

### `Command.long_desc` · method
```python
def long_desc(self) -> str
```

*来源: `scrapy/commands/view.py:15` · 待生成*

---
<a id="sym-scrapy_commands_view.py-20"></a>

### `Command.add_options` · method
```python
def add_options(self, parser: argparse.ArgumentParser) -> None
```

*来源: `scrapy/commands/view.py:20` · 待生成*

---
<a id="sym-scrapy_commands_view.py-24"></a>

### `Command._print_response` · method
```python
def _print_response(self, response: Response, opts: argparse.Namespace) -> None
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`open_in_browser`](scrapy_utils.md#sym-scrapy_utils_response.py-74)

*来源: `scrapy/commands/view.py:24` · 待生成*

---