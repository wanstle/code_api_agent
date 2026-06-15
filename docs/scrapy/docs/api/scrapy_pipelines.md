# API 参考:`scrapy/pipelines`

## `scrapy/pipelines/__init__.py`

<a id="sym-scrapy_pipelines___init__.py-31"></a>

### `ItemPipelineManager` · class
```python
class ItemPipelineManager(MiddlewareManager)
```

*来源: `scrapy/pipelines/__init__.py:31` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-35"></a>

### `ItemPipelineManager._get_mwlist_from_settings` · method
装饰器: `@classmethod`
```python
def _get_mwlist_from_settings(cls, settings: Settings) -> list[Any]
```

**内部调用(库内):**
- [`build_component_list`](scrapy_utils.md#sym-scrapy_utils_conf.py-20)
- [`BaseSettings.get_component_priority_dict_with_base`](scrapy_settings.md#sym-scrapy_settings___init__.py-338)

*来源: `scrapy/pipelines/__init__.py:35` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-40"></a>

### `ItemPipelineManager._add_middleware` · method
```python
def _add_middleware(self, mw: Any) -> None
```

**内部调用(库内):**
- [`MiddlewareManager._check_mw_method_spider_arg`](scrapy.md#sym-scrapy_middleware.py-119)

*来源: `scrapy/pipelines/__init__.py:40` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-51"></a>

### `ItemPipelineManager.process_item` · method
```python
def process_item(self, item: Any, spider: Spider) -> Deferred[Any]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`MiddlewareManager._set_compat_spider`](scrapy.md#sym-scrapy_middleware.py-70)
- [`ItemPipelineManager.process_item_async`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-60)

*来源: `scrapy/pipelines/__init__.py:51` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-60"></a>

### `ItemPipelineManager.process_item_async` · method
```python
async def process_item_async(self, item: Any) -> Any
```

**内部调用(库内):**
- [`MiddlewareManager._process_chain`](scrapy.md#sym-scrapy_middleware.py-131)

*来源: `scrapy/pipelines/__init__.py:60` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-65"></a>

### `ItemPipelineManager._get_dfd` · method
```python
def _get_dfd(
        self,
        method: Callable[..., Coroutine[Any, Any, None] | Deferred[None] | None],
    ) -> Deferred[None]
```

**内部调用(库内):**
- [`_maybeDeferred_coro`](scrapy_utils.md#sym-scrapy_utils_defer.py-434)

*来源: `scrapy/pipelines/__init__.py:65` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-74"></a>

### `ItemPipelineManager._eb` · method
装饰器: `@staticmethod`
```python
def _eb(failure: Failure) -> Failure
```

*来源: `scrapy/pipelines/__init__.py:74` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-78"></a>

### `ItemPipelineManager._process_parallel_dfd` · method
```python
def _process_parallel_dfd(self, methodname: str) -> Deferred[list[None]]
```

**内部调用(库内):**
- [`ItemPipelineManager._get_dfd`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-65)

*来源: `scrapy/pipelines/__init__.py:78` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-93"></a>

### `ItemPipelineManager.get_awaitable` · method
```python
def get_awaitable(
        self,
        method: Callable[..., Coroutine[Any, Any, None] | Deferred[None] | None],
    ) -> Awaitable[None]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/pipelines/__init__.py:93` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-103"></a>

### `ItemPipelineManager._process_parallel_asyncio` · method
```python
async def _process_parallel_asyncio(self, methodname: str) -> list[None]
```

**内部调用(库内):**
- [`ItemPipelineManager.get_awaitable`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-93)

*来源: `scrapy/pipelines/__init__.py:103` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-115"></a>

### `ItemPipelineManager._process_parallel` · method
```python
async def _process_parallel(self, methodname: str) -> list[None]
```

**内部调用(库内):**
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`ItemPipelineManager._process_parallel_asyncio`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-103)
- [`ItemPipelineManager._process_parallel_dfd`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-78)

*来源: `scrapy/pipelines/__init__.py:115` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-120"></a>

### `ItemPipelineManager.open_spider` · method
```python
def open_spider(self, spider: Spider) -> Deferred[list[None]]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`MiddlewareManager._set_compat_spider`](scrapy.md#sym-scrapy_middleware.py-70)
- [`ItemPipelineManager._process_parallel`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-115)

*来源: `scrapy/pipelines/__init__.py:120` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-129"></a>

### `ItemPipelineManager.open_spider_async` · method
```python
async def open_spider_async(self) -> None
```

**内部调用(库内):**
- [`ItemPipelineManager._process_parallel`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-115)

*来源: `scrapy/pipelines/__init__.py:129` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-132"></a>

### `ItemPipelineManager.close_spider` · method
```python
def close_spider(self, spider: Spider) -> Deferred[list[None]]
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`MiddlewareManager._set_compat_spider`](scrapy.md#sym-scrapy_middleware.py-70)
- [`ItemPipelineManager._process_parallel`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-115)

*来源: `scrapy/pipelines/__init__.py:132` · 待生成*

---
<a id="sym-scrapy_pipelines___init__.py-141"></a>

### `ItemPipelineManager.close_spider_async` · method
```python
async def close_spider_async(self) -> None
```

**内部调用(库内):**
- [`ItemPipelineManager._process_parallel`](scrapy_pipelines.md#sym-scrapy_pipelines___init__.py-115)

*来源: `scrapy/pipelines/__init__.py:141` · 待生成*

---

## `scrapy/pipelines/files.py`

<a id="sym-scrapy_pipelines_files.py-57"></a>

### `_to_string` · func
```python
def _to_string(path: str | PathLike[str]) -> str
```

*来源: `scrapy/pipelines/files.py:57` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-61"></a>

### `_md5sum` · func
```python
def _md5sum(file: IO[bytes]) -> str
```

*来源: `scrapy/pipelines/files.py:61` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-78"></a>

### `FileException` · class
```python
class FileException(Exception)
```

*来源: `scrapy/pipelines/files.py:78` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-82"></a>

### `StatInfo` · class
```python
class StatInfo(TypedDict, total=False)
```

*来源: `scrapy/pipelines/files.py:82` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-87"></a>

### `FilesStoreProtocol` · class
```python
class FilesStoreProtocol(Protocol)
```

*来源: `scrapy/pipelines/files.py:87` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-88"></a>

### `FilesStoreProtocol.__init__` · method
```python
def __init__(self, basedir: str)
```

*来源: `scrapy/pipelines/files.py:88` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-90"></a>

### `FilesStoreProtocol.persist_file` · method
```python
def persist_file(
        self,
        path: str,
        buf: BytesIO,
        info: MediaPipeline.SpiderInfo,
        meta: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Deferred[Any] | None
```

*来源: `scrapy/pipelines/files.py:90` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-99"></a>

### `FilesStoreProtocol.stat_file` · method
```python
def stat_file(
        self, path: str, info: MediaPipeline.SpiderInfo
    ) -> StatInfo | Deferred[StatInfo]
```

*来源: `scrapy/pipelines/files.py:99` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-104"></a>

### `FSFilesStore` · class
```python
class FSFilesStore
```

*来源: `scrapy/pipelines/files.py:104` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-105"></a>

### `FSFilesStore.__init__` · method
```python
def __init__(self, basedir: str | PathLike[str])
```

**内部调用(库内):**
- [`_to_string`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-57)
- [`FSFilesStore._mkdir`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-145)

*来源: `scrapy/pipelines/files.py:105` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-115"></a>

### `FSFilesStore.persist_file` · method
```python
def persist_file(
        self,
        path: str | PathLike[str],
        buf: BytesIO,
        info: MediaPipeline.SpiderInfo,
        meta: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None
```

**内部调用(库内):**
- [`FSFilesStore._get_filesystem_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-141)
- [`FSFilesStore._mkdir`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-145)

*来源: `scrapy/pipelines/files.py:115` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-127"></a>

### `FSFilesStore.stat_file` · method
```python
def stat_file(
        self, path: str | PathLike[str], info: MediaPipeline.SpiderInfo
    ) -> StatInfo
```

**内部调用(库内):**
- [`FSFilesStore._get_filesystem_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-141)
- [`_md5sum`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-61)

*来源: `scrapy/pipelines/files.py:127` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-141"></a>

### `FSFilesStore._get_filesystem_path` · method
```python
def _get_filesystem_path(self, path: str | PathLike[str]) -> Path
```

**内部调用(库内):**
- [`_to_string`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-57)

*来源: `scrapy/pipelines/files.py:141` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-145"></a>

### `FSFilesStore._mkdir` · method
```python
def _mkdir(
        self, dirname: Path, domain: MediaPipeline.SpiderInfo | None = None
    ) -> None
```

*来源: `scrapy/pipelines/files.py:145` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-155"></a>

### `S3FilesStore` · class
```python
class S3FilesStore
```

*来源: `scrapy/pipelines/files.py:155` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-169"></a>

### `S3FilesStore.__init__` · method
```python
def __init__(self, uri: str)
```

**内部调用(库内):**
- [`is_botocore_available`](scrapy_utils.md#sym-scrapy_utils_boto.py-4)
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。

*来源: `scrapy/pipelines/files.py:169` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-190"></a>

### `S3FilesStore._onsuccess` · method
装饰器: `@staticmethod`
```python
def _onsuccess(boto_key: dict[str, Any]) -> StatInfo
```

*来源: `scrapy/pipelines/files.py:190` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-196"></a>

### `S3FilesStore.stat_file` · method
```python
def stat_file(
        self, path: str, info: MediaPipeline.SpiderInfo
    ) -> Deferred[StatInfo]
```

**内部调用(库内):**
- [`S3FilesStore._get_boto_key`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-202)

*来源: `scrapy/pipelines/files.py:196` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-202"></a>

### `S3FilesStore._get_boto_key` · method
```python
def _get_boto_key(self, path: str) -> Deferred[dict[str, Any]]
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/pipelines/files.py:202` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-212"></a>

### `S3FilesStore.persist_file` · method
```python
def persist_file(
        self,
        path: str,
        buf: BytesIO,
        info: MediaPipeline.SpiderInfo,
        meta: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Deferred[Any]
```

**内部调用(库内):**
- [`S3FilesStore._headers_to_botocore_kwargs`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-238)
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/pipelines/files.py:212` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-238"></a>

### `S3FilesStore._headers_to_botocore_kwargs` · method
```python
def _headers_to_botocore_kwargs(self, headers: dict[str, Any]) -> dict[str, Any]
```

**内部调用(库内):**
- [`CaseInsensitiveDict`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-102)

*来源: `scrapy/pipelines/files.py:238` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-282"></a>

### `GCSFilesStore` · class
```python
class GCSFilesStore
```

*来源: `scrapy/pipelines/files.py:282` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-291"></a>

### `GCSFilesStore.__init__` · method
```python
def __init__(self, uri: str)
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/pipelines/files.py:291` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-314"></a>

### `GCSFilesStore._onsuccess` · method
装饰器: `@staticmethod`
```python
def _onsuccess(blob: Any) -> StatInfo
```

*来源: `scrapy/pipelines/files.py:314` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-321"></a>

### `GCSFilesStore.stat_file` · method
```python
def stat_file(
        self, path: str, info: MediaPipeline.SpiderInfo
    ) -> Deferred[StatInfo]
```

**内部调用(库内):**
- [`GCSFilesStore._get_blob_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-336)
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/pipelines/files.py:321` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-331"></a>

### `GCSFilesStore._get_content_type` · method
```python
def _get_content_type(self, headers: dict[str, str] | None) -> str
```

*来源: `scrapy/pipelines/files.py:331` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-336"></a>

### `GCSFilesStore._get_blob_path` · method
```python
def _get_blob_path(self, path: str) -> str
```

*来源: `scrapy/pipelines/files.py:336` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-339"></a>

### `GCSFilesStore.persist_file` · method
```python
def persist_file(
        self,
        path: str,
        buf: BytesIO,
        info: MediaPipeline.SpiderInfo,
        meta: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Deferred[Any]
```

**内部调用(库内):**
- [`GCSFilesStore._get_blob_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-336)
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)
- [`GCSFilesStore._get_content_type`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-331)

*来源: `scrapy/pipelines/files.py:339` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-361"></a>

### `FTPFilesStore` · class
```python
class FTPFilesStore
```

*来源: `scrapy/pipelines/files.py:361` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-366"></a>

### `FTPFilesStore.__init__` · method
```python
def __init__(self, uri: str)
```

*来源: `scrapy/pipelines/files.py:366` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-381"></a>

### `FTPFilesStore.persist_file` · method
```python
def persist_file(
        self,
        path: str,
        buf: BytesIO,
        info: MediaPipeline.SpiderInfo,
        meta: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Deferred[Any]
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/pipelines/files.py:381` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-403"></a>

### `FTPFilesStore._stat_file` · method
```python
def _stat_file(self, path: str) -> StatInfo
```

**内部调用(库内):**
- [`Portal.login`](scrapy_extensions.md#sym-scrapy_extensions_telnet.py-89)

*来源: `scrapy/pipelines/files.py:403` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-419"></a>

### `FTPFilesStore.stat_file` · method
```python
def stat_file(
        self, path: str, info: MediaPipeline.SpiderInfo
    ) -> Deferred[StatInfo]
```

**内部调用(库内):**
- [`run_in_thread`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-296)

*来源: `scrapy/pipelines/files.py:419` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-425"></a>

### `FilesPipeline` · class
```python
class FilesPipeline(MediaPipeline)
```

*来源: `scrapy/pipelines/files.py:425` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-456"></a>

### `FilesPipeline.__init__` · method
```python
def __init__(
        self,
        store_uri: str | PathLike[str],
        download_func: None = None,
        *,
        crawler: Crawler,
    )
```

**内部调用(库内):**
- [`_to_string`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-57)
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`FilesPipeline._get_store`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-536)
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/pipelines/files.py:456` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-503"></a>

### `FilesPipeline.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`FilesPipeline._update_stores`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-510)

*来源: `scrapy/pipelines/files.py:503` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-510"></a>

### `FilesPipeline._update_stores` · method
装饰器: `@classmethod`
```python
def _update_stores(cls, settings: BaseSettings) -> None
```

*来源: `scrapy/pipelines/files.py:510` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-536"></a>

### `FilesPipeline._get_store` · method
```python
def _get_store(self, uri: str) -> FilesStoreProtocol
```

*来源: `scrapy/pipelines/files.py:536` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-542"></a>

### `FilesPipeline._onsuccess` · method
```python
def _onsuccess(
        self,
        result: StatInfo,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        path: str,
    ) -> FileInfo | None
```

**内部调用(库内):**
- [`referer_str`](scrapy_utils.md#sym-scrapy_utils_request.py-150)
- [`FilesPipeline.inc_stats`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-684)

*来源: `scrapy/pipelines/files.py:542` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-578"></a>

### `FilesPipeline.media_to_download` · method
```python
def media_to_download(
        self, request: Request, info: MediaPipeline.SpiderInfo, *, item: Any = None
    ) -> Deferred[FileInfo | None] | None
```

**内部调用(库内):**
- [`FilesPipeline.file_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-732)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)

*来源: `scrapy/pipelines/files.py:578` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-597"></a>

### `FilesPipeline.media_failed` · method
```python
def media_failed(
        self, failure: Failure, request: Request, info: MediaPipeline.SpiderInfo
    ) -> NoReturn
```

**内部调用(库内):**
- [`referer_str`](scrapy_utils.md#sym-scrapy_utils_request.py-150)

*来源: `scrapy/pipelines/files.py:597` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-616"></a>

### `FilesPipeline.media_downloaded` · method
```python
async def media_downloaded(
        self,
        response: Response,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item: Any = None,
    ) -> FileInfo
```

**内部调用(库内):**
- [`referer_str`](scrapy_utils.md#sym-scrapy_utils_request.py-150)
- [`FileException`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-78)
- [`FilesPipeline.inc_stats`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-684)
- [`FilesPipeline.file_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-732)
- [`FilesPipeline.file_downloaded`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-715)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)

*来源: `scrapy/pipelines/files.py:616` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-684"></a>

### `FilesPipeline.inc_stats` · method
```python
def inc_stats(self, status: str) -> None
```

*来源: `scrapy/pipelines/files.py:684` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-689"></a>

### `FilesPipeline._file_downloaded` · method
```python
async def _file_downloaded(
        self,
        response: Response,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item: Any = None,
    ) -> str
```

**内部调用(库内):**
- [`FilesPipeline.file_path`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-732)
- [`_md5sum`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-61)
- [`FilesStoreProtocol.persist_file`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-90)

*来源: `scrapy/pipelines/files.py:689` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-705"></a>

### `FilesPipeline.get_media_requests` · method
```python
def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/pipelines/files.py:705` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-715"></a>

### `FilesPipeline.file_downloaded` · method
```python
def file_downloaded(
        self,
        response: Response,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item: Any = None,
    ) -> str | Awaitable[str]
```

**内部调用(库内):**
- [`FilesPipeline._file_downloaded`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-689)

*来源: `scrapy/pipelines/files.py:715` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-725"></a>

### `FilesPipeline.item_completed` · method
```python
def item_completed(
        self, results: list[FileInfoOrError], item: Any, info: MediaPipeline.SpiderInfo
    ) -> Any
```

*来源: `scrapy/pipelines/files.py:725` · 待生成*

---
<a id="sym-scrapy_pipelines_files.py-732"></a>

### `FilesPipeline.file_path` · method
```python
def file_path(
        self,
        request: Request,
        response: Response | None = None,
        info: MediaPipeline.SpiderInfo | None = None,
        *,
        item: Any = None,
    ) -> str
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/pipelines/files.py:732` · 待生成*

---

## `scrapy/pipelines/images.py`

<a id="sym-scrapy_pipelines_images.py-38"></a>

### `ImageException` · class
```python
class ImageException(FileException)
```

*来源: `scrapy/pipelines/images.py:38` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-42"></a>

### `ImagesPipeline` · class
```python
class ImagesPipeline(FilesPipeline)
```

*来源: `scrapy/pipelines/images.py:42` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-56"></a>

### `ImagesPipeline.__init__` · method
```python
def __init__(
        self,
        store_uri: str | PathLike[str],
        download_func: None = None,
        *,
        crawler: Crawler,
    )
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/pipelines/images.py:56` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-113"></a>

### `ImagesPipeline.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`FilesPipeline._update_stores`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-510)

*来源: `scrapy/pipelines/images.py:113` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-119"></a>

### `ImagesPipeline.file_downloaded` · method
```python
async def file_downloaded(
        self,
        response: Response,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item: Any = None,
    ) -> str
```

**内部调用(库内):**
- [`ImagesPipeline.image_downloaded`](scrapy_pipelines.md#sym-scrapy_pipelines_images.py-129)

*来源: `scrapy/pipelines/images.py:119` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-129"></a>

### `ImagesPipeline.image_downloaded` · method
```python
async def image_downloaded(
        self,
        response: Response,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item: Any = None,
    ) -> str
```

**内部调用(库内):**
- [`ImagesPipeline.get_images`](scrapy_pipelines.md#sym-scrapy_pipelines_images.py-155)
- [`_md5sum`](scrapy_pipelines.md#sym-scrapy_pipelines_files.py-61)

*来源: `scrapy/pipelines/images.py:129` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-155"></a>

### `ImagesPipeline.get_images` · method
```python
def get_images(
        self,
        response: Response,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item: Any = None,
    ) -> Iterable[tuple[str, Image.Image, BytesIO]]
```

**内部调用(库内):**
- [`ImagesPipeline.file_path`](scrapy_pipelines.md#sym-scrapy_pipelines_images.py-240)
- [`ImageException`](scrapy_pipelines.md#sym-scrapy_pipelines_images.py-38)
- [`ImagesPipeline.convert_image`](scrapy_pipelines.md#sym-scrapy_pipelines_images.py-187)
- [`ImagesPipeline.thumb_path`](scrapy_pipelines.md#sym-scrapy_pipelines_images.py-251)

*来源: `scrapy/pipelines/images.py:155` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-187"></a>

### `ImagesPipeline.convert_image` · method
```python
def convert_image(
        self,
        image: Image.Image,
        size: tuple[int, int] | None = None,
        *,
        response_body: BytesIO,
    ) -> tuple[Image.Image, BytesIO]
```

*来源: `scrapy/pipelines/images.py:187` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-223"></a>

### `ImagesPipeline.get_media_requests` · method
```python
def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/pipelines/images.py:223` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-233"></a>

### `ImagesPipeline.item_completed` · method
```python
def item_completed(
        self, results: list[FileInfoOrError], item: Any, info: MediaPipeline.SpiderInfo
    ) -> Any
```

*来源: `scrapy/pipelines/images.py:233` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-240"></a>

### `ImagesPipeline.file_path` · method
```python
def file_path(
        self,
        request: Request,
        response: Response | None = None,
        info: MediaPipeline.SpiderInfo | None = None,
        *,
        item: Any = None,
    ) -> str
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/pipelines/images.py:240` · 待生成*

---
<a id="sym-scrapy_pipelines_images.py-251"></a>

### `ImagesPipeline.thumb_path` · method
```python
def thumb_path(
        self,
        request: Request,
        thumb_id: str,
        response: Response | None = None,
        info: MediaPipeline.SpiderInfo | None = None,
        *,
        item: Any = None,
    ) -> str
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/pipelines/images.py:251` · 待生成*

---

## `scrapy/pipelines/media.py`

<a id="sym-scrapy_pipelines_media.py-44"></a>

### `FileInfo` · class
```python
class FileInfo(TypedDict)
```

*来源: `scrapy/pipelines/media.py:44` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-58"></a>

### `MediaPipeline` · class
```python
class MediaPipeline(ABC)
```

*来源: `scrapy/pipelines/media.py:58` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-61"></a>

### `MediaPipeline.SpiderInfo` · class
```python
class SpiderInfo
```

*来源: `scrapy/pipelines/media.py:61` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-62"></a>

### `SpiderInfo.__init__` · method
```python
def __init__(self, spider: Spider)
```

*来源: `scrapy/pipelines/media.py:62` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-70"></a>

### `MediaPipeline.__init__` · method
```python
def __init__(
        self,
        download_func: None = None,
        *,
        crawler: Crawler,
    )
```

**内部调用(库内):**
- [`MediaPipeline._handle_statuses`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-98)

*来源: `scrapy/pipelines/media.py:70` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-98"></a>

### `MediaPipeline._handle_statuses` · method
```python
def _handle_statuses(self, allow_redirects: bool) -> None
```

**内部调用(库内):**
- [`SequenceExclude`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-189)

*来源: `scrapy/pipelines/media.py:98` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-103"></a>

### `MediaPipeline._key_for_pipe` · method
```python
def _key_for_pipe(
        self,
        key: str,
        base_class_name: str | None = None,
        settings: Settings | None = None,
    ) -> str
```

*来源: `scrapy/pipelines/media.py:103` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-120"></a>

### `MediaPipeline.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/pipelines/media.py:120` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-124"></a>

### `MediaPipeline.open_spider` · method
装饰器: `@_warn_spider_arg`
```python
def open_spider(self, spider: Spider | None = None) -> None
```

**内部调用(库内):**
- [`MediaPipeline.SpiderInfo`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-61)

*来源: `scrapy/pipelines/media.py:124` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-129"></a>

### `MediaPipeline.process_item` · method
装饰器: `@_warn_spider_arg`
```python
async def process_item(self, item: Any, spider: Spider | None = None) -> Any
```

**内部调用(库内):**
- [`MediaPipeline.get_media_requests`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-276)
- [`MediaPipeline._process_request`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-151)
- [`is_asyncio_available`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-34)
- [`MediaPipeline.item_completed`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-299)

*来源: `scrapy/pipelines/media.py:129` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-151"></a>

### `MediaPipeline._process_request` · method
```python
async def _process_request(
        self, request: Request, info: SpiderInfo, item: Any
    ) -> FileInfo
```

**内部调用(库内):**
- [`_defer_sleep_async`](scrapy_utils.md#sym-scrapy_utils_defer.py-89)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)
- [`MediaPipeline.media_to_download`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-269)
- [`MediaPipeline._check_media_to_download`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-206)
- [`MediaPipeline._cache_result_and_execute_waiters`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-227)

*来源: `scrapy/pipelines/media.py:151` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-200"></a>

### `MediaPipeline._modify_media_request` · method
```python
def _modify_media_request(self, request: Request) -> None
```

*来源: `scrapy/pipelines/media.py:200` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-206"></a>

### `MediaPipeline._check_media_to_download` · method
```python
async def _check_media_to_download(
        self, request: Request, info: SpiderInfo, item: Any
    ) -> FileInfo
```

**内部调用(库内):**
- [`MediaPipeline._modify_media_request`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-200)
- [`MediaPipeline.media_downloaded`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-281)
- [`MediaPipeline.media_failed`](scrapy_pipelines.md#sym-scrapy_pipelines_media.py-293)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/pipelines/media.py:206` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-227"></a>

### `MediaPipeline._cache_result_and_execute_waiters` · method
```python
def _cache_result_and_execute_waiters(
        self, result: FileInfo | Failure, fp: bytes, info: SpiderInfo
    ) -> None
```

**内部调用(库内):**
- [`call_later`](scrapy_utils.md#sym-scrapy_utils_asyncio.py-234)

*来源: `scrapy/pipelines/media.py:227` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-269"></a>

### `MediaPipeline.media_to_download` · method
装饰器: `@abstractmethod`
```python
def media_to_download(
        self, request: Request, info: SpiderInfo, *, item: Any = None
    ) -> Deferred[FileInfo | None] | None
```

*来源: `scrapy/pipelines/media.py:269` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-276"></a>

### `MediaPipeline.get_media_requests` · method
装饰器: `@abstractmethod`
```python
def get_media_requests(self, item: Any, info: SpiderInfo) -> list[Request]
```

*来源: `scrapy/pipelines/media.py:276` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-281"></a>

### `MediaPipeline.media_downloaded` · method
装饰器: `@abstractmethod`
```python
def media_downloaded(
        self,
        response: Response,
        request: Request,
        info: SpiderInfo,
        *,
        item: Any = None,
    ) -> FileInfo | Awaitable[FileInfo]
```

*来源: `scrapy/pipelines/media.py:281` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-293"></a>

### `MediaPipeline.media_failed` · method
装饰器: `@abstractmethod`
```python
def media_failed(
        self, failure: Failure, request: Request, info: SpiderInfo
    ) -> Failure
```

*来源: `scrapy/pipelines/media.py:293` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-299"></a>

### `MediaPipeline.item_completed` · method
```python
def item_completed(
        self, results: list[FileInfoOrError], item: Any, info: SpiderInfo
    ) -> Any
```

**内部调用(库内):**
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`failure_to_exc_info`](scrapy_utils.md#sym-scrapy_utils_log.py-28)

*来源: `scrapy/pipelines/media.py:299` · 待生成*

---
<a id="sym-scrapy_pipelines_media.py-316"></a>

### `MediaPipeline.file_path` · method
装饰器: `@abstractmethod`
```python
def file_path(
        self,
        request: Request,
        response: Response | None = None,
        info: SpiderInfo | None = None,
        *,
        item: Any = None,
    ) -> str
```

*来源: `scrapy/pipelines/media.py:316` · 待生成*

---