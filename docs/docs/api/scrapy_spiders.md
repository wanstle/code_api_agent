# API 参考:`scrapy/spiders`

## `scrapy/spiders/__init__.py`

<a id="sym-scrapy_spiders___init__.py-31"></a>

### `Spider` · class
```python
class Spider(object_ref)
```

*来源: `scrapy/spiders/__init__.py:31` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-45"></a>

### `Spider.__init__` · method
```python
def __init__(self, name: str | None = None, **kwargs: Any)
```

*来源: `scrapy/spiders/__init__.py:45` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-55"></a>

### `Spider.logger` · method
装饰器: `@property`
```python
def logger(self) -> SpiderLoggerAdapter
```

**内部调用(库内):**
- [`SpiderLoggerAdapter`](scrapy_utils.md#sym-scrapy_utils_log.py-264)

*来源: `scrapy/spiders/__init__.py:55` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-62"></a>

### `Spider.log` · method
```python
def log(self, message: Any, level: int = logging.DEBUG, **kw: Any) -> None
```

*来源: `scrapy/spiders/__init__.py:62` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-72"></a>

### `Spider.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self
```

**内部调用(库内):**
- [`Spider._set_crawler`](scrapy_spiders.md#sym-scrapy_spiders___init__.py-77)

*来源: `scrapy/spiders/__init__.py:72` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-77"></a>

### `Spider._set_crawler` · method
```python
def _set_crawler(self, crawler: Crawler) -> None
```

*来源: `scrapy/spiders/__init__.py:77` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-82"></a>

### `Spider.start` · method
```python
async def start(self) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/spiders/__init__.py:82` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-137"></a>

### `Spider._parse` · method
```python
def _parse(self, response: Response, **kwargs: Any) -> Any
```

**内部调用(库内):**
- [`Spider.parse`](scrapy_spiders.md#sym-scrapy_spiders___init__.py-144)

*来源: `scrapy/spiders/__init__.py:137` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-144"></a>

### `Spider.parse` · method
```python
def parse(self, response: Response, **kwargs: Any) -> Any
```

*来源: `scrapy/spiders/__init__.py:144` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-150"></a>

### `Spider.update_settings` · method
装饰器: `@classmethod`
```python
def update_settings(cls, settings: BaseSettings) -> None
```

**内部调用(库内):**
- [`BaseSettings.setdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-535)

*来源: `scrapy/spiders/__init__.py:150` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-154"></a>

### `Spider.handles_request` · method
装饰器: `@classmethod`
```python
def handles_request(cls, request: Request) -> bool
```

