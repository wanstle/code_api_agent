# API 参考:`scrapy/utils`

## `scrapy/utils/_compression.py`

<a id="sym-scrapy_utils__compression.py-18"></a>

### `_DecompressionMaxSizeExceeded` · class
```python
class _DecompressionMaxSizeExceeded(ValueError)
```

*来源: `scrapy/utils/_compression.py:18` · 待生成*

---
<a id="sym-scrapy_utils__compression.py-19"></a>

### `_DecompressionMaxSizeExceeded.__init__` · method
```python
def __init__(self, decompressed_size: int, max_size: int) -> None
```

*来源: `scrapy/utils/_compression.py:19` · 待生成*

---
<a id="sym-scrapy_utils__compression.py-23"></a>

### `_DecompressionMaxSizeExceeded.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/utils/_compression.py:23` · 待生成*

---
<a id="sym-scrapy_utils__compression.py-31"></a>

### `_check_max_size` · func
```python
def _check_max_size(decompressed_size: int, max_size: int) -> None
```

**内部调用(库内):**
- [`_DecompressionMaxSizeExceeded`](scrapy_utils.md#sym-scrapy_utils__compression.py-18)

*来源: `scrapy/utils/_compression.py:31` · 待生成*

---
<a id="sym-scrapy_utils__compression.py-36"></a>

### `_inflate` · func
```python
def _inflate(data: bytes, *, max_size: int = 0) -> bytes
```

**内部调用(库内):**
- [`_check_max_size`](scrapy_utils.md#sym-scrapy_utils__compression.py-31)

*来源: `scrapy/utils/_compression.py:36` · 待生成*

---
<a id="sym-scrapy_utils__compression.py-62"></a>

### `_unbrotli` · func
```python
def _unbrotli(data: bytes, *, max_size: int = 0) -> bytes
```

**内部调用(库内):**
- [`_check_max_size`](scrapy_utils.md#sym-scrapy_utils__compression.py-31)

*来源: `scrapy/utils/_compression.py:62` · 待生成*

---
<a id="sym-scrapy_utils__compression.py-79"></a>

### `_unzstd` · func
```python
def _unzstd(data: bytes, *, max_size: int = 0) -> bytes
```

**内部调用(库内):**
- [`_check_max_size`](scrapy_utils.md#sym-scrapy_utils__compression.py-31)

*来源: `scrapy/utils/_compression.py:79` · 待生成*

---

## `scrapy/utils/_download_handlers.py`

<a id="sym-scrapy_utils__download_handlers.py-41"></a>

### `NullCookieJar` · class
```python
class NullCookieJar(CookieJar)
```

*来源: `scrapy/utils/_download_handlers.py:41` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-44"></a>

### `NullCookieJar.extract_cookies` · method
```python
def extract_cookies(self, response: HTTPResponse, request: ULRequest) -> None
```

*来源: `scrapy/utils/_download_handlers.py:44` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-47"></a>

### `NullCookieJar.set_cookie` · method
```python
def set_cookie(self, cookie: Cookie) -> None
```

*来源: `scrapy/utils/_download_handlers.py:47` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-52"></a>

### `wrap_twisted_exceptions` · func
装饰器: `@contextmanager`
```python
def wrap_twisted_exceptions() -> Iterator[None]
```

**内部调用(库内):**
- [`UnsupportedURLSchemeError`](scrapy.md#sym-scrapy_exceptions.py-86) — `UnsupportedURLSchemeError` 异常类用于表示请求的 URL 使用了不支持的协议方案。
- [`DownloadCancelledError`](scrapy.md#sym-scrapy_exceptions.py-74) — `DownloadCancelledError` 异常用于表示下载过程中被取消的情况。
- [`DownloadConnectionRefusedError`](scrapy.md#sym-scrapy_exceptions.py-62) — `DownloadConnectionRefusedError` 类代表在下载过程中连接被拒绝时抛出的异常，用于处理网络连接失败的错误情况。
- [`CannotResolveHostError`](scrapy.md#sym-scrapy_exceptions.py-66) — CannotResolveHostError 类用于表示在爬取过程中无法解析主机名的错误，通常由网络请求失败引发。
- [`DownloadFailedError`](scrapy.md#sym-scrapy_exceptions.py-78) — `DownloadFailedError` 是一个异常类，用于表示下载失败时抛出的错误。
- [`DownloadTimeoutError`](scrapy.md#sym-scrapy_exceptions.py-70) — `DownloadTimeoutError` 类代表在下载过程中发生超时错误的异常类型，用于标识网络请求因超时而失败的情况。

*来源: `scrapy/utils/_download_handlers.py:52` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-70"></a>

### `check_stop_download` · func
```python
def check_stop_download(
    signal: object, crawler: Crawler, request: Request, **kwargs: Any
) -> StopDownload | None
```

*来源: `scrapy/utils/_download_handlers.py:70` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-94"></a>

### `make_response` · func
```python
def make_response(
    url: str,
    status: int,
    headers: Headers,
    body: bytes = b"",
    flags: list[str] | None = None,
    certificate: Any = None,
    ip_address: IPv4Address | IPv6Address | None = None,
    protocol: str | None = None,
    stop_download: StopDownload | None = None,
) -> Response
```

**内部调用(库内):**
- [`ResponseTypes.from_args`](scrapy.md#sym-scrapy_responsetypes.py-124)

*来源: `scrapy/utils/_download_handlers.py:94` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-124"></a>

### `get_maxsize_msg` · func
```python
def get_maxsize_msg(size: int, limit: int, request: Request, *, expected: bool) -> str
```

*来源: `scrapy/utils/_download_handlers.py:124` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-132"></a>

### `get_warnsize_msg` · func
```python
def get_warnsize_msg(size: int, limit: int, request: Request, *, expected: bool) -> str
```

*来源: `scrapy/utils/_download_handlers.py:132` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-140"></a>

### `get_dataloss_msg` · func
```python
def get_dataloss_msg(url: str) -> str
```

*来源: `scrapy/utils/_download_handlers.py:140` · 待生成*

---
<a id="sym-scrapy_utils__download_handlers.py-148"></a>

### `normalize_bind_address` · func
```python
def normalize_bind_address(
    value: str | tuple[str, int] | None,
) -> tuple[str, int] | None
```

*来源: `scrapy/utils/_download_handlers.py:148` · 待生成*

---

## `scrapy/utils/asyncgen.py`

<a id="sym-scrapy_utils_asyncgen.py-9"></a>

### `collect_asyncgen` · func
```python
async def collect_asyncgen(result: AsyncIterator[_T]) -> list[_T]
```

*来源: `scrapy/utils/asyncgen.py:9` · 待生成*

---
<a id="sym-scrapy_utils_asyncgen.py-13"></a>

### `as_async_generator` · func
```python
async def as_async_generator(
    it: Iterable[_T] | AsyncIterator[_T],
) -> AsyncGenerator[_T]
```

*来源: `scrapy/utils/asyncgen.py:13` · 待生成*

---

## `scrapy/utils/asyncio.py`

<a id="sym-scrapy_utils_asyncio.py-34"></a>

### `is_asyncio_available` · func
```python
def is_asyncio_available() -> bool
```

**内部调用(库内):**
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)
- [`is_asyncio_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-220)

*来源: `scrapy/utils/asyncio.py:34` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-95"></a>

### `_parallel_asyncio` · func
```python
async def _parallel_asyncio(
    iterable: Iterable[_T] | AsyncIterator[_T],
    count: int,
    callable_: Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]],
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> None
```

**内部调用(库内):**
- [`as_async_generator`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-13)
- [`fill_queue`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-122)
- [`worker`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-112)
- [`CallLaterOnce.wait`](scrapy_utils.md#sym-scrapy_utils_reactor.py-86)

*来源: `scrapy/utils/asyncio.py:95` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-112"></a>

### `worker` · func
```python
async def worker() -> None
```

*来源: `scrapy/utils/asyncio.py:112` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-122"></a>

### `fill_queue` · func
```python
async def fill_queue() -> None
```

**内部调用(库内):**
- [`as_async_generator`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-13)

*来源: `scrapy/utils/asyncio.py:122` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-133"></a>

### `AsyncioLoopingCall` · class
```python
class AsyncioLoopingCall
```

*来源: `scrapy/utils/asyncio.py:133` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-147"></a>

### `AsyncioLoopingCall.__init__` · method
```python
def __init__(self, func: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs)
```

*来源: `scrapy/utils/asyncio.py:147` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-156"></a>

### `AsyncioLoopingCall.running` · method
装饰器: `@property`
```python
def running(self) -> bool
```

*来源: `scrapy/utils/asyncio.py:156` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-159"></a>

### `AsyncioLoopingCall.start` · method
```python
def start(self, interval: float, now: bool = True) -> None
```

**内部调用(库内):**
- [`AsyncioLoopingCall._call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-202)
- [`AsyncioLoopingCall._loop`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-189)

*来源: `scrapy/utils/asyncio.py:159` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-181"></a>

### `AsyncioLoopingCall._to_sleep` · method
```python
def _to_sleep(self) -> float
```

*来源: `scrapy/utils/asyncio.py:181` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-189"></a>

### `AsyncioLoopingCall._loop` · method
```python
async def _loop(self) -> None
```

**内部调用(库内):**
- [`AsyncioLoopingCall._to_sleep`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-181)
- [`AsyncioLoopingCall._call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-202)

*来源: `scrapy/utils/asyncio.py:189` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-195"></a>

### `AsyncioLoopingCall.stop` · method
```python
def stop(self) -> None
```

**内部调用(库内):**
- [`CallLaterResult.cancel`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-283)

*来源: `scrapy/utils/asyncio.py:195` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-202"></a>

### `AsyncioLoopingCall._call` · method
```python
def _call(self) -> None
```

**内部调用(库内):**
- [`AsyncioLoopingCall.stop`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-195)

*来源: `scrapy/utils/asyncio.py:202` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-217"></a>

### `create_looping_call` · func
```python
def create_looping_call(
    func: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs
) -> AsyncioLoopingCall | LoopingCall
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`AsyncioLoopingCall`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-133)

*来源: `scrapy/utils/asyncio.py:217` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-234"></a>

### `call_later` · func
```python
def call_later(
    delay: float, func: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts]
) -> CallLaterResult
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`CallLaterResult.from_asyncio`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-270)
- [`CallLaterResult.from_twisted`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-277)

*来源: `scrapy/utils/asyncio.py:234` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-254"></a>

### `CallLaterResult` · class
```python
class CallLaterResult
```

*来源: `scrapy/utils/asyncio.py:254` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-270"></a>

### `CallLaterResult.from_asyncio` · method
装饰器: `@classmethod`
```python
def from_asyncio(cls, timer_handle: asyncio.TimerHandle) -> Self
```

*来源: `scrapy/utils/asyncio.py:270` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-277"></a>

### `CallLaterResult.from_twisted` · method
装饰器: `@classmethod`
```python
def from_twisted(cls, delayed_call: DelayedCall) -> Self
```

*来源: `scrapy/utils/asyncio.py:277` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-283"></a>

### `CallLaterResult.cancel` · method
```python
def cancel(self) -> None
```

*来源: `scrapy/utils/asyncio.py:283` · 待生成*

---
<a id="sym-scrapy_utils_asyncio.py-296"></a>

### `run_in_thread` · func
```python
async def run_in_thread(
    func: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs
) -> _T
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/utils/asyncio.py:296` · 待生成*

---

## `scrapy/utils/benchserver.py`

<a id="sym-scrapy_utils_benchserver.py-9"></a>

### `Root` · class
```python
class Root(Resource)
```

*来源: `scrapy/utils/benchserver.py:9` · 待生成*

---
<a id="sym-scrapy_utils_benchserver.py-12"></a>

### `Root.getChild` · method
```python
def getChild(self, path: str, request: Request) -> Resource
```

*来源: `scrapy/utils/benchserver.py:12` · 待生成*

---
<a id="sym-scrapy_utils_benchserver.py-15"></a>

### `Root.render` · method
```python
def render(self, request: Request) -> bytes
```

**内部调用(库内):**
- [`_getarg`](scrapy_utils.md#sym-scrapy_utils_benchserver.py-30)

*来源: `scrapy/utils/benchserver.py:15` · 待生成*

---
<a id="sym-scrapy_utils_benchserver.py-30"></a>

### `_getarg` · func
```python
def _getarg(
    request: Request, name: bytes, default: Any = None, type_: type = str
) -> Any
```

*来源: `scrapy/utils/benchserver.py:30` · 待生成*

---
<a id="sym-scrapy_utils_benchserver.py-43"></a>

### `_print_listening` · func
```python
def _print_listening() -> None
```

*来源: `scrapy/utils/benchserver.py:43` · 待生成*

---

## `scrapy/utils/boto.py`

<a id="sym-scrapy_utils_boto.py-4"></a>

### `is_botocore_available` · func
```python
def is_botocore_available() -> bool
```

*来源: `scrapy/utils/boto.py:4` · 待生成*

---

## `scrapy/utils/conf.py`

<a id="sym-scrapy_utils_conf.py-20"></a>

### `build_component_list` · func
```python
def build_component_list(
    compdict: MutableMapping[Any, Any],
    *,
    convert: Callable[[Any], Any] = update_classpath,
) -> list[Any]
```

**内部调用(库内):**
- [`BaseSettings`](scrapy_settings.md#sym-scrapy_settings___init__.py-79)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)
- [`_check_components`](scrapy_utils.md#sym-scrapy_utils_conf.py-28)
- [`_validate_values`](scrapy_utils.md#sym-scrapy_utils_conf.py-52)
- [`_map_keys`](scrapy_utils.md#sym-scrapy_utils_conf.py-35)

*来源: `scrapy/utils/conf.py:20` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-28"></a>

### `_check_components` · func
```python
def _check_components(complist: Collection[Any]) -> None
```

*来源: `scrapy/utils/conf.py:28` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-35"></a>

### `_map_keys` · func
```python
def _map_keys(compdict: Mapping[Any, Any]) -> BaseSettings | dict[Any, Any]
```

**内部调用(库内):**
- [`BaseSettings`](scrapy_settings.md#sym-scrapy_settings___init__.py-79)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)
- [`_check_components`](scrapy_utils.md#sym-scrapy_utils_conf.py-28)

*来源: `scrapy/utils/conf.py:35` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-52"></a>

### `_validate_values` · func
```python
def _validate_values(compdict: Mapping[Any, Any]) -> None
```

*来源: `scrapy/utils/conf.py:52` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-66"></a>

### `arglist_to_dict` · func
```python
def arglist_to_dict(arglist: list[str]) -> dict[str, str]
```

*来源: `scrapy/utils/conf.py:66` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-73"></a>

### `closest_scrapy_cfg` · func
```python
def closest_scrapy_cfg(
    path: str | os.PathLike[str] = ".",
    prevpath: str | os.PathLike[str] | None = None,
) -> str
```

*来源: `scrapy/utils/conf.py:73` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-89"></a>

### `init_env` · func
```python
def init_env(project: str = "default", set_syspath: bool = True) -> None
```

**内部调用(库内):**
- [`get_config`](scrapy_utils.md#sym-scrapy_utils_conf.py-104)
- [`closest_scrapy_cfg`](scrapy_utils.md#sym-scrapy_utils_conf.py-73)

*来源: `scrapy/utils/conf.py:89` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-104"></a>

### `get_config` · func
```python
def get_config(use_closest: bool = True) -> ConfigParser
```

**内部调用(库内):**
- [`get_sources`](scrapy_utils.md#sym-scrapy_utils_conf.py-112)

*来源: `scrapy/utils/conf.py:104` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-112"></a>

### `get_sources` · func
```python
def get_sources(use_closest: bool = True) -> list[str]
```

**内部调用(库内):**
- [`closest_scrapy_cfg`](scrapy_utils.md#sym-scrapy_utils_conf.py-73)

*来源: `scrapy/utils/conf.py:112` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-127"></a>

### `feed_complete_default_values_from_settings` · func
```python
def feed_complete_default_values_from_settings(
    feed: dict[str, Any], settings: BaseSettings
) -> dict[str, Any]
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`BaseSettings.getdictorlist`](scrapy_settings.md#sym-scrapy_settings___init__.py-270)

*来源: `scrapy/utils/conf.py:127` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-144"></a>

### `feed_process_params_from_cli` · func
```python
def feed_process_params_from_cli(
    settings: BaseSettings,
    output: list[str],
    *,
    overwrite_output: list[str] | None = None,
) -> dict[str, dict[str, Any]]
```

**内部调用(库内):**
- [`BaseSettings.getwithbase`](scrapy_settings.md#sym-scrapy_settings___init__.py-319)
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。
- [`check_valid_format`](scrapy_utils.md#sym-scrapy_utils_conf.py-159)
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)

*来源: `scrapy/utils/conf.py:144` · 待生成*

---
<a id="sym-scrapy_utils_conf.py-159"></a>

### `check_valid_format` · func
```python
def check_valid_format(output_format: str) -> None
```

**内部调用(库内):**
- [`UsageError`](scrapy.md#sym-scrapy_exceptions.py-108) — `UsageError` 类用于表示 Scrapy 命令行工具中用户输入错误的情况，通常在命令使用不当或参数不正确时抛出。

*来源: `scrapy/utils/conf.py:159` · 待生成*

---

## `scrapy/utils/console.py`

<a id="sym-scrapy_utils_console.py-15"></a>

### `_embed_ipython_shell` · func
```python
def _embed_ipython_shell(
    namespace: dict[str, Any] | None = None, banner: str = ""
) -> EmbedFuncT
```

*来源: `scrapy/utils/console.py:15` · 待生成*

---
<a id="sym-scrapy_utils_console.py-31"></a>

### `wrapper` · func
装饰器: `@wraps(_embed_ipython_shell)`
```python
def wrapper(namespace: dict[str, Any] = namespace or {}, banner: str = "") -> None
```

*来源: `scrapy/utils/console.py:31` · 待生成*

---
<a id="sym-scrapy_utils_console.py-46"></a>

### `_embed_bpython_shell` · func
```python
def _embed_bpython_shell(
    namespace: dict[str, Any] | None = None, banner: str = ""
) -> EmbedFuncT
```

*来源: `scrapy/utils/console.py:46` · 待生成*

---
<a id="sym-scrapy_utils_console.py-53"></a>

### `wrapper` · func
装饰器: `@wraps(_embed_bpython_shell)`
```python
def wrapper(namespace: dict[str, Any] = namespace or {}, banner: str = "") -> None
```

*来源: `scrapy/utils/console.py:53` · 待生成*

---
<a id="sym-scrapy_utils_console.py-59"></a>

### `_embed_ptpython_shell` · func
```python
def _embed_ptpython_shell(
    namespace: dict[str, Any] | None = None, banner: str = ""
) -> EmbedFuncT
```

*来源: `scrapy/utils/console.py:59` · 待生成*

---
<a id="sym-scrapy_utils_console.py-66"></a>

### `wrapper` · func
装饰器: `@wraps(_embed_ptpython_shell)`
```python
def wrapper(namespace: dict[str, Any] = namespace or {}, banner: str = "") -> None
```

*来源: `scrapy/utils/console.py:66` · 待生成*

---
<a id="sym-scrapy_utils_console.py-73"></a>

### `_embed_standard_shell` · func
```python
def _embed_standard_shell(
    namespace: dict[str, Any] | None = None, banner: str = ""
) -> EmbedFuncT
```

*来源: `scrapy/utils/console.py:73` · 待生成*

---
<a id="sym-scrapy_utils_console.py-87"></a>

### `wrapper` · func
装饰器: `@wraps(_embed_standard_shell)`
```python
def wrapper(namespace: dict[str, Any] = namespace or {}, banner: str = "") -> None
```

*来源: `scrapy/utils/console.py:87` · 待生成*

---
<a id="sym-scrapy_utils_console.py-101"></a>

### `get_shell_embed_func` · func
```python
def get_shell_embed_func(
    shells: Iterable[str] | None = None, known_shells: KnownShellsT | None = None
) -> EmbedFuncT | None
```

*来源: `scrapy/utils/console.py:101` · 待生成*

---
<a id="sym-scrapy_utils_console.py-122"></a>

### `start_python_console` · func
```python
def start_python_console(
    namespace: dict[str, Any] | None = None,
    banner: str = "",
    shells: Iterable[str] | None = None,
) -> None
```

**内部调用(库内):**
- [`get_shell_embed_func`](scrapy_utils.md#sym-scrapy_utils_console.py-101)

*来源: `scrapy/utils/console.py:122` · 待生成*

---

## `scrapy/utils/curl.py`

<a id="sym-scrapy_utils_curl.py-16"></a>

### `DataAction` · class
```python
class DataAction(argparse.Action)
```

*来源: `scrapy/utils/curl.py:16` · 待生成*

---
<a id="sym-scrapy_utils_curl.py-17"></a>

### `DataAction.__call__` · method
```python
def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = None,
    ) -> None
```

*来源: `scrapy/utils/curl.py:17` · 待生成*

---
<a id="sym-scrapy_utils_curl.py-29"></a>

### `CurlParser` · class
```python
class CurlParser(argparse.ArgumentParser)
```

*来源: `scrapy/utils/curl.py:29` · 待生成*

---
<a id="sym-scrapy_utils_curl.py-30"></a>

### `CurlParser.error` · method
```python
def error(self, message: str) -> NoReturn
```

*来源: `scrapy/utils/curl.py:30` · 待生成*

---
<a id="sym-scrapy_utils_curl.py-57"></a>

### `_parse_headers_and_cookies` · func
```python
def _parse_headers_and_cookies(
    parsed_args: argparse.Namespace,
) -> tuple[list[tuple[str, bytes]], dict[str, str]]
```

*来源: `scrapy/utils/curl.py:57` · 待生成*

---
<a id="sym-scrapy_utils_curl.py-87"></a>

### `curl_to_request_kwargs` · func
```python
def curl_to_request_kwargs(
    curl_command: str, ignore_unknown_options: bool = True
) -> dict[str, Any]
```

**内部调用(库内):**
- [`_parse_headers_and_cookies`](scrapy_utils.md#sym-scrapy_utils_curl.py-57)

*来源: `scrapy/utils/curl.py:87` · 待生成*

---

## `scrapy/utils/datatypes.py`

<a id="sym-scrapy_utils_datatypes.py-31"></a>

### `CaselessDict` · class
```python
class CaselessDict(dict)
```

*来源: `scrapy/utils/datatypes.py:31` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-34"></a>

### `CaselessDict.__new__` · method
```python
def __new__(cls, *args: Any, **kwargs: Any) -> Self
```

*来源: `scrapy/utils/datatypes.py:34` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-47"></a>

### `CaselessDict.__init__` · method
```python
def __init__(
        self,
        seq: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    )
```

*来源: `scrapy/utils/datatypes.py:47` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-55"></a>

### `CaselessDict.__getitem__` · method
```python
def __getitem__(self, key: AnyStr) -> Any
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)

*来源: `scrapy/utils/datatypes.py:55` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-58"></a>

### `CaselessDict.__setitem__` · method
```python
def __setitem__(self, key: AnyStr, value: Any) -> None
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)
- [`CaselessDict.normvalue`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-78)

*来源: `scrapy/utils/datatypes.py:58` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-61"></a>

### `CaselessDict.__delitem__` · method
```python
def __delitem__(self, key: AnyStr) -> None
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)

*来源: `scrapy/utils/datatypes.py:61` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-64"></a>

### `CaselessDict.__contains__` · method
```python
def __contains__(self, key: AnyStr) -> bool
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)

*来源: `scrapy/utils/datatypes.py:64` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-69"></a>

### `CaselessDict.__copy__` · method
```python
def __copy__(self) -> Self
```

*来源: `scrapy/utils/datatypes.py:69` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-74"></a>

### `CaselessDict.normkey` · method
```python
def normkey(self, key: AnyStr) -> AnyStr
```

*来源: `scrapy/utils/datatypes.py:74` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-78"></a>

### `CaselessDict.normvalue` · method
```python
def normvalue(self, value: Any) -> Any
```

*来源: `scrapy/utils/datatypes.py:78` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-82"></a>

### `CaselessDict.get` · method
```python
def get(self, key: AnyStr, def_val: Any = None) -> Any
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)
- [`CaselessDict.normvalue`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-78)

*来源: `scrapy/utils/datatypes.py:82` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-85"></a>

### `CaselessDict.setdefault` · method
```python
def setdefault(self, key: AnyStr, def_val: Any = None) -> Any
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)
- [`CaselessDict.normvalue`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-78)

*来源: `scrapy/utils/datatypes.py:85` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-89"></a>

### `CaselessDict.update` · method
```python
def update(self, seq: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]]) -> None
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)
- [`CaselessDict.normvalue`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-78)

*来源: `scrapy/utils/datatypes.py:89` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-95"></a>

### `CaselessDict.fromkeys` · method
装饰器: `@classmethod`
```python
def fromkeys(cls, keys: Iterable[AnyStr], value: Any = None) -> Self
```

*来源: `scrapy/utils/datatypes.py:95` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-98"></a>

### `CaselessDict.pop` · method
```python
def pop(self, key: AnyStr, *args: Any) -> Any
```

**内部调用(库内):**
- [`CaselessDict.normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-74)

*来源: `scrapy/utils/datatypes.py:98` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-102"></a>

### `CaseInsensitiveDict` · class
```python
class CaseInsensitiveDict(collections.UserDict[str | bytes, Any])
```

*来源: `scrapy/utils/datatypes.py:102` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-107"></a>

### `CaseInsensitiveDict.__init__` · method
```python
def __init__(self, *args: Any, **kwargs: Any) -> None
```

*来源: `scrapy/utils/datatypes.py:107` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-111"></a>

### `CaseInsensitiveDict.__getitem__` · method
```python
def __getitem__(self, key: str | bytes) -> Any
```

**内部调用(库内):**
- [`CaseInsensitiveDict._normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-137)

*来源: `scrapy/utils/datatypes.py:111` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-115"></a>

### `CaseInsensitiveDict.__setitem__` · method
```python
def __setitem__(self, key: str | bytes, value: Any) -> None
```

**内部调用(库内):**
- [`CaseInsensitiveDict._normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-137)
- [`CaseInsensitiveDict._normvalue`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-140)

*来源: `scrapy/utils/datatypes.py:115` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-125"></a>

### `CaseInsensitiveDict.__delitem__` · method
```python
def __delitem__(self, key: str | bytes) -> None
```

**内部调用(库内):**
- [`CaseInsensitiveDict._normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-137)

*来源: `scrapy/utils/datatypes.py:125` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-130"></a>

### `CaseInsensitiveDict.__contains__` · method
```python
def __contains__(self, key: str | bytes) -> bool
```

**内部调用(库内):**
- [`CaseInsensitiveDict._normkey`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-137)

*来源: `scrapy/utils/datatypes.py:130` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-134"></a>

### `CaseInsensitiveDict.__repr__` · method
```python
def __repr__(self) -> str
```

*来源: `scrapy/utils/datatypes.py:134` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-137"></a>

### `CaseInsensitiveDict._normkey` · method
```python
def _normkey(self, key: str | bytes) -> str | bytes
```

*来源: `scrapy/utils/datatypes.py:137` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-140"></a>

### `CaseInsensitiveDict._normvalue` · method
```python
def _normvalue(self, value: Any) -> Any
```

*来源: `scrapy/utils/datatypes.py:140` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-144"></a>

### `LocalCache` · class
```python
class LocalCache(OrderedDict[_KT, _VT])
```

*来源: `scrapy/utils/datatypes.py:144` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-150"></a>

### `LocalCache.__init__` · method
```python
def __init__(self, limit: int | None = None)
```

*来源: `scrapy/utils/datatypes.py:150` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-154"></a>

### `LocalCache.__setitem__` · method
```python
def __setitem__(self, key: _KT, value: _VT) -> None
```

*来源: `scrapy/utils/datatypes.py:154` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-161"></a>

### `LocalWeakReferencedCache` · class
```python
class LocalWeakReferencedCache(weakref.WeakKeyDictionary[_KT, _VT | None])
```

*来源: `scrapy/utils/datatypes.py:161` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-173"></a>

### `LocalWeakReferencedCache.__init__` · method
```python
def __init__(self, limit: int | None = None)
```

**内部调用(库内):**
- [`LocalCache`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-144)

*来源: `scrapy/utils/datatypes.py:173` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-177"></a>

### `LocalWeakReferencedCache.__setitem__` · method
```python
def __setitem__(self, key: _KT, value: _VT | None) -> None
```

*来源: `scrapy/utils/datatypes.py:177` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-182"></a>

### `LocalWeakReferencedCache.__getitem__` · method
```python
def __getitem__(self, key: _KT) -> _VT | None
```

*来源: `scrapy/utils/datatypes.py:182` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-189"></a>

### `SequenceExclude` · class
```python
class SequenceExclude
```

*来源: `scrapy/utils/datatypes.py:189` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-192"></a>

### `SequenceExclude.__init__` · method
```python
def __init__(self, seq: Sequence[Any])
```

*来源: `scrapy/utils/datatypes.py:192` · 待生成*

---
<a id="sym-scrapy_utils_datatypes.py-195"></a>

### `SequenceExclude.__contains__` · method
```python
def __contains__(self, item: Any) -> bool
```

*来源: `scrapy/utils/datatypes.py:195` · 待生成*

---

## `scrapy/utils/decorators.py`

<a id="sym-scrapy_utils_decorators.py-22"></a>

### `deprecated` · func
```python
def deprecated(
    use_instead: Any = None,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]
```

**内部调用(库内):**
- [`deco`](scrapy_utils.md#sym-scrapy_utils_decorators.py-29)

*来源: `scrapy/utils/decorators.py:22` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-29"></a>

### `deco` · func
```python
def deco(func: Callable[_P, _T]) -> Callable[_P, _T]
```

*来源: `scrapy/utils/decorators.py:29` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-31"></a>

### `wrapped` · func
装饰器: `@wraps(func)`
```python
def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T
```

*来源: `scrapy/utils/decorators.py:31` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-46"></a>

### `defers` · func
```python
def defers(func: Callable[_P, _T]) -> Callable[_P, Deferred[_T]]
```

*来源: `scrapy/utils/decorators.py:46` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-55"></a>

### `wrapped` · func
装饰器: `@wraps(func)`
```python
def wrapped(*a: _P.args, **kw: _P.kwargs) -> Deferred[_T]
```

*来源: `scrapy/utils/decorators.py:55` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-61"></a>

### `inthread` · func
```python
def inthread(func: Callable[_P, _T]) -> Callable[_P, Deferred[_T]]
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/utils/decorators.py:61` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-70"></a>

### `wrapped` · func
装饰器: `@wraps(func)`
```python
def wrapped(*a: _P.args, **kw: _P.kwargs) -> Deferred[_T]
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/utils/decorators.py:70` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-77"></a>

### `_warn_spider_arg` · func
装饰器: `@overload`
```python
def _warn_spider_arg(
    func: Callable[_P, Coroutine[Any, Any, _T]],
) -> Callable[_P, Coroutine[Any, Any, _T]]
```

*来源: `scrapy/utils/decorators.py:77` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-83"></a>

### `_warn_spider_arg` · func
装饰器: `@overload`
```python
def _warn_spider_arg(
    func: Callable[_P, AsyncGenerator[_T]],
) -> Callable[_P, AsyncGenerator[_T]]
```

*来源: `scrapy/utils/decorators.py:83` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-89"></a>

### `_warn_spider_arg` · func
装饰器: `@overload`
```python
def _warn_spider_arg(func: Callable[_P, _T]) -> Callable[_P, _T]
```

*来源: `scrapy/utils/decorators.py:89` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-92"></a>

### `_warn_spider_arg` · func
```python
def _warn_spider_arg(
    func: Callable[_P, _T],
) -> (
    Callable[_P, _T]
| Callable[_P, Coroutine[Any, Any, _T]] |
| Callable[_P, AsyncGenerator[_T]]      |
)
```

**内部调用(库内):**
- [`check_args`](scrapy_utils.md#sym-scrapy_utils_decorators.py-103)

*来源: `scrapy/utils/decorators.py:92` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-103"></a>

### `check_args` · func
```python
def check_args(*args: _P.args, **kwargs: _P.kwargs) -> None
```

*来源: `scrapy/utils/decorators.py:103` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-116"></a>

### `async_inner` · func
装饰器: `@wraps(func)`
```python
async def async_inner(*args: _P.args, **kwargs: _P.kwargs) -> _T
```

**内部调用(库内):**
- [`check_args`](scrapy_utils.md#sym-scrapy_utils_decorators.py-103)

*来源: `scrapy/utils/decorators.py:116` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-125"></a>

### `asyncgen_inner` · func
装饰器: `@wraps(func)`
```python
async def asyncgen_inner(
            *args: _P.args, **kwargs: _P.kwargs
        ) -> AsyncGenerator[_T]
```

**内部调用(库内):**
- [`check_args`](scrapy_utils.md#sym-scrapy_utils_decorators.py-103)

*来源: `scrapy/utils/decorators.py:125` · 待生成*

---
<a id="sym-scrapy_utils_decorators.py-135"></a>

### `sync_inner` · func
装饰器: `@wraps(func)`
```python
def sync_inner(*args: _P.args, **kwargs: _P.kwargs) -> _T
```

**内部调用(库内):**
- [`check_args`](scrapy_utils.md#sym-scrapy_utils_decorators.py-103)

*来源: `scrapy/utils/decorators.py:135` · 待生成*

---

## `scrapy/utils/defer.py`

<a id="sym-scrapy_utils_defer.py-47"></a>

### `defer_fail` · func
```python
def defer_fail(_failure: Failure) -> Deferred[Any]
```

*来源: `scrapy/utils/defer.py:47` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-68"></a>

### `defer_succeed` · func
```python
def defer_succeed(result: _T) -> Deferred[_T]
```

*来源: `scrapy/utils/defer.py:68` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-89"></a>

### `_defer_sleep_async` · func
```python
async def _defer_sleep_async() -> None
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)

*来源: `scrapy/utils/defer.py:89` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-103"></a>

### `defer_result` · func
```python
def defer_result(result: Any) -> Deferred[Any]
```

*来源: `scrapy/utils/defer.py:103` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-126"></a>

### `mustbe_deferred` · func
装饰器: `@overload`
```python
def mustbe_deferred(
    f: Callable[_P, Deferred[_T]], *args: _P.args, **kw: _P.kwargs
) -> Deferred[_T]
```

*来源: `scrapy/utils/defer.py:126` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-132"></a>

### `mustbe_deferred` · func
装饰器: `@overload`
```python
def mustbe_deferred(
    f: Callable[_P, _T], *args: _P.args, **kw: _P.kwargs
) -> Deferred[_T]
```

*来源: `scrapy/utils/defer.py:132` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-137"></a>

### `mustbe_deferred` · func
```python
def mustbe_deferred(
    f: Callable[_P, Deferred[_T] | _T],
    *args: _P.args,
    **kw: _P.kwargs,
) -> Deferred[_T]
```

**内部调用(库内):**
- [`f`](scrapy_utils.md#sym-scrapy_utils_defer.py-416)
- [`defer_result`](scrapy_utils.md#sym-scrapy_utils_defer.py-103)

*来源: `scrapy/utils/defer.py:137` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-159"></a>

### `parallel` · func
```python
def parallel(
    iterable: Iterable[_T],
    count: int,
    callable: Callable[Concatenate[_T, _P], _T2],  # noqa: A002
    *args: _P.args,
    **named: _P.kwargs,
) -> Deferred[list[tuple[bool, Iterator[_T2]]]]
```

*来源: `scrapy/utils/defer.py:159` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-176"></a>

### `_AsyncCooperatorAdapter` · class
```python
class _AsyncCooperatorAdapter(Iterator[Deferred[Any]], Generic[_T])
```

*来源: `scrapy/utils/defer.py:176` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-222"></a>

### `_AsyncCooperatorAdapter.__init__` · method
```python
def __init__(
        self,
        aiterable: AsyncIterator[_T],
        callable_: Callable[Concatenate[_T, _P], Deferred[Any] | None],
        *callable_args: _P.args,
        **callable_kwargs: _P.kwargs,
    )
```

**内部调用(库内):**
- [`MutableAsyncChain.__aiter__`](scrapy_utils.md#sym-scrapy_utils_python.py-337)

*来源: `scrapy/utils/defer.py:222` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-237"></a>

### `_AsyncCooperatorAdapter._callback` · method
```python
def _callback(self, result: _T) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)
- [`_AsyncCooperatorAdapter._call_anext`](scrapy_utils.md#sym-scrapy_utils_defer.py-262)

*来源: `scrapy/utils/defer.py:237` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-253"></a>

### `_AsyncCooperatorAdapter._errback` · method
```python
def _errback(self, failure: Failure) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/utils/defer.py:253` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-262"></a>

### `_AsyncCooperatorAdapter._call_anext` · method
```python
def _call_anext(self) -> None
```

**内部调用(库内):**
- [`deferred_from_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-384)

*来源: `scrapy/utils/defer.py:262` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-268"></a>

### `_AsyncCooperatorAdapter.__next__` · method
```python
def __next__(self) -> Deferred[Any]
```

**内部调用(库内):**
- [`_AsyncCooperatorAdapter._call_anext`](scrapy_utils.md#sym-scrapy_utils_defer.py-262)

*来源: `scrapy/utils/defer.py:268` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-280"></a>

### `parallel_async` · func
```python
def parallel_async(
    async_iterable: AsyncIterator[_T],
    count: int,
    callable: Callable[Concatenate[_T, _P], Deferred[Any] | None],  # noqa: A002
    *args: _P.args,
    **named: _P.kwargs,
) -> Deferred[list[tuple[bool, Iterator[Deferred[Any]]]]]
```

**内部调用(库内):**
- [`_AsyncCooperatorAdapter`](scrapy_utils.md#sym-scrapy_utils_defer.py-176)

*来源: `scrapy/utils/defer.py:280` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-298"></a>

### `process_chain` · func
```python
def process_chain(
    callbacks: Iterable[Callable[Concatenate[_T, _P], _T]],
    input: _T,  # noqa: A002
    *a: _P.args,
    **kw: _P.kwargs,
) -> Deferred[_T]:  # pragma: no cover
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/utils/defer.py:298` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-317"></a>

### `process_parallel` · func
```python
def process_parallel(
    callbacks: Iterable[Callable[Concatenate[_T, _P], _T2]],
    input: _T,  # noqa: A002
    *a: _P.args,
    **kw: _P.kwargs,
) -> Deferred[list[_T2]]:  # pragma: no cover
```

*来源: `scrapy/utils/defer.py:317` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-337"></a>

### `eb` · func
```python
def eb(failure: Failure) -> Failure
```

*来源: `scrapy/utils/defer.py:337` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-345"></a>

### `iter_errback` · func
```python
def iter_errback(
    iterable: Iterable[_T],
    errback: Callable[Concatenate[Failure, _P], Any],
    *a: _P.args,
    **kw: _P.kwargs,
) -> Iterable[_T]
```

*来源: `scrapy/utils/defer.py:345` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-364"></a>

### `aiter_errback` · func
```python
async def aiter_errback(
    aiterable: AsyncIterator[_T],
    errback: Callable[Concatenate[Failure, _P], Any],
    *a: _P.args,
    **kw: _P.kwargs,
) -> AsyncIterator[_T]
```

*来源: `scrapy/utils/defer.py:364` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-384"></a>

### `deferred_from_coro` · func
装饰器: `@overload`
```python
def deferred_from_coro(o: Awaitable[_T]) -> Deferred[_T]
```

*来源: `scrapy/utils/defer.py:384` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-388"></a>

### `deferred_from_coro` · func
装饰器: `@overload`
```python
def deferred_from_coro(o: _T2) -> _T2
```

*来源: `scrapy/utils/defer.py:388` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-391"></a>

### `deferred_from_coro` · func
```python
def deferred_from_coro(o: Awaitable[_T] | _T2) -> Deferred[_T] | _T2
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)

*来源: `scrapy/utils/defer.py:391` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-406"></a>

### `deferred_f_from_coro_f` · func
```python
def deferred_f_from_coro_f(
    coro_f: Callable[_P, Awaitable[_T]],
) -> Callable[_P, Deferred[_T]]
```

**内部调用(库内):**
- [`deferred_from_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-384)

*来源: `scrapy/utils/defer.py:406` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-416"></a>

### `f` · func
装饰器: `@wraps(coro_f)`
```python
def f(*coro_args: _P.args, **coro_kwargs: _P.kwargs) -> Deferred[_T]
```

**内部调用(库内):**
- [`deferred_from_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-384)

*来源: `scrapy/utils/defer.py:416` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-422"></a>

### `maybeDeferred_coro` · func
```python
def maybeDeferred_coro(
    f: Callable[_P, Any], *args: _P.args, **kw: _P.kwargs
) -> Deferred[Any]
```

**内部调用(库内):**
- [`_maybeDeferred_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-434)

*来源: `scrapy/utils/defer.py:422` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-434"></a>

### `_maybeDeferred_coro` · func
```python
def _maybeDeferred_coro(
    f: Callable[_P, Any], warn: bool, *args: _P.args, **kw: _P.kwargs
) -> Deferred[Any]
```

**内部调用(库内):**
- [`f`](scrapy_utils.md#sym-scrapy_utils_defer.py-416)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`deferred_from_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-384)

*来源: `scrapy/utils/defer.py:434` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-469"></a>

### `deferred_to_future` · func
```python
def deferred_to_future(d: Deferred[_T]) -> Future[_T]
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)

*来源: `scrapy/utils/defer.py:469` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-499"></a>

### `maybe_deferred_to_future` · func
```python
def maybe_deferred_to_future(d: Deferred[_T]) -> Deferred[_T] | Future[_T]
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-469)

*来源: `scrapy/utils/defer.py:499` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-527"></a>

### `_schedule_coro` · func
```python
def _schedule_coro(coro: Coroutine[Any, Any, Any]) -> None
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)

*来源: `scrapy/utils/defer.py:527` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-543"></a>

### `ensure_awaitable` · func
装饰器: `@overload`
```python
def ensure_awaitable(o: Awaitable[_T], _warn: str | None = None) -> Awaitable[_T]
```

*来源: `scrapy/utils/defer.py:543` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-547"></a>

### `ensure_awaitable` · func
装饰器: `@overload`
```python
def ensure_awaitable(o: _T, _warn: str | None = None) -> Awaitable[_T]
```

*来源: `scrapy/utils/defer.py:547` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-550"></a>

### `ensure_awaitable` · func
```python
def ensure_awaitable(o: _T | Awaitable[_T], _warn: str | None = None) -> Awaitable[_T]
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-572)

*来源: `scrapy/utils/defer.py:550` · 待生成*

---
<a id="sym-scrapy_utils_defer.py-572"></a>

### `coro` · func
```python
async def coro() -> _T
```

*来源: `scrapy/utils/defer.py:572` · 待生成*

---

## `scrapy/utils/deprecate.py`

<a id="sym-scrapy_utils_deprecate.py-16"></a>

### `attribute` · func
```python
def attribute(obj: Any, oldattr: str, newattr: str, version: str = "0.12") -> None
```

*来源: `scrapy/utils/deprecate.py:16` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-26"></a>

### `create_deprecated_class` · func
```python
def create_deprecated_class(
    name: str,
    new_class: type,
    clsdict: dict[str, Any] | None = None,
    warn_category: type[Warning] = ScrapyDeprecationWarning,
    warn_once: bool = True,
    old_class_path: str | None = None,
    new_class_path: str | None = None,
    subclass_warn_message: str = "{cls} inherits from deprecated class {old}, please inherit from {new}.",
    instance_warn_message: str = "{cls} is deprecated, instantiate {new} instead.",
) -> type
```

**内部调用(库内):**
- [`DeprecatedClass.__new__`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-68)
- [`_clspath`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-138)
- [`DeprecatedClass.__init__`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-76)
- [`DeprecatedClass.__subclasscheck__`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-97)
- [`DeprecatedClass.__call__`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-111)
- [`DeprecatedClass`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-63)

*来源: `scrapy/utils/deprecate.py:26` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-63"></a>

### `DeprecatedClass` · class
```python
class DeprecatedClass(new_class.__class__)
```

*来源: `scrapy/utils/deprecate.py:63` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-68"></a>

### `DeprecatedClass.__new__` · method
```python
def __new__(  # pylint: disable=bad-classmethod-argument
            metacls, name: str, bases: tuple[type, ...], clsdict_: dict[str, Any]
        ) -> type
```

*来源: `scrapy/utils/deprecate.py:68` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-76"></a>

### `DeprecatedClass.__init__` · method
```python
def __init__(cls, name: str, bases: tuple[type, ...], clsdict_: dict[str, Any])
```

**内部调用(库内):**
- [`_clspath`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-138)

*来源: `scrapy/utils/deprecate.py:76` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-94"></a>

### `DeprecatedClass.__instancecheck__` · method
```python
def __instancecheck__(cls, inst: Any) -> bool
```

**内部调用(库内):**
- [`DeprecatedClass.__subclasscheck__`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-97)

*来源: `scrapy/utils/deprecate.py:94` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-97"></a>

### `DeprecatedClass.__subclasscheck__` · method
```python
def __subclasscheck__(cls, sub: type) -> bool
```

*来源: `scrapy/utils/deprecate.py:97` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-111"></a>

### `DeprecatedClass.__call__` · method
```python
def __call__(cls, *args: Any, **kwargs: Any) -> Any
```

**内部调用(库内):**
- [`_clspath`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-138)

*来源: `scrapy/utils/deprecate.py:111` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-138"></a>

### `_clspath` · func
```python
def _clspath(cls: type, forced: str | None = None) -> str
```

*来源: `scrapy/utils/deprecate.py:138` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-148"></a>

### `update_classpath` · func
装饰器: `@overload`
```python
def update_classpath(path: str) -> str
```

*来源: `scrapy/utils/deprecate.py:148` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-152"></a>

### `update_classpath` · func
装饰器: `@overload`
```python
def update_classpath(path: Any) -> Any
```

*来源: `scrapy/utils/deprecate.py:152` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-155"></a>

### `update_classpath` · func
```python
def update_classpath(path: Any) -> Any
```

*来源: `scrapy/utils/deprecate.py:155` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-169"></a>

### `method_is_overridden` · func
```python
def method_is_overridden(subclass: type, base_class: type, method_name: str) -> bool
```

*来源: `scrapy/utils/deprecate.py:169` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-203"></a>

### `argument_is_required` · func
```python
def argument_is_required(func: Callable[..., Any], arg_name: str) -> bool
```

**内部调用(库内):**
- [`get_func_args_dict`](scrapy_utils.md#sym-scrapy_utils_python.py-175)

*来源: `scrapy/utils/deprecate.py:203` · 待生成*

---
<a id="sym-scrapy_utils_deprecate.py-225"></a>

### `warn_on_deprecated_spider_attribute` · func
```python
def warn_on_deprecated_spider_attribute(attribute_name: str, setting_name: str) -> None
```

*来源: `scrapy/utils/deprecate.py:225` · 待生成*

---

## `scrapy/utils/display.py`

<a id="sym-scrapy_utils_display.py-14"></a>

### `_enable_windows_terminal_processing` · func
```python
def _enable_windows_terminal_processing() -> bool
```

*来源: `scrapy/utils/display.py:14` · 待生成*

---
<a id="sym-scrapy_utils_display.py-20"></a>

### `_tty_supports_color` · func
```python
def _tty_supports_color() -> bool
```

**内部调用(库内):**
- [`_enable_windows_terminal_processing`](scrapy_utils.md#sym-scrapy_utils_display.py-14)

*来源: `scrapy/utils/display.py:20` · 待生成*

---
<a id="sym-scrapy_utils_display.py-32"></a>

### `_colorize` · func
```python
def _colorize(text: str, colorize: bool = True) -> str
```

**内部调用(库内):**
- [`_tty_supports_color`](scrapy_utils.md#sym-scrapy_utils_display.py-20)

*来源: `scrapy/utils/display.py:32` · 待生成*

---
<a id="sym-scrapy_utils_display.py-46"></a>

### `pformat` · func
```python
def pformat(obj: Any, *args: Any, **kwargs: Any) -> str
```

**内部调用(库内):**
- [`_colorize`](scrapy_utils.md#sym-scrapy_utils_display.py-32)

*来源: `scrapy/utils/display.py:46` · 待生成*

---
<a id="sym-scrapy_utils_display.py-50"></a>

### `pprint` · func
```python
def pprint(obj: Any, *args: Any, **kwargs: Any) -> None
```

**内部调用(库内):**
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)

*来源: `scrapy/utils/display.py:50` · 待生成*

---

## `scrapy/utils/engine.py`

<a id="sym-scrapy_utils_engine.py-13"></a>

### `get_engine_status` · func
```python
def get_engine_status(engine: ExecutionEngine) -> list[tuple[str, Any]]
```

*来源: `scrapy/utils/engine.py:13` · 待生成*

---
<a id="sym-scrapy_utils_engine.py-42"></a>

### `format_engine_status` · func
```python
def format_engine_status(engine: ExecutionEngine) -> str
```

**内部调用(库内):**
- [`get_engine_status`](scrapy_utils.md#sym-scrapy_utils_engine.py-13)

*来源: `scrapy/utils/engine.py:42` · 待生成*

---
<a id="sym-scrapy_utils_engine.py-52"></a>

### `print_engine_status` · func
```python
def print_engine_status(engine: ExecutionEngine) -> None
```

**内部调用(库内):**
- [`format_engine_status`](scrapy_utils.md#sym-scrapy_utils_engine.py-42)

*来源: `scrapy/utils/engine.py:52` · 待生成*

---

## `scrapy/utils/ftp.py`

<a id="sym-scrapy_utils_ftp.py-7"></a>

### `ftp_makedirs_cwd` · func
```python
def ftp_makedirs_cwd(ftp: FTP, path: str, first_call: bool = True) -> None
```

*来源: `scrapy/utils/ftp.py:7` · 待生成*

---
<a id="sym-scrapy_utils_ftp.py-21"></a>

### `ftp_store_file` · func
```python
def ftp_store_file(
    *,
    path: str,
    file: IO[bytes],
    host: str,
    port: int,
    username: str,
    password: str,
    use_active_mode: bool = False,
    overwrite: bool = True,
) -> None
```

**内部调用(库内):**
- [`Portal.login`](scrapy_extensions.md#sym-scrapy_extensions_telnet.py-89)
- [`ftp_makedirs_cwd`](scrapy_utils.md#sym-scrapy_utils_ftp.py-7)

*来源: `scrapy/utils/ftp.py:21` · 待生成*

---

## `scrapy/utils/gz.py`

<a id="sym-scrapy_utils_gz.py-14"></a>

### `gunzip` · func
```python
def gunzip(data: bytes, *, max_size: int = 0) -> bytes
```

**内部调用(库内):**
- [`_check_max_size`](scrapy_utils.md#sym-scrapy_utils__compression.py-31)

*来源: `scrapy/utils/gz.py:14` · 待生成*

---
<a id="sym-scrapy_utils_gz.py-39"></a>

### `gzip_magic_number` · func
```python
def gzip_magic_number(response: Response) -> bool
```

*来源: `scrapy/utils/gz.py:39` · 待生成*

---

## `scrapy/utils/httpobj.py`

<a id="sym-scrapy_utils_httpobj.py-18"></a>

### `urlparse_cached` · func
```python
def urlparse_cached(request_or_response: Request | Response) -> ParseResult
```

*来源: `scrapy/utils/httpobj.py:18` · 待生成*

---

## `scrapy/utils/iterators.py`

<a id="sym-scrapy_utils_iterators.py-23"></a>

### `xmliter` · func
```python
def xmliter(obj: Response | str | bytes, nodename: str) -> Iterator[Selector]
```

**内部调用(库内):**
- [`_body_or_str`](scrapy_utils.md#sym-scrapy_utils_iterators.py-219)
- [`re_rsearch`](scrapy_utils.md#sym-scrapy_utils_python.py-114)
- [`Selector`](scrapy_selector.md#sym-scrapy_selector_unified.py-39)

*来源: `scrapy/utils/iterators.py:23` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-81"></a>

### `xmliter_lxml` · func
```python
def xmliter_lxml(
    obj: Response | str | bytes,
    nodename: str,
    namespace: str | None = None,
    prefix: str = "x",
) -> Iterator[Selector]
```

**内部调用(库内):**
- [`_StreamReader`](scrapy_utils.md#sym-scrapy_utils_iterators.py-124)
- [`Selector`](scrapy_selector.md#sym-scrapy_selector_unified.py-39)

*来源: `scrapy/utils/iterators.py:81` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-124"></a>

### `_StreamReader` · class
```python
class _StreamReader
```

*来源: `scrapy/utils/iterators.py:124` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-125"></a>

### `_StreamReader.__init__` · method
```python
def __init__(self, obj: Response | str | bytes)
```

*来源: `scrapy/utils/iterators.py:125` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-137"></a>

### `_StreamReader.read` · method
```python
def read(self, n: int = 65535) -> bytes
```

*来源: `scrapy/utils/iterators.py:137` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-147"></a>

### `_StreamReader._read_string` · method
```python
def _read_string(self, n: int = 65535) -> bytes
```

*来源: `scrapy/utils/iterators.py:147` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-152"></a>

### `_StreamReader._read_unicode` · method
```python
def _read_unicode(self, n: int = 65535) -> bytes
```

*来源: `scrapy/utils/iterators.py:152` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-158"></a>

### `csviter` · func
```python
def csviter(
    obj: Response | str | bytes,
    delimiter: str | None = None,
    headers: list[str] | None = None,
    encoding: str | None = None,
    quotechar: str | None = None,
) -> Iterator[dict[str, str]]
```

**内部调用(库内):**
- [`_body_or_str`](scrapy_utils.md#sym-scrapy_utils_iterators.py-219)

*来源: `scrapy/utils/iterators.py:158` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-219"></a>

### `_body_or_str` · func
装饰器: `@overload`
```python
def _body_or_str(obj: Response | str | bytes) -> str
```

*来源: `scrapy/utils/iterators.py:219` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-223"></a>

### `_body_or_str` · func
装饰器: `@overload`
```python
def _body_or_str(obj: Response | str | bytes, unicode: Literal[True]) -> str
```

*来源: `scrapy/utils/iterators.py:223` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-227"></a>

### `_body_or_str` · func
装饰器: `@overload`
```python
def _body_or_str(obj: Response | str | bytes, unicode: Literal[False]) -> bytes
```

*来源: `scrapy/utils/iterators.py:227` · 待生成*

---
<a id="sym-scrapy_utils_iterators.py-230"></a>

### `_body_or_str` · func
```python
def _body_or_str(obj: Response | str | bytes, unicode: bool = True) -> str | bytes
```

*来源: `scrapy/utils/iterators.py:230` · 待生成*

---

## `scrapy/utils/job.py`

<a id="sym-scrapy_utils_job.py-10"></a>

### `job_dir` · func
```python
def job_dir(settings: BaseSettings) -> str | None
```

*来源: `scrapy/utils/job.py:10` · 待生成*

---

## `scrapy/utils/log.py`

<a id="sym-scrapy_utils_log.py-28"></a>

### `failure_to_exc_info` · func
```python
def failure_to_exc_info(
    failure: Failure,
) -> tuple[type[BaseException], BaseException, TracebackType | None] | None
```

*来源: `scrapy/utils/log.py:28` · 待生成*

---
<a id="sym-scrapy_utils_log.py-43"></a>

### `TopLevelFormatter` · class
```python
class TopLevelFormatter(logging.Filter)
```

*来源: `scrapy/utils/log.py:43` · 待生成*

---
<a id="sym-scrapy_utils_log.py-55"></a>

### `TopLevelFormatter.__init__` · method
```python
def __init__(self, loggers: list[str] | None = None)
```

*来源: `scrapy/utils/log.py:55` · 待生成*

---
<a id="sym-scrapy_utils_log.py-59"></a>

### `TopLevelFormatter.filter` · method
```python
def filter(self, record: logging.LogRecord) -> bool
```

*来源: `scrapy/utils/log.py:59` · 待生成*

---
<a id="sym-scrapy_utils_log.py-91"></a>

### `configure_logging` · func
```python
def configure_logging(
    settings: Settings | dict[str, Any] | None = None,
    install_root_handler: bool = True,
) -> None
```

**内部调用(库内):**
- [`Settings`](scrapy_settings.md#sym-scrapy_settings___init__.py-690)
- [`StreamLogger`](scrapy_utils.md#sym-scrapy_utils_log.py-211)
- [`install_scrapy_root_handler`](scrapy_utils.md#sym-scrapy_utils_log.py-140)

*来源: `scrapy/utils/log.py:91` · 待生成*

---
<a id="sym-scrapy_utils_log.py-140"></a>

### `install_scrapy_root_handler` · func
```python
def install_scrapy_root_handler(settings: Settings) -> None
```

**内部调用(库内):**
- [`_uninstall_scrapy_root_handler`](scrapy_utils.md#sym-scrapy_utils_log.py-149)
- [`_get_handler`](scrapy_utils.md#sym-scrapy_utils_log.py-164)

*来源: `scrapy/utils/log.py:140` · 待生成*

---
<a id="sym-scrapy_utils_log.py-149"></a>

### `_uninstall_scrapy_root_handler` · func
```python
def _uninstall_scrapy_root_handler() -> None
```

*来源: `scrapy/utils/log.py:149` · 待生成*

---
<a id="sym-scrapy_utils_log.py-160"></a>

### `get_scrapy_root_handler` · func
```python
def get_scrapy_root_handler() -> logging.Handler | None
```

*来源: `scrapy/utils/log.py:160` · 待生成*

---
<a id="sym-scrapy_utils_log.py-164"></a>

### `_get_handler` · func
```python
def _get_handler(settings: Settings) -> logging.Handler
```

**内部调用(库内):**
- [`TopLevelFormatter`](scrapy_utils.md#sym-scrapy_utils_log.py-43)

*来源: `scrapy/utils/log.py:164` · 待生成*

---
<a id="sym-scrapy_utils_log.py-187"></a>

### `log_scrapy_info` · func
```python
def log_scrapy_info(settings: Settings) -> None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)
- [`get_versions`](scrapy_utils.md#sym-scrapy_utils_versions.py-28)

*来源: `scrapy/utils/log.py:187` · 待生成*

---
<a id="sym-scrapy_utils_log.py-199"></a>

### `log_reactor_info` · func
```python
def log_reactor_info() -> None
```

*来源: `scrapy/utils/log.py:199` · 待生成*

---
<a id="sym-scrapy_utils_log.py-211"></a>

### `StreamLogger` · class
```python
class StreamLogger
```

*来源: `scrapy/utils/log.py:211` · 待生成*

---
<a id="sym-scrapy_utils_log.py-218"></a>

### `StreamLogger.__init__` · method
```python
def __init__(self, logger: logging.Logger, log_level: int = logging.INFO)
```

*来源: `scrapy/utils/log.py:218` · 待生成*

---
<a id="sym-scrapy_utils_log.py-223"></a>

### `StreamLogger.write` · method
```python
def write(self, buf: str) -> None
```

*来源: `scrapy/utils/log.py:223` · 待生成*

---
<a id="sym-scrapy_utils_log.py-227"></a>

### `StreamLogger.flush` · method
```python
def flush(self) -> None
```

*来源: `scrapy/utils/log.py:227` · 待生成*

---
<a id="sym-scrapy_utils_log.py-232"></a>

### `LogCounterHandler` · class
```python
class LogCounterHandler(logging.Handler)
```

*来源: `scrapy/utils/log.py:232` · 待生成*

---
<a id="sym-scrapy_utils_log.py-235"></a>

### `LogCounterHandler.__init__` · method
```python
def __init__(self, crawler: Crawler, *args: Any, **kwargs: Any)
```

*来源: `scrapy/utils/log.py:235` · 待生成*

---
<a id="sym-scrapy_utils_log.py-239"></a>

### `LogCounterHandler.emit` · method
```python
def emit(self, record: logging.LogRecord) -> None
```

*来源: `scrapy/utils/log.py:239` · 待生成*

---
<a id="sym-scrapy_utils_log.py-245"></a>

### `logformatter_adapter` · func
```python
def logformatter_adapter(
    logkws: LogFormatterResult,
) -> tuple[int, str, dict[str, Any] | tuple[Any, ...]]
```

*来源: `scrapy/utils/log.py:245` · 待生成*

---
<a id="sym-scrapy_utils_log.py-264"></a>

### `SpiderLoggerAdapter` · class
```python
class SpiderLoggerAdapter(logging.LoggerAdapter)
```

*来源: `scrapy/utils/log.py:264` · 待生成*

---
<a id="sym-scrapy_utils_log.py-265"></a>

### `SpiderLoggerAdapter.process` · method
```python
def process(
        self, msg: str, kwargs: MutableMapping[str, Any]
    ) -> tuple[str, MutableMapping[str, Any]]
```

*来源: `scrapy/utils/log.py:265` · 待生成*

---

## `scrapy/utils/misc.py`

<a id="sym-scrapy_utils_misc.py-38"></a>

### `arg_to_iter` · func
装饰器: `@overload`
```python
def arg_to_iter(arg: None) -> tuple[()]
```

*来源: `scrapy/utils/misc.py:38` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-40"></a>

### `arg_to_iter` · func
装饰器: `@overload`
```python
def arg_to_iter(arg: _ITER_T) -> Iterable[_ITER_T]
```

*来源: `scrapy/utils/misc.py:40` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-42"></a>

### `arg_to_iter` · func
装饰器: `@overload`
```python
def arg_to_iter(arg: Iterable[_T]) -> Iterable[_T]
```

*来源: `scrapy/utils/misc.py:42` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-44"></a>

### `arg_to_iter` · func
装饰器: `@overload`
```python
def arg_to_iter(arg: _T) -> Iterable[_T]
```

*来源: `scrapy/utils/misc.py:44` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-45"></a>

### `arg_to_iter` · func
```python
def arg_to_iter(arg: Any) -> Iterable[Any]
```

*来源: `scrapy/utils/misc.py:45` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-58"></a>

### `load_object` · func
```python
def load_object(path: str | Callable[..., Any]) -> Any
```

*来源: `scrapy/utils/misc.py:58` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-93"></a>

### `walk_modules_iter` · func
```python
def walk_modules_iter(path: str) -> Iterable[ModuleType]
```

*来源: `scrapy/utils/misc.py:93` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-119"></a>

### `walk_modules` · func
```python
def walk_modules(path: str) -> list[ModuleType]
```

**内部调用(库内):**
- [`walk_modules_iter`](scrapy_utils.md#sym-scrapy_utils_misc.py-93)

*来源: `scrapy/utils/misc.py:119` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-138"></a>

### `md5sum` · func
```python
def md5sum(file: IO[bytes]) -> str
```

*来源: `scrapy/utils/misc.py:138` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-163"></a>

### `rel_has_nofollow` · func
```python
def rel_has_nofollow(rel: str | None) -> bool
```

*来源: `scrapy/utils/misc.py:163` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-168"></a>

### `SupportsFromCrawler` · class
```python
class SupportsFromCrawler(Protocol[_T_co, _P])
```

*来源: `scrapy/utils/misc.py:168` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-170"></a>

### `SupportsFromCrawler.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls, crawler: Crawler, /, *args: _P.args, **kwargs: _P.kwargs
    ) -> _T_co
```

*来源: `scrapy/utils/misc.py:170` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-176"></a>

### `build_from_crawler` · func
装饰器: `@overload`
```python
def build_from_crawler(
    objcls: SupportsFromCrawler[_T_co, _P],
    crawler: Crawler,
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> _T_co
```

*来源: `scrapy/utils/misc.py:176` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-186"></a>

### `build_from_crawler` · func
装饰器: `@overload`
```python
def build_from_crawler(
    objcls: Callable[_P, _T_co],
    crawler: Crawler,
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> _T_co
```

*来源: `scrapy/utils/misc.py:186` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-195"></a>

### `build_from_crawler` · func
```python
def build_from_crawler(
    objcls: Any,
    crawler: Crawler,
    /,
    *args: Any,
    **kwargs: Any,
) -> Any
```

**内部调用(库内):**
- [`SupportsFromCrawler.from_crawler`](scrapy_utils.md#sym-scrapy_utils_misc.py-170)

*来源: `scrapy/utils/misc.py:195` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-222"></a>

### `set_environ` · func
装饰器: `@contextmanager`
```python
def set_environ(**kwargs: str) -> Iterator[None]
```

*来源: `scrapy/utils/misc.py:222` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-239"></a>

### `walk_callable` · func
```python
def walk_callable(node: ast.AST) -> Iterable[ast.AST]
```

*来源: `scrapy/utils/misc.py:239` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-260"></a>

### `_returns_none` · func
```python
def _returns_none(return_node: ast.Return) -> bool
```

*来源: `scrapy/utils/misc.py:260` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-265"></a>

### `is_generator_with_return_value` · func
```python
def is_generator_with_return_value(callable: Callable[..., Any]) -> bool
```

**内部调用(库内):**
- [`walk_callable`](scrapy_utils.md#sym-scrapy_utils_misc.py-239)
- [`_returns_none`](scrapy_utils.md#sym-scrapy_utils_misc.py-260)

*来源: `scrapy/utils/misc.py:265` · 待生成*

---
<a id="sym-scrapy_utils_misc.py-296"></a>

### `warn_on_generator_with_return_value` · func
```python
def warn_on_generator_with_return_value(
    spider: Spider,
    callable: Callable[..., Any],  # noqa: A002
) -> None
```

**内部调用(库内):**
- [`is_generator_with_return_value`](scrapy_utils.md#sym-scrapy_utils_misc.py-265)

*来源: `scrapy/utils/misc.py:296` · 待生成*

---

## `scrapy/utils/ossignal.py`

<a id="sym-scrapy_utils_ossignal.py-21"></a>

### `install_shutdown_handlers` · func
```python
def install_shutdown_handlers(
    function: SignalHandlerT, override_sigint: bool = True
) -> None
```

*来源: `scrapy/utils/ossignal.py:21` · 待生成*

---

## `scrapy/utils/project.py`

<a id="sym-scrapy_utils_project.py-16"></a>

### `inside_project` · func
```python
def inside_project() -> bool
```

**内部调用(库内):**
- [`closest_scrapy_cfg`](scrapy_utils.md#sym-scrapy_utils_conf.py-73)

*来源: `scrapy/utils/project.py:16` · 待生成*

---
<a id="sym-scrapy_utils_project.py-31"></a>

### `project_data_dir` · func
```python
def project_data_dir(project: str = "default") -> str
```

**内部调用(库内):**
- [`inside_project`](scrapy_utils.md#sym-scrapy_utils_project.py-16)
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`get_config`](scrapy_utils.md#sym-scrapy_utils_conf.py-104)
- [`closest_scrapy_cfg`](scrapy_utils.md#sym-scrapy_utils_conf.py-73)

*来源: `scrapy/utils/project.py:31` · 待生成*

---
<a id="sym-scrapy_utils_project.py-50"></a>

### `data_path` · func
```python
def data_path(path: str | os.PathLike[str], createdir: bool = False) -> str
```

**内部调用(库内):**
- [`inside_project`](scrapy_utils.md#sym-scrapy_utils_project.py-16)
- [`project_data_dir`](scrapy_utils.md#sym-scrapy_utils_project.py-31)

*来源: `scrapy/utils/project.py:50` · 待生成*

---
<a id="sym-scrapy_utils_project.py-66"></a>

### `get_project_settings` · func
```python
def get_project_settings() -> Settings
```

**内部调用(库内):**
- [`init_env`](scrapy_utils.md#sym-scrapy_utils_conf.py-89)
- [`Settings`](scrapy_settings.md#sym-scrapy_settings___init__.py-690)
- [`BaseSettings.setmodule`](scrapy_settings.md#sym-scrapy_settings___init__.py-538)
- [`BaseSettings.setdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-535)

*来源: `scrapy/utils/project.py:66` · 待生成*

---

## `scrapy/utils/python.py`

<a id="sym-scrapy_utils_python.py-35"></a>

### `is_listlike` · func
```python
def is_listlike(x: Any) -> bool
```

*来源: `scrapy/utils/python.py:35` · 待生成*

---
<a id="sym-scrapy_utils_python.py-59"></a>

### `unique` · func
```python
def unique(list_: Iterable[_T], key: Callable[[_T], Any] = lambda x: x) -> list[_T]
```

*来源: `scrapy/utils/python.py:59` · 待生成*

---
<a id="sym-scrapy_utils_python.py-72"></a>

### `to_unicode` · func
```python
def to_unicode(
    text: str | bytes, encoding: str | None = None, errors: str = "strict"
) -> str
```

*来源: `scrapy/utils/python.py:72` · 待生成*

---
<a id="sym-scrapy_utils_python.py-88"></a>

### `to_bytes` · func
```python
def to_bytes(
    text: str | bytes, encoding: str | None = None, errors: str = "strict"
) -> bytes
```

*来源: `scrapy/utils/python.py:88` · 待生成*

---
<a id="sym-scrapy_utils_python.py-104"></a>

### `_chunk_iter` · func
```python
def _chunk_iter(text: str, chunk_size: int) -> Iterable[tuple[str, int]]
```

*来源: `scrapy/utils/python.py:104` · 待生成*

---
<a id="sym-scrapy_utils_python.py-114"></a>

### `re_rsearch` · func
```python
def re_rsearch(
    pattern: str | Pattern[str], text: str, chunk_size: int = 1024
) -> tuple[int, int] | None
```

**内部调用(库内):**
- [`_chunk_iter`](scrapy_utils.md#sym-scrapy_utils_python.py-104)

*来源: `scrapy/utils/python.py:114` · 待生成*

---
<a id="sym-scrapy_utils_python.py-144"></a>

### `memoizemethod_noargs` · func
```python
def memoizemethod_noargs(
    method: Callable[Concatenate[_SelfT, _P], _T],
) -> Callable[Concatenate[_SelfT, _P], _T]
```

*来源: `scrapy/utils/python.py:144` · 待生成*

---
<a id="sym-scrapy_utils_python.py-153"></a>

### `new_method` · func
装饰器: `@wraps(method)`
```python
def new_method(self: _SelfT, *args: _P.args, **kwargs: _P.kwargs) -> _T
```

*来源: `scrapy/utils/python.py:153` · 待生成*

---
<a id="sym-scrapy_utils_python.py-166"></a>

### `binary_is_text` · func
```python
def binary_is_text(data: bytes) -> bool
```

*来源: `scrapy/utils/python.py:166` · 待生成*

---
<a id="sym-scrapy_utils_python.py-175"></a>

### `get_func_args_dict` · func
```python
def get_func_args_dict(
    func: Callable[..., Any], stripself: bool = False
) -> Mapping[str, inspect.Parameter]
```

*来源: `scrapy/utils/python.py:175` · 待生成*

---
<a id="sym-scrapy_utils_python.py-210"></a>

### `get_func_args` · func
```python
def get_func_args(func: Callable[..., Any], stripself: bool = False) -> list[str]
```

**内部调用(库内):**
- [`get_func_args_dict`](scrapy_utils.md#sym-scrapy_utils_python.py-175)

*来源: `scrapy/utils/python.py:210` · 待生成*

---
<a id="sym-scrapy_utils_python.py-215"></a>

### `get_spec` · func
```python
def get_spec(func: Callable[..., Any]) -> tuple[list[str], dict[str, Any]]
```

*来源: `scrapy/utils/python.py:215` · 待生成*

---
<a id="sym-scrapy_utils_python.py-253"></a>

### `without_none_values` · func
装饰器: `@overload`
```python
def without_none_values(iterable: Mapping[_KT, _VT]) -> dict[_KT, _VT]
```

*来源: `scrapy/utils/python.py:253` · 待生成*

---
<a id="sym-scrapy_utils_python.py-257"></a>

### `without_none_values` · func
装饰器: `@overload`
```python
def without_none_values(iterable: Iterable[_KT]) -> Iterable[_KT]
```

*来源: `scrapy/utils/python.py:257` · 待生成*

---
<a id="sym-scrapy_utils_python.py-260"></a>

### `without_none_values` · func
```python
def without_none_values(
    iterable: Mapping[_KT, _VT] | Iterable[_KT],
) -> dict[_KT, _VT] | Iterable[_KT]
```

*来源: `scrapy/utils/python.py:260` · 待生成*

---
<a id="sym-scrapy_utils_python.py-274"></a>

### `global_object_name` · func
```python
def global_object_name(obj: Any) -> str
```

*来源: `scrapy/utils/python.py:274` · 待生成*

---
<a id="sym-scrapy_utils_python.py-288"></a>

### `garbage_collect` · func
```python
def garbage_collect() -> None
```

*来源: `scrapy/utils/python.py:288` · 待生成*

---
<a id="sym-scrapy_utils_python.py-295"></a>

### `garbage_collect` · func
```python
def garbage_collect() -> None
```

*来源: `scrapy/utils/python.py:295` · 待生成*

---
<a id="sym-scrapy_utils_python.py-299"></a>

### `MutableChain` · class
```python
class MutableChain(Iterable[_T])
```

*来源: `scrapy/utils/python.py:299` · 待生成*

---
<a id="sym-scrapy_utils_python.py-300"></a>

### `MutableChain.__init__` · method
```python
def __init__(self, *args: Iterable[_T])
```

*来源: `scrapy/utils/python.py:300` · 待生成*

---
<a id="sym-scrapy_utils_python.py-308"></a>

### `MutableChain.extend` · method
```python
def extend(self, *iterables: Iterable[_T]) -> None
```

*来源: `scrapy/utils/python.py:308` · 待生成*

---
<a id="sym-scrapy_utils_python.py-311"></a>

### `MutableChain.__iter__` · method
```python
def __iter__(self) -> Iterator[_T]
```

*来源: `scrapy/utils/python.py:311` · 待生成*

---
<a id="sym-scrapy_utils_python.py-314"></a>

### `MutableChain.__next__` · method
```python
def __next__(self) -> _T
```

*来源: `scrapy/utils/python.py:314` · 待生成*

---
<a id="sym-scrapy_utils_python.py-318"></a>

### `_async_chain` · func
```python
async def _async_chain(
    *iterables: Iterable[_T] | AsyncIterator[_T],
) -> AsyncIterator[_T]
```

**内部调用(库内):**
- [`as_async_generator`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-13)

*来源: `scrapy/utils/python.py:318` · 待生成*

---
<a id="sym-scrapy_utils_python.py-326"></a>

### `MutableAsyncChain` · class
```python
class MutableAsyncChain(AsyncIterator[_T])
```

*来源: `scrapy/utils/python.py:326` · 待生成*

---
<a id="sym-scrapy_utils_python.py-331"></a>

### `MutableAsyncChain.__init__` · method
```python
def __init__(self, *args: Iterable[_T] | AsyncIterator[_T])
```

**内部调用(库内):**
- [`_async_chain`](scrapy_utils.md#sym-scrapy_utils_python.py-318)

*来源: `scrapy/utils/python.py:331` · 待生成*

---
<a id="sym-scrapy_utils_python.py-334"></a>

### `MutableAsyncChain.extend` · method
```python
def extend(self, *iterables: Iterable[_T] | AsyncIterator[_T]) -> None
```

**内部调用(库内):**
- [`_async_chain`](scrapy_utils.md#sym-scrapy_utils_python.py-318)

*来源: `scrapy/utils/python.py:334` · 待生成*

---
<a id="sym-scrapy_utils_python.py-337"></a>

### `MutableAsyncChain.__aiter__` · method
```python
def __aiter__(self) -> Self
```

*来源: `scrapy/utils/python.py:337` · 待生成*

---
<a id="sym-scrapy_utils_python.py-340"></a>

### `MutableAsyncChain.__anext__` · method
```python
async def __anext__(self) -> _T
```

*来源: `scrapy/utils/python.py:340` · 待生成*

---
<a id="sym-scrapy_utils_python.py-344"></a>

### `_looks_like_import_path` · func
```python
def _looks_like_import_path(value: str) -> bool
```

*来源: `scrapy/utils/python.py:344` · 待生成*

---
<a id="sym-scrapy_utils_python.py-364"></a>

### `_iter_exc_causes` · func
```python
def _iter_exc_causes(exc: BaseException) -> Iterable[BaseException]
```

*来源: `scrapy/utils/python.py:364` · 待生成*

---

## `scrapy/utils/reactor.py`

<a id="sym-scrapy_utils_reactor.py-30"></a>

### `listen_tcp` · func
```python
def listen_tcp(portrange: list[int], host: str, factory: ServerFactory) -> Port
```

*来源: `scrapy/utils/reactor.py:30` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-50"></a>

### `CallLaterOnce` · class
```python
class CallLaterOnce(Generic[_T])
```

*来源: `scrapy/utils/reactor.py:50` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-55"></a>

### `CallLaterOnce.__init__` · method
```python
def __init__(self, func: Callable[_P, _T], *a: _P.args, **kw: _P.kwargs)
```

*来源: `scrapy/utils/reactor.py:55` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-62"></a>

### `CallLaterOnce.schedule` · method
```python
def schedule(self, delay: float = 0) -> None
```

**内部调用(库内):**
- [`call_later`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-234)

*来源: `scrapy/utils/reactor.py:62` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-69"></a>

### `CallLaterOnce.cancel` · method
```python
def cancel(self) -> None
```

*来源: `scrapy/utils/reactor.py:69` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-73"></a>

### `CallLaterOnce.__call__` · method
```python
def __call__(self) -> _T
```

**内部调用(库内):**
- [`call_later`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-234)

*来源: `scrapy/utils/reactor.py:73` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-86"></a>

### `CallLaterOnce.wait` · method
```python
async def wait(self) -> None
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/utils/reactor.py:86` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-98"></a>

### `set_asyncio_event_loop_policy` · func
```python
def set_asyncio_event_loop_policy() -> None
```

*来源: `scrapy/utils/reactor.py:98` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-114"></a>

### `install_reactor` · func
```python
def install_reactor(reactor_path: str, event_loop_path: str | None = None) -> None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`set_asyncio_event_loop_policy`](scrapy_utils.md#sym-scrapy_utils_reactor.py-98)
- [`set_asyncio_event_loop`](scrapy_utils.md#sym-scrapy_utils_reactor.py-136)

*来源: `scrapy/utils/reactor.py:114` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-132"></a>

### `_get_asyncio_event_loop` · func
```python
def _get_asyncio_event_loop() -> AbstractEventLoop
```

**内部调用(库内):**
- [`set_asyncio_event_loop`](scrapy_utils.md#sym-scrapy_utils_reactor.py-136)

*来源: `scrapy/utils/reactor.py:132` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-136"></a>

### `set_asyncio_event_loop` · func
```python
def set_asyncio_event_loop(event_loop_path: str | None) -> AbstractEventLoop
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`_get_asyncio_event_loop`](scrapy_utils.md#sym-scrapy_utils_reactor.py-132)

*来源: `scrapy/utils/reactor.py:136` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-169"></a>

### `verify_installed_reactor` · func
```python
def verify_installed_reactor(reactor_path: str) -> None
```

**内部调用(库内):**
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/utils/reactor.py:169` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-189"></a>

### `verify_installed_asyncio_event_loop` · func
```python
def verify_installed_asyncio_event_loop(loop_path: str) -> None
```

**内部调用(库内):**
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/utils/reactor.py:189` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-215"></a>

### `is_reactor_installed` · func
```python
def is_reactor_installed() -> bool
```

*来源: `scrapy/utils/reactor.py:215` · 待生成*

---
<a id="sym-scrapy_utils_reactor.py-220"></a>

### `is_asyncio_reactor_installed` · func
```python
def is_asyncio_reactor_installed() -> bool
```

**内部调用(库内):**
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)

*来源: `scrapy/utils/reactor.py:220` · 待生成*

---

## `scrapy/utils/reactorless.py`

<a id="sym-scrapy_utils_reactorless.py-16"></a>

### `is_reactorless` · func
```python
def is_reactorless() -> bool
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`is_reactor_installed`](scrapy_utils.md#sym-scrapy_utils_reactor.py-215)

*来源: `scrapy/utils/reactorless.py:16` · 待生成*

---
<a id="sym-scrapy_utils_reactorless.py-33"></a>

### `ReactorImportHook` · class
```python
class ReactorImportHook(MetaPathFinder)
```

*来源: `scrapy/utils/reactorless.py:33` · 待生成*

---
<a id="sym-scrapy_utils_reactorless.py-36"></a>

### `ReactorImportHook.find_spec` · method
```python
def find_spec(
        self,
        fullname: str,
        path: Sequence[str] | None,
        target: ModuleType | None = None,
    ) -> ModuleSpec | None
```

*来源: `scrapy/utils/reactorless.py:36` · 待生成*

---
<a id="sym-scrapy_utils_reactorless.py-50"></a>

### `install_reactor_import_hook` · func
```python
def install_reactor_import_hook() -> None
```

**内部调用(库内):**
- [`ReactorImportHook`](scrapy_utils.md#sym-scrapy_utils_reactorless.py-33)

*来源: `scrapy/utils/reactorless.py:50` · 待生成*

---

## `scrapy/utils/request.py`

<a id="sym-scrapy_utils_request.py-35"></a>

### `fingerprint` · func
```python
def fingerprint(
    request: Request,
    *,
    include_headers: Iterable[bytes | str] | None = None,
    keep_fragments: bool = False,
) -> bytes
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/utils/request.py:35` · 待生成*

---
<a id="sym-scrapy_utils_request.py-106"></a>

### `RequestFingerprinterProtocol` · class
```python
class RequestFingerprinterProtocol(Protocol)
```

*来源: `scrapy/utils/request.py:106` · 待生成*

---
<a id="sym-scrapy_utils_request.py-107"></a>

### `RequestFingerprinterProtocol.fingerprint` · method
```python
def fingerprint(self, request: Request) -> bytes
```

*来源: `scrapy/utils/request.py:107` · 待生成*

---
<a id="sym-scrapy_utils_request.py-110"></a>

### `RequestFingerprinter` · class
```python
class RequestFingerprinter
```

*来源: `scrapy/utils/request.py:110` · 待生成*

---
<a id="sym-scrapy_utils_request.py-123"></a>

### `RequestFingerprinter.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/utils/request.py:123` · 待生成*

---
<a id="sym-scrapy_utils_request.py-126"></a>

### `RequestFingerprinter.__init__` · method
```python
def __init__(self, crawler: Crawler | None = None)
```

*来源: `scrapy/utils/request.py:126` · 待生成*

---
<a id="sym-scrapy_utils_request.py-129"></a>

### `RequestFingerprinter.fingerprint` · method
```python
def fingerprint(self, request: Request) -> bytes
```

*来源: `scrapy/utils/request.py:129` · 待生成*

---
<a id="sym-scrapy_utils_request.py-133"></a>

### `request_httprepr` · func
```python
def request_httprepr(request: Request) -> bytes
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`Headers.to_string`](scrapy_http.md#sym-scrapy_http_headers.py-112)

*来源: `scrapy/utils/request.py:133` · 待生成*

---
<a id="sym-scrapy_utils_request.py-150"></a>

### `referer_str` · func
```python
def referer_str(request: Request) -> str | None
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/utils/request.py:150` · 待生成*

---
<a id="sym-scrapy_utils_request.py-158"></a>

### `request_from_dict` · func
```python
def request_from_dict(d: dict[str, Any], *, spider: Spider | None = None) -> Request
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`_get_method`](scrapy_utils.md#sym-scrapy_utils_request.py-173)

*来源: `scrapy/utils/request.py:158` · 待生成*

---
<a id="sym-scrapy_utils_request.py-173"></a>

### `_get_method` · func
```python
def _get_method(obj: Any, name: Any) -> Any
```

*来源: `scrapy/utils/request.py:173` · 待生成*

---
<a id="sym-scrapy_utils_request.py-182"></a>

### `_cookie_value_to_unicode` · func
```python
def _cookie_value_to_unicode(value: str | bytes | float) -> str
```

*来源: `scrapy/utils/request.py:182` · 待生成*

---
<a id="sym-scrapy_utils_request.py-188"></a>

### `request_to_curl` · func
```python
def request_to_curl(request: Request) -> str
```

**内部调用(库内):**
- [`_cookie_value_to_unicode`](scrapy_utils.md#sym-scrapy_utils_request.py-182)

*来源: `scrapy/utils/request.py:188` · 待生成*

---

## `scrapy/utils/response.py`

<a id="sym-scrapy_utils_response.py-28"></a>

### `get_base_url` · func
```python
def get_base_url(response: TextResponse) -> str
```

*来源: `scrapy/utils/response.py:28` · 待生成*

---
<a id="sym-scrapy_utils_response.py-43"></a>

### `get_meta_refresh` · func
```python
def get_meta_refresh(
    response: TextResponse,
    ignore_tags: Iterable[str] = ("script", "noscript"),
) -> tuple[None, None] | tuple[float, str]
```

**内部调用(库内):**
- [`get_base_url`](scrapy_utils.md#sym-scrapy_utils_response.py-28)

*来源: `scrapy/utils/response.py:43` · 待生成*

---
<a id="sym-scrapy_utils_response.py-56"></a>

### `response_status_message` · func
```python
def response_status_message(status: bytes | float | str) -> str
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/utils/response.py:56` · 待生成*

---
<a id="sym-scrapy_utils_response.py-63"></a>

### `_remove_html_comments` · func
```python
def _remove_html_comments(body: bytes) -> bytes
```

*来源: `scrapy/utils/response.py:63` · 待生成*

---
<a id="sym-scrapy_utils_response.py-74"></a>

### `open_in_browser` · func
```python
def open_in_browser(
    response: TextResponse,
    _openfunc: Callable[[str], Any] = webbrowser.open,
) -> Any
```

**内部调用(库内):**
- [`_remove_html_comments`](scrapy_utils.md#sym-scrapy_utils_response.py-63)
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/utils/response.py:74` · 待生成*

---

## `scrapy/utils/serialize.py`

<a id="sym-scrapy_utils_serialize.py-12"></a>

### `ScrapyJSONEncoder` · class
```python
class ScrapyJSONEncoder(json.JSONEncoder)
```

*来源: `scrapy/utils/serialize.py:12` · 待生成*

---
<a id="sym-scrapy_utils_serialize.py-16"></a>

### `ScrapyJSONEncoder.default` · method
```python
def default(self, o: Any) -> Any
```

*来源: `scrapy/utils/serialize.py:16` · 待生成*

---

## `scrapy/utils/signal.py`

<a id="sym-scrapy_utils_signal.py-36"></a>

### `send_catch_log` · func
```python
def send_catch_log(
    signal: TypingAny = Any,
    sender: TypingAny = Anonymous,
    *arguments: TypingAny,
    **named: TypingAny,
) -> list[tuple[TypingAny, TypingAny]]
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/utils/signal.py:36` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-78"></a>

### `send_catch_log_deferred` · func
```python
def send_catch_log_deferred(
    signal: TypingAny = Any,
    sender: TypingAny = Anonymous,
    *arguments: TypingAny,
    **named: TypingAny,
) -> Deferred[list[tuple[TypingAny, TypingAny]]]
```

**内部调用(库内):**
- [`_send_catch_log_deferred`](scrapy_utils.md#sym-scrapy_utils_signal.py-98)

*来源: `scrapy/utils/signal.py:78` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-98"></a>

### `_send_catch_log_deferred` · func
装饰器: `@inlineCallbacks`
```python
def _send_catch_log_deferred(
    signal: TypingAny,
    sender: TypingAny,
    *arguments: TypingAny,
    **named: TypingAny,
) -> Generator[Deferred[TypingAny], TypingAny, list[tuple[TypingAny, TypingAny]]]
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)
- [`_maybeDeferred_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-434)

*来源: `scrapy/utils/signal.py:98` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-104"></a>

### `logerror` · func
```python
def logerror(failure: Failure, recv: TypingAny) -> Failure
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)

*来源: `scrapy/utils/signal.py:104` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-141"></a>

### `send_catch_log_async` · func
```python
async def send_catch_log_async(
    signal: TypingAny = Any,
    sender: TypingAny = Anonymous,
    *arguments: TypingAny,
    **named: TypingAny,
) -> list[tuple[TypingAny, TypingAny]]
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`_send_catch_log_asyncio`](scrapy_utils.md#sym-scrapy_utils_signal.py-166)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`_send_catch_log_deferred`](scrapy_utils.md#sym-scrapy_utils_signal.py-98)

*来源: `scrapy/utils/signal.py:141` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-166"></a>

### `_send_catch_log_asyncio` · func
```python
async def _send_catch_log_asyncio(
    signal: TypingAny = Any,
    sender: TypingAny = Anonymous,
    *arguments: TypingAny,
    **named: TypingAny,
) -> list[tuple[TypingAny, TypingAny]]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`handler`](scrapy_utils.md#sym-scrapy_utils_signal.py-189)

*来源: `scrapy/utils/signal.py:166` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-189"></a>

### `handler` · func
```python
async def handler(
            receiver: Callable[..., Any],
        ) -> tuple[Callable[..., Any], TypingAny]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/utils/signal.py:189` · 待生成*

---
<a id="sym-scrapy_utils_signal.py-220"></a>

### `disconnect_all` · func
```python
def disconnect_all(signal: TypingAny = Any, sender: TypingAny = Any) -> None
```

**内部调用(库内):**
- [`SignalManager.disconnect`](scrapy.md#sym-scrapy_signalmanager.py-35)

*来源: `scrapy/utils/signal.py:220` · 待生成*

---

## `scrapy/utils/sitemap.py`

<a id="sym-scrapy_utils_sitemap.py-23"></a>

### `Sitemap` · class
```python
class Sitemap
```

*来源: `scrapy/utils/sitemap.py:23` · 待生成*

---
<a id="sym-scrapy_utils_sitemap.py-29"></a>

### `Sitemap.__init__` · method
```python
def __init__(self, xmltext: str | bytes)
```

**内部调用(库内):**
- [`Sitemap._get_tag_name`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-99)

*来源: `scrapy/utils/sitemap.py:29` · 待生成*

---
<a id="sym-scrapy_utils_sitemap.py-51"></a>

### `Sitemap.__iter__` · method
```python
def __iter__(self) -> Iterator[dict[str, Any]]
```

**内部调用(库内):**
- [`Sitemap._get_tag_name`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-99)
- [`Sitemap._process_sitemap_element`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-62)

*来源: `scrapy/utils/sitemap.py:51` · 待生成*

---
<a id="sym-scrapy_utils_sitemap.py-62"></a>

### `Sitemap._process_sitemap_element` · method
```python
def _process_sitemap_element(
        self, elem: lxml.etree._Element
    ) -> dict[str, Any] | None
```

**内部调用(库内):**
- [`Sitemap._get_tag_name`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-99)

*来源: `scrapy/utils/sitemap.py:62` · 待生成*

---
<a id="sym-scrapy_utils_sitemap.py-99"></a>

### `Sitemap._get_tag_name` · method
装饰器: `@staticmethod`
```python
def _get_tag_name(elem: lxml.etree._Element) -> str
```

*来源: `scrapy/utils/sitemap.py:99` · 待生成*

---
<a id="sym-scrapy_utils_sitemap.py-106"></a>

### `sitemap_urls_from_robots` · func
```python
def sitemap_urls_from_robots(
    robots_text: str | bytes,
    base_url: str | None = None,
) -> Iterable[str]
```

**内部调用(库内):**
- [`_sitemap_urls_from_robots_str`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-128)

*来源: `scrapy/utils/sitemap.py:106` · 待生成*

---
<a id="sym-scrapy_utils_sitemap.py-128"></a>

### `_sitemap_urls_from_robots_str` · func
```python
def _sitemap_urls_from_robots_str(
    robots_text: str,
    base_url: str | None = None,
) -> Iterable[str]
```

*来源: `scrapy/utils/sitemap.py:128` · 待生成*

---

## `scrapy/utils/spider.py`

<a id="sym-scrapy_utils_spider.py-28"></a>

### `iterate_spider_output` · func
装饰器: `@overload`
```python
def iterate_spider_output(result: AsyncGenerator[_T]) -> AsyncGenerator[_T]
```

*来源: `scrapy/utils/spider.py:28` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-32"></a>

### `iterate_spider_output` · func
装饰器: `@overload`
```python
def iterate_spider_output(result: CoroutineType[Any, Any, _T]) -> Deferred[_T]
```

*来源: `scrapy/utils/spider.py:32` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-36"></a>

### `iterate_spider_output` · func
装饰器: `@overload`
```python
def iterate_spider_output(result: _T) -> Iterable[Any]
```

*来源: `scrapy/utils/spider.py:36` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-39"></a>

### `iterate_spider_output` · func
```python
def iterate_spider_output(
    result: Any,
) -> Iterable[Any] | AsyncGenerator[_T] | Deferred[_T]
```

*来源: `scrapy/utils/spider.py:39` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-50"></a>

### `iter_spider_classes` · func
```python
def iter_spider_classes(module: ModuleType) -> Iterable[type[Spider]]
```

*来源: `scrapy/utils/spider.py:50` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-65"></a>

### `spidercls_for_request` · func
装饰器: `@overload`
```python
def spidercls_for_request(
    spider_loader: SpiderLoaderProtocol,
    request: Request,
    default_spidercls: type[Spider],
    log_none: bool = ...,
    log_multiple: bool = ...,
) -> type[Spider]
```

*来源: `scrapy/utils/spider.py:65` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-75"></a>

### `spidercls_for_request` · func
装饰器: `@overload`
```python
def spidercls_for_request(
    spider_loader: SpiderLoaderProtocol,
    request: Request,
    default_spidercls: None,
    log_none: bool = ...,
    log_multiple: bool = ...,
) -> type[Spider] | None
```

*来源: `scrapy/utils/spider.py:75` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-85"></a>

### `spidercls_for_request` · func
装饰器: `@overload`
```python
def spidercls_for_request(
    spider_loader: SpiderLoaderProtocol,
    request: Request,
    *,
    log_none: bool = ...,
    log_multiple: bool = ...,
) -> type[Spider] | None
```

*来源: `scrapy/utils/spider.py:85` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-94"></a>

### `spidercls_for_request` · func
```python
def spidercls_for_request(
    spider_loader: SpiderLoaderProtocol,
    request: Request,
    default_spidercls: type[Spider] | None = None,
    log_none: bool = False,
    log_multiple: bool = False,
) -> type[Spider] | None
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/utils/spider.py:94` · 待生成*

---
<a id="sym-scrapy_utils_spider.py-129"></a>

### `DefaultSpider` · class
```python
class DefaultSpider(Spider)
```

*来源: `scrapy/utils/spider.py:129` · 待生成*

---

## `scrapy/utils/ssl.py`

<a id="sym-scrapy_utils_ssl.py-35"></a>

### `_get_tls_version_limit` · func
```python
def _get_tls_version_limit(
    settings: BaseSettings, setting_name: str, converter: Callable[[str], _T]
) -> _T | None
```

*来源: `scrapy/utils/ssl.py:35` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-47"></a>

### `_get_tls_version_limits` · func
```python
def _get_tls_version_limits(
    settings: BaseSettings, converter: Callable[[str], _T]
) -> tuple[_T | None, _T | None]
```

**内部调用(库内):**
- [`_get_tls_version_limit`](scrapy_utils.md#sym-scrapy_utils_ssl.py-35)

*来源: `scrapy/utils/ssl.py:47` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-66"></a>

### `_make_ssl_context` · func
```python
def _make_ssl_context(settings: BaseSettings) -> ssl.SSLContext
```

**内部调用(库内):**
- [`_get_tls_version_limits`](scrapy_utils.md#sym-scrapy_utils_ssl.py-47)

*来源: `scrapy/utils/ssl.py:66` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-95"></a>

### `_make_insecure_ssl_ctx` · func
```python
def _make_insecure_ssl_ctx() -> ssl.SSLContext
```

*来源: `scrapy/utils/ssl.py:95` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-107"></a>

### `_log_sslobj_debug_info` · func
```python
def _log_sslobj_debug_info(sslobj: ssl.SSLObject) -> None
```

*来源: `scrapy/utils/ssl.py:107` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-124"></a>

### `_ffi_buf_to_string` · func
```python
def _ffi_buf_to_string(buf: Any) -> str
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/utils/ssl.py:124` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-128"></a>

### `ffi_buf_to_string` · func
```python
def ffi_buf_to_string(buf: Any) -> str
```

*来源: `scrapy/utils/ssl.py:128` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-137"></a>

### `_x509name_to_string` · func
```python
def _x509name_to_string(x509name: X509Name) -> str
```

**内部调用(库内):**
- [`_ffi_buf_to_string`](scrapy_utils.md#sym-scrapy_utils_ssl.py-124)

*来源: `scrapy/utils/ssl.py:137` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-147"></a>

### `x509name_to_string` · func
```python
def x509name_to_string(x509name: X509Name) -> str
```

**内部调用(库内):**
- [`_x509name_to_string`](scrapy_utils.md#sym-scrapy_utils_ssl.py-137)

*来源: `scrapy/utils/ssl.py:147` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-156"></a>

### `_get_temp_key_info` · func
```python
def _get_temp_key_info(ssl_object: Any) -> str | None
```

**内部调用(库内):**
- [`_ffi_buf_to_string`](scrapy_utils.md#sym-scrapy_utils_ssl.py-124)

*来源: `scrapy/utils/ssl.py:156` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-191"></a>

### `get_temp_key_info` · func
```python
def get_temp_key_info(ssl_object: Any) -> str | None
```

**内部调用(库内):**
- [`_get_temp_key_info`](scrapy_utils.md#sym-scrapy_utils_ssl.py-156)

*来源: `scrapy/utils/ssl.py:191` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-200"></a>

### `get_openssl_version` · func
```python
def get_openssl_version() -> str
```

*来源: `scrapy/utils/ssl.py:200` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-206"></a>

### `_log_ssl_conn_debug_info` · func
```python
def _log_ssl_conn_debug_info(hostname: str, connection: OpenSSL.SSL.Connection) -> None
```

**内部调用(库内):**
- [`_x509name_to_string`](scrapy_utils.md#sym-scrapy_utils_ssl.py-137)
- [`_get_temp_key_info`](scrapy_utils.md#sym-scrapy_utils_ssl.py-156)

*来源: `scrapy/utils/ssl.py:206` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-235"></a>

### `_CertificateOptionsVersionKwargs` · class
```python
class _CertificateOptionsVersionKwargs(TypedDict, total=False)
```

*来源: `scrapy/utils/ssl.py:235` · 待生成*

---
<a id="sym-scrapy_utils_ssl.py-241"></a>

### `_get_cert_options_version_kwargs` · func
```python
def _get_cert_options_version_kwargs(
    min_version: TLSVersion | None, max_version: TLSVersion | None
) -> _CertificateOptionsVersionKwargs
```

*来源: `scrapy/utils/ssl.py:241` · 待生成*

---

## `scrapy/utils/template.py`

<a id="sym-scrapy_utils_template.py-14"></a>

### `render_templatefile` · func
```python
def render_templatefile(path: str | PathLike[str], **kwargs: Any) -> None
```

*来源: `scrapy/utils/template.py:14` · 待生成*

---
<a id="sym-scrapy_utils_template.py-31"></a>

### `string_camelcase` · func
```python
def string_camelcase(string: str) -> str
```

*来源: `scrapy/utils/template.py:31` · 待生成*

---

## `scrapy/utils/trackref.py`

<a id="sym-scrapy_utils_trackref.py-38"></a>

### `object_ref` · class
```python
class object_ref
```

*来源: `scrapy/utils/trackref.py:38` · 待生成*

---
<a id="sym-scrapy_utils_trackref.py-43"></a>

### `object_ref.__new__` · method
```python
def __new__(cls, *args: Any, **kwargs: Any) -> Self
```

*来源: `scrapy/utils/trackref.py:43` · 待生成*

---
<a id="sym-scrapy_utils_trackref.py-50"></a>

### `format_live_refs` · func
```python
def format_live_refs(ignore: Any = NoneType) -> str
```

*来源: `scrapy/utils/trackref.py:50` · 待生成*

---
<a id="sym-scrapy_utils_trackref.py-64"></a>

### `print_live_refs` · func
```python
def print_live_refs(*a: Any, **kw: Any) -> None
```

**内部调用(库内):**
- [`format_live_refs`](scrapy_utils.md#sym-scrapy_utils_trackref.py-50)

*来源: `scrapy/utils/trackref.py:64` · 待生成*

---
<a id="sym-scrapy_utils_trackref.py-69"></a>

### `get_oldest` · func
```python
def get_oldest(class_name: str) -> Any
```

*来源: `scrapy/utils/trackref.py:69` · 待生成*

---
<a id="sym-scrapy_utils_trackref.py-79"></a>

### `iter_all` · func
```python
def iter_all(class_name: str) -> Iterable[Any]
```

*来源: `scrapy/utils/trackref.py:79` · 待生成*

---

## `scrapy/utils/url.py`

<a id="sym-scrapy_utils_url.py-22"></a>

### `url_is_from_any_domain` · func
```python
def url_is_from_any_domain(url: UrlT, domains: Iterable[str]) -> bool
```

*来源: `scrapy/utils/url.py:22` · 待生成*

---
<a id="sym-scrapy_utils_url.py-30"></a>

### `_spider_domains` · func
```python
def _spider_domains(spider: type[Spider]) -> Iterable[str]
```

*来源: `scrapy/utils/url.py:30` · 待生成*

---
<a id="sym-scrapy_utils_url.py-36"></a>

### `url_is_from_spider` · func
```python
def url_is_from_spider(url: UrlT, spider: type[Spider]) -> bool
```

**内部调用(库内):**
- [`url_is_from_any_domain`](scrapy_utils.md#sym-scrapy_utils_url.py-22)
- [`_spider_domains`](scrapy_utils.md#sym-scrapy_utils_url.py-30)

*来源: `scrapy/utils/url.py:36` · 待生成*

---
<a id="sym-scrapy_utils_url.py-41"></a>

### `url_has_any_extension` · func
```python
def url_has_any_extension(url: UrlT, extensions: Iterable[str]) -> bool
```

*来源: `scrapy/utils/url.py:41` · 待生成*

---
<a id="sym-scrapy_utils_url.py-47"></a>

### `add_http_if_no_scheme` · func
```python
def add_http_if_no_scheme(url: str) -> str
```

*来源: `scrapy/utils/url.py:47` · 待生成*

---
<a id="sym-scrapy_utils_url.py-58"></a>

### `_is_posix_path` · func
```python
def _is_posix_path(string: str) -> bool
```

*来源: `scrapy/utils/url.py:58` · 待生成*

---
<a id="sym-scrapy_utils_url.py-80"></a>

### `_is_windows_path` · func
```python
def _is_windows_path(string: str) -> bool
```

*来源: `scrapy/utils/url.py:80` · 待生成*

---
<a id="sym-scrapy_utils_url.py-96"></a>

### `_is_filesystem_path` · func
```python
def _is_filesystem_path(string: str) -> bool
```

**内部调用(库内):**
- [`_is_posix_path`](scrapy_utils.md#sym-scrapy_utils_url.py-58)
- [`_is_windows_path`](scrapy_utils.md#sym-scrapy_utils_url.py-80)

*来源: `scrapy/utils/url.py:96` · 待生成*

---
<a id="sym-scrapy_utils_url.py-100"></a>

### `guess_scheme` · func
```python
def guess_scheme(url: str) -> str
```

**内部调用(库内):**
- [`_is_filesystem_path`](scrapy_utils.md#sym-scrapy_utils_url.py-96)
- [`add_http_if_no_scheme`](scrapy_utils.md#sym-scrapy_utils_url.py-47)

*来源: `scrapy/utils/url.py:100` · 待生成*

---
<a id="sym-scrapy_utils_url.py-108"></a>

### `strip_url` · func
```python
def strip_url(
    url: str,
    strip_credentials: bool = True,
    strip_default_port: bool = True,
    origin_only: bool = False,
    strip_fragment: bool = True,
) -> str
```

*来源: `scrapy/utils/url.py:108` · 待生成*

---

## `scrapy/utils/versions.py`

<a id="sym-scrapy_utils_versions.py-15"></a>

### `_version` · func
```python
def _version(item: str) -> str
```

**内部调用(库内):**
- [`get_openssl_version`](scrapy_utils.md#sym-scrapy_utils_ssl.py-200)

*来源: `scrapy/utils/versions.py:15` · 待生成*

---
<a id="sym-scrapy_utils_versions.py-28"></a>

### `get_versions` · func
```python
def get_versions(
    software: list[str] | None = None,
) -> list[tuple[str, str]]
```

**内部调用(库内):**
- [`_version`](scrapy_utils.md#sym-scrapy_utils_versions.py-15)

*来源: `scrapy/utils/versions.py:28` · 待生成*

---