# API 参考:`scrapy/downloadermiddlewares`

## `scrapy/downloadermiddlewares/cookies.py`

<a id="sym-scrapy_downloadermiddlewares_cookies.py-35"></a>

### `_is_public_domain` · func
```python
def _is_public_domain(domain: str) -> bool
```

*来源: `scrapy/downloadermiddlewares/cookies.py:35` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-40"></a>

### `CookiesMiddleware` · class
```python
class CookiesMiddleware
```

*来源: `scrapy/downloadermiddlewares/cookies.py:40` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-45"></a>

### `CookiesMiddleware.__init__` · method
```python
def __init__(self, debug: bool = False)
```

*来源: `scrapy/downloadermiddlewares/cookies.py:45` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-50"></a>

### `CookiesMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/cookies.py:50` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-57"></a>

### `CookiesMiddleware._process_cookies` · method
```python
def _process_cookies(
        self, cookies: Iterable[Cookie], *, jar: CookieJar, request: Request
    ) -> None
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`_is_public_domain`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-35)
- [`CookieJar.set_cookie_if_ok`](scrapy_http.md#sym-scrapy_http_cookies.py-107)

*来源: `scrapy/downloadermiddlewares/cookies.py:57` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-76"></a>

### `CookiesMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`CookiesMiddleware._get_request_cookies`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-172)
- [`CookiesMiddleware._process_cookies`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-57)
- [`CookieJar.add_cookie_header`](scrapy_http.md#sym-scrapy_http_cookies.py-44)
- [`CookiesMiddleware._debug_cookie`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-110)

*来源: `scrapy/downloadermiddlewares/cookies.py:76` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-94"></a>

### `CookiesMiddleware.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response
```

**内部调用(库内):**
- [`CookieJar.make_cookies`](scrapy_http.md#sym-scrapy_http_cookies.py-99)
- [`CookiesMiddleware._process_cookies`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-57)
- [`CookiesMiddleware._debug_set_cookie`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-121)

*来源: `scrapy/downloadermiddlewares/cookies.py:94` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-110"></a>

### `CookiesMiddleware._debug_cookie` · method
```python
def _debug_cookie(self, request: Request) -> None
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/downloadermiddlewares/cookies.py:110` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-121"></a>

### `CookiesMiddleware._debug_set_cookie` · method
```python
def _debug_set_cookie(self, response: Response) -> None
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/downloadermiddlewares/cookies.py:121` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-132"></a>

### `CookiesMiddleware._format_cookie` · method
```python
def _format_cookie(self, cookie: VerboseCookie, request: Request) -> str | None
```

*来源: `scrapy/downloadermiddlewares/cookies.py:132` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_cookies.py-172"></a>

### `CookiesMiddleware._get_request_cookies` · method
```python
def _get_request_cookies(
        self, jar: CookieJar, request: Request
    ) -> Sequence[Cookie]
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`CookiesMiddleware._format_cookie`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_cookies.py-132)
- [`Response`](scrapy_http.md#sym-scrapy_http_response___init__.py-35)
- [`CookieJar.make_cookies`](scrapy_http.md#sym-scrapy_http_cookies.py-99)

*来源: `scrapy/downloadermiddlewares/cookies.py:172` · 待生成*

---

## `scrapy/downloadermiddlewares/defaultheaders.py`

<a id="sym-scrapy_downloadermiddlewares_defaultheaders.py-25"></a>

### `DefaultHeadersMiddleware` · class
```python
class DefaultHeadersMiddleware
```

*来源: `scrapy/downloadermiddlewares/defaultheaders.py:25` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_defaultheaders.py-26"></a>

### `DefaultHeadersMiddleware.__init__` · method
```python
def __init__(self, headers: Iterable[tuple[str, str]])
```

*来源: `scrapy/downloadermiddlewares/defaultheaders.py:26` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_defaultheaders.py-30"></a>

### `DefaultHeadersMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/defaultheaders.py:30` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_defaultheaders.py-35"></a>

### `DefaultHeadersMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

*来源: `scrapy/downloadermiddlewares/defaultheaders.py:35` · 待生成*

---

## `scrapy/downloadermiddlewares/downloadtimeout.py`

<a id="sym-scrapy_downloadermiddlewares_downloadtimeout.py-23"></a>

### `DownloadTimeoutMiddleware` · class
```python
class DownloadTimeoutMiddleware
```

*来源: `scrapy/downloadermiddlewares/downloadtimeout.py:23` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_downloadtimeout.py-24"></a>

### `DownloadTimeoutMiddleware.__init__` · method
```python
def __init__(self, timeout: float = 180)
```

*来源: `scrapy/downloadermiddlewares/downloadtimeout.py:24` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_downloadtimeout.py-28"></a>

### `DownloadTimeoutMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getfloat`](scrapy_settings.md#sym-scrapy_settings___init__.py-213)

*来源: `scrapy/downloadermiddlewares/downloadtimeout.py:28` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_downloadtimeout.py-33"></a>

### `DownloadTimeoutMiddleware.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`warn_on_deprecated_spider_attribute`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-225)

*来源: `scrapy/downloadermiddlewares/downloadtimeout.py:33` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_downloadtimeout.py-39"></a>

### `DownloadTimeoutMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

*来源: `scrapy/downloadermiddlewares/downloadtimeout.py:39` · 待生成*

---

## `scrapy/downloadermiddlewares/httpauth.py`

<a id="sym-scrapy_downloadermiddlewares_httpauth.py-28"></a>

### `HttpAuthMiddleware` · class
```python
class HttpAuthMiddleware
```

*来源: `scrapy/downloadermiddlewares/httpauth.py:28` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpauth.py-31"></a>

### `HttpAuthMiddleware.__init__` · method
```python
def __init__(self) -> None
```

*来源: `scrapy/downloadermiddlewares/httpauth.py:31` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpauth.py-36"></a>

### `HttpAuthMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/downloadermiddlewares/httpauth.py:36` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpauth.py-54"></a>

### `HttpAuthMiddleware.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

*来源: `scrapy/downloadermiddlewares/httpauth.py:54` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpauth.py-70"></a>

### `HttpAuthMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`url_is_from_any_domain`](scrapy_utils.md#sym-scrapy_utils_url.py-22)

*来源: `scrapy/downloadermiddlewares/httpauth.py:70` · 待生成*

---

## `scrapy/downloadermiddlewares/httpcache.py`

<a id="sym-scrapy_downloadermiddlewares_httpcache.py-31"></a>

### `HttpCacheMiddleware` · class
```python
class HttpCacheMiddleware
```

*来源: `scrapy/downloadermiddlewares/httpcache.py:31` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-44"></a>

### `HttpCacheMiddleware.__init__` · method
```python
def __init__(self, settings: Settings, stats: StatsCollector) -> None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/downloadermiddlewares/httpcache.py:44` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-53"></a>

### `HttpCacheMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/httpcache.py:53` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-61"></a>

### `HttpCacheMiddleware.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

*来源: `scrapy/downloadermiddlewares/httpcache.py:61` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-64"></a>

### `HttpCacheMiddleware.spider_closed` · method
```python
def spider_closed(self, spider: Spider) -> None
```

*来源: `scrapy/downloadermiddlewares/httpcache.py:64` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-68"></a>

### `HttpCacheMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`IgnoreRequest`](scrapy.md#sym-scrapy_exceptions.py-32) — `IgnoreRequest` 异常类用于指示爬虫应忽略某个请求，通常在请求中间件中抛出以阻止请求继续处理。

*来源: `scrapy/downloadermiddlewares/httpcache.py:68` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-103"></a>

### `HttpCacheMiddleware.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response
```

**内部调用(库内):**
- [`HttpCacheMiddleware._cache_response`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpcache.py-146)

*来源: `scrapy/downloadermiddlewares/httpcache.py:103` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-135"></a>

### `HttpCacheMiddleware.process_exception` · method
装饰器: `@_warn_spider_arg`
```python
def process_exception(
        self, request: Request, exception: Exception, spider: Spider | None = None
    ) -> Request | Response | None
```

*来源: `scrapy/downloadermiddlewares/httpcache.py:135` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcache.py-146"></a>

### `HttpCacheMiddleware._cache_response` · method
```python
def _cache_response(self, response: Response, request: Request) -> None
```

*来源: `scrapy/downloadermiddlewares/httpcache.py:146` · 待生成*

---

## `scrapy/downloadermiddlewares/httpcompression.py`

<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-62"></a>

### `HttpCompressionMiddleware` · class
```python
class HttpCompressionMiddleware
```

*来源: `scrapy/downloadermiddlewares/httpcompression.py:62` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-66"></a>

### `HttpCompressionMiddleware.__init__` · method
```python
def __init__(
        self,
        stats: StatsCollector | None = None,
        *,
        crawler: Crawler | None = None,
    )
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/downloadermiddlewares/httpcompression.py:66` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-83"></a>

### `HttpCompressionMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/httpcompression.py:83` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-88"></a>

### `HttpCompressionMiddleware.open_spider` · method
```python
def open_spider(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`warn_on_deprecated_spider_attribute`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-225)

*来源: `scrapy/downloadermiddlewares/httpcompression.py:88` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-99"></a>

### `HttpCompressionMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

*来源: `scrapy/downloadermiddlewares/httpcompression.py:99` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-106"></a>

### `HttpCompressionMiddleware.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response
```

**内部调用(库内):**
- [`HttpCompressionMiddleware._handle_encoding`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpcompression.py-156)
- [`IgnoreRequest`](scrapy.md#sym-scrapy_exceptions.py-32) — `IgnoreRequest` 异常类用于指示爬虫应忽略某个请求，通常在请求中间件中抛出以阻止请求继续处理。
- [`HttpCompressionMiddleware._warn_unknown_encoding`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpcompression.py-197)
- [`ResponseTypes.from_args`](scrapy.md#sym-scrapy_responsetypes.py-124)

*来源: `scrapy/downloadermiddlewares/httpcompression.py:106` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-156"></a>

### `HttpCompressionMiddleware._handle_encoding` · method
```python
def _handle_encoding(
        self, body: bytes, content_encoding: list[bytes], max_size: int
    ) -> tuple[bytes, list[bytes]]
```

**内部调用(库内):**
- [`HttpCompressionMiddleware._split_encodings`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpcompression.py-165)
- [`HttpCompressionMiddleware._decode`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpcompression.py-185)

*来源: `scrapy/downloadermiddlewares/httpcompression.py:156` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-165"></a>

### `HttpCompressionMiddleware._split_encodings` · method
装饰器: `@staticmethod`
```python
def _split_encodings(
        content_encoding: list[bytes],
    ) -> tuple[list[bytes], list[bytes]]
```

*来源: `scrapy/downloadermiddlewares/httpcompression.py:165` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-185"></a>

### `HttpCompressionMiddleware._decode` · method
装饰器: `@staticmethod`
```python
def _decode(body: bytes, encoding: bytes, max_size: int) -> bytes
```

**内部调用(库内):**
- [`gunzip`](scrapy_utils.md#sym-scrapy_utils_gz.py-14)
- [`_inflate`](scrapy_utils.md#sym-scrapy_utils__compression.py-36)
- [`_unbrotli`](scrapy_utils.md#sym-scrapy_utils__compression.py-62)
- [`_unzstd`](scrapy_utils.md#sym-scrapy_utils__compression.py-79)

*来源: `scrapy/downloadermiddlewares/httpcompression.py:185` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpcompression.py-197"></a>

### `HttpCompressionMiddleware._warn_unknown_encoding` · method
```python
def _warn_unknown_encoding(
        self, response: Response, encodings: list[bytes]
    ) -> None
```

*来源: `scrapy/downloadermiddlewares/httpcompression.py:197` · 待生成*

---

## `scrapy/downloadermiddlewares/httpproxy.py`

<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-26"></a>

### `HttpProxyMiddleware` · class
```python
class HttpProxyMiddleware
```

*来源: `scrapy/downloadermiddlewares/httpproxy.py:26` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-27"></a>

### `HttpProxyMiddleware.__init__` · method
```python
def __init__(self, auth_encoding: str | None = "latin-1")
```

**内部调用(库内):**
- [`HttpProxyMiddleware._get_proxy`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpproxy.py-51)

*来源: `scrapy/downloadermiddlewares/httpproxy.py:27` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-39"></a>

### `HttpProxyMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/httpproxy.py:39` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-45"></a>

### `HttpProxyMiddleware._basic_auth_header` · method
```python
def _basic_auth_header(self, username: str, password: str) -> bytes
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/downloadermiddlewares/httpproxy.py:45` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-51"></a>

### `HttpProxyMiddleware._get_proxy` · method
```python
def _get_proxy(self, url: str, orig_type: str) -> tuple[bytes | None, str]
```

**内部调用(库内):**
- [`HttpProxyMiddleware._basic_auth_header`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpproxy.py-45)

*来源: `scrapy/downloadermiddlewares/httpproxy.py:51` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-60"></a>

### `HttpProxyMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`HttpProxyMiddleware._get_proxy`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpproxy.py-51)
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`HttpProxyMiddleware._set_proxy_and_creds`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_httpproxy.py-81)

