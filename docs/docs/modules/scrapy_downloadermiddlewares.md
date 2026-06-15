# scrapy/downloadermiddlewares

<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>

---

## 快速概览

<div class="api-table-container api-simple-table" markdown="0">
<table>
<thead>
<tr>
<th>符号</th>
<th>类型</th>
<th>概述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>BaseRedirectMiddleware</code></td>
<td>class</td>
<td>处理请求重定向的基础中间件类</td>
</tr>
<tr>
<td><code>RedirectMiddleware</code></td>
<td>class</td>
<td>基于响应状态码和 meta-refresh 标签处理重定向的中间件</td>
</tr>
<tr>
<td><code>MetaRefreshMiddleware</code></td>
<td>class</td>
<td>处理 HTML meta refresh 标签的重定向中间件</td>
</tr>
<tr>
<td><code>CookiesMiddleware</code></td>
<td>class</td>
<td>处理 Cookie 的中间件</td>
</tr>
<tr>
<td><code>HttpCompressionMiddleware</code></td>
<td>class</td>
<td>处理 HTTP 压缩（gzip, deflate）的中间件</td>
</tr>
<tr>
<td><code>HttpCacheMiddleware</code></td>
<td>class</td>
<td>处理 HTTP 缓存的中间件</td>
</tr>
<tr>
<td><code>OffsiteMiddleware</code></td>
<td>class</td>
<td>控制站点外请求的中间件</td>
</tr>
<tr>
<td><code>RobotsTxtMiddleware</code></td>
<td>class</td>
<td>处理 robots.txt 的中间件</td>
</tr>
<tr>
<td><code>DownloaderStats</code></td>
<td>class</td>
<td>下载器统计信息中间件</td>
</tr>
<tr>
<td><code>HttpProxyMiddleware</code></td>
<td>class</td>
<td>处理 HTTP 代理的中间件</td>
</tr>
<tr>
<td><code>_is_public_domain</code></td>
<td>function</td>
<td>判断域名是否为公共域</td>
</tr>
<tr>
<td><code>get_header_size</code></td>
<td>function</td>
<td>计算 HTTP 请求头大小</td>
</tr>
<tr>
<td><code>get_status_size</code></td>
<td>function</td>
<td>计算 HTTP 响应状态码大小</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.downloadermiddlewares` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/downloadermiddlewares/__init__.py` (`1` lines)</div>

<div class="api-module-overview" markdown="1">
本模块包含多个下载器中间件，用于处理请求和响应过程中的各种行为，如重定向、Cookie 管理、压缩处理、缓存、站点外请求控制、robots.txt 解析、统计信息收集等。这些中间件通过 Scrapy 的信号机制与引擎进行交互，支持通过配置项控制其行为。中间件类通常通过 `from_crawler` 类方法从爬虫配置中初始化，并在请求/响应处理阶段被调用。
</div>


---

## 类参考

### `BaseRedirectMiddleware`
> **Summary**: 处理请求重定向的基础中间件类
**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`
**Inheritance**: `BaseRedirectMiddleware` → `object`
#### 构造方法
```python
BaseRedirectMiddleware(settings: BaseSettings)
```
<div class="api-table-container api-fields-table" markdown="0">
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>settings</code></td>
<td><code>BaseSettings</code></td>
<td>Scrapy 配置对象</td>
</tr>
</tbody>
</table>
</div>
**Raises**: `NotConfigured` — 当 `REDIRECT_ENABLED` 设置为 `False` 时。
#### 方法
<div class="api-table-container api-methods-table" markdown="0">
<table>
<thead>
<tr>
<th>方法</th>
<th>返回值</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__init__(settings: BaseSettings)</code></td>
<td><code>None</code></td>
<td>初始化中间件并检查是否启用</td>
</tr>
<tr>
<td><code>from_crawler(crawler: Crawler)</code></td>
<td><code>Self</code></td>
<td>从爬虫实例创建中间件实例</td>
</tr>
</tbody>
</table>
</div>
##### `__init__`
```python
__init__(settings: BaseSettings)
```
<div class="api-table-container api-fields-table" markdown="0">
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>settings</code></td>
<td><code>BaseSettings</code></td>
<td>Scrapy 配置对象</td>
</tr>
</tbody>
</table>
</div>
**Raises**: `NotConfigured` — 当 `REDIRECT_ENABLED` 设置为 `False` 时。
##### `from_crawler`
```python
from_crawler(crawler: Crawler) -> Self
```
<div class="api-table-container api-fields-table" markdown="0">
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>crawler</code></td>
<td><code>Crawler</code></td>
<td>爬虫实例</td>
</tr><tr class="api-returns-row"><td><strong>Returns</strong></td><td><code>Self</code></td><td>中间件实例</td></tr>
</tbody>
</table>
</div>
**See Also**: `RedirectMiddleware`, `MetaRefreshMiddleware`

---
### `RedirectMiddleware`
> **Summary**: 基于响应状态码和 meta-refresh 标签处理重定向的中间件
**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`
**Inheritance**: `RedirectMiddleware` → `BaseRedirectMiddleware`
### `MetaRefreshMiddleware`
> **Summary**: 处理 HTML meta refresh 标签的重定向中间件
**Type**: `class` | **Module**: `scrapy.downloadermiddlewares.redirect`
**Inheritance**: `MetaRefreshMiddleware` → `BaseRedirectMiddleware`


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>