# API 参考:`scrapy/core`

## `scrapy/core/downloader/__init__.py`

<a id="sym-scrapy_core_downloader___init__.py-45"></a>

### `Slot` · class
装饰器: `@dataclass(slots=True, eq=False)`
```python
class Slot
```

*来源: `scrapy/core/downloader/__init__.py:45` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-60"></a>

### `Slot.free_transfer_slots` · method
```python
def free_transfer_slots(self) -> int
```

*来源: `scrapy/core/downloader/__init__.py:60` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-63"></a>

### `Slot.download_delay` · method
```python
def download_delay(self) -> float
```

*来源: `scrapy/core/downloader/__init__.py:63` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-68"></a>

### `Slot.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/core/downloader/__init__.py:68` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-73"></a>

### `Slot.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/core/downloader/__init__.py:73` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-83"></a>

### `_get_concurrency_delay` · func
```python
def _get_concurrency_delay(
    concurrency: int, spider: Spider, settings: BaseSettings
) -> tuple[int, float]
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)
- [`warn_on_deprecated_spider_attribute`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-225)

*来源: `scrapy/core/downloader/__init__.py:83` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-99"></a>

### `Downloader` · class
```python
class Downloader
```

*来源: `scrapy/core/downloader/__init__.py:99` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-103"></a>

### `Downloader.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`DownloadHandlers`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-49)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)

*来源: `scrapy/core/downloader/__init__.py:103` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-126"></a>

### `Downloader.fetch` · method
装饰器: `@inlineCallbacks` `@_warn_spider_arg`
```python
def fetch(
        self, request: Request, spider: Spider | None = None
    ) -> Generator[Deferred[Any], Any, Response | Request]
```

*来源: `scrapy/core/downloader/__init__.py:126` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-140"></a>

### `Downloader.needs_backout` · method
```python
def needs_backout(self) -> bool
```

*来源: `scrapy/core/downloader/__init__.py:140` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-144"></a>

### `Downloader._get_slot` · method
装饰器: `@_warn_spider_arg`
```python
def _get_slot(
        self, request: Request, spider: Spider | None = None
    ) -> tuple[str, Slot]
```

**内部调用(库内):**
- [`Downloader.get_slot_key`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-166)
- [`_get_concurrency_delay`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-83)
- [`Slot`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-45)
- [`Downloader._start_slot_gc`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-275)

*来源: `scrapy/core/downloader/__init__.py:144` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-166"></a>

### `Downloader.get_slot_key` · method
```python
def get_slot_key(self, request: Request) -> str
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/core/downloader/__init__.py:166` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-178"></a>

### `Downloader._enqueue_request` · method
```python
async def _enqueue_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`Downloader._get_slot`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-144)
- [`Downloader._process_queue`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-195)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/downloader/__init__.py:178` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-195"></a>

### `Downloader._process_queue` · method
```python
def _process_queue(self, slot: Slot) -> None
```

**内部调用(库内):**
- [`Slot.download_delay`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-63)
- [`call_later`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-234)
- [`Slot.free_transfer_slots`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-60)
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`Downloader._wait_for_download`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-254)

*来源: `scrapy/core/downloader/__init__.py:195` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-219"></a>

### `Downloader._latercall` · method
```python
def _latercall(self, slot: Slot) -> None
```

**内部调用(库内):**
- [`Downloader._process_queue`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-195)

*来源: `scrapy/core/downloader/__init__.py:219` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-223"></a>

### `Downloader._download` · method
```python
async def _download(self, slot: Slot, request: Request) -> Response
```

**内部调用(库内):**
- [`DownloadHandlers.download_request_async`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-141)
- [`_defer_sleep_async`](scrapy_utils.md#sym-scrapy_utils_defer.py-89)
- [`Downloader._process_queue`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-195)

*来源: `scrapy/core/downloader/__init__.py:223` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-254"></a>

### `Downloader._wait_for_download` · method
```python
async def _wait_for_download(
        self, slot: Slot, request: Request, queue_dfd: Deferred[Response]
    ) -> None
```

**内部调用(库内):**
- [`Downloader._download`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-223)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/downloader/__init__.py:254` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-264"></a>

### `Downloader.close` · method
```python
def close(self) -> None
```

**内部调用(库内):**
- [`Downloader._stop_slot_gc`](scrapy_core.md#sym-scrapy_core_downloader___init__.py-281)

*来源: `scrapy/core/downloader/__init__.py:264` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-269"></a>

### `Downloader._slot_gc` · method
```python
def _slot_gc(self, age: float = 60) -> None
```

*来源: `scrapy/core/downloader/__init__.py:269` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-275"></a>

### `Downloader._start_slot_gc` · method
```python
def _start_slot_gc(self) -> None
```

**内部调用(库内):**
- [`create_looping_call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-217)

*来源: `scrapy/core/downloader/__init__.py:275` · 待生成*

---
<a id="sym-scrapy_core_downloader___init__.py-281"></a>

### `Downloader._stop_slot_gc` · method
```python
def _stop_slot_gc(self) -> None
```

*来源: `scrapy/core/downloader/__init__.py:281` · 待生成*

---

## `scrapy/core/downloader/contextfactory.py`

<a id="sym-scrapy_core_downloader_contextfactory.py-42"></a>

### `_ScrapyClientContextFactory` · class
装饰器: `@implementer(IPolicyForHTTPS)`
```python
class _ScrapyClientContextFactory(BrowserLikePolicyForHTTPS)
```

*来源: `scrapy/core/downloader/contextfactory.py:42` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-55"></a>

### `_ScrapyClientContextFactory.__init__` · method
```python
def __init__(
        self,
        method: int | None = SSL.SSLv23_METHOD,  # noqa: S503
        tls_verbose_logging: bool = False,
        tls_ciphers: str | None = None,
        *args: Any,
        verify_certificates: bool = False,
        tls_min_version: TLSVersion | None = None,
        tls_max_version: TLSVersion | None = None,
        **kwargs: Any,
    )
```

*来源: `scrapy/core/downloader/contextfactory.py:55` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-79"></a>

### `_ScrapyClientContextFactory.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls,
        crawler: Crawler,
        method: int | None = SSL.SSLv23_METHOD,  # noqa: S503
        *args: Any,
        **kwargs: Any,
    ) -> Self
```

**内部调用(库内):**
- [`_get_tls_version_limits`](scrapy_utils.md#sym-scrapy_utils_ssl.py-47)

*来源: `scrapy/core/downloader/contextfactory.py:79` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-110"></a>

### `_ScrapyClientContextFactory.getCertificateOptions` · method
```python
def getCertificateOptions(self) -> CertificateOptions
```

**内部调用(库内):**
- [`_ScrapyClientContextFactory._get_cert_options`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-113)

*来源: `scrapy/core/downloader/contextfactory.py:110` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-113"></a>

### `_ScrapyClientContextFactory._get_cert_options` · method
```python
def _get_cert_options(self) -> CertificateOptions
```

**内部调用(库内):**
- [`_ScrapyCertificateOptions`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-256)
- [`_ScrapyClientContextFactory._get_cert_options_kwargs`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-116)

*来源: `scrapy/core/downloader/contextfactory.py:113` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-116"></a>

### `_ScrapyClientContextFactory._get_cert_options_kwargs` · method
```python
def _get_cert_options_kwargs(self) -> dict[str, Any]
```

**内部调用(库内):**
- [`_get_cert_options_version_kwargs`](scrapy_utils.md#sym-scrapy_utils_ssl.py-241)

*来源: `scrapy/core/downloader/contextfactory.py:116` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-133"></a>

### `_ScrapyClientContextFactory.getContext` · method
```python
def getContext(
        self, hostname: Any = None, port: Any = None
    ) -> SSL.Context
```

**内部调用(库内):**
- [`_ScrapyClientContextFactory._get_context`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-138)

*来源: `scrapy/core/downloader/contextfactory.py:133` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-138"></a>

### `_ScrapyClientContextFactory._get_context` · method
```python
def _get_context(self) -> SSL.Context
```

**内部调用(库内):**
- [`_ScrapyClientContextFactory.getContext`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-133)
- [`_ScrapyClientContextFactory._get_cert_options`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-113)

*来源: `scrapy/core/downloader/contextfactory.py:138` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-141"></a>

### `_ScrapyClientContextFactory.creatorForNetloc` · method
```python
def creatorForNetloc(self, hostname: bytes, port: int) -> ClientTLSOptions
```

**内部调用(库内):**
- [`_ScrapyClientTLSOptions26`](scrapy_core.md#sym-scrapy_core_downloader_tls.py-121)
- [`_ScrapyClientContextFactory._get_cert_options`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-113)
- [`_ScrapyClientTLSOptions`](scrapy_core.md#sym-scrapy_core_downloader_tls.py-71)
- [`_ScrapyClientContextFactory._get_context`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-138)
- [`_ScrapyClientContextFactory._get_cert_options_kwargs`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-116)

*来源: `scrapy/core/downloader/contextfactory.py:141` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-169"></a>

### `BrowserLikeContextFactory` · class
装饰器: `@implementer(IPolicyForHTTPS)`
```python
class BrowserLikeContextFactory(_ScrapyClientContextFactory)
```

*来源: `scrapy/core/downloader/contextfactory.py:169` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-184"></a>

### `BrowserLikeContextFactory.__init__` · method
```python
def __init__(self, *args: Any, **kwargs: Any)
```

*来源: `scrapy/core/downloader/contextfactory.py:184` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-194"></a>

### `BrowserLikeContextFactory.creatorForNetloc` · method
```python
def creatorForNetloc(self, hostname: bytes, port: int) -> ClientTLSOptions
```

**内部调用(库内):**
- [`_ScrapyClientContextFactory._get_cert_options_kwargs`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-116)

*来源: `scrapy/core/downloader/contextfactory.py:194` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-202"></a>

### `_AcceptableProtocolsContextFactory` · class
装饰器: `@implementer(IPolicyForHTTPS)`
```python
class _AcceptableProtocolsContextFactory
```

*来源: `scrapy/core/downloader/contextfactory.py:202` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-230"></a>

### `_AcceptableProtocolsContextFactory.__init__` · method
```python
def __init__(self, context_factory: Any, acceptable_protocols: list[bytes])
```

*来源: `scrapy/core/downloader/contextfactory.py:230` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-235"></a>

### `_AcceptableProtocolsContextFactory.creatorForNetloc` · method
```python
def creatorForNetloc(self, hostname: bytes, port: int) -> ClientTLSOptions
```

*来源: `scrapy/core/downloader/contextfactory.py:235` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-256"></a>

### `_ScrapyCertificateOptions` · class
```python
class _ScrapyCertificateOptions(CertificateOptions)
```

*来源: `scrapy/core/downloader/contextfactory.py:256` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-259"></a>

### `_ScrapyCertificateOptions._makeContext` · method
```python
def _makeContext(self, skipCiphers: bool = False) -> SSL.Context
```

*来源: `scrapy/core/downloader/contextfactory.py:259` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-268"></a>

### `_load_context_factory_from_settings` · func
```python
def _load_context_factory_from_settings(crawler: Crawler) -> IPolicyForHTTPS
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/core/downloader/contextfactory.py:268` · 待生成*

---
<a id="sym-scrapy_core_downloader_contextfactory.py-304"></a>

### `load_context_factory_from_settings` · func
```python
def load_context_factory_from_settings(
    settings: BaseSettings, crawler: Crawler
) -> IPolicyForHTTPS
```

**内部调用(库内):**
- [`_load_context_factory_from_settings`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-268)

*来源: `scrapy/core/downloader/contextfactory.py:304` · 待生成*

---

## `scrapy/core/downloader/handlers/__init__.py`

<a id="sym-scrapy_core_downloader_handlers___init__.py-41"></a>

### `DownloadHandlerProtocol` · class
```python
class DownloadHandlerProtocol(Protocol)
```

*来源: `scrapy/core/downloader/handlers/__init__.py:41` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-44"></a>

### `DownloadHandlerProtocol.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

*来源: `scrapy/core/downloader/handlers/__init__.py:44` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-46"></a>

### `DownloadHandlerProtocol.close` · method
```python
async def close(self) -> None
```

*来源: `scrapy/core/downloader/handlers/__init__.py:46` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-49"></a>

### `DownloadHandlers` · class
```python
class DownloadHandlers
```

*来源: `scrapy/core/downloader/handlers/__init__.py:49` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-50"></a>

### `DownloadHandlers.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`BaseSettings.getwithbase`](scrapy_settings.md#sym-scrapy_settings___init__.py-319)
- [`DownloadHandlers._load_handler`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-86)

*来源: `scrapy/core/downloader/handlers/__init__.py:50` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-72"></a>

### `DownloadHandlers._get_handler` · method
```python
def _get_handler(self, scheme: str) -> DownloadHandlerProtocol | None
```

**内部调用(库内):**
- [`DownloadHandlers._load_handler`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-86)

*来源: `scrapy/core/downloader/handlers/__init__.py:72` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-86"></a>

### `DownloadHandlers._load_handler` · method
```python
def _load_handler(
        self, scheme: str, skip_lazy: bool = False
    ) -> DownloadHandlerProtocol | None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/core/downloader/handlers/__init__.py:86` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-131"></a>

### `DownloadHandlers.download_request` · method
```python
def download_request(
        self, request: Request, spider: Spider | None = None
    ) -> Deferred[Response]
```

**内部调用(库内):**
- [`DownloadHandlers.download_request_async`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-141)

*来源: `scrapy/core/downloader/handlers/__init__.py:131` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-141"></a>