*来源: `scrapy/downloadermiddlewares/httpproxy.py:60` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_httpproxy.py-81"></a>

### `HttpProxyMiddleware._set_proxy_and_creds` · method
```python
def _set_proxy_and_creds(
        self,
        request: Request,
        proxy_url: str | None,
        creds: bytes | None,
        scheme: str | None,
    ) -> None
```

*来源: `scrapy/downloadermiddlewares/httpproxy.py:81` · 待生成*

---

## `scrapy/downloadermiddlewares/offsite.py`

<a id="sym-scrapy_downloadermiddlewares_offsite.py-24"></a>

### `OffsiteMiddleware` · class
```python
class OffsiteMiddleware
```

*来源: `scrapy/downloadermiddlewares/offsite.py:24` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-27"></a>

### `OffsiteMiddleware.__init__` · method
```python
def __init__(self, stats: StatsCollector)
```

*来源: `scrapy/downloadermiddlewares/offsite.py:27` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-32"></a>

### `OffsiteMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/offsite.py:32` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-40"></a>

### `OffsiteMiddleware.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`OffsiteMiddleware.get_host_regex`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_offsite.py-73)

*来源: `scrapy/downloadermiddlewares/offsite.py:40` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-43"></a>

### `OffsiteMiddleware.request_scheduled` · method
```python
def request_scheduled(self, request: Request, spider: Spider) -> None
```

