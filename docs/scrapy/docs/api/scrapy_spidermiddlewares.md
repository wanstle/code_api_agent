# API 参考:`scrapy/spidermiddlewares`

## `scrapy/spidermiddlewares/base.py`

<a id="sym-scrapy_spidermiddlewares_base.py-18"></a>

### `BaseSpiderMiddleware` · class
```python
class BaseSpiderMiddleware
```

*来源: `scrapy/spidermiddlewares/base.py:18` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-37"></a>

### `BaseSpiderMiddleware.__init__` · method
```python
def __init__(self, crawler: Crawler)
```

*来源: `scrapy/spidermiddlewares/base.py:37` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-41"></a>

### `BaseSpiderMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/spidermiddlewares/base.py:41` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-44"></a>

### `BaseSpiderMiddleware.process_start` · method
```python
async def process_start(self, start: AsyncIterator[Any]) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`BaseSpiderMiddleware._get_processed`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_base.py-68)

*来源: `scrapy/spidermiddlewares/base.py:44` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-50"></a>

### `BaseSpiderMiddleware.process_spider_output` · method
装饰器: `@_warn_spider_arg`
```python
def process_spider_output(
        self, response: Response, result: Iterable[Any], spider: Spider | None = None
    ) -> Iterable[Any]
```

**内部调用(库内):**
- [`BaseSpiderMiddleware._get_processed`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_base.py-68)

*来源: `scrapy/spidermiddlewares/base.py:50` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-58"></a>

### `BaseSpiderMiddleware.process_spider_output_async` · method
装饰器: `@_warn_spider_arg`
```python
async def process_spider_output_async(
        self,
        response: Response,
        result: AsyncIterator[Any],
        spider: Spider | None = None,
    ) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`BaseSpiderMiddleware._get_processed`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_base.py-68)

*来源: `scrapy/spidermiddlewares/base.py:58` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-68"></a>

### `BaseSpiderMiddleware._get_processed` · method
```python
def _get_processed(self, o: Any, response: Response | None) -> Any
```

**内部调用(库内):**
- [`BaseSpiderMiddleware.get_processed_request`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_base.py-73)
- [`BaseSpiderMiddleware.get_processed_item`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_base.py-93)

*来源: `scrapy/spidermiddlewares/base.py:68` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-73"></a>

### `BaseSpiderMiddleware.get_processed_request` · method
```python
def get_processed_request(
        self, request: Request, response: Response | None
    ) -> Request | None
```

*来源: `scrapy/spidermiddlewares/base.py:73` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_base.py-93"></a>

### `BaseSpiderMiddleware.get_processed_item` · method
```python
def get_processed_item(self, item: Any, response: Response | None) -> Any
```

*来源: `scrapy/spidermiddlewares/base.py:93` · 待生成*

---

## `scrapy/spidermiddlewares/depth.py`

<a id="sym-scrapy_spidermiddlewares_depth.py-30"></a>

### `DepthMiddleware` · class
```python
class DepthMiddleware(BaseSpiderMiddleware)
```

*来源: `scrapy/spidermiddlewares/depth.py:30` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_depth.py-33"></a>

### `DepthMiddleware.__init__` · method
```python
def __init__(  # pylint: disable=super-init-not-called
        self,
        maxdepth: int,
        stats: StatsCollector,
        verbose_stats: bool = False,
        prio: int = 1,
    )
```

*来源: `scrapy/spidermiddlewares/depth.py:33` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_depth.py-46"></a>

### `DepthMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/spidermiddlewares/depth.py:46` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_depth.py-57"></a>

### `DepthMiddleware.process_spider_output` · method
装饰器: `@_warn_spider_arg`
```python
def process_spider_output(
        self, response: Response, result: Iterable[Any], spider: Spider | None = None
    ) -> Iterable[Any]
```

**内部调用(库内):**
- [`DepthMiddleware._init_depth`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_depth.py-74)

