# scrapy/utils

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
<td><code>CaselessDict</code></td>
<td>class</td>
<td>大小写不敏感字典，已废弃</td>
</tr>
<tr>
<td><code>CaseInsensitiveDict</code></td>
<td>class</td>
<td>大小写不敏感字典，支持字符串或字节键</td>
</tr>
<tr>
<td><code>LocalCache</code></td>
<td>class</td>
<td>有限大小的缓存字典，旧项优先过期</td>
</tr>
<tr>
<td><code>LocalWeakReferencedCache</code></td>
<td>class</td>
<td>弱引用缓存字典，有限大小</td>
</tr>
<tr>
<td><code>SequenceExclude</code></td>
<td>class</td>
<td>序列排除工具类</td>
</tr>
<tr>
<td><code>_AsyncCooperatorAdapter</code></td>
<td>class</td>
<td>异步协程适配器</td>
</tr>
<tr>
<td><code>defer_fail</code></td>
<td>function</td>
<td>延迟失败的延迟对象</td>
</tr>
<tr>
<td><code>defer_succeed</code></td>
<td>function</td>
<td>延迟成功的延迟对象</td>
</tr>
<tr>
<td><code>mustbe_deferred</code></td>
<td>function</td>
<td>确保返回值为延迟对象</td>
</tr>
<tr>
<td><code>is_listlike</code></td>
<td>function</td>
<td>判断是否为列表类对象</td>
</tr>
<tr>
<td><code>to_unicode</code></td>
<td>function</td>
<td>字节转 Unicode</td>
</tr>
<tr>
<td><code>to_bytes</code></td>
<td>function</td>
<td>Unicode 转字节</td>
</tr>
<tr>
<td><code>MutableChain</code></td>
<td>class</td>
<td>可变链式迭代器</td>
</tr>
<tr>
<td><code>MutableAsyncChain</code></td>
<td>class</td>
<td>可变异步链式迭代器</td>
</tr>
<tr>
<td><code>TopLevelFormatter</code></td>
<td>class</td>
<td>日志格式化器</td>
</tr>
<tr>
<td><code>StreamLogger</code></td>
<td>class</td>
<td>日志流重定向器</td>
</tr>
<tr>
<td><code>LogCounterHandler</code></td>
<td>class</td>
<td>日志计数处理器</td>
</tr>
<tr>
<td><code>SpiderLoggerAdapter</code></td>
<td>class</td>
<td>爬虫日志适配器</td>
</tr>
<tr>
<td><code>failure_to_exc_info</code></td>
<td>function</td>
<td>异常信息转换</td>
</tr>
<tr>
<td><code>configure_logging</code></td>
<td>function</td>
<td>日志配置</td>
</tr>
<tr>
<td><code>install_scrapy_root_handler</code></td>
<td>function</td>
<td>安装 Scrapy 根处理器</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.utils` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/utils/datatypes.py` (`196` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及多个工具类和函数，主要提供数据结构、异步处理、日志管理等基础功能。其中包含大小写不敏感字典、有限缓存、异步延迟处理、日志格式化等组件。这些工具类和函数被 Scrapy 的核心模块广泛使用，例如在请求处理、响应解析、缓存机制和日志系统中。
</div>


---

## 类参考

### `CaselessDict`
> **Summary**: 大小写不敏感字典，已废弃，建议使用 `CaseInsensitiveDict`。
**Type**: `<class>` | **Module**: `scrapy.utils.datatypes`
**Inheritance**: `CaselessDict` → `dict`
**See Also**: `CaseInsensitiveDict`
**Typical Usage**:
```python
from scrapy.utils.datatypes import CaselessDict
```
#### 构造方法
```python
CaselessDict(*args, **kwargs)
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
<td><code>*args</code></td>
<td><code>Any</code></td>
<td>任意参数</td>
</tr>
<tr>
<td><code>**kwargs</code></td>
<td><code>Any</code></td>
<td>任意关键字参数</td>
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
<td><code>__new__(cls, *args, **kwargs)</code></td>
<td><code>Self</code></td>
<td>构造函数，带废弃警告</td>
</tr>
<tr>
<td><code>__init__(self, *args, **kwargs)</code></td>
<td><code>None</code></td>
<td>初始化方法</td>
</tr>
</tbody>
</table>
</div>

---
### `CaseInsensitiveDict`
> **Summary**: 大小写不敏感字典，支持字符串或字节键。
**Type**: `<class>` | **Module**: `scrapy.utils.datatypes`
**Inheritance**: `CaseInsensitiveDict` → `collections.UserDict[str | bytes, Any]`
**Typical Usage**:
```python
from scrapy.utils.datatypes import CaseInsensitiveDict
d = CaseInsensitiveDict({'key': 'value'})
print(d['KEY'])  # 输出 'value'
```
#### 字段
| 名称  | 类型  |


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>