**内部调用(库内):**
- [`OffsiteMiddleware.process_request`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_offsite.py-47)

*来源: `scrapy/downloadermiddlewares/offsite.py:43` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-47"></a>

### `OffsiteMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(self, request: Request, spider: Spider | None = None) -> None
```

**内部调用(库内):**
- [`OffsiteMiddleware.should_follow`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_offsite.py-67)
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/downloadermiddlewares/offsite.py:47` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-67"></a>

### `OffsiteMiddleware.should_follow` · method
```python
def should_follow(self, request: Request, spider: Spider) -> bool
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/downloadermiddlewares/offsite.py:67` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_offsite.py-73"></a>

### `OffsiteMiddleware.get_host_regex` · method
```python
def get_host_regex(self, spider: Spider) -> re.Pattern[str]
```

*来源: `scrapy/downloadermiddlewares/offsite.py:73` · 待生成*

---

## `scrapy/downloadermiddlewares/redirect.py`

<a id="sym-scrapy_downloadermiddlewares_redirect.py-30"></a>

### `BaseRedirectMiddleware` · class
```python
class BaseRedirectMiddleware
```

*来源: `scrapy/downloadermiddlewares/redirect.py:30` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-34"></a>

### `BaseRedirectMiddleware.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/downloadermiddlewares/redirect.py:34` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-43"></a>

