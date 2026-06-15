# API 参考:`scrapy/selector`

## `scrapy/selector/unified.py`

<a id="sym-scrapy_selector_unified.py-21"></a>

### `_st` · func
```python
def _st(response: TextResponse | None, st: str | None) -> str
```

*来源: `scrapy/selector/unified.py:21` · 待生成*

---
<a id="sym-scrapy_selector_unified.py-27"></a>

### `_response_from_text` · func
```python
def _response_from_text(text: str | bytes, st: str | None) -> TextResponse
```

**内部调用(库内):**
- [`to_bytes`](scrapy_utils.md#sym-scrapy_utils_python.py-88)

*来源: `scrapy/selector/unified.py:27` · 待生成*

---
<a id="sym-scrapy_selector_unified.py-32"></a>

### `SelectorList` · class
```python
class SelectorList(_ParselSelector.selectorlist_cls, object_ref)
```

*来源: `scrapy/selector/unified.py:32` · 待生成*

---
<a id="sym-scrapy_selector_unified.py-39"></a>

### `Selector` · class
```python
class Selector(_ParselSelector, object_ref)
```

*来源: `scrapy/selector/unified.py:39` · 待生成*

---
<a id="sym-scrapy_selector_unified.py-74"></a>

### `Selector.__init__` · method
```python
def __init__(
        self,
        response: TextResponse | None = None,
        text: str | None = None,
        type: str | None = None,  # noqa: A002
        root: Any | None = _NOT_SET,
        **kwargs: Any,
    )
```

**内部调用(库内):**
- [`_st`](scrapy_selector.md#sym-scrapy_selector_unified.py-21)
- [`_response_from_text`](scrapy_selector.md#sym-scrapy_selector_unified.py-27)
- [`get_base_url`](scrapy_utils.md#sym-scrapy_utils_response.py-28)

*来源: `scrapy/selector/unified.py:74` · 待生成*

---