### `DownloadHandlers.download_request_async` · method
```python
async def download_request_async(self, request: Request) -> Response
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`DownloadHandlers._get_handler`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-72)
- [`NotSupported`](scrapy.md#sym-scrapy_exceptions.py-101) — `NotSupported` 类代表一个异常，用于表示某些功能或操作不被支持。
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`DownloadHandlers.download_request`](scrapy_core.md#sym-scrapy_core_downloader_handlers___init__.py-131)

*来源: `scrapy/core/downloader/handlers/__init__.py:141` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers___init__.py-158"></a>

### `DownloadHandlers._close` · method
```python
async def _close(self) -> None
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/core/downloader/handlers/__init__.py:158` · 待生成*

---

## `scrapy/core/downloader/handlers/_base_http.py`

<a id="sym-scrapy_core_downloader_handlers__base_http.py-12"></a>

### `BaseHttpDownloadHandler` · class
```python
class BaseHttpDownloadHandler(BaseDownloadHandler, ABC)
```

*来源: `scrapy/core/downloader/handlers/_base_http.py:12` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_http.py-15"></a>

### `BaseHttpDownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/core/downloader/handlers/_base_http.py:15` · 待生成*

---

## `scrapy/core/downloader/handlers/_base_streaming.py`

<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-49"></a>

### `_BaseResponseArgs` · class
```python
class _BaseResponseArgs(TypedDict)
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:49` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-58"></a>

### `BaseStreamingDownloadHandler` · class
```python
class BaseStreamingDownloadHandler(BaseHttpDownloadHandler, ABC, Generic[_ResponseT])
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:58` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-68"></a>

### `BaseStreamingDownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`BaseStreamingDownloadHandler._check_deps_installed`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-95)
- [`normalize_bind_address`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-148)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:68` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-95"></a>

### `BaseStreamingDownloadHandler._check_deps_installed` · method
装饰器: `@staticmethod` `@abstractmethod`
```python
def _check_deps_installed() -> None
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:95` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-100"></a>

### `BaseStreamingDownloadHandler._make_request` · method
装饰器: `@abstractmethod`
```python
def _make_request(
        self, request: Request, timeout: float
    ) -> AbstractAsyncContextManager[_ResponseT]
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:100` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-111"></a>

### `BaseStreamingDownloadHandler._extract_headers` · method
装饰器: `@staticmethod` `@abstractmethod`
```python
def _extract_headers(response: _ResponseT) -> Headers
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:111` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-118"></a>

### `BaseStreamingDownloadHandler._build_base_response_args` · method
装饰器: `@staticmethod` `@abstractmethod`
```python
def _build_base_response_args(
        response: _ResponseT, request: Request, headers: Headers
    ) -> _BaseResponseArgs
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:118` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-126"></a>

### `BaseStreamingDownloadHandler._iter_body_chunks` · method
装饰器: `@staticmethod` `@abstractmethod`
```python
def _iter_body_chunks(response: _ResponseT) -> AsyncIterable[SizedBuffer]
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:126` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-132"></a>

### `BaseStreamingDownloadHandler._is_dataloss_exception` · method
装饰器: `@staticmethod` `@abstractmethod`
```python
def _is_dataloss_exception(exc: Exception) -> bool
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:132` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-136"></a>

### `BaseStreamingDownloadHandler._log_tls_info` · method
```python
def _log_tls_info(self, response: _ResponseT, request: Request) -> None
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:136` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-139"></a>

### `BaseStreamingDownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`BaseStreamingDownloadHandler._make_request`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-100)
- [`BaseStreamingDownloadHandler._read_response`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-157)

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:139` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-157"></a>

### `BaseStreamingDownloadHandler._read_response` · method
```python
async def _read_response(self, response: _ResponseT, request: Request) -> Response
```

**内部调用(库内):**
- [`BaseStreamingDownloadHandler._extract_headers`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-111)
- [`BaseStreamingDownloadHandler._cancel_maxsize`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-264)
- [`get_warnsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-132)
- [`BaseStreamingDownloadHandler._build_base_response_args`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-118)
- [`BaseStreamingDownloadHandler._log_tls_info`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-136)
- [`check_stop_download`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-70)
- [`BaseStreamingDownloadHandler._iter_body_chunks`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-126)
- [`BaseStreamingDownloadHandler._is_dataloss_exception`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-132)
- [`get_dataloss_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-140)
- [`ResponseDataLossError`](scrapy.md#sym-scrapy_exceptions.py-82) — `ResponseDataLossError` 类用于表示在请求响应过程中发生数据丢失的异常情况。

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:157` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-244"></a>

### `BaseStreamingDownloadHandler._get_bind_address_host` · method
```python
def _get_bind_address_host(self) -> str | None
```

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:244` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-264"></a>

### `BaseStreamingDownloadHandler._cancel_maxsize` · method
装饰器: `@staticmethod`
```python
def _cancel_maxsize(
        size: int, limit: int, request: Request, *, expected: bool
    ) -> NoReturn
```

**内部调用(库内):**
- [`get_maxsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-124)
- [`DownloadCancelledError`](scrapy.md#sym-scrapy_exceptions.py-74) — `DownloadCancelledError` 异常用于表示下载过程中被取消的情况。

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:264` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-272"></a>

### `BaseStreamingDownloadHandler._extract_proxy` · method
装饰器: `@staticmethod`
```python
def _extract_proxy(request: Request) -> tuple[str | None, str | None]
```

**内部调用(库内):**
- [`add_http_if_no_scheme`](scrapy_utils.md#sym-scrapy_utils_url.py-47)

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:272` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__base_streaming.py-287"></a>

### `BaseStreamingDownloadHandler._extract_proxy_url_with_creds` · method
```python
def _extract_proxy_url_with_creds(self, request: Request) -> str | None
```

**内部调用(库内):**
- [`BaseStreamingDownloadHandler._extract_proxy`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-272)

*来源: `scrapy/core/downloader/handlers/_base_streaming.py:287` · 待生成*

---

## `scrapy/core/downloader/handlers/_httpx.py`

<a id="sym-scrapy_core_downloader_handlers__httpx.py-76"></a>

### `HttpxDownloadHandler` · class
```python
class HttpxDownloadHandler(_Base)
```

*来源: `scrapy/core/downloader/handlers/_httpx.py:76` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-79"></a>

### `HttpxDownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`_make_ssl_context`](scrapy_utils.md#sym-scrapy_utils_ssl.py-66)
- [`BaseStreamingDownloadHandler._get_bind_address_host`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-244)
- [`HttpxDownloadHandler._make_client`](scrapy_core.md#sym-scrapy_core_downloader_handlers__httpx.py-110)

*来源: `scrapy/core/downloader/handlers/_httpx.py:79` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-104"></a>

### `HttpxDownloadHandler._check_deps_installed` · method
装饰器: `@staticmethod`
```python
def _check_deps_installed() -> None
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。

*来源: `scrapy/core/downloader/handlers/_httpx.py:104` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-110"></a>

### `HttpxDownloadHandler._make_client` · method
```python
def _make_client(self, proxy_url: str | None = None) -> httpx.AsyncClient
```

**内部调用(库内):**
- [`_make_insecure_ssl_ctx`](scrapy_utils.md#sym-scrapy_utils_ssl.py-95)
- [`NullCookieJar`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-41)

*来源: `scrapy/core/downloader/handlers/_httpx.py:110` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-136"></a>

### `HttpxDownloadHandler._get_client` · method
```python
def _get_client(self, proxy_url: str | None) -> httpx.AsyncClient
```

**内部调用(库内):**
- [`HttpxDownloadHandler._make_client`](scrapy_core.md#sym-scrapy_core_downloader_handlers__httpx.py-110)

*来源: `scrapy/core/downloader/handlers/_httpx.py:136` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-146"></a>

### `HttpxDownloadHandler._make_request` · method
装饰器: `@asynccontextmanager`
```python
async def _make_request(
        self, request: Request, timeout: float
    ) -> AsyncIterator[httpx.Response]
```

**内部调用(库内):**
- [`BaseStreamingDownloadHandler._extract_proxy_url_with_creds`](scrapy_core.md#sym-scrapy_core_downloader_handlers__base_streaming.py-287)
- [`HttpxDownloadHandler._get_client`](scrapy_core.md#sym-scrapy_core_downloader_handlers__httpx.py-136)
- [`Headers.to_tuple_list`](scrapy_http.md#sym-scrapy_http_headers.py-127)
- [`DownloadTimeoutError`](scrapy.md#sym-scrapy_exceptions.py-70) — `DownloadTimeoutError` 类代表在下载过程中发生超时错误的异常类型，用于标识网络请求因超时而失败的情况。
- [`UnsupportedURLSchemeError`](scrapy.md#sym-scrapy_exceptions.py-86) — `UnsupportedURLSchemeError` 异常类用于表示请求的 URL 使用了不支持的协议方案。
- [`_iter_exc_causes`](scrapy_utils.md#sym-scrapy_utils_python.py-364)
- [`CannotResolveHostError`](scrapy.md#sym-scrapy_exceptions.py-66) — CannotResolveHostError 类用于表示在爬取过程中无法解析主机名的错误，通常由网络请求失败引发。
- [`DownloadConnectionRefusedError`](scrapy.md#sym-scrapy_exceptions.py-62) — `DownloadConnectionRefusedError` 类代表在下载过程中连接被拒绝时抛出的异常，用于处理网络连接失败的错误情况。
- [`DownloadFailedError`](scrapy.md#sym-scrapy_exceptions.py-78) — `DownloadFailedError` 是一个异常类，用于表示下载失败时抛出的错误。

*来源: `scrapy/core/downloader/handlers/_httpx.py:146` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-181"></a>

### `HttpxDownloadHandler._extract_headers` · method
装饰器: `@staticmethod`
```python
def _extract_headers(response: httpx.Response) -> Headers
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/core/downloader/handlers/_httpx.py:181` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-185"></a>

### `HttpxDownloadHandler._build_base_response_args` · method
装饰器: `@staticmethod`
```python
def _build_base_response_args(
        response: httpx.Response,
        request: Request,
        headers: Headers,
    ) -> _BaseResponseArgs
```

*来源: `scrapy/core/downloader/handlers/_httpx.py:185` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-208"></a>

### `HttpxDownloadHandler._iter_body_chunks` · method
装饰器: `@staticmethod`
```python
def _iter_body_chunks(response: httpx.Response) -> AsyncIterator[bytes]
```

*来源: `scrapy/core/downloader/handlers/_httpx.py:208` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-212"></a>

### `HttpxDownloadHandler._is_dataloss_exception` · method
装饰器: `@staticmethod`
```python
def _is_dataloss_exception(exc: Exception) -> bool
```

*来源: `scrapy/core/downloader/handlers/_httpx.py:212` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-217"></a>

### `HttpxDownloadHandler._log_tls_info` · method
```python
def _log_tls_info(self, response: httpx.Response, request: Request) -> None
```

**内部调用(库内):**
- [`_log_sslobj_debug_info`](scrapy_utils.md#sym-scrapy_utils_ssl.py-107)

*来源: `scrapy/core/downloader/handlers/_httpx.py:217` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers__httpx.py-223"></a>

### `HttpxDownloadHandler.close` · method
```python
async def close(self) -> None
```

*来源: `scrapy/core/downloader/handlers/_httpx.py:223` · 待生成*

---

## `scrapy/core/downloader/handlers/base.py`

<a id="sym-scrapy_core_downloader_handlers_base.py-15"></a>

### `BaseDownloadHandler` · class
```python
class BaseDownloadHandler(ABC)
```

*来源: `scrapy/core/downloader/handlers/base.py:15` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_base.py-20"></a>

### `BaseDownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/core/downloader/handlers/base.py:20` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_base.py-24"></a>

### `BaseDownloadHandler.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/core/downloader/handlers/base.py:24` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_base.py-28"></a>

### `BaseDownloadHandler.download_request` · method
装饰器: `@abstractmethod`
```python
async def download_request(self, request: Request) -> Response
```

*来源: `scrapy/core/downloader/handlers/base.py:28` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_base.py-31"></a>

### `BaseDownloadHandler.close` · method
```python
async def close(self) -> None
```

*来源: `scrapy/core/downloader/handlers/base.py:31` · 待生成*

---

## `scrapy/core/downloader/handlers/datauri.py`

<a id="sym-scrapy_core_downloader_handlers_datauri.py-15"></a>

### `DataURIDownloadHandler` · class
```python
class DataURIDownloadHandler(BaseDownloadHandler)
```

*来源: `scrapy/core/downloader/handlers/datauri.py:15` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_datauri.py-16"></a>

### `DataURIDownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`ResponseTypes.from_mimetype`](scrapy.md#sym-scrapy_responsetypes.py-51)

*来源: `scrapy/core/downloader/handlers/datauri.py:16` · 待生成*

---

## `scrapy/core/downloader/handlers/file.py`

<a id="sym-scrapy_core_downloader_handlers_file.py-17"></a>

### `FileDownloadHandler` · class
```python
class FileDownloadHandler(BaseDownloadHandler)
```

*来源: `scrapy/core/downloader/handlers/file.py:17` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_file.py-18"></a>

### `FileDownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)
- [`ResponseTypes.from_args`](scrapy.md#sym-scrapy_responsetypes.py-124)

*来源: `scrapy/core/downloader/handlers/file.py:18` · 待生成*

---

## `scrapy/core/downloader/handlers/ftp.py`

<a id="sym-scrapy_core_downloader_handlers_ftp.py-55"></a>

### `ReceivedDataProtocol` · class
```python
class ReceivedDataProtocol(Protocol)
```

*来源: `scrapy/core/downloader/handlers/ftp.py:55` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-56"></a>

### `ReceivedDataProtocol.__init__` · method
```python
def __init__(self, filename: bytes | None = None)
```

*来源: `scrapy/core/downloader/handlers/ftp.py:56` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-63"></a>

### `ReceivedDataProtocol.dataReceived` · method
```python
def dataReceived(self, data: bytes) -> None
```

*来源: `scrapy/core/downloader/handlers/ftp.py:63` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-68"></a>

### `ReceivedDataProtocol.filename` · method
装饰器: `@property`
```python
def filename(self) -> bytes | None
```

*来源: `scrapy/core/downloader/handlers/ftp.py:68` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-71"></a>

### `ReceivedDataProtocol.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/core/downloader/handlers/ftp.py:71` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-81"></a>

### `FTPDownloadHandler` · class
```python
class FTPDownloadHandler(BaseDownloadHandler)
```

*来源: `scrapy/core/downloader/handlers/ftp.py:81` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-87"></a>

### `FTPDownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。

*来源: `scrapy/core/downloader/handlers/ftp.py:87` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_ftp.py-95"></a>

### `FTPDownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`ReceivedDataProtocol`](scrapy_core.md#sym-scrapy_core_downloader_handlers_ftp.py-55)
- [`Response`](scrapy_http.md#sym-scrapy_http_response___init__.py-35)
- [`ResponseTypes.from_args`](scrapy.md#sym-scrapy_responsetypes.py-124)

*来源: `scrapy/core/downloader/handlers/ftp.py:95` · 待生成*

---

## `scrapy/core/downloader/handlers/http11.py`

<a id="sym-scrapy_core_downloader_handlers_http11.py-76"></a>

### `_ResultT` · class
```python
class _ResultT(TypedDict)
```

*来源: `scrapy/core/downloader/handlers/http11.py:76` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-85"></a>

### `HTTP11DownloadHandler` · class
```python
class HTTP11DownloadHandler(BaseHttpDownloadHandler)
```

*来源: `scrapy/core/downloader/handlers/http11.py:85` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-86"></a>

### `HTTP11DownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`_load_context_factory_from_settings`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-268)

*来源: `scrapy/core/downloader/handlers/http11.py:86` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-106"></a>

### `HTTP11DownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`warn_on_deprecated_spider_attribute`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-225)
- [`_ScrapyAgent`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-385)
- [`wrap_twisted_exceptions`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-52)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`get_dataloss_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-140)

*来源: `scrapy/core/downloader/handlers/http11.py:106` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-138"></a>

### `HTTP11DownloadHandler.close` · method
```python
async def close(self) -> None
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/downloader/handlers/http11.py:138` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-161"></a>

### `TunnelError` · class
```python
class TunnelError(Exception)
```

*来源: `scrapy/core/downloader/handlers/http11.py:161` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-165"></a>

### `_TunnelingTCP4ClientEndpoint` · class
```python
class _TunnelingTCP4ClientEndpoint(TCP4ClientEndpoint)
```

*来源: `scrapy/core/downloader/handlers/http11.py:165` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-180"></a>

### `_TunnelingTCP4ClientEndpoint.__init__` · method
```python
def __init__(
        self,
        reactor: ReactorBase,
        host: str,
        port: int,
        proxyConf: tuple[str, int, bytes | None],
        contextFactory: IPolicyForHTTPS,
        timeout: float = 30,
        bindAddress: tuple[str, int] | None = None,
    )
```

*来源: `scrapy/core/downloader/handlers/http11.py:180` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-198"></a>

### `_TunnelingTCP4ClientEndpoint.requestTunnel` · method
```python
def requestTunnel(self, protocol: Protocol) -> Protocol
```

**内部调用(库内):**
- [`_tunnel_request_data`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-262)

*来源: `scrapy/core/downloader/handlers/http11.py:198` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-210"></a>

### `_TunnelingTCP4ClientEndpoint.processProxyResponse` · method
```python
def processProxyResponse(self, data: bytes) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)
- [`TunnelError`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-161)

*来源: `scrapy/core/downloader/handlers/http11.py:210` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-250"></a>

### `_TunnelingTCP4ClientEndpoint.connectFailed` · method
```python
def connectFailed(self, reason: Failure) -> None
```

*来源: `scrapy/core/downloader/handlers/http11.py:250` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-254"></a>

### `_TunnelingTCP4ClientEndpoint.connect` · method
```python
def connect(self, protocolFactory: Factory) -> Deferred[Protocol]
```

*来源: `scrapy/core/downloader/handlers/http11.py:254` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-262"></a>

### `_tunnel_request_data` · func
```python
def _tunnel_request_data(
    host: str, port: int, proxy_auth_header: bytes | None = None
) -> bytes
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/core/downloader/handlers/http11.py:262` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-285"></a>

### `_TunnelingAgent` · class
```python
class _TunnelingAgent(Agent)
```

*来源: `scrapy/core/downloader/handlers/http11.py:285` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-293"></a>

### `_TunnelingAgent.__init__` · method
```python
def __init__(
        self,
        *,
        reactor: ReactorBase,
        proxyConf: tuple[str, int, bytes | None],
        contextFactory: IPolicyForHTTPS,
        connectTimeout: float | None = None,
        bindAddress: tuple[str, int] | None = None,
        pool: HTTPConnectionPool | None = None,
    )
```

*来源: `scrapy/core/downloader/handlers/http11.py:293` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-307"></a>

### `_TunnelingAgent._getEndpoint` · method
```python
def _getEndpoint(self, uri: URI) -> _TunnelingTCP4ClientEndpoint
```

**内部调用(库内):**
- [`_TunnelingTCP4ClientEndpoint`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-165)

*来源: `scrapy/core/downloader/handlers/http11.py:307` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-318"></a>

### `_TunnelingAgent._requestWithEndpoint` · method
```python
def _requestWithEndpoint(
        self,
        key: Any,
        endpoint: TCP4ClientEndpoint,
        method: bytes,
        parsedURI: URI,
        headers: TxHeaders | None,
        bodyProducer: IBodyProducer | None,
        requestPath: bytes,
    ) -> Deferred[IResponse]
```

*来源: `scrapy/core/downloader/handlers/http11.py:318` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-343"></a>

### `_ScrapyProxyAgent` · class
```python
class _ScrapyProxyAgent(Agent)
```

*来源: `scrapy/core/downloader/handlers/http11.py:343` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-344"></a>

### `_ScrapyProxyAgent.__init__` · method
```python
def __init__(
        self,
        reactor: ReactorBase,
        proxyURI: bytes,
        contextFactory: IPolicyForHTTPS,
        connectTimeout: float | None = None,
        bindAddress: tuple[str, int] | None = None,
        pool: HTTPConnectionPool | None = None,
    )
```

*来源: `scrapy/core/downloader/handlers/http11.py:344` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-362"></a>

### `_ScrapyProxyAgent.request` · method
```python
def request(
        self,
        method: bytes,
        uri: bytes,
        headers: TxHeaders | None = None,
        bodyProducer: IBodyProducer | None = None,
    ) -> Deferred[IResponse]
```

**内部调用(库内):**
- [`_TunnelingAgent._requestWithEndpoint`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-318)
- [`_TunnelingAgent._getEndpoint`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-307)

*来源: `scrapy/core/downloader/handlers/http11.py:362` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-385"></a>

### `_ScrapyAgent` · class
```python
class _ScrapyAgent
```

*来源: `scrapy/core/downloader/handlers/http11.py:385` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-386"></a>

### `_ScrapyAgent.__init__` · method
```python
def __init__(
        self,
        *,
        contextFactory: IPolicyForHTTPS,
        connectTimeout: float = 10,
        bindAddress: str | tuple[str, int] | None = None,
        pool: HTTPConnectionPool | None = None,
        maxsize: int = 0,
        warnsize: int = 0,
        fail_on_dataloss: bool = True,
        crawler: Crawler,
        tls_verbose_logging: bool = False,
    )
```

*来源: `scrapy/core/downloader/handlers/http11.py:386` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-410"></a>

### `_ScrapyAgent._get_agent` · method
```python
def _get_agent(self, request: Request, timeout: float) -> Agent
```

**内部调用(库内):**
- [`normalize_bind_address`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-148)
- [`add_http_if_no_scheme`](scrapy_utils.md#sym-scrapy_utils_url.py-47)
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`_TunnelingAgent`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-285)
- [`_ScrapyProxyAgent`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-343)
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/core/downloader/handlers/http11.py:410` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-456"></a>

### `_ScrapyAgent.download_request` · method
```python
def download_request(self, request: Request) -> Deferred[Response]
```

**内部调用(库内):**
- [`_ScrapyAgent._get_agent`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-410)
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`_RequestBodyProducer`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-601)
- [`_ScrapyProxyAgent.request`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-362)

*来源: `scrapy/core/downloader/handlers/http11.py:456` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-486"></a>

### `_ScrapyAgent._cb_timeout` · method
```python
def _cb_timeout(self, result: _T, request: Request, url: str, timeout: float) -> _T
```

**内部调用(库内):**
- [`_RequestBodyProducer.stopProducing`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-613)
- [`DownloadTimeoutError`](scrapy.md#sym-scrapy_exceptions.py-70) — `DownloadTimeoutError` 类代表在下载过程中发生超时错误的异常类型，用于标识网络请求因超时而失败的情况。

*来源: `scrapy/core/downloader/handlers/http11.py:486` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-497"></a>

### `_ScrapyAgent._cb_latency` · method
```python
def _cb_latency(self, result: _T, request: Request, start_time: float) -> _T
```

*来源: `scrapy/core/downloader/handlers/http11.py:497` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-502"></a>

### `_ScrapyAgent._headers_from_twisted_response` · method
装饰器: `@staticmethod`
```python
def _headers_from_twisted_response(response: TxResponse) -> Headers
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/core/downloader/handlers/http11.py:502` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-509"></a>

### `_ScrapyAgent._cb_bodyready` · method
```python
def _cb_bodyready(
        self, txresponse: TxResponse, request: Request
    ) -> _ResultT | Deferred[_ResultT]
```

**内部调用(库内):**
- [`check_stop_download`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-70)
- [`_ScrapyAgent._headers_from_twisted_response`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-502)
- [`_RequestBodyProducer.stopProducing`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-613)
- [`get_maxsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-124)
- [`DownloadCancelledError`](scrapy.md#sym-scrapy_exceptions.py-74) — `DownloadCancelledError` 异常用于表示下载过程中被取消的情况。
- [`get_warnsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-132)
- [`_ResponseReader`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-617)

*来源: `scrapy/core/downloader/handlers/http11.py:509` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-576"></a>

### `_ScrapyAgent._cancel` · method
装饰器: `@staticmethod`
```python
def _cancel(_: Any, txresponse: TxResponse) -> None
```

*来源: `scrapy/core/downloader/handlers/http11.py:576` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-580"></a>

### `_ScrapyAgent._cb_bodydone` · method
```python
def _cb_bodydone(self, result: _ResultT, url: str) -> Response
```

**内部调用(库内):**
- [`_ScrapyAgent._headers_from_twisted_response`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-502)
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/core/downloader/handlers/http11.py:580` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-601"></a>

### `_RequestBodyProducer` · class
装饰器: `@implementer(IBodyProducer)`
```python
class _RequestBodyProducer
```

*来源: `scrapy/core/downloader/handlers/http11.py:601` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-602"></a>

### `_RequestBodyProducer.__init__` · method
```python
def __init__(self, body: bytes)
```

*来源: `scrapy/core/downloader/handlers/http11.py:602` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-606"></a>

### `_RequestBodyProducer.startProducing` · method
```python
def startProducing(self, consumer: IConsumer) -> Deferred[None]
```

*来源: `scrapy/core/downloader/handlers/http11.py:606` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-610"></a>

### `_RequestBodyProducer.pauseProducing` · method
```python
def pauseProducing(self) -> None
```

*来源: `scrapy/core/downloader/handlers/http11.py:610` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-613"></a>

### `_RequestBodyProducer.stopProducing` · method
```python
def stopProducing(self) -> None
```

*来源: `scrapy/core/downloader/handlers/http11.py:613` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-617"></a>

### `_ResponseReader` · class
```python
class _ResponseReader(Protocol)
```

*来源: `scrapy/core/downloader/handlers/http11.py:617` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-618"></a>

### `_ResponseReader.__init__` · method
```python
def __init__(
        self,
        finished: Deferred[_ResultT],
        txresponse: TxResponse,
        request: Request,
        maxsize: int,
        warnsize: int,
        fail_on_dataloss: bool,
        crawler: Crawler,
        *,
        tls_verbose_logging: bool = False,
    )
```

*来源: `scrapy/core/downloader/handlers/http11.py:618` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-644"></a>

### `_ResponseReader._finish_response` · method
```python
def _finish_response(
        self, flags: list[str] | None = None, stop_download: StopDownload | None = None
    ) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/downloader/handlers/http11.py:644` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-658"></a>

### `_ResponseReader.connectionMade` · method
```python
def connectionMade(self) -> None
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`_log_ssl_conn_debug_info`](scrapy_utils.md#sym-scrapy_utils_ssl.py-206)

*来源: `scrapy/core/downloader/handlers/http11.py:658` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-677"></a>

### `_ResponseReader.dataReceived` · method
```python
def dataReceived(self, data: bytes) -> None
```

**内部调用(库内):**
- [`check_stop_download`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-70)
- [`_RequestBodyProducer.stopProducing`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-613)
- [`_ResponseReader._finish_response`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-644)
- [`get_maxsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-124)
- [`get_warnsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-132)

*来源: `scrapy/core/downloader/handlers/http11.py:677` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http11.py-715"></a>

### `_ResponseReader.connectionLost` · method
```python
def connectionLost(self, reason: Failure = connectionDone) -> None
```

**内部调用(库内):**
- [`_ResponseReader._finish_response`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http11.py-644)
- [`ResponseDataLossError`](scrapy.md#sym-scrapy_exceptions.py-82) — `ResponseDataLossError` 类用于表示在请求响应过程中发生数据丢失的异常情况。

*来源: `scrapy/core/downloader/handlers/http11.py:715` · 待生成*

---

## `scrapy/core/downloader/handlers/http2.py`

<a id="sym-scrapy_core_downloader_handlers_http2.py-32"></a>

### `H2DownloadHandler` · class
```python
class H2DownloadHandler(BaseDownloadHandler)
```

*来源: `scrapy/core/downloader/handlers/http2.py:32` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-35"></a>

### `H2DownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`H2ConnectionPool`](scrapy_core.md#sym-scrapy_core_http2_agent.py-32)
- [`_load_context_factory_from_settings`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-268)

*来源: `scrapy/core/downloader/handlers/http2.py:35` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-47"></a>

### `H2DownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`UnsupportedURLSchemeError`](scrapy.md#sym-scrapy_exceptions.py-86) — `UnsupportedURLSchemeError` 异常类用于表示请求的 URL 使用了不支持的协议方案。
- [`_ScrapyH2Agent`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http2.py-68)
- [`wrap_twisted_exceptions`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-52)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/downloader/handlers/http2.py:47` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-64"></a>

### `H2DownloadHandler.close` · method
```python
async def close(self) -> None
```

**内部调用(库内):**
- [`H2ConnectionPool.close_connections`](scrapy_core.md#sym-scrapy_core_http2_agent.py-116)

*来源: `scrapy/core/downloader/handlers/http2.py:64` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-68"></a>

### `_ScrapyH2Agent` · class
```python
class _ScrapyH2Agent
```

*来源: `scrapy/core/downloader/handlers/http2.py:68` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-69"></a>

### `_ScrapyH2Agent.__init__` · method
```python
def __init__(
        self,
        context_factory: IPolicyForHTTPS,
        pool: H2ConnectionPool,
        connect_timeout: int = 10,
        bind_address: str | tuple[str, int] | None = None,
        crawler: Crawler | None = None,
    ) -> None
```

*来源: `scrapy/core/downloader/handlers/http2.py:69` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-83"></a>

### `_ScrapyH2Agent._get_agent` · method
```python
def _get_agent(self, request: Request, timeout: float | None) -> H2Agent
```

**内部调用(库内):**
- [`normalize_bind_address`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-148)
- [`H2Agent`](scrapy_core.md#sym-scrapy_core_http2_agent.py-127)

*来源: `scrapy/core/downloader/handlers/http2.py:83` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-98"></a>

### `_ScrapyH2Agent.download_request` · method
```python
def download_request(self, request: Request, spider: Spider) -> Deferred[Response]
```

**内部调用(库内):**
- [`_ScrapyH2Agent._get_agent`](scrapy_core.md#sym-scrapy_core_downloader_handlers_http2.py-83)

*来源: `scrapy/core/downloader/handlers/http2.py:98` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-113"></a>

### `_ScrapyH2Agent._cb_latency` · method
装饰器: `@staticmethod`
```python
def _cb_latency(
        response: Response, request: Request, start_time: float
    ) -> Response
```

*来源: `scrapy/core/downloader/handlers/http2.py:113` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_http2.py-120"></a>

### `_ScrapyH2Agent._cb_timeout` · method
装饰器: `@staticmethod`
```python
def _cb_timeout(
        response: Response, request: Request, timeout: float, timeout_cl: DelayedCall
    ) -> Response
```

**内部调用(库内):**
- [`DownloadTimeoutError`](scrapy.md#sym-scrapy_exceptions.py-70) — `DownloadTimeoutError` 类代表在下载过程中发生超时错误的异常类型，用于标识网络请求因超时而失败的情况。

*来源: `scrapy/core/downloader/handlers/http2.py:120` · 待生成*

---

## `scrapy/core/downloader/handlers/s3.py`

<a id="sym-scrapy_core_downloader_handlers_s3.py-19"></a>

### `S3DownloadHandler` · class
```python
class S3DownloadHandler(BaseDownloadHandler)
```

*来源: `scrapy/core/downloader/handlers/s3.py:19` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_s3.py-22"></a>

### `S3DownloadHandler.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`is_botocore_available`](scrapy_utils.md#sym-scrapy_utils_boto.py-4)
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`BaseSettings.getwithbase`](scrapy_settings.md#sym-scrapy_settings___init__.py-319)

*来源: `scrapy/core/downloader/handlers/s3.py:22` · 待生成*

---
<a id="sym-scrapy_core_downloader_handlers_s3.py-50"></a>

### `S3DownloadHandler.download_request` · method
```python
async def download_request(self, request: Request) -> Response
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`Headers.to_unicode_dict`](scrapy_http.md#sym-scrapy_http_headers.py-115)

*来源: `scrapy/core/downloader/handlers/s3.py:50` · 待生成*

---

## `scrapy/core/downloader/middleware.py`

<a id="sym-scrapy_core_downloader_middleware.py-34"></a>

### `DownloaderMiddlewareManager` · class
```python
class DownloaderMiddlewareManager(MiddlewareManager)
```

*来源: `scrapy/core/downloader/middleware.py:34` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-38"></a>

### `DownloaderMiddlewareManager._get_mwlist_from_settings` · method
装饰器: `@classmethod`
```python
def _get_mwlist_from_settings(cls, settings: BaseSettings) -> list[Any]
```

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`BaseSettings.get_component_priority_dict_with_base`](scrapy_settings.md#sym-scrapy_settings___init__.py-338)

*来源: `scrapy/core/downloader/middleware.py:38` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-43"></a>

### `DownloaderMiddlewareManager._add_middleware` · method
```python
def _add_middleware(self, mw: Any) -> None
```

**内部调用(库内):**
- [`MiddlewareManager._check_mw_method_spider_arg`](scrapy.md#sym-scrapy_middleware.py-119)

*来源: `scrapy/core/downloader/middleware.py:43` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-54"></a>

### `DownloaderMiddlewareManager.download` · method
```python
def download(
        self,
        download_func: Callable[[Request, Spider], Deferred[Response]],
        request: Request,
        spider: Spider,
    ) -> Deferred[Response | Request]
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`MiddlewareManager._set_compat_spider`](scrapy.md#sym-scrapy_middleware.py-70)
- [`DownloaderMiddlewareManager.download_async`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-73)

*来源: `scrapy/core/downloader/middleware.py:54` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-67"></a>

### `DownloaderMiddlewareManager.download_func_wrapped` · method
装饰器: `@wraps(download_func)`
```python
async def download_func_wrapped(request: Request) -> Response
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/downloader/middleware.py:67` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-73"></a>

### `DownloaderMiddlewareManager.download_async` · method
```python
async def download_async(
        self,
        download_func: Callable[[Request], Coroutine[Any, Any, Response]],
        request: Request,
    ) -> Response | Request
```

**内部调用(库内):**
- [`DownloaderMiddlewareManager._process_request`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-96)
- [`_defer_sleep_async`](scrapy_utils.md#sym-scrapy_utils_defer.py-89)
- [`DownloaderMiddlewareManager._process_exception`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-140)
- [`DownloaderMiddlewareManager._process_response`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-116)

*来源: `scrapy/core/downloader/middleware.py:73` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-90"></a>

### `DownloaderMiddlewareManager._handle_mw_method` · method
```python
def _handle_mw_method(self, method: Callable[..., Any], **kwargs: Any) -> Any
```

*来源: `scrapy/core/downloader/middleware.py:90` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-96"></a>

### `DownloaderMiddlewareManager._process_request` · method
```python
async def _process_request(
        self,
        request: Request,
        download_func: Callable[[Request], Coroutine[Any, Any, Response]],
    ) -> Response | Request
```

**内部调用(库内):**
- [`DownloaderMiddlewareManager._handle_mw_method`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-90)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`_InvalidOutput`](scrapy.md#sym-scrapy_exceptions.py-22) — 这个类 `_InvalidOutput` 是一个类型错误的子类，用于表示爬虫输出数据无效的情况。

*来源: `scrapy/core/downloader/middleware.py:96` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-116"></a>

### `DownloaderMiddlewareManager._process_response` · method
```python
async def _process_response(
        self, response: Response | Request, request: Request
    ) -> Response | Request
```

**内部调用(库内):**
- [`DownloaderMiddlewareManager._handle_mw_method`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-90)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`_InvalidOutput`](scrapy.md#sym-scrapy_exceptions.py-22) — 这个类 `_InvalidOutput` 是一个类型错误的子类，用于表示爬虫输出数据无效的情况。

*来源: `scrapy/core/downloader/middleware.py:116` · 待生成*

---
<a id="sym-scrapy_core_downloader_middleware.py-140"></a>

### `DownloaderMiddlewareManager._process_exception` · method
```python
async def _process_exception(
        self, exception: Exception, request: Request | Response
    ) -> Response | Request
```

**内部调用(库内):**
- [`DownloaderMiddlewareManager._handle_mw_method`](scrapy_core.md#sym-scrapy_core_downloader_middleware.py-90)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`_InvalidOutput`](scrapy.md#sym-scrapy_exceptions.py-22) — 这个类 `_InvalidOutput` 是一个类型错误的子类，用于表示爬虫输出数据无效的情况。

*来源: `scrapy/core/downloader/middleware.py:140` · 待生成*

---

## `scrapy/core/downloader/tls.py`

<a id="sym-scrapy_core_downloader_tls.py-45"></a>

### `__getattr__` · func
```python
def __getattr__(name: str) -> Any
```

*来源: `scrapy/core/downloader/tls.py:45` · 待生成*

---
<a id="sym-scrapy_core_downloader_tls.py-71"></a>

### `_ScrapyClientTLSOptions` · class
```python
class _ScrapyClientTLSOptions(ClientTLSOptions)
```

*来源: `scrapy/core/downloader/tls.py:71` · 待生成*

---
<a id="sym-scrapy_core_downloader_tls.py-87"></a>

### `_ScrapyClientTLSOptions._identityVerifyingInfoCallback` · method
```python
def _identityVerifyingInfoCallback(
        self, connection: SSL.Connection, where: int, ret: Any
    ) -> None
```

*来源: `scrapy/core/downloader/tls.py:87` · 待生成*

---
<a id="sym-scrapy_core_downloader_tls.py-121"></a>

### `_ScrapyClientTLSOptions26` · class
```python
class _ScrapyClientTLSOptions26(ClientTLSOptions)
```

*来源: `scrapy/core/downloader/tls.py:121` · 待生成*

---
<a id="sym-scrapy_core_downloader_tls.py-137"></a>

### `_ScrapyClientTLSOptions26.clientConnectionForTLS` · method
```python
def clientConnectionForTLS(
        self, tlsProtocol: TLSMemoryBIOProtocol
    ) -> SSL.Connection
```

**内部调用(库内):**
- [`_ScrapyClientTLSOptions26._verifyCB`](scrapy_core.md#sym-scrapy_core_downloader_tls.py-147)

*来源: `scrapy/core/downloader/tls.py:137` · 待生成*

---
<a id="sym-scrapy_core_downloader_tls.py-147"></a>

### `_ScrapyClientTLSOptions26._verifyCB` · method
装饰器: `@staticmethod`
```python
def _verifyCB(
        hostIsDNS: bool, hostnameASCII: str
    ) -> Callable[[SSL.Connection, X509, int, int, int], bool]
```

*来源: `scrapy/core/downloader/tls.py:147` · 待生成*

---
<a id="sym-scrapy_core_downloader_tls.py-154"></a>

### `_ScrapyClientTLSOptions26.verifyCallback` · method
```python
def verifyCallback(
            conn: SSL.Connection, cert: X509, err: int, depth: int, ok: int
        ) -> bool
```

*来源: `scrapy/core/downloader/tls.py:154` · 待生成*

---

## `scrapy/core/engine.py`

<a id="sym-scrapy_core_engine.py-65"></a>

### `_Slot` · class
```python
class _Slot
```

*来源: `scrapy/core/engine.py:65` · 待生成*

---
<a id="sym-scrapy_core_engine.py-66"></a>

### `_Slot.__init__` · method
```python
def __init__(
        self,
        close_if_idle: bool,
        nextcall: CallLaterOnce[None],
        scheduler: BaseScheduler,
    ) -> None
```

**内部调用(库内):**
- [`create_looping_call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-217)

*来源: `scrapy/core/engine.py:66` · 待生成*

---
<a id="sym-scrapy_core_engine.py-81"></a>

### `_Slot.add_request` · method
```python
def add_request(self, request: Request) -> None
```

*来源: `scrapy/core/engine.py:81` · 待生成*

---
<a id="sym-scrapy_core_engine.py-84"></a>

### `_Slot.remove_request` · method
```python
def remove_request(self, request: Request) -> None
```

**内部调用(库内):**
- [`_Slot._maybe_fire_closing`](scrapy_core.md#sym-scrapy_core_engine.py-93)

*来源: `scrapy/core/engine.py:84` · 待生成*

---
<a id="sym-scrapy_core_engine.py-88"></a>

### `_Slot.close` · method
```python
async def close(self) -> None
```

**内部调用(库内):**
- [`_Slot._maybe_fire_closing`](scrapy_core.md#sym-scrapy_core_engine.py-93)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/engine.py:88` · 待生成*

---
<a id="sym-scrapy_core_engine.py-93"></a>

### `_Slot._maybe_fire_closing` · method
```python
def _maybe_fire_closing(self) -> None
```

**内部调用(库内):**
- [`ExecutionEngine.stop`](scrapy_core.md#sym-scrapy_core_engine.py-205)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/engine.py:93` · 待生成*

---
<a id="sym-scrapy_core_engine.py-102"></a>

### `ExecutionEngine` · class
```python
class ExecutionEngine
```

*来源: `scrapy/core/engine.py:102` · 待生成*

---
<a id="sym-scrapy_core_engine.py-105"></a>

### `ExecutionEngine.__init__` · method
```python
def __init__(
        self,
        crawler: Crawler,
        spider_closed_callback: Callable[
            [Spider], Coroutine[Any, Any, None] | Deferred[None] | None
        ],
    ) -> None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`ExecutionEngine._get_scheduler_class`](scrapy_core.md#sym-scrapy_core_engine.py-155)
- [`argument_is_required`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-203)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`Scraper`](scrapy_core.md#sym-scrapy_core_scraper.py-102)

*来源: `scrapy/core/engine.py:105` · 待生成*

---
<a id="sym-scrapy_core_engine.py-155"></a>

### `ExecutionEngine._get_scheduler_class` · method
```python
def _get_scheduler_class(self, settings: BaseSettings) -> type[BaseScheduler]
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/core/engine.py:155` · 待生成*

---
<a id="sym-scrapy_core_engine.py-164"></a>

### `ExecutionEngine.start` · method
```python
def start(
        self, _start_request_processing: bool = True
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`ExecutionEngine.start_async`](scrapy_core.md#sym-scrapy_core_engine.py-176)

*来源: `scrapy/core/engine.py:164` · 待生成*

---
<a id="sym-scrapy_core_engine.py-176"></a>

### `ExecutionEngine.start_async` · method
```python
async def start_async(self, *, _start_request_processing: bool = True) -> None
```

**内部调用(库内):**
- [`ExecutionEngine._start_request_processing`](scrapy_core.md#sym-scrapy_core_engine.py-299)
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/engine.py:176` · 待生成*

---
<a id="sym-scrapy_core_engine.py-205"></a>

### `ExecutionEngine.stop` · method
```python
def stop(self) -> Deferred[None]
```

**内部调用(库内):**
- [`ExecutionEngine.stop_async`](scrapy_core.md#sym-scrapy_core_engine.py-213)

*来源: `scrapy/core/engine.py:205` · 待生成*

---
<a id="sym-scrapy_core_engine.py-213"></a>

### `ExecutionEngine.stop_async` · method
```python
async def stop_async(self) -> None
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`ExecutionEngine.close_spider_async`](scrapy_core.md#sym-scrapy_core_engine.py-595)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/engine.py:213` · 待生成*

---
<a id="sym-scrapy_core_engine.py-241"></a>

### `ExecutionEngine.close` · method
```python
def close(self) -> Deferred[None]
```

**内部调用(库内):**
- [`ExecutionEngine.close_async`](scrapy_core.md#sym-scrapy_core_engine.py-249)

*来源: `scrapy/core/engine.py:241` · 待生成*

---
<a id="sym-scrapy_core_engine.py-249"></a>

### `ExecutionEngine.close_async` · method
```python
async def close_async(self) -> None
```

**内部调用(库内):**
- [`ExecutionEngine.stop_async`](scrapy_core.md#sym-scrapy_core_engine.py-213)
- [`ExecutionEngine.close_spider_async`](scrapy_core.md#sym-scrapy_core_engine.py-595)

*来源: `scrapy/core/engine.py:249` · 待生成*

---
<a id="sym-scrapy_core_engine.py-263"></a>

### `ExecutionEngine.pause` · method
```python
def pause(self) -> None
```

*来源: `scrapy/core/engine.py:263` · 待生成*

---
<a id="sym-scrapy_core_engine.py-266"></a>

### `ExecutionEngine.unpause` · method
```python
def unpause(self) -> None
```

*来源: `scrapy/core/engine.py:266` · 待生成*

---
<a id="sym-scrapy_core_engine.py-269"></a>

### `ExecutionEngine._process_start_next` · method
```python
async def _process_start_next(self) -> None
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`ExecutionEngine.crawl`](scrapy_core.md#sym-scrapy_core_engine.py-433)
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`Scraper.start_itemproc_async`](scrapy_core.md#sym-scrapy_core_scraper.py-480)
- [`CallLaterOnce.schedule`](scrapy_utils.md#sym-scrapy_utils_reactor.py-62)

*来源: `scrapy/core/engine.py:269` · 待生成*

---
<a id="sym-scrapy_core_engine.py-299"></a>

### `ExecutionEngine._start_request_processing` · method
```python
async def _start_request_processing(self) -> None
```

**内部调用(库内):**
- [`CallLaterOnce.schedule`](scrapy_utils.md#sym-scrapy_utils_reactor.py-62)
- [`ExecutionEngine.start`](scrapy_core.md#sym-scrapy_core_engine.py-164)
- [`ExecutionEngine._process_start_next`](scrapy_core.md#sym-scrapy_core_engine.py-269)
- [`ExecutionEngine.needs_backout`](scrapy_core.md#sym-scrapy_core_engine.py-341)
- [`CallLaterOnce.wait`](scrapy_utils.md#sym-scrapy_utils_reactor.py-86)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`ExecutionEngine.stop_async`](scrapy_core.md#sym-scrapy_core_engine.py-213)

*来源: `scrapy/core/engine.py:299` · 待生成*

---
<a id="sym-scrapy_core_engine.py-330"></a>

### `ExecutionEngine._start_scheduled_requests` · method
```python
def _start_scheduled_requests(self) -> None
```

**内部调用(库内):**
- [`ExecutionEngine.needs_backout`](scrapy_core.md#sym-scrapy_core_engine.py-341)
- [`ExecutionEngine._start_scheduled_request`](scrapy_core.md#sym-scrapy_core_engine.py-360)
- [`ExecutionEngine.spider_is_idle`](scrapy_core.md#sym-scrapy_core_engine.py-422)
- [`ExecutionEngine._spider_idle`](scrapy_core.md#sym-scrapy_core_engine.py-560)

*来源: `scrapy/core/engine.py:330` · 待生成*

---
<a id="sym-scrapy_core_engine.py-341"></a>

### `ExecutionEngine.needs_backout` · method
```python
def needs_backout(self) -> bool
```

*来源: `scrapy/core/engine.py:341` · 待生成*

---
<a id="sym-scrapy_core_engine.py-356"></a>

### `ExecutionEngine._remove_request` · method
```python
def _remove_request(self, _: Any, request: Request) -> None
```

**内部调用(库内):**
- [`_Slot.remove_request`](scrapy_core.md#sym-scrapy_core_engine.py-84)

*来源: `scrapy/core/engine.py:356` · 待生成*

---
<a id="sym-scrapy_core_engine.py-360"></a>

### `ExecutionEngine._start_scheduled_request` · method
```python
def _start_scheduled_request(self) -> bool
```

**内部调用(库内):**
- [`ExecutionEngine._download`](scrapy_core.md#sym-scrapy_core_engine.py-485)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)
- [`CallLaterOnce.schedule`](scrapy_utils.md#sym-scrapy_utils_reactor.py-62)

*来源: `scrapy/core/engine.py:360` · 待生成*

---
<a id="sym-scrapy_core_engine.py-399"></a>

### `ExecutionEngine._handle_downloader_output` · method
装饰器: `@inlineCallbacks`
```python
def _handle_downloader_output(
        self, result: Request | Response | Failure, request: Request
    ) -> Generator[Deferred[Any], Any, None]
```

**内部调用(库内):**
- [`ExecutionEngine.crawl`](scrapy_core.md#sym-scrapy_core_engine.py-433)
- [`Scraper.enqueue_scrape`](scrapy_core.md#sym-scrapy_core_scraper.py-217)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/core/engine.py:399` · 待生成*

---
<a id="sym-scrapy_core_engine.py-422"></a>

### `ExecutionEngine.spider_is_idle` · method
```python
def spider_is_idle(self) -> bool
```

*来源: `scrapy/core/engine.py:422` · 待生成*

---
<a id="sym-scrapy_core_engine.py-433"></a>

### `ExecutionEngine.crawl` · method
```python
def crawl(self, request: Request) -> None
```

**内部调用(库内):**
- [`ExecutionEngine._schedule_request`](scrapy_core.md#sym-scrapy_core_engine.py-440)
- [`CallLaterOnce.schedule`](scrapy_utils.md#sym-scrapy_utils_reactor.py-62)

*来源: `scrapy/core/engine.py:433` · 待生成*

---
<a id="sym-scrapy_core_engine.py-440"></a>

### `ExecutionEngine._schedule_request` · method
```python
def _schedule_request(self, request: Request) -> None
```

*来源: `scrapy/core/engine.py:440` · 待生成*

---
<a id="sym-scrapy_core_engine.py-455"></a>

### `ExecutionEngine.download` · method
```python
def download(self, request: Request) -> Deferred[Response]
```

**内部调用(库内):**
- [`ExecutionEngine.download_async`](scrapy_core.md#sym-scrapy_core_engine.py-464)

*来源: `scrapy/core/engine.py:455` · 待生成*

---
<a id="sym-scrapy_core_engine.py-464"></a>

### `ExecutionEngine.download_async` · method
```python
async def download_async(self, request: Request) -> Response
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`ExecutionEngine._download`](scrapy_core.md#sym-scrapy_core_engine.py-485)
- [`_Slot.remove_request`](scrapy_core.md#sym-scrapy_core_engine.py-84)

*来源: `scrapy/core/engine.py:464` · 待生成*

---
<a id="sym-scrapy_core_engine.py-485"></a>

### `ExecutionEngine._download` · method
装饰器: `@inlineCallbacks`
```python
def _download(
        self, request: Request
    ) -> Generator[Deferred[Any], Any, Response | Request]
```

**内部调用(库内):**
- [`_Slot.add_request`](scrapy_core.md#sym-scrapy_core_engine.py-81)
- [`logformatter_adapter`](scrapy_utils.md#sym-scrapy_utils_log.py-245)
- [`CallLaterOnce.schedule`](scrapy_utils.md#sym-scrapy_utils_reactor.py-62)

*来源: `scrapy/core/engine.py:485` · 待生成*

---
<a id="sym-scrapy_core_engine.py-520"></a>

### `ExecutionEngine.open_spider` · method
```python
def open_spider(
        self, spider: Spider, close_if_idle: bool = True
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`ExecutionEngine.open_spider_async`](scrapy_core.md#sym-scrapy_core_engine.py-530)

*来源: `scrapy/core/engine.py:520` · 待生成*

---
<a id="sym-scrapy_core_engine.py-530"></a>

### `ExecutionEngine.open_spider_async` · method
```python
async def open_spider_async(self, *, close_if_idle: bool = True) -> None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`CallLaterOnce`](scrapy_utils.md#sym-scrapy_utils_reactor.py-50)
- [`_Slot`](scrapy_core.md#sym-scrapy_core_engine.py-65)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`argument_is_required`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-203)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`ExecutionEngine.open_spider`](scrapy_core.md#sym-scrapy_core_engine.py-520)

*来源: `scrapy/core/engine.py:530` · 待生成*

---
<a id="sym-scrapy_core_engine.py-560"></a>

### `ExecutionEngine._spider_idle` · method
```python
def _spider_idle(self) -> None
```

**内部调用(库内):**
- [`ExecutionEngine.spider_is_idle`](scrapy_core.md#sym-scrapy_core_engine.py-422)
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`ExecutionEngine.close_spider_async`](scrapy_core.md#sym-scrapy_core_engine.py-595)

*来源: `scrapy/core/engine.py:560` · 待生成*

---
<a id="sym-scrapy_core_engine.py-585"></a>

### `ExecutionEngine.close_spider` · method
```python
def close_spider(
        self, spider: Spider, reason: str = "cancelled"
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`ExecutionEngine.close_spider_async`](scrapy_core.md#sym-scrapy_core_engine.py-595)

*来源: `scrapy/core/engine.py:585` · 待生成*

---
<a id="sym-scrapy_core_engine.py-595"></a>

### `ExecutionEngine.close_spider_async` · method
```python
async def close_spider_async(self, *, reason: str = "cancelled") -> None
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`argument_is_required`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-203)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`ExecutionEngine.close_spider`](scrapy_core.md#sym-scrapy_core_engine.py-585)

*来源: `scrapy/core/engine.py:595` · 待生成*

---

## `scrapy/core/http2/agent.py`

<a id="sym-scrapy_core_http2_agent.py-32"></a>

### `H2ConnectionPool` · class
```python
class H2ConnectionPool
```

*来源: `scrapy/core/http2/agent.py:32` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-33"></a>

### `H2ConnectionPool.__init__` · method
```python
def __init__(self, reactor: ReactorBase, settings: Settings) -> None
```

*来源: `scrapy/core/http2/agent.py:33` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-50"></a>

### `H2ConnectionPool.get_connection` · method
```python
def get_connection(
        self, key: ConnectionKeyT, uri: URI, endpoint: HostnameEndpoint
    ) -> Deferred[H2ClientProtocol]
```

**内部调用(库内):**
- [`H2ConnectionPool._new_connection`](scrapy_core.md#sym-scrapy_core_http2_agent.py-70)

*来源: `scrapy/core/http2/agent.py:50` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-70"></a>

### `H2ConnectionPool._new_connection` · method
```python
def _new_connection(
        self, key: ConnectionKeyT, uri: URI, endpoint: HostnameEndpoint
    ) -> Deferred[H2ClientProtocol]
```

**内部调用(库内):**
- [`H2ClientFactory`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-460)

*来源: `scrapy/core/http2/agent.py:70` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-91"></a>

### `H2ConnectionPool.put_connection` · method
```python
def put_connection(
        self, conn: H2ClientProtocol, key: ConnectionKeyT
    ) -> H2ClientProtocol
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/http2/agent.py:91` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-105"></a>

### `H2ConnectionPool._remove_connection` · method
```python
def _remove_connection(
        self, errors: list[BaseException], key: ConnectionKeyT
    ) -> None
```

*来源: `scrapy/core/http2/agent.py:105` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-116"></a>

### `H2ConnectionPool.close_connections` · method
```python
def close_connections(self) -> None
```

*来源: `scrapy/core/http2/agent.py:116` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-127"></a>

### `H2Agent` · class
```python
class H2Agent
```

*来源: `scrapy/core/http2/agent.py:127` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-128"></a>

### `H2Agent.__init__` · method
```python
def __init__(
        self,
        reactor: ReactorBase,
        pool: H2ConnectionPool,
        context_factory: BrowserLikePolicyForHTTPS = BrowserLikePolicyForHTTPS(),
```

**内部调用(库内):**
- [`_AcceptableProtocolsContextFactory`](scrapy_core.md#sym-scrapy_core_downloader_contextfactory.py-202)

*来源: `scrapy/core/http2/agent.py:128` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-145"></a>

### `H2Agent.get_endpoint` · method
```python
def get_endpoint(self, uri: URI) -> HostnameEndpoint
```

*来源: `scrapy/core/http2/agent.py:145` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-148"></a>

### `H2Agent.get_key` · method
```python
def get_key(self, uri: URI) -> ConnectionKeyT
```

*来源: `scrapy/core/http2/agent.py:148` · 待生成*

---
<a id="sym-scrapy_core_http2_agent.py-155"></a>

### `H2Agent.request` · method
```python
def request(self, request: Request, spider: Spider) -> Deferred[Response]
```

**内部调用(库内):**
- [`H2Agent.get_endpoint`](scrapy_core.md#sym-scrapy_core_http2_agent.py-145)
- [`H2Agent.get_key`](scrapy_core.md#sym-scrapy_core_http2_agent.py-148)
- [`H2ConnectionPool.get_connection`](scrapy_core.md#sym-scrapy_core_http2_agent.py-50)

*来源: `scrapy/core/http2/agent.py:155` · 待生成*

---

## `scrapy/core/http2/protocol.py`

<a id="sym-scrapy_core_http2_protocol.py-57"></a>

### `InvalidNegotiatedProtocol` · class
```python
class InvalidNegotiatedProtocol(H2Error)
```

*来源: `scrapy/core/http2/protocol.py:57` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-58"></a>

### `InvalidNegotiatedProtocol.__init__` · method
```python
def __init__(self, negotiated_protocol: bytes) -> None
```

*来源: `scrapy/core/http2/protocol.py:58` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-61"></a>

### `InvalidNegotiatedProtocol.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/core/http2/protocol.py:61` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-65"></a>

### `RemoteTerminatedConnection` · class
```python
class RemoteTerminatedConnection(H2Error)
```

*来源: `scrapy/core/http2/protocol.py:65` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-66"></a>

### `RemoteTerminatedConnection.__init__` · method
```python
def __init__(
        self,
        remote_ip_address: IPv4Address | IPv6Address | None,
        event: ConnectionTerminated,
    ) -> None
```

*来源: `scrapy/core/http2/protocol.py:66` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-74"></a>

### `RemoteTerminatedConnection.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/core/http2/protocol.py:74` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-78"></a>

### `MethodNotAllowed405` · class
```python
class MethodNotAllowed405(H2Error)
```

*来源: `scrapy/core/http2/protocol.py:78` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-79"></a>

### `MethodNotAllowed405.__init__` · method
```python
def __init__(self, remote_ip_address: IPv4Address | IPv6Address | None) -> None
```

*来源: `scrapy/core/http2/protocol.py:79` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-82"></a>

### `MethodNotAllowed405.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/core/http2/protocol.py:82` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-87"></a>

### `H2ClientProtocol` · class
装饰器: `@implementer(IHandshakeListener)`
```python
class H2ClientProtocol(Protocol, TimeoutMixin)
```

*来源: `scrapy/core/http2/protocol.py:87` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-90"></a>

### `H2ClientProtocol.__init__` · method
```python
def __init__(
        self,
        uri: URI,
        settings: Settings,
        conn_lost_deferred: Deferred[list[BaseException]],
        *,
        tls_verbose_logging: bool = False,
    ) -> None
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/core/http2/protocol.py:90` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-156"></a>

### `H2ClientProtocol.h2_connected` · method
装饰器: `@property`
```python
def h2_connected(self) -> bool
```

*来源: `scrapy/core/http2/protocol.py:156` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-165"></a>

### `H2ClientProtocol.allowed_max_concurrent_streams` · method
装饰器: `@property`
```python
def allowed_max_concurrent_streams(self) -> int
```

*来源: `scrapy/core/http2/protocol.py:165` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-176"></a>

### `H2ClientProtocol._send_pending_requests` · method
```python
def _send_pending_requests(self) -> None
```

**内部调用(库内):**
- [`Stream.initiate_request`](scrapy_core.md#sym-scrapy_core_http2_stream.py-260)
- [`H2ClientProtocol._write_to_transport`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-221)

*来源: `scrapy/core/http2/protocol.py:176` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-191"></a>

### `H2ClientProtocol.pop_stream` · method
```python
def pop_stream(self, stream_id: int) -> Stream
```

**内部调用(库内):**
- [`H2ClientProtocol._send_pending_requests`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-176)

*来源: `scrapy/core/http2/protocol.py:191` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-198"></a>

### `H2ClientProtocol._new_stream` · method
```python
def _new_stream(self, request: Request, spider: Spider) -> Stream
```

**内部调用(库内):**
- [`warn_on_deprecated_spider_attribute`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-225)
- [`Stream`](scrapy_core.md#sym-scrapy_core_http2_stream.py-86)

*来源: `scrapy/core/http2/protocol.py:198` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-221"></a>

### `H2ClientProtocol._write_to_transport` · method
```python
def _write_to_transport(self) -> None
```

*来源: `scrapy/core/http2/protocol.py:221` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-232"></a>

### `H2ClientProtocol.request` · method
```python
def request(self, request: Request, spider: Spider) -> Deferred[Response]
```

**内部调用(库内):**
- [`H2ClientProtocol._new_stream`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-198)
- [`H2ClientProtocol._send_pending_requests`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-176)

*来源: `scrapy/core/http2/protocol.py:232` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-249"></a>

### `H2ClientProtocol.connectionMade` · method
```python
def connectionMade(self) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol._write_to_transport`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-221)

*来源: `scrapy/core/http2/protocol.py:249` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-264"></a>

### `H2ClientProtocol._lose_connection_with_error` · method
```python
def _lose_connection_with_error(self, errors: list[BaseException]) -> None
```

*来源: `scrapy/core/http2/protocol.py:264` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-271"></a>

### `H2ClientProtocol.handshakeCompleted` · method
```python
def handshakeCompleted(self) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol._lose_connection_with_error`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-264)
- [`InvalidNegotiatedProtocol`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-57)
- [`_log_ssl_conn_debug_info`](scrapy_utils.md#sym-scrapy_utils_ssl.py-206)

*来源: `scrapy/core/http2/protocol.py:271` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-290"></a>

### `H2ClientProtocol._check_received_data` · method
```python
def _check_received_data(self, data: bytes) -> None
```

**内部调用(库内):**
- [`MethodNotAllowed405`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-78)

*来源: `scrapy/core/http2/protocol.py:290` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-300"></a>

### `H2ClientProtocol.dataReceived` · method
```python
def dataReceived(self, data: bytes) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol._check_received_data`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-290)
- [`Stream.receive_data`](scrapy_core.md#sym-scrapy_core_http2_stream.py-337)
- [`H2ClientProtocol._handle_events`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-376)
- [`H2ClientProtocol._lose_connection_with_error`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-264)
- [`H2ClientProtocol._write_to_transport`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-221)

*来源: `scrapy/core/http2/protocol.py:300` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-324"></a>

### `H2ClientProtocol.timeoutConnection` · method
```python
def timeoutConnection(self) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol._write_to_transport`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-221)
- [`H2ClientProtocol._lose_connection_with_error`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-264)
- [`DownloadTimeoutError`](scrapy.md#sym-scrapy_exceptions.py-70) — `DownloadTimeoutError` 类代表在下载过程中发生超时错误的异常类型，用于标识网络请求因超时而失败的情况。

*来源: `scrapy/core/http2/protocol.py:324` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-350"></a>

### `H2ClientProtocol.connectionLost` · method
```python
def connectionLost(self, reason: Failure = connectionDone) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/http2/protocol.py:350` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-376"></a>

### `H2ClientProtocol._handle_events` · method
```python
def _handle_events(self, events: list[Event]) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol.connection_terminated`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-402)
- [`H2ClientProtocol.data_received`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-407)
- [`H2ClientProtocol.response_received`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-415)
- [`H2ClientProtocol.stream_ended`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-434)
- [`H2ClientProtocol.stream_reset`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-442)
- [`H2ClientProtocol.window_updated`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-450)
- [`H2ClientProtocol.settings_acknowledged`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-423)

*来源: `scrapy/core/http2/protocol.py:376` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-402"></a>

### `H2ClientProtocol.connection_terminated` · method
```python
def connection_terminated(self, event: ConnectionTerminated) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol._lose_connection_with_error`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-264)
- [`RemoteTerminatedConnection`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-65)

*来源: `scrapy/core/http2/protocol.py:402` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-407"></a>

### `H2ClientProtocol.data_received` · method
```python
def data_received(self, event: DataReceived) -> None
```

**内部调用(库内):**
- [`Stream.receive_data`](scrapy_core.md#sym-scrapy_core_http2_stream.py-337)

*来源: `scrapy/core/http2/protocol.py:407` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-415"></a>

### `H2ClientProtocol.response_received` · method
```python
def response_received(self, event: ResponseReceived) -> None
```

**内部调用(库内):**
- [`Stream.receive_headers`](scrapy_core.md#sym-scrapy_core_http2_stream.py-364)

*来源: `scrapy/core/http2/protocol.py:415` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-423"></a>

### `H2ClientProtocol.settings_acknowledged` · method
```python
def settings_acknowledged(self, event: SettingsAcknowledged) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol._send_pending_requests`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-176)

*来源: `scrapy/core/http2/protocol.py:423` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-434"></a>

### `H2ClientProtocol.stream_ended` · method
```python
def stream_ended(self, event: StreamEnded) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol.pop_stream`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-191)

*来源: `scrapy/core/http2/protocol.py:434` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-442"></a>

### `H2ClientProtocol.stream_reset` · method
```python
def stream_reset(self, event: StreamReset) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol.pop_stream`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-191)

*来源: `scrapy/core/http2/protocol.py:442` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-450"></a>

### `H2ClientProtocol.window_updated` · method
```python
def window_updated(self, event: WindowUpdated) -> None
```

**内部调用(库内):**
- [`Stream.receive_window_update`](scrapy_core.md#sym-scrapy_core_http2_stream.py-325)

*来源: `scrapy/core/http2/protocol.py:450` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-460"></a>

### `H2ClientFactory` · class
装饰器: `@implementer(IProtocolNegotiationFactory)`
```python
class H2ClientFactory(Factory)
```

*来源: `scrapy/core/http2/protocol.py:460` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-461"></a>

### `H2ClientFactory.__init__` · method
```python
def __init__(
        self,
        uri: URI,
        settings: Settings,
        conn_lost_deferred: Deferred[list[BaseException]],
        *,
        tls_verbose_logging: bool = False,
    ) -> None
```

*来源: `scrapy/core/http2/protocol.py:461` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-474"></a>

### `H2ClientFactory.buildProtocol` · method
```python
def buildProtocol(self, addr: IAddress) -> H2ClientProtocol
```

**内部调用(库内):**
- [`H2ClientProtocol`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-87)

*来源: `scrapy/core/http2/protocol.py:474` · 待生成*

---
<a id="sym-scrapy_core_http2_protocol.py-482"></a>

### `H2ClientFactory.acceptableProtocols` · method
```python
def acceptableProtocols(self) -> list[bytes]
```

*来源: `scrapy/core/http2/protocol.py:482` · 待生成*

---

## `scrapy/core/http2/stream.py`

<a id="sym-scrapy_core_http2_stream.py-34"></a>

### `InactiveStreamClosed` · class
```python
class InactiveStreamClosed(ConnectionClosed)
```

*来源: `scrapy/core/http2/stream.py:34` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-39"></a>

### `InactiveStreamClosed.__init__` · method
```python
def __init__(self, request: Request) -> None
```

*来源: `scrapy/core/http2/stream.py:39` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-42"></a>

### `InactiveStreamClosed.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/core/http2/stream.py:42` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-46"></a>

### `InvalidHostname` · class
```python
class InvalidHostname(H2Error)
```

*来源: `scrapy/core/http2/stream.py:46` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-47"></a>

### `InvalidHostname.__init__` · method
```python
def __init__(
        self, request: Request, expected_hostname: str, expected_netloc: str
    ) -> None
```

*来源: `scrapy/core/http2/stream.py:47` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-54"></a>

### `InvalidHostname.__str__` · method
```python
def __str__(self) -> str
```

*来源: `scrapy/core/http2/stream.py:54` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-58"></a>

### `StreamCloseReason` · class
```python
class StreamCloseReason(Enum)
```

*来源: `scrapy/core/http2/stream.py:58` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-86"></a>

### `Stream` · class
```python
class Stream
```

*来源: `scrapy/core/http2/stream.py:86` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-97"></a>

### `Stream.__init__` · method
```python
def __init__(
        self,
        stream_id: int,
        request: Request,
        protocol: H2ClientProtocol,
        download_maxsize: int = 0,
        download_warnsize: int = 0,
    ) -> None
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/core/http2/stream.py:97` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-160"></a>

### `Stream._cancel` · method
```python
def _cancel(self, _: Any) -> None
```

**内部调用(库内):**
- [`Stream.reset_stream`](scrapy_core.md#sym-scrapy_core_http2_stream.py-385)

*来源: `scrapy/core/http2/stream.py:160` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-169"></a>

### `Stream.__repr__` · method
```python
def __repr__(self) -> str
```

*来源: `scrapy/core/http2/stream.py:169` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-173"></a>

### `Stream._log_warnsize` · method
装饰器: `@property`
```python
def _log_warnsize(self) -> bool
```

*来源: `scrapy/core/http2/stream.py:173` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-193"></a>

### `Stream.get_response` · method
```python
def get_response(self) -> Deferred[Response]
```

*来源: `scrapy/core/http2/stream.py:193` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-199"></a>

### `Stream.check_request_url` · method
```python
def check_request_url(self) -> bool
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/core/http2/stream.py:199` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-209"></a>

### `Stream._get_request_headers` · method
```python
def _get_request_headers(self) -> list[tuple[str, str]]
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/core/http2/stream.py:209` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-260"></a>

### `Stream.initiate_request` · method
```python
def initiate_request(self) -> None
```

**内部调用(库内):**
- [`Stream.check_request_url`](scrapy_core.md#sym-scrapy_core_http2_stream.py-199)
- [`Stream._get_request_headers`](scrapy_core.md#sym-scrapy_core_http2_stream.py-209)
- [`Stream.send_data`](scrapy_core.md#sym-scrapy_core_http2_stream.py-271)

*来源: `scrapy/core/http2/stream.py:260` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-271"></a>

### `Stream.send_data` · method
```python
def send_data(self) -> None
```

*来源: `scrapy/core/http2/stream.py:271` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-325"></a>

### `Stream.receive_window_update` · method
```python
def receive_window_update(self) -> None
```

**内部调用(库内):**
- [`Stream.send_data`](scrapy_core.md#sym-scrapy_core_http2_stream.py-271)

*来源: `scrapy/core/http2/stream.py:325` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-337"></a>

### `Stream.receive_data` · method
```python
def receive_data(self, data: bytes, flow_controlled_length: int) -> None
```

**内部调用(库内):**
- [`Stream.reset_stream`](scrapy_core.md#sym-scrapy_core_http2_stream.py-385)
- [`get_warnsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-132)

*来源: `scrapy/core/http2/stream.py:337` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-364"></a>

### `Stream.receive_headers` · method
```python
def receive_headers(self, headers: list[tuple[str, str]]) -> None
```

**内部调用(库内):**
- [`Headers.appendlist`](scrapy_http.md#sym-scrapy_http_headers.py-98)
- [`Stream.reset_stream`](scrapy_core.md#sym-scrapy_core_http2_stream.py-385)
- [`get_warnsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-132)

*来源: `scrapy/core/http2/stream.py:364` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-385"></a>

### `Stream.reset_stream` · method
```python
def reset_stream(self, reason: StreamCloseReason = StreamCloseReason.RESET) -> None
```

*来源: `scrapy/core/http2/stream.py:385` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-397"></a>

### `Stream.close` · method
```python
def close(
        self,
        reason: StreamCloseReason,
        errors: Sequence[BaseException] | None = None,
        from_protocol: bool = False,
    ) -> None
```

**内部调用(库内):**
- [`H2ClientProtocol.pop_stream`](scrapy_core.md#sym-scrapy_core_http2_protocol.py-191)
- [`get_maxsize_msg`](scrapy_utils.md#sym-scrapy_utils__download_handlers.py-124)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`DownloadCancelledError`](scrapy.md#sym-scrapy_exceptions.py-74) — `DownloadCancelledError` 异常用于表示下载过程中被取消的情况。
- [`Stream._fire_response_deferred`](scrapy_core.md#sym-scrapy_core_http2_stream.py-493)
- [`InactiveStreamClosed`](scrapy_core.md#sym-scrapy_core_http2_stream.py-34)
- [`InvalidHostname`](scrapy_core.md#sym-scrapy_core_http2_stream.py-46)

*来源: `scrapy/core/http2/stream.py:397` · 待生成*

---
<a id="sym-scrapy_core_http2_stream.py-493"></a>

### `Stream._fire_response_deferred` · method
```python
def _fire_response_deferred(self) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/http2/stream.py:493` · 待生成*

---

## `scrapy/core/scheduler.py`

<a id="sym-scrapy_core_scheduler.py-33"></a>

### `BaseSchedulerMeta` · class
```python
class BaseSchedulerMeta(type)
```

*来源: `scrapy/core/scheduler.py:33` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-38"></a>

### `BaseSchedulerMeta.__instancecheck__` · method
```python
def __instancecheck__(cls, instance: Any) -> bool
```

**内部调用(库内):**
- [`BaseSchedulerMeta.__subclasscheck__`](scrapy_core.md#sym-scrapy_core_scheduler.py-41)

*来源: `scrapy/core/scheduler.py:38` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-41"></a>

### `BaseSchedulerMeta.__subclasscheck__` · method
```python
def __subclasscheck__(cls, subclass: type) -> bool
```

*来源: `scrapy/core/scheduler.py:41` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-52"></a>

### `BaseScheduler` · class
```python
class BaseScheduler(metaclass=BaseSchedulerMeta)
```

*来源: `scrapy/core/scheduler.py:52` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-69"></a>

### `BaseScheduler.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/core/scheduler.py:69` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-75"></a>

### `BaseScheduler.open` · method
```python
def open(self, spider: Spider) -> Deferred[None] | None
```

*来源: `scrapy/core/scheduler.py:75` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-84"></a>

### `BaseScheduler.close` · method
```python
def close(self, reason: str) -> Deferred[None] | None
```

*来源: `scrapy/core/scheduler.py:84` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-94"></a>

### `BaseScheduler.has_pending_requests` · method
装饰器: `@abstractmethod`
```python
def has_pending_requests(self) -> bool
```

*来源: `scrapy/core/scheduler.py:94` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-101"></a>

### `BaseScheduler.enqueue_request` · method
装饰器: `@abstractmethod`
```python
def enqueue_request(self, request: Request) -> bool
```

*来源: `scrapy/core/scheduler.py:101` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-115"></a>

### `BaseScheduler.next_request` · method
装饰器: `@abstractmethod`
```python
def next_request(self) -> Request | None
```

*来源: `scrapy/core/scheduler.py:115` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-127"></a>

### `Scheduler` · class
```python
class Scheduler(BaseScheduler)
```

*来源: `scrapy/core/scheduler.py:127` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-254"></a>

### `Scheduler.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`job_dir`](scrapy_utils.md#sym-scrapy_utils_job.py-10)

*来源: `scrapy/core/scheduler.py:254` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-267"></a>

### `Scheduler.__init__` · method
```python
def __init__(
        self,
        dupefilter: BaseDupeFilter,
        jobdir: str | None = None,
        dqclass: type[BaseQueue] | None = None,
        mqclass: type[BaseQueue] | None = None,
        logunser: bool = False,
        stats: StatsCollector | None = None,
        pqclass: type[ScrapyPriorityQueue] | None = None,
        crawler: Crawler | None = None,
    )
```

**内部调用(库内):**
- [`Scheduler._dqdir`](scrapy_core.md#sym-scrapy_core_scheduler.py-480)
- [`Scheduler._get_start_queue_cls`](scrapy_core.md#sym-scrapy_core_scheduler.py-329)

*来源: `scrapy/core/scheduler.py:267` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-329"></a>

### `Scheduler._get_start_queue_cls` · method
```python
def _get_start_queue_cls(
        self, crawler: Crawler | None, queue: str
    ) -> type[BaseQueue] | None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/core/scheduler.py:329` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-339"></a>

### `Scheduler.has_pending_requests` · method
```python
def has_pending_requests(self) -> bool
```

*来源: `scrapy/core/scheduler.py:339` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-342"></a>

### `Scheduler.open` · method
```python
def open(self, spider: Spider) -> Deferred[None] | None
```

**内部调用(库内):**
- [`Scheduler._mq`](scrapy_core.md#sym-scrapy_core_scheduler.py-446)
- [`Scheduler._dq`](scrapy_core.md#sym-scrapy_core_scheduler.py-458)

*来源: `scrapy/core/scheduler.py:342` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-353"></a>

### `Scheduler.close` · method
```python
def close(self, reason: str) -> Deferred[None] | None
```

**内部调用(库内):**
- [`Scheduler._write_dqs_state`](scrapy_core.md#sym-scrapy_core_scheduler.py-496)

*来源: `scrapy/core/scheduler.py:353` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-364"></a>

### `Scheduler.enqueue_request` · method
```python
def enqueue_request(self, request: Request) -> bool
```

**内部调用(库内):**
- [`Scheduler._dqpush`](scrapy_core.md#sym-scrapy_core_scheduler.py-414)
- [`Scheduler._mqpush`](scrapy_core.md#sym-scrapy_core_scheduler.py-438)

*来源: `scrapy/core/scheduler.py:364` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-387"></a>

### `Scheduler.next_request` · method
```python
def next_request(self) -> Request | None
```

**内部调用(库内):**
- [`Scheduler._dqpop`](scrapy_core.md#sym-scrapy_core_scheduler.py-441)

*来源: `scrapy/core/scheduler.py:387` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-408"></a>

### `Scheduler.__len__` · method
```python
def __len__(self) -> int
```

*来源: `scrapy/core/scheduler.py:408` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-414"></a>

### `Scheduler._dqpush` · method
```python
def _dqpush(self, request: Request) -> bool
```

*来源: `scrapy/core/scheduler.py:414` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-438"></a>

### `Scheduler._mqpush` · method
```python
def _mqpush(self, request: Request) -> None
```

*来源: `scrapy/core/scheduler.py:438` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-441"></a>

### `Scheduler._dqpop` · method
```python
def _dqpop(self) -> Request | None
```

*来源: `scrapy/core/scheduler.py:441` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-446"></a>

### `Scheduler._mq` · method
```python
def _mq(self) -> ScrapyPriorityQueue
```

*来源: `scrapy/core/scheduler.py:446` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-458"></a>

### `Scheduler._dq` · method
```python
def _dq(self) -> ScrapyPriorityQueue
```

**内部调用(库内):**
- [`Scheduler._read_dqs_state`](scrapy_core.md#sym-scrapy_core_scheduler.py-489)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/core/scheduler.py:458` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-480"></a>

### `Scheduler._dqdir` · method
```python
def _dqdir(self, jobdir: str | None) -> str | None
```

*来源: `scrapy/core/scheduler.py:480` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-489"></a>

### `Scheduler._read_dqs_state` · method
```python
def _read_dqs_state(self, dqdir: str) -> Any
```

*来源: `scrapy/core/scheduler.py:489` · 待生成*

---
<a id="sym-scrapy_core_scheduler.py-496"></a>

### `Scheduler._write_dqs_state` · method
```python
def _write_dqs_state(self, dqdir: str, state: Any) -> None
```

*来源: `scrapy/core/scheduler.py:496` · 待生成*

---

## `scrapy/core/scraper.py`

<a id="sym-scrapy_core_scraper.py-58"></a>

### `Slot` · class
```python
class Slot
```

*来源: `scrapy/core/scraper.py:58` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-63"></a>

### `Slot.__init__` · method
```python
def __init__(self, max_active_size: int = 5000000)
```

*来源: `scrapy/core/scraper.py:63` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-71"></a>

### `Slot.add_response_request` · method
```python
def add_response_request(
        self, result: Response | Failure, request: Request
    ) -> Deferred[None]
```

*来源: `scrapy/core/scraper.py:71` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-83"></a>

### `Slot.next_response_request_deferred` · method
```python
def next_response_request_deferred(self) -> QueueTuple
```

*来源: `scrapy/core/scraper.py:83` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-88"></a>

### `Slot.finish_response` · method
```python
def finish_response(self, result: Response | Failure, request: Request) -> None
```

*来源: `scrapy/core/scraper.py:88` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-95"></a>

### `Slot.is_idle` · method
```python
def is_idle(self) -> bool
```

*来源: `scrapy/core/scraper.py:95` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-98"></a>

### `Slot.needs_backout` · method
```python
def needs_backout(self) -> bool
```

*来源: `scrapy/core/scraper.py:98` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-102"></a>

### `Scraper` · class
```python
class Scraper
```

*来源: `scrapy/core/scraper.py:102` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-103"></a>

### `Scraper.__init__` · method
```python
def __init__(self, crawler: Crawler) -> None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`Scraper._check_deprecated_itemproc_method`](scrapy_core.md#sym-scrapy_core_scraper.py-126)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/core/scraper.py:103` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-126"></a>

### `Scraper._check_deprecated_itemproc_method` · method
```python
def _check_deprecated_itemproc_method(self, method: str) -> None
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`method_is_overridden`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-169)

*来源: `scrapy/core/scraper.py:126` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-153"></a>

### `Scraper.open_spider` · method
```python
def open_spider(
        self, spider: Spider | None = None
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`Scraper.open_spider_async`](scrapy_core.md#sym-scrapy_core_scraper.py-163)

*来源: `scrapy/core/scraper.py:153` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-163"></a>

### `Scraper.open_spider_async` · method
```python
async def open_spider_async(self) -> None
```

**内部调用(库内):**
- [`Slot`](scrapy_core.md#sym-scrapy_core_scraper.py-58)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`Scraper.open_spider`](scrapy_core.md#sym-scrapy_core_scraper.py-153)

*来源: `scrapy/core/scraper.py:163` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-180"></a>

### `Scraper.close_spider` · method
```python
def close_spider(self) -> Deferred[None]
```

**内部调用(库内):**
- [`Scraper.close_spider_async`](scrapy_core.md#sym-scrapy_core_scraper.py-188)

*来源: `scrapy/core/scraper.py:180` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-188"></a>

### `Scraper.close_spider_async` · method
```python
async def close_spider_async(self) -> None
```

**内部调用(库内):**
- [`Scraper._check_if_closing`](scrapy_core.md#sym-scrapy_core_scraper.py-210)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`Scraper.close_spider`](scrapy_core.md#sym-scrapy_core_scraper.py-180)

*来源: `scrapy/core/scraper.py:188` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-206"></a>

### `Scraper.is_idle` · method
```python
def is_idle(self) -> bool
```

*来源: `scrapy/core/scraper.py:206` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-210"></a>

### `Scraper._check_if_closing` · method
```python
def _check_if_closing(self) -> None
```

**内部调用(库内):**
- [`Scraper.is_idle`](scrapy_core.md#sym-scrapy_core_scraper.py-206)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/scraper.py:210` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-217"></a>

### `Scraper.enqueue_scrape` · method
装饰器: `@inlineCallbacks`
```python
def enqueue_scrape(
        self, result: Response | Failure, request: Request
    ) -> Generator[Deferred[Any], Any, None]
```

**内部调用(库内):**
- [`Slot.add_response_request`](scrapy_core.md#sym-scrapy_core_scraper.py-71)
- [`Scraper._scrape_next`](scrapy_core.md#sym-scrapy_core_scraper.py-238)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`Slot.finish_response`](scrapy_core.md#sym-scrapy_core_scraper.py-88)
- [`Scraper._check_if_closing`](scrapy_core.md#sym-scrapy_core_scraper.py-210)

*来源: `scrapy/core/scraper.py:217` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-238"></a>

### `Scraper._scrape_next` · method
```python
def _scrape_next(self) -> None
```

**内部调用(库内):**
- [`Slot.next_response_request_deferred`](scrapy_core.md#sym-scrapy_core_scraper.py-83)
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`Scraper._wait_for_processing`](scrapy_core.md#sym-scrapy_core_scraper.py-285)

*来源: `scrapy/core/scraper.py:238` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-244"></a>

### `Scraper._scrape` · method
```python
async def _scrape(self, result: Response | Failure, request: Request) -> None
```

**内部调用(库内):**
- [`SpiderMiddlewareManager.scrape_response_async`](scrapy_core.md#sym-scrapy_core_spidermw.py-209)
- [`Scraper.handle_spider_error`](scrapy_core.md#sym-scrapy_core_scraper.py-348)
- [`Scraper.handle_spider_output_async`](scrapy_core.md#sym-scrapy_core_scraper.py-399)
- [`Scraper.call_spider_async`](scrapy_core.md#sym-scrapy_core_scraper.py-305)
- [`LogFormatter.download_error`](scrapy.md#sym-scrapy_logformatter.py-171) — 记录爬虫在下载过程中发生的错误信息。
- [`logformatter_adapter`](scrapy_utils.md#sym-scrapy_utils_log.py-245)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)

*来源: `scrapy/core/scraper.py:244` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-285"></a>

### `Scraper._wait_for_processing` · method
```python
async def _wait_for_processing(
        self, result: Response | Failure, request: Request, queue_dfd: Deferred[None]
    ) -> None
```

**内部调用(库内):**
- [`Scraper._scrape`](scrapy_core.md#sym-scrapy_core_scraper.py-244)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/scraper.py:285` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-295"></a>

### `Scraper.call_spider` · method
```python
def call_spider(
        self, result: Response | Failure, request: Request, spider: Spider | None = None
    ) -> Deferred[Iterable[Any] | AsyncIterator[Any]]
```

**内部调用(库内):**
- [`Scraper.call_spider_async`](scrapy_core.md#sym-scrapy_core_scraper.py-305)

*来源: `scrapy/core/scraper.py:295` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-305"></a>

### `Scraper.call_spider_async` · method
```python
async def call_spider_async(
        self, result: Response | Failure, request: Request
    ) -> Iterable[Any] | AsyncIterator[Any]
```

**内部调用(库内):**
- [`_defer_sleep_async`](scrapy_utils.md#sym-scrapy_utils_defer.py-89)
- [`warn_on_generator_with_return_value`](scrapy_utils.md#sym-scrapy_utils_misc.py-296)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/core/scraper.py:305` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-348"></a>

### `Scraper.handle_spider_error` · method
```python
def handle_spider_error(
        self,
        _failure: Failure,
        request: Request,
        response: Response | Failure,
    ) -> None
```

**内部调用(库内):**
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`Scraper.close_spider_async`](scrapy_core.md#sym-scrapy_core_scraper.py-188)
- [`LogFormatter.spider_error`](scrapy.md#sym-scrapy_logformatter.py-154) — 记录爬虫错误信息的日志。
- [`logformatter_adapter`](scrapy_utils.md#sym-scrapy_utils_log.py-245)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)

*来源: `scrapy/core/scraper.py:348` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-383"></a>

### `Scraper.handle_spider_output` · method
```python
def handle_spider_output(
        self,
        result: Iterable[_T] | AsyncIterator[_T],
        request: Request,
        response: Response | Failure,
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`Scraper.handle_spider_output_async`](scrapy_core.md#sym-scrapy_core_scraper.py-399)

*来源: `scrapy/core/scraper.py:383` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-399"></a>

### `Scraper.handle_spider_output_async` · method
```python
async def handle_spider_output_async(
        self,
        result: Iterable[_T] | AsyncIterator[_T],
        request: Request,
        response: Response | Failure,
    ) -> None
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`aiter_errback`](scrapy_utils.md#sym-scrapy_utils_defer.py-364)
- [`iter_errback`](scrapy_utils.md#sym-scrapy_utils_defer.py-345)
- [`_parallel_asyncio`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-95)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`parallel_async`](scrapy_utils.md#sym-scrapy_utils_defer.py-280)
- [`parallel`](scrapy_utils.md#sym-scrapy_utils_defer.py-159)

*来源: `scrapy/core/scraper.py:399` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-440"></a>

### `Scraper._process_spidermw_output` · method
```python
def _process_spidermw_output(
        self, output: Any, response: Response | Failure
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`Scraper._process_spidermw_output_async`](scrapy_core.md#sym-scrapy_core_scraper.py-450)

*来源: `scrapy/core/scraper.py:440` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-450"></a>

### `Scraper._process_spidermw_output_async` · method
```python
async def _process_spidermw_output_async(
        self, output: Any, response: Response | Failure
    ) -> None
```

**内部调用(库内):**
- [`Scraper.start_itemproc_async`](scrapy_core.md#sym-scrapy_core_scraper.py-480)

*来源: `scrapy/core/scraper.py:450` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-465"></a>

### `Scraper.start_itemproc` · method
```python
def start_itemproc(
        self, item: Any, *, response: Response | Failure | None
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`Scraper.start_itemproc_async`](scrapy_core.md#sym-scrapy_core_scraper.py-480)

*来源: `scrapy/core/scraper.py:465` · 待生成*

---
<a id="sym-scrapy_core_scraper.py-480"></a>

### `Scraper.start_itemproc_async` · method
```python
async def start_itemproc_async(
        self, item: Any, *, response: Response | Failure | None
    ) -> None
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`logformatter_adapter`](scrapy_utils.md#sym-scrapy_utils_log.py-245)

*来源: `scrapy/core/scraper.py:480` · 待生成*

---

## `scrapy/core/spidermw.py`

<a id="sym-scrapy_core_spidermw.py-48"></a>

### `SpiderMiddlewareManager` · class
```python
class SpiderMiddlewareManager(MiddlewareManager)
```

*来源: `scrapy/core/spidermw.py:48` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-52"></a>

### `SpiderMiddlewareManager._get_mwlist_from_settings` · method
装饰器: `@classmethod`
```python
def _get_mwlist_from_settings(cls, settings: BaseSettings) -> list[Any]
```

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`BaseSettings.get_component_priority_dict_with_base`](scrapy_settings.md#sym-scrapy_settings___init__.py-338)

*来源: `scrapy/core/spidermw.py:52` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-57"></a>

### `SpiderMiddlewareManager._add_middleware` · method
```python
def _add_middleware(self, mw: Any) -> None
```

**内部调用(库内):**
- [`MiddlewareManager._check_mw_method_spider_arg`](scrapy.md#sym-scrapy_middleware.py-119)
- [`SpiderMiddlewareManager._get_process_spider_output`](scrapy_core.md#sym-scrapy_core_spidermw.py-251)

*来源: `scrapy/core/spidermw.py:57` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-75"></a>

### `SpiderMiddlewareManager._process_spider_input` · method
```python
async def _process_spider_input(
        self,
        scrape_func: ScrapeFunc[_T],
        response: Response,
        request: Request,
    ) -> Iterable[_T] | AsyncIterator[_T]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`_InvalidOutput`](scrapy.md#sym-scrapy_exceptions.py-22) — 这个类 `_InvalidOutput` 是一个类型错误的子类，用于表示爬虫输出数据无效的情况。

*来源: `scrapy/core/spidermw.py:75` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-100"></a>

### `SpiderMiddlewareManager._evaluate_iterable` · method
```python
async def _evaluate_iterable(
        self,
        response: Response,
        iterable: AsyncIterator[_T],
        exception_processor_index: int,
        recover_to: MutableAsyncChain[_T],
    ) -> AsyncIterator[_T]
```

**内部调用(库内):**
- [`SpiderMiddlewareManager._process_spider_exception`](scrapy_core.md#sym-scrapy_core_spidermw.py-116)

*来源: `scrapy/core/spidermw.py:100` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-116"></a>

### `SpiderMiddlewareManager._process_spider_exception` · method
```python
def _process_spider_exception(
        self,
        response: Response,
        exception: Exception,
        start_index: int = 0,
    ) -> MutableAsyncChain[_T]
```

**内部调用(库内):**
- [`as_async_generator`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-13)
- [`SpiderMiddlewareManager._process_spider_output`](scrapy_core.md#sym-scrapy_core_spidermw.py-152)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`_InvalidOutput`](scrapy.md#sym-scrapy_exceptions.py-22) — 这个类 `_InvalidOutput` 是一个类型错误的子类，用于表示爬虫输出数据无效的情况。

*来源: `scrapy/core/spidermw.py:116` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-152"></a>

### `SpiderMiddlewareManager._process_spider_output` · method
```python
def _process_spider_output(
        self,
        response: Response,
        result: AsyncIterator[_T],
        start_index: int = 0,
    ) -> MutableAsyncChain[_T]
```

**内部调用(库内):**
- [`MutableAsyncChain`](scrapy_utils.md#sym-scrapy_utils_python.py-326)
- [`SpiderMiddlewareManager._evaluate_iterable`](scrapy_core.md#sym-scrapy_core_spidermw.py-100)

*来源: `scrapy/core/spidermw.py:152` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-174"></a>

### `SpiderMiddlewareManager._process_callback_output` · method
```python
async def _process_callback_output(
        self, response: Response, result: AsyncIterator[_T]
    ) -> MutableAsyncChain[_T]
```

**内部调用(库内):**
- [`MutableAsyncChain`](scrapy_utils.md#sym-scrapy_utils_python.py-326)
- [`SpiderMiddlewareManager._evaluate_iterable`](scrapy_core.md#sym-scrapy_core_spidermw.py-100)
- [`SpiderMiddlewareManager._process_spider_output`](scrapy_core.md#sym-scrapy_core_spidermw.py-152)

*来源: `scrapy/core/spidermw.py:174` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-182"></a>

### `SpiderMiddlewareManager.scrape_response` · method
```python
def scrape_response(
        self,
        scrape_func: Callable[
            [Response | Failure, Request],
            Deferred[Iterable[_T] | AsyncIterator[_T]],
        ],
        response: Response,
        request: Request,
        spider: Spider,
    ) -> Deferred[MutableAsyncChain[_T]]
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`MiddlewareManager._set_compat_spider`](scrapy.md#sym-scrapy_middleware.py-70)
- [`SpiderMiddlewareManager.scrape_response_async`](scrapy_core.md#sym-scrapy_core_spidermw.py-209)

*来源: `scrapy/core/spidermw.py:182` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-199"></a>

### `SpiderMiddlewareManager.scrape_func_wrapped` · method
装饰器: `@wraps(scrape_func)`
```python
async def scrape_func_wrapped(
            response: Response | Failure, request: Request
        ) -> Iterable[_T] | AsyncIterator[_T]
```

**内部调用(库内):**
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/core/spidermw.py:199` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-209"></a>

### `SpiderMiddlewareManager.scrape_response_async` · method
```python
async def scrape_response_async(
        self,
        scrape_func: ScrapeFunc[_T],
        response: Response,
        request: Request,
    ) -> MutableAsyncChain[_T]
```

**内部调用(库内):**
- [`SpiderMiddlewareManager._process_spider_input`](scrapy_core.md#sym-scrapy_core_spidermw.py-75)
- [`as_async_generator`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-13)
- [`SpiderMiddlewareManager._process_callback_output`](scrapy_core.md#sym-scrapy_core_spidermw.py-174)
- [`_defer_sleep_async`](scrapy_utils.md#sym-scrapy_utils_defer.py-89)
- [`SpiderMiddlewareManager._process_spider_exception`](scrapy_core.md#sym-scrapy_core_spidermw.py-116)

*来源: `scrapy/core/spidermw.py:209` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-230"></a>

### `SpiderMiddlewareManager.process_start` · method
```python
async def process_start(
        self, spider: Spider | None = None
    ) -> AsyncIterator[Any] | None
```

**内部调用(库内):**
- [`MiddlewareManager._set_compat_spider`](scrapy.md#sym-scrapy_middleware.py-70)
- [`MiddlewareManager._process_chain`](scrapy.md#sym-scrapy_middleware.py-131)

*来源: `scrapy/core/spidermw.py:230` · 待生成*

---
<a id="sym-scrapy_core_spidermw.py-251"></a>

### `SpiderMiddlewareManager._get_process_spider_output` · method
装饰器: `@staticmethod`
```python
def _get_process_spider_output(mw: Any) -> Callable[..., Any] | None
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/core/spidermw.py:251` · 待生成*

---