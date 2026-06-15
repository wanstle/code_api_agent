# Module: scrapy/downloadermiddlewares
> **Package**: `scrapy.downloadermiddlewares` | **Source**: `scrapy/downloadermiddlewares/__init__.py` (`1` lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `BaseRedirectMiddleware` | class | 处理重定向的基类中间件 |
| `RedirectMiddleware` | class | 基于响应状态和 meta-refresh 标签处理重定向 |
| `MetaRefreshMiddleware` | class | 处理 HTML meta refresh 标签的重定向中间件 |
| `CookiesMiddleware` | class | 支持处理 Cookie 的中间件 |
| `HttpCompressionMiddleware` | class | 处理 HTTP 压缩（gzip, deflate）的中间件 |
| `HttpCacheMiddleware` | class | 实现 HTTP 缓存功能的中间件 |
| `OffsiteMiddleware` | class | 控制请求是否允许访问站点外域名的中间件 |
| `RobotsTxtMiddleware` | class | 实现 robots.txt 规则的中间件 |
| `DownloaderStats` | class | 下载器统计信息收集中间件 |
| `HttpProxyMiddleware` | class | 处理 HTTP 代理设置的中间件 |
| `_is_public_domain` | function | 判断域名是否为公共域名 |
| `get_header_size` | function | 计算 HTTP 请求头大小 |
| `get_status_size` | function | 计算 HTTP 响应状态行大小 |

---

## 模块概述

本模块是 Scrapy 网络请求处理流程中的中间件集合，负责在请求发送前和响应返回后执行特定逻辑。它作为下载器（Downloader）与爬虫（Spider）之间的桥梁，提供诸如重定向、Cookie 管理、压缩支持、缓存、代理、robots.txt 遵守、统计信息等核心功能。这些中间件通过信号机制与 Scrapy 引擎交互，可被配置启用或禁用，以满足不同爬虫任务的需求。模块中的类和函数被设计为可插拔组件，允许用户自定义行为。

---

## 类参考

### `BaseRedirectMiddleware`
> **Summary**: 处理重定向的基类中间件

**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`

**Inheritance**: `BaseRedirectMiddleware` → `object`

#### 构造方法

```python
BaseRedirectMiddleware(settings: BaseSettings)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `settings` | `BaseSettings` | Scrapy 配置对象 |

**Raises**: `NotConfigured` — 当 `REDIRECT_ENABLED` 设置为 `False` 时。

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

---

### `RedirectMiddleware`
> **Summary**: 基于响应状态和 meta-refresh 标签处理重定向

**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`

**Inheritance**: `RedirectMiddleware` → `BaseRedirectMiddleware`

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `process_response(request: Request, response: Response, spider: Spider | None = None)` | `Request | Response` | 处理响应并决定是否重定向 |

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

---

### `MetaRefreshMiddleware`
> **Summary**: 处理 HTML meta refresh 标签的重定向中间件

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
| `process_response(request: Request, response: Response, spider: Spider | None = None)` | `Request | Response` | 处理响应并决定是否重定向 |

##### `process_response`

```python
process_response(request: Request, response: Response, spider: Spider | None = None) -> Request | Response
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `request` | `Request` | 请求对象 |
| `response` | `Response` | 响应对象 |
| `spider` | `Spider | None` | 爬虫实例 |

**Returns**: `Request | Response