# tests/AsyncCrawlerProcess

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
<td><code>UppercasePipeline</code></td>
<td>class</td>
<td>异步管道，用于将 URL 转换为大写</td>
</tr>
<tr>
<td><code>UrlSpider</code></td>
<td>class</td>
<td>使用 <code>UppercasePipeline</code> 的爬虫</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `tests.AsyncCrawlerProcess` &nbsp;|&nbsp; <strong>Source</strong>: `tests/AsyncCrawlerProcess/asyncio_deferred_signal.py` (`48` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及多个测试用例，用于验证异步爬虫进程中的协程管道、信号处理、反应器环境检测及主机名解析行为。这些测试场景主要围绕 `asyncio` 与 `Twisted` 反应器的集成使用，包括异步管道的初始化、爬虫启动流程、自定义设置、以及 DNS 解析行为的测试。例如，`UppercasePipeline` 展示了如何在异步环境中打开爬虫并处理数据项；`UrlSpider` 则演示了如何通过自定义设置启用该管道。
</div>


---

## 类参考

### `UppercasePipeline`
<!-- api: class | visibility: public | source: tests/AsyncCrawlerProcess/asyncio_deferred_signal.py:11 -->
> **Summary**: 异步管道，用于将 URL 转换为大写
**Type**: `<class>` | **Module**: `tests.AsyncCrawlerProcess`
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
<td><code>open_spider(spider)</code></td>
<td><code>Deferred</code></td>
<td>异步打开爬虫</td>
</tr>
<tr>
<td><code>process_item(item)</code></td>
<td><code>dict</code></td>
<td>处理项，将 URL 转换为大写</td>
</tr>
</tbody>
</table>
</div>
##### `open_spider`
```python
open_spider(spider)
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
<td><code>spider</code></td>
<td><code>Spider</code></td>
<td>爬虫实例</td>
</tr><tr class="api-returns-row"><td><strong>Returns</strong></td><td><code>Deferred</code></td><td>异步操作的延迟对象</td></tr>
</tbody>
</table>
</div>
##### `process_item`
```python
process_item(item)
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
<td><code>item</code></td>
<td><code>dict</code></td>
<td>输入项</td>
</tr><tr class="api-returns-row"><td><strong>Returns</strong></td><td><code>dict</code></td><td>处理后的项，URL 被转换为大写</td></tr>
</tbody>
</table>
</div>

---
### `UrlSpider`
<!-- api: class | visibility: public | source: tests/AsyncCrawlerProcess/asyncio_deferred_signal.py:23 -->
> **Summary**: 使用 `UppercasePipeline` 的爬虫
**Type**: `<class>` | **Module**: `tests.AsyncCrawlerProcess`
**Inheritance**: `UrlSpider` → `Spider`
#### 构造方法
```python
UrlSpider()
```
**See Also**: `UppercasePipeline`

---
### `ReactorCheckExtension`
<!-- api: class | visibility: public | source: tests/AsyncCrawlerProcess/asyncio_enabled_no_reactor.py:6 -->
> **Summary**: 检查是否启用了 asyncio 反应器的扩展类
**Type**: `<class>` | **Module**: `tests.AsyncCrawlerProcess`
### `NoRequestsSpider`
<!-- api: class | visibility: public | source: tests/AsyncCrawlerProcess/asyncio_enabled_no_reactor.py:12 -->
> **Summary**: 无请求的异步爬虫，用于测试反应器环境
**Type**: `<class>` | **Module**: `tests.AsyncCrawlerProcess`
### `CachingHostnameResolverSpider`
<!-- api: class | visibility: public | source: tests/AsyncCrawlerProcess/caching_hostname_resolver.py:7 -->
> **Summary**: 测试主机名解析缓存行为的爬虫
**Type**: `<class>` | **Module**: `tests.AsyncCrawlerProcess`
**Inheritance**: `CachingHostnameResolverSpider` →


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>