**内部调用(库内):**
- [`url_is_from_spider`](scrapy_utils.md#sym-scrapy_utils_url.py-36)

*来源: `scrapy/spiders/__init__.py:154` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-158"></a>

### `Spider.close` · method
装饰器: `@staticmethod`
```python
def close(spider: Spider, reason: str) -> Deferred[None] | None
```

*来源: `scrapy/spiders/__init__.py:158` · 待生成*

---
<a id="sym-scrapy_spiders___init__.py-164"></a>

### `Spider.__repr__` · method
```python
def __repr__(self) -> str
```

*来源: `scrapy/spiders/__init__.py:164` · 待生成*

---

## `scrapy/spiders/crawl.py`

<a id="sym-scrapy_spiders_crawl.py-42"></a>

### `_identity` · func
```python
def _identity(x: _T) -> _T
```

*来源: `scrapy/spiders/crawl.py:42` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-46"></a>

### `_identity_process_request` · func
```python
def _identity_process_request(request: Request, response: Response) -> Request | None
```

*来源: `scrapy/spiders/crawl.py:46` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-50"></a>

### `_get_method` · func
```python
def _get_method(
    method: Callable[..., Any] | str | None, spider: Spider
) -> Callable[..., Any] | None
```

*来源: `scrapy/spiders/crawl.py:50` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-63"></a>

### `Rule` · class
```python
class Rule
```

*来源: `scrapy/spiders/crawl.py:63` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-64"></a>

### `Rule.__init__` · method
```python
def __init__(
        self,
        link_extractor: LinkExtractor | None = None,
        callback: CallbackT | str | None = None,
        cb_kwargs: dict[str, Any] | None = None,
        follow: bool | None = None,
        process_links: ProcessLinksT | str | None = None,
        process_request: ProcessRequestT | str | None = None,
        errback: Callable[[Failure], Any] | str | None = None,
    )
```

*来源: `scrapy/spiders/crawl.py:64` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-84"></a>

### `Rule._compile` · method
```python
def _compile(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`_get_method`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-50)

*来源: `scrapy/spiders/crawl.py:84` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-98"></a>

### `CrawlSpider` · class
```python
class CrawlSpider(Spider)
```

*来源: `scrapy/spiders/crawl.py:98` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-103"></a>

### `CrawlSpider.__init__` · method
```python
def __init__(self, *a: Any, **kw: Any)
```

**内部调用(库内):**
- [`CrawlSpider._compile_rules`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-213)
- [`method_is_overridden`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-169)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/spiders/crawl.py:103` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-116"></a>

### `CrawlSpider._parse` · method
```python
def _parse(self, response: Response, **kwargs: Any) -> Any
```

**内部调用(库内):**
- [`CrawlSpider.parse_with_rules`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-170)

*来源: `scrapy/spiders/crawl.py:116` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-124"></a>

### `CrawlSpider.parse_start_url` · method
```python
def parse_start_url(self, response: Response, **kwargs: Any) -> Any
```

*来源: `scrapy/spiders/crawl.py:124` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-127"></a>

### `CrawlSpider.process_results` · method
```python
def process_results(
        self, response: Response, results: Iterable[Any]
    ) -> Iterable[Any]
```

*来源: `scrapy/spiders/crawl.py:127` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-132"></a>

### `CrawlSpider._build_request` · method
```python
def _build_request(self, rule_index: int, link: Link) -> Request
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/spiders/crawl.py:132` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-140"></a>

### `CrawlSpider._requests_to_follow` · method
```python
def _requests_to_follow(self, response: Response) -> Iterable[Request | None]
```

**内部调用(库内):**
- [`CrawlSpider._build_request`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-132)

*来源: `scrapy/spiders/crawl.py:140` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-155"></a>

### `CrawlSpider._callback` · method
```python
def _callback(self, response: Response, **cb_kwargs: Any) -> Any
```

**内部调用(库内):**
- [`CrawlSpider.parse_with_rules`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-170)

*来源: `scrapy/spiders/crawl.py:155` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-164"></a>

### `CrawlSpider._errback` · method
```python
def _errback(self, failure: Failure) -> Iterable[Any]
```

**内部调用(库内):**
- [`CrawlSpider._handle_failure`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-206)

*来源: `scrapy/spiders/crawl.py:164` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-170"></a>

### `CrawlSpider.parse_with_rules` · method
```python
async def parse_with_rules(
        self,
        response: Response,
        callback: CallbackT | None,
        cb_kwargs: dict[str, Any],
        follow: bool = True,
    ) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)
- [`collect_asyncgen`](scrapy_utils.md#sym-scrapy_utils_asyncgen.py-9)
- [`CrawlSpider.process_results`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-127)
- [`CrawlSpider._requests_to_follow`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-140)

*来源: `scrapy/spiders/crawl.py:170` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-191"></a>

### `CrawlSpider._parse_response` · method
```python
def _parse_response(
        self,
        response: Response,
        callback: CallbackT | None,
        cb_kwargs: dict[str, Any],
        follow: bool = True,
    ) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`CrawlSpider.parse_with_rules`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-170)

*来源: `scrapy/spiders/crawl.py:191` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-206"></a>

### `CrawlSpider._handle_failure` · method
```python
def _handle_failure(
        self, failure: Failure, errback: Callable[[Failure], Any] | None
    ) -> Iterable[Any]
```

*来源: `scrapy/spiders/crawl.py:206` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-213"></a>

### `CrawlSpider._compile_rules` · method
```python
def _compile_rules(self) -> None
```