### `BaseRedirectMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/redirect.py:43` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-49"></a>

### `BaseRedirectMiddleware.handle_referer` · method
```python
def handle_referer(self, request: Request, response: Response) -> None
```

*来源: `scrapy/downloadermiddlewares/redirect.py:49` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-66"></a>

### `BaseRedirectMiddleware._engine_started` · method
```python
def _engine_started(self) -> None
```

**内部调用(库内):**
- [`Crawler.get_spider_middleware`](scrapy.md#sym-scrapy_crawler.py-326) — 返回指定类或其子类的爬虫中间件实例，若未找到则返回 None。
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/downloadermiddlewares/redirect.py:66` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-93"></a>

### `BaseRedirectMiddleware._redirect` · method
```python
def _redirect(self, redirected: Request, request: Request, reason: Any) -> Request
```

**内部调用(库内):**
- [`IgnoreRequest`](scrapy.md#sym-scrapy_exceptions.py-32) — `IgnoreRequest` 异常类用于指示爬虫应忽略某个请求，通常在请求中间件中抛出以阻止请求继续处理。

*来源: `scrapy/downloadermiddlewares/redirect.py:93` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-123"></a>

### `BaseRedirectMiddleware._build_redirect_request` · method
```python
def _build_redirect_request(
        self, source_request: Request, response: Response, *, url: str, **kwargs: Any
    ) -> Request
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`BaseRedirectMiddleware.handle_referer`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-49)

