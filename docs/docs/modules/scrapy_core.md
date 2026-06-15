# scrapy/core

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
<td><code>_ResultT</code></td>
<td>class</td>
<td>用于描述下载结果的结构化数据类型</td>
</tr>
<tr>
<td><code>HTTP11DownloadHandler</code></td>
<td>class</td>
<td>HTTP/1.1 下载处理器</td>
</tr>
<tr>
<td><code>TunnelError</code></td>
<td>class</td>
<td>代理隧道连接失败异常</td>
</tr>
<tr>
<td><code>_TunnelingTCP4ClientEndpoint</code></td>
<td>class</td>
<td>隧道 TCP 客户端端点</td>
</tr>
<tr>
<td><code>_TunnelingAgent</code></td>
<td>class</td>
<td>隧道代理</td>
</tr>
<tr>
<td><code>_ScrapyProxyAgent</code></td>
<td>class</td>
<td>Scrapy 代理代理</td>
</tr>
<tr>
<td><code>_ScrapyAgent</code></td>
<td>class</td>
<td>Scrapy 下载代理</td>
</tr>
<tr>
<td><code>_RequestBodyProducer</code></td>
<td>class</td>
<td>请求体生产者</td>
</tr>
<tr>
<td><code>_ResponseReader</code></td>
<td>class</td>
<td>响应读取器</td>
</tr>
<tr>
<td><code>_tunnel_request_data</code></td>
<td>function</td>
<td>隧道请求数据生成函数</td>
</tr>
<tr>
<td><code>InvalidNegotiatedProtocol</code></td>
<td>class</td>
<td>HTTP/2 协议协商失败异常</td>
</tr>
<tr>
<td><code>RemoteTerminatedConnection</code></td>
<td>class</td>
<td>远程连接终止异常</td>
</tr>
<tr>
<td><code>MethodNotAllowed405</code></td>
<td>class</td>
<td>HTTP/2 405 方法不允许异常</td>
</tr>
<tr>
<td><code>H2ClientProtocol</code></td>
<td>class</td>
<td>HTTP/2 客户端协议</td>
</tr>
<tr>
<td><code>H2ClientFactory</code></td>
<td>class</td>
<td>HTTP/2 客户端工厂</td>
</tr>
<tr>
<td><code>_Slot</code></td>
<td>class</td>
<td>引擎中的任务槽</td>
</tr>
<tr>
<td><code>ExecutionEngine</code></td>
<td>class</td>
<td>Scrapy 执行引擎</td>
</tr>
<tr>
<td><code>Slot</code></td>
<td>class</td>
<td>爬虫任务槽</td>
</tr>
<tr>
<td><code>Scraper</code></td>
<td>class</td>
<td>爬虫组件</td>
</tr>
<tr>
<td><code>BaseSchedulerMeta</code></td>
<td>class</td>
<td>调度器元类</td>
</tr>
<tr>
<td><code>BaseScheduler</code></td>
<td>class</td>
<td>基础调度器</td>
</tr>
<tr>
<td><code>Scheduler</code></td>
<td>class</td>
<td>默认调度器</td>
</tr>
<tr>
<td><code>InactiveStreamClosed</code></td>
<td>class</td>
<td>非活跃流关闭异常</td>
</tr>
<tr>
<td><code>InvalidHostname</code></td>
<td>class</td>
<td>无效主机名异常</td>
</tr>
<tr>
<td><code>StreamCloseReason</code></td>
<td>class</td>
<td>流关闭原因</td>
</tr>
<tr>
<td><code>Stream</code></td>
<td>class</td>
<td>HTTP/2 流</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.core` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/core/downloader/handlers/http11.py` (`739` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及 HTTP/1.1 和 HTTP/2 下载处理器、代理隧道支持、连接池管理等，提供基于 Twisted 的异步网络请求能力。它包含下载处理逻辑、HTTP/2 协议支持、调度器机制、引擎执行流程等核心组件，用于构建 Scrapy 爬虫系统的网络请求与任务调度部分。该模块被 `scrapy` 核心引擎调用，依赖 Twisted 异步框架实现高效并发请求处理。
</div>


---

## 类参考

### `_ResultT`
<!-- api: class | visibility: public | source: scrapy/core/downloader/handlers/http11.py:76 -->
> **Summary**: 用于描述下载结果的结构化数据类型
**Type**: `<class>` | **Module**: `scrapy.core`
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
<td><code>txresponse</code></td>
<td><code>TxResponse</code></td>
<td><code>(unknown)</code></td>
<td>Twisted 响应对象</td>
</tr>
<tr>
<td><code>body</code></td>
<td><code>NotRequired[bytes]</code></td>
<td><code>(unknown)</code></td>
<td>响应体</td>
</tr>
<tr>
<td><code>flags</code></td>
<td>NotRequired[list[str]</td>
<td>None]</td>
<td><code>(unknown)</code></td>
</tr>
<tr>
<td><code>certificate</code></td>
<td>NotRequired[ssl.Certificate</td>
<td>None]</td>
<td><code>(unknown)</code></td>
</tr>
<tr>
<td><code>ip_address</code></td>
<td>NotRequired[ipaddress.IPv4Address</td>
<td>ipaddress.IPv6Address</td>
<td>None]</td>
</tr>
<tr>
<td><code>stop_download</code></td>
<td>NotRequired[StopDownload</td>
<td>None]</td>
<td><code>(unknown)</code></td>
</tr>
</tbody>
</table>
</div>

---
### `HTTP11Download


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>