# scrapy/extensions

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
<td><code>ItemFilter</code></td>
<td>class</td>
<td>用于决定是否允许特定类型的 item 被导出到指定 feed</td>
</tr>
<tr>
<td><code>IFeedStorage</code></td>
<td>class</td>
<td>所有 Feed Storage 必须实现的接口</td>
</tr>
<tr>
<td><code>FeedStorageProtocol</code></td>
<td>class</td>
<td>用于类型提示的 FeedStorage 接口重写</td>
</tr>
<tr>
<td><code>BlockingFeedStorage</code></td>
<td>class</td>
<td>基于阻塞 I/O 的 Feed 存储实现</td>
</tr>
<tr>
<td><code>StdoutFeedStorage</code></td>
<td>class</td>
<td>将数据输出到标准输出的 Feed 存储</td>
</tr>
<tr>
<td><code>FileFeedStorage</code></td>
<td>class</td>
<td>将数据写入文件系统的 Feed 存储</td>
</tr>
<tr>
<td><code>S3FeedStorage</code></td>
<td>class</td>
<td>使用 Amazon S3 作为存储后端的 Feed 存储</td>
</tr>
<tr>
<td><code>GCSFeedStorage</code></td>
<td>class</td>
<td>使用 Google Cloud Storage 作为存储后端的 Feed 存储</td>
</tr>
<tr>
<td><code>FTPFeedStorage</code></td>
<td>class</td>
<td>使用 FTP 作为存储后端的 Feed 存储</td>
</tr>
<tr>
<td><code>FeedSlot</code></td>
<td>class</td>
<td>管理并发导出任务的资源分配</td>
</tr>
<tr>
<td><code>FeedExporter</code></td>
<td>class</td>
<td>协调数据导出流程的核心组件</td>
</tr>
<tr>
<td><code>DummyPolicy</code></td>
<td>class</td>
<td>不缓存任何响应的 HTTP 缓存策略</td>
</tr>
<tr>
<td><code>RFC2616Policy</code></td>
<td>class</td>
<td>实现 RFC 2616 缓存策略的 HTTP 缓存策略</td>
</tr>
<tr>
<td><code>DbmCacheStorage</code></td>
<td>class</td>
<td>使用 DBM 数据库存储 HTTP 缓存的实现</td>
</tr>
<tr>
<td><code>FilesystemCacheStorage</code></td>
<td>class</td>
<td>使用文件系统存储 HTTP 缓存的实现</td>
</tr>
<tr>
<td><code>parse_cachecontrol</code></td>
<td>function</td>
<td>解析 Cache-Control 头部</td>
</tr>
<tr>
<td><code>rfc1123_to_epoch</code></td>
<td>function</td>
<td>将 RFC 1123 格式的日期转换为 Unix 时间戳</td>
</tr>
<tr>
<td><code>GzipPlugin</code></td>
<td>class</td>
<td>使用 gzip 压缩数据的插件</td>
</tr>
<tr>
<td><code>Bz2Plugin</code></td>
<td>class</td>
<td>使用 bz2 压缩数据的插件</td>
</tr>
<tr>
<td><code>LZMAPlugin</code></td>
<td>class</td>
<td>使用 LZMA 压缩数据的插件</td>
</tr>
<tr>
<td><code>PostProcessingManager</code></td>
<td>class</td>
<td>管理导出后处理插件的管理器</td>
</tr>
<tr>
<td><code>CloseSpider</code></td>
<td>class</td>
<td>控制爬虫关闭行为的扩展</td>
</tr>
<tr>
<td><code>MemoryUsage</code></td>
<td>class</td>
<td>监控内存使用情况的扩展</td>
</tr>
<tr>
<td><code>PeriodicLog</code></td>
<td>class</td>
<td>定期记录爬虫统计信息的扩展</td>
</tr>
<tr>
<td><code>AutoThrottle</code></td>
<td>class</td>
<td>自动节流控制扩展</td>
</tr>
<tr>
<td><code>TelnetConsole</code></td>
<td>class</td>
<td>提供 Telnet 控制台的扩展</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.extensions` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/extensions/__init__.py` (`1` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及 FeedExporter、多种存储后端（如 S3、GCS、FTP）及过滤机制等，用于控制数据导出行为和存储方式。它包含用于管理 HTTP 缓存策略和存储的类，以及支持压缩后处理的插件。此外，还包含控制爬虫关闭、内存使用监控和定期日志记录等功能的扩展。
</div>


---

## 类参考

### `ItemFilter`
<!-- api: class | visibility: public | source: scrapy/extensions/feedexport.py:55 -->
> **Summary**: 用于决定是否允许特定类型的 item 被导出到指定 feed
**Type**: `<class>` | **Module**: `scrapy.extensions.feedexport`
#### 字段
<div class="api-table-container api-fields-table" markdown="0">
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>默认值</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>feed_options</code></td>
<td>dict[str, Any]</td>
<td>None</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>item_classes</code></td>
<td><code>tuple[type, ...]</code></td>
<td><code>()</code></td>
<td>允许导出的 item 类型</td>
</tr>
</tbody>
</table>
</div>
#### 构造方法
```python
ItemFilter(feed_options: dict[str, Any] | None)
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
<td><code>feed_options</code></td>
<td>dict[str, Any]</td>
<td>None</td>
</tr>
</tbody>
</table>
</div>

---
### `IFeedStorage`
<!-- api: class | visibility: public | source: scrapy/extensions/feedexport.py:91 -->
> **Summary**: 所有 Feed Storage 必须实现的接口
**Type**: `<


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>