*来源: `scrapy/spidermiddlewares/depth.py:57` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_depth.py-64"></a>

### `DepthMiddleware.process_spider_output_async` · method
装饰器: `@_warn_spider_arg`
```python
async def process_spider_output_async(
        self,
        response: Response,
        result: AsyncIterator[Any],
        spider: Spider | None = None,
    ) -> AsyncIterator[Any]
```

**内部调用(库内):**
- [`DepthMiddleware._init_depth`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_depth.py-74)

*来源: `scrapy/spidermiddlewares/depth.py:64` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_depth.py-74"></a>

### `DepthMiddleware._init_depth` · method
```python
def _init_depth(self, response: Response) -> None
```

*来源: `scrapy/spidermiddlewares/depth.py:74` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_depth.py-81"></a>

### `DepthMiddleware.get_processed_request` · method
```python
def get_processed_request(
        self, request: Request, response: Response | None
    ) -> Request | None
```

*来源: `scrapy/spidermiddlewares/depth.py:81` · 待生成*

---

## `scrapy/spidermiddlewares/httperror.py`

<a id="sym-scrapy_spidermiddlewares_httperror.py-30"></a>

### `HttpError` · class
```python
class HttpError(IgnoreRequest)
```

*来源: `scrapy/spidermiddlewares/httperror.py:30` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_httperror.py-33"></a>

### `HttpError.__init__` · method
```python
def __init__(self, response: Response, *args: Any, **kwargs: Any)
```

*来源: `scrapy/spidermiddlewares/httperror.py:33` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_httperror.py-38"></a>

### `HttpErrorMiddleware` · class
```python
class HttpErrorMiddleware
```

*来源: `scrapy/spidermiddlewares/httperror.py:38` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_httperror.py-41"></a>

### `HttpErrorMiddleware.__init__` · method
```python
def __init__(self, settings: BaseSettings)
```

*来源: `scrapy/spidermiddlewares/httperror.py:41` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_httperror.py-48"></a>

### `HttpErrorMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/spidermiddlewares/httperror.py:48` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_httperror.py-54"></a>

### `HttpErrorMiddleware.process_spider_input` · method
装饰器: `@_warn_spider_arg`
```python
def process_spider_input(
        self, response: Response, spider: Spider | None = None
    ) -> None
```

**内部调用(库内):**
- [`HttpError`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_httperror.py-30)

*来源: `scrapy/spidermiddlewares/httperror.py:54` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_httperror.py-77"></a>

### `HttpErrorMiddleware.process_spider_exception` · method
装饰器: `@_warn_spider_arg`
```python
def process_spider_exception(
        self, response: Response, exception: Exception, spider: Spider | None = None
    ) -> Iterable[Any] | None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/spidermiddlewares/httperror.py:77` · 待生成*

---

## `scrapy/spidermiddlewares/referer.py`

<a id="sym-scrapy_spidermiddlewares_referer.py-28"></a>

### `_PolicyKwargs` · class
```python
class _PolicyKwargs(TypedDict, total=False)
```

*来源: `scrapy/spidermiddlewares/referer.py:28` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-50"></a>

### `ReferrerPolicy` · class
```python
class ReferrerPolicy(ABC)
```

*来源: `scrapy/spidermiddlewares/referer.py:50` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-57"></a>

### `ReferrerPolicy.referrer` · method
装饰器: `@abstractmethod`
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

*来源: `scrapy/spidermiddlewares/referer.py:57` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-60"></a>

### `ReferrerPolicy.stripped_referrer` · method
```python
def stripped_referrer(self, url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.strip_url`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-70)

*来源: `scrapy/spidermiddlewares/referer.py:60` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-65"></a>

### `ReferrerPolicy.origin_referrer` · method
```python
def origin_referrer(self, url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.origin`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-94)

*来源: `scrapy/spidermiddlewares/referer.py:65` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-70"></a>