*来源: `scrapy/downloadermiddlewares/redirect.py:123` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-180"></a>

### `BaseRedirectMiddleware._redirect_request_using_get` · method
```python
def _redirect_request_using_get(
        self, request: Request, response: Response, redirect_url: str
    ) -> Request
```

**内部调用(库内):**
- [`BaseRedirectMiddleware._build_redirect_request`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-123)

*来源: `scrapy/downloadermiddlewares/redirect.py:180` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-198"></a>

### `RedirectMiddleware` · class
```python
class RedirectMiddleware(BaseRedirectMiddleware)
```

*来源: `scrapy/downloadermiddlewares/redirect.py:198` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-205"></a>

### `RedirectMiddleware.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`BaseRedirectMiddleware._build_redirect_request`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-123)
- [`BaseRedirectMiddleware._redirect_request_using_get`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-180)
- [`BaseRedirectMiddleware._redirect`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-93)

*来源: `scrapy/downloadermiddlewares/redirect.py:205` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-253"></a>

### `MetaRefreshMiddleware` · class
```python
class MetaRefreshMiddleware(BaseRedirectMiddleware)
```

*来源: `scrapy/downloadermiddlewares/redirect.py:253` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-256"></a>

### `MetaRefreshMiddleware.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/downloadermiddlewares/redirect.py:256` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_redirect.py-262"></a>

### `MetaRefreshMiddleware.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`get_meta_refresh`](scrapy_utils.md#sym-scrapy_utils_response.py-43)
- [`BaseRedirectMiddleware._redirect_request_using_get`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-180)
- [`BaseRedirectMiddleware._redirect`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_redirect.py-93)

*来源: `scrapy/downloadermiddlewares/redirect.py:262` · 待生成*

---

## `scrapy/downloadermiddlewares/retry.py`

<a id="sym-scrapy_downloadermiddlewares_retry.py-38"></a>

