# scrapy/http

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
<td><code>CookieJar</code></td>
<td>class</td>
<td>管理 HTTP cookie 的类</td>
</tr>
<tr>
<td><code>Headers</code></td>
<td>class</td>
<td>HTTP 请求头的大小写不敏感字典</td>
</tr>
<tr>
<td><code>Request</code></td>
<td>class</td>
<td>表示一个 HTTP 请求</td>
</tr>
<tr>
<td><code>Response</code></td>
<td>class</td>
<td>表示一个 HTTP 响应</td>
</tr>
<tr>
<td><code>TextResponse</code></td>
<td>class</td>
<td>表示一个文本类型的 HTTP 响应</td>
</tr>
<tr>
<td><code>FormRequest</code></td>
<td>class</td>
<td>表示一个表单提交的 HTTP 请求</td>
</tr>
<tr>
<td><code>JsonRequest</code></td>
<td>class</td>
<td>表示一个 JSON 数据的 HTTP 请求</td>
</tr>
<tr>
<td><code>XmlRpcRequest</code></td>
<td>class</td>
<td>表示一个 XML-RPC 的 HTTP 请求</td>
</tr>
<tr>
<td><code>VerboseCookie</code></td>
<td>class</td>
<td>定义 cookie 字典结构的类型提示</td>
</tr>
<tr>
<td><code>NO_CALLBACK</code></td>
<td>function</td>
<td>用于标记请求不需要回调函数</td>
</tr>
<tr>
<td><code>potential_domain_matches</code></td>
<td>function</td>
<td>判断域名是否匹配</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.http` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/http/__init__.py` (`1` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及 HTTP 请求与响应的定义、管理与处理，包含 `Request` 和 `Response` 类及其子类，用于表示和操作爬虫中的 HTTP 交互。它还包含用于处理 cookie 的 `CookieJar` 类，以及封装请求与响应对象以适配 cookie 管理的 `WrappedRequest` 和 `WrappedResponse` 类。此外，模块中定义了 `Headers` 类用于处理 HTTP 请求头，以及 `VerboseCookie` 类用于类型提示。模块中还包含 `FormRequest`、`JsonRequest` 和 `XmlRpcRequest` 等用于特定类型请求的子类。这些类共同构成了 Scrapy 中处理 HTTP 请求与响应的核心结构。
</div>


---

## 类参考

### `CookieJar`
> **Summary**: 管理 HTTP cookie 的类
**Type**: `<class>` | **Module**: `scrapy.http`
**Inheritance**: `CookieJar` → `object`
**Typical Usage**:
```python
jar = CookieJar()
jar.extract_cookies(response, request)
jar.add_cookie_header(request)
```
#### 构造方法
```python
CookieJar(policy: CookiePolicy | None = None, check_expired_frequency: int = 10000)
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
<td><code>policy</code></td>
<td>CookiePolicy</td>
<td>None</td>
</tr>
<tr>
<td><code>check_expired_frequency</code></td>
<td><code>int</code></td>
<td>检查过期 cookie 的频率</td>
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
<td><code>extract_cookies(response: Response, request: Request)</code></td>
<td><code>None</code></td>
<td>从响应中提取 cookie</td>
</tr>
<tr>
<td><code>add_cookie_header(request: Request)</code></td>
<td><code>None</code></td>
<td>为请求添加 cookie 头</td>
</tr>
</tbody>
</table>
</div>

---
### `Headers`
> **Summary**: HTTP 请求头的大小写不敏感字典
**Type**: `<class>` | **Module**: `scrapy.http`
**Inheritance**: `Headers` → `CaselessDict`
### `Request`
> **Summary**: 表示一个 HTTP 请求
**Type**: `<class>` | **Module**: `scrapy.http`
**Inheritance**: `Request` → `object`


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>