### `ReferrerPolicy.strip_url` · method
```python
def strip_url(self, url: str, origin_only: bool = False) -> str | None
```

*来源: `scrapy/spidermiddlewares/referer.py:70` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-94"></a>

### `ReferrerPolicy.origin` · method
```python
def origin(self, url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.strip_url`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-70)

*来源: `scrapy/spidermiddlewares/referer.py:94` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-98"></a>

### `ReferrerPolicy.potentially_trustworthy` · method
```python
def potentially_trustworthy(self, url: str) -> bool
```

**内部调用(库内):**
- [`ReferrerPolicy.tls_protected`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-105)

*来源: `scrapy/spidermiddlewares/referer.py:98` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-105"></a>

### `ReferrerPolicy.tls_protected` · method
```python
def tls_protected(self, url: str) -> bool
```

*来源: `scrapy/spidermiddlewares/referer.py:105` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-109"></a>

### `NoReferrerPolicy` · class
```python
class NoReferrerPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:109` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-120"></a>

### `NoReferrerPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

*来源: `scrapy/spidermiddlewares/referer.py:120` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-124"></a>

### `NoReferrerWhenDowngradePolicy` · class
```python
class NoReferrerWhenDowngradePolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:124` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-141"></a>

### `NoReferrerWhenDowngradePolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.tls_protected`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-105)
- [`ReferrerPolicy.stripped_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-60)

*来源: `scrapy/spidermiddlewares/referer.py:141` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-147"></a>

### `SameOriginPolicy` · class
```python
class SameOriginPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:147` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-160"></a>

### `SameOriginPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.origin`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-94)
- [`ReferrerPolicy.stripped_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-60)

*来源: `scrapy/spidermiddlewares/referer.py:160` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-166"></a>

### `OriginPolicy` · class
```python
class OriginPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:166` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-178"></a>

### `OriginPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.origin_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-65)

*来源: `scrapy/spidermiddlewares/referer.py:178` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-182"></a>

### `StrictOriginPolicy` · class
```python
class StrictOriginPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:182` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-198"></a>

### `StrictOriginPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.tls_protected`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-105)
- [`ReferrerPolicy.potentially_trustworthy`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-98)
- [`ReferrerPolicy.origin_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-65)

*来源: `scrapy/spidermiddlewares/referer.py:198` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-207"></a>

### `OriginWhenCrossOriginPolicy` · class
```python
class OriginWhenCrossOriginPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:207` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-221"></a>

### `OriginWhenCrossOriginPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.origin`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-94)
- [`ReferrerPolicy.stripped_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-60)

*来源: `scrapy/spidermiddlewares/referer.py:221` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-228"></a>

### `StrictOriginWhenCrossOriginPolicy` · class
```python
class StrictOriginWhenCrossOriginPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:228` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-248"></a>

### `StrictOriginWhenCrossOriginPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.origin`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-94)
- [`ReferrerPolicy.stripped_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-60)
- [`ReferrerPolicy.tls_protected`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-105)
- [`ReferrerPolicy.potentially_trustworthy`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-98)
- [`ReferrerPolicy.origin_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-65)

*来源: `scrapy/spidermiddlewares/referer.py:248` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-260"></a>

### `UnsafeUrlPolicy` · class
```python
class UnsafeUrlPolicy(ReferrerPolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:260` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-276"></a>

### `UnsafeUrlPolicy.referrer` · method
```python
def referrer(self, response_url: str, request_url: str) -> str | None
```

