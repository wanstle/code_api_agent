# Module: scrapy.http
> **Package**: `scrapy.http` | **Source**: `scrapy/http/cookies.py` (`216` lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `CookieJar` | class | 管理 HTTP cookie 的类 |
| `_DummyLock` | class | 用于线程安全的空锁实现 |
| `WrappedRequest` | class | 封装 Scrapy Request 以适配 CookieJar 接口 |
| `WrappedResponse` | class | 封装 Scrapy Response 以适配 CookieJar 接口 |
| `potential_domain_matches` | function | 判断域名是否匹配 |
| `VerboseCookie` | class | 定义 cookie 的类型提示 |
| `Request` | class | 表示一个 HTTP 请求 |
| `NO_CALLBACK` | function | 指示请求不使用回调的标记函数 |
| `_find_method` | function | 查找请求方法 |
| `Response` | class | 表示一个 HTTP 响应 |
| `TextResponse` | class | 表示文本格式的 HTTP 响应 |
| `_InvalidSelector` | class | 当无法从选择器获取 URL 时抛出的异常 |
| `_url_from_selector` | function | 从选择器中提取 URL |
| `Headers` | class | 大小写不敏感的 HTTP 头部字典 |
| `FormRequest` | class | 表示一个表单提交的 HTTP 请求 |
| `_get_form_url` | function | 获取表单的 URL |
| `_urlencode` | function | 对表单数据进行 URL 编码 |
| `_get_form` | function | 获取表单元素 |
| `_get_inputs` | function | 获取表单输入项 |
| `_value` | function | 获取表单值 |
| `_select_value` | function | 选择表单值 |
| `_get_clickable` | function | 获取可点击元素 |
| `JsonRequest` | class | 表示一个 JSON 格式的 HTTP 请求 |
| `XmlRpcRequest` | class | 表示一个 XML-RPC 格式的 HTTP 请求 |

---

## 模块概述

本模块涉及 HTTP 请求与响应相关的类和工具，包括请求对象、响应对象、头部管理、Cookie 管理、表单处理等。其中，`CookieJar` 类用于管理 cookie 的提取与添加逻辑，其内部使用 `_DummyLock` 来保证线程安全；`WrappedRequest` 和 `WrappedResponse` 类封装了 Scrapy 的 Request 和 Response 对象以适配 CookieJar 的接口。此外，模块还定义了 `Request` 和 `Response` 类作为核心的 HTTP 请求与响应表示，以及 `Headers` 类用于处理 HTTP 头部。`FormRequest`、`JsonRequest` 和 `XmlRpcRequest` 等子类扩展了基础请求类型，支持不同格式的数据提交。`VerboseCookie` 类提供了 cookie 的类型提示，增强了类型安全性。

---

## 类参考

### `CookieJar`
<!-- api: class | visibility: public | source: scrapy/http/cookies.py:27 -->

> **Summary**: 管理 HTTP cookie 的类

**Type**: `<class>` | **Module**: `scrapy.http`

**Inheritance**: `CookieJar` → `object`

#### 构造方法

```python
CookieJar(policy: CookiePolicy | None = None, check_expired_frequency: int = 10000)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `policy` | `CookiePolicy | None` | Cookie 策略 |
| `check_expired_frequency` | `int` | 检查过期频率 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `extract_cookies(response: Response, request: Request)` | `None` | 从响应中提取 cookie |
| `add_cookie_header(request: Request)` | `None` | 向请求中添加 cookie 头部 |

---

### `_DummyLock`
<!-- api: class | visibility: public | source: scrapy/http/cookies.py: