# API 参考:`scrapy/http`

## `scrapy/http/cookies.py`

<a id="sym-scrapy_http_cookies.py-27"></a>

### `CookieJar` · class
```python
class CookieJar
```

*来源: `scrapy/http/cookies.py:27` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-28"></a>

### `CookieJar.__init__` · method
```python
def __init__(
        self,
        policy: CookiePolicy | None = None,
        check_expired_frequency: int = 10000,
    )
```

**内部调用(库内):**
- [`_DummyLock`](scrapy_http.md#sym-scrapy_http_cookies.py-130)

*来源: `scrapy/http/cookies.py:28` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-39"></a>

### `CookieJar.extract_cookies` · method
```python
def extract_cookies(self, response: Response, request: Request) -> None
```

**内部调用(库内):**
- [`WrappedRequest`](scrapy_http.md#sym-scrapy_http_cookies.py-138)
- [`WrappedResponse`](scrapy_http.md#sym-scrapy_http_cookies.py-206)

*来源: `scrapy/http/cookies.py:39` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-44"></a>

### `CookieJar.add_cookie_header` · method
```python
def add_cookie_header(self, request: Request) -> None
```

**内部调用(库内):**
- [`WrappedRequest`](scrapy_http.md#sym-scrapy_http_cookies.py-138)
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)
- [`potential_domain_matches`](scrapy_http.md#sym-scrapy_http_cookies.py-111)
- [`WrappedRequest.has_header`](scrapy_http.md#sym-scrapy_http_cookies.py-186)
- [`WrappedRequest.add_unredirected_header`](scrapy_http.md#sym-scrapy_http_cookies.py-202)

*来源: `scrapy/http/cookies.py:44` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-76"></a>

### `CookieJar._cookies` · method
装饰器: `@property`
```python
def _cookies(self) -> dict[str, dict[str, dict[str, Cookie]]]
```

*来源: `scrapy/http/cookies.py:76` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-79"></a>

### `CookieJar.clear_session_cookies` · method
```python
def clear_session_cookies(self) -> None
```

*来源: `scrapy/http/cookies.py:79` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-82"></a>

### `CookieJar.clear` · method
```python
def clear(
        self,
        domain: str | None = None,
        path: str | None = None,
        name: str | None = None,
    ) -> None
```

*来源: `scrapy/http/cookies.py:82` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-90"></a>

### `CookieJar.__iter__` · method
```python
def __iter__(self) -> Iterator[Cookie]
```

*来源: `scrapy/http/cookies.py:90` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-93"></a>

### `CookieJar.__len__` · method
```python
def __len__(self) -> int
```

*来源: `scrapy/http/cookies.py:93` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-96"></a>

### `CookieJar.set_policy` · method
```python
def set_policy(self, pol: CookiePolicy) -> None
```

*来源: `scrapy/http/cookies.py:96` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-99"></a>

### `CookieJar.make_cookies` · method
```python
def make_cookies(self, response: Response, request: Request) -> Sequence[Cookie]
```

**内部调用(库内):**
- [`WrappedRequest`](scrapy_http.md#sym-scrapy_http_cookies.py-138)
- [`WrappedResponse`](scrapy_http.md#sym-scrapy_http_cookies.py-206)

*来源: `scrapy/http/cookies.py:99` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-104"></a>

### `CookieJar.set_cookie` · method
```python
def set_cookie(self, cookie: Cookie) -> None
```

*来源: `scrapy/http/cookies.py:104` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-107"></a>

### `CookieJar.set_cookie_if_ok` · method
```python
def set_cookie_if_ok(self, cookie: Cookie, request: Request) -> None
```

**内部调用(库内):**
- [`WrappedRequest`](scrapy_http.md#sym-scrapy_http_cookies.py-138)

*来源: `scrapy/http/cookies.py:107` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-111"></a>

### `potential_domain_matches` · func
```python
def potential_domain_matches(domain: str) -> list[str]
```

*来源: `scrapy/http/cookies.py:111` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-130"></a>

### `_DummyLock` · class
```python
class _DummyLock
```

*来源: `scrapy/http/cookies.py:130` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-131"></a>

### `_DummyLock.acquire` · method
```python
def acquire(self) -> None
```

*来源: `scrapy/http/cookies.py:131` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-134"></a>

### `_DummyLock.release` · method
```python
def release(self) -> None
```

*来源: `scrapy/http/cookies.py:134` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-138"></a>

### `WrappedRequest` · class
```python
class WrappedRequest
```

*来源: `scrapy/http/cookies.py:138` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-144"></a>

### `WrappedRequest.__init__` · method
```python
def __init__(self, request: Request)
```

*来源: `scrapy/http/cookies.py:144` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-147"></a>

### `WrappedRequest.get_full_url` · method
```python
def get_full_url(self) -> str
```

*来源: `scrapy/http/cookies.py:147` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-150"></a>

### `WrappedRequest.get_host` · method
```python
def get_host(self) -> str
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/http/cookies.py:150` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-153"></a>

### `WrappedRequest.get_type` · method
```python
def get_type(self) -> str
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/http/cookies.py:153` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-156"></a>

### `WrappedRequest.is_unverifiable` · method
```python
def is_unverifiable(self) -> bool
```

*来源: `scrapy/http/cookies.py:156` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-167"></a>

### `WrappedRequest.full_url` · method
装饰器: `@property`
```python
def full_url(self) -> str
```

**内部调用(库内):**
- [`WrappedRequest.get_full_url`](scrapy_http.md#sym-scrapy_http_cookies.py-147)

*来源: `scrapy/http/cookies.py:167` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-171"></a>

### `WrappedRequest.host` · method
装饰器: `@property`
```python
def host(self) -> str
```

**内部调用(库内):**
- [`WrappedRequest.get_host`](scrapy_http.md#sym-scrapy_http_cookies.py-150)

*来源: `scrapy/http/cookies.py:171` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-175"></a>

### `WrappedRequest.type` · method
装饰器: `@property`
```python
def type(self) -> str
```

**内部调用(库内):**
- [`WrappedRequest.get_type`](scrapy_http.md#sym-scrapy_http_cookies.py-153)

*来源: `scrapy/http/cookies.py:175` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-179"></a>

### `WrappedRequest.unverifiable` · method
装饰器: `@property`
```python
def unverifiable(self) -> bool
```

**内部调用(库内):**
- [`WrappedRequest.is_unverifiable`](scrapy_http.md#sym-scrapy_http_cookies.py-156)

*来源: `scrapy/http/cookies.py:179` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-183"></a>

### `WrappedRequest.origin_req_host` · method
装饰器: `@property`
```python
def origin_req_host(self) -> str
```

**内部调用(库内):**
- [`urlparse_cached`](scrapy_utils.md#sym-scrapy_utils_httpobj.py-18)

*来源: `scrapy/http/cookies.py:183` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-186"></a>

### `WrappedRequest.has_header` · method
```python
def has_header(self, name: str) -> bool
```

*来源: `scrapy/http/cookies.py:186` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-189"></a>

### `WrappedRequest.get_header` · method
```python
def get_header(self, name: str, default: str | None = None) -> str | None
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/http/cookies.py:189` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-193"></a>

### `WrappedRequest.header_items` · method
```python
def header_items(self) -> list[tuple[str, list[str]]]
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/http/cookies.py:193` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-202"></a>

### `WrappedRequest.add_unredirected_header` · method
```python
def add_unredirected_header(self, name: str, value: str) -> None
```

**内部调用(库内):**
- [`Headers.appendlist`](scrapy_http.md#sym-scrapy_http_headers.py-98)

*来源: `scrapy/http/cookies.py:202` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-206"></a>

### `WrappedResponse` · class
```python
class WrappedResponse
```

*来源: `scrapy/http/cookies.py:206` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-207"></a>

### `WrappedResponse.__init__` · method
```python
def __init__(self, response: Response)
```

*来源: `scrapy/http/cookies.py:207` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-210"></a>

### `WrappedResponse.info` · method
```python
def info(self) -> Self
```

*来源: `scrapy/http/cookies.py:210` · 待生成*

---
<a id="sym-scrapy_http_cookies.py-213"></a>

### `WrappedResponse.get_all` · method
```python
def get_all(self, name: str, default: Any = None) -> list[str]
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/http/cookies.py:213` · 待生成*

---

## `scrapy/http/headers.py`

<a id="sym-scrapy_http_headers.py-23"></a>

### `Headers` · class
```python
class Headers(CaselessDict)
```

*来源: `scrapy/http/headers.py:23` · 待生成*

---
<a id="sym-scrapy_http_headers.py-26"></a>

### `Headers.__init__` · method
```python
def __init__(
        self,
        seq: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        encoding: str = "utf-8",
    )
```

*来源: `scrapy/http/headers.py:26` · 待生成*

---
<a id="sym-scrapy_http_headers.py-34"></a>

### `Headers.update` · method
```python
def update(  # type: ignore[override]
        self, seq: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]]
    ) -> None
```

**内部调用(库内):**
- [`Headers.normkey`](scrapy_http.md#sym-scrapy_http_headers.py-43)
- [`Headers.normvalue`](scrapy_http.md#sym-scrapy_http_headers.py-47)

*来源: `scrapy/http/headers.py:34` · 待生成*

---
<a id="sym-scrapy_http_headers.py-43"></a>

### `Headers.normkey` · method
```python
def normkey(self, key: AnyStr) -> bytes
```

**内部调用(库内):**
- [`Headers._tobytes`](scrapy_http.md#sym-scrapy_http_headers.py-61)

*来源: `scrapy/http/headers.py:43` · 待生成*

---
<a id="sym-scrapy_http_headers.py-47"></a>

### `Headers.normvalue` · method
```python
def normvalue(self, value: _RawValue | Iterable[_RawValue]) -> list[bytes]
```

**内部调用(库内):**
- [`Headers._tobytes`](scrapy_http.md#sym-scrapy_http_headers.py-61)

*来源: `scrapy/http/headers.py:47` · 待生成*

---
<a id="sym-scrapy_http_headers.py-61"></a>

### `Headers._tobytes` · method
```python
def _tobytes(self, x: _RawValue) -> bytes
```

*来源: `scrapy/http/headers.py:61` · 待生成*

---
<a id="sym-scrapy_http_headers.py-70"></a>

### `Headers.__getitem__` · method
```python
def __getitem__(self, key: AnyStr) -> bytes | None
```

*来源: `scrapy/http/headers.py:70` · 待生成*

---
<a id="sym-scrapy_http_headers.py-76"></a>

### `Headers.get` · method
```python
def get(self, key: AnyStr, def_val: Any = None) -> bytes | None
```

*来源: `scrapy/http/headers.py:76` · 待生成*

---
<a id="sym-scrapy_http_headers.py-82"></a>

### `Headers.getlist` · method
```python
def getlist(self, key: AnyStr, def_val: Any = None) -> list[bytes]
```

**内部调用(库内):**
- [`Headers.__getitem__`](scrapy_http.md#sym-scrapy_http_headers.py-70)
- [`Headers.normvalue`](scrapy_http.md#sym-scrapy_http_headers.py-47)

*来源: `scrapy/http/headers.py:82` · 待生成*

---
<a id="sym-scrapy_http_headers.py-90"></a>

### `Headers.setlist` · method
```python
def setlist(self, key: AnyStr, list_: Iterable[_RawValue]) -> None
```

*来源: `scrapy/http/headers.py:90` · 待生成*

---
<a id="sym-scrapy_http_headers.py-93"></a>

### `Headers.setlistdefault` · method
```python
def setlistdefault(
        self, key: AnyStr, default_list: Iterable[_RawValue] = ()
    ) -> Any
```

*来源: `scrapy/http/headers.py:93` · 待生成*

---
<a id="sym-scrapy_http_headers.py-98"></a>

### `Headers.appendlist` · method
```python
def appendlist(self, key: AnyStr, value: Iterable[_RawValue]) -> None
```

**内部调用(库内):**
- [`Headers.getlist`](scrapy_http.md#sym-scrapy_http_headers.py-82)
- [`Headers.normvalue`](scrapy_http.md#sym-scrapy_http_headers.py-47)

*来源: `scrapy/http/headers.py:98` · 待生成*

---
<a id="sym-scrapy_http_headers.py-103"></a>

### `Headers.items` · method
```python
def items(self) -> Iterable[tuple[bytes, list[bytes]]]
```

**内部调用(库内):**
- [`Headers.getlist`](scrapy_http.md#sym-scrapy_http_headers.py-82)

*来源: `scrapy/http/headers.py:103` · 待生成*

---
<a id="sym-scrapy_http_headers.py-106"></a>

### `Headers.values` · method
```python
def values(self) -> list[bytes | None]
```

*来源: `scrapy/http/headers.py:106` · 待生成*

---
<a id="sym-scrapy_http_headers.py-112"></a>

### `Headers.to_string` · method
```python
def to_string(self) -> bytes
```

*来源: `scrapy/http/headers.py:112` · 待生成*

---
<a id="sym-scrapy_http_headers.py-115"></a>

### `Headers.to_unicode_dict` · method
```python
def to_unicode_dict(self) -> CaseInsensitiveDict
```

**内部调用(库内):**
- [`CaseInsensitiveDict`](scrapy_utils.md#sym-scrapy_utils_datatypes.py-102)
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/http/headers.py:115` · 待生成*

---
<a id="sym-scrapy_http_headers.py-127"></a>

### `Headers.to_tuple_list` · method
```python
def to_tuple_list(self) -> list[tuple[str, str]]
```

*来源: `scrapy/http/headers.py:127` · 待生成*

---
<a id="sym-scrapy_http_headers.py-138"></a>

### `Headers.__copy__` · method
```python
def __copy__(self) -> Self
```

*来源: `scrapy/http/headers.py:138` · 待生成*

---

## `scrapy/http/request/__init__.py`

<a id="sym-scrapy_http_request___init__.py-46"></a>

### `VerboseCookie` · class
```python
class VerboseCookie(TypedDict)
```

*来源: `scrapy/http/request/__init__.py:46` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-60"></a>

### `NO_CALLBACK` · func
```python
def NO_CALLBACK(*args: Any, **kwargs: Any) -> NoReturn
```

*来源: `scrapy/http/request/__init__.py:60` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-84"></a>

### `Request` · class
```python
class Request(object_ref)
```

*来源: `scrapy/http/request/__init__.py:84` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-123"></a>

### `Request.__init__` · method
```python
def __init__(
        self,
        url: str,
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str = "utf-8",
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        flags: list[str] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
    ) -> None
```

**内部调用(库内):**
- [`Request._set_url`](scrapy_http.md#sym-scrapy_http_request___init__.py-258)
- [`Request._set_body`](scrapy_http.md#sym-scrapy_http_request___init__.py-278)
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/http/request/__init__.py:123` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-240"></a>

### `Request.cb_kwargs` · method
装饰器: `@property`
```python
def cb_kwargs(self) -> dict[str, Any]
```

*来源: `scrapy/http/request/__init__.py:240` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-246"></a>

### `Request.meta` · method
装饰器: `@property`
```python
def meta(self) -> dict[str, Any]
```

*来源: `scrapy/http/request/__init__.py:246` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-252"></a>

### `Request.url` · method
装饰器: `@property`
```python
def url(self) -> str
```

*来源: `scrapy/http/request/__init__.py:252` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-255"></a>

### `Request._url_is_verbatim` · method
```python
def _url_is_verbatim(self) -> bool
```

*来源: `scrapy/http/request/__init__.py:255` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-258"></a>

### `Request._set_url` · method
```python
def _set_url(self, url: str) -> None
```

**内部调用(库内):**
- [`Request._url_is_verbatim`](scrapy_http.md#sym-scrapy_http_request___init__.py-255)

*来源: `scrapy/http/request/__init__.py:258` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-275"></a>

### `Request.body` · method
装饰器: `@property`
```python
def body(self) -> bytes
```

*来源: `scrapy/http/request/__init__.py:275` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-278"></a>

### `Request._set_body` · method
```python
def _set_body(self, body: str | bytes | None) -> None
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/http/request/__init__.py:278` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-282"></a>

### `Request.encoding` · method
装饰器: `@property`
```python
def encoding(self) -> str
```

*来源: `scrapy/http/request/__init__.py:282` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-286"></a>

### `Request.flags` · method
装饰器: `@property`
```python
def flags(self) -> list[str]
```

*来源: `scrapy/http/request/__init__.py:286` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-292"></a>

### `Request.flags` · method
装饰器: `@flags.setter`
```python
def flags(self, value: list[str] | None) -> None
```

*来源: `scrapy/http/request/__init__.py:292` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-296"></a>

### `Request.cookies` · method
装饰器: `@property`
```python
def cookies(self) -> CookiesT
```

*来源: `scrapy/http/request/__init__.py:296` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-302"></a>

### `Request.cookies` · method
装饰器: `@cookies.setter`
```python
def cookies(self, value: CookiesT | None) -> None
```

*来源: `scrapy/http/request/__init__.py:302` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-306"></a>

### `Request.headers` · method
装饰器: `@property`
```python
def headers(self) -> Headers
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/http/request/__init__.py:306` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-312"></a>

### `Request.headers` · method
装饰器: `@headers.setter`
```python
def headers(
        self, value: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None
    ) -> None
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/http/request/__init__.py:312` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-322"></a>

### `Request.__repr__` · method
```python
def __repr__(self) -> str
```

*来源: `scrapy/http/request/__init__.py:322` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-325"></a>

### `Request.copy` · method
```python
def copy(self) -> Self
```

*来源: `scrapy/http/request/__init__.py:325` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-329"></a>

### `Request.replace` · method
装饰器: `@overload`
```python
def replace(
        self, *args: Any, cls: type[RequestTypeVar], **kwargs: Any
    ) -> RequestTypeVar
```

*来源: `scrapy/http/request/__init__.py:329` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-334"></a>

### `Request.replace` · method
装饰器: `@overload`
```python
def replace(self, *args: Any, cls: None = None, **kwargs: Any) -> Self
```

*来源: `scrapy/http/request/__init__.py:334` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-336"></a>

### `Request.replace` · method
```python
def replace(
        self, *args: Any, cls: type[Request] | None = None, **kwargs: Any
    ) -> Request
```

*来源: `scrapy/http/request/__init__.py:336` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-347"></a>

### `Request.from_curl` · method
装饰器: `@classmethod`
```python
def from_curl(
        cls,
        curl_command: str,
        ignore_unknown_options: bool = True,
        **kwargs: Any,
    ) -> Self
```

**内部调用(库内):**
- [`curl_to_request_kwargs`](scrapy_utils.md#sym-scrapy_utils_curl.py-87)

*来源: `scrapy/http/request/__init__.py:347` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-384"></a>

### `Request.to_dict` · method
```python
def to_dict(self, *, spider: scrapy.Spider | None = None) -> dict[str, Any]
```

**内部调用(库内):**
- [`_find_method`](scrapy_http.md#sym-scrapy_http_request___init__.py-413)

*来源: `scrapy/http/request/__init__.py:384` · 待生成*

---
<a id="sym-scrapy_http_request___init__.py-413"></a>

### `_find_method` · func
```python
def _find_method(obj: Any, func: Callable[..., Any]) -> str
```

*来源: `scrapy/http/request/__init__.py:413` · 待生成*

---

## `scrapy/http/request/form.py`

<a id="sym-scrapy_http_request_form.py-47"></a>

### `FormRequest` · class
```python
class FormRequest(Request)
```

*来源: `scrapy/http/request/form.py:47` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-52"></a>

### `FormRequest.__init__` · method
```python
def __init__(
        self, *args: Any, formdata: FormdataType = None, **kwargs: Any
    ) -> None
```

**内部调用(库内):**
- [`_urlencode`](scrapy_http.md#sym-scrapy_http_request_form.py-115)

*来源: `scrapy/http/request/form.py:52` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-74"></a>

### `FormRequest.from_response` · method
装饰器: `@classmethod`
```python
def from_response(
        cls,
        response: TextResponse,
        formname: str | None = None,
        formid: str | None = None,
        formnumber: int = 0,
        formdata: FormdataType = None,
        clickdata: dict[str, str | int] | None = None,
        dont_click: bool = False,
        formxpath: str | None = None,
        formcss: str | None = None,
        **kwargs: Any,
    ) -> Self
```

**内部调用(库内):**
- [`_get_form`](scrapy_http.md#sym-scrapy_http_request_form.py-124)
- [`_get_inputs`](scrapy_http.md#sym-scrapy_http_request_form.py-168)
- [`_get_form_url`](scrapy_http.md#sym-scrapy_http_request_form.py-105)

*来源: `scrapy/http/request/form.py:74` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-105"></a>

### `_get_form_url` · func
```python
def _get_form_url(form: FormElement, url: str | None) -> str
```

*来源: `scrapy/http/request/form.py:105` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-115"></a>

### `_urlencode` · func
```python
def _urlencode(seq: Iterable[FormdataKVType], enc: str) -> str
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)
- [`is_listlike`](scrapy_utils.md#sym-scrapy_utils_python.py-35)

*来源: `scrapy/http/request/form.py:115` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-124"></a>

### `_get_form` · func
```python
def _get_form(
    response: TextResponse,
    formname: str | None,
    formid: str | None,
    formnumber: int,
    formxpath: str | None,
) -> FormElement
```

*来源: `scrapy/http/request/form.py:124` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-168"></a>

### `_get_inputs` · func
```python
def _get_inputs(
    form: FormElement,
    formdata: FormdataType,
    dont_click: bool,
    clickdata: dict[str, str | int] | None,
) -> list[FormdataKVType]
```

**内部调用(库内):**
- [`_value`](scrapy_http.md#sym-scrapy_http_request_form.py-207)
- [`_get_clickable`](scrapy_http.md#sym-scrapy_http_request_form.py-229)

*来源: `scrapy/http/request/form.py:168` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-207"></a>

### `_value` · func
```python
def _value(
    ele: InputElement | SelectElement | TextareaElement,
) -> tuple[str | None, str | MultipleSelectOptions | None]
```

**内部调用(库内):**
- [`_select_value`](scrapy_http.md#sym-scrapy_http_request_form.py-217)

*来源: `scrapy/http/request/form.py:207` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-217"></a>

### `_select_value` · func
```python
def _select_value(
    ele: SelectElement, n: str | None, v: str | MultipleSelectOptions | None
) -> tuple[str | None, str | MultipleSelectOptions | None]
```

*来源: `scrapy/http/request/form.py:217` · 待生成*

---
<a id="sym-scrapy_http_request_form.py-229"></a>

### `_get_clickable` · func
```python
def _get_clickable(
    clickdata: dict[str, str | int] | None, form: FormElement
) -> tuple[str, str] | None
```

*来源: `scrapy/http/request/form.py:229` · 待生成*

---

## `scrapy/http/request/json_request.py`

<a id="sym-scrapy_http_request_json_request.py-22"></a>

### `JsonRequest` · class
```python
class JsonRequest(Request)
```

*来源: `scrapy/http/request/json_request.py:22` · 待生成*

---
<a id="sym-scrapy_http_request_json_request.py-27"></a>

### `JsonRequest.__init__` · method
```python
def __init__(
        self, *args: Any, dumps_kwargs: dict[str, Any] | None = None, **kwargs: Any
    ) -> None
```

**内部调用(库内):**
- [`Item.deepcopy`](scrapy.md#sym-scrapy_item.py-130) — 返回此 item 的深拷贝。
- [`JsonRequest._dumps`](scrapy_http.md#sym-scrapy_http_request_json_request.py-81)

*来源: `scrapy/http/request/json_request.py:27` · 待生成*

---
<a id="sym-scrapy_http_request_json_request.py-54"></a>

### `JsonRequest.dumps_kwargs` · method
装饰器: `@property`
```python
def dumps_kwargs(self) -> dict[str, Any]
```

*来源: `scrapy/http/request/json_request.py:54` · 待生成*

---
<a id="sym-scrapy_http_request_json_request.py-58"></a>

### `JsonRequest.replace` · method
装饰器: `@overload`
```python
def replace(
        self, *args: Any, cls: type[RequestTypeVar], **kwargs: Any
    ) -> RequestTypeVar
```

*来源: `scrapy/http/request/json_request.py:58` · 待生成*

---
<a id="sym-scrapy_http_request_json_request.py-63"></a>

### `JsonRequest.replace` · method
装饰器: `@overload`
```python
def replace(self, *args: Any, cls: None = None, **kwargs: Any) -> Self
```

*来源: `scrapy/http/request/json_request.py:63` · 待生成*

---
<a id="sym-scrapy_http_request_json_request.py-65"></a>

### `JsonRequest.replace` · method
```python
def replace(
        self, *args: Any, cls: type[Request] | None = None, **kwargs: Any
    ) -> Request
```

**内部调用(库内):**
- [`JsonRequest._dumps`](scrapy_http.md#sym-scrapy_http_request_json_request.py-81)

*来源: `scrapy/http/request/json_request.py:65` · 待生成*

---
<a id="sym-scrapy_http_request_json_request.py-81"></a>

### `JsonRequest._dumps` · method
```python
def _dumps(self, data: Any) -> str
```

*来源: `scrapy/http/request/json_request.py:81` · 待生成*

---

## `scrapy/http/request/rpc.py`

<a id="sym-scrapy_http_request_rpc.py-23"></a>

### `XmlRpcRequest` · class
```python
class XmlRpcRequest(Request)
```

*来源: `scrapy/http/request/rpc.py:23` · 待生成*

---
<a id="sym-scrapy_http_request_rpc.py-26"></a>

### `XmlRpcRequest.__init__` · method
```python
def __init__(self, *args: Any, encoding: str | None = None, **kwargs: Any)
```

*来源: `scrapy/http/request/rpc.py:26` · 待生成*

---

## `scrapy/http/response/__init__.py`

<a id="sym-scrapy_http_response___init__.py-35"></a>

### `Response` · class
```python
class Response(object_ref)
```

*来源: `scrapy/http/response/__init__.py:35` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-71"></a>

### `Response.__init__` · method
```python
def __init__(
        self,
        url: str,
        status: int = 200,
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes = b"",
        flags: list[str] | None = None,
        request: Request | None = None,
        certificate: Any = None,
        ip_address: IPv4Address | IPv6Address | None = None,
        protocol: str | None = None,
    )
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)
- [`Response._set_body`](scrapy_http.md#sym-scrapy_http_response___init__.py-128)
- [`Response._set_url`](scrapy_http.md#sym-scrapy_http_response___init__.py-116)

*来源: `scrapy/http/response/__init__.py:71` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-94"></a>

### `Response.cb_kwargs` · method
装饰器: `@property`
```python
def cb_kwargs(self) -> dict[str, Any]
```

*来源: `scrapy/http/response/__init__.py:94` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-104"></a>

### `Response.meta` · method
装饰器: `@property`
```python
def meta(self) -> dict[str, Any]
```

*来源: `scrapy/http/response/__init__.py:104` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-113"></a>

### `Response.url` · method
装饰器: `@property`
```python
def url(self) -> str
```

*来源: `scrapy/http/response/__init__.py:113` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-116"></a>

### `Response._set_url` · method
```python
def _set_url(self, url: str) -> None
```

*来源: `scrapy/http/response/__init__.py:116` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-125"></a>

### `Response.body` · method
装饰器: `@property`
```python
def body(self) -> bytes
```

*来源: `scrapy/http/response/__init__.py:125` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-128"></a>

### `Response._set_body` · method
```python
def _set_body(self, body: bytes | None) -> None
```

*来源: `scrapy/http/response/__init__.py:128` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-141"></a>

### `Response.headers` · method
装饰器: `@property`
```python
def headers(self) -> Headers
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/http/response/__init__.py:141` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-147"></a>

### `Response.headers` · method
装饰器: `@headers.setter`
```python
def headers(
        self, value: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None
    ) -> None
```

**内部调用(库内):**
- [`Headers`](scrapy_http.md#sym-scrapy_http_headers.py-23)

*来源: `scrapy/http/response/__init__.py:147` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-156"></a>

### `Response.flags` · method
装饰器: `@property`
```python
def flags(self) -> list[str]
```

*来源: `scrapy/http/response/__init__.py:156` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-162"></a>

### `Response.flags` · method
装饰器: `@flags.setter`
```python
def flags(self, value: list[str] | None) -> None
```

*来源: `scrapy/http/response/__init__.py:162` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-165"></a>

### `Response.__repr__` · method
```python
def __repr__(self) -> str
```

*来源: `scrapy/http/response/__init__.py:165` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-168"></a>

### `Response.copy` · method
```python
def copy(self) -> Self
```

*来源: `scrapy/http/response/__init__.py:168` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-173"></a>

### `Response.replace` · method
装饰器: `@overload`
```python
def replace(
        self, *args: Any, cls: type[ResponseTypeVar], **kwargs: Any
    ) -> ResponseTypeVar
```

*来源: `scrapy/http/response/__init__.py:173` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-178"></a>

### `Response.replace` · method
装饰器: `@overload`
```python
def replace(self, *args: Any, cls: None = None, **kwargs: Any) -> Self
```

*来源: `scrapy/http/response/__init__.py:178` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-180"></a>

### `Response.replace` · method
```python
def replace(
        self, *args: Any, cls: type[Response] | None = None, **kwargs: Any
    ) -> Response
```

*来源: `scrapy/http/response/__init__.py:180` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-190"></a>

### `Response.urljoin` · method
```python
def urljoin(self, url: str) -> str
```

*来源: `scrapy/http/response/__init__.py:190` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-196"></a>

### `Response.text` · method
装饰器: `@property`
```python
def text(self) -> str
```

*来源: `scrapy/http/response/__init__.py:196` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-202"></a>

### `Response.css` · method
```python
def css(self, *a: Any, **kw: Any) -> SelectorList
```

**内部调用(库内):**
- [`NotSupported`](scrapy.md#sym-scrapy_exceptions.py-101) — `NotSupported` 类代表一个异常，用于表示某些功能或操作不被支持。

*来源: `scrapy/http/response/__init__.py:202` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-208"></a>

### `Response.jmespath` · method
```python
def jmespath(self, *a: Any, **kw: Any) -> SelectorList
```

**内部调用(库内):**
- [`NotSupported`](scrapy.md#sym-scrapy_exceptions.py-101) — `NotSupported` 类代表一个异常，用于表示某些功能或操作不被支持。

*来源: `scrapy/http/response/__init__.py:208` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-214"></a>

### `Response.xpath` · method
```python
def xpath(self, *a: Any, **kw: Any) -> SelectorList
```

**内部调用(库内):**
- [`NotSupported`](scrapy.md#sym-scrapy_exceptions.py-101) — `NotSupported` 类代表一个异常，用于表示某些功能或操作不被支持。

*来源: `scrapy/http/response/__init__.py:214` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-220"></a>

### `Response.follow` · method
```python
def follow(
        self,
        url: str | Link,
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str | None = "utf-8",
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
        flags: list[str] | None = None,
    ) -> Request
```

**内部调用(库内):**
- [`Response.urljoin`](scrapy_http.md#sym-scrapy_http_response___init__.py-190)
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `scrapy/http/response/__init__.py:220` · 待生成*

---
<a id="sym-scrapy_http_response___init__.py-270"></a>

### `Response.follow_all` · method
```python
def follow_all(
        self,
        urls: Iterable[str | Link],
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str | None = "utf-8",
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
        flags: list[str] | None = None,
    ) -> Iterable[Request]
```

**内部调用(库内):**
- [`Response.follow`](scrapy_http.md#sym-scrapy_http_response___init__.py-220)

*来源: `scrapy/http/response/__init__.py:270` · 待生成*

---

## `scrapy/http/response/html.py`

<a id="sym-scrapy_http_response_html.py-11"></a>

### `HtmlResponse` · class
```python
class HtmlResponse(TextResponse)
```

*来源: `scrapy/http/response/html.py:11` · 待生成*

---

## `scrapy/http/response/json.py`

<a id="sym-scrapy_http_response_json.py-11"></a>

### `JsonResponse` · class
```python
class JsonResponse(TextResponse)
```

*来源: `scrapy/http/response/json.py:11` · 待生成*

---

## `scrapy/http/response/text.py`

<a id="sym-scrapy_http_response_text.py-42"></a>

### `TextResponse` · class
```python
class TextResponse(Response)
```

*来源: `scrapy/http/response/text.py:42` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-54"></a>

### `TextResponse.__init__` · method
```python
def __init__(self, *args: Any, **kwargs: Any)
```

*来源: `scrapy/http/response/text.py:54` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-62"></a>

### `TextResponse._set_body` · method
```python
def _set_body(self, body: str | bytes | None) -> None
```

*来源: `scrapy/http/response/text.py:62` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-75"></a>

### `TextResponse.encoding` · method
装饰器: `@property`
```python
def encoding(self) -> str
```

**内部调用(库内):**
- [`TextResponse._declared_encoding`](scrapy_http.md#sym-scrapy_http_response_text.py-78)
- [`TextResponse._body_inferred_encoding`](scrapy_http.md#sym-scrapy_http_response_text.py-113)

*来源: `scrapy/http/response/text.py:75` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-78"></a>

### `TextResponse._declared_encoding` · method
```python
def _declared_encoding(self) -> str | None
```

**内部调用(库内):**
- [`TextResponse._bom_encoding`](scrapy_http.md#sym-scrapy_http_response_text.py-143)
- [`TextResponse._headers_encoding`](scrapy_http.md#sym-scrapy_http_response_text.py-109)
- [`TextResponse._body_declared_encoding`](scrapy_http.md#sym-scrapy_http_response_text.py-139)

*来源: `scrapy/http/response/text.py:78` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-86"></a>

### `TextResponse.json` · method
```python
def json(self) -> Any
```

*来源: `scrapy/http/response/text.py:86` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-93"></a>

### `TextResponse.text` · method
装饰器: `@property`
```python
def text(self) -> str
```

*来源: `scrapy/http/response/text.py:93` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-103"></a>

### `TextResponse.urljoin` · method
```python
def urljoin(self, url: str) -> str
```

**内部调用(库内):**
- [`get_base_url`](scrapy_utils.md#sym-scrapy_utils_response.py-28)

*来源: `scrapy/http/response/text.py:103` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-109"></a>

### `TextResponse._headers_encoding` · method
装饰器: `@memoizemethod_noargs`
```python
def _headers_encoding(self) -> str | None
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/http/response/text.py:109` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-113"></a>

### `TextResponse._body_inferred_encoding` · method
```python
def _body_inferred_encoding(self) -> str
```

**内部调用(库内):**
- [`to_unicode`](scrapy_utils.md#sym-scrapy_utils_python.py-72)

*来源: `scrapy/http/response/text.py:113` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-129"></a>

### `TextResponse._auto_detect_fun` · method
```python
def _auto_detect_fun(self, text: bytes) -> str | None
```

*来源: `scrapy/http/response/text.py:129` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-139"></a>

### `TextResponse._body_declared_encoding` · method
装饰器: `@memoizemethod_noargs`
```python
def _body_declared_encoding(self) -> str | None
```

*来源: `scrapy/http/response/text.py:139` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-143"></a>

### `TextResponse._bom_encoding` · method
装饰器: `@memoizemethod_noargs`
```python
def _bom_encoding(self) -> str | None
```

*来源: `scrapy/http/response/text.py:143` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-147"></a>

### `TextResponse.selector` · method
装饰器: `@property`
```python
def selector(self) -> Selector
```

**内部调用(库内):**
- [`Selector`](scrapy_selector.md#sym-scrapy_selector_unified.py-39)

*来源: `scrapy/http/response/text.py:147` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-155"></a>

### `TextResponse.jmespath` · method
```python
def jmespath(self, query: str, **kwargs: Any) -> SelectorList
```

*来源: `scrapy/http/response/text.py:155` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-162"></a>

### `TextResponse.xpath` · method
```python
def xpath(self, query: str, **kwargs: Any) -> SelectorList
```

*来源: `scrapy/http/response/text.py:162` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-165"></a>

### `TextResponse.css` · method
```python
def css(self, query: str) -> SelectorList
```

*来源: `scrapy/http/response/text.py:165` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-168"></a>

### `TextResponse.follow` · method
```python
def follow(
        self,
        url: str | Link | parsel.Selector,
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str | None = None,
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
        flags: list[str] | None = None,
    ) -> Request
```

**内部调用(库内):**
- [`_url_from_selector`](scrapy_http.md#sym-scrapy_http_response_text.py-301)

*来源: `scrapy/http/response/text.py:168` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-221"></a>

### `TextResponse.follow_all` · method
```python
def follow_all(
        self,
        urls: Iterable[str | Link] | parsel.SelectorList[Any] | None = None,
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str | None = None,
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
        flags: list[str] | None = None,
        css: str | None = None,
        xpath: str | None = None,
    ) -> Iterable[Request]
```

**内部调用(库内):**
- [`TextResponse.css`](scrapy_http.md#sym-scrapy_http_response_text.py-165)
- [`TextResponse.xpath`](scrapy_http.md#sym-scrapy_http_response_text.py-162)
- [`_url_from_selector`](scrapy_http.md#sym-scrapy_http_response_text.py-301)

*来源: `scrapy/http/response/text.py:221` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-295"></a>

### `_InvalidSelector` · class
```python
class _InvalidSelector(ValueError)
```

*来源: `scrapy/http/response/text.py:295` · 待生成*

---
<a id="sym-scrapy_http_response_text.py-301"></a>

### `_url_from_selector` · func
```python
def _url_from_selector(sel: parsel.Selector) -> str
```

**内部调用(库内):**
- [`_InvalidSelector`](scrapy_http.md#sym-scrapy_http_response_text.py-295)

*来源: `scrapy/http/response/text.py:301` · 待生成*

---

## `scrapy/http/response/xml.py`

<a id="sym-scrapy_http_response_xml.py-11"></a>

### `XmlResponse` · class
```python
class XmlResponse(TextResponse)
```

*来源: `scrapy/http/response/xml.py:11` · 待生成*

---