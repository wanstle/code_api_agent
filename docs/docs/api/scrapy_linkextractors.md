# API 参考:`scrapy/linkextractors`

## `scrapy/linkextractors/__init__.py`

<a id="sym-scrapy_linkextractors___init__.py-119"></a>

### `_matches` · func
```python
def _matches(url: str, regexs: Iterable[Pattern[str]]) -> bool
```

*来源: `scrapy/linkextractors/__init__.py:119` · 待生成*

---
<a id="sym-scrapy_linkextractors___init__.py-123"></a>

### `_is_valid_url` · func
```python
def _is_valid_url(url: str) -> bool
```

*来源: `scrapy/linkextractors/__init__.py:123` · 待生成*

---

## `scrapy/linkextractors/lxmlhtml.py`

<a id="sym-scrapy_linkextractors_lxmlhtml.py-42"></a>

### `_nons` · func
```python
def _nons(tag: Any) -> Any
```

*来源: `scrapy/linkextractors/lxmlhtml.py:42` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-52"></a>

### `_identity` · func
```python
def _identity(x: Any) -> Any
```

*来源: `scrapy/linkextractors/lxmlhtml.py:52` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-56"></a>

### `_canonicalize_link_url` · func
```python
def _canonicalize_link_url(link: Link) -> str
```

*来源: `scrapy/linkextractors/lxmlhtml.py:56` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-60"></a>

### `LxmlParserLinkExtractor` · class
```python
class LxmlParserLinkExtractor
```

*来源: `scrapy/linkextractors/lxmlhtml.py:60` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-61"></a>

### `LxmlParserLinkExtractor.__init__` · method
```python
def __init__(
        self,
        tag: str | Callable[[str], bool] = "a",
        attr: str | Callable[[str], bool] = "href",
        process: Callable[[Any], Any] | None = None,
        unique: bool = False,
        strip: bool = True,
        canonicalized: bool = False,
    )
```

*来源: `scrapy/linkextractors/lxmlhtml.py:61` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-92"></a>

### `LxmlParserLinkExtractor._iter_links` · method
```python
def _iter_links(
        self, document: HtmlElement
    ) -> Iterable[tuple[HtmlElement, str, str]]
```

**内部调用(库内):**
- [`_nons`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-42)

*来源: `scrapy/linkextractors/lxmlhtml.py:92` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-104"></a>

### `LxmlParserLinkExtractor._extract_links` · method
```python
def _extract_links(
        self,
        selector: Selector,
        response_url: str,
        response_encoding: str,
        base_url: str,
    ) -> list[Link]
```