**内部调用(库内):**
- [`ReferrerPolicy.stripped_referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-60)

*来源: `scrapy/spidermiddlewares/referer.py:276` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-280"></a>

### `DefaultReferrerPolicy` · class
```python
class DefaultReferrerPolicy(NoReferrerWhenDowngradePolicy)
```

*来源: `scrapy/spidermiddlewares/referer.py:280` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-291"></a>

### `RefererMiddleware` · class
```python
class RefererMiddleware(BaseSpiderMiddleware)
```

*来源: `scrapy/spidermiddlewares/referer.py:291` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-292"></a>

### `RefererMiddleware.__init__` · method
```python
def __init__(self, settings: BaseSettings | None = None)
```

**内部调用(库内):**
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`RefererMiddleware._load_policy_class`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-380)

*来源: `scrapy/spidermiddlewares/referer.py:292` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-325"></a>

### `RefererMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

*来源: `scrapy/spidermiddlewares/referer.py:325` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-330"></a>

### `RefererMiddleware.policy` · method
```python
def policy(
        self,
        response: Response | str | None = None,
        request: Request | None = None,
        **kwargs: Unpack[_PolicyKwargs],
    ) -> ReferrerPolicy
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)
- [`RefererMiddleware._load_policy_class`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-380)

*来源: `scrapy/spidermiddlewares/referer.py:330` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-380"></a>

### `RefererMiddleware._load_policy_class` · method
```python
def _load_policy_class(
        self,
        policy: str,
        warning_only: bool = False,
        *,
        allow_import_path: bool = False,
    ) -> type[ReferrerPolicy] | None
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`_looks_like_import_path`](scrapy_utils.md#sym-scrapy_utils_python.py-344)

*来源: `scrapy/spidermiddlewares/referer.py:380` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_referer.py-430"></a>

### `RefererMiddleware.get_processed_request` · method
```python
def get_processed_request(
        self, request: Request, response: Response | None
    ) -> Request | None
```

**内部调用(库内):**
- [`ReferrerPolicy.referrer`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-57)
- [`RefererMiddleware.policy`](scrapy_spidermiddlewares.md#sym-scrapy_spidermiddlewares_referer.py-330)

*来源: `scrapy/spidermiddlewares/referer.py:430` · 待生成*

---

## `scrapy/spidermiddlewares/start.py`

<a id="sym-scrapy_spidermiddlewares_start.py-12"></a>

### `StartSpiderMiddleware` · class
```python
class StartSpiderMiddleware(BaseSpiderMiddleware)
```

*来源: `scrapy/spidermiddlewares/start.py:12` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_start.py-26"></a>

### `StartSpiderMiddleware.get_processed_request` · method
```python
def get_processed_request(
        self, request: Request, response: Response | None
    ) -> Request | None
```

*来源: `scrapy/spidermiddlewares/start.py:26` · 待生成*

---

## `scrapy/spidermiddlewares/urllength.py`

<a id="sym-scrapy_spidermiddlewares_urllength.py-26"></a>

### `UrlLengthMiddleware` · class
```python
class UrlLengthMiddleware(BaseSpiderMiddleware)
```

*来源: `scrapy/spidermiddlewares/urllength.py:26` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_urllength.py-29"></a>

### `UrlLengthMiddleware.__init__` · method
```python
def __init__(self, maxlength: int)
```

*来源: `scrapy/spidermiddlewares/urllength.py:29` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_urllength.py-33"></a>

### `UrlLengthMiddleware.from_crawler` · method
装饰器: `@classmethod`
```python
def from_crawler(cls, crawler: Crawler) -> Self
```

**内部调用(库内):**
- [`BaseSettings.getint`](scrapy_settings.md#sym-scrapy_settings___init__.py-201)

*来源: `scrapy/spidermiddlewares/urllength.py:33` · 待生成*

---
<a id="sym-scrapy_spidermiddlewares_urllength.py-41"></a>

### `UrlLengthMiddleware.get_processed_request` · method
```python
def get_processed_request(
        self, request: Request, response: Response | None
    ) -> Request | None
```

**内部调用(库内):**
- [`WrappedResponse.info`](scrapy_http.md#sym-scrapy_http_cookies.py-210)

*来源: `scrapy/spidermiddlewares/urllength.py:41` · 待生成*

---