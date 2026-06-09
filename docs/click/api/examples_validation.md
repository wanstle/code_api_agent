# API 参考:`examples/validation`


## `examples/validation/validation.py`

<a id="sym-examples_validation_validation.py-6"></a>
### `validate_count` · func
```python
def validate_count(ctx, param, value)
```

验证输入值是否为正的偶数。

**Parameters**:
- ctx — Context: 上下文对象。
- param — Parameter: 参数对象。
- value — int: 输入值。

**Returns**:
- int: 验证通过的输入值。

**Raises**:
- BadParameter: 如果输入值不是正的偶数。

**内部调用(库内):**
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `examples/validation/validation.py:6`*

---
<a id="sym-examples_validation_validation.py-12"></a>
### `URL` · class
```python
class URL(click.ParamType[urlparse.ParseResult])
```

`URL` 类用于验证和转换用户输入的 URL 字符串，确保其符合标准的 URL 格式。

- **Parameters**:
  - `value` — `str` — 用户输入的 URL 字符串。
  - `param` — `click.Parameter` — 当前参数对象。
  - `ctx` — `click.Context` — 当前命令上下文对象。

- **Returns**:
  - `urlparse.ParseResult` — 验证并解析后的 URL 对象。

- **Raises**:
  - `click.BadParameter` — 如果输入的 URL 字符串不符合标准格式。

*来源: `examples/validation/validation.py:12`*

---
<a id="sym-examples_validation_validation.py-15"></a>
### `URL.convert` · method
```python
def convert(self, value, param, ctx) -> urlparse.ParseResult
```

将输入的 URL 转换为 `urlparse.ParseResult` 对象。

**Parameters**:
- `value` — `str` — 要转换的 URL 字符串。
- `param` — `click.Parameter` — 当前参数对象。
- `ctx` — `click.Context` — 当前上下文对象。

**Returns**:
- `urlparse.ParseResult` — 转换后的 URL 对象。

**Raises**:
- `click.BadParameter` — 如果 URL 方案不是 "http" 或 "https"。

*来源: `examples/validation/validation.py:15`*

---
<a id="sym-examples_validation_validation.py-34"></a>
### `cli` · func
装饰器: `@click.command()` `@click.option(
    "--count", default=2, callback=validate_count, help="A positive even number."
)` `@click.option("--foo", help="A mysterious parameter.")` `@click.option("--url", help="A URL", type=URL())` `@click.version_option()`
```python
def cli(count, foo, url)
```

### `cli(count, foo, url)`

This function validates parameters and prints their values.

**Parameters:**
- `count` — `int` — The count value.
- `foo` — `str` — The foo value, must be "wat" if provided.
- `url` — `str` — The URL value.

**Returns:**
- `None`

**Raises:**
- `click.BadParameter` — If `foo` is provided and not equal to "wat".

**内部调用(库内):**
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `examples/validation/validation.py:34`*

---