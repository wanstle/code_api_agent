# Module: scrapy.http
> **Package**: `scrapy.http` | **Source**: `scrapy/http/__init__.py` (`1` lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `CookieJar` | class | HTTP cookies 管理器 |
| `Headers` | class | HTTP headers 容器 |
| `Request` | class | HTTP 请求对象 |
| `Response` | class | HTTP 响应对象 |
| `TextResponse` | class | 文本内容的 HTTP 响应对象 |
| `FormRequest` | class | 表单提交的 HTTP 请求对象 |
| `JsonRequest` | class | JSON 数据的 HTTP 请求对象 |
| `XmlRpcRequest` | class | XML-RPC 的 HTTP 请求对象 |
| `VerboseCookie` | class | 详细 Cookie 结构定义 |
| `NO_CALLBACK` | function | 表示不使用回调的特殊值 |
| `potential_domain_matches` | function | 检查域名是否匹配 |

---

## 模块概述

本模块是 Scrapy 框架中 HTTP 请求与响应处理的核心模块，负责定义和管理 HTTP 请求（Request）和响应（Response）对象。它提供了基础的 HTTP 协议交互接口，包括请求头、Cookie、表单数据、JSON 数据等常见 HTTP 元素的封装。该模块作为 Scrapy 网络层的基础，被下载器（Downloader）和爬虫（Spider）模块广泛使用，是整个爬虫系统中数据流转的关键桥梁。

---

## 类参考

### `CookieJar`
> **Summary**: HTTP cookies 管理器，用于处理请求和响应中的 Cookie。

**Type**: `class` | **Module**: `scrapy.http.cookies`

**Inheritance**: `CookieJar` → `object`

#### 构造方法

```python
CookieJar(policy: CookiePolicy | None = None, check_expired_frequency: int = 10000)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `policy` | `CookiePolicy | None` | Cookie 策略对象 |
| `check_expired_frequency` | `int` | 检查过期频率 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `extract_cookies(response: Response, request: Request)` | `None` | 从响应中提取 Cookie |
| `add_cookie_header(request: Request)` | `None` | 为请求添加 Cookie 头 |

---

### `Headers`
> **Summary**: HTTP headers 容器，支持大小写不敏感的键访问。

**Type**: `class` | **Module**: `scrapy.http.headers`

**Inheritance**: `Headers` → `CaselessDict`

#### 构造方法

```python
Headers(seq: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None, encoding: str = "utf-8")
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `seq` | `Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None` | 初始数据 |
| `encoding` | `str` | 编码格式 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `update(seq: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]])` | `None` | 更新 headers |

---

### `Request`
> **Summary**: 表示一个 HTTP 请求，通常由 Spider 生成并由 Downloader 执行。

**Type**: `class` | **Module**: `scrapy.http.request`

**Inheritance**: `Request` → `object`

#### 构造方法

```python
Request(url: str, callback: Callable | None = None, method: str = "GET", headers: Headers | None = None, body: bytes | None = None, cookies: dict[str, str] | None = None, meta: dict | None = None, encoding: str = "utf-8", flags: list[str] | None = None, dont_filter: bool = False, errback: Callable | None = None, cb_kwargs: dict | None = None)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `url` | `str` | 请求 URL |
| `callback` | `Callable | None` | 回调函数 |
| `method` | `str` | HTTP 方法 |
| `headers` | `Headers | None` | 请求头 |
| `body` | `bytes | None` | 请求体 |
| `cookies` | `dict[str, str] | None` | Cookie |
| `meta` | `dict | None` | 元数据 |
| `encoding` | `str` | 编码 |
| `flags` | `list[str] | None` | 标志 |
| `dont_filter` | `bool` | 是否过滤重复请求 |
| `errback` | `Callable | None` | 错误回调 |
| `cb_kwargs` | `dict | None` | 回调参数 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `__init__(url: str, callback: Callable | None = None, method: str = "GET", headers: Headers | None = None, body: bytes | None = None, cookies: dict[str, str] | None = None, meta: dict | None = None, encoding: str