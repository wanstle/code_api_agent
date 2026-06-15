# Module: scrapy/core
> **Package**: `scrapy.core` | **Source**: `scrapy/core/downloader/handlers/http11.py` (`739` lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `_ResultT` | class | HTTP 下载结果的结构化类型定义 |
| `HTTP11DownloadHandler` | class | HTTP/1.1 协议下载处理器 |
| `TunnelError` | class | 代理隧道连接失败异常 |
| `_TunnelingTCP4ClientEndpoint` | class | 隧道 TCP 客户端端点 |
| `_TunnelingAgent` | class | 隧道代理 |
| `_ScrapyProxyAgent` | class | Scrapy 代理代理 |
| `_ScrapyAgent` | class | Scrapy 原生代理 |
| `_RequestBodyProducer` | class | 请求体生产者 |
| `_ResponseReader` | class | 响应读取器 |
| `_tunnel_request_data` | function | 隧道请求数据生成函数 |
| `InvalidNegotiatedProtocol` | class | HTTP/2 协议协商失败异常 |
| `RemoteTerminatedConnection` | class | HTTP/2 远程连接终止异常 |
| `MethodNotAllowed405` | class | HTTP/2 405 方法不允许异常 |
| `H2ClientProtocol` | class | HTTP/2 客户端协议 |
| `H2ClientFactory` | class | HTTP/2 客户端工厂 |
| `_Slot` | class | 引擎任务槽 |
| `ExecutionEngine` | class | Scrapy 执行引擎 |
| `Slot` | class | 爬虫任务槽 |
| `Scraper` | class | 爬虫组件 |
| `BaseSchedulerMeta` | class | 调度器元类 |
| `BaseScheduler` | class | 基础调度器 |
| `Scheduler` | class | 默认调度器 |
| `InactiveStreamClosed` | class | HTTP/2 非活跃流关闭异常 |
| `InvalidHostname` | class | HTTP/2 无效主机名异常 |
| `StreamCloseReason` | class | HTTP/2 流关闭原因 |
| `Stream` | class | HTTP/2 流 |

---

## 模块概述

本模块涉及 HTTP/1.1 和 HTTP/2 下载处理器、代理隧道支持、连接池管理等，提供基于 Twisted 的异步网络请求能力。它包含下载处理、连接管理、协议实现、调度和爬虫执行等核心组件，作为 Scrapy 网络请求与任务调度的核心层，被引擎模块调用，依赖 Twisted 异步框架和配置系统。

---

## 类参考

### `_ResultT`
<!-- api: class | visibility: public | source: scrapy/core/downloader/handlers/http11.py:76 -->

> **Summary**: HTTP 下载结果的结构化类型定义

**Type**: `class` | **Module**: `scrapy.core`

#### 字段

| 名称 | 类型 | 默认值 | 描述 |
|------|------|---------|-------------|
| `txresponse` | `TxResponse` | `(unknown)` | Twisted 响应对象 |
| `body` | `NotRequired[bytes]` | `(unknown)` | 响应体 |
| `flags` | `NotRequired[list[str] | None]` | `(unknown)` | 标志列表 |
| `certificate` | `NotRequired[ssl.Certificate | None]` | `(unknown)` | SSL 证书 |
| `ip_address` | `NotRequired[ipaddress.IPv4Address | ipaddress.IPv6Address | None]` | `(unknown)` | IP 地址 |
| `stop_download` | `NotRequired[StopDownload | None]` | `(unknown)` | 停止下载标志 |

---

### `HTTP11DownloadHandler`
<!-- api