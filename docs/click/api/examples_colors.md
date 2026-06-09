# API 参考:`examples/colors`


## `examples/colors/colors.py`

<a id="sym-examples_colors_colors.py-25"></a>
### `cli` · func
装饰器: `@click.command()`
```python
def cli()
```

### 用途
This script prints colored text using the `click` library. It automatically removes ANSI styles if the output is piped into a file.

### Parameters
- None

### Returns
- None

### Raises
- None

**内部调用(库内):**
- [`style`](src_click.md#sym-src_click_termui.py-569) — **用途**: Styles a text with ANSI styles and returns the new string.

*来源: `examples/colors/colors.py:25`*

---