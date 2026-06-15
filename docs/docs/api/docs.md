# API 参考:`docs`

## `docs/conftest.py`

<a id="sym-docs_conftest.py-17"></a>

### `load_response` · func
```python
def load_response(url: str, filename: str) -> HtmlResponse
```

从文件加载响应内容并返回 HtmlResponse 对象。

**Parameters**
- `url` (str): 响应的 URL 地址。
- `filename` (str): 要加载的文件名。

**Returns**
- `HtmlResponse`: 包含从文件读取的响应体的 HtmlResponse 对象。

**Raises**
- (unknown)

**内部调用(库内):**
- [`HtmlResponse`](scrapy_http.md#sym-scrapy_http_response_html.py-11)

*来源: `docs/conftest.py:17`*

---
<a id="sym-docs_conftest.py-22"></a>

### `setup` · func
```python
def setup(namespace)
```

设置命名空间，添加 `load_response` 函数。

**Parameters**
- `namespace` (dict): 用于存储 `load_response` 函数的命名空间字典。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `docs/conftest.py:22`*

---