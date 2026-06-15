# scrapy

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
<td><code>Crawler</code></td>
<td>class</td>
<td>封装单个爬虫的配置与运行环境</td>
</tr>
<tr>
<td><code>CrawlerRunnerBase</code></td>
<td>class</td>
<td>提供爬虫运行器的核心逻辑与爬虫集合管理</td>
</tr>
<tr>
<td><code>CrawlerRunner</code></td>
<td>class</td>
<td>提供基于 Twisted 的 Deferred API 来运行爬虫</td>
</tr>
<tr>
<td><code>AsyncCrawlerRunner</code></td>
<td>class</td>
<td>提供异步协程 API 来运行爬虫</td>
</tr>
<tr>
<td><code>CrawlerProcessBase</code></td>
<td>class</td>
<td>提供爬虫进程运行的基础接口</td>
</tr>
<tr>
<td><code>CrawlerProcess</code></td>
<td>class</td>
<td>提供独立进程运行爬虫的能力</td>
</tr>
<tr>
<td><code>AsyncCrawlerProcess</code></td>
<td>class</td>
<td>提供异步协程方式运行爬虫的进程</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.crawler` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/crawler.py` (`1050` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及爬虫实例管理、运行器与进程控制等，提供爬虫启动、配置及生命周期管理等能力。它定义了 `Crawler` 类用于封装单个爬虫的配置与运行环境，`CrawlerRunnerBase` 作为基类提供爬虫运行器的核心逻辑与爬虫集合管理，`CrawlerRunner` 提供基于 Twisted 的 Deferred API 来运行爬虫，`CrawlerProcess` 提供独立进程运行爬虫的能力。这些类共同构成了 Scrapy 爬虫运行的核心机制。
</div>


---

## 类参考

### `Crawler`
> **Summary**: 封装单个爬虫的配置与运行环境
**Type**: `class` | **Module**: `scrapy.crawler`
**Inheritance**: `Crawler` → `object`
#### 构造方法
```python
Crawler(spidercls: type[Spider], settings: dict[str, Any] | Settings | None = None, init_reactor: bool = False)
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
<td><code>spidercls</code></td>
<td><code>type[Spider]</code></td>
<td>爬虫类</td>
</tr>
<tr>
<td><code>settings</code></td>
<td>dict[str, Any]</td>
<td>Settings</td>
</tr>
<tr>
<td><code>init_reactor</code></td>
<td><code>bool</code></td>
<td>是否初始化 reactor</td>
</tr>
</tbody>
</table>
</div>
**Raises**: `ValueError` — 当 `spidercls` 是一个实例而非类时。
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
<td><code>crawl(request_or_spidercls, **kwargs)</code></td>
<td><code>Deferred</code></td>
<td>启动爬虫任务</td>
</tr>
<tr>
<td><code>crawl_async(request_or_spidercls, **kwargs)</code></td>
<td><code>Coroutine</code></td>
<td>异步启动爬虫任务</td>
</tr>
<tr>
<td><code>get_downloader_middleware()</code></td>
<td><code>list</code></td>
<td>获取下载中间件</td>
</tr>
<tr>
<td><code>get_extension()</code></td>
<td><code>list</code></td>
<td>获取扩展</td>
</tr>
<tr>
<td><code>get_item_pipeline()</code></td>
<td><code>list</code></td>
<td>获取项目管道</td>
</tr>
<tr>
<td><code>get_spider_middleware()</code></td>
<td><code>list</code></td>
<td>获取爬虫中间件</td>
</tr>
<tr>
<td><code>start()</code></td>
<td><code>Deferred</code></td>
<td>启动爬虫</td>
</tr>
<tr>
<td><code>stop()</code></td>
<td><code>Deferred</code></td>
<td>停止爬虫</td>
</tr>
</tbody>
</table>
</div>

---
### `CrawlerRunnerBase`
> **Summary**: 提供爬虫运行器的核心逻辑与爬虫集合管理
**Type**: `class` | **Module**: `scrapy.crawler`
**Inheritance**: `CrawlerRunnerBase` → `object`


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>