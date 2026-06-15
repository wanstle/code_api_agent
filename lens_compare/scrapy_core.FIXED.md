# Module: scrapy/core
> **Package**: `scrapy.core` | **Source**: `scrapy/core/downloader/handlers/http11.py` (`739` lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `_ResultT` | class | HTTP11 下载处理器返回值的类型定义 |
| `HTTP11DownloadHandler` | class | HTTP/1.1 下载处理器实现 |
| `TunnelError` | class | 代理隧道连接失败异常 |
| `_TunnelingTCP4ClientEndpoint` | class | 支持隧道的 TCP 客户端端点 |
| `_TunnelingAgent` | class | 支持隧道的 HTTP 代理 |
| `_ScrapyProxyAgent` | class | Scrapy 代理代理类 |
| `_ScrapyAgent` | class | Scrapy 核心 HTTP 代理 |
| `_RequestBodyProducer` | class | 请求体生产者 |
| `_ResponseReader` | class | 响应读取器 |
| `_tunnel_request_data` | function | 隧道请求数据处理函数 |
| `InvalidNegotiatedProtocol` | class | HTTP/2 协议协商失败异常 |
| `RemoteTerminatedConnection` | class | 远程连接终止异常 |
| `MethodNotAllowed405` | class | HTTP 405 方法不允许异常 |
| `_Slot` | class | 引擎中的任务槽 |
| `ExecutionEngine` | class | Scrapy 引擎主类 |
| `Slot` | class | 爬虫任务槽 |
| `Scraper` | class | 爬虫处理核心 |
| `BaseSchedulerMeta` | class | 调度器元类 |
| `BaseScheduler` | class | 调度器基类 |
| `Scheduler` | class | 默认调度器实现 |
| `InactiveStreamClosed` | class | HTTP/2 流未激活关闭异常 |
| `InvalidHostname` | class | HTTP/2 无效主机名异常 |
| `StreamCloseReason` | class | HTTP/2 流关闭原因 |
| `Stream` | class | HTTP/2 流对象 |

---

## 模块概述

本模块是 Scrapy 爬虫框架的核心引擎与调度模块，负责管理爬虫的运行流程、请求调度、下载处理及数据抓取等关键功能。它作为 Scrapy 架构的中心枢纽，协调各个组件之间的交互，包括下载器、调度器、爬虫处理器等。该模块被 `scrapy/crawler.py` 和 `scrapy/commands/parse.py` 等模块调用，依赖于 `scrapy/settings` 和 `scrapy/http` 模块提供的配置与 HTTP 支持。其职责边界在于控制爬虫生命周期、任务分发和数据流转，不直接处理具体业务逻辑。

---

## 类参考

### `_ResultT`
<!-- api: class | visibility: public | source: scrapy/core/downloader/handlers/http11.py:76 -->

> **Summary**: 定义 HTTP11 下载处理器返回值的结构化类型

**Type**: `<class>` | **Module**: `scrapy.core`

#### 字段

| 名称 | 类型 | 默认值 | 描述 |
|------|------|---------|-------------|
| `txresponse` | `TxResponse` | `None` | Twisted 响应对象 |
| `body` | `NotRequired[bytes]` | `None` | 响应体内容 |
| `flags` | `NotRequired[list[str] | None]` | `None` | 标志位列表 |
| `certificate` | `NotRequired[ssl.Certificate | None]` | `None` | SSL 证书 |
| `ip_address` | `NotRequired[ipaddress.IPv4Address | ipaddress.IPv6Address | None]` | `None` | IP 地址 |
| `stop_download` | `NotRequired[StopDownload | None]` | `None` | 停止下载标志 |

---

### `HTTP11DownloadHandler`
<!-- api: class | visibility: public | source: scrapy/core/downloader/handlers/http11.py:85 -->

> **Summary**: 实现 HTTP/1.1 协议的下载处理器

**Type**: `<class>` | **Module**: `scrapy.core`  
**Inheritance**: `HTTP11DownloadHandler` → `BaseHttpDownloadHandler`

**Typical Usage**:
```python
handler = HTTP11DownloadHandler(crawler)
```

#### 构造方法

```python
HTTP11DownloadHandler(crawler: Crawler)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `crawler` | `Crawler` | 爬虫实例 |

**Raises**: `NotConfigured` — 当未启用 Twisted reactor 时。

---

### `TunnelError`
<!-- api: class | visibility: public | source: scrapy/core/downloader/handlers/http11.py:161 -->

> **Summary**: 代理隧道连接失败时抛出的异常

**Type**: `<class>` | **Module**: `scrapy.core`

---

### `_TunnelingTCP4ClientEndpoint`
<!-- api: class | visibility: public | source: scrapy/core/downloader/handlers/http11.py:165 -->

> **Summary**: 支持 HTTP CONNECT 隧道的 TCP 客户端端点

**Type**: `<class>` | **Module**: `sc