**内部调用(库内):**
- [`LxmlParserLinkExtractor._iter_links`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-92)
- [`Link`](scrapy.md#sym-scrapy_link.py-9) — `Link` 类用于表示一个链接，包含 URL、文本、片段和是否nofollow等属性。
- [`rel_has_nofollow`](scrapy_utils.md#sym-scrapy_utils_misc.py-163)
- [`LxmlParserLinkExtractor._deduplicate_if_needed`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-154)

*来源: `scrapy/linkextractors/lxmlhtml.py:104` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-141"></a>

### `LxmlParserLinkExtractor.extract_links` · method
```python
def extract_links(self, response: TextResponse) -> list[Link]
```

**内部调用(库内):**
- [`get_base_url`](scrapy_utils.md#sym-scrapy_utils_response.py-28)
- [`LxmlParserLinkExtractor._extract_links`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-104)

*来源: `scrapy/linkextractors/lxmlhtml.py:141` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-147"></a>

### `LxmlParserLinkExtractor._process_links` · method
```python
def _process_links(self, links: list[Link]) -> list[Link]
```

**内部调用(库内):**
- [`LxmlParserLinkExtractor._deduplicate_if_needed`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-154)

*来源: `scrapy/linkextractors/lxmlhtml.py:147` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-154"></a>

### `LxmlParserLinkExtractor._deduplicate_if_needed` · method
```python
def _deduplicate_if_needed(self, links: list[Link]) -> list[Link]
```

*来源: `scrapy/linkextractors/lxmlhtml.py:154` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-164"></a>

### `LxmlLinkExtractor` · class
```python
class LxmlLinkExtractor
```

*来源: `scrapy/linkextractors/lxmlhtml.py:164` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-167"></a>

### `LxmlLinkExtractor.__init__` · method
```python
def __init__(
        self,
        allow: _RegexOrSeveral = (),
        deny: _RegexOrSeveral = (),
        allow_domains: str | Iterable[str] = (),
        deny_domains: str | Iterable[str] = (),
        restrict_xpaths: str | Iterable[str] = (),
        tags: str | Iterable[str] = ("a", "area"),
        attrs: str | Iterable[str] = ("href",),
        canonicalize: bool = False,
        unique: bool = True,
        process_value: Callable[[Any], Any] | None = None,
        deny_extensions: str | Iterable[str] | None = None,
        restrict_css: str | Iterable[str] = (),
        strip: bool = True,
        restrict_text: _RegexOrSeveral | None = None,
    )
```

**内部调用(库内):**
- [`LxmlParserLinkExtractor`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-60)
- [`LxmlLinkExtractor._compile_regexes`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-211)

*来源: `scrapy/linkextractors/lxmlhtml.py:167` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-211"></a>

### `LxmlLinkExtractor._compile_regexes` · method
装饰器: `@staticmethod`
```python
def _compile_regexes(value: _RegexOrSeveral | None) -> list[re.Pattern[str]]
```

*来源: `scrapy/linkextractors/lxmlhtml.py:211` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-217"></a>

### `LxmlLinkExtractor._link_allowed` · method
```python
def _link_allowed(self, link: Link) -> bool
```

**内部调用(库内):**
- [`_is_valid_url`](scrapy_linkextractors.md#sym-scrapy_linkextractors___init__.py-123)
- [`_matches`](scrapy_linkextractors.md#sym-scrapy_linkextractors___init__.py-119)
- [`url_is_from_any_domain`](scrapy_utils.md#sym-scrapy_utils_url.py-22)
- [`url_has_any_extension`](scrapy_utils.md#sym-scrapy_utils_url.py-41)

*来源: `scrapy/linkextractors/lxmlhtml.py:217` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-237"></a>

### `LxmlLinkExtractor.matches` · method
```python
def matches(self, url: str) -> bool
```

**内部调用(库内):**
- [`url_is_from_any_domain`](scrapy_utils.md#sym-scrapy_utils_url.py-22)

*来源: `scrapy/linkextractors/lxmlhtml.py:237` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-251"></a>

### `LxmlLinkExtractor._process_links` · method
```python
def _process_links(self, links: list[Link]) -> list[Link]
```

**内部调用(库内):**
- [`LxmlLinkExtractor._link_allowed`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-217)

*来源: `scrapy/linkextractors/lxmlhtml.py:251` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-258"></a>

### `LxmlLinkExtractor._extract_links` · method
```python
def _extract_links(self, *args: Any, **kwargs: Any) -> list[Link]
```

*来源: `scrapy/linkextractors/lxmlhtml.py:258` · 待生成*

---
<a id="sym-scrapy_linkextractors_lxmlhtml.py-261"></a>

### `LxmlLinkExtractor.extract_links` · method
```python
def extract_links(self, response: TextResponse) -> list[Link]
```

**内部调用(库内):**
- [`get_base_url`](scrapy_utils.md#sym-scrapy_utils_response.py-28)
- [`LxmlLinkExtractor._extract_links`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-258)
- [`LxmlLinkExtractor._process_links`](scrapy_linkextractors.md#sym-scrapy_linkextractors_lxmlhtml.py-251)

*来源: `scrapy/linkextractors/lxmlhtml.py:261` · 待生成*

---