# tests/mockserver

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
<td><code>ForeverTakingResource</code></td>
<td>class</td>
<td>永不结束响应的测试资源</td>
</tr>
<tr>
<td><code>HostHeaderResource</code></td>
<td>class</td>
<td>返回请求 Host 头部值的测试资源</td>
</tr>
<tr>
<td><code>ClientIPResource</code></td>
<td>class</td>
<td>返回请求客户端 IP 地址的测试资源</td>
</tr>
<tr>
<td><code>PayloadResource</code></td>
<td>class</td>
<td>返回指定负载内容的测试资源</td>
</tr>
<tr>
<td><code>LeafResource</code></td>
<td>class</td>
<td>叶子资源，返回固定内容</td>
</tr>
<tr>
<td><code>Follow</code></td>
<td>class</td>
<td>模拟跟随重定向的资源</td>
</tr>
<tr>
<td><code>Delay</code></td>
<td>class</td>
<td>延迟响应的资源</td>
</tr>
<tr>
<td><code>Status</code></td>
<td>class</td>
<td>返回指定状态码的资源</td>
</tr>
<tr>
<td><code>Raw</code></td>
<td>class</td>
<td>返回原始请求内容的资源</td>
</tr>
<tr>
<td><code>Echo</code></td>
<td>class</td>
<td>回显请求内容的资源</td>
</tr>
<tr>
<td><code>RedirectTo</code></td>
<td>class</td>
<td>重定向到指定 URL 的资源</td>
</tr>
<tr>
<td><code>Partial</code></td>
<td>class</td>
<td>返回部分数据的资源</td>
</tr>
<tr>
<td><code>Drop</code></td>
<td>class</td>
<td>模拟连接中断的资源</td>
</tr>
<tr>
<td><code>ArbitraryLengthPayloadResource</code></td>
<td>class</td>
<td>返回任意长度负载的资源</td>
</tr>
<tr>
<td><code>NoMetaRefreshRedirect</code></td>
<td>class</td>
<td>不包含 meta refresh 的重定向资源</td>
</tr>
<tr>
<td><code>ContentLengthHeaderResource</code></td>
<td>class</td>
<td>返回指定 Content-Length 头部的资源</td>
</tr>
<tr>
<td><code>ChunkedResource</code></td>
<td>class</td>
<td>返回分块传输编码内容的资源</td>
</tr>
<tr>
<td><code>BrokenChunkedResource</code></td>
<td>class</td>
<td>返回损坏分块传输编码的资源</td>
</tr>
<tr>
<td><code>BrokenDownloadResource</code></td>
<td>class</td>
<td>模拟下载中断的资源</td>
</tr>
<tr>
<td><code>EmptyContentTypeHeaderResource</code></td>
<td>class</td>
<td>返回空 Content-Type 头部的资源</td>
</tr>
<tr>
<td><code>LargeChunkedFileResource</code></td>
<td>class</td>
<td>返回大分块文件的资源</td>
</tr>
<tr>
<td><code>DuplicateHeaderResource</code></td>
<td>class</td>
<td>返回重复头部的资源</td>
</tr>
<tr>
<td><code>UriResource</code></td>
<td>class</td>
<td>返回请求 URI 的资源</td>
</tr>
<tr>
<td><code>ResponseHeadersResource</code></td>
<td>class</td>
<td>返回响应头部的资源</td>
</tr>
<tr>
<td><code>Compress</code></td>
<td>class</td>
<td>返回压缩内容的资源</td>
</tr>
<tr>
<td><code>SetCookie</code></td>
<td>class</td>
<td>设置 Cookie 的资源</td>
</tr>
<tr>
<td><code>getarg</code></td>
<td>function</td>
<td>获取 URL 参数的函数</td>
</tr>
<tr>
<td><code>close_connection</code></td>
<td>function</td>
<td>关闭连接的函数</td>
</tr>
<tr>
<td><code>BaseMockServer</code></td>
<td>class</td>
<td>Mock 服务器基础类</td>
</tr>
<tr>
<td><code>main_factory</code></td>
<td>function</td>
<td>创建主函数工厂</td>
</tr>
<tr>
<td><code>main</code></td>
<td>function</td>
<td>主运行函数</td>
</tr>
<tr>
<td><code>print_listening</code></td>
<td>function</td>
<td>打印监听地址</td>
</tr>
<tr>
<td><code>MockDNSResolver</code></td>
<td>class</td>
<td>模拟 DNS 解析器</td>
</tr>
<tr>
<td><code>MockDNSServer</code></td>
<td>class</td>
<td>模拟 DNS 服务器</td>
</tr>
<tr>
<td><code>MockFTPServer</code></td>
<td>class</td>
<td>模拟 FTP 服务器</td>
</tr>
<tr>
<td><code>Root</code></td>
<td>class</td>
<td>根资源类</td>
</tr>
<tr>
<td><code>SimpleMockServer</code></td>
<td>class</td>
<td>简单 HTTPS Mock 服务器</td>
</tr>
<tr>
<td><code>MockServer</code></td>
<td>class</td>
<td>HTTP Mock 服务器</td>
</tr>
<tr>
<td><code>MitmProxy</code></td>
<td>class</td>
<td>MITM 代理类</td>
</tr>
<tr>
<td><code>wrong_credentials</code></td>
<td>function</td>
<td>返回错误认证信息的函数</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `tests.mockserver` &nbsp;|&nbsp; <strong>Source</strong>: `tests/mockserver/http_resources.py` (`381` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及用于构建 HTTP 测试服务器和模拟各种 HTTP 响应行为的资源类与基础框架等。它包含多个用于测试不同 HTTP 行为的资源类，如 `ForeverTakingResource`、`HostHeaderResource`、`ClientIPResource` 等，以及基础的 `BaseMockServer` 类，用于启动和管理测试服务器。此外，还包含 DNS 和 FTP 的模拟服务器实现，以及用于测试代理行为的 `MitmProxy` 类。
</div>


---

## 类参考

### `ForeverTakingResource`
> **Summary**: 永不结束响应的测试资源
**Type**: `class` | **Module**: `tests.mockserver.http_resources`
**Inheritance**: `ForeverTakingResource` → `resource.Resource`
#### 构造方法
```python
ForeverTakingResource(write: bool = False)
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
<td><code>write</code></td>
<td><code>bool</code></td>
<td>是否写入初始数据</td>
</tr>
</tbody>
</table>
</div>
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
<td><code>render(request)</code></td>
<td><code>bytes</code></td>
<td>渲染请求，永不结束响应</td>
</tr>
</tbody>
</table>
</div>
##### `render`
```python
render(request) -> bytes
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
<td><code>request</code></td>
<td><code>Request</code></td>
<td>HTTP 请求对象</td>
</tr><tr class="api-returns-row"><td><strong>Returns</strong></td><td><code>bytes</code></td><td>返回 `server.NOT_DONE_YET` 表示响应未完成</td></tr>
</tbody>
</table>
</div>

---
### `HostHeaderResource`
> **Summary**: 返回请求 Host 头部值的测试资源
**Type**: `class` | **Module**: `tests.mockserver.http_resources`
**Inheritance**: `HostHeaderResource` → `resource.Resource`


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>