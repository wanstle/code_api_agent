# Module: scrapy/downloadermiddlewares
> **Package**: `scrapy.downloadermiddlewares` | **Source**: `scrapy/downloadermiddlewares/__init__.py` (`1` lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `BaseRedirectMiddleware` | class | 基础重定向中间件类，用于处理请求重定向逻辑 |
| `RedirectMiddleware` | class | 处理基于响应状态码和 meta-refresh 标签的重定向 |
| `MetaRefreshMiddleware` | class | 处理 HTML meta refresh 标签的重定向 |
| `CookiesMiddleware` | class | 处理 Cookie 的中间件 |
| `HttpCompressionMiddleware` | class | 处理 HTTP 压缩（gzip, deflate）的中间件 |
| `HttpCacheMiddleware` | class | 处理 HTTP 缓存的中间件 |
| `OffsiteMiddleware` | class | 控制站点外请求的中间件 |
| `RobotsTxtMiddleware` | class | 处理 robots.txt 的中间件 |
| `DownloaderStats` | class | 下载器统计中间件 |
| `HttpProxyMiddleware` | class | 处理 HTTP 代理的中间件 |
| `_is_public_domain` | function | 判断域名是否为公共域 |
| `get_header_size` | function | 计算 HTTP 请求头大小 |
| `get_status_size` | function | 计算 HTTP 响应状态码大小 |

---

## 模块概述

本模块包含多个下载器中间件类和函数，用于处理请求和响应的预处理与后处理逻辑。这些中间件在 Scrapy 爬虫流程中负责处理如重定向、Cookie、压缩、缓存、代理、站点限制、robots.txt、统计等常见功能。它们通过信号机制与爬虫引擎交互，并通过配置项控制行为。模块中的类通常通过 `from_crawler` 类方法初始化，并与 `Crawler` 对象关联。

---

## 类参考

### `BaseRedirectMiddleware`
> **Summary**: 基础重定向中间件类，用于处理请求重定向逻辑

**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`

**Inheritance**: `BaseRedirectMiddleware` → `object`

#### 构造方法

```python
BaseRedirectMiddleware(settings: BaseSettings)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `settings` | `BaseSettings` | Scrapy 配置对象 |

**Raises**: `NotConfigured` — 当 `REDIRECT_ENABLED` 设置为 `False` 时

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `from_crawler(crawler: Crawler)` | `Self` | 从爬虫实例创建中间件实例 |

##### `from_crawler`

```python
from_crawler(crawler: Crawler) -> Self
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `crawler` | `Crawler` | 爬虫实例 |

**Returns**: `Self` — 中间件实例

**See Also**: `RedirectMiddleware`, `MetaRefreshMiddleware`

---

### `RedirectMiddleware`
> **Summary**: 处理基于响应状态码和 meta-refresh 标签的重定向

**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`

**Inheritance**: `RedirectMiddleware` → `BaseRedirectMiddleware`

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `process_response(request: Request, response: Response, spider: Spider | None)` | `Request | Response` | 处理响应并决定是否重定向 |

##### `process_response`

```python
process_response(request: Request, response: Response, spider: Spider | None = None) -> Request | Response
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `request` | `Request` | 请求对象 |
| `response` | `Response` | 响应对象 |
| `spider` | `Spider | None` | 爬虫实例 |

**Returns**: `Request | Response` — 重定向请求或原始响应

**Raises**: `IgnoreRequest` — 当请求被标记为不重定向或状态码被忽略时

**See Also**: `BaseRedirectMiddleware`, `MetaRefreshMiddleware`

---

### `MetaRefreshMiddleware`
> **Summary**: 处理 HTML meta refresh 标签的重定向

**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`

**Inheritance**: `MetaRefreshMiddleware` → `BaseRedirectMiddleware`

#### 构造方法

```python
MetaRefreshMiddleware(settings: BaseSettings)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `settings` | `BaseSettings` | Scrapy 配置对象 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `process_response(request: Request, response: Response, spider: Spider | None)` | `Request | Response` | 处理响应并决定是否重定向 |

##### `process_response`

```python
process_response(request: Request, response: Response, spider: Spider | None = None) -> Request | Response
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `request` | `Request` | 请求对象 |
| `response` | `Response` | 响应对象 |
| `spider