### `get_retry_request` · func
```python
def get_retry_request(
    request: Request,
    *,
    spider: scrapy.Spider,
    reason: str | Exception | type[Exception] = "unspecified",
    max_retry_times: int | None = None,
    priority_adjust: int | None = None,
    logger: Logger = retry_logger,
    give_up_log_level: int | str | None = None,
    stats_base_key: str = "retry",
) -> Request | None
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/downloadermiddlewares/retry.py:38` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_retry.py-141"></a>

### `RetryMiddleware` · class
```python
class RetryMiddleware
```

*来源: `scrapy/downloadermiddlewares/retry.py:141` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_retry.py-144"></a>

### `RetryMiddleware.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)

*来源: `scrapy/downloadermiddlewares/retry.py:144` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_retry.py-157"></a>

### `RetryMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/retry.py:157` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_retry.py-163"></a>

### `RetryMiddleware.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self,
        request: Request,
        response: Response,
        spider: scrapy.Spider | None = None,
    ) -> Request | Response
```

**内部调用(库内):**
- [`response_status_message`](scrapy_utils.md#sym-scrapy_utils_response.py-56)
- [`RetryMiddleware._retry`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_retry.py-189)

*来源: `scrapy/downloadermiddlewares/retry.py:163` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_retry.py-177"></a>

### `RetryMiddleware.process_exception` · method
装饰器: `@_warn_spider_arg`
```python
def process_exception(
        self,
        request: Request,
        exception: Exception,
        spider: scrapy.Spider | None = None,
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`RetryMiddleware._retry`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_retry.py-189)

*来源: `scrapy/downloadermiddlewares/retry.py:177` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_retry.py-189"></a>

### `RetryMiddleware._retry` · method
```python
def _retry(
        self, request: Request, reason: str | Exception | type[Exception]
    ) -> Request | None
```

**内部调用(库内):**
- [`get_retry_request`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_retry.py-38)

*来源: `scrapy/downloadermiddlewares/retry.py:189` · 待生成*

---

## `scrapy/downloadermiddlewares/robotstxt.py`

<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-34"></a>

### `RobotsTxtMiddleware` · class
```python
class RobotsTxtMiddleware
```

*来源: `scrapy/downloadermiddlewares/robotstxt.py:34` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-37"></a>

### `RobotsTxtMiddleware.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`RobotsTxtMiddleware.from_crawler`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_robotstxt.py-52)

*来源: `scrapy/downloadermiddlewares/robotstxt.py:37` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-52"></a>

### `RobotsTxtMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/robotstxt.py:52` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-56"></a>

### `RobotsTxtMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
async def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> None
```

**内部调用(库内):**
- [`RobotsTxtMiddleware.robot_parser`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_robotstxt.py-84)
- [`RobotsTxtMiddleware.process_request_2`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_robotstxt.py-66)

*来源: `scrapy/downloadermiddlewares/robotstxt.py:56` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-66"></a>

### `RobotsTxtMiddleware.process_request_2` · method
```python
def process_request_2(self, rp: RobotParser | None, request: Request) -> None
```

**内部调用(库内):**
- [`IgnoreRequest`](scrapy.md#sym-scrapy_exceptions.py-32) — `IgnoreRequest` 异常类用于指示爬虫应忽略某个请求，通常在请求中间件中抛出以阻止请求继续处理。

*来源: `scrapy/downloadermiddlewares/robotstxt.py:66` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-84"></a>

### `RobotsTxtMiddleware.robot_parser` · method
```python
async def robot_parser(self, request: Request) -> RobotParser | None
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)
- [`RobotsTxtMiddleware._parse_robots`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_robotstxt.py-118)
- [`CurlParser.error`](scrapy_utils.md#sym-scrapy_utils_curl.py-30)
- [`RobotsTxtMiddleware._robots_error`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_robotstxt.py-130)
- [`maybe_deferred_to_future`](scrapy_utils.md#sym-scrapy_utils_defer.py-499)

*来源: `scrapy/downloadermiddlewares/robotstxt.py:84` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-118"></a>

### `RobotsTxtMiddleware._parse_robots` · method
```python
def _parse_robots(self, response: Response, netloc: str) -> None
```

**内部调用(库内):**
- [`RobotsTxtMiddleware.from_crawler`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_robotstxt.py-52)
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/downloadermiddlewares/robotstxt.py:118` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_robotstxt.py-130"></a>

### `RobotsTxtMiddleware._robots_error` · method
```python
def _robots_error(self, exc: Exception, netloc: str) -> None
```

**内部调用(库内):**
- [`Command.callback`](scrapy_commands.md#sym-scrapy_commands_parse.py-343)

*来源: `scrapy/downloadermiddlewares/robotstxt.py:130` · 待生成*

---

## `scrapy/downloadermiddlewares/stats.py`

<a id="sym-scrapy_downloadermiddlewares_stats.py-22"></a>

### `get_header_size` · func
```python
def get_header_size(
    headers: dict[str, list[str | bytes] | tuple[str | bytes, ...]],
) -> int
```

*来源: `scrapy/downloadermiddlewares/stats.py:22` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-33"></a>

### `get_status_size` · func
```python
def get_status_size(response_status: int) -> int
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/downloadermiddlewares/stats.py:33` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-38"></a>

### `DownloaderStats` · class
```python
class DownloaderStats
```

*来源: `scrapy/downloadermiddlewares/stats.py:38` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-39"></a>

### `DownloaderStats.__init__` · method
```python
def __init__(self, stats: StatsCollector)
```

*来源: `scrapy/downloadermiddlewares/stats.py:39` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-43"></a>

### `DownloaderStats.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/stats.py:43` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-50"></a>

### `DownloaderStats.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`request_httprepr`](scrapy_utils.md#sym-scrapy_utils_request.py-133)

*来源: `scrapy/downloadermiddlewares/stats.py:50` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-60"></a>

### `DownloaderStats.process_response` · method
装饰器: `@_warn_spider_arg`
```python
def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response
```

**内部调用(库内):**
- [`get_header_size`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_stats.py-22)
- [`get_status_size`](scrapy_downloadermiddlewares.md#sym-scrapy_downloadermiddlewares_stats.py-33)

*来源: `scrapy/downloadermiddlewares/stats.py:60` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_stats.py-76"></a>

### `DownloaderStats.process_exception` · method
装饰器: `@_warn_spider_arg`
```python
def process_exception(
        self, request: Request, exception: Exception, spider: Spider | None = None
    ) -> Request | Response | None
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/downloadermiddlewares/stats.py:76` · 待生成*

---

## `scrapy/downloadermiddlewares/useragent.py`

<a id="sym-scrapy_downloadermiddlewares_useragent.py-19"></a>

### `UserAgentMiddleware` · class
```python
class UserAgentMiddleware
```

*来源: `scrapy/downloadermiddlewares/useragent.py:19` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_useragent.py-22"></a>

### `UserAgentMiddleware.__init__` · method
```python
def __init__(self, user_agent: str = "Scrapy")
```

*来源: `scrapy/downloadermiddlewares/useragent.py:22` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_useragent.py-26"></a>

### `UserAgentMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/downloadermiddlewares/useragent.py:26` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_useragent.py-31"></a>

### `UserAgentMiddleware.spider_opened` · method
```python
def spider_opened(self, spider: Spider) -> None
```

**内部调用(库内):**
- [`warn_on_deprecated_spider_attribute`](scrapy_utils.md#sym-scrapy_utils_deprecate.py-225)

*来源: `scrapy/downloadermiddlewares/useragent.py:31` · 待生成*

---
<a id="sym-scrapy_downloadermiddlewares_useragent.py-38"></a>

### `UserAgentMiddleware.process_request` · method
装饰器: `@_warn_spider_arg`
```python
def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None
```

*来源: `scrapy/downloadermiddlewares/useragent.py:38` · 待生成*

---