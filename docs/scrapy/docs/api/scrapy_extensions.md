# API 参考:`scrapy/extensions`

## `scrapy/extensions/closespider.py`

<a id="sym-scrapy_extensions_closespider.py-37"></a>

### `CloseSpider` · class
```python
class CloseSpider
```

*来源: `scrapy/extensions/closespider.py:37` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-38"></a>

### `CloseSpider.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/extensions/closespider.py:38` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-84"></a>

### `CloseSpider.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/closespider.py:84` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-87"></a>

### `CloseSpider.error_count` · method
```python
def error_count(self, failure: Failure, response: Response, spider: Spider) -> None
```

**内部调用(库内):**
- [`CloseSpider._close_spider`](scrapy_extensions.md#sym-scrapy_extensions_closespider.py-148)

*来源: `scrapy/extensions/closespider.py:87` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-92"></a>

### `CloseSpider.page_count` · method
```python
def page_count(self, response: Response, request: Request, spider: Spider) -> None
```

**内部调用(库内):**
- [`CloseSpider._close_spider`](scrapy_extensions.md#sym-scrapy_extensions_closespider.py-148)

*来源: `scrapy/extensions/closespider.py:92` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-104"></a>

### `CloseSpider.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`call_later`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-234)

*来源: `scrapy/extensions/closespider.py:104` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-110"></a>

### `CloseSpider.item_scraped` · method
```python
def item_scraped(self, item: Any, spider: Spider) -> None
```

**内部调用(库内):**
- [`CloseSpider._close_spider`](scrapy_extensions.md#sym-scrapy_extensions_closespider.py-148)

*来源: `scrapy/extensions/closespider.py:110` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-116"></a>

### `CloseSpider.spider_closed` · method
```python
def spider_closed(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/closespider.py:116` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-126"></a>

### `CloseSpider.spider_opened_no_item` · method
```python
def spider_opened_no_item(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`create_looping_call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-217)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/closespider.py:126` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-135"></a>

### `CloseSpider.item_scraped_no_item` · method
```python
def item_scraped_no_item(self, item: Any, spider: Spider) -> None
```

*来源: `scrapy/extensions/closespider.py:135` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-138"></a>

### `CloseSpider._count_items_produced` · method
```python
def _count_items_produced(self) -> None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)
- [`CloseSpider._close_spider`](scrapy_extensions.md#sym-scrapy_extensions_closespider.py-148)

*来源: `scrapy/extensions/closespider.py:138` · 待生成*

---
<a id="sym-scrapy_extensions_closespider.py-148"></a>

### `CloseSpider._close_spider` · method
```python
def _close_spider(self, reason: str) -> None
```

**内部调用(库内):**
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)

*来源: `scrapy/extensions/closespider.py:148` · 待生成*

---

## `scrapy/extensions/corestats.py`

<a id="sym-scrapy_extensions_corestats.py-21"></a>

### `CoreStats` · class
```python
class CoreStats
```

*来源: `scrapy/extensions/corestats.py:21` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-22"></a>

### `CoreStats.__init__` · method
```python
def __init__(self, stats: StatsCollector)
```

*来源: `scrapy/extensions/corestats.py:22` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-28"></a>

### `CoreStats.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/corestats.py:28` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-38"></a>

### `CoreStats.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/corestats.py:38` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-43"></a>

### `CoreStats.spider_closed` · method
```python
def spider_closed(self, spider: Spider, reason: str) -> None
```

*来源: `scrapy/extensions/corestats.py:43` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-52"></a>

### `CoreStats.item_scraped` · method
```python
def item_scraped(self, item: Any, spider: Spider) -> None
```

*来源: `scrapy/extensions/corestats.py:52` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-55"></a>

### `CoreStats.response_received` · method
```python
def response_received(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/corestats.py:55` · 待生成*

---
<a id="sym-scrapy_extensions_corestats.py-58"></a>

### `CoreStats.item_dropped` · method
```python
def item_dropped(self, item: Any, spider: Spider, exception: BaseException) -> None
```

*来源: `scrapy/extensions/corestats.py:58` · 待生成*

---

## `scrapy/extensions/debug.py`

<a id="sym-scrapy_extensions_debug.py-33"></a>

### `StackTraceDump` · class
```python
class StackTraceDump
```

*来源: `scrapy/extensions/debug.py:33` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-34"></a>

### `StackTraceDump.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/extensions/debug.py:34` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-44"></a>

### `StackTraceDump.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/debug.py:44` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-47"></a>

### `StackTraceDump.dump_stacktrace` · method
```python
def dump_stacktrace(self, signum: int, frame: FrameType | None) -> None
```

**内部调用(库内):**
- [`StackTraceDump._thread_stacks`](scrapy_extensions.md#sym-scrapy_extensions_debug.py-61)
- [`format_engine_status`](scrapy_utils.md#sym-scrapy_utils_engine.py-42)
- [`format_live_refs`](scrapy_utils.md#sym-scrapy_utils_trackref.py-50)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/debug.py:47` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-61"></a>

### `StackTraceDump._thread_stacks` · method
```python
def _thread_stacks(self) -> str
```

*来源: `scrapy/extensions/debug.py:61` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-71"></a>

### `Debugger` · class
```python
class Debugger
```

*来源: `scrapy/extensions/debug.py:71` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-72"></a>

### `Debugger.__init__` · method
```python
def __init__(self) -> None
```

*来源: `scrapy/extensions/debug.py:72` · 待生成*

---
<a id="sym-scrapy_extensions_debug.py-77"></a>

### `Debugger._enter_debugger` · method
```python
def _enter_debugger(self, signum: int, frame: FrameType | None) -> None
```

*来源: `scrapy/extensions/debug.py:77` · 待生成*

---

## `scrapy/extensions/feedexport.py`

<a id="sym-scrapy_extensions_feedexport.py-55"></a>

### `ItemFilter` · class
```python
class ItemFilter
```

*来源: `scrapy/extensions/feedexport.py:55` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-67"></a>

### `ItemFilter.__init__` · method
```python
def __init__(self, feed_options: dict[str, Any] | None) -> None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/extensions/feedexport.py:67` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-77"></a>

### `ItemFilter.accepts` · method
```python
def accepts(self, item: Any) -> bool
```

*来源: `scrapy/extensions/feedexport.py:77` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-91"></a>

### `IFeedStorage` · class
```python
class IFeedStorage(Interface)
```

*来源: `scrapy/extensions/feedexport.py:91` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-96"></a>

### `IFeedStorage.__init__` · method
```python
def __init__(uri, *, feed_options=None)
```

*来源: `scrapy/extensions/feedexport.py:96` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-100"></a>

### `IFeedStorage.open` · method
```python
def open(spider)
```

*来源: `scrapy/extensions/feedexport.py:100` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-104"></a>

### `IFeedStorage.store` · method
```python
def store(file)
```

*来源: `scrapy/extensions/feedexport.py:104` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-108"></a>

### `FeedStorageProtocol` · class
```python
class FeedStorageProtocol(Protocol)
```

*来源: `scrapy/extensions/feedexport.py:108` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-111"></a>

### `FeedStorageProtocol.__init__` · method
```python
def __init__(self, uri: str, *, feed_options: dict[str, Any] | None = None)
```

*来源: `scrapy/extensions/feedexport.py:111` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-115"></a>

### `FeedStorageProtocol.open` · method
```python
def open(self, spider: Spider) -> IO[bytes]
```

*来源: `scrapy/extensions/feedexport.py:115` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-119"></a>

### `FeedStorageProtocol.store` · method
```python
def store(self, file: IO[bytes]) -> Deferred[None] | None
```

*来源: `scrapy/extensions/feedexport.py:119` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-124"></a>

### `BlockingFeedStorage` · class
装饰器: `@implementer(IFeedStorage)`
```python
class BlockingFeedStorage(ABC)
```

*来源: `scrapy/extensions/feedexport.py:124` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-125"></a>

### `BlockingFeedStorage.open` · method
```python
def open(self, spider: Spider) -> IO[bytes]
```

*来源: `scrapy/extensions/feedexport.py:125` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-132"></a>

### `BlockingFeedStorage.store` · method
```python
def store(self, file: IO[bytes]) -> Deferred[None] | None
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/extensions/feedexport.py:132` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-136"></a>

### `BlockingFeedStorage._store_in_thread` · method
装饰器: `@abstractmethod`
```python
def _store_in_thread(self, file: IO[bytes]) -> None
```

*来源: `scrapy/extensions/feedexport.py:136` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-141"></a>

### `StdoutFeedStorage` · class
装饰器: `@implementer(IFeedStorage)`
```python
class StdoutFeedStorage
```

*来源: `scrapy/extensions/feedexport.py:141` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-142"></a>

### `StdoutFeedStorage.__init__` · method
```python
def __init__(
        self,
        uri: str,
        _stdout: IO[bytes] | None = None,
        *,
        feed_options: dict[str, Any] | None = None,
    )
```

*来源: `scrapy/extensions/feedexport.py:142` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-160"></a>

### `StdoutFeedStorage.open` · method
```python
def open(self, spider: Spider) -> IO[bytes]
```

*来源: `scrapy/extensions/feedexport.py:160` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-163"></a>

### `StdoutFeedStorage.store` · method
```python
def store(self, file: IO[bytes]) -> Deferred[None] | None
```

*来源: `scrapy/extensions/feedexport.py:163` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-168"></a>

### `FileFeedStorage` · class
装饰器: `@implementer(IFeedStorage)`
```python
class FileFeedStorage
```

*来源: `scrapy/extensions/feedexport.py:168` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-169"></a>

### `FileFeedStorage.__init__` · method
```python
def __init__(self, uri: str, *, feed_options: dict[str, Any] | None = None)
```

*来源: `scrapy/extensions/feedexport.py:169` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-176"></a>

### `FileFeedStorage.open` · method
```python
def open(self, spider: Spider) -> IO[bytes]
```

*来源: `scrapy/extensions/feedexport.py:176` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-182"></a>

### `FileFeedStorage.store` · method
```python
def store(self, file: IO[bytes]) -> Deferred[None] | None
```

*来源: `scrapy/extensions/feedexport.py:182` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-187"></a>

### `S3FeedStorage` · class
```python
class S3FeedStorage(BlockingFeedStorage)
```

*来源: `scrapy/extensions/feedexport.py:187` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-188"></a>

### `S3FeedStorage.__init__` · method
```python
def __init__(
        self,
        uri: str,
        access_key: str | None = None,
        secret_key: str | None = None,
        acl: str | None = None,
        endpoint_url: str | None = None,
        *,
        feed_options: dict[str, Any] | None = None,
        session_token: str | None = None,
        region_name: str | None = None,
    )
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。

*来源: `scrapy/extensions/feedexport.py:188` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-233"></a>

### `S3FeedStorage.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls,
        crawler: Crawler,
        uri: str,
        *,
        feed_options: dict[str, Any] | None = None,
    ) -> Self
```

*来源: `scrapy/extensions/feedexport.py:233` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-251"></a>

### `S3FeedStorage._store_in_thread` · method
```python
def _store_in_thread(self, file: IO[bytes]) -> None
```

*来源: `scrapy/extensions/feedexport.py:251` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-269"></a>

### `GCSFeedStorage` · class
```python
class GCSFeedStorage(BlockingFeedStorage)
```

*来源: `scrapy/extensions/feedexport.py:269` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-270"></a>

### `GCSFeedStorage.__init__` · method
```python
def __init__(
        self,
        uri: str,
        project_id: str | None,
        acl: str | None,
        *,
        feed_options: dict[str, Any] | None = None,
    )
```

*来源: `scrapy/extensions/feedexport.py:270` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-293"></a>

### `GCSFeedStorage.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls,
        crawler: Crawler,
        uri: str,
        *,
        feed_options: dict[str, Any] | None = None,
    ) -> Self
```

*来源: `scrapy/extensions/feedexport.py:293` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-307"></a>

### `GCSFeedStorage._store_in_thread` · method
```python
def _store_in_thread(self, file: IO[bytes]) -> None
```

*来源: `scrapy/extensions/feedexport.py:307` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-320"></a>

### `FTPFeedStorage` · class
```python
class FTPFeedStorage(BlockingFeedStorage)
```

*来源: `scrapy/extensions/feedexport.py:320` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-321"></a>

### `FTPFeedStorage.__init__` · method
```python
def __init__(
        self,
        uri: str,
        use_active_mode: bool = False,
        *,
        feed_options: dict[str, Any] | None = None,
    )
```

*来源: `scrapy/extensions/feedexport.py:321` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-340"></a>

### `FTPFeedStorage.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(
        cls,
        crawler: Crawler,
        uri: str,
        *,
        feed_options: dict[str, Any] | None = None,
    ) -> Self
```

*来源: `scrapy/extensions/feedexport.py:340` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-353"></a>

### `FTPFeedStorage._store_in_thread` · method
```python
def _store_in_thread(self, file: IO[bytes]) -> None
```

**内部调用(库内):**
- [`ftp_store_file`](scrapy_utils.md#sym-scrapy_utils_ftp.py-21)

*来源: `scrapy/extensions/feedexport.py:353` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-366"></a>

### `FeedSlot` · class
```python
class FeedSlot
```

*来源: `scrapy/extensions/feedexport.py:366` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-367"></a>

### `FeedSlot.__init__` · method
```python
def __init__(
        self,
        storage: FeedStorageProtocol,
        uri: str,
        format: str,  # noqa: A002
        store_empty: bool,
        batch_id: int,
        uri_template: str,
        filter: ItemFilter,  # noqa: A002
        feed_options: dict[str, Any],
        spider: Spider,
        exporters: dict[str, type[BaseItemExporter]],
        settings: BaseSettings,
        crawler: Crawler,
    )
```

*来源: `scrapy/extensions/feedexport.py:367` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-403"></a>

### `FeedSlot.start_exporting` · method
```python
def start_exporting(self) -> None
```

**内部调用(库内):**
- [`PostProcessingManager`](scrapy_extensions.md#sym-scrapy_extensions_postprocessing.py-118)
- [`FeedSlot._get_exporter`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-430)

*来源: `scrapy/extensions/feedexport.py:403` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-430"></a>

### `FeedSlot._get_exporter` · method
```python
def _get_exporter(
        self, file: IO[bytes], format_: str, *args: Any, **kwargs: Any
    ) -> BaseItemExporter
```

*来源: `scrapy/extensions/feedexport.py:430` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-437"></a>

### `FeedSlot.finish_exporting` · method
```python
def finish_exporting(self) -> None
```

*来源: `scrapy/extensions/feedexport.py:437` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-444"></a>

### `FeedExporter` · class
```python
class FeedExporter
```

*来源: `scrapy/extensions/feedexport.py:444` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-446"></a>

### `FeedExporter.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/feedexport.py:446` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-453"></a>

### `FeedExporter.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`feed_complete_default_values_from_settings`](scrapy_utils.md#sym-scrapy_utils_conf.py-127)
- [`FeedExporter._load_filter`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-726)
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)
- [`FeedExporter._load_components`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-650)
- [`FeedExporter._storage_supported`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-684)
- [`FeedExporter._settings_are_valid`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-666)
- [`FeedExporter._exporter_supported`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-660)

*来源: `scrapy/extensions/feedexport.py:453` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-509"></a>

### `FeedExporter.open_spider` · method
```python
def open_spider(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`FeedExporter._get_uri_params`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-707)
- [`FeedExporter._start_new_batch`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-582)

*来源: `scrapy/extensions/feedexport.py:509` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-522"></a>

### `FeedExporter.close_spider` · method
```python
async def close_spider(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`FeedExporter._close_slot`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-548)
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`CallLaterOnce.wait`](scrapy_utils.md#sym-scrapy_utils_reactor.py-86)

*来源: `scrapy/extensions/feedexport.py:522` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-541"></a>

### `FeedExporter._get_file` · method
装饰器: `@staticmethod`
```python
def _get_file(slot_: FeedSlot) -> IO[bytes]
```

*来源: `scrapy/extensions/feedexport.py:541` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-548"></a>

### `FeedExporter._close_slot` · method
```python
async def _close_slot(self, slot: FeedSlot, spider: Spider) -> None
```

**内部调用(库内):**
- [`FeedSlot.finish_exporting`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-437)
- [`FeedSlot.start_exporting`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-403)
- [`IFeedStorage.store`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-104)
- [`FeedExporter._get_file`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-541)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/feedexport.py:548` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-582"></a>

### `FeedExporter._start_new_batch` · method
```python
def _start_new_batch(
        self,
        batch_id: int,
        uri: str,
        feed_options: dict[str, Any],
        spider: Spider,
        uri_template: str,
    ) -> FeedSlot
```

**内部调用(库内):**
- [`FeedExporter._get_storage`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-699)
- [`FeedSlot`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-366)

*来源: `scrapy/extensions/feedexport.py:582` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-615"></a>

### `FeedExporter.item_scraped` · method
```python
def item_scraped(self, item: Any, spider: Spider) -> None
```

**内部调用(库内):**
- [`ItemFilter.accepts`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-77)
- [`FeedSlot.start_exporting`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-403)
- [`FeedExporter._get_uri_params`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-707)
- [`FeedExporter._close_slot`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-548)
- [`FeedExporter._start_new_batch`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-582)

*来源: `scrapy/extensions/feedexport.py:615` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-650"></a>

### `FeedExporter._load_components` · method
```python
def _load_components(self, setting_prefix: str) -> dict[str, Any]
```

**内部调用(库内):**
- [`BaseSettings.getwithbase`](scrapy_settings.md#sym-scrapy_settings___init__.py-319)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/extensions/feedexport.py:650` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-660"></a>

### `FeedExporter._exporter_supported` · method
```python
def _exporter_supported(self, format_: str) -> bool
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/extensions/feedexport.py:660` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-666"></a>

### `FeedExporter._settings_are_valid` · method
```python
def _settings_are_valid(self) -> bool
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/extensions/feedexport.py:666` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-684"></a>

### `FeedExporter._storage_supported` · method
```python
def _storage_supported(self, uri: str, feed_options: dict[str, Any]) -> bool
```

**内部调用(库内):**
- [`FeedExporter._get_storage`](scrapy_extensions.md#sym-scrapy_extensions_feedexport.py-699)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/extensions/feedexport.py:684` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-699"></a>

### `FeedExporter._get_storage` · method
```python
def _get_storage(
        self, uri: str, feed_options: dict[str, Any]
    ) -> FeedStorageProtocol
```

*来源: `scrapy/extensions/feedexport.py:699` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-707"></a>

### `FeedExporter._get_uri_params` · method
```python
def _get_uri_params(
        self,
        spider: Spider,
        uri_params_function: str | UriParamsCallableT | None,
        slot: FeedSlot | None = None,
    ) -> dict[str, Any]
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/extensions/feedexport.py:707` · 待生成*

---
<a id="sym-scrapy_extensions_feedexport.py-726"></a>

### `FeedExporter._load_filter` · method
```python
def _load_filter(self, feed_options: dict[str, Any]) -> ItemFilter
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/extensions/feedexport.py:726` · 待生成*

---

## `scrapy/extensions/httpcache.py`

<a id="sym-scrapy_extensions_httpcache.py-35"></a>

### `DummyPolicy` · class
```python
class DummyPolicy
```

*来源: `scrapy/extensions/httpcache.py:35` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-36"></a>

### `DummyPolicy.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

*来源: `scrapy/extensions/httpcache.py:36` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-42"></a>

### `DummyPolicy.should_cache_request` · method
```python
def should_cache_request(self, request: Request) -> bool
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/extensions/httpcache.py:42` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-45"></a>

### `DummyPolicy.should_cache_response` · method
```python
def should_cache_response(self, response: Response, request: Request) -> bool
```

*来源: `scrapy/extensions/httpcache.py:45` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-48"></a>

### `DummyPolicy.is_cached_response_fresh` · method
```python
def is_cached_response_fresh(
        self, cachedresponse: Response, request: Request
    ) -> bool
```

*来源: `scrapy/extensions/httpcache.py:48` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-53"></a>

### `DummyPolicy.is_cached_response_valid` · method
```python
def is_cached_response_valid(
        self, cachedresponse: Response, response: Response, request: Request
    ) -> bool
```

*来源: `scrapy/extensions/httpcache.py:53` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-59"></a>

### `RFC2616Policy` · class
```python
class RFC2616Policy
```

*来源: `scrapy/extensions/httpcache.py:59` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-62"></a>

### `RFC2616Policy.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/extensions/httpcache.py:62` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-73"></a>

### `RFC2616Policy._parse_cachecontrol` · method
```python
def _parse_cachecontrol(self, r: Request | Response) -> dict[bytes, bytes | None]
```

**内部调用(库内):**
- [`parse_cachecontrol`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-394)

*来源: `scrapy/extensions/httpcache.py:73` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-84"></a>

### `RFC2616Policy.should_cache_request` · method
```python
def should_cache_request(self, request: Request) -> bool
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`RFC2616Policy._parse_cachecontrol`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-73)

*来源: `scrapy/extensions/httpcache.py:84` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-91"></a>

### `RFC2616Policy.should_cache_response` · method
```python
def should_cache_response(self, response: Response, request: Request) -> bool
```

**内部调用(库内):**
- [`RFC2616Policy._parse_cachecontrol`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-73)

*来源: `scrapy/extensions/httpcache.py:91` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-119"></a>

### `RFC2616Policy.is_cached_response_fresh` · method
```python
def is_cached_response_fresh(
        self, cachedresponse: Response, request: Request
    ) -> bool
```

**内部调用(库内):**
- [`RFC2616Policy._parse_cachecontrol`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-73)
- [`RFC2616Policy._compute_freshness_lifetime`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-192)
- [`RFC2616Policy._compute_current_age`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-225)
- [`RFC2616Policy._get_max_age`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-186)
- [`RFC2616Policy._set_conditional_validators`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-175)

*来源: `scrapy/extensions/httpcache.py:119` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-162"></a>

### `RFC2616Policy.is_cached_response_valid` · method
```python
def is_cached_response_valid(
        self, cachedresponse: Response, response: Response, request: Request
    ) -> bool
```

**内部调用(库内):**
- [`RFC2616Policy._parse_cachecontrol`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-73)

*来源: `scrapy/extensions/httpcache.py:162` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-175"></a>

### `RFC2616Policy._set_conditional_validators` · method
```python
def _set_conditional_validators(
        self, request: Request, cachedresponse: Response
    ) -> None
```

*来源: `scrapy/extensions/httpcache.py:175` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-186"></a>

### `RFC2616Policy._get_max_age` · method
```python
def _get_max_age(self, cc: dict[bytes, bytes | None]) -> int | None
```

*来源: `scrapy/extensions/httpcache.py:186` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-192"></a>

### `RFC2616Policy._compute_freshness_lifetime` · method
```python
def _compute_freshness_lifetime(
        self, response: Response, request: Request, now: float
    ) -> float
```

**内部调用(库内):**
- [`RFC2616Policy._parse_cachecontrol`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-73)
- [`RFC2616Policy._get_max_age`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-186)
- [`rfc1123_to_epoch`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-414)

*来源: `scrapy/extensions/httpcache.py:192` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-225"></a>

### `RFC2616Policy._compute_current_age` · method
```python
def _compute_current_age(
        self, response: Response, request: Request, now: float
    ) -> float
```

**内部调用(库内):**
- [`rfc1123_to_epoch`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-414)

*来源: `scrapy/extensions/httpcache.py:225` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-247"></a>

### `DbmCacheStorage` · class
```python
class DbmCacheStorage
```

*来源: `scrapy/extensions/httpcache.py:247` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-248"></a>

### `DbmCacheStorage.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`data_path`](scrapy_utils.md#sym-scrapy_utils_project.py-50)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/extensions/httpcache.py:248` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-254"></a>

### `DbmCacheStorage.open_spider` · method
```python
def open_spider(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/httpcache.py:254` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-269"></a>

### `DbmCacheStorage.close_spider` · method
```python
def close_spider(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/httpcache.py:269` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-272"></a>

### `DbmCacheStorage.retrieve_response` · method
```python
def retrieve_response(self, spider: Spider, request: Request) -> Response | None
```

**内部调用(库内):**
- [`DbmCacheStorage._read_data`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-296)
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)
- [`ResponseTypes.from_args`](scrapy.md#sym-scrapy_responsetypes.py-124)

*来源: `scrapy/extensions/httpcache.py:272` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-283"></a>

### `DbmCacheStorage.store_response` · method
```python
def store_response(
        self, spider: Spider, request: Request, response: Response
    ) -> None
```

*来源: `scrapy/extensions/httpcache.py:283` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-296"></a>

### `DbmCacheStorage._read_data` · method
```python
def _read_data(self, spider: Spider, request: Request) -> dict[str, Any] | None
```

*来源: `scrapy/extensions/httpcache.py:296` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-310"></a>

### `FilesystemCacheStorage` · class
```python
class FilesystemCacheStorage
```

*来源: `scrapy/extensions/httpcache.py:310` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-311"></a>

### `FilesystemCacheStorage.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`data_path`](scrapy_utils.md#sym-scrapy_utils_project.py-50)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/extensions/httpcache.py:311` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-322"></a>

### `FilesystemCacheStorage.open_spider` · method
```python
def open_spider(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/httpcache.py:322` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-332"></a>

### `FilesystemCacheStorage.close_spider` · method
```python
def close_spider(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/httpcache.py:332` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-335"></a>

### `FilesystemCacheStorage.retrieve_response` · method
```python
def retrieve_response(self, spider: Spider, request: Request) -> Response | None
```

**内部调用(库内):**
- [`FilesystemCacheStorage._read_meta`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-382)
- [`FilesystemCacheStorage._get_request_path`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-378)
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)
- [`ResponseTypes.from_args`](scrapy.md#sym-scrapy_responsetypes.py-124)

*来源: `scrapy/extensions/httpcache.py:335` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-351"></a>

### `FilesystemCacheStorage.store_response` · method
```python
def store_response(
        self, spider: Spider, request: Request, response: Response
    ) -> None
```

**内部调用(库内):**
- [`FilesystemCacheStorage._get_request_path`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-378)
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/extensions/httpcache.py:351` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-378"></a>

### `FilesystemCacheStorage._get_request_path` · method
```python
def _get_request_path(self, spider: Spider, request: Request) -> str
```

*来源: `scrapy/extensions/httpcache.py:378` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-382"></a>

### `FilesystemCacheStorage._read_meta` · method
```python
def _read_meta(self, spider: Spider, request: Request) -> dict[str, Any] | None
```

**内部调用(库内):**
- [`FilesystemCacheStorage._get_request_path`](scrapy_extensions.md#sym-scrapy_extensions_httpcache.py-378)

*来源: `scrapy/extensions/httpcache.py:382` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-394"></a>

### `parse_cachecontrol` · func
```python
def parse_cachecontrol(header: bytes) -> dict[bytes, bytes | None]
```

*来源: `scrapy/extensions/httpcache.py:394` · 待生成*

---
<a id="sym-scrapy_extensions_httpcache.py-414"></a>

### `rfc1123_to_epoch` · func
```python
def rfc1123_to_epoch(date_str: str | bytes | None) -> int | None
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/extensions/httpcache.py:414` · 待生成*

---

## `scrapy/extensions/logcount.py`

<a id="sym-scrapy_extensions_logcount.py-19"></a>

### `LogCount` · class
```python
class LogCount
```

*来源: `scrapy/extensions/logcount.py:19` · 待生成*

---
<a id="sym-scrapy_extensions_logcount.py-28"></a>

### `LogCount.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/extensions/logcount.py:28` · 待生成*

---
<a id="sym-scrapy_extensions_logcount.py-33"></a>

### `LogCount.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/logcount.py:33` · 待生成*

---
<a id="sym-scrapy_extensions_logcount.py-39"></a>

### `LogCount.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`LogCounterHandler`](scrapy_utils.md#sym-scrapy_utils_log.py-232)

*来源: `scrapy/extensions/logcount.py:39` · 待生成*

---
<a id="sym-scrapy_extensions_logcount.py-45"></a>

### `LogCount.spider_closed` · method
```python
def spider_closed(self, spider: Spider, reason: str) -> None
```

*来源: `scrapy/extensions/logcount.py:45` · 待生成*

---

## `scrapy/extensions/logstats.py`

<a id="sym-scrapy_extensions_logstats.py-23"></a>

### `LogStats` · class
```python
class LogStats
```

*来源: `scrapy/extensions/logstats.py:23` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-29"></a>

### `LogStats.__init__` · method
```python
def __init__(self, stats: StatsCollector, interval: float = 60.0)
```

*来源: `scrapy/extensions/logstats.py:29` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-36"></a>

### `LogStats.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/extensions/logstats.py:36` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-46"></a>

### `LogStats.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`create_looping_call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-217)

*来源: `scrapy/extensions/logstats.py:46` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-53"></a>

### `LogStats.log` · method
```python
def log(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`LogStats.calculate_stats`](scrapy_extensions.md#sym-scrapy_extensions_logstats.py-68)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/logstats.py:53` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-68"></a>

### `LogStats.calculate_stats` · method
```python
def calculate_stats(self) -> None
```

*来源: `scrapy/extensions/logstats.py:68` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-75"></a>

### `LogStats.spider_closed` · method
```python
def spider_closed(self, spider: Spider, reason: str) -> None
```

**内部调用(库内):**
- [`LogStats.calculate_final_stats`](scrapy_extensions.md#sym-scrapy_extensions_logstats.py-83)

*来源: `scrapy/extensions/logstats.py:75` · 待生成*

---
<a id="sym-scrapy_extensions_logstats.py-83"></a>

### `LogStats.calculate_final_stats` · method
```python
def calculate_final_stats(
        self, spider: Spider
    ) -> tuple[None, None] | tuple[float, float]
```

*来源: `scrapy/extensions/logstats.py:83` · 待生成*

---

## `scrapy/extensions/memdebug.py`

<a id="sym-scrapy_extensions_memdebug.py-24"></a>

### `MemoryDebugger` · class
```python
class MemoryDebugger
```

*来源: `scrapy/extensions/memdebug.py:24` · 待生成*

---
<a id="sym-scrapy_extensions_memdebug.py-25"></a>

### `MemoryDebugger.__init__` · method
```python
def __init__(self, stats: StatsCollector)
```

*来源: `scrapy/extensions/memdebug.py:25` · 待生成*

---
<a id="sym-scrapy_extensions_memdebug.py-29"></a>

### `MemoryDebugger.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/memdebug.py:29` · 待生成*

---
<a id="sym-scrapy_extensions_memdebug.py-37"></a>

### `MemoryDebugger.spider_closed` · method
```python
def spider_closed(self, spider: Spider, reason: str) -> None
```

*来源: `scrapy/extensions/memdebug.py:37` · 待生成*

---

## `scrapy/extensions/memusage.py`

<a id="sym-scrapy_extensions_memusage.py-35"></a>

### `MemoryUsage` · class
```python
class MemoryUsage
```

*来源: `scrapy/extensions/memusage.py:35` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-36"></a>

### `MemoryUsage.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`MemoryUsage.from_crawler`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-69)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/extensions/memusage.py:36` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-69"></a>

### `MemoryUsage.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/memusage.py:69` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-72"></a>

### `MemoryUsage.get_virtual_size` · method
```python
def get_virtual_size(self) -> int
```

*来源: `scrapy/extensions/memusage.py:72` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-79"></a>

### `MemoryUsage.engine_started` · method
```python
def engine_started(self) -> None
```

**内部调用(库内):**
- [`MemoryUsage.get_virtual_size`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-72)
- [`create_looping_call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-217)

*来源: `scrapy/extensions/memusage.py:79` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-95"></a>

### `MemoryUsage.engine_stopped` · method
```python
def engine_stopped(self) -> None
```

*来源: `scrapy/extensions/memusage.py:95` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-100"></a>

### `MemoryUsage.update` · method
```python
def update(self) -> None
```

**内部调用(库内):**
- [`MemoryUsage.get_virtual_size`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-72)

*来源: `scrapy/extensions/memusage.py:100` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-104"></a>

### `MemoryUsage._check_limit` · method
```python
def _check_limit(self) -> None
```

**内部调用(库内):**
- [`MemoryUsage.get_virtual_size`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-72)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`MemoryUsage._send_report`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-158)
- [`_schedule_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-527)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/memusage.py:104` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-136"></a>

### `MemoryUsage._check_warning` · method
```python
def _check_warning(self) -> None
```

**内部调用(库内):**
- [`MemoryUsage.get_virtual_size`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-72)
- [`MemoryUsage._send_report`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-158)

*来源: `scrapy/extensions/memusage.py:136` · 待生成*

---
<a id="sym-scrapy_extensions_memusage.py-158"></a>

### `MemoryUsage._send_report` · method
```python
def _send_report(self, rcpts: list[str], subject: str) -> None
```

**内部调用(库内):**
- [`MemoryUsage.get_virtual_size`](scrapy_extensions.md#sym-scrapy_extensions_memusage.py-72)
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)
- [`get_engine_status`](scrapy_utils.md#sym-scrapy_utils_engine.py-13)

*来源: `scrapy/extensions/memusage.py:158` · 待生成*

---

## `scrapy/extensions/periodic_log.py`

<a id="sym-scrapy_extensions_periodic_log.py-28"></a>

### `PeriodicLog` · class
```python
class PeriodicLog
```

*来源: `scrapy/extensions/periodic_log.py:28` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-31"></a>

### `PeriodicLog.__init__` · method
```python
def __init__(
        self,
        stats: StatsCollector,
        interval: float = 60.0,
        ext_stats: dict[str, Any] | None = None,
        ext_delta: dict[str, Any] | None = None,
        ext_timing_enabled: bool = False,
    )
```

**内部调用(库内):**
- [`ScrapyJSONEncoder`](scrapy_utils.md#sym-scrapy_utils_serialize.py-12)

*来源: `scrapy/extensions/periodic_log.py:31` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-61"></a>

### `PeriodicLog.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)

*来源: `scrapy/extensions/periodic_log.py:61` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-105"></a>

### `PeriodicLog.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`create_looping_call`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-217)

*来源: `scrapy/extensions/periodic_log.py:105` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-113"></a>

### `PeriodicLog.log` · method
```python
def log(self) -> None
```

**内部调用(库内):**
- [`PeriodicLog.log_timing`](scrapy_extensions.md#sym-scrapy_extensions_periodic_log.py-134)
- [`PeriodicLog.log_delta`](scrapy_extensions.md#sym-scrapy_extensions_periodic_log.py-123)
- [`PeriodicLog.log_crawler_stats`](scrapy_extensions.md#sym-scrapy_extensions_periodic_log.py-146)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/periodic_log.py:113` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-123"></a>

### `PeriodicLog.log_delta` · method
```python
def log_delta(self) -> dict[str, Any]
```

**内部调用(库内):**
- [`PeriodicLog.param_allowed`](scrapy_extensions.md#sym-scrapy_extensions_periodic_log.py-154)

*来源: `scrapy/extensions/periodic_log.py:123` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-134"></a>

### `PeriodicLog.log_timing` · method
```python
def log_timing(self) -> dict[str, Any]
```

*来源: `scrapy/extensions/periodic_log.py:134` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-146"></a>

### `PeriodicLog.log_crawler_stats` · method
```python
def log_crawler_stats(self) -> dict[str, Any]
```

**内部调用(库内):**
- [`PeriodicLog.param_allowed`](scrapy_extensions.md#sym-scrapy_extensions_periodic_log.py-154)

*来源: `scrapy/extensions/periodic_log.py:146` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-154"></a>

### `PeriodicLog.param_allowed` · method
```python
def param_allowed(
        self, stat_name: str, include: Sequence[str], exclude: Sequence[str]
    ) -> bool
```

*来源: `scrapy/extensions/periodic_log.py:154` · 待生成*

---
<a id="sym-scrapy_extensions_periodic_log.py-166"></a>

### `PeriodicLog.spider_closed` · method
```python
def spider_closed(self, spider: Spider, reason: str) -> None
```

**内部调用(库内):**
- [`PeriodicLog.log`](scrapy_extensions.md#sym-scrapy_extensions_periodic_log.py-113)

*来源: `scrapy/extensions/periodic_log.py:166` · 待生成*

---

## `scrapy/extensions/postprocessing.py`

<a id="sym-scrapy_extensions_postprocessing.py-14"></a>

### `GzipPlugin` · class
```python
class GzipPlugin
```

*来源: `scrapy/extensions/postprocessing.py:14` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-27"></a>

### `GzipPlugin.__init__` · method
```python
def __init__(self, file: BinaryIO, feed_options: dict[str, Any]) -> None
```

*来源: `scrapy/extensions/postprocessing.py:27` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-41"></a>

### `GzipPlugin.write` · method
```python
def write(self, data: bytes) -> int
```

*来源: `scrapy/extensions/postprocessing.py:41` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-44"></a>

### `GzipPlugin.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/extensions/postprocessing.py:44` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-48"></a>

### `Bz2Plugin` · class
```python
class Bz2Plugin
```

*来源: `scrapy/extensions/postprocessing.py:48` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-59"></a>

### `Bz2Plugin.__init__` · method
```python
def __init__(self, file: BinaryIO, feed_options: dict[str, Any]) -> None
```

*来源: `scrapy/extensions/postprocessing.py:59` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-67"></a>

### `Bz2Plugin.write` · method
```python
def write(self, data: bytes) -> int
```

*来源: `scrapy/extensions/postprocessing.py:67` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-70"></a>

### `Bz2Plugin.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/extensions/postprocessing.py:70` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-74"></a>

### `LZMAPlugin` · class
```python
class LZMAPlugin
```

*来源: `scrapy/extensions/postprocessing.py:74` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-91"></a>

### `LZMAPlugin.__init__` · method
```python
def __init__(self, file: BinaryIO, feed_options: dict[str, Any]) -> None
```

*来源: `scrapy/extensions/postprocessing.py:91` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-108"></a>

### `LZMAPlugin.write` · method
```python
def write(self, data: bytes) -> int
```

*来源: `scrapy/extensions/postprocessing.py:108` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-111"></a>

### `LZMAPlugin.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/extensions/postprocessing.py:111` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-118"></a>

### `PostProcessingManager` · class
```python
class PostProcessingManager(IOBase)
```

*来源: `scrapy/extensions/postprocessing.py:118` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-128"></a>

### `PostProcessingManager.__init__` · method
```python
def __init__(
        self, plugins: list[Any], file: IO[bytes], feed_options: dict[str, Any]
    ) -> None
```

**内部调用(库内):**
- [`PostProcessingManager._load_plugins`](scrapy_extensions.md#sym-scrapy_extensions_postprocessing.py-159)
- [`PostProcessingManager._get_head_plugin`](scrapy_extensions.md#sym-scrapy_extensions_postprocessing.py-162)

*来源: `scrapy/extensions/postprocessing.py:128` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-136"></a>

### `PostProcessingManager.write` · method
```python
def write(self, data: bytes) -> int
```

*来源: `scrapy/extensions/postprocessing.py:136` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-147"></a>

### `PostProcessingManager.tell` · method
```python
def tell(self) -> int
```

*来源: `scrapy/extensions/postprocessing.py:147` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-150"></a>

### `PostProcessingManager.close` · method
```python
def close(self) -> None
```

*来源: `scrapy/extensions/postprocessing.py:150` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-156"></a>

### `PostProcessingManager.writable` · method
```python
def writable(self) -> bool
```

*来源: `scrapy/extensions/postprocessing.py:156` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-159"></a>

### `PostProcessingManager._load_plugins` · method
```python
def _load_plugins(self, plugins: list[Any]) -> list[Any]
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/extensions/postprocessing.py:159` · 待生成*

---
<a id="sym-scrapy_extensions_postprocessing.py-162"></a>

### `PostProcessingManager._get_head_plugin` · method
```python
def _get_head_plugin(self) -> Any
```

*来源: `scrapy/extensions/postprocessing.py:162` · 待生成*

---

## `scrapy/extensions/spiderstate.py`

<a id="sym-scrapy_extensions_spiderstate.py-18"></a>

### `SpiderState` · class
```python
class SpiderState
```

*来源: `scrapy/extensions/spiderstate.py:18` · 待生成*

---
<a id="sym-scrapy_extensions_spiderstate.py-21"></a>

### `SpiderState.__init__` · method
```python
def __init__(self, jobdir: str | None = None)
```

*来源: `scrapy/extensions/spiderstate.py:21` · 待生成*

---
<a id="sym-scrapy_extensions_spiderstate.py-25"></a>

### `SpiderState.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`job_dir`](scrapy_utils.md#sym-scrapy_utils_job.py-10)

*来源: `scrapy/extensions/spiderstate.py:25` · 待生成*

---
<a id="sym-scrapy_extensions_spiderstate.py-35"></a>

### `SpiderState.spider_closed` · method
```python
def spider_closed(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/spiderstate.py:35` · 待生成*

---
<a id="sym-scrapy_extensions_spiderstate.py-41"></a>

### `SpiderState.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

*来源: `scrapy/extensions/spiderstate.py:41` · 待生成*

---
<a id="sym-scrapy_extensions_spiderstate.py-49"></a>

### `SpiderState.statefn` · method
装饰器: `@property`
```python
def statefn(self) -> str
```

*来源: `scrapy/extensions/spiderstate.py:49` · 待生成*

---

## `scrapy/extensions/statsmailer.py`

<a id="sym-scrapy_extensions_statsmailer.py-33"></a>

### `StatsMailer` · class
```python
class StatsMailer
```

*来源: `scrapy/extensions/statsmailer.py:33` · 待生成*

---
<a id="sym-scrapy_extensions_statsmailer.py-34"></a>

### `StatsMailer.__init__` · method
```python
def __init__(self, stats: StatsCollector, recipients: list[str], mail: MailSender)
```

*来源: `scrapy/extensions/statsmailer.py:34` · 待生成*

---
<a id="sym-scrapy_extensions_statsmailer.py-40"></a>

### `StatsMailer.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/statsmailer.py:40` · 待生成*

---
<a id="sym-scrapy_extensions_statsmailer.py-50"></a>

### `StatsMailer.spider_closed` · method
```python
def spider_closed(self, spider: Spider) -> Deferred[None] | None
```

*来源: `scrapy/extensions/statsmailer.py:50` · 待生成*

---

## `scrapy/extensions/telnet.py`

<a id="sym-scrapy_extensions_telnet.py-42"></a>

### `TelnetConsole` · class
```python
class TelnetConsole(protocol.ServerFactory)
```

*来源: `scrapy/extensions/telnet.py:42` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-43"></a>

### `TelnetConsole.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/telnet.py:43` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-70"></a>

### `TelnetConsole.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/telnet.py:70` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-73"></a>

### `TelnetConsole.start_listening` · method
```python
def start_listening(self) -> None
```

**内部调用(库内):**
- [`listen_tcp`](scrapy_utils.md#sym-scrapy_utils_reactor.py-30)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/telnet.py:73` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-82"></a>

### `TelnetConsole.stop_listening` · method
```python
def stop_listening(self) -> None
```

*来源: `scrapy/extensions/telnet.py:82` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-85"></a>

### `TelnetConsole.protocol` · method
```python
def protocol(self) -> telnet.TelnetTransport
```

**内部调用(库内):**
- [`TelnetConsole._get_telnet_vars`](scrapy_extensions.md#sym-scrapy_extensions_telnet.py-105)
- [`TelnetConsole.Portal`](scrapy_extensions.md#sym-scrapy_extensions_telnet.py-86)

*来源: `scrapy/extensions/telnet.py:85` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-86"></a>

### `TelnetConsole.Portal` · class
```python
class Portal
```

*来源: `scrapy/extensions/telnet.py:86` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-89"></a>

### `Portal.login` · method
```python
def login(self_, credentials, mind, *interfaces)
```

**内部调用(库内):**
- [`TelnetConsole._get_telnet_vars`](scrapy_extensions.md#sym-scrapy_extensions_telnet.py-105)

*来源: `scrapy/extensions/telnet.py:89` · 待生成*

---
<a id="sym-scrapy_extensions_telnet.py-105"></a>

### `TelnetConsole._get_telnet_vars` · method
```python
def _get_telnet_vars(self) -> dict[str, Any]
```

**内部调用(库内):**
- [`print_engine_status`](scrapy_utils.md#sym-scrapy_utils_engine.py-52)

*来源: `scrapy/extensions/telnet.py:105` · 待生成*

---

## `scrapy/extensions/throttle.py`

<a id="sym-scrapy_extensions_throttle.py-21"></a>

### `AutoThrottle` · class
```python
class AutoThrottle
```

*来源: `scrapy/extensions/throttle.py:21` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-22"></a>

### `AutoThrottle.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。

*来源: `scrapy/extensions/throttle.py:22` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-42"></a>

### `AutoThrottle.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/extensions/throttle.py:42` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-45"></a>

### `AutoThrottle._spider_opened` · method
```python
def _spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`AutoThrottle._min_delay`](scrapy_extensions.md#sym-scrapy_extensions_throttle.py-50)
- [`AutoThrottle._max_delay`](scrapy_extensions.md#sym-scrapy_extensions_throttle.py-54)
- [`AutoThrottle._start_delay`](scrapy_extensions.md#sym-scrapy_extensions_throttle.py-57)

*来源: `scrapy/extensions/throttle.py:45` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-50"></a>

### `AutoThrottle._min_delay` · method
```python
def _min_delay(self, spider: Spider) -> float
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/extensions/throttle.py:50` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-54"></a>

### `AutoThrottle._max_delay` · method
```python
def _max_delay(self, spider: Spider) -> float
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/extensions/throttle.py:54` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-57"></a>

### `AutoThrottle._start_delay` · method
```python
def _start_delay(self, spider: Spider) -> float
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/extensions/throttle.py:57` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-62"></a>

### `AutoThrottle._response_downloaded` · method
```python
def _response_downloaded(
        self, response: Response, request: Request, spider: Spider
    ) -> None
```

**内部调用(库内):**
- [`AutoThrottle._get_slot`](scrapy_extensions.md#sym-scrapy_extensions_throttle.py-95)
- [`AutoThrottle._adjust_delay`](scrapy_extensions.md#sym-scrapy_extensions_throttle.py-104)
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/extensions/throttle.py:62` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-95"></a>

### `AutoThrottle._get_slot` · method
```python
def _get_slot(
        self, request: Request, spider: Spider
    ) -> tuple[str | None, Slot | None]
```

*来源: `scrapy/extensions/throttle.py:95` · 待生成*

---
<a id="sym-scrapy_extensions_throttle.py-104"></a>

### `AutoThrottle._adjust_delay` · method
```python
def _adjust_delay(self, slot: Slot, latency: float, response: Response) -> None
```

*来源: `scrapy/extensions/throttle.py:104` · 待生成*

---