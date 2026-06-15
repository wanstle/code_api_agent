# tests

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
<td><code>FromCrawlerMixin</code></td>
<td>class</td>
<td>测试用例中用于验证 from_crawler 方法是否被调用的混合类</td>
</tr>
<tr>
<td><code>FromCrawlerCsvItemExporter</code></td>
<td>class</td>
<td>继承自 CsvItemExporter 和 FromCrawlerMixin 的测试类</td>
</tr>
<tr>
<td><code>FromCrawlerFileFeedStorage</code></td>
<td>class</td>
<td>继承自 FileFeedStorage 和 FromCrawlerMixin 的测试类</td>
</tr>
<tr>
<td><code>DummyBlockingFeedStorage</code></td>
<td>class</td>
<td>模拟阻塞存储器的测试类</td>
</tr>
<tr>
<td><code>FailingBlockingFeedStorage</code></td>
<td>class</td>
<td>模拟失败存储器的测试类</td>
</tr>
<tr>
<td><code>LogOnStoreFileStorage</code></td>
<td>class</td>
<td>在存储时记录日志的测试类</td>
</tr>
<tr>
<td><code>TestFeedExportBase</code></td>
<td>class</td>
<td>FeedExport 功能测试的基础类</td>
</tr>
<tr>
<td><code>InstrumentedFeedSlot</code></td>
<td>class</td>
<td>用于监控 FeedSlot 的测试类</td>
</tr>
<tr>
<td><code>IsExportingListener</code></td>
<td>class</td>
<td>监听导出状态的测试类</td>
</tr>
<tr>
<td><code>ExceptionJsonItemExporter</code></td>
<td>class</td>
<td>抛出异常的 JsonItemExporter 测试类</td>
</tr>
<tr>
<td><code>TestFeedExport</code></td>
<td>class</td>
<td>FeedExport 功能的测试类</td>
</tr>
<tr>
<td><code>TestFeedExporterSignals</code></td>
<td>class</td>
<td>测试 FeedExporter 信号的类</td>
</tr>
<tr>
<td><code>TestFeedExportInit</code></td>
<td>class</td>
<td>测试 FeedExport 初始化的类</td>
</tr>
<tr>
<td><code>path_to_url</code></td>
<td>function</td>
<td>将路径转换为 URL 的辅助函数</td>
</tr>
<tr>
<td><code>printf_escape</code></td>
<td>function</td>
<td>对字符串进行 printf 转义的辅助函数</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `tests` &nbsp;|&nbsp; <strong>Source</strong>: `tests/test_feedexport.py` (`1404` lines)</div>

<div class="api-module-overview" markdown="1">
该模块涉及多个测试用例和测试工具类，主要用于验证 Scrapy 中 FeedExport 功能的实现逻辑。测试内容包括导出器（exporter）和存储器（storage）的初始化、异常处理、信号触发等。此外，还包含对爬虫设置、下载器处理、爬虫运行器等模块的测试逻辑，以确保其在不同场景下的行为符合预期。
</div>


---

## 类参考

### `FromCrawlerMixin`
> **Summary**: 用于测试 from_crawler 方法是否被调用的混合类
**Type**: `class` | **Module**: `tests`
**Inheritance**: `FromCrawler


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>