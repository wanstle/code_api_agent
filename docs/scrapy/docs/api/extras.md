# API 参考:`extras`

## `extras/qps-bench-server.py`

<a id="sym-extras_qps-bench-server.py-10"></a>

### `Root` · class
```python
class Root(Resource)
```

`Root` 类代表 Scrapy 项目的根资源，用于处理 HTTP 请求并提供统计信息的访问接口。

### 关键方法

- **`__init__(self)`**  
  初始化 `Root` 实例，设置其作为资源树的根节点。

- **`_reset_stats(self)`**  
  重置当前爬虫的统计信息。

- **`getChild(self, path, request)`**  
  根据请求路径获取子资源，通常用于处理嵌套路由。

- **`render(self, request)`**  
  渲染请求对应的响应内容，通常是返回 JSON 格式的统计信息。

- **`_finish(self, request)`**  
  完成请求处理并关闭连接。

*来源: `extras/qps-bench-server.py:10`*

---
<a id="sym-extras_qps-bench-server.py-11"></a>

### `Root.__init__` · method
```python
def __init__(self)
```

初始化 Root 实例，设置并发计数、尾部队列和重置统计信息。

**Parameters**
- `self` - Root 类实例

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`Root._reset_stats`](extras.md#sym-extras_qps-bench-server.py-17) — 重置统计相关的时间和标记。

*来源: `extras/qps-bench-server.py:11`*

---
<a id="sym-extras_qps-bench-server.py-17"></a>

### `Root._reset_stats` · method
```python
def _reset_stats(self)
```

重置统计相关的时间和标记。

**Parameters**
- `self` - 该方法属于 `Root` 类的实例。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `extras/qps-bench-server.py:17`*

---
<a id="sym-extras_qps-bench-server.py-21"></a>

### `Root.getChild` · method
```python
def getChild(self, path, request)
```

获取当前资源的子资源。

**Parameters**
- `path` - 路径
- `request` - 请求对象

**Returns**
- 当前实例本身

**Raises**
- (unknown)

*来源: `extras/qps-bench-server.py:21`*

---
<a id="sym-extras_qps-bench-server.py-24"></a>

### `Root.render` · method
```python
def render(self, request)
```

用途:处理请求并根据延迟和并发情况更新统计信息。

**Parameters**
- `request`: 请求对象，包含客户端参数。

**Returns**
- 返回空字符串或 `NOT_DONE_YET`（当存在 `latency` 参数时）。

**Raises**
- (unknown)

**内部调用(库内):**
- [`Root._reset_stats`](extras.md#sym-extras_qps-bench-server.py-17) — 重置统计相关的时间和标记。

*来源: `extras/qps-bench-server.py:24`*

---
<a id="sym-extras_qps-bench-server.py-52"></a>

### `Root._finish` · method
```python
def _finish(self, request)
```

结束请求并减少并发计数。

**Parameters**
- `request` - 要完成的请求对象

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `extras/qps-bench-server.py:52`*

---

## `extras/qpsclient.py`

<a id="sym-extras_qpsclient.py-15"></a>

### `QPSSpider` · class
```python
class QPSSpider(Spider)
```

QPSSpider 是一个继承自 Spider 的爬虫类，用于实现特定的网页抓取逻辑。

### 方法说明

- **`__init__(self, *a, **kw)`**  
  初始化方法，用于实例化 QPSSpider 对象，接受任意位置和关键字参数。

- **`start(self)`**  
  启动方法，负责启动爬虫的执行流程。

- **`parse(self, response)`**  
  解析方法，处理 HTTP 响应并提取数据，接收一个 `response` 参数。

*来源: `extras/qpsclient.py:15`*

---
<a id="sym-extras_qpsclient.py-29"></a>

### `QPSSpider.__init__` · method
```python
def __init__(self, *a, **kw)
```

初始化 QPSSpider 实例，并根据 qps 或 download_delay 属性设置下载延迟。

**Parameters**

- `*a` - 传递给父类构造函数的位置参数。
- `**kw` - 传递给父类构造函数的关键字参数。

**Returns**

(unknown)

**Raises**

(unknown)

*来源: `extras/qpsclient.py:29`*

---
<a id="sym-extras_qpsclient.py-37"></a>

### `QPSSpider.start` · method
```python
async def start(self)
```

用于异步启动爬虫，生成请求以访问指定 URL 并支持多槽位并发请求。

**Parameters**
- `self` - 爬虫实例

**Returns**
- `async_generator` - 生成器，产生 `Request` 对象

**Raises**
- (unknown)

**内部调用(库内):**
- [`Request`](scrapy_http.md#sym-scrapy_http_request___init__.py-84)

*来源: `extras/qpsclient.py:37`*

---
<a id="sym-extras_qpsclient.py-54"></a>

### `QPSSpider.parse` · method
```python
def parse(self, response)
```

用途:处理响应数据的解析方法。

**Parameters**
- `response` (scrapy.http.Response): 从网站获取的响应对象。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `extras/qpsclient.py:54`*

---