**内部调用(库内):**
- [`Rule._compile`](scrapy_spiders.md#sym-scrapy_spiders_crawl.py-84)

*来源: `scrapy/spiders/crawl.py:213` · 待生成*

---
<a id="sym-scrapy_spiders_crawl.py-221"></a>

### `CrawlSpider.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self
```

*来源: `scrapy/spiders/crawl.py:221` · 待生成*

---

## `scrapy/spiders/feed.py`

<a id="sym-scrapy_spiders_feed.py-23"></a>

### `XMLFeedSpider` · class
```python
class XMLFeedSpider(Spider)
```

*来源: `scrapy/spiders/feed.py:23` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-37"></a>

### `XMLFeedSpider.process_results` · method
```python
def process_results(
        self, response: Response, results: Iterable[Any]
    ) -> Iterable[Any]
```

*来源: `scrapy/spiders/feed.py:37` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-49"></a>

### `XMLFeedSpider.adapt_response` · method
```python
def adapt_response(self, response: Response) -> Response
```

*来源: `scrapy/spiders/feed.py:49` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-56"></a>

### `XMLFeedSpider.parse_node` · method
```python
def parse_node(self, response: Response, selector: Selector) -> Any
```

*来源: `scrapy/spiders/feed.py:56` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-62"></a>

### `XMLFeedSpider.parse_nodes` · method
```python
def parse_nodes(self, response: Response, nodes: Iterable[Selector]) -> Any
```

**内部调用(库内):**
- [`XMLFeedSpider.parse_node`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-56)
- [`XMLFeedSpider.process_results`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-37)

*来源: `scrapy/spiders/feed.py:62` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-74"></a>

### `XMLFeedSpider._parse` · method
```python
def _parse(self, response: Response, **kwargs: Any) -> Any
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`XMLFeedSpider.adapt_response`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-49)
- [`XMLFeedSpider._iternodes`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-101)
- [`Selector`](scrapy_selector.md#sym-scrapy_selector_unified.py-39)
- [`XMLFeedSpider._register_namespaces`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-106)
- [`NotSupported`](scrapy.md#sym-scrapy_exceptions.py-101) — `NotSupported` 类代表一个异常，用于表示某些功能或操作不被支持。
- [`XMLFeedSpider.parse_nodes`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-62)

*来源: `scrapy/spiders/feed.py:74` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-101"></a>

### `XMLFeedSpider._iternodes` · method
```python
def _iternodes(self, response: Response) -> Iterable[Selector]
```

**内部调用(库内):**
- [`xmliter_lxml`](scrapy_utils.md#sym-scrapy_utils_iterators.py-81)
- [`XMLFeedSpider._register_namespaces`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-106)

*来源: `scrapy/spiders/feed.py:101` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-106"></a>

### `XMLFeedSpider._register_namespaces` · method
```python
def _register_namespaces(self, selector: Selector) -> None
```

*来源: `scrapy/spiders/feed.py:106` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-111"></a>

### `CSVFeedSpider` · class
```python
class CSVFeedSpider(Spider)
```

*来源: `scrapy/spiders/feed.py:111` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-128"></a>

### `CSVFeedSpider.process_results` · method
```python
def process_results(
        self, response: Response, results: Iterable[Any]
    ) -> Iterable[Any]
```

*来源: `scrapy/spiders/feed.py:128` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-134"></a>

### `CSVFeedSpider.adapt_response` · method
```python
def adapt_response(self, response: Response) -> Response
```

*来源: `scrapy/spiders/feed.py:134` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-138"></a>

### `CSVFeedSpider.parse_row` · method
```python
def parse_row(self, response: Response, row: dict[str, str]) -> Any
```

*来源: `scrapy/spiders/feed.py:138` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-142"></a>

### `CSVFeedSpider.parse_rows` · method
```python
def parse_rows(self, response: Response) -> Any
```

**内部调用(库内):**
- [`csviter`](scrapy_utils.md#sym-scrapy_utils_iterators.py-158)
- [`CSVFeedSpider.parse_row`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-138)
- [`CSVFeedSpider.process_results`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-128)

*来源: `scrapy/spiders/feed.py:142` · 待生成*

---
<a id="sym-scrapy_spiders_feed.py-155"></a>

### `CSVFeedSpider._parse` · method
```python
def _parse(self, response: Response, **kwargs: Any) -> Any
```

**内部调用(库内):**
- [`NotConfigured`](scrapy.md#sym-scrapy_exceptions.py-18) — `NotConfigured` 异常类用于表示某个组件或配置未正确设置，通常在 Scrapy 框架尝试使用未配置的组件时抛出。
- [`CSVFeedSpider.adapt_response`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-134)
- [`CSVFeedSpider.parse_rows`](scrapy_spiders.md#sym-scrapy_spiders_feed.py-142)

*来源: `scrapy/spiders/feed.py:155` · 待生成*

---

## `scrapy/spiders/sitemap.py`

<a id="sym-scrapy_spiders_sitemap.py-26"></a>

### `SitemapSpider` · class
```python
class SitemapSpider(Spider)
```

*来源: `scrapy/spiders/sitemap.py:26` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-37"></a>

### `SitemapSpider.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/spiders/sitemap.py:37` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-47"></a>

### `SitemapSpider.__init__` · method
```python
def __init__(self, *a: Any, **kw: Any)
```

**内部调用(库内):**
- [`regex`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-153)

*来源: `scrapy/spiders/sitemap.py:47` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-56"></a>

### `SitemapSpider.start` · method
```python
async def start(self) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/spiders/sitemap.py:56` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-60"></a>

### `SitemapSpider.sitemap_filter` · method
```python
def sitemap_filter(
        self, entries: Iterable[dict[str, Any]]
    ) -> Iterable[dict[str, Any]]
```

*来源: `scrapy/spiders/sitemap.py:60` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-69"></a>

### `SitemapSpider._parse_sitemap` · method
```python
def _parse_sitemap(self, response: Response) -> Iterable[Request]
```

**内部调用(库内):**
- [`sitemap_urls_from_robots`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-106)
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)
- [`SitemapSpider._get_sitemap_body`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-119)
- [`Sitemap`](scrapy_utils.md#sym-scrapy_utils_sitemap.py-23)
- [`SitemapSpider._get_urls_from_sitemapindex`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-103)
- [`SitemapSpider.sitemap_filter`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-60)
- [`SitemapSpider._get_urls_and_callbacks_from_urlset`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-110)

*来源: `scrapy/spiders/sitemap.py:69` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-103"></a>

### `SitemapSpider._get_urls_from_sitemapindex` · method
```python
def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]
```

**内部调用(库内):**
- [`iterloc`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-159)

*来源: `scrapy/spiders/sitemap.py:103` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-110"></a>

### `SitemapSpider._get_urls_and_callbacks_from_urlset` · method
```python
def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]
```

**内部调用(库内):**
- [`iterloc`](scrapy_spiders.md#sym-scrapy_spiders_sitemap.py-159)

*来源: `scrapy/spiders/sitemap.py:110` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-119"></a>

### `SitemapSpider._get_sitemap_body` · method
```python
def _get_sitemap_body(self, response: Response) -> bytes | None
```

**内部调用(库内):**
- [`gzip_magic_number`](scrapy_utils.md#sym-scrapy_utils_gz.py-39)
- [`gunzip`](scrapy_utils.md#sym-scrapy_utils_gz.py-14)

*来源: `scrapy/spiders/sitemap.py:119` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-153"></a>

### `regex` · func
```python
def regex(x: re.Pattern[str] | str) -> re.Pattern[str]
```

*来源: `scrapy/spiders/sitemap.py:153` · 待生成*

---
<a id="sym-scrapy_spiders_sitemap.py-159"></a>

### `iterloc` · func
```python
def iterloc(it: Iterable[dict[str, Any]], alt: bool = False) -> Iterable[str]
```

*来源: `scrapy/spiders/sitemap.py:159` · 待生成*

---