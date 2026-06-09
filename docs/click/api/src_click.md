# API 参考:`src/click`


## `src/click/__init__.py`

<a id="sym-src_click___init__.py-77"></a>
### `__getattr__` · func
```python
def __getattr__(name: str) -> object
```

用途: 提供对 `BaseCommand`、`MultiCommand` 和 `OptionParser` 的向后兼容性，并在使用时发出弃用警告。

**Parameters**:
- `name` — `str` — 要获取的属性的名称。

**Returns**:
- `object` — 根据 `name` 返回相应的对象。

**Raises**:
- 无

*来源: `src/click/__init__.py:77`*

---

## `src/click/_compat.py`

<a id="sym-src_click__compat.py-18"></a>
### `_make_text_stream` · func
```python
def _make_text_stream(
    stream: t.BinaryIO,
    encoding: str | None,
    errors: str | None,
    force_readable: bool = False,
    force_writable: bool = False,
) -> t.TextIO
```

创建一个文本流包装器，处理二进制流并将其转换为文本流。

**Parameters**:
- `stream` — `t.BinaryIO` — 二进制输入输出流。
- `encoding` — `str | None` — 字符编码，如果为 `None`，则使用 `get_best_encoding` 获取最佳编码。
- `errors` — `str | None` — 错误处理方式，如果为 `None`，则使用 `"replace"`。
- `force_readable` — `bool` — 是否强制可读，默认为 `False`。
- `force_writable` — `bool` — 是否强制可写，默认为 `False`。

**Returns**:
- `t.TextIO` — 返回一个文本流包装器。

**Raises**:
- 无

**内部调用(库内):**
- [`get_best_encoding`](src_click.md#sym-src_click__compat.py-47) — Returns the best encoding for the given stream.
- [`_NonClosingTextIOWrapper`](src_click.md#sym-src_click__compat.py-55) — `_NonClosingTextIOWrapper` 是一个用于包装二进制流的类，提供文本I/O操作，同时确保流在关闭时不会被意外关闭。

*来源: `src/click/_compat.py:18`*

---
<a id="sym-src_click__compat.py-39"></a>
### `is_ascii_encoding` · func
```python
def is_ascii_encoding(encoding: str) -> bool
```

Checks if a given encoding is ascii.

**Parameters**:
- `encoding` — `str` — The encoding to check.

**Returns**:
- `bool` — `True` if the encoding is ascii, `False` otherwise.

**Raises**:
- `None`

*来源: `src/click/_compat.py:39`*

---
<a id="sym-src_click__compat.py-47"></a>
### `get_best_encoding` · func
```python
def get_best_encoding(stream: t.IO[t.Any]) -> str
```

Returns the best encoding for the given stream.

**Parameters**:
- stream — t.IO[t.Any] — The input stream to determine the encoding for.

**Returns**:
- str — The best encoding for the stream.

**Raises**:
- None

**内部调用(库内):**
- [`is_ascii_encoding`](src_click.md#sym-src_click__compat.py-39) — Checks if a given encoding is ascii.

*来源: `src/click/_compat.py:47`*

---
<a id="sym-src_click__compat.py-55"></a>
### `_NonClosingTextIOWrapper` · class
```python
class _NonClosingTextIOWrapper(io.TextIOWrapper)
```

`_NonClosingTextIOWrapper` 是一个用于包装二进制流的类，提供文本I/O操作，同时确保流在关闭时不会被意外关闭。

### 方法

- **`__init__(self, stream: t.BinaryIO, encoding: str | None, errors: str | None, force_readable: bool = False, force_writable: bool = False, **extra: t.Any) -> None`**
  - **Parameters**:
    - `stream` — `t.BinaryIO` — 要包装的二进制流。
    - `encoding` — `str | None` — 字符编码，如果为 `None`，则使用默认编码。
    - `errors` — `str | None` — 错误处理策略，如果为 `None`，则使用默认策略。
    - `force_readable` — `bool` — 是否强制流为可读，默认为 `False`。
    - `force_writable` — `bool` — 是否强制流为可写，默认为 `False`。
    - `**extra` — `t.Any` — 其他额外参数。
  - **Returns**: `None`

- **`__del__(self) -> None`**
  - **Parameters**: 无
  - **Returns**: `None`

- **`isatty(self) -> bool`**
  - **Parameters**: 无
  - **Returns**: `bool` — 是否为终端设备。
  - **Raises**: 无

*来源: `src/click/_compat.py:55`*

---
<a id="sym-src_click__compat.py-56"></a>
### `_NonClosingTextIOWrapper.__init__` · method
```python
def __init__(
        self,
        stream: t.BinaryIO,
        encoding: str | None,
        errors: str | None,
        force_readable: bool = False,
        force_writable: bool = False,
        **extra: t.Any,
    ) -> None
```

### _NonClosingTextIOWrapper.__init__

初始化一个 `_NonClosingTextIOWrapper` 对象。

**Parameters:**
- `stream` — `t.BinaryIO` — 要包装的二进制流。
- `encoding` — `str | None` — 字符编码，如果为 `None` 则使用默认编码。
- `errors` — `str | None` — 错误处理方案，如果为 `None` 则使用默认错误处理方案。
- `force_readable` — `bool` — 是否强制流为可读模式，默认为 `False`。
- `force_writable` — `bool` — 是否强制流为可写模式，默认为 `False`。
- `**extra` — `t.Any` — 其他关键字参数。

**Returns:**
- `None`

**Raises:**
- 无

**内部调用(库内):**
- [`_FixupStream`](src_click.md#sym-src_click__compat.py-81) — `_FixupStream` 类用于包装二进制流，提供额外的读取和写入控制。

*来源: `src/click/_compat.py:56`*

---
<a id="sym-src_click__compat.py-70"></a>
### `_NonClosingTextIOWrapper.__del__` · method
```python
def __del__(self) -> None
```

### 用途
在对象被垃圾回收时，尝试关闭文件流。

### Parameters
- 无

### Returns
- `None`

### Raises
- 无

*来源: `src/click/_compat.py:70`*

---
<a id="sym-src_click__compat.py-76"></a>
### `_NonClosingTextIOWrapper.isatty` · method
```python
def isatty(self) -> bool:
        # https://bitbucket.org/pypy/pypy/issue/1803
```

检查底层流是否为终端。

**Parameters**:
- 无

**Returns**:
- `bool`: 如果底层流是终端则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:76`*

---
<a id="sym-src_click__compat.py-81"></a>
### `_FixupStream` · class
```python
class _FixupStream
```

`_FixupStream` 类用于包装二进制流，提供额外的读取和写入控制。

- **Parameters**:
  - `stream` — `t.BinaryIO` — 要包装的二进制流。
  - `force_readable` — `bool` — 是否强制流可读，默认为 `False`。
  - `force_writable` — `bool` — 是否强制流可写，默认为 `False`。

- **Returns**:
  - 无

- **Raises**:
  - 无

*来源: `src/click/_compat.py:81`*

---
<a id="sym-src_click__compat.py-91"></a>
### `_FixupStream.__init__` · method
```python
def __init__(
        self,
        stream: t.BinaryIO,
        force_readable: bool = False,
        force_writable: bool = False,
    )
```

### `_FixupStream.__init__`

初始化 `_FixupStream` 对象。

**Parameters**:
- `stream` — `t.BinaryIO` — 要处理的二进制流。
- `force_readable` — `bool` — 是否强制流为可读，默认为 `False`。
- `force_writable` — `bool` — 是否强制流为可写，默认为 `False`。

**Returns**:
- 无返回值。

**Raises**:
- 无异常抛出。

*来源: `src/click/_compat.py:91`*

---
<a id="sym-src_click__compat.py-101"></a>
### `_FixupStream.__getattr__` · method
```python
def __getattr__(self, name: str) -> t.Any
```

### 用途
递归调用 `_stream` 对象的 `__getattr__` 方法，获取指定属性。

### Parameters
- `name` — `str` — 要获取的属性名称。

### Returns
- `t.Any` — `_stream` 对象中指定属性的值。

### Raises
- 无

*来源: `src/click/_compat.py:101`*

---
<a id="sym-src_click__compat.py-104"></a>
### `_FixupStream.read1` · method
```python
def read1(self, size: int) -> bytes
```

读取最多 `size` 字节的数据。

**Parameters**:
- `size` — `int` — 要读取的最大字节数。

**Returns**:
- `bytes` — 读取的数据。

**Raises**:
- 无

*来源: `src/click/_compat.py:104`*

---
<a id="sym-src_click__compat.py-112"></a>
### `_FixupStream.readable` · method
```python
def readable(self) -> bool
```

检查流是否可读。

**Parameters**:
- 无

**Returns**:
- `bool` — 如果流可读则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:112`*

---
<a id="sym-src_click__compat.py-124"></a>
### `_FixupStream.writable` · method
```python
def writable(self) -> bool
```

检查流是否可写。

**Parameters**:
- 无

**Returns**:
- `bool` — 如果流可写则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:124`*

---
<a id="sym-src_click__compat.py-139"></a>
### `_FixupStream.seekable` · method
```python
def seekable(self) -> bool
```

检查流是否支持 seek 操作。

**Parameters**:
- 无

**Returns**:
- `bool` — 如果流支持 seek 操作则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:139`*

---
<a id="sym-src_click__compat.py-150"></a>
### `_is_binary_reader` · func
```python
def _is_binary_reader(stream: t.IO[t.Any], default: bool = False) -> bool
```

检查给定的流是否为二进制读取流。

**Parameters**:
- `stream` — `t.IO[t.Any]` — 要检查的流。
- `default` — `bool` — 如果流无法检查，则返回的默认值。默认为 `False`。

**Returns**:
- `bool` — 如果流是二进制读取流，则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:150`*

---
<a id="sym-src_click__compat.py-159"></a>
### `_is_binary_writer` · func
```python
def _is_binary_writer(stream: t.IO[t.Any], default: bool = False) -> bool
```

检查给定的流是否是二进制写入流。

**Parameters**:
- `stream` — `t.IO[t.Any]` — 要检查的流。
- `default` — `bool` — 如果无法确定流类型时的默认值。

**Returns**:
- `bool` — 如果流是二进制写入流则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:159`*

---
<a id="sym-src_click__compat.py-172"></a>
### `_find_binary_reader` · func
```python
def _find_binary_reader(stream: t.IO[t.Any]) -> t.BinaryIO | None:
    # We need to figure out if the given stream is already binary.
    # This can happen because the official docs recommend detaching
    # the streams to get binary streams.  Some code might do this, so
    # we need to deal with this case explicitly.
```

### _find_binary_reader

Finds a binary reader from the given stream, if available.

**Parameters**:
- `stream` — `t.IO[t.Any]` — The input stream to check.

**Returns**:
- `t.BinaryIO | None` — The binary reader if found, otherwise `None`.

**Raises**:
- None

**内部调用(库内):**
- [`_is_binary_reader`](src_click.md#sym-src_click__compat.py-150) — 检查给定的流是否为二进制读取流。

*来源: `src/click/_compat.py:172`*

---
<a id="sym-src_click__compat.py-190"></a>
### `_find_binary_writer` · func
```python
def _find_binary_writer(stream: t.IO[t.Any]) -> t.BinaryIO | None:
    # We need to figure out if the given stream is already binary.
    # This can happen because the official docs recommend detaching
    # the streams to get binary streams.  Some code might do this, so
    # we need to deal with this case explicitly.
```

### _find_binary_writer

Finds a binary writer from the given stream, if it exists.

**Parameters**:
- `stream` — `t.IO[t.Any]` — The input stream to check.

**Returns**:
- `t.BinaryIO | None` — The binary writer if found, otherwise `None`.

**Raises**:
- None

**内部调用(库内):**
- [`_is_binary_writer`](src_click.md#sym-src_click__compat.py-159) — 检查给定的流是否是二进制写入流。

*来源: `src/click/_compat.py:190`*

---
<a id="sym-src_click__compat.py-208"></a>
### `_stream_is_misconfigured` · func
```python
def _stream_is_misconfigured(stream: t.TextIO) -> bool
```

检查给定的文本流是否配置不正确，即其编码是否为 ASCII。

**Parameters**:
- `stream` — `t.TextIO` — 要检查的文本流。

**Returns**:
- `bool` — 如果流的编码为 ASCII，则返回 `True`，否则返回 `False`。

**Raises**:
- 无

**内部调用(库内):**
- [`is_ascii_encoding`](src_click.md#sym-src_click__compat.py-39) — Checks if a given encoding is ascii.

*来源: `src/click/_compat.py:208`*

---
<a id="sym-src_click__compat.py-217"></a>
### `_is_compat_stream_attr` · func
```python
def _is_compat_stream_attr(stream: t.TextIO, attr: str, value: str | None) -> bool
```

检查流对象的属性是否与给定值兼容。

**Parameters**:
- `stream` — `t.TextIO` — 要检查的流对象。
- `attr` — `str` — 要检查的属性名称。
- `value` — `str | None` — 要比较的值，如果为 `None`，则检查属性是否有值。

**Returns**:
- `bool` — 如果属性值与给定值兼容或属性有值且值未设置，则返回 `True`，否则返回 `False`。

*来源: `src/click/_compat.py:217`*

---
<a id="sym-src_click__compat.py-226"></a>
### `_is_compatible_text_stream` · func
```python
def _is_compatible_text_stream(
    stream: t.TextIO, encoding: str | None, errors: str | None
) -> bool
```

检查一个流的编码和错误处理属性是否与所需值兼容。

**Parameters**:
- `stream` — `t.TextIO` — 要检查的流。
- `encoding` — `str | None` — 所需的编码值。
- `errors` — `str | None` — 所需的错误处理值。

**Returns**:
- `bool` — 如果流的编码和错误处理属性与所需值兼容，则返回 `True`，否则返回 `False`。

**内部调用(库内):**
- [`_is_compat_stream_attr`](src_click.md#sym-src_click__compat.py-217) — 检查流对象的属性是否与给定值兼容。

*来源: `src/click/_compat.py:226`*

---
<a id="sym-src_click__compat.py-237"></a>
### `_force_correct_text_stream` · func
```python
def _force_correct_text_stream(
    text_stream: t.IO[t.Any],
    encoding: str | None,
    errors: str | None,
    is_binary: t.Callable[[t.IO[t.Any], bool], bool],
    find_binary: t.Callable[[t.IO[t.Any]], t.BinaryIO | None],
    force_readable: bool = False,
    force_writable: bool = False,
) -> t.TextIO
```

**用途**: 确保文本流的正确性，处理二进制和文本流之间的转换。

**Parameters**:
- `text_stream` (t.IO[t.Any]) — 输入的文本流。
- `encoding` (str | None) — 指定的编码。
- `errors` (str | None) — 处理编码错误的方式。
- `is_binary` (t.Callable[[t.IO[t.Any], bool], bool]) — 判断流是否为二进制的函数。
- `find_binary` (t.Callable[[t.IO[t.Any]], t.BinaryIO | None]) — 查找底层二进制流的函数。
- `force_readable` (bool) — 是否强制流可读。
- `force_writable` (bool) — 是否强制流可写。

**Returns**:
- t.TextIO — 确保正确的文本流。

**Raises**:
- 无

**内部调用(库内):**
- [`_is_compatible_text_stream`](src_click.md#sym-src_click__compat.py-226) — 检查一个流的编码和错误处理属性是否与所需值兼容。
- [`_stream_is_misconfigured`](src_click.md#sym-src_click__compat.py-208) — 检查给定的文本流是否配置不正确，即其编码是否为 ASCII。
- [`_make_text_stream`](src_click.md#sym-src_click__compat.py-18) — 创建一个文本流包装器，处理二进制流并将其转换为文本流。

*来源: `src/click/_compat.py:237`*

---
<a id="sym-src_click__compat.py-283"></a>
### `_force_correct_text_reader` · func
```python
def _force_correct_text_reader(
    text_reader: t.IO[t.Any],
    encoding: str | None,
    errors: str | None,
    force_readable: bool = False,
) -> t.TextIO
```

**用途**: 强制将一个二进制流转换为文本流。

**Parameters**:
- `text_reader` — `t.IO[t.Any]` — 一个二进制或文本流。
- `encoding` — `str | None` — 文本编码，如果为 `None`，则使用默认编码。
- `errors` — `str | None` — 错误处理方式，如果为 `None`，则使用默认错误处理方式。
- `force_readable` — `bool` — 是否强制文本流可读，默认为 `False`。

**Returns**:
- `t.TextIO` — 一个文本流。

**Raises**:
- 无

**内部调用(库内):**
- [`_force_correct_text_stream`](src_click.md#sym-src_click__compat.py-237) — **用途**: 确保文本流的正确性，处理二进制和文本流之间的转换。

*来源: `src/click/_compat.py:283`*

---
<a id="sym-src_click__compat.py-299"></a>
### `_force_correct_text_writer` · func
```python
def _force_correct_text_writer(
    text_writer: t.IO[t.Any],
    encoding: str | None,
    errors: str | None,
    force_writable: bool = False,
) -> t.TextIO
```

**用途**: 强制将给定的文本写入器转换为正确的文本流。

**Parameters**:
- `text_writer` — `t.IO[t.Any]` — 要转换的文本写入器。
- `encoding` — `str | None` — 编码方式，如果为 `None`，则使用默认编码。
- `errors` — `str | None` — 错误处理方式，如果为 `None`，则使用默认错误处理方式。
- `force_writable` — `bool` — 是否强制可写，默认为 `False`。

**Returns**:
- `t.TextIO` — 转换后的文本流。

**Raises**:
- 无

**内部调用(库内):**
- [`_force_correct_text_stream`](src_click.md#sym-src_click__compat.py-237) — **用途**: 确保文本流的正确性，处理二进制和文本流之间的转换。

*来源: `src/click/_compat.py:299`*

---
<a id="sym-src_click__compat.py-315"></a>
### `get_binary_stdin` · func
```python
def get_binary_stdin() -> t.BinaryIO
```

获取二进制标准输入流。

**Parameters**:
- 无

**Returns**:
- `t.BinaryIO`: 二进制标准输入流。

**Raises**:
- `RuntimeError`: 如果无法确定 `sys.stdin` 的二进制流。

**内部调用(库内):**
- [`_find_binary_reader`](src_click.md#sym-src_click__compat.py-172) — _find_binary_reader

*来源: `src/click/_compat.py:315`*

---
<a id="sym-src_click__compat.py-322"></a>
### `get_binary_stdout` · func
```python
def get_binary_stdout() -> t.BinaryIO
```

获取 `sys.stdout` 的二进制写入流。

**Parameters**:
- 无

**Returns**:
- `t.BinaryIO`: `sys.stdout` 的二进制写入流。

**Raises**:
- `RuntimeError`: 如果无法确定 `sys.stdout` 的二进制流。

**内部调用(库内):**
- [`_find_binary_writer`](src_click.md#sym-src_click__compat.py-190) — _find_binary_writer

*来源: `src/click/_compat.py:322`*

---
<a id="sym-src_click__compat.py-329"></a>
### `get_binary_stderr` · func
```python
def get_binary_stderr() -> t.BinaryIO
```

获取标准错误输出的二进制流。

**Parameters**:
- 无

**Returns**:
- `t.BinaryIO`: 标准错误输出的二进制流。

**Raises**:
- `RuntimeError`: 如果无法确定标准错误输出的二进制流。

**内部调用(库内):**
- [`_find_binary_writer`](src_click.md#sym-src_click__compat.py-190) — _find_binary_writer

*来源: `src/click/_compat.py:329`*

---
<a id="sym-src_click__compat.py-336"></a>
### `get_text_stdin` · func
```python
def get_text_stdin(encoding: str | None = None, errors: str | None = None) -> t.TextIO
```

获取标准输入的文本流。

**Parameters**:
- `encoding` — `str | None` — 指定输入流的编码格式，如果为 `None`，则使用系统默认编码。
- `errors` — `str | None` — 指定错误处理方案，如果为 `None`，则使用默认错误处理。

**Returns**:
- `t.TextIO` — 返回一个文本输入流对象。

**Raises**:
- 无

**内部调用(库内):**
- [`_get_windows_console_stream`](src_click.md#sym-src_click__compat.py-526) — `_get_windows_console_stream`
- [`_force_correct_text_reader`](src_click.md#sym-src_click__compat.py-283) — **用途**: 强制将一个二进制流转换为文本流。

*来源: `src/click/_compat.py:336`*

---
<a id="sym-src_click__compat.py-343"></a>
### `get_text_stdout` · func
```python
def get_text_stdout(encoding: str | None = None, errors: str | None = None) -> t.TextIO
```

获取标准输出的文本流。

**Parameters:**
- `encoding` (str | None) — 字符编码，如 'utf-8'。如果为 `None`，则使用系统默认编码。
- `errors` (str | None) — 错误处理方案，如 'ignore'、'replace'。如果为 `None`，则使用默认错误处理方案。

**Returns:**
- t.TextIO — 标准输出的文本流。

**Raises:**
- 无

**内部调用(库内):**
- [`_get_windows_console_stream`](src_click.md#sym-src_click__compat.py-526) — `_get_windows_console_stream`
- [`_force_correct_text_writer`](src_click.md#sym-src_click__compat.py-299) — **用途**: 强制将给定的文本写入器转换为正确的文本流。

*来源: `src/click/_compat.py:343`*

---
<a id="sym-src_click__compat.py-350"></a>
### `get_text_stderr` · func
```python
def get_text_stderr(encoding: str | None = None, errors: str | None = None) -> t.TextIO
```

获取标准错误输出的文本流。

**Parameters**:
- `encoding` — `str | None` — 指定编码，如果为 `None`，则使用默认编码。
- `errors` — `str | None` — 指定错误处理方案，如果为 `None`，则使用默认错误处理方案。

**Returns**:
- `t.TextIO` — 标准错误输出的文本流。

**Raises**:
- 无

**内部调用(库内):**
- [`_get_windows_console_stream`](src_click.md#sym-src_click__compat.py-526) — `_get_windows_console_stream`
- [`_force_correct_text_writer`](src_click.md#sym-src_click__compat.py-299) — **用途**: 强制将给定的文本写入器转换为正确的文本流。

*来源: `src/click/_compat.py:350`*

---
<a id="sym-src_click__compat.py-357"></a>
### `_wrap_io_open` · func
```python
def _wrap_io_open(
    file: str | os.PathLike[str] | int,
    mode: str,
    encoding: str | None,
    errors: str | None,
) -> t.IO[t.Any]
```

Handles not passing `encoding` and `errors` in binary mode.

**Parameters**:
- `file` — `str | os.PathLike[str] | int` — The file to open.
- `mode` — `str` — The mode in which to open the file.
- `encoding` — `str | None` — The encoding to use for the file.
- `errors` — `str | None` — The error handling scheme to use for the file.

**Returns**:
- `t.IO[t.Any]` — The file object.

*来源: `src/click/_compat.py:357`*

---
<a id="sym-src_click__compat.py-370"></a>
### `open_stream` · func
```python
def open_stream(
    filename: str | os.PathLike[str],
    mode: str = "r",
    encoding: str | None = None,
    errors: str | None = "strict",
    atomic: bool = False,
) -> tuple[t.IO[t.Any], bool]
```

### `open_stream`

打开一个文件或标准流，并返回一个文件对象和一个布尔值，指示是否是原子写。

**Parameters**:
- `filename` — `str | os.PathLike[str]` — 文件路径或标准流标识符。
- `mode` — `str` — 文件打开模式，默认为 `"r"`。
- `encoding` — `str | None` — 文件编码，默认为 `None`。
- `errors` — `str | None` — 错误处理方式，默认为 `"strict"`。
- `atomic` — `bool` — 是否使用原子写，默认为 `False`。

**Returns**:
- `tuple[t.IO[t.Any], bool]` — 文件对象和一个布尔值，指示是否是原子写。

**Raises**:
- `ValueError` — 如果尝试追加到现有文件或使用不支持的模式。

**内部调用(库内):**
- [`get_binary_stdout`](src_click.md#sym-src_click__compat.py-322) — 获取 `sys.stdout` 的二进制写入流。
- [`get_text_stdout`](src_click.md#sym-src_click__compat.py-343) — 获取标准输出的文本流。
- [`get_binary_stdin`](src_click.md#sym-src_click__compat.py-315) — 获取二进制标准输入流。
- [`get_text_stdin`](src_click.md#sym-src_click__compat.py-336) — 获取标准输入的文本流。
- [`_wrap_io_open`](src_click.md#sym-src_click__compat.py-357) — Handles not passing `encoding` and `errors` in binary mode.
- [`_AtomicFile`](src_click.md#sym-src_click__compat.py-451) — `_AtomicFile` 类用于在文件操作中提供原子性，确保文件写入操作的完整性。

*来源: `src/click/_compat.py:370`*

---
<a id="sym-src_click__compat.py-451"></a>
### `_AtomicFile` · class
```python
class _AtomicFile
```

`_AtomicFile` 类用于在文件操作中提供原子性，确保文件写入操作的完整性。

- **Parameters**:
  - `f` — `t.IO[t.Any]` — 文件对象。
  - `tmp_filename` — `str` — 临时文件名。
  - `real_filename` — `str` — 实际文件名。

- **Returns**:
  - 无

- **Raises**:
  - 无

- **Methods**:
  - `name(self) -> str` — 返回文件名。
  - `close(self, delete: bool = False) -> None` — 关闭文件，可选删除临时文件。
  - `__getattr__(self, name: str) -> t.Any` — 获取文件对象的属性。
  - `__enter__(self) -> _AtomicFile` — 上下文管理器入口。
  - `__exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` — 上下文管理器出口。
  - `__repr__(self) -> str` — 返回对象的字符串表示。

*来源: `src/click/_compat.py:451`*

---
<a id="sym-src_click__compat.py-452"></a>
### `_AtomicFile.__init__` · method
```python
def __init__(self, f: t.IO[t.Any], tmp_filename: str, real_filename: str) -> None
```

**用途**: 初始化一个 `_AtomicFile` 对象，用于原子地写入文件。

**Parameters**:
- `f` — `t.IO[t.Any]` — 实际文件对象。
- `tmp_filename` — `str` — 临时文件名。
- `real_filename` — `str` — 实际文件名。

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/_compat.py:452`*

---
<a id="sym-src_click__compat.py-459"></a>
### `_AtomicFile.name` · method
装饰器: `@property`
```python
def name(self) -> str
```

返回文件的原始名称。

**Parameters**:
- 无

**Returns**:
- `str`: 文件的原始名称。

*来源: `src/click/_compat.py:459`*

---
<a id="sym-src_click__compat.py-462"></a>
### `_AtomicFile.close` · method
```python
def close(self, delete: bool = False) -> None
```

Closes the file, optionally deleting the temporary file if `delete` is `True`.

**Parameters**:
- `delete` — `bool` — If `True`, the temporary file will be deleted after closing.

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/_compat.py:462`*

---
<a id="sym-src_click__compat.py-469"></a>
### `_AtomicFile.__getattr__` · method
```python
def __getattr__(self, name: str) -> t.Any
```

用途: 代理对文件对象的属性访问。

**Parameters**:
- `name` — `str` — 要访问的属性名称。

**Returns**:
- `t.Any` — 文件对象对应属性的值。

**Raises**:
- 无

*来源: `src/click/_compat.py:469`*

---
<a id="sym-src_click__compat.py-472"></a>
### `_AtomicFile.__enter__` · method
```python
def __enter__(self) -> _AtomicFile
```

用途: 返回当前的 `_AtomicFile` 实例。

**Parameters**:
- 无

**Returns**:
- `_AtomicFile`: 当前的 `_AtomicFile` 实例。

**Raises**:
- 无

*来源: `src/click/_compat.py:472`*

---
<a id="sym-src_click__compat.py-475"></a>
### `_AtomicFile.__exit__` · method
```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None
```

Closes the file, optionally deleting it if an exception occurred.

**Parameters**:
- `exc_type` (`type[BaseException] | None`): The type of the exception that was raised, or `None` if no exception was raised.
- `exc_value` (`BaseException | None`): The exception instance that was raised, or `None` if no exception was raised.
- `tb` (`TracebackType | None`): The traceback object associated with the exception, or `None` if no exception was raised.

**Returns**:
- `None`

**Raises**:
- None

*来源: `src/click/_compat.py:475`*

---
<a id="sym-src_click__compat.py-483"></a>
### `_AtomicFile.__repr__` · method
```python
def __repr__(self) -> str
```

返回文件对象的字符串表示。

**Parameters**:
- 无

**Returns**:
- `str`: 文件对象的字符串表示。

**Raises**:
- 无

*来源: `src/click/_compat.py:483`*

---
<a id="sym-src_click__compat.py-487"></a>
### `strip_ansi` · func
```python
def strip_ansi(value: str) -> str
```

**用途**: 移除字符串中的 ANSI 转义码。

**Parameters**:
- `value` — `str` — 需要处理的字符串。

**Returns**:
- `str` — 移除 ANSI 转义码后的字符串。

*来源: `src/click/_compat.py:487`*

---
<a id="sym-src_click__compat.py-491"></a>
### `_is_jupyter_kernel_output` · func
```python
def _is_jupyter_kernel_output(stream: t.IO[t.Any]) -> bool
```

检查给定的流是否是 Jupyter 内核输出流。

**Parameters**:
- `stream` — `t.IO[t.Any]` — 要检查的流。

**Returns**:
- `bool` — 如果流是 Jupyter 内核输出流，则返回 `True`，否则返回 `False`。

*来源: `src/click/_compat.py:491`*

---
<a id="sym-src_click__compat.py-498"></a>
### `should_strip_ansi` · func
```python
def should_strip_ansi(
    stream: t.IO[t.Any] | None = None, color: bool | None = None
) -> bool
```

### should_strip_ansi

Determine whether ANSI escape codes should be stripped from the given stream.

**Parameters**:
- `stream` (`t.IO[t.Any] | None`): The stream to check. If `None`, defaults to `sys.stdin`.
- `color` (`bool | None`): Whether to strip ANSI escape codes. If `None`, ANSI codes are stripped if the stream is not a TTY and not a Jupyter kernel output.

**Returns**:
- `bool`: `True` if ANSI escape codes should be stripped, `False` otherwise.

**Raises**:
- None

**内部调用(库内):**
- [`isatty`](src_click.md#sym-src_click__compat.py-536) — 检查给定的流对象是否为终端设备。
- [`_is_jupyter_kernel_output`](src_click.md#sym-src_click__compat.py-491) — 检查给定的流是否是 Jupyter 内核输出流。

*来源: `src/click/_compat.py:498`*

---
<a id="sym-src_click__compat.py-516"></a>
### `_get_argv_encoding` · func
```python
def _get_argv_encoding() -> str
```

获取当前系统首选的命令行参数编码。

**Parameters**:
- 无

**Returns**:
- `str`: 当前系统首选的命令行参数编码。

**Raises**:
- 无

*来源: `src/click/_compat.py:516`*

---
<a id="sym-src_click__compat.py-523"></a>
### `_get_argv_encoding` · func
```python
def _get_argv_encoding() -> str
```

获取命令行参数的编码。

**Parameters**:
- 无

**Returns**:
- `str`: 命令行参数的编码。

**Raises**:
- 无

*来源: `src/click/_compat.py:523`*

---
<a id="sym-src_click__compat.py-526"></a>
### `_get_windows_console_stream` · func
```python
def _get_windows_console_stream(
        f: t.TextIO, encoding: str | None, errors: str | None
    ) -> t.TextIO | None
```

### `_get_windows_console_stream`

Returns `None`.

*来源: `src/click/_compat.py:526`*

---
<a id="sym-src_click__compat.py-532"></a>
### `term_len` · func
```python
def term_len(x: str) -> int
```

计算去除 ANSI 转义码后的字符串长度。

**Parameters**:
- x — str — 输入的字符串。

**Returns**:
- int — 去除 ANSI 转义码后的字符串长度。

**Raises**:
- 无

**内部调用(库内):**
- [`strip_ansi`](src_click.md#sym-src_click__compat.py-487) — **用途**: 移除字符串中的 ANSI 转义码。

*来源: `src/click/_compat.py:532`*

---
<a id="sym-src_click__compat.py-536"></a>
### `isatty` · func
```python
def isatty(stream: t.IO[t.Any]) -> bool
```

检查给定的流对象是否为终端设备。

**Parameters**:
- `stream` — `t.IO[t.Any]` — 要检查的流对象。

**Returns**:
- `bool` — 如果流对象是终端设备则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_compat.py:536`*

---
<a id="sym-src_click__compat.py-543"></a>
### `_make_cached_stream_func` · func
```python
def _make_cached_stream_func(
    src_func: t.Callable[[], t.TextIO | None],
    wrapper_func: t.Callable[[], t.TextIO],
) -> t.Callable[[], t.TextIO | None]
```

创建一个缓存装饰器函数，用于缓存流对象。

**Parameters**:
- `src_func` — `Callable[[], TextIO | None]` — 一个返回流对象或 `None` 的函数。
- `wrapper_func` — `Callable[[], TextIO]` — 一个返回流对象的函数，用于包装原始流对象。

**Returns**:
- `Callable[[], TextIO | None]` — 返回一个装饰后的函数，该函数会缓存流对象以避免重复创建。

**Raises**:
- 无

*来源: `src/click/_compat.py:543`*

---
<a id="sym-src_click__compat.py-549"></a>
### `func` · func
```python
def func() -> t.TextIO | None
```

### func

- **Returns**: `t.TextIO | None` — The result of the function, which could be a text stream or `None`.
- **Raises**: `Exception` — If an exception occurs during the execution of `src_func()` or `wrapper_func()`.

*来源: `src/click/_compat.py:549`*

---

## `src/click/_termui_impl.py`

<a id="sym-src_click__termui_impl.py-37"></a>
### `_BufferedTextPagerStream` · class
```python
class _BufferedTextPagerStream(t.Protocol)
```

`_BufferedTextPagerStream` 类代表一个用于分页显示文本的缓冲流。它承担将长文本分页显示在终端中的职责。

**Parameters**:
- 无

**Returns**:
- 无

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:37`*

---
<a id="sym-src_click__termui_impl.py-41"></a>
### `_has_binary_buffer` · func
```python
def _has_binary_buffer(
    stream: t.BinaryIO | t.TextIO,
) -> t.TypeGuard[_BufferedTextPagerStream]:
    # TextIO is wider than TextIOWrapper; text-only streams such as StringIO
    # are valid TextIO values but do not expose a binary buffer to wrap.
```

检查给定的流是否具有二进制缓冲区。

**Parameters**:
- `stream` — `t.BinaryIO | t.TextIO` — 要检查的流。

**Returns**:
- `t.TypeGuard[_BufferedTextPagerStream]` — 如果流具有二进制缓冲区，则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:41`*

---
<a id="sym-src_click__termui_impl.py-57"></a>
### `ProgressBar` · class
```python
class ProgressBar(t.Generic[V])
```

`ProgressBar` 类用于创建和管理进度条，提供进度更新、渲染和格式化等功能。

### 方法

#### `__init__`
- **Parameters**:
  - `iterable` — `cabc.Iterable[V] | None` — 要迭代的可迭代对象。
  - `length` — `int | None` — 进度条的长度。
  - `fill_char` — `str` — 进度条填充字符，默认为 `#`。
  - `empty_char` — `str` — 进度条空字符，默认为 ` `。
  - `bar_template` — `str` — 进度条模板，默认为 `%(bar)s`。
  - `info_sep` — `str` — 信息分隔符，默认为 `  `。
  - `hidden` — `bool` — 是否隐藏进度条，默认为 `False`。
  - `show_eta` — `bool` — 是否显示预计完成时间，默认为 `True`。
  - `show_percent` — `bool | None` — 是否显示百分比，默认为 `None`。
  - `show_pos` — `bool` — 是否显示当前位置，默认为 `False`。
  - `item_show_func` — `t.Callable[[V | None], str | None] | None` — 显示当前项的函数，默认为 `None`。
  - `label` — `str | None` — 进度条标签，默认为 `None`。
  - `

*来源: `src/click/_termui_impl.py:57`*

---
<a id="sym-src_click__termui_impl.py-58"></a>
### `ProgressBar.__init__` · method
```python
def __init__(
        self,
        iterable: cabc.Iterable[V] | None,
        length: int | None = None,
        fill_char: str = "#",
        empty_char: str = " ",
        bar_template: str = "%(bar)s",
        info_sep: str = "  ",
        hidden: bool = False,
        show_eta: bool = True,
        show_percent: bool | None = None,
        show_pos: bool = False,
        item_show_func: t.Callable[[V | None], str | None] | None = None,
        label: str | None = None,
        file: t.TextIO | None = None,
        color: bool | None = None,
        update_min_steps: int = 1,
        width: int = 30,
    ) -> None
```

### ProgressBar.__init__

初始化一个进度条对象。

**Parameters**:
- `iterable` — `cabc.Iterable[V] | None` — 要遍历的可迭代对象。
- `length` — `int | None` — 进度条的总长度。
- `fill_char` — `str` — 进度条已填充部分的字符。
- `empty_char` — `str` — 进度条未填充部分的字符。
- `bar_template` — `str` — 进度条的模板字符串。
- `info_sep` — `str` — 信息部分与进度条之间的分隔符。
- `hidden` — `bool` — 是否隐藏进度条。
- `show_eta` — `bool` — 是否显示剩余时间。
- `show_percent` — `bool | None` — 是否显示百分比。
- `show_pos` — `bool` — 是否显示当前位置。
- `item_show_func` — `t.Callable[[V | None], str | None] | None` — 显示每个项目的函数。
- `label` — `str | None` — 进度条的标签。
- `file` — `t.TextIO | None` — 输出进度条的文件对象。
- `color` — `bool | None` — 是否启用颜色。
- `update_min_steps` — `int` — 更新进度条的最小步数。
- `width` — `int` — 进度条的宽度。

**Returns

*来源: `src/click/_termui_impl.py:58`*

---
<a id="sym-src_click__termui_impl.py-129"></a>
### `ProgressBar.__enter__` · method
```python
def __enter__(self) -> ProgressBar[V]
```

### ProgressBar.__enter__

Enters the context manager and renders the initial progress bar.

**Parameters**:
- `self` — `ProgressBar[V]` — The ProgressBar instance.

**Returns**:
- `ProgressBar[V]` — The ProgressBar instance.

**Raises**:
- None

**内部调用(库内):**
- [`ProgressBar.render_progress`](src_click.md#sym-src_click__termui_impl.py-256) — ProgressBar.render_progress

*来源: `src/click/_termui_impl.py:129`*

---
<a id="sym-src_click__termui_impl.py-134"></a>
### `ProgressBar.__exit__` · method
```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None
```

### ProgressBar.__exit__

结束进度条的渲染。

**Parameters**:
- `exc_type` (type[BaseException] | None) — 异常类型，如果存在异常则为异常类型，否则为 `None`。
- `exc_value` (BaseException | None) — 异常实例，如果存在异常则为异常实例，否则为 `None`。
- `tb` (TracebackType | None) — 异常的回溯信息，如果存在异常则为回溯信息，否则为 `None`。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`ProgressBar.render_finish`](src_click.md#sym-src_click__termui_impl.py-156) — ProgressBar.render_finish

*来源: `src/click/_termui_impl.py:134`*

---
<a id="sym-src_click__termui_impl.py-142"></a>
### `ProgressBar.__iter__` · method
```python
def __iter__(self) -> cabc.Iterator[V]
```

### ProgressBar.__iter__

Iterates over the progress bar, rendering the progress and yielding values.

**Parameters**:
- `self` — `ProgressBar` — The progress bar instance.

**Returns**:
- `cabc.Iterator[V]` — An iterator that yields values as the progress bar progresses.

**Raises**:
- `RuntimeError` — If the progress bar is not used within a `with` block.

**内部调用(库内):**
- [`ProgressBar.render_progress`](src_click.md#sym-src_click__termui_impl.py-256) — ProgressBar.render_progress
- [`ProgressBar.generator`](src_click.md#sym-src_click__termui_impl.py-355) — **用途**: 返回一个生成器，该生成器在构造进度条时逐个生成添加到进度条中的项目，并在生成器块返回后更新进度条。

*来源: `src/click/_termui_impl.py:142`*

---
<a id="sym-src_click__termui_impl.py-148"></a>
### `ProgressBar.__next__` · method
```python
def __next__(self) -> V:
        # Iteration is defined in terms of a generator function,
        # returned by iter(self); use that to define next(). This works
        # because `self.iter` is an iterable consumed by that generator,
        # so it is re-entry safe. Calling `next(self.generator())`
        # twice works and does "what you want".
```

**用途**: 迭代器的 `__next__` 方法，用于获取迭代器的下一个值。

**Parameters**:
- 无

**Returns**:
- `V`: 迭代器的下一个值。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:148`*

---
<a id="sym-src_click__termui_impl.py-156"></a>
### `ProgressBar.render_finish` · method
```python
def render_finish(self) -> None
```

### ProgressBar.render_finish

Renders the finish state of the progress bar.

**Parameters**:
- `self` — `ProgressBar` — The progress bar instance.

**Returns**:
- `None`

**Raises**:
- None

*来源: `src/click/_termui_impl.py:156`*

---
<a id="sym-src_click__termui_impl.py-163"></a>
### `ProgressBar.pct` · method
装饰器: `@property`
```python
def pct(self) -> float
```

**用途**: 计算并返回进度条的百分比。

**Parameters**:
- 无

**Returns**:
- `float`: 进度条的百分比，范围从 0.0 到 1.0。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:163`*

---
<a id="sym-src_click__termui_impl.py-169"></a>
### `ProgressBar.time_per_iteration` · method
装饰器: `@property`
```python
def time_per_iteration(self) -> float
```

计算进度条每个迭代的平均时间。

**Parameters**:
- 无

**Returns**:
- `float`: 进度条每个迭代的平均时间。如果 `avg` 列表为空，则返回 0.0。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:169`*

---
<a id="sym-src_click__termui_impl.py-175"></a>
### `ProgressBar.eta` · method
装饰器: `@property`
```python
def eta(self) -> float
```

**用途**: 计算并返回进度条的估计剩余时间（以秒为单位）。

**Parameters**:
- 无

**Returns**:
- `float`: 估计的剩余时间（以秒为单位）。如果进度条已完成或长度未定义，则返回 0.0。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:175`*

---
<a id="sym-src_click__termui_impl.py-180"></a>
### `ProgressBar.format_eta` · method
```python
def format_eta(self) -> str
```

用途: 格式化进度条的剩余时间。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的剩余时间字符串，格式为 "d天 h小时 m分钟 s秒" 或 "h小时 m分钟 s秒"。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:180`*

---
<a id="sym-src_click__termui_impl.py-201"></a>
### `ProgressBar.format_pos` · method
```python
def format_pos(self) -> str
```

**用途**: 格式化进度条的当前位置。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的进度条当前位置，格式为 `pos/length` 或仅 `pos`。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:201`*

---
<a id="sym-src_click__termui_impl.py-207"></a>
### `ProgressBar.format_pct` · method
```python
def format_pct(self) -> str
```

格式化进度条的百分比。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的百分比字符串。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:207`*

---
<a id="sym-src_click__termui_impl.py-210"></a>
### `ProgressBar.format_bar` · method
```python
def format_bar(self) -> str
```

### ProgressBar.format_bar

生成进度条的格式化字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的进度条字符串

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:210`*

---
<a id="sym-src_click__termui_impl.py-229"></a>
### `ProgressBar.format_progress_line` · method
```python
def format_progress_line(self) -> str
```

### ProgressBar.format_progress_line

格式化进度条的进度行。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的进度条进度行。

**Raises**:
- 无

**内部调用(库内):**
- [`ProgressBar.format_pos`](src_click.md#sym-src_click__termui_impl.py-201) — **用途**: 格式化进度条的当前位置。
- [`ProgressBar.format_pct`](src_click.md#sym-src_click__termui_impl.py-207) — 格式化进度条的百分比。
- [`ProgressBar.format_eta`](src_click.md#sym-src_click__termui_impl.py-180) — 用途: 格式化进度条的剩余时间。
- [`ProgressBar.format_bar`](src_click.md#sym-src_click__termui_impl.py-210) — ProgressBar.format_bar

*来源: `src/click/_termui_impl.py:229`*

---
<a id="sym-src_click__termui_impl.py-256"></a>
### `ProgressBar.render_progress` · method
```python
def render_progress(self) -> None
```

### ProgressBar.render_progress

Renders the progress bar to the output file.

**Parameters**:
- `self` — `ProgressBar` — The ProgressBar instance.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`term_len`](src_click.md#sym-src_click__compat.py-532) — 计算去除 ANSI 转义码后的字符串长度。
- [`ProgressBar.format_progress_line`](src_click.md#sym-src_click__termui_impl.py-229) — ProgressBar.format_progress_line

*来源: `src/click/_termui_impl.py:256`*

---
<a id="sym-src_click__termui_impl.py-302"></a>
### `ProgressBar.make_step` · method
```python
def make_step(self, n_steps: int) -> None
```

### ProgressBar.make_step

增加进度条的进度。

- **Parameters**:
  - `n_steps` — `int` — 增加的进度步数。
- **Returns**:
  - `None`
- **Raises**:
  - 无

*来源: `src/click/_termui_impl.py:302`*

---
<a id="sym-src_click__termui_impl.py-324"></a>
### `ProgressBar.update` · method
```python
def update(self, n_steps: int, current_item: V | None = None) -> None
```

**用途**: 更新进度条，通过增加指定的步数，并可选地设置当前位置的项目。

**Parameters**:
- `n_steps` — `int` — 要前进的步数。
- `current_item` — `V | None` — 可选参数，用于设置当前位置的项目。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`ProgressBar.make_step`](src_click.md#sym-src_click__termui_impl.py-302) — ProgressBar.make_step
- [`ProgressBar.render_progress`](src_click.md#sym-src_click__termui_impl.py-256) — ProgressBar.render_progress

*来源: `src/click/_termui_impl.py:324`*

---
<a id="sym-src_click__termui_impl.py-350"></a>
### `ProgressBar.finish` · method
```python
def finish(self) -> None
```

### ProgressBar.finish

结束进度条的显示。

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:350`*

---
<a id="sym-src_click__termui_impl.py-355"></a>
### `ProgressBar.generator` · method
```python
def generator(self) -> cabc.Iterator[V]
```

**用途**: 返回一个生成器，该生成器在构造进度条时逐个生成添加到进度条中的项目，并在生成器块返回后更新进度条。

**Parameters**:
- 无

**Returns**:
- `cabc.Iterator[V]`: 一个生成器，逐个生成添加到进度条中的项目。

**Raises**:
- `RuntimeError`: 如果在 `with` 块之外使用进度条。

**内部调用(库内):**
- [`ProgressBar.render_progress`](src_click.md#sym-src_click__termui_impl.py-256) — ProgressBar.render_progress
- [`ProgressBar.finish`](src_click.md#sym-src_click__termui_impl.py-350) — ProgressBar.finish

*来源: `src/click/_termui_impl.py:355`*

---
<a id="sym-src_click__termui_impl.py-389"></a>
### `MaybeStripAnsi` · class
```python
class MaybeStripAnsi(io.TextIOWrapper)
```

`MaybeStripAnsi` 类用于在输出中可能去除 ANSI 转义码，以确保在不支持 ANSI 的环境中正确显示文本。

### 方法

#### `__init__(self, stream: t.IO[bytes], *, color: bool, **kwargs: t.Any)`

- **参数**:
  - `stream` — `t.IO[bytes]` — 要包装的字节流。
  - `color` — `bool` — 是否去除 ANSI 转义码。
  - `**kwargs` — `t.Any` — 传递给 `io.TextIOWrapper` 的其他关键字参数。

- **返回**:
  - 无返回值。

#### `write(self, text: str) -> int`

- **参数**:
  - `text` — `str` — 要写入的文本。

- **返回**:
  - `int` — 写入的字符数。

- **异常**:
  - 无异常。

*来源: `src/click/_termui_impl.py:389`*

---
<a id="sym-src_click__termui_impl.py-390"></a>
### `MaybeStripAnsi.__init__` · method
```python
def __init__(self, stream: t.IO[bytes], *, color: bool, **kwargs: t.Any)
```

### `MaybeStripAnsi.__init__`

初始化 `MaybeStripAnsi` 类，用于可能去除 ANSI 转义码的流。

**Parameters**:
- `stream` — `t.IO[bytes]` — 输入流。
- `color` — `bool` — 是否去除 ANSI 转义码。
- `**kwargs` — `t.Any` — 其他关键字参数。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:390`*

---
<a id="sym-src_click__termui_impl.py-394"></a>
### `MaybeStripAnsi.write` · method
```python
def write(self, text: str) -> int
```

###用途
`MaybeStripAnsi.write` 方法用于在写入文本时，如果启用了颜色控制，则去除 ANSI 转义码。

###Parameters
- `text` — `str` — 要写入的文本。

###Returns
- `int` — 写入的字符数。

###Raises
- 无

**内部调用(库内):**
- [`strip_ansi`](src_click.md#sym-src_click__compat.py-487) — **用途**: 移除字符串中的 ANSI 转义码。

*来源: `src/click/_termui_impl.py:394`*

---
<a id="sym-src_click__termui_impl.py-400"></a>
### `_pager_contextmanager` · func
```python
def _pager_contextmanager(
    color: bool | None = None,
) -> t.ContextManager[tuple[t.BinaryIO | t.TextIO, str, bool]]
```

```markdown
Decide what method to use for paging through text.

**Parameters**:
- `color` — `bool | None` — Whether to enable color output.

**Returns**:
- `t.ContextManager[tuple[t.BinaryIO | t.TextIO, str, bool]]` — A context manager that provides a pager for text output.

**Raises**:
- None
```

**内部调用(库内):**
- [`_nullpager`](src_click.md#sym-src_click__termui_impl.py-637) — Simply print unformatted text. This is the ultimate fallback. Don't close the ou
- [`_tempfilepager`](src_click.md#sym-src_click__termui_impl.py-580) — Page through text by invoking a program on a temporary file.
- [`_pipepager`](src_click.md#sym-src_click__termui_impl.py-470) — Page through text by feeding it to another program.

*来源: `src/click/_termui_impl.py:400`*

---
<a id="sym-src_click__termui_impl.py-432"></a>
### `get_pager_file` · func
装饰器: `@contextlib.contextmanager`
```python
def get_pager_file(color: bool | None = None) -> t.Generator[t.TextIO, None, None]
```

**用途**: 提供一个上下文管理器，用于生成一个可写文件对象，该对象可以作为输出分页器使用。

**Parameters**:
- `color` — `bool | None` — 控制分页器是否支持 ANSI 颜色。默认为自动检测。

**Returns**:
- `t.Generator[t.TextIO, None, None]` — 一个生成器，每次迭代时返回一个可写文件对象，该对象可以用于分页输出。

**Raises**:
- 无

**内部调用(库内):**
- [`_pager_contextmanager`](src_click.md#sym-src_click__termui_impl.py-400) — ```markdown
- [`_has_binary_buffer`](src_click.md#sym-src_click__termui_impl.py-41) — 检查给定的流是否具有二进制缓冲区。
- [`MaybeStripAnsi`](src_click.md#sym-src_click__termui_impl.py-389) — `MaybeStripAnsi` 类用于在输出中可能去除 ANSI 转义码，以确保在不支持 ANSI 的环境中正确显示文本。

*来源: `src/click/_termui_impl.py:432`*

---
<a id="sym-src_click__termui_impl.py-470"></a>
### `_pipepager` · func
装饰器: `@contextlib.contextmanager`
```python
def _pipepager(
    cmd_parts: list[str], color: bool | None = None
) -> t.Iterator[tuple[t.BinaryIO | t.TextIO, str, bool]]
```

Page through text by feeding it to another program.

**Parameters**:
- `cmd_parts` — `list[str]` — The command and its parameters to be executed.
- `color` — `bool | None` — Whether to enable color support in the pager.

**Returns**:
- `t.Iterator[tuple[t.BinaryIO | t.TextIO, str, bool]]` — An iterator yielding tuples containing the pager stream, the command used, and a boolean indicating if color support is enabled.

**Raises**:
- None

**内部调用(库内):**
- [`_nullpager`](src_click.md#sym-src_click__termui_impl.py-637) — Simply print unformatted text. This is the ultimate fallback. Don't close the ou
- [`Path`](src_click.md#sym-src_click_types.py-1001) — `Path` 类用于处理文件路径，提供验证和转换路径的功能。
- [`get_best_encoding`](src_click.md#sym-src_click__compat.py-47) — Returns the best encoding for the given stream.

*来源: `src/click/_termui_impl.py:470`*

---
<a id="sym-src_click__termui_impl.py-580"></a>
### `_tempfilepager` · func
装饰器: `@contextlib.contextmanager`
```python
def _tempfilepager(
    cmd_parts: list[str], color: bool | None = None
) -> t.Iterator[tuple[t.BinaryIO | t.TextIO, str, bool]]
```

Page through text by invoking a program on a temporary file.

**Parameters**:
- `cmd_parts` — `list[str]` — The command parts to invoke.
- `color` — `bool | None` — Whether to enable color output.

**Returns**:
- `t.Iterator[tuple[t.BinaryIO | t.TextIO, str, bool]]` — An iterator yielding tuples of the pager stream, the pager command, and a boolean indicating whether color is enabled.

**Raises**:
- None

**内部调用(库内):**
- [`_nullpager`](src_click.md#sym-src_click__termui_impl.py-637) — Simply print unformatted text. This is the ultimate fallback. Don't close the ou
- [`Path`](src_click.md#sym-src_click_types.py-1001) — `Path` 类用于处理文件路径，提供验证和转换路径的功能。
- [`get_best_encoding`](src_click.md#sym-src_click__compat.py-47) — Returns the best encoding for the given stream.

*来源: `src/click/_termui_impl.py:580`*

---
<a id="sym-src_click__termui_impl.py-637"></a>
### `_nullpager` · func
装饰器: `@contextlib.contextmanager`
```python
def _nullpager(
    stream: t.TextIO, color: bool | None = None
) -> t.Iterator[tuple[t.TextIO, str, bool]]
```

Simply print unformatted text. This is the ultimate fallback. Don't close the output stream in this case, since it's coming from elsewhere rather than our internal helpers.

**Parameters**:
- stream — t.TextIO — The input stream to be printed.
- color — bool | None — Whether to enable color output. If None, defaults to False.

**Returns**:
- t.Iterator[tuple[t.TextIO, str, bool]] — An iterator yielding a tuple containing the wrapped stream, the encoding, and the color flag.

**Raises**:
- None

**内部调用(库内):**
- [`get_best_encoding`](src_click.md#sym-src_click__compat.py-47) — Returns the best encoding for the given stream.
- [`KeepOpenFile`](src_click.md#sym-src_click_utils.py-206) — `KeepOpenFile` 类用于包装一个文件对象，确保在上下文管理器中使用时文件保持打开状态，直到显式关闭。

*来源: `src/click/_termui_impl.py:637`*

---
<a id="sym-src_click__termui_impl.py-656"></a>
### `Editor` · class
```python
class Editor
```

`Editor` 类用于管理文本编辑器的配置和操作，提供编辑文件和文本的功能。

- **Parameters**:
  - `editor` — `str | None` — 指定要使用的编辑器，例如 "vim" 或 "nano"。如果未指定，将使用环境变量中的 `EDITOR` 或 `VISUAL`。
  - `env` — `cabc.Mapping[str, str] | None` — 传递给编辑器的环境变量。
  - `require_save` — `bool` — 是否要求编辑器保存更改。默认为 `True`。
  - `extension` — `str` — 编辑文件的默认扩展名。默认为 `.txt`。

- **Returns**:
  - `None`

- **Raises**:
  - `None`

### 关键方法

- **get_editor()**
  - **Returns**:
    - `str` — 当前配置的编辑器名称。

- **edit_files(filenames: cabc.Iterable[str])**
  - **Parameters**:
    - `filenames` — `cabc.Iterable[str]` — 要编辑的文件名列表。
  - **Returns**:
    - `None`

- **edit(text: bytes | bytearray) -> bytes | None**
  - **Parameters**:
    - `text` — `bytes | bytearray` — 要编辑的二进制文本。
  - **Returns**:
    - `bytes | None` — 编辑后的二进制

*来源: `src/click/_termui_impl.py:656`*

---
<a id="sym-src_click__termui_impl.py-657"></a>
### `Editor.__init__` · method
```python
def __init__(
        self,
        editor: str | None = None,
        env: cabc.Mapping[str, str] | None = None,
        require_save: bool = True,
        extension: str = ".txt",
    ) -> None
```

初始化一个 `Editor` 对象。

**Parameters**:
- `editor` — `str | None` — 编辑器的路径，如果为 `None`，则使用系统默认编辑器。
- `env` — `cabc.Mapping[str, str] | None` — 传递给编辑器的环境变量。
- `require_save` — `bool` — 是否要求编辑器保存文件。
- `extension` — `str` — 文件的扩展名，默认为 `.txt`。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:657`*

---
<a id="sym-src_click__termui_impl.py-669"></a>
### `Editor.get_editor` · method
```python
def get_editor(self) -> str
```

获取当前编辑器的名称。

**Parameters**:
- 无

**Returns**:
- `str`: 当前编辑器的名称。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:669`*

---
<a id="sym-src_click__termui_impl.py-686"></a>
### `Editor.edit_files` · method
```python
def edit_files(self, filenames: cabc.Iterable[str]) -> None
```

Open files in the user's editor.

**Parameters**:
- `filenames` — `cabc.Iterable[str]` — The files to edit.

**Returns**:
- `None`

**Raises**:
- `ClickException` — If the editor fails to open or if the editing process exits with a non-zero status.

**内部调用(库内):**
- [`Editor.get_editor`](src_click.md#sym-src_click__termui_impl.py-669) — 获取当前编辑器的名称。
- [`ClickException`](src_click.md#sym-src_click_exceptions.py-35) — `ClickException` 是 Click 库中用于表示各种异常的基类。

*来源: `src/click/_termui_impl.py:686`*

---
<a id="sym-src_click__termui_impl.py-717"></a>
### `Editor.edit` · method
装饰器: `@t.overload`
```python
def edit(self, text: bytes | bytearray) -> bytes | None
```

### `Editor.edit`

编辑给定的文本并返回编辑后的文本。

**Parameters**:
- `text` — `bytes | bytearray` — 要编辑的文本。

**Returns**:
- `bytes | None` — 编辑后的文本，如果编辑失败则返回 `None`。

*来源: `src/click/_termui_impl.py:717`*

---
<a id="sym-src_click__termui_impl.py-722"></a>
### `Editor.edit` · method
装饰器: `@t.overload`
```python
def edit(self, text: str | None) -> str | None
```

###用途
编辑给定的文本并返回编辑后的文本。

###Parameters
- `text` — `str | None` — 要编辑的文本，如果为 `None`，则表示没有文本。

###Returns
- `str | None` — 编辑后的文本，如果原始文本为 `None`，则返回 `None`。

###Raises
- 无

*来源: `src/click/_termui_impl.py:722`*

---
<a id="sym-src_click__termui_impl.py-724"></a>
### `Editor.edit` · method
```python
def edit(self, text: str | bytes | bytearray | None) -> str | bytes | None
```

用途: 使用系统编辑器打开并编辑给定的文本。

**Parameters**:
- `text` — `str | bytes | bytearray | None` — 要编辑的文本内容，可以是字符串、字节或字节数组，也可以是 `None`。

**Returns**:
- `str | bytes | None` — 编辑后的内容，如果用户没有保存更改，则返回 `None`。

**Raises**:
- `ClickException` — 如果在编辑过程中发生错误。

**内部调用(库内):**
- [`Editor.edit_files`](src_click.md#sym-src_click__termui_impl.py-686) — Open files in the user's editor.

*来源: `src/click/_termui_impl.py:724`*

---
<a id="sym-src_click__termui_impl.py-772"></a>
### `open_url` · func
```python
def open_url(url: str, wait: bool = False, locate: bool = False) -> int
```

用途: 打开指定 URL 并根据需要等待或定位。

**Parameters**:
- `url` — `str` — 要打开的 URL。
- `wait` — `bool` — 是否等待 URL 页面加载完成。默认为 `False`。
- `locate` — `bool` — 是否定位到 URL 文件。默认为 `False`。

**Returns**:
- `int` — 进程退出状态码。

**Raises**:
- 无

**内部调用(库内):**
- [`_unquote_file`](src_click.md#sym-src_click__termui_impl.py-775) — _unquote_file

*来源: `src/click/_termui_impl.py:772`*

---
<a id="sym-src_click__termui_impl.py-775"></a>
### `_unquote_file` · func
```python
def _unquote_file(url: str) -> str
```

### _unquote_file

Unquotes a file URL by removing the "file://" prefix and decoding the URL.

**Parameters**:
- `url` — `str` — The file URL to unquote.

**Returns**:
- `str` — The unquoted file path.

**Raises**:
- (None)

*来源: `src/click/_termui_impl.py:775`*

---
<a id="sym-src_click__termui_impl.py-842"></a>
### `_translate_ch_to_exc` · func
```python
def _translate_ch_to_exc(ch: str) -> None
```

### _translate_ch_to_exc

Translates specific control characters to exceptions.

**Parameters**:
- `ch` — `str` — The control character to translate.

**Raises**:
- `KeyboardInterrupt` — If the control character is `"\x03"` (Ctrl+C).
- `EOFError` — If the control character is `"\x04"` (Ctrl+D) on Unix-like systems or `"\x1a"` (Ctrl+Z) on Windows.

*来源: `src/click/_termui_impl.py:842`*

---
<a id="sym-src_click__termui_impl.py-857"></a>
### `raw_terminal` · func
装饰器: `@contextlib.contextmanager`
```python
def raw_terminal() -> cabc.Iterator[int]
```

提供一个生成器，每次迭代返回 `-1`。

**Parameters**:
- 无

**Returns**:
- `cabc.Iterator[int]`: 一个生成器，每次迭代返回 `-1`。

**Raises**:
- 无

*来源: `src/click/_termui_impl.py:857`*

---
<a id="sym-src_click__termui_impl.py-860"></a>
### `getchar` · func
```python
def getchar(echo: bool) -> str:
        # The function `getch` will return a bytes object corresponding to
        # the pressed character. Since Windows 10 build 1803, it will also
        # return \x00 when called a second time after pressing a regular key.
        #
        # `getwch` does not share this probably-bugged behavior. Moreover, it
        # returns a Unicode object by default, which is what we want.
        #
        # Either of these functions will return \x00 or \xe0 to indicate
        # a special key, and you need to call the same function again to get
        # the "rest" of the code. The fun part is that \u00e0 is
        # "latin small letter a with grave", so if you type that on a French
        # keyboard, you _also_ get a \xe0.
        # E.g., consider the Up arrow. This returns \xe0 and then \x48. The
        # resulting Unicode string reads as "a with grave" + "capital H".
        # This is indistinguishable from when the user actually types
        # "a with grave" and then "capital H".
        #
        # When \xe0 is returned, we assume it's part of a special-key sequence
        # and call `getwch` again, but that means that when the user types
        # the \u00e0 character, `getchar` doesn't return until a second
        # character is typed.
        # The alternative is returning immediately, but that would mess up
        # cross-platform handling of arrow keys and others that start with
        # \xe0. Another option is using `getch`, but then we can't reliably
        # read non-ASCII characters, because return values of `getch` are
        # limited to the current 8-bit codepage.
        #
        # Anyway, Click doesn't claim to do this Right(tm), and using `getwch`
        # is doing the right thing in more situations than with `getch`.
```

获取用户输入的单个字符。

**Parameters**:
- `echo` — `bool` — 是否回显输入的字符。

**Returns**:
- `str` — 用户输入的单个字符。

**Raises**:
- 无

**内部调用(库内):**
- [`func`](src_click.md#sym-src_click__compat.py-549) — func
- [`_translate_ch_to_exc`](src_click.md#sym-src_click__termui_impl.py-842) — _translate_ch_to_exc

*来源: `src/click/_termui_impl.py:860`*

---
<a id="sym-src_click__termui_impl.py-911"></a>
### `raw_terminal` · func
装饰器: `@contextlib.contextmanager`
```python
def raw_terminal() -> cabc.Iterator[int]
```

### `raw_terminal`

获取一个原始终端文件描述符的迭代器。

**Parameters**:
- 无

**Returns**:
- `Iterator[int]`: 一个迭代器，每次迭代返回一个原始终端文件描述符。

**Raises**:
- `termios.error`: 如果在设置终端为原始模式时发生错误。

*来源: `src/click/_termui_impl.py:911`*

---
<a id="sym-src_click__termui_impl.py-937"></a>
### `getchar` · func
```python
def getchar(echo: bool) -> str
```

读取一个字符并返回。

**Parameters**:
- `echo` — `bool` — 是否在读取后回显字符到标准输出。

**Returns**:
- `str` — 读取的字符。

**Raises**:
- 无

**内部调用(库内):**
- [`raw_terminal`](src_click.md#sym-src_click__termui_impl.py-857) — 提供一个生成器，每次迭代返回 `-1`。
- [`get_best_encoding`](src_click.md#sym-src_click__compat.py-47) — Returns the best encoding for the given stream.
- [`_translate_ch_to_exc`](src_click.md#sym-src_click__termui_impl.py-842) — _translate_ch_to_exc

*来源: `src/click/_termui_impl.py:937`*

---

## `src/click/_textwrap.py`

<a id="sym-src_click__textwrap.py-11"></a>
### `_truncate_visible` · func
```python
def _truncate_visible(text: str, n: int) -> str
```

**用途**: 返回 `text` 的最长前缀，该前缀包含最多 `n` 个可见字符。ANSI 转义序列在前缀中保持完整，不计入可见宽度。切勿在转义序列内部进行切割。

**Parameters**:
- `text` — `str` — 输入的文本。
- `n` — `int` — 最大可见字符数。

**Returns**:
- `str` — 最长的可见字符前缀。

**Raises**:
- 无

*来源: `src/click/_textwrap.py:11`*

---
<a id="sym-src_click__textwrap.py-38"></a>
### `TextWrapper` · class
```python
class TextWrapper(textwrap.TextWrapper)
```

`TextWrapper` 类用于处理文本的换行和格式化，确保文本在指定宽度内正确显示。

### 方法

- **_handle_long_word**
  - **Parameters**:
    - `reversed_chunks` — `list[str]` — 反转的文本块列表。
    - `cur_line` — `list[str]` — 当前行的文本块列表。
    - `cur_len` — `int` — 当前行的长度。
    - `width` — `int` — 文本块的最大宽度。
  - **Returns**: `None`

- **_wrap_chunks**
  - **Parameters**:
    - `chunks` — `list[str]` — 需要换行的文本块列表。
  - **Returns**:
    - `list[str]` — 换行后的文本块列表。

- **extra_indent**
  - **Parameters**:
    - `indent` — `str` — 额外的缩进字符串。
  - **Returns**:
    - `cabc.Iterator[None]` — 一个迭代器，用于处理额外的缩进。

- **indent_only**
  - **Parameters**:
    - `text` — `str` — 需要缩进的文本。
  - **Returns**:
    - `str` — 缩进后的文本。

*来源: `src/click/_textwrap.py:38`*

---
<a id="sym-src_click__textwrap.py-48"></a>
### `TextWrapper._handle_long_word` · method
```python
def _handle_long_word(
        self,
        reversed_chunks: list[str],
        cur_line: list[str],
        cur_len: int,
        width: int,
    ) -> None
```

### `_handle_long_word`

处理过长的单词，根据 `break_long_words` 的设置决定是否截断单词或将其单独放在新行。

**Parameters**:
- `reversed_chunks` — `list[str]` — 逆序的文本块列表。
- `cur_line` — `list[str]` — 当前行的文本块列表。
- `cur_len` — `int` — 当前行的当前长度。
- `width` — `int` — 文本的总宽度。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`_truncate_visible`](src_click.md#sym-src_click__textwrap.py-11) — **用途**: 返回 `text` 的最长前缀，该前缀包含最多 `n` 个可见字符。ANSI 转义序列在前缀中保持完整，不计入可见宽度。切勿在转义序列内部进行切

*来源: `src/click/_textwrap.py:48`*

---
<a id="sym-src_click__textwrap.py-66"></a>
### `TextWrapper._wrap_chunks` · method
```python
def _wrap_chunks(self, chunks: list[str]) -> list[str]
```

Wrap chunks counting widths in visible characters.

**Parameters**:
- `chunks` — `list[str]` — The list of text chunks to wrap.

**Returns**:
- `list[str]` — The wrapped list of text chunks.

**Raises**:
- `ValueError` — If the width is less than or equal to 0.
- `ValueError` — If the placeholder is too large for the maximum width.

**内部调用(库内):**
- [`term_len`](src_click.md#sym-src_click__compat.py-532) — 计算去除 ANSI 转义码后的字符串长度。
- [`TextWrapper._handle_long_word`](src_click.md#sym-src_click__textwrap.py-48) — `_handle_long_word`

*来源: `src/click/_textwrap.py:66`*

---
<a id="sym-src_click__textwrap.py-165"></a>
### `TextWrapper.extra_indent` · method
装饰器: `@contextmanager`
```python
def extra_indent(self, indent: str) -> cabc.Iterator[None]
```

增加文本包装器的缩进。

**Parameters**:
- `indent` — `str` — 要添加的缩进字符串。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/_textwrap.py:165`*

---
<a id="sym-src_click__textwrap.py-177"></a>
### `TextWrapper.indent_only` · method
```python
def indent_only(self, text: str) -> str
```

对文本进行缩进处理。

**Parameters**:
- `text` — `str` — 需要缩进的文本。

**Returns**:
- `str` — 缩进后的文本。

**Raises**:
- 无

*来源: `src/click/_textwrap.py:177`*

---

## `src/click/_utils.py`

<a id="sym-src_click__utils.py-7"></a>
### `Sentinel` · class
```python
class Sentinel(enum.Enum)
```

`Sentinel` 类代表一个特殊的枚举类型，用于在代码中表示一些特殊的标记或状态。

- **Parameters**:
  - 无

- **Returns**:
  - `str`: 返回 Sentinel 枚举成员的字符串表示。

- **Raises**:
  - 无

*来源: `src/click/_utils.py:7`*

---
<a id="sym-src_click__utils.py-18"></a>
### `Sentinel.__repr__` · method
```python
def __repr__(self) -> str
```

用途: 返回 Sentinel 对象的字符串表示。

**Parameters**:
- 无

**Returns**:
- `str`: Sentinel 对象的字符串表示，格式为 `{self.__class__.__name__}.{self.name}`。

**Raises**:
- 无

*来源: `src/click/_utils.py:18`*

---

## `src/click/_winconsole.py`

<a id="sym-src_click__winconsole.py-88"></a>
### `Py_buffer` · class
```python
class Py_buffer(Structure)
```

`Py_buffer` 类代表一个用于处理 Python 缓冲区的结构体。

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| 无 | 无 | 无 |

| 返回 | 类型 | 含义 |
| --- | --- | --- |
| 无 | 无 | 无 |

| 异常 | 类型 | 含义 |
| --- | --- | --- |
| 无 | 无 | 无 |

`Py_buffer` 类用于处理 Python 缓冲区，通常在与 C 扩展模块交互时使用。它定义了缓冲区的结构，包括缓冲区的指针、大小和步长等信息。

*来源: `src/click/_winconsole.py:88`*

---
<a id="sym-src_click__winconsole.py-106"></a>
### `get_buffer` · func
```python
def get_buffer(obj: Buffer, writable: bool = False) -> Array[c_char]
```

获取一个对象的缓冲区。

**Parameters**:
- `obj` — `Buffer` — 要获取缓冲区的对象。
- `writable` — `bool` — 是否可写，默认为 `False`。

**Returns**:
- `Array[c_char]` — 缓冲区的内容。

**Raises**:
- 无

**内部调用(库内):**
- [`Py_buffer`](src_click.md#sym-src_click__winconsole.py-88) — `Py_buffer` 类代表一个用于处理 Python 缓冲区的结构体。

*来源: `src/click/_winconsole.py:106`*

---
<a id="sym-src_click__winconsole.py-119"></a>
### `_WindowsConsoleRawIOBase` · class
```python
class _WindowsConsoleRawIOBase(io.RawIOBase)
```

`_WindowsConsoleRawIOBase` 类代表一个用于 Windows 控制台的原始输入输出基类，主要用于处理控制台的原始输入和输出操作。

### 方法

- **`__init__(self, handle: int | None) -> None`**
  - **Parameters**:
    - `handle` — `int | None` — 控制台句柄，可以是整数或 `None`。
  - **Returns**:
    - `None`
  - **Raises**:
    - 无

- **`isatty(self) -> t.Literal[True]`**
  - **Parameters**:
    - 无
  - **Returns**:
    - `t.Literal[True]` — 始终返回 `True`，表示该对象是一个终端。
  - **Raises**:
    - 无

*来源: `src/click/_winconsole.py:119`*

---
<a id="sym-src_click__winconsole.py-120"></a>
### `_WindowsConsoleRawIOBase.__init__` · method
```python
def __init__(self, handle: int | None) -> None
```

初始化 Windows 控制台的原始 I/O 对象。

**Parameters**:
- `handle` — `int | None` — 控制台句柄。

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/_winconsole.py:120`*

---
<a id="sym-src_click__winconsole.py-123"></a>
### `_WindowsConsoleRawIOBase.isatty` · method
```python
def isatty(self) -> t.Literal[True]
```

用途: 返回 `True`，表示该流是一个终端。

**Parameters**:
- 无

**Returns**:
- `t.Literal[True]`: 表示该流是一个终端。

**Raises**:
- 无

*来源: `src/click/_winconsole.py:123`*

---
<a id="sym-src_click__winconsole.py-128"></a>
### `_WindowsConsoleReader` · class
```python
class _WindowsConsoleReader(_WindowsConsoleRawIOBase)
```

`_WindowsConsoleReader` 是一个用于在 Windows 控制台中读取输入的类，继承自 `_WindowsConsoleRawIOBase`。

- **readable(self) -> t.Literal[True]**: 返回 `True`，表示该对象是可读的。
- **readinto(self, b: Buffer) -> int**: 从控制台读取数据并写入到缓冲区 `b` 中，返回实际读取的字节数。

*来源: `src/click/_winconsole.py:128`*

---
<a id="sym-src_click__winconsole.py-129"></a>
### `_WindowsConsoleReader.readable` · method
```python
def readable(self) -> t.Literal[True]
```

**用途**: 返回一个布尔值，表示该 Windows 控制台读取器是可读的。

**Parameters**:
- 无

**Returns**:
- `t.Literal[True]`: 布尔值 `True`，表示该 Windows 控制台读取器是可读的。

*来源: `src/click/_winconsole.py:129`*

---
<a id="sym-src_click__winconsole.py-132"></a>
### `_WindowsConsoleReader.readinto` · method
```python
def readinto(self, b: Buffer) -> int
```

从 Windows 控制台读取指定数量的字节到缓冲区。

**Parameters**:
- `b` — `Buffer` — 要读取到的缓冲区。

**Returns**:
- `int` — 读取的字节数。

**Raises**:
- `ValueError` — 如果要读取的字节数是奇数。
- `OSError` — 如果 Windows 操作失败。

**内部调用(库内):**
- [`get_buffer`](src_click.md#sym-src_click__winconsole.py-106) — 获取一个对象的缓冲区。

*来源: `src/click/_winconsole.py:132`*

---
<a id="sym-src_click__winconsole.py-163"></a>
### `_WindowsConsoleWriter` · class
```python
class _WindowsConsoleWriter(_WindowsConsoleRawIOBase)
```

`_WindowsConsoleWriter` 类是用于 Windows 控制台的写入操作的抽象基类，负责处理控制台的写入操作。

- **writable(self) -> t.Literal[True]**: 返回 `True`，表示该对象是可写的。
- **_get_error_message(errno: int) -> str**: 根据错误码 `errno` 返回相应的错误信息。
- **write(self, b: Buffer) -> int**: 将缓冲区 `b` 中的数据写入控制台，并返回实际写入的字节数。

*来源: `src/click/_winconsole.py:163`*

---
<a id="sym-src_click__winconsole.py-164"></a>
### `_WindowsConsoleWriter.writable` · method
```python
def writable(self) -> t.Literal[True]
```

### _WindowsConsoleWriter.writable

返回 `True`，表示该写入器是可写的。

**Parameters**:
- 无

**Returns**:
- `t.Literal[True]` — 表示该写入器是可写的。

*来源: `src/click/_winconsole.py:164`*

---
<a id="sym-src_click__winconsole.py-168"></a>
### `_WindowsConsoleWriter._get_error_message` · method
装饰器: `@staticmethod`
```python
def _get_error_message(errno: int) -> str
```

### _WindowsConsoleWriter._get_error_message

获取 Windows 错误消息。

**Parameters**:
- `errno` — `int` — 错误码

**Returns**:
- `str` — 错误消息

**Raises**:
- 无

*来源: `src/click/_winconsole.py:168`*

---
<a id="sym-src_click__winconsole.py-175"></a>
### `_WindowsConsoleWriter.write` · method
```python
def write(self, b: Buffer) -> int
```

### _WindowsConsoleWriter.write

Writes data to the Windows console.

**Parameters:**

- `b` — `Buffer` — The data to write to the console.

**Returns:**

- `int` — The number of bytes written to the console.

**Raises:**

- `OSError` — If an error occurs during the write operation.

**内部调用(库内):**
- [`get_buffer`](src_click.md#sym-src_click__winconsole.py-106) — 获取一个对象的缓冲区。
- [`_WindowsConsoleWriter._get_error_message`](src_click.md#sym-src_click__winconsole.py-168) — _WindowsConsoleWriter._get_error_message

*来源: `src/click/_winconsole.py:175`*

---
<a id="sym-src_click__winconsole.py-195"></a>
### `ConsoleStream` · class
```python
class ConsoleStream
```

`ConsoleStream` 类用于处理控制台输入输出流，提供了一个统一的接口来处理文本和二进制数据。

- **Parameters**:
  - `text_stream` — `t.TextIO` — 文本输入输出流。
  - `byte_stream` — `t.BinaryIO` — 二进制输入输出流。

- **Returns**:
  - 无

- **Raises**:
  - 无

### 关键方法

- **name(self) -> str**
  - **Returns**:
    - `str` — 返回流的名称。

- **write(self, x: t.AnyStr) -> int**
  - **Parameters**:
    - `x` — `t.AnyStr` — 要写入的数据。
  - **Returns**:
    - `int` — 写入的字符数。

- **writelines(self, lines: cabc.Iterable[t.AnyStr]) -> None**
  - **Parameters**:
    - `lines` — `cabc.Iterable[t.AnyStr]` — 要写入的行列表。

- **__getattr__(self, name: str) -> t.Any**
  - **Parameters**:
    - `name` — `str` — 要获取的属性名。
  - **Returns**:
    - `t.Any` — 属性值。

- **isatty(self) -> bool**
  - **Returns**:
    - `bool` — 如果流是交互式的则返回 `True`，

*来源: `src/click/_winconsole.py:195`*

---
<a id="sym-src_click__winconsole.py-196"></a>
### `ConsoleStream.__init__` · method
```python
def __init__(self, text_stream: t.TextIO, byte_stream: t.BinaryIO) -> None
```

初始化一个 `ConsoleStream` 对象。

**Parameters**:
- `text_stream` — `t.TextIO` — 用于文本操作的流。
- `byte_stream` — `t.BinaryIO` — 用于字节操作的流。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/_winconsole.py:196`*

---
<a id="sym-src_click__winconsole.py-201"></a>
### `ConsoleStream.name` · method
装饰器: `@property`
```python
def name(self) -> str
```

获取当前缓冲区的名称。

**Parameters**:
- 无

**Returns**:
- `str`: 当前缓冲区的名称。

**Raises**:
- 无

*来源: `src/click/_winconsole.py:201`*

---
<a id="sym-src_click__winconsole.py-204"></a>
### `ConsoleStream.write` · method
```python
def write(self, x: t.AnyStr) -> int
```

### ConsoleStream.write

Writes a string or bytes to the stream. If the input is a string, it writes to the text stream; otherwise, it flushes the stream and writes to the buffer.

**Parameters**:
- `x` — `t.AnyStr` — The string or bytes to write.

**Returns**:
- `int` — The number of bytes written.

**Raises**:
- None

*来源: `src/click/_winconsole.py:204`*

---
<a id="sym-src_click__winconsole.py-213"></a>
### `ConsoleStream.writelines` · method
```python
def writelines(self, lines: cabc.Iterable[t.AnyStr]) -> None
```

### ConsoleStream.writelines

写入多行字符串到控制台流中。

**Parameters**:
- `lines` — `cabc.Iterable[t.AnyStr]` — 要写入的多行字符串。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/_winconsole.py:213`*

---
<a id="sym-src_click__winconsole.py-217"></a>
### `ConsoleStream.__getattr__` · method
```python
def __getattr__(self, name: str) -> t.Any
```

用途: 通过代理访问 `_text_stream` 对象的属性和方法。

**Parameters**:
- `name` — `str` — 要访问的属性或方法的名称。

**Returns**:
- `t.Any` — `_text_stream` 对象上指定属性或方法的返回值。

**Raises**:
- 无

*来源: `src/click/_winconsole.py:217`*

---
<a id="sym-src_click__winconsole.py-220"></a>
### `ConsoleStream.isatty` · method
```python
def isatty(self) -> bool
```

检查当前流是否连接到一个终端。

- **Parameters**:
  - 无

- **Returns**:
  - `bool`: 如果流连接到一个终端则返回 `True`，否则返回 `False`。

- **Raises**:
  - 无

*来源: `src/click/_winconsole.py:220`*

---
<a id="sym-src_click__winconsole.py-223"></a>
### `ConsoleStream.__repr__` · method
```python
def __repr__(self) -> str
```

返回一个表示 `ConsoleStream` 对象的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 表示 `ConsoleStream` 对象的字符串。

**Raises**:
- 无

*来源: `src/click/_winconsole.py:223`*

---
<a id="sym-src_click__winconsole.py-227"></a>
### `_get_text_stdin` · func
```python
def _get_text_stdin(buffer_stream: t.BinaryIO) -> t.TextIO
```

**用途**: 获取一个文本输入流，用于从标准输入读取数据。

**Parameters**:
- `buffer_stream` — `t.BinaryIO` — 一个二进制输入流，用于缓冲输入数据。

**Returns**:
- `t.TextIO` — 一个文本输入流，用于从标准输入读取数据。

**Raises**:
- 无

**内部调用(库内):**
- [`_NonClosingTextIOWrapper`](src_click.md#sym-src_click__compat.py-55) — `_NonClosingTextIOWrapper` 是一个用于包装二进制流的类，提供文本I/O操作，同时确保流在关闭时不会被意外关闭。
- [`_WindowsConsoleReader`](src_click.md#sym-src_click__winconsole.py-128) — `_WindowsConsoleReader` 是一个用于在 Windows 控制台中读取输入的类，继承自 `_WindowsConsoleRawIOBase`
- [`ConsoleStream`](src_click.md#sym-src_click__winconsole.py-195) — `ConsoleStream` 类用于处理控制台输入输出流，提供了一个统一的接口来处理文本和二进制数据。

*来源: `src/click/_winconsole.py:227`*

---
<a id="sym-src_click__winconsole.py-237"></a>
### `_get_text_stdout` · func
```python
def _get_text_stdout(buffer_stream: t.BinaryIO) -> t.TextIO
```

获取文本标准输出流。

**Parameters**:
- `buffer_stream` — `t.BinaryIO` — 缓冲流。

**Returns**:
- `t.TextIO` — 文本标准输出流。

**Raises**:
- 无

**内部调用(库内):**
- [`_NonClosingTextIOWrapper`](src_click.md#sym-src_click__compat.py-55) — `_NonClosingTextIOWrapper` 是一个用于包装二进制流的类，提供文本I/O操作，同时确保流在关闭时不会被意外关闭。
- [`_WindowsConsoleWriter`](src_click.md#sym-src_click__winconsole.py-163) — `_WindowsConsoleWriter` 类是用于 Windows 控制台的写入操作的抽象基类，负责处理控制台的写入操作。
- [`ConsoleStream`](src_click.md#sym-src_click__winconsole.py-195) — `ConsoleStream` 类用于处理控制台输入输出流，提供了一个统一的接口来处理文本和二进制数据。

*来源: `src/click/_winconsole.py:237`*

---
<a id="sym-src_click__winconsole.py-247"></a>
### `_get_text_stderr` · func
```python
def _get_text_stderr(buffer_stream: t.BinaryIO) -> t.TextIO
```

获取标准错误输出的文本流。

**Parameters**:
- buffer_stream — t.BinaryIO — 二进制缓冲流。

**Returns**:
- t.TextIO — 文本流。

**Raises**:
- 无

**内部调用(库内):**
- [`_NonClosingTextIOWrapper`](src_click.md#sym-src_click__compat.py-55) — `_NonClosingTextIOWrapper` 是一个用于包装二进制流的类，提供文本I/O操作，同时确保流在关闭时不会被意外关闭。
- [`_WindowsConsoleWriter`](src_click.md#sym-src_click__winconsole.py-163) — `_WindowsConsoleWriter` 类是用于 Windows 控制台的写入操作的抽象基类，负责处理控制台的写入操作。
- [`ConsoleStream`](src_click.md#sym-src_click__winconsole.py-195) — `ConsoleStream` 类用于处理控制台输入输出流，提供了一个统一的接口来处理文本和二进制数据。

*来源: `src/click/_winconsole.py:247`*

---
<a id="sym-src_click__winconsole.py-264"></a>
### `_is_console` · func
```python
def _is_console(f: t.TextIO) -> bool
```

检查给定的文件对象是否是控制台。

**Parameters**:
- `f` — `t.TextIO` — 要检查的文件对象。

**Returns**:
- `bool` — 如果文件对象是控制台则返回 `True`，否则返回 `False`。

**Raises**:
- `OSError` — 如果无法获取文件描述符。
- `io.UnsupportedOperation` — 如果文件对象不支持文件操作。

*来源: `src/click/_winconsole.py:264`*

---
<a id="sym-src_click__winconsole.py-277"></a>
### `_get_windows_console_stream` · func
```python
def _get_windows_console_stream(
    f: t.TextIO, encoding: str | None, errors: str | None
) -> t.TextIO | None
```

获取 Windows 控制台流。

**Parameters**:
- f — t.TextIO — 文件对象。
- encoding — str | None — 编码。
- errors — str | None — 错误处理方式。

**Returns**:
- t.TextIO | None — 控制台流或 None。

**Raises**:
- 无

**内部调用(库内):**
- [`_is_console`](src_click.md#sym-src_click__winconsole.py-264) — 检查给定的文件对象是否是控制台。
- [`func`](src_click.md#sym-src_click__compat.py-549) — func

*来源: `src/click/_winconsole.py:277`*

---

## `src/click/core.py`

<a id="sym-src_click_core.py-59"></a>
### `_complete_visible_commands` · func
```python
def _complete_visible_commands(
    ctx: Context, incomplete: str
) -> cabc.Iterator[tuple[str, Command]]
```

List all the subcommands of a group that start with the incomplete value and aren't hidden.

**Parameters**:
- `ctx` — `Context` — Invocation context for the group.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns**:
- `cabc.Iterator[tuple[str, Command]]` — Iterator yielding tuples of command name and command object.

**Raises**:
- None

**内部调用(库内):**
- [`Group.list_commands`](src_click.md#sym-src_click_core.py-1895) — Returns a list of subcommand names in the order they should appear.
- [`Group.get_command`](src_click.md#sym-src_click_core.py-1889) — Given a context and a command name, this method returns a `Command` object if it

*来源: `src/click/core.py:59`*

---
<a id="sym-src_click_core.py-78"></a>
### `_check_nested_chain` · func
```python
def _check_nested_chain(
    base_command: Group, cmd_name: str, cmd: Command, register: bool = False
) -> None
```

检查嵌套命令链，确保在链式模式下不添加组命令。

**Parameters**:
- `base_command` — `Group` — 基础命令组。
- `cmd_name` — `str` — 命令名称。
- `cmd` — `Command` — 命令对象。
- `register` — `bool` — 是否注册命令，默认为 `False`。

**Returns**:
- `None`

**Raises**:
- `RuntimeError` — 如果在链式模式下尝试添加组命令。

*来源: `src/click/core.py:78`*

---
<a id="sym-src_click_core.py-98"></a>
### `_format_deprecated_label` · func
```python
def _format_deprecated_label(deprecated: bool | str) -> str
```

Return the parenthesized deprecation label shown in help text.

**Parameters**:
- `deprecated` — `bool | str` — The deprecation status or message.

**Returns**:
- `str` — The formatted deprecation label.

*来源: `src/click/core.py:98`*

---
<a id="sym-src_click_core.py-106"></a>
### `_format_deprecated_suffix` · func
```python
def _format_deprecated_suffix(deprecated: bool | str) -> str
```

Return the trailing reason for a `DeprecationWarning` message, prefixed with a space, or an empty string when no reason was given.

**Parameters**:
- `deprecated` — `bool | str` — The reason for deprecation, either as a string or a boolean indicating no reason.

**Returns**:
- `str` — The formatted deprecation reason, prefixed with a space if provided.

*来源: `src/click/core.py:106`*

---
<a id="sym-src_click_core.py-115"></a>
### `batch` · func
```python
def batch(iterable: cabc.Iterable[V], batch_size: int) -> list[tuple[V, ...]]
```

将可迭代对象分成指定大小的批次。

**Parameters**:
- `iterable` — `cabc.Iterable[V]` — 要分批处理的可迭代对象。
- `batch_size` — `int` — 每个批次的大小。

**Returns**:
- `list[tuple[V, ...]]` — 包含分批处理结果的列表，每个元素是一个元组，包含 `batch_size` 个元素。

**Raises**:
- 无

*来源: `src/click/core.py:115`*

---
<a id="sym-src_click_core.py-120"></a>
### `augment_usage_errors` · func
装饰器: `@contextmanager`
```python
def augment_usage_errors(
    ctx: Context, param: Parameter | None = None
) -> cabc.Generator[None]
```

Context manager that attaches extra information to exceptions.

**Parameters**:
- `ctx` — `Context` — The context to attach to exceptions.
- `param` — `Parameter | None` — The parameter to attach to exceptions.

**Returns**:
- `cabc.Generator[None]` — A generator that yields nothing.

**Raises**:
- `BadParameter` — If a `BadParameter` exception is caught, it is re-raised with the context and parameter attached.
- `UsageError` — If a `UsageError` exception is caught, it is re-raised with the context attached.

*来源: `src/click/core.py:120`*

---
<a id="sym-src_click_core.py-138"></a>
### `iter_params_for_processing` · func
```python
def iter_params_for_processing(
    invocation_order: cabc.Sequence[Parameter],
    declaration_order: cabc.Sequence[Parameter],
) -> list[Parameter]
```

Returns all declared parameters in the order they should be processed.

**Parameters**:
- `invocation_order` — `cabc.Sequence[Parameter]` — The order in which the parameters were invoked.
- `declaration_order` — `cabc.Sequence[Parameter]` — The order in which the parameters were declared.

**Returns**:
- `list[Parameter]` — The parameters sorted based on the invocation order and eagerness.

**Raises**:
- (无)

*来源: `src/click/core.py:138`*

---
<a id="sym-src_click_core.py-154"></a>
### `sort_key` · func
```python
def sort_key(item: Parameter) -> tuple[bool, float]
```

用途: 用于生成排序键，根据参数的延迟执行和在调用顺序中的位置进行排序。

**Parameters**:
- `item` — `Parameter` — 要排序的参数。

**Returns**:
- `tuple[bool, float]` — 排序键，第一个元素是布尔值，表示参数是否延迟执行，第二个元素是参数在调用顺序中的索引。

**Raises**:
- 无

*来源: `src/click/core.py:154`*

---
<a id="sym-src_click_core.py-165"></a>
### `ParameterSource` · class
```python
class ParameterSource(enum.IntEnum)
```

`ParameterSource` 是一个枚举类，用于表示命令行参数的来源。

| 参数名 | 类型 | 含义 |
| --- | --- | --- |
| 无方法 | 无 | 无方法 |

这个类主要用于在 Click 命令行工具中标识参数的来源，例如环境变量、配置文件或命令行输入。

*来源: `src/click/core.py:165`*

---
<a id="sym-src_click_core.py-204"></a>
### `Context` · class
```python
class Context
```

`Context` 类代表一个命令行上下文，负责管理命令的执行环境和状态。

- **Parameters**:
  - `command` — `Command` — 当前执行的命令。
  - `parent` — `Context | None` — 父上下文，如果存在。
  - `info_name` — `str | None` — 命令的名称。
  - `obj` — `t.Any | None` — 与命令关联的对象。
  - `auto_envvar_prefix` — `str | None` — 自动环境变量前缀。
  - `default_map` — `cabc.MutableMapping[str, t.Any] | None` — 默认值映射。
  - `terminal_width` — `int | None` — 终端宽度。
  - `max_content_width` — `int | None` — 内容最大宽度。
  - `resilient_parsing` — `bool` — 是否弹性解析。
  - `allow_extra_args` — `bool | None` — 是否允许额外参数。
  - `allow_interspersed_args` — `bool | None` — 是否允许交错参数。
  - `ignore_unknown_options` — `bool | None` — 是否忽略未知选项。
  - `help_option_names` — `list[str] | None` — 帮助选项名称列表。
  - `token_normalize_func` — `t.Callable[[str], str] | None` — 令牌规范化函数。
  - `color`

*来源: `src/click/core.py:204`*

---
<a id="sym-src_click_core.py-336"></a>
### `Context.__init__` · method
```python
def __init__(
        self,
        command: Command,
        parent: Context | None = None,
        info_name: str | None = None,
        obj: t.Any | None = None,
        auto_envvar_prefix: str | None = None,
        default_map: cabc.MutableMapping[str, t.Any] | None = None,
        terminal_width: int | None = None,
        max_content_width: int | None = None,
        resilient_parsing: bool = False,
        allow_extra_args: bool | None = None,
        allow_interspersed_args: bool | None = None,
        ignore_unknown_options: bool | None = None,
        help_option_names: list[str] | None = None,
        token_normalize_func: t.Callable[[str], str] | None = None,
        color: bool | None = None,
        show_default: bool | None = None,
    ) -> None:
        #: the parent context or `None` if none exists.
```

初始化一个新的 `Context` 对象。

**Parameters**:
- `command` — `Command` — 当前命令对象。
- `parent` — `Context | None` — 父上下文对象，如果不存在则为 `None`。
- `info_name` — `str | None` — 描述性信息名称。
- `obj` — `t.Any | None` — 关联的对象。
- `auto_envvar_prefix` — `str | None` — 自动环境变量前缀。
- `default_map` — `cabc.MutableMapping[str, t.Any] | None` — 默认值映射。
- `terminal_width` — `int | None` — 终端宽度。
- `max_content_width` — `int | None` — 内容最大宽度。
- `resilient_parsing` — `bool` — 是否具有弹性解析。
- `allow_extra_args` — `bool | None` — 是否允许额外参数。
- `allow_interspersed_args` — `bool | None` — 是否允许交错参数。
- `ignore_unknown_options` — `bool | None` — 是否忽略未知选项。
- `help_option_names` — `list[str] | None` — 帮助选项名称列表。
- `token_normalize_func` — `t.Callable[[str], str] | None` — 令牌规范化函数。
- `color` — `bool | None` — 是否启用颜色。
- `show_default` — `bool | None` — 是否显示

*来源: `src/click/core.py:336`*

---
<a id="sym-src_click_core.py-513"></a>
### `Context.protected_args` · method
装饰器: `@property`
```python
def protected_args(self) -> list[str]
```

**用途**: 返回当前上下文中的受保护参数列表。

**Parameters**:
- 无

**Returns**:
- `list[str]`: 受保护参数列表。

**Raises**:
- `DeprecationWarning`: 警告 `'protected_args'` 已弃用，将在 Click 9.0 中移除。`'args'` 将包含剩余未解析的标记。

*来源: `src/click/core.py:513`*

---
<a id="sym-src_click_core.py-524"></a>
### `Context.to_info_dict` · method
```python
def to_info_dict(self) -> dict[str, t.Any]
```

Gather information that could be useful for a tool generating user-facing documentation. This traverses the entire CLI structure.

**Parameters**:
- `self` — `Context` — The current context instance.

**Returns**:
- `dict[str, t.Any]` — A dictionary containing information about the command, including its name, whether it allows extra arguments, interspersed arguments, and more.

**Raises**:
- None

*来源: `src/click/core.py:524`*

---
<a id="sym-src_click_core.py-545"></a>
### `Context.__enter__` · method
```python
def __enter__(self) -> Self
```

**用途**: 进入上下文管理器，增加上下文深度并推入当前上下文。

**Parameters**:
- `self` — `Context` — 当前上下文对象。

**Returns**:
- `Self` — 当前上下文对象。

**Raises**:
- 无

**内部调用(库内):**
- [`push_context`](src_click.md#sym-src_click_globals.py-44) — Pushes a new context to the current stack.

*来源: `src/click/core.py:545`*

---
<a id="sym-src_click_core.py-550"></a>
### `Context.__exit__` · method
```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None
```

**用途**: 退出 Click 上下文，处理异常并关闭上下文。

**Parameters**:
- `exc_type` — `type[BaseException] | None` — 异常类型，如果存在异常则为异常类型，否则为 `None`。
- `exc_value` — `BaseException | None` — 异常实例，如果存在异常则为异常实例，否则为 `None`。
- `tb` — `TracebackType | None` — 异常的回溯信息，如果存在异常则为回溯信息，否则为 `None`。

**Returns**:
- `bool | None` — 如果上下文深度为 0，则调用 `_close_with_exception_info` 并返回其结果；否则返回 `None`。

**Raises**:
- 无

**内部调用(库内):**
- [`Context._close_with_exception_info`](src_click.md#sym-src_click_core.py-692) — Unwind the exit stack by calling its `__exit__` method with the exception inform
- [`pop_context`](src_click.md#sym-src_click_globals.py-49) — **用途**: Removes the top level from the stack.

*来源: `src/click/core.py:550`*

---
<a id="sym-src_click_core.py-565"></a>
### `Context.scope` · method
装饰器: `@contextmanager`
```python
def scope(self, cleanup: bool = True) -> cabc.Generator[Context]
```

**用途**: This method promotes the context object to the current thread local and optionally runs cleanup functions.

**Parameters**:
- `cleanup` — `bool` — Controls if the cleanup functions should be run or not. The default is to run these functions. In some situations the context only wants to be temporarily pushed in which case this can be disabled. Nested pushes automatically defer the cleanup.

**Returns**:
- `cabc.Generator[Context]` — A generator that yields the context object.

**Raises**:
- None

*来源: `src/click/core.py:565`*

---
<a id="sym-src_click_core.py-603"></a>
### `Context.meta` · method
装饰器: `@property`
```python
def meta(self) -> dict[str, t.Any]
```

**用途**: 返回一个共享的字典，该字典在所有嵌套的上下文中共享。用于存储一些状态信息，但需要代码管理该字典。

**Parameters**:
- 无

**Returns**:
- `dict[str, t.Any]`: 一个共享的字典，用于存储状态信息。

**Raises**:
- 无

*来源: `src/click/core.py:603`*

---
<a id="sym-src_click_core.py-630"></a>
### `Context.make_formatter` · method
```python
def make_formatter(self) -> HelpFormatter
```

Creates the :class:`~click.HelpFormatter` for the help and usage output.

**Parameters**:
- `self` — `Context` — The context instance.

**Returns**:
- `HelpFormatter` — The created formatter instance.

**Raises**:
- None

*来源: `src/click/core.py:630`*

---
<a id="sym-src_click_core.py-644"></a>
### `Context.with_resource` · method
```python
def with_resource(self, context_manager: AbstractContextManager[V]) -> V
```

**用途**: Register a resource as if it were used in a `with` statement. The resource will be cleaned up when the context is popped.

**Parameters**:
- `context_manager` — `AbstractContextManager[V]` — The context manager to enter.

**Returns**:
- `V` — Whatever `context_manager.__enter__()` returns.

**Raises**:
- None

*来源: `src/click/core.py:644`*

---
<a id="sym-src_click_core.py-673"></a>
### `Context.call_on_close` · method
```python
def call_on_close(self, f: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]
```

Register a function to be called when the context tears down.

**Parameters**:
- `f` — `t.Callable[..., t.Any]` — The function to execute on teardown.

**Returns**:
- `t.Callable[..., t.Any]` — The original function, allowing for method chaining.

**Raises**:
- None

*来源: `src/click/core.py:673`*

---
<a id="sym-src_click_core.py-685"></a>
### `Context.close` · method
```python
def close(self) -> None
```

Invoke all close callbacks registered with :meth:`call_on_close`, and exit all context managers entered with :meth:`with_resource`.

**Parameters**:
- `exc_type` — `type[BaseException] | None` — The type of the exception that was raised, if any.
- `exc_value` — `BaseException | None` — The exception instance that was raised, if any.
- `tb` — `TracebackType | None` — The traceback object associated with the exception, if any.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Context._close_with_exception_info`](src_click.md#sym-src_click_core.py-692) — Unwind the exit stack by calling its `__exit__` method with the exception inform

*来源: `src/click/core.py:685`*

---
<a id="sym-src_click_core.py-692"></a>
### `Context._close_with_exception_info` · method
```python
def _close_with_exception_info(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None
```

Unwind the exit stack by calling its `__exit__` method with the exception information to allow for exception handling by the various resources registered using `with_resource`.

**Parameters**:
- `exc_type` (type[BaseException] | None) — The type of the exception being handled.
- `exc_value` (BaseException | None) — The exception instance being handled.
- `tb` (TracebackType | None) — The traceback associated with the exception.

**Returns**:
- `bool | None` — Whatever `exit_stack.__exit__()` returns.

**Raises**:
- None

**内部调用(库内):**
- [`Context.__exit__`](src_click.md#sym-src_click_core.py-550) — **用途**: 退出 Click 上下文，处理异常并关闭上下文。

*来源: `src/click/core.py:692`*

---
<a id="sym-src_click_core.py-711"></a>
### `Context.command_path` · method
装饰器: `@property`
```python
def command_path(self) -> str
```

**用途**: 返回计算出的命令路径，用于帮助页面的 `usage` 信息。它通过递归组合父上下文的命令路径和参数使用片段来生成。

**Parameters**:
- `self` — `Context` — 当前上下文对象。

**Returns**:
- `str` — 计算出的命令路径。

**Raises**:
- 无

**内部调用(库内):**
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Parameter.get_usage_pieces`](src_click.md#sym-src_click_core.py-2768) — **用途**: 获取参数的使用片段列表。

*来源: `src/click/core.py:711`*

---
<a id="sym-src_click_core.py-729"></a>
### `Context.find_root` · method
```python
def find_root(self) -> Context
```

用途: 找到当前上下文的最外层上下文。

**Parameters**:
- 无

**Returns**:
- `Context` — 最外层上下文

**Raises**:
- 无

*来源: `src/click/core.py:729`*

---
<a id="sym-src_click_core.py-736"></a>
### `Context.find_object` · method
```python
def find_object(self, object_type: type[V]) -> V | None
```

Finds the closest object of a given type.

**Parameters**:
- `object_type` — `type[V]` — The type of the object to find.

**Returns**:
- `V | None` — The closest object of the given type, or `None` if no such object is found.

*来源: `src/click/core.py:736`*

---
<a id="sym-src_click_core.py-748"></a>
### `Context.ensure_object` · method
```python
def ensure_object(self, object_type: type[V]) -> V
```

**用途**: 确保在当前上下文中存在指定类型的对象，如果不存在则创建一个新的实例。

**Parameters**:
- `object_type` — `type[V]` — 要确保的对象类型。

**Returns**:
- `V` — 返回当前上下文中的对象实例。

**Raises**:
- 无

**内部调用(库内):**
- [`Context.find_object`](src_click.md#sym-src_click_core.py-736) — Finds the closest object of a given type.

*来源: `src/click/core.py:748`*

---
<a id="sym-src_click_core.py-757"></a>
### `Context._default_map_has` · method
```python
def _default_map_has(self, name: str | None) -> bool
```

检查 `default_map` 是否包含名为 `name` 的真实值。

**Parameters**:
- `name` — `str | None` — 要检查的键名。

**Returns**:
- `bool` — 如果 `default_map` 包含名为 `name` 的真实值，则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/core.py:757`*

---
<a id="sym-src_click_core.py-772"></a>
### `Context.lookup_default` · method
装饰器: `@t.overload`
```python
def lookup_default(
        self, name: str, call: t.Literal[True] = True
    ) -> t.Any | None
```

查找默认值。

**Parameters**:
- `name` — `str` — 要查找的默认值的名称。
- `call` — `t.Literal[True]` — 是否调用默认值的回调函数（默认为 `True`）。

**Returns**:
- `t.Any | None` — 返回找到的默认值，如果未找到则返回 `None`。

*来源: `src/click/core.py:772`*

---
<a id="sym-src_click_core.py-777"></a>
### `Context.lookup_default` · method
装饰器: `@t.overload`
```python
def lookup_default(
        self, name: str, call: t.Literal[False] = ...
    ) -> t.Any | t.Callable[[], t.Any] | None
```

查找默认值。

**Parameters**:
- `name` — `str` — 要查找的默认值的名称。
- `call` — `t.Literal[False]` — 是否调用默认值。默认为 `False`。

**Returns**:
- `t.Any | t.Callable[[], t.Any] | None` — 返回找到的默认值、可调用对象或 `None`。

*来源: `src/click/core.py:777`*

---
<a id="sym-src_click_core.py-781"></a>
### `Context.lookup_default` · method
```python
def lookup_default(self, name: str, call: bool = True) -> t.Any | None
```

获取参数的默认值。

**Parameters**:
- name — str — 参数的名称。
- call — bool — 如果默认值是一个可调用对象，调用它。禁用以返回可调用对象本身。

**Returns**:
- t.Any | None — 参数的默认值或 `None`。

**Raises**:
- 无

**内部调用(库内):**
- [`Context._default_map_has`](src_click.md#sym-src_click_core.py-757) — 检查 `default_map` 是否包含名为 `name` 的真实值。

*来源: `src/click/core.py:781`*

---
<a id="sym-src_click_core.py-803"></a>
### `Context.fail` · method
```python
def fail(self, message: str) -> t.NoReturn
```

Aborts the execution of the program with a specific error message.

**Parameters**:
- message — str — the error message to fail with.

**Raises**:
- UsageError — ClickException — Aborts the execution of the program with the provided error message.

**内部调用(库内):**
- [`UsageError`](src_click.md#sym-src_click_exceptions.py-68) — `UsageError` 类用于表示用户输入错误，通常在命令行工具中用于提示用户输入不正确。

*来源: `src/click/core.py:803`*

---
<a id="sym-src_click_core.py-811"></a>
### `Context.abort` · method
```python
def abort(self) -> t.NoReturn
```

Abort the script execution.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- Abort: Raised to abort the script execution.

**内部调用(库内):**
- [`Abort`](src_click.md#sym-src_click_exceptions.py-362) — `Abort` 类继承自 `RuntimeError`，用于表示命令执行过程中发生了中止操作。

*来源: `src/click/core.py:811`*

---
<a id="sym-src_click_core.py-815"></a>
### `Context.exit` · method
```python
def exit(self, code: int = 0) -> t.NoReturn
```

Exits the application with a given exit code.

**Parameters**:
- `code` — `int` — The exit code to use.

**Returns**:
- `t.NoReturn` — This method does not return.

**Raises**:
- `Exit` — A `RuntimeError` subclass that indicates the application should exit with the specified code.

**内部调用(库内):**
- [`Exit`](src_click.md#sym-src_click_exceptions.py-366) — `Exit` 类用于表示程序应该退出，并提供一个退出代码。

*来源: `src/click/core.py:815`*

---
<a id="sym-src_click_core.py-825"></a>
### `Context.get_usage` · method
```python
def get_usage(self) -> str
```

获取当前上下文和命令的格式化使用字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 当前上下文和命令的格式化使用字符串。

**Raises**:
- 无

*来源: `src/click/core.py:825`*

---
<a id="sym-src_click_core.py-831"></a>
### `Context.get_help` · method
```python
def get_help(self) -> str
```

获取当前上下文和命令的格式化帮助页面。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化帮助页面

**Raises**:
- 无

*来源: `src/click/core.py:831`*

---
<a id="sym-src_click_core.py-837"></a>
### `Context._make_sub_context` · method
```python
def _make_sub_context(self, command: Command) -> Context
```

创建一个新的上下文，该上下文与当前上下文相同类型，但针对一个新的命令。

**Parameters**:
- `command` — `Command` — 新命令对象。

**Returns**:
- `Context` — 新创建的上下文对象。

**Raises**:
- 无

*来源: `src/click/core.py:837`*

---
<a id="sym-src_click_core.py-846"></a>
### `Context.invoke` · method
装饰器: `@t.overload`
```python
def invoke(
        self, callback: t.Callable[..., V], /, *args: t.Any, **kwargs: t.Any
    ) -> V
```

调用指定的回调函数并返回其结果。

**Parameters**:
- `callback` — `t.Callable[..., V]` — 要调用的回调函数。
- `*args` — `t.Any` — 传递给回调函数的位置参数。
- `**kwargs` — `t.Any` — 传递给回调函数的关键字参数。

**Returns**:
- `V` — 回调函数的返回值。

**Raises**:
- 无

*来源: `src/click/core.py:846`*

---
<a id="sym-src_click_core.py-851"></a>
### `Context.invoke` · method
装饰器: `@t.overload`
```python
def invoke(self, callback: Command, /, *args: t.Any, **kwargs: t.Any) -> t.Any
```

调用一个命令并返回其结果。

**Parameters**:
- `callback` — `Command` — 要调用的命令。
- `*args` — `t.Any` — 传递给命令的参数。
- `**kwargs` — `t.Any` — 传递给命令的关键字参数。

**Returns**:
- `t.Any` — 命令的返回结果。

**Raises**:
- 无

*来源: `src/click/core.py:851`*

---
<a id="sym-src_click_core.py-853"></a>
### `Context.invoke` · method
```python
def invoke(
        self, callback: Command | t.Callable[..., V], /, *args: t.Any, **kwargs: t.Any
    ) -> t.Any | V
```

**用途**: Invokes a command callback in exactly the way it expects, handling both direct function calls and Click command objects.

**Parameters**:
- `callback` — `Command | t.Callable[..., V]` — The command callback to invoke.
- `*args` — `t.Any` — Positional arguments to pass to the callback.
- `**kwargs` — `t.Any` — Keyword arguments to pass to the callback.

**Returns**:
- `t.Any | V` — The result of the callback invocation.

**Raises**:
- `TypeError` — If the given command does not have a callback that can be invoked.

**内部调用(库内):**
- [`Context._make_sub_context`](src_click.md#sym-src_click_core.py-837) — 创建一个新的上下文，该上下文与当前上下文相同类型，但针对一个新的命令。
- [`Parameter.get_default`](src_click.md#sym-src_click_core.py-2383) — 获取参数的默认值。
- [`Parameter.type_cast_value`](src_click.md#sym-src_click_core.py-2476) — Convert and validate a value against the parameter's type, multiple, and nargs.
- [`augment_usage_errors`](src_click.md#sym-src_click_core.py-120) — Context manager that attaches extra information to exceptions.

*来源: `src/click/core.py:853`*

---
<a id="sym-src_click_core.py-909"></a>
### `Context.forward` · method
```python
def forward(self, cmd: Command, /, *args: t.Any, **kwargs: t.Any) -> t.Any
```

**用途**: 调用另一个命令并填充默认关键字参数。

**Parameters**:
- `cmd` — `Command` — 要调用的命令。
- `*args` — `t.Any` — 传递给命令的可变位置参数。
- `**kwargs` — `t.Any` — 传递给命令的关键字参数。

**Returns**:
- `t.Any` — 命令的返回值。

**Raises**:
- `TypeError` — 如果 `cmd` 不是 `Command` 类型。

**内部调用(库内):**
- [`Context.invoke`](src_click.md#sym-src_click_core.py-846) — 调用指定的回调函数并返回其结果。

*来源: `src/click/core.py:909`*

---
<a id="sym-src_click_core.py-928"></a>
### `Context.set_parameter_source` · method
```python
def set_parameter_source(self, name: str, source: ParameterSource) -> None
```

Set the source of a parameter. This indicates the location from which the value of the parameter was obtained.

**Parameters**:
- name — str — The name of the parameter.
- source — ParameterSource — A member of :class:`~click.core.ParameterSource`.

**Returns**:
- None

*来源: `src/click/core.py:928`*

---
<a id="sym-src_click_core.py-937"></a>
### `Context.get_parameter_source` · method
```python
def get_parameter_source(self, name: str) -> ParameterSource | None
```

获取参数的来源。这表明参数值是从哪里获得的。

**Parameters**:
- `name` — `str` — 参数的名称。

**Returns**:
- `ParameterSource | None` — 参数的来源，如果参数未从任何来源提供，则返回 `None`。

**Raises**:
- 无

*来源: `src/click/core.py:937`*

---
<a id="sym-src_click_core.py-956"></a>
### `Command` · class
```python
class Command
```

`Command` 类代表一个 Click 命令，用于定义和执行命令行操作。它负责解析命令行参数、调用回调函数并生成帮助信息。

### 关键方法

- **`__init__`**
  - **Parameters**:
    - `name` — `str | None`: 命令的名称。
    - `context_settings` — `cabc.MutableMapping[str, t.Any] | None`: 上下文设置。
    - `callback` — `t.Callable[..., t.Any] | None`: 命令的回调函数。
    - `params` — `list[Parameter] | None`: 命令的参数列表。
    - `help` — `str | None`: 命令的帮助信息。
    - `epilog` — `str | None`: 命令的尾注信息。
    - `short_help` — `str | None`: 命令的简短帮助信息。
    - `options_metavar` — `str | None`: 选项元变量。
    - `add_help_option` — `bool`: 是否添加帮助选项。
    - `no_args_is_help` — `bool`: 是否将无参数视为帮助。
    - `hidden` — `bool`: 是否隐藏命令。
    - `deprecated` — `bool | str`: 是否弃用命令。
  - **Returns**: `None`

- **`to_info_dict`**
  - **Parameters**:
    - `ctx` — `Context`: 上

*来源: `src/click/core.py:956`*

---
<a id="sym-src_click_core.py-1032"></a>
### `Command.__init__` · method
```python
def __init__(
        self,
        name: str | None,
        context_settings: cabc.MutableMapping[str, t.Any] | None = None,
        callback: t.Callable[..., t.Any] | None = None,
        params: list[Parameter] | None = None,
        help: str | None = None,
        epilog: str | None = None,
        short_help: str | None = None,
        options_metavar: str | None = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool | str = False,
    ) -> None:
        #: the name the command thinks it has.  Upon registering a command
        #: on a :class:`Group` the group will default the command name
        #: with this information.  You should instead use the
        #: :class:`Context`\'s :attr:`~Context.info_name` attribute.
```

### `Command.__init__`

初始化一个 `Command` 对象。

**Parameters**:
- `name` — `str | None`: 命令的名称。在注册到 `Group` 时，组会默认使用此信息。建议使用 `Context` 的 `info_name` 属性。
- `context_settings` — `cabc.MutableMapping[str, t.Any] | None`: 传递给上下文的可选默认字典。
- `callback` — `t.Callable[..., t.Any] | None`: 当命令触发时执行的回调函数。可能为 `None`，在这种情况下不会执行任何操作。
- `params` — `list[Parameter] | None`: 命令的参数列表，按顺序显示在帮助页面和执行。懒加载参数会自动在非懒加载参数之前处理。
- `help` — `str | None`: 命令的帮助信息。
- `epilog` — `str | None`: 命令的尾注信息。
- `short_help` — `str | None`: 命令的简短帮助信息。
- `options_metavar` — `str | None`: 选项的元变量，默认为 `[OPTIONS]`。
- `add_help_option` — `bool`: 是否添加帮助选项，默认为 `True`。
- `no_args_is_help` — `bool`: 是否将没有参数的情况视为帮助选项，默认为 `False`。
- `hidden` — `bool`: 是否隐藏命令，默认为 `False`

*来源: `src/click/core.py:1032`*

---
<a id="sym-src_click_core.py-1076"></a>
### `Command.to_info_dict` · method
```python
def to_info_dict(self, ctx: Context) -> dict[str, t.Any]
```

将命令的详细信息转换为字典。

**Parameters**:
- `ctx` — `Context` — 命令的上下文。

**Returns**:
- `dict[str, t.Any]` — 包含命令详细信息的字典。

**Raises**:
- 无

**内部调用(库内):**
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。

*来源: `src/click/core.py:1076`*

---
<a id="sym-src_click_core.py-1087"></a>
### `Command.__repr__` · method
```python
def __repr__(self) -> str
```

### `Command.__repr__`

返回一个表示 `Command` 对象的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 表示 `Command` 对象的字符串。

**Raises**:
- 无

*来源: `src/click/core.py:1087`*

---
<a id="sym-src_click_core.py-1090"></a>
### `Command.get_usage` · method
```python
def get_usage(self, ctx: Context) -> str
```

Formats the usage line into a string and returns it.

**Parameters**:
- `ctx` — `Context` — The context object for the command.

**Returns**:
- `str` — The formatted usage line.

**Raises**:
- None

**内部调用(库内):**
- [`Context.make_formatter`](src_click.md#sym-src_click_core.py-630) — Creates the :class:`~click.HelpFormatter` for the help and usage output.
- [`Command.format_usage`](src_click.md#sym-src_click_core.py-1124) — Writes the usage line into the formatter.
- [`HelpFormatter.getvalue`](src_click.md#sym-src_click_formatting.py-297) — Returns the contents of the buffer as a string.

*来源: `src/click/core.py:1090`*

---
<a id="sym-src_click_core.py-1099"></a>
### `Command.get_params` · method
```python
def get_params(self, ctx: Context) -> list[Parameter]
```

获取命令的所有参数，包括帮助选项。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `list[Parameter]` — 命令的所有参数列表。

**Raises**:
- 无

**内部调用(库内):**
- [`Command.get_help_option`](src_click.md#sym-src_click_core.py-1151) — Returns the help option object.

*来源: `src/click/core.py:1099`*

---
<a id="sym-src_click_core.py-1124"></a>
### `Command.format_usage` · method
```python
def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None
```

Writes the usage line into the formatter.

**Parameters**:
- `ctx` — `Context` — The context object.
- `formatter` — `HelpFormatter` — The formatter object.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Command.collect_usage_pieces`](src_click.md#sym-src_click_core.py-1132) — `Command.collect_usage_pieces`
- [`HelpFormatter.write_usage`](src_click.md#sym-src_click_formatting.py-158) — HelpFormatter.write_usage

*来源: `src/click/core.py:1124`*

---
<a id="sym-src_click_core.py-1132"></a>
### `Command.collect_usage_pieces` · method
```python
def collect_usage_pieces(self, ctx: Context) -> list[str]
```

### `Command.collect_usage_pieces`

Returns all the pieces that go into the usage line and returns it as a list of strings.

**Parameters**:
- `ctx` — `Context` — The current context.

**Returns**:
- `list[str]` — A list of strings representing the pieces of the usage line.

**Raises**:
- None

**内部调用(库内):**
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Parameter.get_usage_pieces`](src_click.md#sym-src_click_core.py-2768) — **用途**: 获取参数的使用片段列表。

*来源: `src/click/core.py:1132`*

---
<a id="sym-src_click_core.py-1143"></a>
### `Command.get_help_option_names` · method
```python
def get_help_option_names(self, ctx: Context) -> list[str]
```

Returns the names for the help option.

**Parameters**:
- `ctx` — `Context` — The context object.

**Returns**:
- `list[str]` — The names for the help option.

*来源: `src/click/core.py:1143`*

---
<a id="sym-src_click_core.py-1151"></a>
### `Command.get_help_option` · method
```python
def get_help_option(self, ctx: Context) -> Option | None
```

Returns the help option object.

**Parameters**:
- `ctx` — `Context` — The context object.

**Returns**:
- `Option | None` — The help option object if it exists, otherwise `None`.

**Raises**:
- None

**内部调用(库内):**
- [`Command.get_help_option_names`](src_click.md#sym-src_click_core.py-1143) — Returns the names for the help option.
- [`help_option`](src_click.md#sym-src_click_decorators.py-527) — Pre-configured `--help` option which immediately prints the help page and exits 

*来源: `src/click/core.py:1151`*

---
<a id="sym-src_click_core.py-1178"></a>
### `Command.make_parser` · method
```python
def make_parser(self, ctx: Context) -> _OptionParser
```

创建该命令的底层选项解析器。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `_OptionParser` — 该命令的选项解析器。

**Raises**:
- 无

**内部调用(库内):**
- [`_OptionParser`](src_click.md#sym-src_click_parser.py-224) — `_OptionParser` 类用于解析命令行选项和参数，并将其转换为 Click 命令的上下文。
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Parameter.add_to_parser`](src_click.md#sym-src_click_core.py-2426) — 将参数添加到解析器中。

*来源: `src/click/core.py:1178`*

---
<a id="sym-src_click_core.py-1185"></a>
### `Command.get_help` · method
```python
def get_help(self, ctx: Context) -> str
```

Formats the help into a string and returns it.

**Parameters**:
- `ctx` — `Context` — The context object for the command.

**Returns**:
- `str` — The formatted help string.

**Raises**:
- None

**内部调用(库内):**
- [`Context.make_formatter`](src_click.md#sym-src_click_core.py-630) — Creates the :class:`~click.HelpFormatter` for the help and usage output.
- [`Command.format_help`](src_click.md#sym-src_click_core.py-1210) — Writes the help into the formatter if it exists.
- [`HelpFormatter.getvalue`](src_click.md#sym-src_click_formatting.py-297) — Returns the contents of the buffer as a string.

*来源: `src/click/core.py:1185`*

---
<a id="sym-src_click_core.py-1194"></a>
### `Command.get_short_help_str` · method
```python
def get_short_help_str(self, limit: int = 45) -> str
```

获取命令的简短帮助字符串，如果未提供则通过缩短长帮助字符串生成。

**Parameters**:
- `limit` — `int` — 帮助字符串的最大长度，默认为45。

**Returns**:
- `str` — 命令的简短帮助字符串。

**Raises**:
- 无

**内部调用(库内):**
- [`make_default_short_help`](src_click.md#sym-src_click_utils.py-59) — Returns a condensed version of the help string, ensuring it does not exceed the 
- [`_format_deprecated_label`](src_click.md#sym-src_click_core.py-98) — Return the parenthesized deprecation label shown in help text.

*来源: `src/click/core.py:1194`*

---
<a id="sym-src_click_core.py-1210"></a>
### `Command.format_help` · method
```python
def format_help(self, ctx: Context, formatter: HelpFormatter) -> None
```

Writes the help into the formatter if it exists.

**Parameters**:
- `ctx` — `Context` — The context object.
- `formatter` — `HelpFormatter` — The formatter object.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Command.format_usage`](src_click.md#sym-src_click_core.py-1124) — Writes the usage line into the formatter.
- [`Command.format_help_text`](src_click.md#sym-src_click_core.py-1229) — Writes the help text to the formatter if it exists.
- [`Command.format_arguments`](src_click.md#sym-src_click_core.py-1259) — Writes the arguments that have a help record into the formatter.
- [`Command.format_options`](src_click.md#sym-src_click_core.py-1247) — Writes all the options into the formatter if they exist.
- [`Command.format_epilog`](src_click.md#sym-src_click_core.py-1271) — Writes the epilog into the formatter if it exists.

*来源: `src/click/core.py:1210`*

---
<a id="sym-src_click_core.py-1229"></a>
### `Command.format_help_text` · method
```python
def format_help_text(self, ctx: Context, formatter: HelpFormatter) -> None
```

Writes the help text to the formatter if it exists.

**Parameters**:
- `ctx` — `Context` — The context object.
- `formatter` — `HelpFormatter` — The formatter object.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`_format_deprecated_label`](src_click.md#sym-src_click_core.py-98) — Return the parenthesized deprecation label shown in help text.
- [`HelpFormatter.write_paragraph`](src_click.md#sym-src_click_formatting.py-208) — Writes a paragraph into the buffer.
- [`HelpFormatter.indentation`](src_click.md#sym-src_click_formatting.py-289) — 增加缩进的上下文管理器。
- [`HelpFormatter.write_text`](src_click.md#sym-src_click_formatting.py-213) — Writes re-indented text into the buffer. This rewraps and preserves paragraphs.

*来源: `src/click/core.py:1229`*

---
<a id="sym-src_click_core.py-1247"></a>
### `Command.format_options` · method
```python
def format_options(self, ctx: Context, formatter: HelpFormatter) -> None
```

Writes all the options into the formatter if they exist.

**Parameters**:
- `ctx` — `Context` — The context object for the command.
- `formatter` — `HelpFormatter` — The formatter to write the options to.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Parameter.get_help_record`](src_click.md#sym-src_click_core.py-2765) — 获取参数的帮助记录。
- [`HelpFormatter.section`](src_click.md#sym-src_click_formatting.py-274) — Helpful context manager that writes a paragraph, a heading, and the indents.
- [`HelpFormatter.write_dl`](src_click.md#sym-src_click_formatting.py-229) — Writes a definition list into the buffer. This is how options and commands are u

*来源: `src/click/core.py:1247`*

---
<a id="sym-src_click_core.py-1259"></a>
### `Command.format_arguments` · method
```python
def format_arguments(self, ctx: Context, formatter: HelpFormatter) -> None
```

Writes the arguments that have a help record into the formatter.

**Parameters**:
- `ctx` — `Context` — The current context.
- `formatter` — `HelpFormatter` — The formatter to write to.

**Returns**:
- `None`

**内部调用(库内):**
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Parameter.get_help_record`](src_click.md#sym-src_click_core.py-2765) — 获取参数的帮助记录。
- [`HelpFormatter.section`](src_click.md#sym-src_click_formatting.py-274) — Helpful context manager that writes a paragraph, a heading, and the indents.
- [`HelpFormatter.write_dl`](src_click.md#sym-src_click_formatting.py-229) — Writes a definition list into the buffer. This is how options and commands are u

*来源: `src/click/core.py:1259`*

---
<a id="sym-src_click_core.py-1271"></a>
### `Command.format_epilog` · method
```python
def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None
```

Writes the epilog into the formatter if it exists.

**Parameters**:
- `ctx` — `Context` — The context object.
- `formatter` — `HelpFormatter` — The formatter object.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`HelpFormatter.write_paragraph`](src_click.md#sym-src_click_formatting.py-208) — Writes a paragraph into the buffer.
- [`HelpFormatter.indentation`](src_click.md#sym-src_click_formatting.py-289) — 增加缩进的上下文管理器。
- [`HelpFormatter.write_text`](src_click.md#sym-src_click_formatting.py-213) — Writes re-indented text into the buffer. This rewraps and preserves paragraphs.

*来源: `src/click/core.py:1271`*

---
<a id="sym-src_click_core.py-1280"></a>
### `Command.make_context` · method
```python
def make_context(
        self,
        info_name: str | None,
        args: list[str],
        parent: Context | None = None,
        **extra: t.Any,
    ) -> Context
```

### `Command.make_context`

This method creates a new `Context` instance by parsing the provided arguments and applying the command's settings.

**Parameters:**

- `info_name` — `str | None`: The descriptive name for the script or command.
- `args` — `list[str]`: The arguments to parse as a list of strings.
- `parent` — `Context | None`: The parent context if available.
- `extra` — `t.Any`: Extra keyword arguments forwarded to the context constructor.

**Returns:**

- `Context`: A new `Context` instance.

**Raises:**

- `NoArgsIsHelpError`: If no arguments are provided and the command does not have a default help option.

**内部调用(库内):**
- [`Context.scope`](src_click.md#sym-src_click_core.py-565) — **用途**: This method promotes the context object to the current thread local and 
- [`Command.parse_args`](src_click.md#sym-src_click_core.py-1317) — `Command.parse_args`

*来源: `src/click/core.py:1280`*

---
<a id="sym-src_click_core.py-1317"></a>
### `Command.parse_args` · method
```python
def parse_args(self, ctx: Context, args: list[str]) -> list[str]
```

### `Command.parse_args`

解析命令行参数并处理它们。

**Parameters:**

- `ctx` — `Context` — 命令上下文。
- `args` — `list[str]` — 命令行参数列表。

**Returns:**

- `list[str]` — 处理后的命令行参数列表。

**Raises:**

- `NoArgsIsHelpError` — 当没有参数且 `no_args_is_help` 为真且 `resilient_parsing` 为假时抛出。

**内部调用(库内):**
- [`NoArgsIsHelpError`](src_click.md#sym-src_click_exceptions.py-332) — `NoArgsIsHelpError` 类继承自 `UsageError`，用于在命令行没有提供参数时显示帮助信息。
- [`Command.make_parser`](src_click.md#sym-src_click_core.py-1178) — 创建该命令的底层选项解析器。
- [`iter_params_for_processing`](src_click.md#sym-src_click_core.py-138) — Returns all declared parameters in the order they should be processed.
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Parameter.handle_parse_result`](src_click.md#sym-src_click_core.py-2677) — 用途
- [`Context.fail`](src_click.md#sym-src_click_core.py-803) — Aborts the execution of the program with a specific error message.

*来源: `src/click/core.py:1317`*

---
<a id="sym-src_click_core.py-1353"></a>
### `Command.invoke` · method
```python
def invoke(self, ctx: Context) -> t.Any
```

### Command.invoke

Given a context, this invokes the attached callback (if it exists) in the right way.

**Parameters**:
- `ctx` — `Context` — The context object containing the command and its parameters.

**Returns**:
- `t.Any` — The result of the callback function, if it exists.

**Raises**:
- `DeprecationWarning` — If the command is deprecated, a warning message is printed to the standard error stream.

**内部调用(库内):**
- [`_format_deprecated_suffix`](src_click.md#sym-src_click_core.py-106) — Return the trailing reason for a `DeprecationWarning` message, prefixed with a s
- [`style`](src_click.md#sym-src_click_termui.py-569) — **用途**: Styles a text with ANSI styles and returns the new string.

*来源: `src/click/core.py:1353`*

---
<a id="sym-src_click_core.py-1369"></a>
### `Command.shell_complete` · method
```python
def shell_complete(self, ctx: Context, incomplete: str) -> list[CompletionItem]
```

### `Command.shell_complete`

Return a list of completions for the incomplete value. Looks at the names of options and chained multi-commands.

**Parameters:**
- `ctx` — `Context` — Invocation context for this command.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns:**
- `list[CompletionItem]` — A list of completion items.

**Raises:**
- None

**内部调用(库内):**
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`Context.get_parameter_source`](src_click.md#sym-src_click_core.py-937) — 获取参数的来源。这表明参数值是从哪里获得的。
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。
- [`Command.get_short_help_str`](src_click.md#sym-src_click_core.py-1194) — 获取命令的简短帮助字符串，如果未提供则通过缩短长帮助字符串生成。
- [`_complete_visible_commands`](src_click.md#sym-src_click_core.py-59) — List all the subcommands of a group that start with the incomplete value and are

*来源: `src/click/core.py:1369`*

---
<a id="sym-src_click_core.py-1417"></a>
### `Command.main` · method
装饰器: `@t.overload`
```python
def main(
        self,
        args: cabc.Sequence[str] | None = None,
        prog_name: str | None = None,
        complete_var: str | None = None,
        standalone_mode: t.Literal[True] = True,
        **extra: t.Any,
    ) -> t.NoReturn
```

### `Command.main`

调用命令的主方法，处理命令行参数并执行相应的操作。

**Parameters:**
- `args` (`cabc.Sequence[str] | None`): 命令行参数序列，如果为 `None`，则使用 `sys.argv`。
- `prog_name` (`str | None`): 程序名称，如果为 `None`，则使用 `args[0]`。
- `complete_var` (`str | None`): 完成变量名，用于 shell 自动补全。
- `standalone_mode` (`t.Literal[True]`): 是否以独立模式运行，通常设置为 `True`。
- `**extra` (`t.Any`): 其他额外参数。

**Returns:**
- `t.NoReturn`: 该方法不返回任何值，通常用于递归调用自身。

**Raises:**
- 无

*来源: `src/click/core.py:1417`*

---
<a id="sym-src_click_core.py-1427"></a>
### `Command.main` · method
装饰器: `@t.overload`
```python
def main(
        self,
        args: cabc.Sequence[str] | None = None,
        prog_name: str | None = None,
        complete_var: str | None = None,
        standalone_mode: bool = ...,
        **extra: t.Any,
    ) -> t.Any
```

### `Command.main`

调用命令的主方法，执行命令的逻辑。

**Parameters**:
- `args` — `cabc.Sequence[str] | None` — 命令行参数序列，如果为 `None`，则使用 `sys.argv`。
- `prog_name` — `str | None` — 程序名称，如果为 `None`，则使用 `args[0]`。
- `complete_var` — `str | None` — 自动补全变量名。
- `standalone_mode` — `bool` — 是否以独立模式运行。
- `**extra` — `t.Any` — 其他额外参数。

**Returns**:
- `t.Any` — 命令执行的结果。

**Raises**:
- 无

*来源: `src/click/core.py:1427`*

---
<a id="sym-src_click_core.py-1436"></a>
### `Command.main` · method
```python
def main(
        self,
        args: cabc.Sequence[str] | None = None,
        prog_name: str | None = None,
        complete_var: str | None = None,
        standalone_mode: bool = True,
        windows_expand_args: bool = True,
        **extra: t.Any,
    ) -> t.Any
```

### `Command.main`

This method is used to invoke a script as a command line application, handling all the necessary setup and teardown.

**Parameters:**
- `args` (`cabc.Sequence[str] | None`): The arguments to be used for parsing. If not provided, `sys.argv[1:]` is used.
- `prog_name` (`str | None`): The program name to be used. By default, it is constructed from `sys.argv[0]`.
- `complete_var` (`str | None`): The environment variable that controls bash completion support. The default is `"_<prog_name>_COMPLETE"` with `prog_name` in uppercase.
- `standalone_mode` (`bool`): If `True`, Click will handle exceptions and convert them into error messages, and the function will never return. If `False`, exceptions will be propagated to the caller.
- `windows_expand_args` (`bool`): Expand glob patterns, user dir, and env vars in command line args on Windows.
- `extra` (`t.Any`): Extra keyword arguments are forwarded to the context constructor.

**Returns:**
- `t.Any`: The return value of the `invoke` method if `standalone_mode` is `False`.

**Raises:**
- `Abort(RuntimeError)`: If an error occurs during execution.

**内部调用(库内):**
- [`_expand_args`](src_click.md#sym-src_click_utils.py-598) — Simulate Unix shell expansion with Python functions.
- [`_detect_program_name`](src_click.md#sym-src_click_utils.py-543) — Determine the command used to run the program, for use in help text. If a file o
- [`Command._main_shell_completion`](src_click.md#sym-src_click_core.py-1549) — 用途
- [`Command.make_context`](src_click.md#sym-src_click_core.py-1280) — `Command.make_context`
- [`Command.invoke`](src_click.md#sym-src_click_core.py-1353) — Command.invoke
- [`Context.exit`](src_click.md#sym-src_click_core.py-815) — Exits the application with a given exit code.
- [`Abort`](src_click.md#sym-src_click_exceptions.py-362) — `Abort` 类继承自 `RuntimeError`，用于表示命令执行过程中发生了中止操作。
- [`PacifyFlushWrapper`](src_click.md#sym-src_click_utils.py-516) — `PacifyFlushWrapper` 是一个包装器类，用于在不立即刷新底层文件对象的情况下提供一个文件对象的接口。

*来源: `src/click/core.py:1436`*

---
<a id="sym-src_click_core.py-1549"></a>
### `Command._main_shell_completion` · method
```python
def _main_shell_completion(
        self,
        ctx_args: cabc.MutableMapping[str, t.Any],
        prog_name: str,
        complete_var: str | None = None,
    ) -> None
```

### 用途
Check if the shell is asking for tab completion, process that, then exit early. Called from :meth:`main` before the program is invoked.

### Parameters
- `ctx_args` — `MutableMapping[str, Any]` — Arguments passed to the command context.
- `prog_name` — `str` — Name of the executable in the shell.
- `complete_var` — `str | None` — Name of the environment variable that holds the completion instruction. Defaults to ``_{PROG_NAME}_COMPLETE``.

### Returns
- `None`

### Raises
- `Exit(RuntimeError)`

**内部调用(库内):**
- [`Command.shell_complete`](src_click.md#sym-src_click_core.py-1369) — `Command.shell_complete`
- [`Context.exit`](src_click.md#sym-src_click_core.py-815) — Exits the application with a given exit code.

*来源: `src/click/core.py:1549`*

---
<a id="sym-src_click_core.py-1581"></a>
### `Command.__call__` · method
```python
def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any
```

调用命令的主方法。

**Parameters**:
- `args` — `t.Any` — 传递给命令的参数。
- `kwargs` — `t.Any` — 传递给命令的关键字参数。

**Returns**:
- `t.Any` — 命令执行的结果。

**Raises**:
- 无

**内部调用(库内):**
- [`Command.main`](src_click.md#sym-src_click_core.py-1417) — `Command.main`

*来源: `src/click/core.py:1581`*

---
<a id="sym-src_click_core.py-1586"></a>
### `_FakeSubclassCheck` · class
```python
class _FakeSubclassCheck(type)
```

`_FakeSubclassCheck` 类是一个元类，用于检查子类是否正确继承自某个类。

- **Parameters**:
  - `cls` — `type` — 当前元类。
  - `subclass` — `type` — 要检查的子类。

- **Returns**:
  - `bool` — 如果子类正确继承自某个类，则返回 `True`，否则返回 `False`。

- **Raises**:
  - 无

*来源: `src/click/core.py:1586`*

---
<a id="sym-src_click_core.py-1587"></a>
### `_FakeSubclassCheck.__subclasscheck__` · method
```python
def __subclasscheck__(cls, subclass: type) -> bool
```

用途: 检查给定的子类是否是当前类的直接基类的子类。

**Parameters**:
- `cls` — `type` — 当前类。
- `subclass` — `type` — 要检查的子类。

**Returns**:
- `bool` — 如果 `subclass` 是 `cls.__bases__[0]` 的子类，则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/core.py:1587`*

---
<a id="sym-src_click_core.py-1590"></a>
### `_FakeSubclassCheck.__instancecheck__` · method
```python
def __instancecheck__(cls, instance: t.Any) -> bool
```

用途: 检查给定实例是否是类的第一个基类的实例。

**Parameters**:
- `cls` — `t.Any` — 要检查的类。
- `instance` — `t.Any` — 要检查的实例。

**Returns**:
- `bool` — 如果实例是类的第一个基类的实例，则返回 `True`，否则返回 `False`。

*来源: `src/click/core.py:1590`*

---
<a id="sym-src_click_core.py-1594"></a>
### `_BaseCommand` · class
```python
class _BaseCommand(Command, metaclass=_FakeSubclassCheck)
```

`_BaseCommand` 是 Click 库中的一个基类，用于定义命令行命令的基本结构和行为。

- **Parameters**:
  - 无参数。

- **Returns**:
  - `Command`: 返回一个命令对象。

- **Raises**:
  - 无异常抛出。

*来源: `src/click/core.py:1594`*

---
<a id="sym-src_click_core.py-1601"></a>
### `Group` · class
```python
class Group(Command)
```

`Group` 类继承自 `Command` 类，用于创建一个命令组，可以包含多个子命令。

### 方法

- **`__init__`**
  - **用途**: 初始化一个命令组。
  - **Parameters**:
    - `name` — `str | None` — 命令组的名称。
    - `commands` — `cabc.MutableMapping[str, Command] | cabc.Sequence[Command] | None` — 命令组中的子命令。
    - `invoke_without_command` — `bool` — 是否在没有子命令时调用。
    - `no_args_is_help` — `bool | None` — 是否在没有参数时显示帮助信息。
    - `subcommand_metavar` — `str | None` — 子命令的元变量。
    - `chain` — `bool` — 是否链式调用。
    - `result_callback` — `t.Callable[..., t.Any] | None` — 结果回调函数。
    - `**kwargs` — `t.Any` — 其他关键字参数。
  - **Returns**: `None`

- **`to_info_dict`**
  - **用途**: 将命令组转换为信息字典。
  - **Parameters**:
    - `ctx` — `Context` — 上下文对象。
  - **Returns**: `dict[str, t.Any]`

- **`add_command`**
  - **用途**: 向命令组中添加一个子命令。
  - **

*来源: `src/click/core.py:1601`*

---
<a id="sym-src_click_core.py-1660"></a>
### `Group.__init__` · method
```python
def __init__(
        self,
        name: str | None = None,
        commands: cabc.MutableMapping[str, Command]
        | cabc.Sequence[Command]
        | None = None,
        invoke_without_command: bool = False,
        no_args_is_help: bool | None = None,
        subcommand_metavar: str | None = None,
        chain: bool = False,
        result_callback: t.Callable[..., t.Any] | None = None,
        **kwargs: t.Any,
    ) -> None
```

### Group.__init__

初始化一个 `Group` 对象。

**Parameters**:
- `name` — `str | None` — 组的名称。
- `commands` — `cabc.MutableMapping[str, Command] | cabc.Sequence[Command] | None` — 组中注册的子命令。
- `invoke_without_command` — `bool` — 是否允许在没有子命令的情况下调用。
- `no_args_is_help` — `bool | None` — 是否在没有参数时显示帮助信息。
- `subcommand_metavar` — `str | None` — 子命令的元变量。
- `chain` — `bool` — 是否允许链式调用。
- `result_callback` — `t.Callable[..., t.Any] | None` — 结果回调函数。
- `**kwargs` — `t.Any` — 其他关键字参数。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/core.py:1660`*

---
<a id="sym-src_click_core.py-1715"></a>
### `Group.to_info_dict` · method
```python
def to_info_dict(self, ctx: Context) -> dict[str, t.Any]
```

将 `Group` 对象转换为包含命令信息的字典。

**Parameters**:
- `ctx` — `Context` — 当前上下文对象。

**Returns**:
- `dict[str, t.Any]` — 包含命令信息的字典。

**Raises**:
- 无

**内部调用(库内):**
- [`Group.list_commands`](src_click.md#sym-src_click_core.py-1895) — Returns a list of subcommand names in the order they should appear.
- [`Group.get_command`](src_click.md#sym-src_click_core.py-1889) — Given a context and a command name, this method returns a `Command` object if it
- [`Context._make_sub_context`](src_click.md#sym-src_click_core.py-837) — 创建一个新的上下文，该上下文与当前上下文相同类型，但针对一个新的命令。
- [`Context.scope`](src_click.md#sym-src_click_core.py-565) — **用途**: This method promotes the context object to the current thread local and 

*来源: `src/click/core.py:1715`*

---
<a id="sym-src_click_core.py-1733"></a>
### `Group.add_command` · method
```python
def add_command(self, cmd: Command, name: str | None = None) -> None
```

Registers another :class:`Command` with this group. If the name is not provided, the name of the command is used.

**Parameters**:
- `cmd` — `Command` — The command to register.
- `name` — `str | None` — The name under which the command will be registered. If not provided, the command's name is used.

**Returns**:
- `None`

**Raises**:
- `TypeError` — If the command has no name.

**内部调用(库内):**
- [`_check_nested_chain`](src_click.md#sym-src_click_core.py-78) — 检查嵌套命令链，确保在链式模式下不添加组命令。

*来源: `src/click/core.py:1733`*

---
<a id="sym-src_click_core.py-1744"></a>
### `Group.command` · method
装饰器: `@t.overload`
```python
def command(self, __func: t.Callable[..., t.Any]) -> Command
```

将一个函数注册为一个命令。

**Parameters**:
- `__func` — `t.Callable[..., t.Any]` — 要注册的函数。

**Returns**:
- `Command` — 注册后的命令对象。

**Raises**:
- 无

*来源: `src/click/core.py:1744`*

---
<a id="sym-src_click_core.py-1747"></a>
### `Group.command` · method
装饰器: `@t.overload`
```python
def command(
        self, *args: t.Any, **kwargs: t.Any
    ) -> t.Callable[[t.Callable[..., t.Any]], Command]
```

用途: 用于在 `Group` 对象上注册一个命令。

**Parameters**:
- `*args` — `t.Any` — 传递给命令的参数。
- `**kwargs` — `t.Any` — 传递给命令的关键字参数。

**Returns**:
- `t.Callable[[t.Callable[..., t.Any]], Command]` — 返回一个装饰器，用于装饰命令函数并将其注册到 `Group` 对象中。

*来源: `src/click/core.py:1747`*

---
<a id="sym-src_click_core.py-1751"></a>
### `Group.command` · method
```python
def command(
        self, *args: t.Any, **kwargs: t.Any
    ) -> t.Callable[[t.Callable[..., t.Any]], Command] | Command
```

**用途**: 用于声明并附加一个命令到组中。这个装饰器接受与 `command` 函数相同的参数，并立即通过调用 `add_command` 方法将创建的命令注册到该组。

**Parameters**:
- `*args` — `t.Any` — 传递给命令的参数。
- `**kwargs` — `t.Any` — 传递给命令的关键字参数。

**Returns**:
- `t.Callable[[t.Callable[..., t.Any]], Command] | Command` — 返回一个装饰器或命令对象。

**Raises**:
- 无

**内部调用(库内):**
- [`Group.command`](src_click.md#sym-src_click_core.py-1744) — 将一个函数注册为一个命令。
- [`Group.add_command`](src_click.md#sym-src_click_core.py-1733) — Registers another :class:`Command` with this group. If the name is not provided,
- [`Group.decorator`](src_click.md#sym-src_click_core.py-1782) — 将一个函数转换为命令并添加到组中。

*来源: `src/click/core.py:1751`*

---
<a id="sym-src_click_core.py-1782"></a>
### `Group.decorator` · method
```python
def decorator(f: t.Callable[..., t.Any]) -> Command
```

将一个函数转换为命令并添加到组中。

**Parameters**:
- `f` — `t.Callable[..., t.Any]` — 要转换为命令的函数。

**Returns**:
- `Command` — 转换后的命令对象。

**Raises**:
- 无

**内部调用(库内):**
- [`Group.command`](src_click.md#sym-src_click_core.py-1744) — 将一个函数注册为一个命令。
- [`Group.add_command`](src_click.md#sym-src_click_core.py-1733) — Registers another :class:`Command` with this group. If the name is not provided,

*来源: `src/click/core.py:1782`*

---
<a id="sym-src_click_core.py-1793"></a>
### `Group.group` · method
装饰器: `@t.overload`
```python
def group(self, __func: t.Callable[..., t.Any]) -> Group
```

用途: 用于将一个函数注册为子命令。

**Parameters**:
- `__func` — `t.Callable[..., t.Any]` — 要注册为子命令的函数。

**Returns**:
- `Group` — 返回当前的 `Group` 对象，以便可以继续添加子命令。

**Raises**:
- 无

*来源: `src/click/core.py:1793`*

---
<a id="sym-src_click_core.py-1796"></a>
### `Group.group` · method
装饰器: `@t.overload`
```python
def group(
        self, *args: t.Any, **kwargs: t.Any
    ) -> t.Callable[[t.Callable[..., t.Any]], Group]
```

**用途**: 用于创建一个子命令组。

**Parameters**:
- `*args` — `t.Any` — 传递给子命令组的参数。
- `**kwargs` — `t.Any` — 传递给子命令组的关键字参数。

**Returns**:
- `t.Callable[[t.Callable[..., t.Any]], Group]` — 返回一个装饰器，用于定义子命令组。

**Raises**:
- 无

*来源: `src/click/core.py:1796`*

---
<a id="sym-src_click_core.py-1800"></a>
### `Group.group` · method
```python
def group(
        self, *args: t.Any, **kwargs: t.Any
    ) -> t.Callable[[t.Callable[..., t.Any]], Group] | Group
```

**用途**: 用于声明和附加一个子组到当前组，并立即通过调用 `add_command` 方法将创建的子组注册到当前组。

**Parameters**:
- `*args` — `t.Any` — 传递给子组的参数。
- `**kwargs` — `t.Any` — 传递给子组的关键字参数。

**Returns**:
- `t.Callable[[t.Callable[..., t.Any]], Group] | Group` — 返回一个装饰器或子组对象。

**Raises**:
- 无

**内部调用(库内):**
- [`Group.group`](src_click.md#sym-src_click_core.py-1793) — 用途: 用于将一个函数注册为子命令。
- [`Group.add_command`](src_click.md#sym-src_click_core.py-1733) — Registers another :class:`Command` with this group. If the name is not provided,
- [`Group.decorator`](src_click.md#sym-src_click_core.py-1782) — 将一个函数转换为命令并添加到组中。

*来源: `src/click/core.py:1800`*

---
<a id="sym-src_click_core.py-1834"></a>
### `Group.decorator` · method
```python
def decorator(f: t.Callable[..., t.Any]) -> Group
```

用途: 为 `Group` 对象添加一个命令装饰器。

**Parameters**:
- `f` — `t.Callable[..., t.Any]` — 要装饰的命令函数。

**Returns**:
- `Group` — 装饰后的 `Group` 对象。

**Raises**:
- 无

**内部调用(库内):**
- [`Group.group`](src_click.md#sym-src_click_core.py-1793) — 用途: 用于将一个函数注册为子命令。
- [`Group.add_command`](src_click.md#sym-src_click_core.py-1733) — Registers another :class:`Command` with this group. If the name is not provided,

*来源: `src/click/core.py:1834`*

---
<a id="sym-src_click_core.py-1844"></a>
### `Group.result_callback` · method
```python
def result_callback(self, replace: bool = False) -> t.Callable[[F], F]
```

用途: Adds a result callback to the command.

**Parameters**:
- `replace` — `bool` — if set to `True` an already existing result callback will be removed.

**Returns**:
- `Callable[[F], F]` — A decorator that adds a result callback to the command.

**Raises**:
- None

*来源: `src/click/core.py:1844`*

---
<a id="sym-src_click_core.py-1873"></a>
### `Group.decorator` · method
```python
def decorator(f: F) -> F
```

为 `Group` 类添加一个装饰器，用于修改或扩展其结果回调函数。

**Parameters:**
- `f` — `F` — 要装饰的函数。

**Returns:**
- `F` — 装饰后的函数。

**Raises:**
- 无

*来源: `src/click/core.py:1873`*

---
<a id="sym-src_click_core.py-1880"></a>
### `Group.function` · method
```python
def function(value: t.Any, /, *args: t.Any, **kwargs: t.Any) -> t.Any
```

### Group.function

调用一个旧的回调函数，并将其结果传递给另一个函数进行处理。

**Parameters:**
- `value` — `t.Any` — 传递给旧回调函数的值。
- `*args` — `t.Any` — 传递给旧回调函数的额外位置参数。
- `**kwargs` — `t.Any` — 传递给旧回调函数的额外关键字参数。

**Returns:**
- `t.Any` — 处理后的结果。

**Raises:**
- 无

*来源: `src/click/core.py:1880`*

---
<a id="sym-src_click_core.py-1889"></a>
### `Group.get_command` · method
```python
def get_command(self, ctx: Context, cmd_name: str) -> Command | None
```

Given a context and a command name, this method returns a `Command` object if it exists or returns `None`.

**Parameters**:
- `ctx` — `Context` — The context object.
- `cmd_name` — `str` — The name of the command.

**Returns**:
- `Command | None` — The command object if it exists, otherwise `None`.

*来源: `src/click/core.py:1889`*

---
<a id="sym-src_click_core.py-1895"></a>
### `Group.list_commands` · method
```python
def list_commands(self, ctx: Context) -> list[str]
```

Returns a list of subcommand names in the order they should appear.

**Parameters**:
- `ctx` — `Context` — The context object.

**Returns**:
- `list[str]` — A list of subcommand names.

*来源: `src/click/core.py:1895`*

---
<a id="sym-src_click_core.py-1899"></a>
### `Group.collect_usage_pieces` · method
```python
def collect_usage_pieces(self, ctx: Context) -> list[str]
```

### Group.collect_usage_pieces

Collects usage pieces for the group, appending the subcommand metavar to the result.

**Parameters**:
- `ctx` — `Context` — The current context.

**Returns**:
- `list[str]` — A list of usage pieces.

**Raises**:
- None

*来源: `src/click/core.py:1899`*

---
<a id="sym-src_click_core.py-1904"></a>
### `Group.format_options` · method
```python
def format_options(self, ctx: Context, formatter: HelpFormatter) -> None
```

### Group.format_options

格式化命令组的选项。

**Parameters:**
- `ctx` — `Context` — 上下文对象。
- `formatter` — `HelpFormatter` — 帮助格式化对象。

**Returns:**
- `None`

**Raises:**
- 无

**内部调用(库内):**
- [`Group.format_commands`](src_click.md#sym-src_click_core.py-1908) — Group.format_commands

*来源: `src/click/core.py:1904`*

---
<a id="sym-src_click_core.py-1908"></a>
### `Group.format_commands` · method
```python
def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None
```

### Group.format_commands

Extra format methods for multi methods that adds all the commands after the options.

**Parameters**:
- `ctx` — `Context` — The context object for the command.
- `formatter` — `HelpFormatter` — The formatter object used to format the help output.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Group.list_commands`](src_click.md#sym-src_click_core.py-1895) — Returns a list of subcommand names in the order they should appear.
- [`Group.get_command`](src_click.md#sym-src_click_core.py-1889) — Given a context and a command name, this method returns a `Command` object if it
- [`Command.get_short_help_str`](src_click.md#sym-src_click_core.py-1194) — 获取命令的简短帮助字符串，如果未提供则通过缩短长帮助字符串生成。
- [`HelpFormatter.section`](src_click.md#sym-src_click_formatting.py-274) — Helpful context manager that writes a paragraph, a heading, and the indents.
- [`HelpFormatter.write_dl`](src_click.md#sym-src_click_formatting.py-229) — Writes a definition list into the buffer. This is how options and commands are u

*来源: `src/click/core.py:1908`*

---
<a id="sym-src_click_core.py-1936"></a>
### `Group.parse_args` · method
```python
def parse_args(self, ctx: Context, args: list[str]) -> list[str]
```

### Group.parse_args

解析命令行参数并返回剩余的参数列表。

**Parameters:**
- `ctx` — `Context` — 命令上下文对象。
- `args` — `list[str]` — 命令行参数列表。

**Returns:**
- `list[str]` — 解析后的剩余参数列表。

**Raises:**
- `NoArgsIsHelpError` — 当没有参数且 `no_args_is_help` 为真且 `resilient_parsing` 为假时抛出。

**内部调用(库内):**
- [`NoArgsIsHelpError`](src_click.md#sym-src_click_exceptions.py-332) — `NoArgsIsHelpError` 类继承自 `UsageError`，用于在命令行没有提供参数时显示帮助信息。

*来源: `src/click/core.py:1936`*

---
<a id="sym-src_click_core.py-1950"></a>
### `Group.invoke` · method
```python
def invoke(self, ctx: Context) -> t.Any
```

### Group.invoke

调用子命令并返回结果。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `t.Any` — 子命令的返回值。

**Raises**:
- `UsageError` — 如果没有子命令被调用。

**内部调用(库内):**
- [`Group._process_result`](src_click.md#sym-src_click_core.py-1951) — Group._process_result
- [`Context.fail`](src_click.md#sym-src_click_core.py-803) — Aborts the execution of the program with a specific error message.
- [`Group.resolve_command`](src_click.md#sym-src_click_core.py-2018) — Group.resolve_command
- [`Command.make_context`](src_click.md#sym-src_click_core.py-1280) — `Command.make_context`

*来源: `src/click/core.py:1950`*

---
<a id="sym-src_click_core.py-1951"></a>
### `Group._process_result` · method
```python
def _process_result(value: t.Any) -> t.Any
```

### Group._process_result

处理命令执行结果。

**Parameters**:
- `value` — `t.Any` — 命令执行的结果。

**Returns**:
- `t.Any` — 处理后的结果。

**Raises**:
- 无

**内部调用(库内):**
- [`Group.invoke`](src_click.md#sym-src_click_core.py-1950) — Group.invoke

*来源: `src/click/core.py:1951`*

---
<a id="sym-src_click_core.py-2018"></a>
### `Group.resolve_command` · method
```python
def resolve_command(
        self, ctx: Context, args: list[str]
    ) -> tuple[str | None, Command | None, list[str]]
```

### Group.resolve_command

解析命令并返回命令名称、命令对象和剩余的参数。

**Parameters:**
- `ctx` — `Context` — 上下文对象。
- `args` — `list[str]` — 命令行参数列表。

**Returns:**
- `tuple[str | None, Command | None, list[str]]` — 返回一个包含命令名称、命令对象和剩余参数的元组。

**Raises:**
- `NoSuchCommand` — 如果找不到命令且无法通过规范化函数找到命令。

**内部调用(库内):**
- [`make_str`](src_click.md#sym-src_click_utils.py-49) — Converts a value into a valid string.
- [`Group.get_command`](src_click.md#sym-src_click_core.py-1889) — Given a context and a command name, this method returns a `Command` object if it
- [`_split_opt`](src_click.md#sym-src_click_parser.py-111) — _split_opt
- [`Group.parse_args`](src_click.md#sym-src_click_core.py-1936) — Group.parse_args
- [`NoSuchCommand`](src_click.md#sym-src_click_exceptions.py-268) — `NoSuchCommand` 类用于表示在命令行中尝试执行一个不存在的命令时抛出的异常。

*来源: `src/click/core.py:2018`*

---
<a id="sym-src_click_core.py-2044"></a>
### `Group.shell_complete` · method
```python
def shell_complete(self, ctx: Context, incomplete: str) -> list[CompletionItem]
```

Return a list of completions for the incomplete value. Looks at the names of options, subcommands, and chained multi-commands.

**Parameters**:
- `ctx` — `Context` — Invocation context for this command.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns**:
- `list[CompletionItem]` — A list of completion items.

**Raises**:
- None

**内部调用(库内):**
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。
- [`Command.get_short_help_str`](src_click.md#sym-src_click_core.py-1194) — 获取命令的简短帮助字符串，如果未提供则通过缩短长帮助字符串生成。
- [`_complete_visible_commands`](src_click.md#sym-src_click_core.py-59) — List all the subcommands of a group that start with the incomplete value and are

*来源: `src/click/core.py:2044`*

---
<a id="sym-src_click_core.py-2064"></a>
### `_MultiCommand` · class
```python
class _MultiCommand(Group, metaclass=_FakeSubclassCheck)
```

`_MultiCommand` 是一个用于处理多个子命令的命令类，它继承自 `Group` 并使用 `_FakeSubclassCheck` 作为元类。

- **Parameters**:
  - 无参数

- **Returns**:
  - `None`

- **Raises**:
  - 无异常

*来源: `src/click/core.py:2064`*

---
<a id="sym-src_click_core.py-2071"></a>
### `CommandCollection` · class
```python
class CommandCollection(Group)
```

`CommandCollection` 是一个用于管理多个命令集合的类，它继承自 `Group` 类。

### 方法

#### `__init__`

```python
def __init__(
    self,
    name: str | None = None,
    sources: list[Group] | None = None,
    **kwargs: t.Any,
) -> None
```

**Parameters:**

- `name` — `str | None` — 命令集合的名称。
- `sources` — `list[Group] | None` — 包含其他命令集合的列表。
- `**kwargs` — `t.Any` — 其他关键字参数。

**Returns:**

- `None`

**Raises:**

- 无

#### `add_source`

```python
def add_source(self, group: Group) -> None
```

**Parameters:**

- `group` — `Group` — 要添加的命令集合。

**Returns:**

- `None`

**Raises:**

- 无

#### `get_command`

```python
def get_command(self, ctx: Context, cmd_name: str) -> Command | None
```

**Parameters:**

- `ctx` — `Context` — 当前上下文。
- `cmd_name` — `str` — 要获取的命令名称。

**Returns:**

- `Command | None` — 找到的命令对象，如果没有找到则返回 `None`。

**Raises:**

- 无

#### `list_commands`

```python

*来源: `src/click/core.py:2071`*

---
<a id="sym-src_click_core.py-2089"></a>
### `CommandCollection.__init__` · method
```python
def __init__(
        self,
        name: str | None = None,
        sources: list[Group] | None = None,
        **kwargs: t.Any,
    ) -> None
```

初始化一个 `CommandCollection` 对象。

**Parameters**:
- `name` — `str | None` — 命令集合的名称。
- `sources` — `list[Group] | None` — 注册的组列表。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/core.py:2089`*

---
<a id="sym-src_click_core.py-2099"></a>
### `CommandCollection.add_source` · method
```python
def add_source(self, group: Group) -> None
```

**用途**: 将一个组作为命令来源添加到命令集合中。

**Parameters**:
- `group` — `Group` — 要添加的组。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/core.py:2099`*

---
<a id="sym-src_click_core.py-2103"></a>
### `CommandCollection.get_command` · method
```python
def get_command(self, ctx: Context, cmd_name: str) -> Command | None
```

### `CommandCollection.get_command`

获取指定名称的命令。

**Parameters:**
- `ctx` — `Context` — 上下文对象。
- `cmd_name` — `str` — 命令名称。

**Returns:**
- `Command | None` — 返回找到的命令对象，如果未找到则返回 `None`。

**Raises:**
- 无

**内部调用(库内):**
- [`_check_nested_chain`](src_click.md#sym-src_click_core.py-78) — 检查嵌套命令链，确保在链式模式下不添加组命令。

*来源: `src/click/core.py:2103`*

---
<a id="sym-src_click_core.py-2120"></a>
### `CommandCollection.list_commands` · method
```python
def list_commands(self, ctx: Context) -> list[str]
```

**用途**: 列出当前命令集合及其所有子命令的名称。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `list[str]` — 排序后的命令名称列表。

**Raises**:
- 无

*来源: `src/click/core.py:2120`*

---
<a id="sym-src_click_core.py-2129"></a>
### `_check_iter` · func
```python
def _check_iter(value: cabc.Iterable[V]) -> cabc.Iterator[V]
```

检查值是否可迭代但不是字符串。如果是字符串，则抛出类型错误；否则返回该值的迭代器。

**Parameters**:
- value — cabc.Iterable[V] — 要检查的值。

**Returns**:
- cabc.Iterator[V] — 值的迭代器。

**Raises**:
- TypeError — 如果值是字符串。

*来源: `src/click/core.py:2129`*

---
<a id="sym-src_click_core.py-2139"></a>
### `Parameter` · class
```python
class Parameter(ABC)
```

`Parameter` 类是 Click 库中的一个抽象基类，用于定义命令行参数。它负责解析和处理命令行参数的声明、类型、默认值、回调函数等。

### 关键方法与典型用法

- **`__init__`**
  - **Parameters**:
    - `param_decls` — `Sequence[str] | None`: 参数的声明，例如 `['-v', '--verbose']`。
    - `type` — `ParamType[t.Any] | t.Any | None`: 参数的类型，例如 `int`。
    - `required` — `bool`: 参数是否为必需。
    - `default` — `Any | Callable[[], Any] | None`: 参数的默认值。
    - `callback` — `Callable[[Context, Parameter, Any], Any] | None`: 参数的回调函数。
    - `nargs` — `int | None`: 参数的预期数量。
    - `multiple` — `bool`: 是否允许多个值。
    - `metavar` — `str | None`: 参数的元变量名称。
    - `expose_value` — `bool`: 是否暴露参数值。
    - `is_eager` — `bool`: 是否在解析时立即处理。
    - `envvar` — `str | Sequence[str] | None`: 环境变量名称。
    - `shell_complete` — `Callable[[Context, Parameter, str], list[CompletionItem] | list[str]] | None`: shell 自动补

*来源: `src/click/core.py:2139`*

---
<a id="sym-src_click_core.py-2251"></a>
### `Parameter.__init__` · method
```python
def __init__(
        self,
        param_decls: cabc.Sequence[str] | None = None,
        type: types.ParamType[t.Any] | t.Any | None = None,
        required: bool = False,
        # XXX The default historically embed two concepts:
        # - the declaration of a Parameter object carrying the default (handy to
        #   arbitrage the default value of coupled Parameters sharing the same
        #   self.name, like flag options),
        # - and the actual value of the default.
        # It is confusing and is the source of many issues discussed in:
        # https://github.com/pallets/click/pull/3030
        # In the future, we might think of splitting it in two, not unlike
        # Option.is_flag and Option.flag_value: we could have something like
        # Parameter.is_default and Parameter.default_value.
        default: t.Any | t.Callable[[], t.Any] | None = UNSET,
        callback: t.Callable[[Context, Parameter, t.Any], t.Any] | None = None,
        nargs: int | None = None,
        multiple: bool = False,
        metavar: str | None = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: str | cabc.Sequence[str] | None = None,
        shell_complete: t.Callable[
            [Context, Parameter, str], list[CompletionItem] | list[str]
        ]
        | None = None,
        deprecated: bool | str = False,
    ) -> None
```

### `Parameter.__init__`

初始化一个 `Parameter` 对象。

**Parameters:**
- `param_decls` (`cabc.Sequence[str] | None`): 参数声明的序列，例如 `["-v", "--verbose"]`。
- `type` (`types.ParamType[t.Any] | t.Any | None`): 参数的类型，例如 `int` 或 `str`。
- `required` (`bool`): 参数是否为必需的，默认为 `False`。
- `default` (`t.Any | t.Callable[[], t.Any] | None`): 参数的默认值，可以是任何类型或一个返回默认值的函数。
- `callback` (`t.Callable[[Context, Parameter, t.Any], t.Any] | None`): 一个回调函数，在参数解析时调用。
- `nargs` (`int | None`): 参数的预期数量。
- `multiple` (`bool`): 是否允许多个值，默认为 `False`。
- `metavar` (`str | None`): 参数的元变量名称。
- `expose_value` (`bool`): 是否暴露参数值，默认为 `True`。
- `is_eager` (`bool`): 是否在解析时立即处理参数，默认为 `False`。
- `envvar` (`str | cabc.Sequence[str] | None`): 环境变量名称。
- `shell_complete` (`t.Callable[[Context, Parameter, str], list[CompletionItem] | list[str]] | None`):

**内部调用(库内):**
- [`Parameter._parse_decls`](src_click.md#sym-src_click_core.py-2357) — 用途

*来源: `src/click/core.py:2251`*

---
<a id="sym-src_click_core.py-2325"></a>
### `Parameter.to_info_dict` · method
```python
def to_info_dict(self) -> dict[str, t.Any]
```

Gather information that could be useful for a tool generating user-facing documentation.

**Parameters**:
- `self` — `Parameter` — The parameter instance.

**Returns**:
- `dict[str, t.Any]` — A dictionary containing information about the parameter, suitable for documentation purposes.

**Raises**:
- None

*来源: `src/click/core.py:2325`*

---
<a id="sym-src_click_core.py-2353"></a>
### `Parameter.__repr__` · method
```python
def __repr__(self) -> str
```

返回参数的字符串表示形式。

**Parameters**:
- 无

**Returns**:
- `str`: 参数的字符串表示形式，格式为 `<Parameter 类名 参数名>`。

*来源: `src/click/core.py:2353`*

---
<a id="sym-src_click_core.py-2357"></a>
### `Parameter._parse_decls` · method
装饰器: `@abstractmethod`
```python
def _parse_decls(
        self, decls: cabc.Sequence[str], expose_value: bool
    ) -> tuple[str, list[str], list[str]]
```

### 用途
解析参数声明并返回参数名称、选项和值。

### Parameters
- `decls` — `cabc.Sequence[str]` — 参数声明的序列。
- `expose_value` — `bool` — 是否暴露值。

### Returns
- `tuple[str, list[str], list[str]]` — 包含参数名称、选项和值的元组。

### Raises
- 无

*来源: `src/click/core.py:2357`*

---
<a id="sym-src_click_core.py-2362"></a>
### `Parameter.human_readable_name` · method
装饰器: `@property`
```python
def human_readable_name(self) -> str
```

Returns the human readable name of this parameter. This is the same as the name for options, but the metavar for arguments.

- **Returns**: `str` — The human readable name of the parameter.

*来源: `src/click/core.py:2362`*

---
<a id="sym-src_click_core.py-2368"></a>
### `Parameter.make_metavar` · method
```python
def make_metavar(self, ctx: Context) -> str
```

生成命令行参数的元变量字符串。

**Parameters**:
- `ctx` — `Context` — 命令行上下文。

**Returns**:
- `str` — 生成的元变量字符串。

**Raises**:
- 无

*来源: `src/click/core.py:2368`*

---
<a id="sym-src_click_core.py-2383"></a>
### `Parameter.get_default` · method
装饰器: `@t.overload`
```python
def get_default(
        self, ctx: Context, call: t.Literal[True] = True
    ) -> t.Any | None
```

获取参数的默认值。

**Parameters:**
- `ctx` — `Context` — 上下文对象。
- `call` — `Literal[True]` — 是否调用默认值生成函数（默认为 `True`）。

**Returns:**
- `Any | None` — 参数的默认值或 `None`。

**Raises:**
- 无

*来源: `src/click/core.py:2383`*

---
<a id="sym-src_click_core.py-2388"></a>
### `Parameter.get_default` · method
装饰器: `@t.overload`
```python
def get_default(
        self, ctx: Context, call: bool = ...
    ) -> t.Any | t.Callable[[], t.Any] | None
```

获取参数的默认值。

**Parameters**:
- `ctx` — `Context` — 上下文对象。
- `call` — `bool` — 是否调用默认值函数。

**Returns**:
- `t.Any | t.Callable[[], t.Any] | None` — 参数的默认值、默认值函数或 `None`。

*来源: `src/click/core.py:2388`*

---
<a id="sym-src_click_core.py-2392"></a>
### `Parameter.get_default` · method
```python
def get_default(
        self, ctx: Context, call: bool = True
    ) -> t.Any | t.Callable[[], t.Any] | None
```

###用途
获取参数的默认值。首先尝试通过 `Context.lookup_default` 查找默认值，然后查找本地默认值。

###Parameters
- `ctx` — `Context` — 当前上下文。
- `call` — `bool` — 如果默认值是一个可调用对象，是否调用它。禁用时返回可调用对象本身。

###Returns
- `t.Any | t.Callable[[], t.Any] | None` — 返回参数的默认值。如果默认值是一个可调用对象且 `call` 为 `True`，则调用该可调用对象并返回其结果。

###Raises
- 无

**内部调用(库内):**
- [`Context.lookup_default`](src_click.md#sym-src_click_core.py-772) — 查找默认值。
- [`Context._default_map_has`](src_click.md#sym-src_click_core.py-757) — 检查 `default_map` 是否包含名为 `name` 的真实值。

*来源: `src/click/core.py:2392`*

---
<a id="sym-src_click_core.py-2426"></a>
### `Parameter.add_to_parser` · method
装饰器: `@abstractmethod`
```python
def add_to_parser(self, parser: _OptionParser, ctx: Context) -> None
```

将参数添加到解析器中。

**Parameters**:
- `parser` — `_OptionParser` — 选项解析器。
- `ctx` — `Context` — 上下文。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/core.py:2426`*

---
<a id="sym-src_click_core.py-2428"></a>
### `Parameter.consume_value` · method
```python
def consume_value(
        self, ctx: Context, opts: cabc.Mapping[str, t.Any]
    ) -> tuple[t.Any, ParameterSource]
```

Returns the parameter value produced by the parser.

**Parameters**:
- `ctx` — `Context` — The context object.
- `opts` — `Mapping[str, Any]` — The options dictionary.

**Returns**:
- `tuple[Any, ParameterSource]` — The parameter value and its source.

**Raises**:
- None

**内部调用(库内):**
- [`Parameter.value_from_envvar`](src_click.md#sym-src_click_core.py-2661) — Process the raw environment variable string for this parameter.
- [`Context.lookup_default`](src_click.md#sym-src_click_core.py-772) — 查找默认值。
- [`Context._default_map_has`](src_click.md#sym-src_click_core.py-757) — 检查 `default_map` 是否包含名为 `name` 的真实值。
- [`ParamType.split_envvar_value`](src_click.md#sym-src_click_types.py-147) — Given a value from an environment variable, this method splits it into small chu
- [`Parameter.get_default`](src_click.md#sym-src_click_core.py-2383) — 获取参数的默认值。

*来源: `src/click/core.py:2428`*

---
<a id="sym-src_click_core.py-2476"></a>
### `Parameter.type_cast_value` · method
```python
def type_cast_value(self, ctx: Context, value: t.Any) -> t.Any
```

Convert and validate a value against the parameter's type, multiple, and nargs.

**Parameters**:
- `ctx` — `Context` — The context object for the current command.
- `value` — `t.Any` — The value to be converted and validated.

**Returns**:
- `t.Any` — The converted and validated value.

**Raises**:
- `BadParameter` — If the value is not an iterable when nargs is -1.

**内部调用(库内):**
- [`_check_iter`](src_click.md#sym-src_click_core.py-2129) — 检查值是否可迭代但不是字符串。如果是字符串，则抛出类型错误；否则返回该值的迭代器。
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。
- [`Parameter.check_iter`](src_click.md#sym-src_click_core.py-2486) — 检查传入的值是否为可迭代对象，并返回一个迭代器。
- [`Parameter.convert`](src_click.md#sym-src_click_core.py-2501) — Converts the given value using the parameter's type.

*来源: `src/click/core.py:2476`*

---
<a id="sym-src_click_core.py-2486"></a>
### `Parameter.check_iter` · method
```python
def check_iter(value: t.Any) -> cabc.Iterator[t.Any]
```

检查传入的值是否为可迭代对象，并返回一个迭代器。

**Parameters**:
- value — `t.Any` — 要检查的值。

**Returns**:
- `cabc.Iterator[t.Any]` — 如果值是可迭代对象，则返回一个迭代器。

**Raises**:
- `BadParameter` — 如果值不是可迭代对象。

**内部调用(库内):**
- [`_check_iter`](src_click.md#sym-src_click_core.py-2129) — 检查值是否可迭代但不是字符串。如果是字符串，则抛出类型错误；否则返回该值的迭代器。
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `src/click/core.py:2486`*

---
<a id="sym-src_click_core.py-2501"></a>
### `Parameter.convert` · method
```python
def convert(value: t.Any) -> t.Any
```

Converts the given value using the parameter's type.

**Parameters**:
- `value` — `t.Any` — The value to convert.
- `ctx` — `t.Any` — The context in which the conversion is taking place.

**Returns**:
- `t.Any` — The converted value.

**Raises**:
- `BadParameter` — If the value cannot be converted using the parameter's type.

*来源: `src/click/core.py:2501`*

---
<a id="sym-src_click_core.py-2506"></a>
### `Parameter.convert` · method
```python
def convert(value: t.Any) -> t.Any:  # tuple[t.Any, ...]
```

将输入值转换为参数类型。

**Parameters**:
- value — t.Any — 要转换的值。

**Returns**:
- t.Any — 转换后的值。

**Raises**:
- BadParameter — 如果转换失败。

**内部调用(库内):**
- [`Parameter.check_iter`](src_click.md#sym-src_click_core.py-2486) — 检查传入的值是否为可迭代对象，并返回一个迭代器。

*来源: `src/click/core.py:2506`*

---
<a id="sym-src_click_core.py-2511"></a>
### `Parameter.convert` · method
```python
def convert(value: t.Any) -> t.Any:  # tuple[t.Any, ...]
```

Converts the given value to a tuple of values, each converted by the parameter's type.

**Parameters**:
- `value` — `t.Any` — The value to convert.

**Returns**:
- `t.Any` — A tuple of converted values.

**Raises**:
- `BadParameter` — If the number of values does not match the expected number (`nargs`).

**内部调用(库内):**
- [`Parameter.check_iter`](src_click.md#sym-src_click_core.py-2486) — 检查传入的值是否为可迭代对象，并返回一个迭代器。
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `src/click/core.py:2511`*

---
<a id="sym-src_click_core.py-2532"></a>
### `Parameter.value_is_missing` · method
```python
def value_is_missing(self, value: t.Any) -> bool
```

判断一个值是否缺失。

**Parameters**:
- value — t.Any — 要检查的值。

**Returns**:
- bool — 如果值缺失则返回 True，否则返回 False。

**Raises**:
- 无

*来源: `src/click/core.py:2532`*

---
<a id="sym-src_click_core.py-2550"></a>
### `Parameter.process_value` · method
```python
def process_value(self, ctx: Context, value: t.Any) -> t.Any
```

### `Parameter.process_value`

Process the value of this parameter, including type casting, missing value checks, and callback invocation.

**Parameters**:
- `ctx` — `Context` — The context in which the parameter is being processed.
- `value` — `t.Any` — The value to be processed.

**Returns**:
- `t.Any` — The processed value.

**Raises**:
- `MissingParameter` — If the value is required but missing.
- `BadParameter` — If the value is invalid.

**内部调用(库内):**
- [`Parameter.type_cast_value`](src_click.md#sym-src_click_core.py-2476) — Convert and validate a value against the parameter's type, multiple, and nargs.
- [`Parameter.value_is_missing`](src_click.md#sym-src_click_core.py-2532) — 判断一个值是否缺失。
- [`MissingParameter`](src_click.md#sym-src_click_exceptions.py-159) — `MissingParameter` 类用于表示在命令行参数解析过程中缺少必要参数的情况。

*来源: `src/click/core.py:2550`*

---
<a id="sym-src_click_core.py-2616"></a>
### `Parameter.resolve_envvar_value` · method
```python
def resolve_envvar_value(self, ctx: Context) -> str | None
```

Returns the value found in the environment variable(s) attached to this parameter.

**Parameters**:

- `ctx` — `Context` — The context object for the current command.

**Returns**:

- `str | None` — The value found in the environment variable(s), or `None` if the environment variable is not set or is empty.

**Raises**:

- None

*来源: `src/click/core.py:2616`*

---
<a id="sym-src_click_core.py-2661"></a>
### `Parameter.value_from_envvar` · method
```python
def value_from_envvar(self, ctx: Context) -> str | cabc.Sequence[str] | None
```

Process the raw environment variable string for this parameter.

**Parameters**:
- `ctx` — `Context` — The context object for the current command.

**Returns**:
- `str | cabc.Sequence[str] | None` — The processed value from the environment variable, split into a sequence if `nargs` is not 1.

**Raises**:
- None

**内部调用(库内):**
- [`Parameter.resolve_envvar_value`](src_click.md#sym-src_click_core.py-2616) — Returns the value found in the environment variable(s) attached to this paramete
- [`ParamType.split_envvar_value`](src_click.md#sym-src_click_types.py-147) — Given a value from an environment variable, this method splits it into small chu

*来源: `src/click/core.py:2661`*

---
<a id="sym-src_click_core.py-2677"></a>
### `Parameter.handle_parse_result` · method
```python
def handle_parse_result(
        self, ctx: Context, opts: cabc.Mapping[str, t.Any], args: list[str]
    ) -> tuple[t.Any, list[str]]
```

### 用途
处理用户输入解析结果，对值进行类型处理，并根据需要显示弃用警告。

### Parameters
- `ctx` — `Context` — 上下文对象，包含解析结果。
- `opts` — `Mapping[str, Any]` — 从解析器获取的选项值。
- `args` — `list[str]` — 从解析器获取的非选项参数值。

### Returns
- `tuple[Any, list[str]]` — 处理后的值和剩余的非选项参数值。

### Raises
- `UsageError` — 如果在处理过程中发生错误。

**内部调用(库内):**
- [`Context.get_parameter_source`](src_click.md#sym-src_click_core.py-937) — 获取参数的来源。这表明参数值是从哪里获得的。
- [`augment_usage_errors`](src_click.md#sym-src_click_core.py-120) — Context manager that attaches extra information to exceptions.
- [`Parameter.consume_value`](src_click.md#sym-src_click_core.py-2428) — Returns the parameter value produced by the parser.
- [`Context.set_parameter_source`](src_click.md#sym-src_click_core.py-928) — Set the source of a parameter. This indicates the location from which the value 
- [`_format_deprecated_suffix`](src_click.md#sym-src_click_core.py-106) — Return the trailing reason for a `DeprecationWarning` message, prefixed with a s
- [`style`](src_click.md#sym-src_click_termui.py-569) — **用途**: Styles a text with ANSI styles and returns the new string.
- [`Parameter.process_value`](src_click.md#sym-src_click_core.py-2550) — `Parameter.process_value`

*来源: `src/click/core.py:2677`*

---
<a id="sym-src_click_core.py-2765"></a>
### `Parameter.get_help_record` · method
```python
def get_help_record(self, ctx: Context) -> tuple[str, str] | None
```

获取参数的帮助记录。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `tuple[str, str] | None` — 参数的帮助记录，格式为 (名称, 描述)，如果无帮助记录则返回 `None`。

*来源: `src/click/core.py:2765`*

---
<a id="sym-src_click_core.py-2768"></a>
### `Parameter.get_usage_pieces` · method
```python
def get_usage_pieces(self, ctx: Context) -> list[str]
```

**用途**: 获取参数的使用片段列表。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `list[str]` — 参数的使用片段列表。

*来源: `src/click/core.py:2768`*

---
<a id="sym-src_click_core.py-2771"></a>
### `Parameter.get_error_hint` · method
```python
def get_error_hint(self, ctx: Context | None) -> str
```

**用途**: 获取一个字符串化的参数版本，用于错误消息中指示哪个参数导致了错误。

**Parameters**:
- `ctx` — `Context | None` — 上下文对象，可选。

**Returns**:
- `str` — 参数的字符串化版本，用于错误消息。

**Raises**:
- 无

*来源: `src/click/core.py:2771`*

---
<a id="sym-src_click_core.py-2781"></a>
### `Parameter.shell_complete` · method
```python
def shell_complete(self, ctx: Context, incomplete: str) -> list[CompletionItem]
```

**用途**: Return a list of completions for the incomplete value.

**Parameters**:
- `ctx` — `Context` — Invocation context for this command.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns**:
- `list[CompletionItem]` — A list of completions.

**Raises**:
- None

**内部调用(库内):**
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。

*来源: `src/click/core.py:2781`*

---
<a id="sym-src_click_core.py-2805"></a>
### `Option` · class
```python
class Option(Parameter)
```

`Option` 类是 Click 库中的一个类，用于定义命令行选项。它允许用户在命令行中指定参数，并提供各种属性和方法来控制这些选项的行为。

### 关键方法与典型用法

- **`__init__`**
  - **用途**: 初始化一个 `Option` 对象。
  - **Parameters**:
    - `param_decls` — `Sequence[str] | None` — 选项的声明，例如 `['-v', '--verbose']`。
    - `show_default` — `bool | str | None` — 是否显示默认值。
    - `prompt` — `bool | str` — 是否提示用户输入。
    - `confirmation_prompt` — `bool | str` — 是否提示用户确认输入。
    - `prompt_required` — `bool` — 是否要求用户输入。
    - `hide_input` — `bool` — 是否隐藏输入。
    - `is_flag` — `bool | None` — 是否是标志选项。
    - `flag_value` — `Any` — 标志选项的值。
    - `multiple` — `bool` — 是否允许多个值。
    - `count` — `bool` — 是否计数。
    - `allow_from_autoenv` — `bool` — 是否允许从环境变量中读取值。
    - `type` — `ParamType | Any | None` — 选项的类型。
    - `help` — `str | None` — 选项的帮助信息。

*来源: `src/click/core.py:2805`*

---
<a id="sym-src_click_core.py-2897"></a>
### `Option.__init__` · method
```python
def __init__(
        self,
        param_decls: cabc.Sequence[str] | None = None,
        show_default: bool | str | None = None,
        prompt: bool | str = False,
        confirmation_prompt: bool | str = False,
        prompt_required: bool = True,
        hide_input: bool = False,
        is_flag: bool | None = None,
        flag_value: t.Any = UNSET,
        multiple: bool = False,
        count: bool = False,
        allow_from_autoenv: bool = True,
        type: types.ParamType[t.Any] | t.Any | None = None,
        help: str | None = None,
        hidden: bool = False,
        show_choices: bool = True,
        show_envvar: bool = False,
        deprecated: bool | str = False,
        **attrs: t.Any,
    ) -> None
```

### Option.__init__

初始化一个命令行选项。

**Parameters**:
- `param_decls` — `cabc.Sequence[str] | None` — 选项的声明名称，例如 `["-v", "--verbose"]`。
- `show_default` — `bool | str | None` — 是否显示默认值，可以是布尔值或字符串。
- `prompt` — `bool | str` — 是否提示用户输入，可以是布尔值或字符串。
- `confirmation_prompt` — `bool | str` — 是否在确认时提示用户输入，可以是布尔值或字符串。
- `prompt_required` — `bool` — 是否要求用户输入。
- `hide_input` — `bool` — 是否隐藏用户输入。
- `is_flag` — `bool | None` — 是否是标志选项。
- `flag_value` — `t.Any` — 标志选项的值。
- `multiple` — `bool` — 是否允许多个值。
- `count` — `bool` — 是否计数。
- `allow_from_autoenv` — `bool` — 是否允许从自动环境变量中读取。
- `type` — `types.ParamType[t.Any] | t.Any | None` — 选项的类型。
- `help` — `str | None` — 选项的帮助信息。
- `hidden` — `bool` — 是否隐藏选项。
- `show_choices` — `bool` — 是否显示选项的可能值。
- `show_envvar` — `bool`

**内部调用(库内):**
- [`_format_deprecated_label`](src_click.md#sym-src_click_core.py-98) — Return the parenthesized deprecation label shown in help text.
- [`BoolParamType`](src_click.md#sym-src_click_types.py-761) — `BoolParamType` 类用于处理布尔类型的参数，提供将字符串或布尔值转换为布尔值的方法。
- [`IntRange`](src_click.md#sym-src_click_types.py-686) — `IntRange` 类用于定义一个整数范围参数类型，限制输入值在指定的整数范围内。

*来源: `src/click/core.py:2897`*

---
<a id="sym-src_click_core.py-3062"></a>
### `Option.to_info_dict` · method
```python
def to_info_dict(self) -> dict[str, t.Any]
```

将 `Option` 对象转换为包含相关信息的字典。

**Parameters**:
- 无

**Returns**:
- `dict[str, t.Any]`: 包含 `Option` 对象信息的字典，包括 `help`、`prompt`、`is_flag`、`flag_value`、`count` 和 `hidden`。

**Raises**:
- 无

*来源: `src/click/core.py:3062`*

---
<a id="sym-src_click_core.py-3081"></a>
### `Option.get_default` · method
```python
def get_default(
        self, ctx: Context, call: bool = True
    ) -> t.Any | t.Callable[[], t.Any] | None
```

**用途**: 返回此选项的默认值。

**Parameters**:
- `ctx` — `Context` — 上下文对象。
- `call` — `bool` — 是否调用默认值（默认为 `True`）。

**Returns**:
- `t.Any | t.Callable[[], t.Any] | None` — 默认值、可调用对象或 `None`。

**Raises**:
- 无

*来源: `src/click/core.py:3081`*

---
<a id="sym-src_click_core.py-3114"></a>
### `Option.get_error_hint` · method
```python
def get_error_hint(self, ctx: Context | None) -> str
```

### 用途
获取选项的错误提示信息。

### Parameters
- `ctx` — `Context | None` — 上下文对象，可选。

### Returns
- `str` — 选项的错误提示信息。

### Raises
- 无

*来源: `src/click/core.py:3114`*

---
<a id="sym-src_click_core.py-3120"></a>
### `Option._parse_decls` · method
```python
def _parse_decls(
        self, decls: cabc.Sequence[str], expose_value: bool
    ) -> tuple[str, list[str], list[str]]
```

解析命令行选项声明并返回选项名称、主要选项和次要选项。

**Parameters**:
- `decls` — `Sequence[str]` — 命令行选项声明的序列。
- `expose_value` — `bool` — 是否暴露值。

**Returns**:
- `tuple[str, list[str], list[str]]` — 选项名称、主要选项和次要选项的元组。

**Raises**:
- `TypeError` — 如果名称被定义两次。
- `ValueError` — 如果布尔选项使用相同的标志表示真和假。

**内部调用(库内):**
- [`_split_opt`](src_click.md#sym-src_click_parser.py-111) — _split_opt

*来源: `src/click/core.py:3120`*

---
<a id="sym-src_click_core.py-3181"></a>
### `Option.add_to_parser` · method
```python
def add_to_parser(self, parser: _OptionParser, ctx: Context) -> None
```

将选项添加到解析器中。

**Parameters**:
- `parser` — `_OptionParser` — 选项解析器对象。
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`_OptionParser.add_option`](src_click.md#sym-src_click_parser.py-265) — Adds a new option to the parser.

*来源: `src/click/core.py:3181`*

---
<a id="sym-src_click_core.py-3220"></a>
### `Option.get_help_record` · method
```python
def get_help_record(self, ctx: Context) -> tuple[str, str] | None
```

### 用途
获取选项的帮助记录。

### Parameters
- `ctx` — `Context` — 上下文对象。

### Returns
- `tuple[str, str] | None` — 选项的帮助记录，格式为 (选项名称, 描述)；如果选项被隐藏，则返回 `None`。

### Raises
- 无

**内部调用(库内):**
- [`join_options`](src_click.md#sym-src_click_formatting.py-302) — Given a list of option strings, this function joins them in the most appropriate
- [`Parameter.make_metavar`](src_click.md#sym-src_click_core.py-2368) — 生成命令行参数的元变量字符串。
- [`Option._write_opts`](src_click.md#sym-src_click_core.py-3226) — **用途**: 将选项列表转换为格式化的字符串。
- [`Option.get_help_extra`](src_click.md#sym-src_click_core.py-3265) — **用途**: 获取选项的帮助额外信息，包括环境变量和默认值。

*来源: `src/click/core.py:3220`*

---
<a id="sym-src_click_core.py-3226"></a>
### `Option._write_opts` · method
```python
def _write_opts(opts: cabc.Sequence[str]) -> str
```

**用途**: 将选项列表转换为格式化的字符串。

**Parameters**:
- `opts` — `cabc.Sequence[str]` — 选项列表。

**Returns**:
- `str` — 格式化的选项字符串。

**Raises**:
- 无

**内部调用(库内):**
- [`join_options`](src_click.md#sym-src_click_formatting.py-302) — Given a list of option strings, this function joins them in the most appropriate
- [`Parameter.make_metavar`](src_click.md#sym-src_click_core.py-2368) — 生成命令行参数的元变量字符串。

*来源: `src/click/core.py:3226`*

---
<a id="sym-src_click_core.py-3265"></a>
### `Option.get_help_extra` · method
```python
def get_help_extra(self, ctx: Context) -> types.OptionHelpExtra
```

**用途**: 获取选项的帮助额外信息，包括环境变量和默认值。

**Parameters**:
- `ctx` — `Context` — 上下文对象，包含命令行解析和执行的上下文信息。

**Returns**:
- `OptionHelpExtra` — 一个字典，包含选项的帮助额外信息，如环境变量和默认值。

**Raises**:
- 无

**内部调用(库内):**
- [`Option.get_default`](src_click.md#sym-src_click_core.py-3081) — **用途**: 返回此选项的默认值。
- [`_split_opt`](src_click.md#sym-src_click_parser.py-111) — _split_opt
- [`_NumberRangeBase._describe_range`](src_click.md#sym-src_click_types.py-659) — **用途**: 生成用于帮助文本的范围描述。

*来源: `src/click/core.py:3265`*

---
<a id="sym-src_click_core.py-3349"></a>
### `Option.prompt_for_value` · method
```python
def prompt_for_value(self, ctx: Context) -> t.Any
```

### 用途
`Option.prompt_for_value` 方法用于在值不存在时提示用户输入一个有效值，并返回处理后的值。

### Parameters
- `ctx` — `Context` — 上下文对象，包含当前命令的上下文信息。

### Returns
- `t.Any` — 处理后的值。

### Raises
- `Abort` — 如果用户输入无效值并选择中止。

**内部调用(库内):**
- [`Option.get_default`](src_click.md#sym-src_click_core.py-3081) — **用途**: 返回此选项的默认值。
- [`confirm`](src_click.md#sym-src_click_termui.py-231) — **用途**: Prompts the user for confirmation with a yes/no question.
- [`prompt`](src_click.md#sym-src_click_termui.py-118) — **用途**: 提示用户输入，并根据参数进行类型检查和确认。
- [`Option.process_value`](src_click.md#sym-src_click_core.py-3527) — `Option.process_value`

*来源: `src/click/core.py:3349`*

---
<a id="sym-src_click_core.py-3399"></a>
### `Option.resolve_envvar_value` · method
```python
def resolve_envvar_value(self, ctx: Context) -> str | None
```

### 用途
`Option.resolve_envvar_value` 方法用于解析选项的环境变量值。它首先尝试从 `Option` 的 `envvar` 属性中获取环境变量值。如果未找到，则尝试使用 `Context` 的 `auto_envvar_prefix` 自动构建环境变量名称，并从环境变量中获取值。

### Parameters
- `ctx` — `Context` — 上下文对象，包含解析环境变量所需的信息。

### Returns
- `str | None` — 如果成功解析到环境变量值，则返回该值；否则返回 `None`。

### Raises
- 无

*来源: `src/click/core.py:3399`*

---
<a id="sym-src_click_core.py-3423"></a>
### `Option.value_from_envvar` · method
```python
def value_from_envvar(self, ctx: Context) -> t.Any
```

### 用途
处理环境变量值，根据选项类型和配置返回相应的值。

### Parameters
- `ctx` — `Context` — 上下文对象，包含命令行解析和执行的上下文信息。

### Returns
- `t.Any` — 根据选项类型和配置返回相应的值，可能是 `None`、布尔值或字符串列表。

### Raises
- 无

**内部调用(库内):**
- [`Option.resolve_envvar_value`](src_click.md#sym-src_click_core.py-3399) — 用途
- [`BoolParamType.str_to_bool`](src_click.md#sym-src_click_types.py-798) — Convert a string to a boolean value.
- [`ParamType.split_envvar_value`](src_click.md#sym-src_click_types.py-147) — Given a value from an environment variable, this method splits it into small chu
- [`batch`](src_click.md#sym-src_click_core.py-115) — 将可迭代对象分成指定大小的批次。

*来源: `src/click/core.py:3423`*

---
<a id="sym-src_click_core.py-3465"></a>
### `Option.consume_value` · method
```python
def consume_value(
        self, ctx: Context, opts: cabc.Mapping[str, Parameter]
    ) -> tuple[t.Any, ParameterSource]
```

### Option.consume_value

Consume the value for an option, handling both flag options and interactive prompts.

**Parameters**:
- `ctx` — `Context`: The context object for the current command.
- `opts` — `Mapping[str, Parameter]`: A mapping of option names to parameter objects.

**Returns**:
- `tuple[Any, ParameterSource]`: A tuple containing the value and the source of the value.

**Raises**:
- None

**内部调用(库内):**
- [`Option.prompt_for_value`](src_click.md#sym-src_click_core.py-3349) — 用途

*来源: `src/click/core.py:3465`*

---
<a id="sym-src_click_core.py-3527"></a>
### `Option.process_value` · method
```python
def process_value(self, ctx: Context, value: t.Any) -> t.Any:
        # process_value has to be overridden on Options in order to capture
        # `value == UNSET` cases before `type_cast_value()` gets called.
        #
        # Refs:
        # https://github.com/pallets/click/issues/3069
```

### `Option.process_value`

处理选项的值。如果选项是标志且未设置且是布尔标志，则将其设置为 `False`。如果存在回调函数，则调用回调函数并返回其结果。

**Parameters**:
- `ctx` — `Context` — 上下文对象。
- `value` — `t.Any` — 选项的值。

**Returns**:
- `t.Any` — 处理后的值。

**Raises**:
- 无

*来源: `src/click/core.py:3527`*

---
<a id="sym-src_click_core.py-3545"></a>
### `Argument` · class
```python
class Argument(Parameter)
```

`Argument` 类代表一个命令行参数，用于定义和处理命令行中的位置参数。

### 方法

- **__init__(self, param_decls: cabc.Sequence[str], required: bool | None = None, help: str | None = None, **attrs: t.Any) -> None**
  - **参数**:
    - `param_decls` — `cabc.Sequence[str]` — 参数的声明名称，例如 `['<filename>']`。
    - `required` — `bool | None` — 参数是否为必需，默认为 `None`，自动检测。
    - `help` — `str | None` — 参数的帮助信息，默认为 `None`。
    - `**attrs` — `t.Any` — 其他自定义属性。
  - **用途**: 初始化一个 `Argument` 对象，设置参数的声明名称、是否必需和帮助信息。

- **to_info_dict(self) -> dict[str, t.Any]**
  - **返回**:
    - `dict[str, t.Any]` — 参数的详细信息字典。
  - **用途**: 返回参数的详细信息字典，用于生成命令行帮助信息。

- **human_readable_name(self) -> str**
  - **返回**:
    - `str` — 参数的人类可读名称。
  - **用途**: 返回参数的人类可读名称，用于显示在命令行帮助信息中。

- **make_metavar(self, ctx: Context) -> str**
  - **参数**:

*来源: `src/click/core.py:3545`*

---
<a id="sym-src_click_core.py-3560"></a>
### `Argument.__init__` · method
```python
def __init__(
        self,
        param_decls: cabc.Sequence[str],
        required: bool | None = None,
        help: str | None = None,
        **attrs: t.Any,
    ) -> None:
        # Auto-detect the requirement status of the argument if not explicitly set.
```

**用途**: 初始化一个 `Argument` 对象，用于处理命令行参数。

**Parameters**:
- `param_decls` — `Sequence[str]` — 参数声明的序列，通常是一个包含参数名称的字符串列表。
- `required` — `bool | None` — 参数是否必需，默认为 `None`，表示根据其他属性自动检测。
- `help` — `str | None` — 参数的帮助信息，默认为 `None`。
- `**attrs` — `Any` — 其他任意属性。

**Returns**:
- `None`

**Raises**:
- `TypeError` — 如果传入了 `multiple` 关键字参数。

**内部调用(库内):**
- [`_format_deprecated_label`](src_click.md#sym-src_click_core.py-98) — Return the parenthesized deprecation label shown in help text.

*来源: `src/click/core.py:3560`*

---
<a id="sym-src_click_core.py-3593"></a>
### `Argument.to_info_dict` · method
```python
def to_info_dict(self) -> dict[str, t.Any]
```

将 `Argument` 对象转换为包含帮助信息的字典。

**Parameters**:
- 无

**Returns**:
- `dict[str, t.Any]`: 包含帮助信息的字典。

**Raises**:
- 无

*来源: `src/click/core.py:3593`*

---
<a id="sym-src_click_core.py-3599"></a>
### `Argument.human_readable_name` · method
装饰器: `@property`
```python
def human_readable_name(self) -> str
```

返回参数的可读名称。

**Parameters**:
- 无

**Returns**:
- `str`: 参数的可读名称。如果 `metavar` 属性不为 `None`，则返回 `metavar`；否则返回 `name` 的大写形式。

*来源: `src/click/core.py:3599`*

---
<a id="sym-src_click_core.py-3604"></a>
### `Argument.make_metavar` · method
```python
def make_metavar(self, ctx: Context) -> str
```

生成命令行参数的元变量字符串。

**Parameters:**
- `ctx` — `Context` — 上下文对象。

**Returns:**
- `str` — 生成的元变量字符串。

**Raises:**
- 无

*来源: `src/click/core.py:3604`*

---
<a id="sym-src_click_core.py-3618"></a>
### `Argument._parse_decls` · method
```python
def _parse_decls(
        self, decls: cabc.Sequence[str], expose_value: bool
    ) -> tuple[str, list[str], list[str]]
```

### Argument._parse_decls

解析参数声明并返回参数名称、参数列表和选项列表。

**Parameters**:
- `decls` — `Sequence[str]` — 参数声明列表。
- `expose_value` — `bool` — 是否暴露值。

**Returns**:
- `tuple[str, list[str], list[str]]` — 参数名称、参数列表和选项列表。

**Raises**:
- `TypeError` — 如果参数声明列表长度不为1且未暴露值。

*来源: `src/click/core.py:3618`*

---
<a id="sym-src_click_core.py-3637"></a>
### `Argument.get_usage_pieces` · method
```python
def get_usage_pieces(self, ctx: Context) -> list[str]
```

获取命令行参数的使用片段。

**Parameters**:
- `ctx` — `Context` — 上下文对象。

**Returns**:
- `list[str]` — 参数的使用片段列表。

**Raises**:
- 无

**内部调用(库内):**
- [`Argument.make_metavar`](src_click.md#sym-src_click_core.py-3604) — 生成命令行参数的元变量字符串。

*来源: `src/click/core.py:3637`*

---
<a id="sym-src_click_core.py-3640"></a>
### `Argument.get_help_record` · method
```python
def get_help_record(self, ctx: Context) -> tuple[str, str] | None
```

### Argument.get_help_record

Returns a tuple containing the metavar and help text for the argument, or `None` if no help text is provided.

**Parameters**:
- `ctx` — `Context` — The context in which the argument is being processed.

**Returns**:
- `tuple[str, str] | None` — A tuple containing the metavar and help text, or `None` if no help text is provided.

**内部调用(库内):**
- [`Argument.make_metavar`](src_click.md#sym-src_click_core.py-3604) — 生成命令行参数的元变量字符串。

*来源: `src/click/core.py:3640`*

---
<a id="sym-src_click_core.py-3646"></a>
### `Argument.get_error_hint` · method
```python
def get_error_hint(self, ctx: Context | None) -> str
```

### Argument.get_error_hint

Returns a hint for an error related to the argument, formatted based on the context.

**Parameters**:
- `ctx` — `Context | None` — The context in which the argument is used, or `None` if no context is available.

**Returns**:
- `str` — A string hint for the error, typically the metavar or human-readable name of the argument.

**Raises**:
- None

**内部调用(库内):**
- [`Argument.make_metavar`](src_click.md#sym-src_click_core.py-3604) — 生成命令行参数的元变量字符串。

*来源: `src/click/core.py:3646`*

---
<a id="sym-src_click_core.py-3651"></a>
### `Argument.add_to_parser` · method
```python
def add_to_parser(self, parser: _OptionParser, ctx: Context) -> None
```

将当前参数添加到解析器中。

**Parameters**:
- `parser` — `_OptionParser` — 用于解析命令行参数的解析器对象。
- `ctx` — `Context` — 命令行上下文对象。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`_OptionParser.add_argument`](src_click.md#sym-src_click_parser.py-290) — Adds a positional argument named `dest` to the parser.

*来源: `src/click/core.py:3651`*

---
<a id="sym-src_click_core.py-3655"></a>
### `__getattr__` · func
```python
def __getattr__(name: str) -> object
```

用途: 重写 `__getattr__` 方法，用于处理对未定义属性的访问。

**Parameters**:
- `name` — `str` — 要访问的属性名称。

**Returns**:
- `object` — 返回与属性名称对应的对象。

**Raises**:
- `AttributeError` — 如果属性名称未定义且不是 `BaseCommand` 或 `MultiCommand`。

*来源: `src/click/core.py:3655`*

---

## `src/click/decorators.py`

<a id="sym-src_click_decorators.py-28"></a>
### `pass_context` · func
```python
def pass_context(f: t.Callable[te.Concatenate[Context, P], R]) -> t.Callable[P, R]
```

用途: 标记一个回调函数，使其能够接收当前上下文对象作为第一个参数。

**Parameters**:
- `f` — `t.Callable[te.Concatenate[Context, P], R]` — 要标记的回调函数。

**Returns**:
- `t.Callable[P, R]` — 返回一个新的回调函数，该函数会在调用时自动将当前上下文对象作为第一个参数传递给原始函数。

**Raises**:
- 无

*来源: `src/click/decorators.py:28`*

---
<a id="sym-src_click_decorators.py-33"></a>
### `new_func` · func
```python
def new_func(*args: P.args, **kwargs: P.kwargs) -> R
```

调用当前上下文并传递参数。

**Parameters**:
- `*args` — `P.args` — 传递给当前上下文的位置参数。
- `**kwargs` — `P.kwargs` — 传递给当前上下文的关键字参数。

**Returns**:
- `R` — 返回当前上下文的处理结果。

*来源: `src/click/decorators.py:33`*

---
<a id="sym-src_click_decorators.py-39"></a>
### `pass_obj` · func
```python
def pass_obj(f: t.Callable[te.Concatenate[T, P], R]) -> t.Callable[P, R]
```

**用途**: 将对象传递给函数，该对象来自当前上下文的 `Context.obj`。

**Parameters**:
- `f` — `t.Callable[te.Concatenate[T, P], R]` — 要包装的函数，它接受一个额外的第一个参数 `T`，通常代表上下文对象。

**Returns**:
- `t.Callable[P, R]` — 返回一个新的函数，该函数在调用时会将当前上下文的 `Context.obj` 作为第一个参数传递给原始函数 `f`。

**Raises**:
- 无

*来源: `src/click/decorators.py:39`*

---
<a id="sym-src_click_decorators.py-45"></a>
### `new_func` · func
```python
def new_func(*args: P.args, **kwargs: P.kwargs) -> R
```

调用当前上下文对象的方法，并传递给定的参数。

**Parameters**:
- `*args` — `P.args` — 传递给方法的参数。
- `**kwargs` — `P.kwargs` — 传递给方法的关键字参数。

**Returns**:
- `R` — 方法的返回值。

**Raises**:
- 无

*来源: `src/click/decorators.py:45`*

---
<a id="sym-src_click_decorators.py-51"></a>
### `make_pass_decorator` · func
```python
def make_pass_decorator(
    object_type: type[T], ensure: bool = False
) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]
```

### `make_pass_decorator`

Given an object type, this creates a decorator that will work similarly to `pass_obj` but instead of passing the object of the current context, it will find the innermost context of type `object_type`.

**Parameters:**
- `object_type` — `type[T]` — The type of the object to pass.
- `ensure` — `bool` — If set to `True`, a new object will be created and remembered on the context if it's not there yet.

**Returns:**
- `t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]` — A decorator that can be used to pass an object of the specified type to a function.

**Raises:**
- `RuntimeError` — If the callback is invoked without a context object of the specified type existing.

**内部调用(库内):**
- [`Context.ensure_object`](src_click.md#sym-src_click_core.py-748) — **用途**: 确保在当前上下文中存在指定类型的对象，如果不存在则创建一个新的实例。
- [`Context.find_object`](src_click.md#sym-src_click_core.py-736) — Finds the closest object of a given type.

*来源: `src/click/decorators.py:51`*

---
<a id="sym-src_click_decorators.py-76"></a>
### `decorator` · func
```python
def decorator(f: t.Callable[te.Concatenate[T, P], R]) -> t.Callable[P, R]
```

用途: 装饰器函数，用于在调用被装饰的函数时，确保上下文中存在指定类型的对象，并调用该函数。

**Parameters**:
- `f` — `t.Callable[te.Concatenate[T, P], R]` — 被装饰的函数。

**Returns**:
- `t.Callable[P, R]` — 装饰后的函数。

**Raises**:
- `RuntimeError` — 如果上下文中不存在指定类型的对象。

**内部调用(库内):**
- [`Context.ensure_object`](src_click.md#sym-src_click_core.py-748) — **用途**: 确保在当前上下文中存在指定类型的对象，如果不存在则创建一个新的实例。
- [`Context.find_object`](src_click.md#sym-src_click_core.py-736) — Finds the closest object of a given type.

*来源: `src/click/decorators.py:76`*

---
<a id="sym-src_click_decorators.py-77"></a>
### `new_func` · func
```python
def new_func(*args: P.args, **kwargs: P.kwargs) -> R
```

调用当前上下文中的对象，并在对象不存在时抛出异常。

**Parameters**:
- `args` — `P.args` — 传递给回调函数的位置参数。
- `kwargs` — `P.kwargs` — 传递给回调函数的关键字参数。

**Returns**:
- `R` — 回调函数的返回值。

**Raises**:
- `RuntimeError` — 如果上下文中不存在指定类型的对象。

**内部调用(库内):**
- [`Context.ensure_object`](src_click.md#sym-src_click_core.py-748) — **用途**: 确保在当前上下文中存在指定类型的对象，如果不存在则创建一个新的实例。
- [`Context.find_object`](src_click.md#sym-src_click_core.py-736) — Finds the closest object of a given type.

*来源: `src/click/decorators.py:77`*

---
<a id="sym-src_click_decorators.py-100"></a>
### `pass_meta_key` · func
```python
def pass_meta_key(
    key: str, *, doc_description: str | None = None
) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]
```

用途: 创建一个装饰器，将 `click.Context.meta` 中的指定键作为第一个参数传递给被装饰的函数。

**Parameters**:
- `key` — `str` — `Context.meta` 中的键，用于传递。
- `doc_description` — `str | None` — 描述被传递的对象，插入到装饰器的文档字符串中。默认为 "the 'key' key from Context.meta"。

**Returns**:
- `Callable[[Callable[Concatenate[T, P], R]], Callable[P, R]]` — 返回一个装饰器，该装饰器将 `key` 作为第一个参数传递给被装饰的函数。

*来源: `src/click/decorators.py:100`*

---
<a id="sym-src_click_decorators.py-115"></a>
### `decorator` · func
```python
def decorator(f: t.Callable[te.Concatenate[T, P], R]) -> t.Callable[P, R]
```

用途: 用于装饰函数，使其在调用时能够访问当前上下文并传递对象。

**Parameters**:
- `f` — `t.Callable[te.Concatenate[T, P], R]` — 要装饰的函数。

**Returns**:
- `t.Callable[P, R]` — 装饰后的函数。

**Raises**:
- 无

*来源: `src/click/decorators.py:115`*

---
<a id="sym-src_click_decorators.py-116"></a>
### `new_func` · func
```python
def new_func(*args: P.args, **kwargs: P.kwargs) -> R
```

调用当前上下文中的函数并传递参数。

**Parameters**:
- `args` — `P.args` — 传递给函数的参数。
- `kwargs` — `P.kwargs` — 传递给函数的关键字参数。

**Returns**:
- `R` — 函数的返回值。

**Raises**:
- 无

*来源: `src/click/decorators.py:116`*

---
<a id="sym-src_click_decorators.py-138"></a>
### `command` · func
装饰器: `@t.overload`
```python
def command(name: _AnyCallable) -> Command
```

用途: 定义一个命令行命令。

**Parameters**:
- `name` — `_AnyCallable` — 要定义的命令的名称或可调用对象。

**Returns**:
- `Command` — 返回一个 `Command` 对象，表示定义的命令。

*来源: `src/click/decorators.py:138`*

---
<a id="sym-src_click_decorators.py-144"></a>
### `command` · func
装饰器: `@t.overload`
```python
def command(
    name: str | None,
    cls: type[CmdType],
    **attrs: t.Any,
) -> t.Callable[[_AnyCallable], CmdType]
```

### command

定义一个命令行命令。

**Parameters**:
- `name` — `str | None` — 命令的名称。
- `cls` — `type[CmdType]` — 命令类。
- `**attrs` — `t.Any` — 其他属性。

**Returns**:
- `CmdType` — 返回一个命令类。

*来源: `src/click/decorators.py:144`*

---
<a id="sym-src_click_decorators.py-153"></a>
### `command` · func
装饰器: `@t.overload`
```python
def command(
    name: None = None,
    *,
    cls: type[CmdType],
    **attrs: t.Any,
) -> t.Callable[[_AnyCallable], CmdType]
```

定义一个命令行命令。

**Parameters**:
- `name` — `None` — 命令的名称。
- `cls` — `type[CmdType]` — 命令的类。
- `**attrs` — `t.Any` — 其他属性。

**Returns**:
- `t.Callable[[_AnyCallable], CmdType]` — 返回一个装饰器函数。

*来源: `src/click/decorators.py:153`*

---
<a id="sym-src_click_decorators.py-163"></a>
### `command` · func
装饰器: `@t.overload`
```python
def command(
    name: str | None = ..., cls: None = None, **attrs: t.Any
) -> t.Callable[[_AnyCallable], Command]
```

用途: 定义一个命令行命令。

**Parameters**:
- `name` — `str | None` — 命令的名称。如果未提供，则使用函数名。
- `cls` — `None` — 命令类。默认为 `None`。
- `**attrs` — `t.Any` — 传递给命令类的其他属性。

**Returns**:
- `t.Callable[[_AnyCallable], Command]` — 一个装饰器，用于将函数转换为命令。

*来源: `src/click/decorators.py:163`*

---
<a id="sym-src_click_decorators.py-168"></a>
### `command` · func
```python
def command(
    name: str | _AnyCallable | None = None,
    cls: type[CmdType] | None = None,
    **attrs: t.Any,
) -> Command | t.Callable[[_AnyCallable], Command | CmdType]
```

创建一个新的 `Command` 并使用装饰的函数作为回调。这还会自动将所有装饰的 `option` 和 `argument` 作为参数附加到命令上。

**Parameters:**
- `name` — `str | _AnyCallable | None` — 命令的名称。默认值为修改函数名称，将下划线 `_` 替换为短横线 `-`，并移除后缀 `_command`, `_cmd`, `_group`, `_grp`。
- `cls` — `type[CmdType] | None` — 要创建的命令类。默认值为 `Command`。

**Returns:**
- `Command | t.Callable[[_AnyCallable], Command | CmdType]` — 装饰后的函数变为 `Command` 实例，可以作为命令行工具调用或附加到命令 `Group`。

**内部调用(库内):**
- [`decorator`](src_click.md#sym-src_click_decorators.py-76) — 用途: 装饰器函数，用于在调用被装饰的函数时，确保上下文中存在指定类型的对象，并调用该函数。

*来源: `src/click/decorators.py:168`*

---
<a id="sym-src_click_decorators.py-217"></a>
### `decorator` · func
```python
def decorator(f: _AnyCallable) -> CmdType
```

将一个可调用对象转换为命令对象。

**Parameters**:
- `f` — `_AnyCallable` — 要转换的可调用对象。

**Returns**:
- `CmdType` — 转换后的命令对象。

**Raises**:
- `TypeError` — 如果尝试将一个回调对象两次转换为命令对象。

*来源: `src/click/decorators.py:217`*

---
<a id="sym-src_click_decorators.py-263"></a>
### `group` · func
装饰器: `@t.overload`
```python
def group(name: _AnyCallable) -> Group
```

创建一个命令组。

**Parameters**:
- `name` — `_AnyCallable` — 命令组的名称。

**Returns**:
- `Group` — 创建的命令组对象。

*来源: `src/click/decorators.py:263`*

---
<a id="sym-src_click_decorators.py-269"></a>
### `group` · func
装饰器: `@t.overload`
```python
def group(
    name: str | None,
    cls: type[GrpType],
    **attrs: t.Any,
) -> t.Callable[[_AnyCallable], GrpType]
```

创建一个命令组。

**Parameters:**
- `name` — `str | None` — 命令组的名称。
- `cls` — `type[GrpType]` — 命令组的类。
- `**attrs` — `t.Any` — 传递给命令组类的其他属性。

**Returns:**
- `t.Callable[[_AnyCallable], GrpType]` — 一个装饰器，用于将函数转换为命令组。

*来源: `src/click/decorators.py:269`*

---
<a id="sym-src_click_decorators.py-278"></a>
### `group` · func
装饰器: `@t.overload`
```python
def group(
    name: None = None,
    *,
    cls: type[GrpType],
    **attrs: t.Any,
) -> t.Callable[[_AnyCallable], GrpType]
```

### group

创建一个命令组。

**Parameters**:
- `name` — `None` — 命令组的名称。
- `cls` — `type[GrpType]` — 命令组的类。
- `**attrs` — `t.Any` — 其他属性。

**Returns**:
- `t.Callable[[_AnyCallable], GrpType]` — 返回一个装饰器，用于将函数转换为命令组。

*来源: `src/click/decorators.py:278`*

---
<a id="sym-src_click_decorators.py-288"></a>
### `group` · func
装饰器: `@t.overload`
```python
def group(
    name: str | None = ..., cls: None = None, **attrs: t.Any
) -> t.Callable[[_AnyCallable], Group]
```

**用途**: 用于创建一个命令组，可以包含多个子命令。

**Parameters**:
- `name` — `str | None` — 命令组的名称。
- `cls` — `None` — 自定义的命令组类。
- `**attrs` — `t.Any` — 传递给命令组类的其他属性。

**Returns**:
- `t.Callable[[_AnyCallable], Group]` — 返回一个装饰器，用于将函数转换为命令组。

*来源: `src/click/decorators.py:288`*

---
<a id="sym-src_click_decorators.py-293"></a>
### `group` · func
```python
def group(
    name: str | _AnyCallable | None = None,
    cls: type[GrpType] | None = None,
    **attrs: t.Any,
) -> Group | t.Callable[[_AnyCallable], Group | GrpType]
```

**用途**: 创建一个新的 `Group` 对象，使用一个函数作为回调。这与 `command` 函数类似，但 `cls` 参数被设置为 `Group`。

**Parameters**:
- `name` — `str | _AnyCallable | None` — 命令的名称或回调函数。
- `cls` — `type[GrpType] | None` — 用于创建组的类，默认为 `Group`。
- `**attrs` — `t.Any` — 传递给组的其他属性。

**Returns**:
- `Group | t.Callable[[_AnyCallable], Group | GrpType]` — 如果 `name` 是可调用的，则返回一个 `Group` 对象；否则返回一个装饰器函数。

**Raises**:
- 无

**内部调用(库内):**
- [`command`](src_click.md#sym-src_click_decorators.py-138) — 用途: 定义一个命令行命令。

*来源: `src/click/decorators.py:293`*

---
<a id="sym-src_click_decorators.py-314"></a>
### `_param_memo` · func
```python
def _param_memo(f: t.Callable[..., t.Any], param: Parameter) -> None
```

### _param_memo

将参数添加到命令或函数的参数列表中。

**Parameters**:
- `f` — `t.Callable[..., t.Any]` — 要添加参数的命令或函数。
- `param` — `Parameter` — 要添加的参数。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/decorators.py:314`*

---
<a id="sym-src_click_decorators.py-324"></a>
### `argument` · func
```python
def argument(
    *param_decls: str, cls: type[Argument] | None = None, **attrs: t.Any
) -> t.Callable[[FC], FC]
```

Attaches an argument to the command. All positional arguments are passed as parameter declarations to :class:`Argument`; all keyword arguments are forwarded unchanged (except ``cls``).

**Parameters**:
- `param_decls` — `str` — Passed as positional arguments to the constructor of ``cls``.
- `cls` — `type[Argument] | None` — The argument class to instantiate. This defaults to :class:`Argument`.
- `attrs` — `t.Any` — Passed as keyword arguments to the constructor of ``cls``.

**Returns**:
- `FC` — The decorated function.

**Raises**:
- None

**内部调用(库内):**
- [`_param_memo`](src_click.md#sym-src_click_decorators.py-314) — _param_memo

*来源: `src/click/decorators.py:324`*

---
<a id="sym-src_click_decorators.py-345"></a>
### `decorator` · func
```python
def decorator(f: FC) -> FC
```

用途: 装饰器函数，用于将参数声明和属性应用到目标函数上。

**Parameters**:
- `f` — `FC` — 目标函数，将要被装饰的函数。

**Returns**:
- `FC` — 装饰后的函数。

**Raises**:
- 无

**内部调用(库内):**
- [`_param_memo`](src_click.md#sym-src_click_decorators.py-314) — _param_memo

*来源: `src/click/decorators.py:345`*

---
<a id="sym-src_click_decorators.py-352"></a>
### `option` · func
```python
def option(
    *param_decls: str, cls: type[Option] | None = None, **attrs: t.Any
) -> t.Callable[[FC], FC]
```

Attaches an option to the command. All positional arguments are passed as parameter declarations to :class:`Option`; all keyword arguments are forwarded unchanged (except ``cls``).

**Parameters**:
- `param_decls` — `str` — Passed as positional arguments to the constructor of ``cls``.
- `cls` — `type[Option] | None` — The option class to instantiate. This defaults to :class:`Option`.
- `attrs` — `t.Any` — Passed as keyword arguments to the constructor of ``cls``.

**Returns**:
- `FC` — The decorated function.

**Raises**:
- None

**内部调用(库内):**
- [`_param_memo`](src_click.md#sym-src_click_decorators.py-314) — _param_memo

*来源: `src/click/decorators.py:352`*

---
<a id="sym-src_click_decorators.py-373"></a>
### `decorator` · func
```python
def decorator(f: FC) -> FC
```

用途: 用于装饰函数，添加参数声明和属性。

**Parameters**:
- `f` — `FC` — 要装饰的函数。

**Returns**:
- `FC` — 装饰后的函数。

**Raises**:
- 无

**内部调用(库内):**
- [`_param_memo`](src_click.md#sym-src_click_decorators.py-314) — _param_memo

*来源: `src/click/decorators.py:373`*

---
<a id="sym-src_click_decorators.py-380"></a>
### `confirmation_option` · func
```python
def confirmation_option(*param_decls: str, **kwargs: t.Any) -> t.Callable[[FC], FC]
```

### confirmation_option

Add a `--yes` option which shows a prompt before continuing if not passed. If the prompt is declined, the program will exit.

**Parameters**:
- `param_decls` — `str` — One or more option names. Defaults to the single value `"--yes"`.
- `kwargs` — `t.Any` — Extra arguments are passed to `option`.

**Returns**:
- `t.Callable[[FC], FC]` — A decorator that can be applied to a command function to add the confirmation option.

**Raises**:
- `Abort(RuntimeError)` — If the prompt is declined, the program will exit.

**内部调用(库内):**
- [`Context.abort`](src_click.md#sym-src_click_core.py-811) — Abort the script execution.
- [`option`](src_click.md#sym-src_click_decorators.py-352) — Attaches an option to the command. All positional arguments are passed as parame

*来源: `src/click/decorators.py:380`*

---
<a id="sym-src_click_decorators.py-389"></a>
### `callback` · func
```python
def callback(ctx: Context, param: Parameter, value: bool) -> None
```

用途: 在命令行参数处理过程中，根据参数值决定是否中止命令执行。

**Parameters**:
- `ctx` — `Context` — 命令上下文对象。
- `param` — `Parameter` — 当前处理的参数对象。
- `value` — `bool` — 参数的值，`True` 或 `False`。

**Returns**:
- `None`

**Raises**:
- `RuntimeError` — 如果 `value` 为 `False`，则调用 `ctx.abort()` 中止命令执行。

**内部调用(库内):**
- [`Context.abort`](src_click.md#sym-src_click_core.py-811) — Abort the script execution.

*来源: `src/click/decorators.py:389`*

---
<a id="sym-src_click_decorators.py-404"></a>
### `password_option` · func
```python
def password_option(*param_decls: str, **kwargs: t.Any) -> t.Callable[[FC], FC]
```

Add a `--password` option which prompts for a password, hiding input and asking to enter the value again for confirmation.

**Parameters**:
- `param_decls` — `str` — One or more option names. Defaults to the single value `"--password"`.
- `kwargs` — `t.Any` — Extra arguments are passed to `option`.

**Returns**:
- `t.Callable[[FC], FC]` — A decorator that adds the `--password` option to the command.

**内部调用(库内):**
- [`option`](src_click.md#sym-src_click_decorators.py-352) — Attaches an option to the command. All positional arguments are passed as parame

*来源: `src/click/decorators.py:404`*

---
<a id="sym-src_click_decorators.py-421"></a>
### `version_option` · func
```python
def version_option(
    version: str | None = None,
    *param_decls: str,
    package_name: str | None = None,
    prog_name: str | None = None,
    message: str | None = None,
    **kwargs: t.Any,
) -> t.Callable[[FC], FC]
```

**用途**: 添加一个 `--version` 选项，该选项会立即打印版本号并退出程序。

**Parameters**:
- `version` — `str | None` — 要显示的版本号。如果未提供，Click 将尝试检测它。
- `param_decls` — `str` — 一个或多个选项名称。默认值为单个值 `--version`。
- `package_name` — `str | None` — 用于检测版本的包名称。如果未提供，Click 将尝试检测它。
- `prog_name` — `str | None` — 要在消息中显示的 CLI 名称。如果未提供，将从命令中检测。
- `message` — `str | None` — 要显示的消息。可用的值包括 `%(prog)s`、`%(package)s` 和 `%(version)s`。默认值为 `%(prog)s, version %(version)s`。
- `kwargs` — `t.Any` — 传递给 `option` 的额外参数。

**Returns**:
- `t.Callable[[FC], FC]` — 返回一个装饰器函数。

**Raises**:
- `RuntimeError` — 如果无法检测版本。

**内部调用(库内):**
- [`Context.find_root`](src_click.md#sym-src_click_core.py-729) — 用途: 找到当前上下文的最外层上下文。
- [`Context.exit`](src_click.md#sym-src_click_core.py-815) — Exits the application with a given exit code.
- [`option`](src_click.md#sym-src_click_decorators.py-352) — Attaches an option to the command. All positional arguments are passed as parame

*来源: `src/click/decorators.py:421`*

---
<a id="sym-src_click_decorators.py-484"></a>
### `callback` · func
```python
def callback(ctx: Context, param: Parameter, value: bool) -> None
```

### `callback` 函数

在命令行工具中处理版本信息的回调函数。

**Parameters:**
- `ctx` — `Context` — 命令行上下文对象。
- `param` — `Parameter` — 当前参数对象。
- `value` — `bool` — 参数的值。

**Returns:**
- `None`

**Raises:**
- `RuntimeError` — 如果无法确定包的版本信息。

**内部调用(库内):**
- [`Context.find_root`](src_click.md#sym-src_click_core.py-729) — 用途: 找到当前上下文的最外层上下文。
- [`Context.exit`](src_click.md#sym-src_click_core.py-815) — Exits the application with a given exit code.

*来源: `src/click/decorators.py:484`*

---
<a id="sym-src_click_decorators.py-527"></a>
### `help_option` · func
```python
def help_option(*param_decls: str, **kwargs: t.Any) -> t.Callable[[FC], FC]
```

Pre-configured `--help` option which immediately prints the help page and exits the program.

**Parameters**:
- `param_decls` — `str` — One or more option names. Defaults to the single value `"--help"`.
- `kwargs` — `t.Any` — Extra arguments are passed to `option`.

**Returns**:
- `t.Callable[[FC], FC]` — A decorator that can be applied to a command to add the `--help` option.

**Raises**:
- `None`

**内部调用(库内):**
- [`Context.exit`](src_click.md#sym-src_click_core.py-815) — Exits the application with a given exit code.
- [`option`](src_click.md#sym-src_click_decorators.py-352) — Attaches an option to the command. All positional arguments are passed as parame

*来源: `src/click/decorators.py:527`*

---
<a id="sym-src_click_decorators.py-536"></a>
### `show_help` · func
```python
def show_help(ctx: Context, param: Parameter, value: bool) -> None
```

显示帮助页面并退出。

**Parameters**:
- ctx — Context — 上下文对象。
- param — Parameter — 参数对象。
- value — bool — 是否显示帮助。

**Returns**:
- None

**Raises**:
- None

**内部调用(库内):**
- [`Context.exit`](src_click.md#sym-src_click_core.py-815) — Exits the application with a given exit code.

*来源: `src/click/decorators.py:536`*

---

## `src/click/exceptions.py`

<a id="sym-src_click_exceptions.py-19"></a>
### `_join_param_hints` · func
```python
def _join_param_hints(param_hint: cabc.Sequence[str] | str | None) -> str | None
```

将参数提示（`param_hint`）合并成一个字符串。

**Parameters**:
- `param_hint` — `cabc.Sequence[str] | str | None` — 参数提示，可以是字符串序列、单个字符串或 `None`。

**Returns**:
- `str | None` — 合并后的参数提示字符串或 `None`。

**Raises**:
- 无

*来源: `src/click/exceptions.py:19`*

---
<a id="sym-src_click_exceptions.py-26"></a>
### `_format_possibilities` · func
```python
def _format_possibilities(possibilities: list[str]) -> str
```

格式化可能的选项列表。

**Parameters**:
- `possibilities` — `list[str]` — 可能的选项列表。

**Returns**:
- `str` — 格式化后的字符串，提示用户可能的选项。

**Raises**:
- 无

*来源: `src/click/exceptions.py:26`*

---
<a id="sym-src_click_exceptions.py-35"></a>
### `ClickException` · class
```python
class ClickException(Exception)
```

`ClickException` 是 Click 库中用于表示各种异常的基类。

- **Parameters**:
  - `message` — `str` — 异常的详细描述信息。
- **Returns**:
  - `None`
- **Raises**:
  - 无

### 关键方法

- **format_message(self) -> str**
  - 格式化异常消息，返回格式化后的字符串。
  - **Returns**:
    - `str` — 格式化后的异常消息。

- **__str__(self) -> str**
  - 返回异常的字符串表示。
  - **Returns**:
    - `str` — 异常的字符串表示。

- **show(self, file: t.IO[t.Any] | None = None) -> None**
  - 显示异常信息到指定的文件流中。
  - **Parameters**:
    - `file` — `t.IO[t.Any] | None` — 目标文件流，默认为标准错误流。
  - **Returns**:
    - `None`

*来源: `src/click/exceptions.py:35`*

---
<a id="sym-src_click_exceptions.py-44"></a>
### `ClickException.__init__` · method
```python
def __init__(self, message: str) -> None
```

ClickException 类的构造函数，用于初始化 Click 异常对象。

**Parameters**:
- message — str — 异常的错误信息。

**Returns**:
- None

**Raises**:
- 无

**内部调用(库内):**
- [`resolve_color_default`](src_click.md#sym-src_click_globals.py-54) — 获取颜色标志的默认值。如果传递了一个值，则返回该值；否则，从当前上下文中查找。

*来源: `src/click/exceptions.py:44`*

---
<a id="sym-src_click_exceptions.py-51"></a>
### `ClickException.format_message` · method
```python
def format_message(self) -> str
```

ClickException.format_message

- **Returns**: `str` — 返回异常的错误消息。

*来源: `src/click/exceptions.py:51`*

---
<a id="sym-src_click_exceptions.py-54"></a>
### `ClickException.__str__` · method
```python
def __str__(self) -> str
```

ClickException 类的 `__str__` 方法用于返回异常的字符串表示。

**Parameters**
- 无

**Returns**
- `str` — 异常的字符串表示

**Raises**
- 无

*来源: `src/click/exceptions.py:54`*

---
<a id="sym-src_click_exceptions.py-57"></a>
### `ClickException.show` · method
```python
def show(self, file: t.IO[t.Any] | None = None) -> None
```

### ClickException.show

显示异常信息。

**Parameters**:
- `file` — `t.IO[t.Any] | None` — 输出文件对象，如果为 `None`，则使用标准错误流。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`get_text_stderr`](src_click.md#sym-src_click__compat.py-350) — 获取标准错误输出的文本流。
- [`ClickException.format_message`](src_click.md#sym-src_click_exceptions.py-51) — ClickException.format_message

*来源: `src/click/exceptions.py:57`*

---
<a id="sym-src_click_exceptions.py-68"></a>
### `UsageError` · class
```python
class UsageError(ClickException)
```

`UsageError` 类用于表示用户输入错误，通常在命令行工具中用于提示用户输入不正确。

- **Parameters**:
  - `message` — `str` — 错误信息，描述用户输入错误的具体内容。
  - `ctx` — `Context | None` — 可选参数，表示当前的命令上下文。

- **Returns**:
  - `None`

- **Raises**:
  - 无

*来源: `src/click/exceptions.py:68`*

---
<a id="sym-src_click_exceptions.py-82"></a>
### `UsageError.__init__` · method
```python
def __init__(self, message: str, ctx: Context | None = None) -> None
```

### UsageError.__init__

初始化一个 `UsageError` 异常。

**Parameters**:
- `message` — `str` — 错误消息。
- `ctx` — `Context | None` — 上下文对象，可选。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/exceptions.py:82`*

---
<a id="sym-src_click_exceptions.py-87"></a>
### `UsageError.show` · method
```python
def show(self, file: t.IO[t.Any] | None = None) -> None
```

显示一个 `UsageError` 的错误信息。

**Parameters**:
- `file` — `t.IO[t.Any] | None` — 输出错误信息的文件对象，默认为标准错误流。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`get_text_stderr`](src_click.md#sym-src_click__compat.py-350) — 获取标准错误输出的文本流。
- [`Command.get_help_option`](src_click.md#sym-src_click_core.py-1151) — Returns the help option object.
- [`Command.get_help_option_names`](src_click.md#sym-src_click_core.py-1143) — Returns the names for the help option.
- [`ClickException.format_message`](src_click.md#sym-src_click_exceptions.py-51) — ClickException.format_message

*来源: `src/click/exceptions.py:87`*

---
<a id="sym-src_click_exceptions.py-114"></a>
### `BadParameter` · class
```python
class BadParameter(UsageError)
```

`BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

### 方法

#### `__init__(self, message: str, ctx: Context | None = None, param: Parameter | None = None, param_hint: cabc.Sequence[str] | str | None = None) -> None`

- **Parameters**:
  - `message` — `str` — 错误信息，描述了无效参数的具体问题。
  - `ctx` — `Context | None` — 可选参数，表示当前命令行上下文。
  - `param` — `Parameter | None` — 可选参数，表示无效参数的实例。
  - `param_hint` — `cabc.Sequence[str] | str | None` — 可选参数，表示无效参数的提示信息。

#### `format_message(self) -> str`

- **Returns**:
  - `str` — 格式化后的错误信息，包含上下文、参数和提示信息。

### 示例

```python
from click import BadParameter, Context, Parameter

def my_command(ctx: Context, param: Parameter, value: str) -> None:
    if not value.isdigit():
        raise BadParameter("Value must be a number", ctx, param, "number")

ctx = Context(my_command)
try:
    my_command(ctx, Parameter("value"), "abc")
except BadParameter as e:
    print(e.format_message())
```

输出:
```
Usage error: Value must be a number

*来源: `src/click/exceptions.py:114`*

---
<a id="sym-src_click_exceptions.py-135"></a>
### `BadParameter.__init__` · method
```python
def __init__(
        self,
        message: str,
        ctx: Context | None = None,
        param: Parameter | None = None,
        param_hint: cabc.Sequence[str] | str | None = None,
    ) -> None
```

### `BadParameter.__init__`

初始化 `BadParameter` 异常。

**Parameters:**
- `message` — `str` — 错误消息。
- `ctx` — `Context | None` — 上下文对象，可选。
- `param` — `Parameter | None` — 引发错误的参数对象，可选。
- `param_hint` — `cabc.Sequence[str] | str | None` — 参数提示信息，可选。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/exceptions.py:135`*

---
<a id="sym-src_click_exceptions.py-146"></a>
### `BadParameter.format_message` · method
```python
def format_message(self) -> str
```

### `BadParameter.format_message`

生成一个格式化的错误消息，描述无效的参数值。

**Parameters:**
- `self` — `BadParameter` — 当前的 `BadParameter` 实例。

**Returns:**
- `str` — 格式化的错误消息。

**Raises:**
- 无

**内部调用(库内):**
- [`_join_param_hints`](src_click.md#sym-src_click_exceptions.py-19) — 将参数提示（`param_hint`）合并成一个字符串。

*来源: `src/click/exceptions.py:146`*

---
<a id="sym-src_click_exceptions.py-159"></a>
### `MissingParameter` · class
```python
class MissingParameter(BadParameter)
```

`MissingParameter` 类用于表示在命令行参数解析过程中缺少必要参数的情况。

### 方法

- **__init__(self, message: str | None = None, ctx: Context | None = None, param: Parameter | None = None, param_hint: cabc.Sequence[str] | str | None = None, param_type: str | None = None) -> None**
  - **Parameters**:
    - `message` — `str | None` — 自定义错误消息。
    - `ctx` — `Context | None` — 当前命令行上下文。
    - `param` — `Parameter | None` — 缺失的参数对象。
    - `param_hint` — `cabc.Sequence[str] | str | None` — 参数的提示信息。
    - `param_type` — `str | None` — 参数的类型。
  - **Returns**: `None`
  - **Raises**: `None`

- **format_message(self) -> str**
  - **Parameters**: `None`
  - **Returns**: `str` — 格式化后的错误消息。
  - **Raises**: `None`

- **__str__(self) -> str**
  - **Parameters**: `None`
  - **Returns**: `str` — 错误消息的字符串表示。
  - **Raises**: `None`

*来源: `src/click/exceptions.py:159`*

---
<a id="sym-src_click_exceptions.py-173"></a>
### `MissingParameter.__init__` · method
```python
def __init__(
        self,
        message: str | None = None,
        ctx: Context | None = None,
        param: Parameter | None = None,
        param_hint: cabc.Sequence[str] | str | None = None,
        param_type: str | None = None,
    ) -> None
```

### MissingParameter.__init__

初始化一个 `MissingParameter` 异常。

**Parameters:**
- `message` — `str | None` — 异常消息，如果未提供则为空字符串。
- `ctx` — `Context | None` — 上下文对象，如果未提供则为 `None`。
- `param` — `Parameter | None` — 缺失的参数对象，如果未提供则为 `None`。
- `param_hint` — `cabc.Sequence[str] | str | None` — 参数提示，如果未提供则为 `None`。
- `param_type` — `str | None` — 参数类型，如果未提供则为 `None`。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/exceptions.py:173`*

---
<a id="sym-src_click_exceptions.py-184"></a>
### `MissingParameter.format_message` · method
```python
def format_message(self) -> str
```

### 用途
格式化缺失参数的错误消息。

### Parameters
- `self` — `MissingParameter` — 当前的 `MissingParameter` 实例。

### Returns
- `str` — 格式化后的错误消息。

### Raises
- 无

**内部调用(库内):**
- [`_join_param_hints`](src_click.md#sym-src_click_exceptions.py-19) — 将参数提示（`param_hint`）合并成一个字符串。

*来源: `src/click/exceptions.py:184`*

---
<a id="sym-src_click_exceptions.py-224"></a>
### `MissingParameter.__str__` · method
```python
def __str__(self) -> str
```

###用途
返回一个表示缺少参数的字符串。

###Parameters
- 无

###Returns
- `str` — 表示缺少参数的字符串。

###Raises
- 无

*来源: `src/click/exceptions.py:224`*

---
<a id="sym-src_click_exceptions.py-232"></a>
### `NoSuchOption` · class
```python
class NoSuchOption(UsageError)
```

`NoSuchOption` 类用于表示在命令行解析过程中遇到不存在的选项时抛出的异常。

### 方法

- **__init__(self, option_name: str, message: str | None = None, possibilities: cabc.Iterable[str] | None = None, ctx: Context | None = None) -> None**
  - **Parameters**:
    - `option_name` — `str` — 不存在的选项名称。
    - `message` — `str | None` — 自定义错误消息，可选。
    - `possibilities` — `cabc.Iterable[str] | None` — 可能的正确选项名称列表，可选。
    - `ctx` — `Context | None` — 当前上下文，可选。
  - **Returns**: `None`
  - **Raises**: `None`

- **format_message(self) -> str**
  - **Parameters**: `None`
  - **Returns**: `str` — 格式化后的错误消息。
  - **Raises**: `None`

*来源: `src/click/exceptions.py:232`*

---
<a id="sym-src_click_exceptions.py-241"></a>
### `NoSuchOption.__init__` · method
```python
def __init__(
        self,
        option_name: str,
        message: str | None = None,
        possibilities: cabc.Iterable[str] | None = None,
        ctx: Context | None = None,
    ) -> None
```

### NoSuchOption.__init__

初始化一个表示选项不存在的异常。

**Parameters**:
- `option_name` — `str` — 不存在的选项名称。
- `message` — `str | None` — 自定义错误消息。如果未提供，则使用默认消息。
- `possibilities` — `cabc.Iterable[str] | None` — 可能的正确选项名称列表。
- `ctx` — `Context | None` — 当前上下文。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/exceptions.py:241`*

---
<a id="sym-src_click_exceptions.py-262"></a>
### `NoSuchOption.format_message` · method
```python
def format_message(self) -> str
```

### NoSuchOption.format_message

格式化并返回一个错误消息，如果提供了可能的选项，则包含这些选项。

**Parameters**:
- `self` — `NoSuchOption` — 当前的 `NoSuchOption` 实例。

**Returns**:
- `str` — 格式化后的错误消息，如果提供了可能的选项，则包含这些选项。

**Raises**:
- 无

**内部调用(库内):**
- [`_format_possibilities`](src_click.md#sym-src_click_exceptions.py-26) — 格式化可能的选项列表。

*来源: `src/click/exceptions.py:262`*

---
<a id="sym-src_click_exceptions.py-268"></a>
### `NoSuchCommand` · class
```python
class NoSuchCommand(UsageError)
```

`NoSuchCommand` 类用于表示在命令行中尝试执行一个不存在的命令时抛出的异常。

### 方法

#### `__init__(self, command_name: str, message: str | None = None, possibilities: cabc.Iterable[str] | None = None, ctx: Context | None = None) -> None`

**Parameters:**

- `command_name` — `str` — 尝试执行的命令名称。
- `message` — `str | None` — 可选的自定义错误消息。
- `possibilities` — `cabc.Iterable[str] | None` — 可选的命令名称列表，用于提供可能的替代命令。
- `ctx` — `Context | None` — 可选的命令上下文。

**Returns:**

- `None`

**Raises:**

- `None`

#### `format_message(self) -> str`

**Parameters:**

- `None`

**Returns:**

- `str` — 格式化后的错误消息。

**Raises:**

- `None`

*来源: `src/click/exceptions.py:268`*

---
<a id="sym-src_click_exceptions.py-277"></a>
### `NoSuchCommand.__init__` · method
```python
def __init__(
        self,
        command_name: str,
        message: str | None = None,
        possibilities: cabc.Iterable[str] | None = None,
        ctx: Context | None = None,
    ) -> None
```

### NoSuchCommand.__init__

初始化 `NoSuchCommand` 异常。

**Parameters:**
- `command_name` — `str` — 未找到的命令名称。
- `message` — `str | None` — 自定义错误消息。如果为 `None`，则使用默认消息。
- `possibilities` — `cabc.Iterable[str] | None` — 可能的命令名称列表，用于提供自动完成功能。
- `ctx` — `Context | None` — 当前上下文。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/exceptions.py:277`*

---
<a id="sym-src_click_exceptions.py-298"></a>
### `NoSuchCommand.format_message` · method
```python
def format_message(self) -> str
```

**用途**: 格式化 `NoSuchCommand` 异常的消息，如果存在可能的命令列表，则包含这些命令。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的异常消息。

**Raises**:
- 无

**内部调用(库内):**
- [`_format_possibilities`](src_click.md#sym-src_click_exceptions.py-26) — 格式化可能的选项列表。

*来源: `src/click/exceptions.py:298`*

---
<a id="sym-src_click_exceptions.py-304"></a>
### `BadOptionUsage` · class
```python
class BadOptionUsage(UsageError)
```

`BadOptionUsage` 类用于表示在使用命令行选项时出现错误的情况。

- **Parameters**:
  - `option_name` — `str` — 错误的选项名称。
  - `message` — `str` — 描述错误的详细信息。
  - `ctx` — `Context | None` — 可选的命令上下文对象。

- **Returns**:
  - `None`

- **Raises**:
  - 无

*来源: `src/click/exceptions.py:304`*

---
<a id="sym-src_click_exceptions.py-316"></a>
### `BadOptionUsage.__init__` · method
```python
def __init__(
        self, option_name: str, message: str, ctx: Context | None = None
    ) -> None
```

### BadOptionUsage.__init__

初始化一个 `BadOptionUsage` 异常。

**Parameters**:
- `option_name` — `str` — 无效选项的名称。
- `message` — `str` — 异常的详细消息。
- `ctx` — `Context | None` — 与异常相关的上下文，可选。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/exceptions.py:316`*

---
<a id="sym-src_click_exceptions.py-323"></a>
### `BadArgumentUsage` · class
```python
class BadArgumentUsage(UsageError)
```

`BadArgumentUsage` 类继承自 `UsageError`，用于表示在命令行参数使用中出现了错误。

- **Parameters**:
  - 无参数。

- **Returns**:
  - 无返回值。

- **Raises**:
  - 无异常抛出。

*来源: `src/click/exceptions.py:323`*

---
<a id="sym-src_click_exceptions.py-332"></a>
### `NoArgsIsHelpError` · class
```python
class NoArgsIsHelpError(UsageError)
```

`NoArgsIsHelpError` 类继承自 `UsageError`，用于在命令行没有提供参数时显示帮助信息。

- **Parameters**:
  - `ctx` — `Context` — 命令上下文对象。
- **Returns**:
  - `None`
- **Raises**:
  - 无

*来源: `src/click/exceptions.py:332`*

---
<a id="sym-src_click_exceptions.py-335"></a>
### `NoArgsIsHelpError.__init__` · method
```python
def __init__(self, ctx: Context) -> None
```

当命令没有参数时，显示帮助信息。

**Parameters**:
- `ctx` — `Context` — 命令上下文。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/exceptions.py:335`*

---
<a id="sym-src_click_exceptions.py-338"></a>
### `NoArgsIsHelpError.show` · method
```python
def show(self, file: t.IO[t.Any] | None = None) -> None
```

显示错误信息。

**Parameters**:
- file (t.IO[t.Any] | None) — 输出流，如果为 `None`，则使用标准错误流。

**Returns**:
- None

**Raises**:
- None

**内部调用(库内):**
- [`ClickException.format_message`](src_click.md#sym-src_click_exceptions.py-51) — ClickException.format_message

*来源: `src/click/exceptions.py:338`*

---
<a id="sym-src_click_exceptions.py-342"></a>
### `FileError` · class
```python
class FileError(ClickException)
```

`FileError` 类继承自 `ClickException`，用于表示与文件操作相关的错误。

### 方法

- **__init__(self, filename: str, hint: str | None = None) -> None**
  - **Parameters**:
    - `filename` — `str` — 文件名，表示发生错误的文件。
    - `hint` — `str | None` — 可选参数，提供错误的提示信息。
  - **Returns**:
    - `None`
  - **Raises**:
    - 无

- **format_message(self) -> str**
  - **Parameters**:
    - 无
  - **Returns**:
    - `str` — 格式化后的错误信息字符串。
  - **Raises**:
    - 无

*来源: `src/click/exceptions.py:342`*

---
<a id="sym-src_click_exceptions.py-348"></a>
### `FileError.__init__` · method
```python
def __init__(self, filename: str, hint: str | None = None) -> None
```

### FileError.__init__

初始化一个 `FileError` 对象。

**Parameters:**
- `filename` — `str` — 文件名。
- `hint` — `str | None` — 错误提示，默认为 "unknown error"。

**Returns:**
- `None`

**Raises:**
- 无

**内部调用(库内):**
- [`format_filename`](src_click.md#sym-src_click_utils.py-425) — Format a filename for display, ensuring it can be displayed by replacing any inv

*来源: `src/click/exceptions.py:348`*

---
<a id="sym-src_click_exceptions.py-356"></a>
### `FileError.format_message` · method
```python
def format_message(self) -> str
```

**用途**: 格式化文件错误消息。

**Parameters**:
- 无

**Returns**:
- `str`: 格式化后的错误消息。

**Raises**:
- 无

*来源: `src/click/exceptions.py:356`*

---
<a id="sym-src_click_exceptions.py-362"></a>
### `Abort` · class
```python
class Abort(RuntimeError)
```

`Abort` 类继承自 `RuntimeError`，用于表示命令执行过程中发生了中止操作。

- **Parameters**:
  - 无

- **Returns**:
  - 无

- **Raises**:
  - `Abort`: 当需要中止命令执行时抛出此异常。

*来源: `src/click/exceptions.py:362`*

---
<a id="sym-src_click_exceptions.py-366"></a>
### `Exit` · class
```python
class Exit(RuntimeError)
```

`Exit` 类用于表示程序应该退出，并提供一个退出代码。

- **Parameters**:
  - `code` — `int` — 退出代码，默认为 0。

- **Returns**:
  - `None`

- **Raises**:
  - `None`

*来源: `src/click/exceptions.py:366`*

---
<a id="sym-src_click_exceptions.py-377"></a>
### `Exit.__init__` · method
```python
def __init__(self, code: int = 0) -> None
```

用途: 初始化一个 Exit 对象，设置退出代码。

**Parameters**:
- `code` — `int` — 退出代码，默认为 0。

**Returns**:
- `None`

*来源: `src/click/exceptions.py:377`*

---

## `src/click/formatting.py`

<a id="sym-src_click_formatting.py-14"></a>
### `measure_table` · func
```python
def measure_table(rows: cabc.Iterable[tuple[str, str]]) -> tuple[int, ...]
```

### measure_table

计算表格中每一列的最大宽度。

**Parameters**:
- `rows` — `cabc.Iterable[tuple[str, str]]` — 表格的行，每行是一个包含两个字符串的元组。

**Returns**:
- `tuple[int, ...]` — 每一列的最大宽度。

**Raises**:
- 无

**内部调用(库内):**
- [`term_len`](src_click.md#sym-src_click__compat.py-532) — 计算去除 ANSI 转义码后的字符串长度。

*来源: `src/click/formatting.py:14`*

---
<a id="sym-src_click_formatting.py-24"></a>
### `iter_rows` · func
```python
def iter_rows(
    rows: cabc.Iterable[tuple[str, str]], col_count: int
) -> cabc.Iterator[tuple[str, ...]]
```

### iter_rows

Iterates over a list of rows, padding each row with empty strings to match the specified column count.

**Parameters**:
- `rows` — `cabc.Iterable[tuple[str, str]]` — An iterable of tuples, each representing a row with two strings.
- `col_count` — `int` — The total number of columns each row should have.

**Returns**:
- `cabc.Iterator[tuple[str, ...]]` — An iterator yielding each row as a tuple, padded with empty strings if necessary.

**Raises**:
- (无)

*来源: `src/click/formatting.py:24`*

---
<a id="sym-src_click_formatting.py-31"></a>
### `wrap_text` · func
```python
def wrap_text(
    text: str,
    width: int = 78,
    initial_indent: str = "",
    subsequent_indent: str = "",
    preserve_paragraphs: bool = False,
) -> str
```

**用途**: A helper function that intelligently wraps text, handling paragraphs and preserving formatting.

**Parameters**:
- `text` — `str` — The text that should be rewrapped.
- `width` — `int` — The maximum width for the text. Default is 78.
- `initial_indent` — `str` — The initial indent that should be placed on the first line as a string. Default is an empty string.
- `subsequent_indent` — `str` — The indent string that should be placed on each consecutive line. Default is an empty string.
- `preserve_paragraphs` — `bool` — If this flag is set, then the wrapping will intelligently handle paragraphs. Default is `False`.

**Returns**:
- `str` — The rewrapped text.

**Raises**:
- None

**内部调用(库内):**
- [`TextWrapper`](src_click.md#sym-src_click__textwrap.py-38) — `TextWrapper` 类用于处理文本的换行和格式化，确保文本在指定宽度内正确显示。
- [`_flush_par`](src_click.md#sym-src_click_formatting.py-78) — 将缓冲区中的内容刷新到输出列表中。
- [`term_len`](src_click.md#sym-src_click__compat.py-532) — 计算去除 ANSI 转义码后的字符串长度。
- [`TextWrapper.extra_indent`](src_click.md#sym-src_click__textwrap.py-165) — 增加文本包装器的缩进。
- [`TextWrapper.indent_only`](src_click.md#sym-src_click__textwrap.py-177) — 对文本进行缩进处理。

*来源: `src/click/formatting.py:31`*

---
<a id="sym-src_click_formatting.py-78"></a>
### `_flush_par` · func
```python
def _flush_par() -> None
```

将缓冲区中的内容刷新到输出列表中。

**Parameters**:
- `buf` — `List[str]` — 缓冲区，包含要刷新的内容。
- `p` — `List[Tuple[int, bool, str]]` — 输出列表，用于存储格式化后的文本。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/formatting.py:78`*

---
<a id="sym-src_click_formatting.py-110"></a>
### `HelpFormatter` · class
```python
class HelpFormatter
```

`HelpFormatter` 类用于格式化命令行工具的帮助信息。

- **__init__(self, indent_increment: int = 2, width: int | None = None, max_width: int | None = None) -> None**
  - **Parameters**:
    - `indent_increment` — `int` — 每次缩进的增量，默认为2。
    - `width` — `int | None` — 输出的总宽度，默认为None。
    - `max_width` — `int | None` — 最大宽度，默认为None。
  - **Returns**: `None`
  - **Raises**: `None`

- **write(self, string: str) -> None**
  - **Parameters**:
    - `string` — `str` — 要写入的字符串。
  - **Returns**: `None`
  - **Raises**: `None`

- **indent(self) -> None**
  - **Parameters**: `None`
  - **Returns**: `None`
  - **Raises**: `None`

- **dedent(self) -> None**
  - **Parameters**: `None`
  - **Returns**: `None`
  - **Raises**: `None`

- **write_usage(self, prog: str, args: str = "", prefix: str | None = None) -> None**
  - **Parameters**:
    - `prog` — `str` — 程序名称。
    - `args` — `str` — 命令行参数，默认为空字符串。

*来源: `src/click/formatting.py:110`*

---
<a id="sym-src_click_formatting.py-127"></a>
### `HelpFormatter.__init__` · method
```python
def __init__(
        self,
        indent_increment: int = 2,
        width: int | None = None,
        max_width: int | None = None,
    ) -> None
```

### HelpFormatter.__init__

初始化 `HelpFormatter` 对象，用于格式化帮助信息。

**Parameters:**
- `indent_increment` — `int` — 每级缩进的增量，默认为 2。
- `width` — `int | None` — 输出的宽度，默认为终端宽度或 80。
- `max_width` — `int | None` — 最大宽度，默认为 80。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/formatting.py:127`*

---
<a id="sym-src_click_formatting.py-146"></a>
### `HelpFormatter.write` · method
```python
def write(self, string: str) -> None
```

### HelpFormatter.write

Writes a unicode string into the internal buffer.

**Parameters**:
- `string` — `str` — The unicode string to be written.

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/formatting.py:146`*

---
<a id="sym-src_click_formatting.py-150"></a>
### `HelpFormatter.indent` · method
```python
def indent(self) -> None
```

增加当前缩进。

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/formatting.py:150`*

---
<a id="sym-src_click_formatting.py-154"></a>
### `HelpFormatter.dedent` · method
```python
def dedent(self) -> None
```

Decreases the indentation.

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/formatting.py:154`*

---
<a id="sym-src_click_formatting.py-158"></a>
### `HelpFormatter.write_usage` · method
```python
def write_usage(self, prog: str, args: str = "", prefix: str | None = None) -> None
```

### HelpFormatter.write_usage

Writes a usage line into the buffer.

**Parameters:**

- `prog` — `str` — The program name.
- `args` — `str` — Whitespace separated list of arguments. Defaults to an empty string.
- `prefix` — `str | None` — The prefix for the first line. Defaults to `"Usage: "`.

**Returns:**

- `None`

**Raises:**

- None

**内部调用(库内):**
- [`term_len`](src_click.md#sym-src_click__compat.py-532) — 计算去除 ANSI 转义码后的字符串长度。
- [`wrap_text`](src_click.md#sym-src_click_formatting.py-31) — **用途**: A helper function that intelligently wraps text, handling paragraphs and

*来源: `src/click/formatting.py:158`*

---
<a id="sym-src_click_formatting.py-204"></a>
### `HelpFormatter.write_heading` · method
```python
def write_heading(self, heading: str) -> None
```

Writes a heading into the buffer.

**Parameters**:
- `heading` — `str` — The heading text to write.

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/formatting.py:204`*

---
<a id="sym-src_click_formatting.py-208"></a>
### `HelpFormatter.write_paragraph` · method
```python
def write_paragraph(self) -> None
```

Writes a paragraph into the buffer.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `src/click/formatting.py:208`*

---
<a id="sym-src_click_formatting.py-213"></a>
### `HelpFormatter.write_text` · method
```python
def write_text(self, text: str) -> None
```

Writes re-indented text into the buffer. This rewraps and preserves paragraphs.

**Parameters**:
- `text` — `str` — The text to write.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`wrap_text`](src_click.md#sym-src_click_formatting.py-31) — **用途**: A helper function that intelligently wraps text, handling paragraphs and

*来源: `src/click/formatting.py:213`*

---
<a id="sym-src_click_formatting.py-229"></a>
### `HelpFormatter.write_dl` · method
```python
def write_dl(
        self,
        rows: cabc.Iterable[tuple[str, str]],
        col_max: int = 30,
        col_spacing: int = 2,
    ) -> None
```

Writes a definition list into the buffer. This is how options and commands are usually formatted.

- **Parameters**:
  - `rows` — `cabc.Iterable[tuple[str, str]]` — A list of two-item tuples for the terms and values.
  - `col_max` — `int` — The maximum width of the first column. Default is 30.
  - `col_spacing` — `int` — The number of spaces between the first and second column. Default is 2.

- **Returns**:
  - `None`

- **Raises**:
  - `TypeError` — If the expected two columns for the definition list are not provided.

**内部调用(库内):**
- [`measure_table`](src_click.md#sym-src_click_formatting.py-14) — measure_table
- [`iter_rows`](src_click.md#sym-src_click_formatting.py-24) — iter_rows
- [`term_len`](src_click.md#sym-src_click__compat.py-532) — 计算去除 ANSI 转义码后的字符串长度。
- [`wrap_text`](src_click.md#sym-src_click_formatting.py-31) — **用途**: A helper function that intelligently wraps text, handling paragraphs and

*来源: `src/click/formatting.py:229`*

---
<a id="sym-src_click_formatting.py-274"></a>
### `HelpFormatter.section` · method
装饰器: `@contextmanager`
```python
def section(self, name: str) -> cabc.Generator[None]
```

Helpful context manager that writes a paragraph, a heading, and the indents.

**Parameters**:
- `name` — `str` — the section name that is written as heading.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`HelpFormatter.write_paragraph`](src_click.md#sym-src_click_formatting.py-208) — Writes a paragraph into the buffer.
- [`HelpFormatter.write_heading`](src_click.md#sym-src_click_formatting.py-204) — Writes a heading into the buffer.
- [`HelpFormatter.indent`](src_click.md#sym-src_click_formatting.py-150) — 增加当前缩进。
- [`HelpFormatter.dedent`](src_click.md#sym-src_click_formatting.py-154) — Decreases the indentation.

*来源: `src/click/formatting.py:274`*

---
<a id="sym-src_click_formatting.py-289"></a>
### `HelpFormatter.indentation` · method
装饰器: `@contextmanager`
```python
def indentation(self) -> cabc.Generator[None]
```

增加缩进的上下文管理器。

**Parameters**:
- 无

**Returns**:
- `Generator[None]`: 一个生成器，用于在缩进的上下文中执行代码。

**Raises**:
- 无

**内部调用(库内):**
- [`HelpFormatter.indent`](src_click.md#sym-src_click_formatting.py-150) — 增加当前缩进。
- [`HelpFormatter.dedent`](src_click.md#sym-src_click_formatting.py-154) — Decreases the indentation.

*来源: `src/click/formatting.py:289`*

---
<a id="sym-src_click_formatting.py-297"></a>
### `HelpFormatter.getvalue` · method
```python
def getvalue(self) -> str
```

Returns the contents of the buffer as a string.

**Parameters**:
- 无

**Returns**:
- `str`: 缓冲区的内容。

**Raises**:
- 无

*来源: `src/click/formatting.py:297`*

---
<a id="sym-src_click_formatting.py-302"></a>
### `join_options` · func
```python
def join_options(options: cabc.Iterable[str]) -> tuple[str, bool]
```

Given a list of option strings, this function joins them in the most appropriate way and returns them in the form `(formatted_string, any_prefix_is_slash)` where the second item in the tuple is a flag that indicates if any of the option prefixes was a slash.

**Parameters**:
- `options` — `cabc.Iterable[str]` — A list of option strings.

**Returns**:
- `tuple[str, bool]` — A tuple containing the formatted string of joined options and a boolean flag indicating if any of the option prefixes was a slash.

**Raises**:
- None

**内部调用(库内):**
- [`_split_opt`](src_click.md#sym-src_click_parser.py-111) — _split_opt

*来源: `src/click/formatting.py:302`*

---

## `src/click/globals.py`

<a id="sym-src_click_globals.py-13"></a>
### `get_current_context` · func
装饰器: `@t.overload`
```python
def get_current_context(silent: t.Literal[False] = False) -> Context
```

获取当前的 Click 上下文。

**Parameters**:
- `silent` — `t.Literal[False]` — 如果为 `False`，则在没有上下文时抛出异常。

**Returns**:
- `Context` — 当前的 Click 上下文。

**Raises**:
- `RuntimeError` — 如果没有上下文且 `silent` 为 `False`。

*来源: `src/click/globals.py:13`*

---
<a id="sym-src_click_globals.py-17"></a>
### `get_current_context` · func
装饰器: `@t.overload`
```python
def get_current_context(silent: bool = ...) -> Context | None
```

获取当前的 Click 上下文。

**Parameters**:
- silent — bool — 如果为 `True`，则在没有上下文时返回 `None`，否则抛出异常。

**Returns**:
- Context | None — 当前的 Click 上下文，如果存在。

**Raises**:
- None

*来源: `src/click/globals.py:17`*

---
<a id="sym-src_click_globals.py-20"></a>
### `get_current_context` · func
```python
def get_current_context(silent: bool = False) -> Context | None
```

Returns the current click context. This can be used as a way to access the current context object from anywhere. This is a more implicit alternative to the :func:`pass_context` decorator. This function is primarily useful for helpers such as :func:`echo` which might be interested in changing its behavior based on the current context.

**Parameters**:

- `silent` — `bool` — If set to `True` the return value is `None` if no context is available. The default behavior is to raise a :exc:`RuntimeError`.

**Returns**:

- `Context | None` — The current click context or `None` if no context is available and `silent` is `True`.

**Raises**:

- `RuntimeError` — If no context is available and `silent` is `False`.

*来源: `src/click/globals.py:20`*

---
<a id="sym-src_click_globals.py-44"></a>
### `push_context` · func
```python
def push_context(ctx: Context) -> None
```

Pushes a new context to the current stack.

**Parameters**:
- `ctx` — `Context` — The context to push onto the stack.

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/globals.py:44`*

---
<a id="sym-src_click_globals.py-49"></a>
### `pop_context` · func
```python
def pop_context() -> None
```

**用途**: Removes the top level from the stack.

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/globals.py:49`*

---
<a id="sym-src_click_globals.py-54"></a>
### `resolve_color_default` · func
```python
def resolve_color_default(color: bool | None = None) -> bool | None
```

获取颜色标志的默认值。如果传递了一个值，则返回该值；否则，从当前上下文中查找。

**Parameters:**
- `color` (bool | None) — 颜色标志的值，如果传递则返回该值，否则从上下文中查找。

**Returns:**
- (bool | None) — 颜色标志的默认值。

**Raises:**
- 无

**内部调用(库内):**
- [`get_current_context`](src_click.md#sym-src_click_globals.py-13) — 获取当前的 Click 上下文。

*来源: `src/click/globals.py:54`*

---

## `src/click/parser.py`

<a id="sym-src_click_parser.py-51"></a>
### `_unpack_args` · func
```python
def _unpack_args(
    args: cabc.Sequence[str], nargs_spec: cabc.Sequence[int]
) -> tuple[cabc.Sequence[str | cabc.Sequence[str | T_UNSET] | T_UNSET], list[str]]
```

Given an iterable of arguments and an iterable of nargs specifications, it returns a tuple with all the unpacked arguments at the first index and all remaining arguments as the second.

**Parameters**:
- `args` — `cabc.Sequence[str]` — An iterable of arguments to be unpacked.
- `nargs_spec` — `cabc.Sequence[int]` — An iterable of nargs specifications indicating how many arguments each position should consume.

**Returns**:
- `tuple[cabc.Sequence[str | cabc.Sequence[str | T_UNSET] | T_UNSET], list[str]]` — A tuple containing the unpacked arguments and any remaining arguments.

**Raises**:
- None

**内部调用(库内):**
- [`_fetch`](src_click.md#sym-src_click_parser.py-68) — 从双端队列中获取元素，如果队列为空则返回 `UNSET`。

*来源: `src/click/parser.py:51`*

---
<a id="sym-src_click_parser.py-68"></a>
### `_fetch` · func
```python
def _fetch(c: deque[str]) -> str | T_UNSET
```

从双端队列中获取元素，如果队列为空则返回 `UNSET`。

**Parameters**:
- `c` — `deque[str]` — 双端队列，从中获取元素。

**Returns**:
- `str | T_UNSET` — 如果队列不为空，返回队列的第一个或最后一个元素；如果队列为空，返回 `UNSET`。

**Raises**:
- `IndexError` — 如果尝试从空队列中获取元素。

*来源: `src/click/parser.py:68`*

---
<a id="sym-src_click_parser.py-111"></a>
### `_split_opt` · func
```python
def _split_opt(opt: str) -> tuple[str, str]
```

### _split_opt

Splits an option string into a prefix and the rest.

- **Parameters**:
  - `opt` — `str` — The option string to split.

- **Returns**:
  - `tuple[str, str]` — A tuple containing the prefix and the rest of the option string.

- **Raises**:
  - None

*来源: `src/click/parser.py:111`*

---
<a id="sym-src_click_parser.py-120"></a>
### `_normalize_opt` · func
```python
def _normalize_opt(opt: str, ctx: Context | None) -> str
```

**用途**: Normalize an option string using the token normalization function from the provided context.

**Parameters**:
- `opt` — `str` — The option string to normalize.
- `ctx` — `Context | None` — The context containing the token normalization function.

**Returns**:
- `str` — The normalized option string.

**Raises**:
- None

**内部调用(库内):**
- [`_split_opt`](src_click.md#sym-src_click_parser.py-111) — _split_opt

*来源: `src/click/parser.py:120`*

---
<a id="sym-src_click_parser.py-127"></a>
### `_Option` · class
```python
class _Option
```

`_Option` 类用于处理命令行选项，解析用户输入并将其转换为程序可使用的参数。

### 方法

- **`__init__(self, obj: CoreOption, opts: cabc.Sequence[str], dest: str | None, action: str | None = None, nargs: int = 1, const: t.Any | None = None)`**
  - **Parameters**:
    - `obj` — `CoreOption` — 原始的命令行选项对象。
    - `opts` — `cabc.Sequence[str]` — 选项的短名称和长名称列表。
    - `dest` — `str | None` — 选项值在解析后存储的目标属性名。
    - `action` — `str | None` — 选项的处理方式，如 'store', 'store_true', 'store_false' 等。
    - `nargs` — `int` — 选项期望的参数数量。
    - `const` — `t.Any | None` — 选项值为常量时的值。
  - **Returns**: `None`
  - **Raises**: `None`

- **`takes_value(self) -> bool`**
  - **Parameters**: `None`
  - **Returns**: `bool` — 如果选项需要值则返回 `True`，否则返回 `False`。
  - **Raises**: `None`

- **`process(self, value: t.Any, state: _ParsingState) -> None`**
  - **Parameters**

*来源: `src/click/parser.py:127`*

---
<a id="sym-src_click_parser.py-128"></a>
### `_Option.__init__` · method
```python
def __init__(
        self,
        obj: CoreOption,
        opts: cabc.Sequence[str],
        dest: str | None,
        action: str | None = None,
        nargs: int = 1,
        const: t.Any | None = None,
    )
```

**用途**: 初始化一个 `_Option` 对象，解析选项字符串并设置相关属性。

**Parameters**:
- `obj` — `CoreOption` — 选项对象。
- `opts` — `Sequence[str]` — 选项字符串列表。
- `dest` — `str | None` — 目标属性名。
- `action` — `str | None` — 动作类型，默认为 "store"。
- `nargs` — `int` — 参数数量，默认为 1。
- `const` — `Any | None` — 常量值。

**Returns**:
- 无返回值。

**Raises**:
- `ValueError` — 如果选项字符串的起始字符无效。

**内部调用(库内):**
- [`_split_opt`](src_click.md#sym-src_click_parser.py-111) — _split_opt

*来源: `src/click/parser.py:128`*

---
<a id="sym-src_click_parser.py-166"></a>
### `_Option.takes_value` · method
装饰器: `@property`
```python
def takes_value(self) -> bool
```

### _Option.takes_value

Determines if the option takes a value.

**Parameters**:
- `self` — `_Option` — The option instance.

**Returns**:
- `bool` — `True` if the option takes a value, otherwise `False`.

**Raises**:
- (无)

*来源: `src/click/parser.py:166`*

---
<a id="sym-src_click_parser.py-169"></a>
### `_Option.process` · method
```python
def process(self, value: t.Any, state: _ParsingState) -> None
```

处理命令行选项的值并更新解析状态。

**Parameters**:
- `value` — `t.Any` — 选项的值。
- `state` — `_ParsingState` — 解析状态对象。

**Returns**:
- `None`

**Raises**:
- `ValueError` — 如果 `action` 不是已知的值。

*来源: `src/click/parser.py:169`*

---
<a id="sym-src_click_parser.py-185"></a>
### `_Argument` · class
```python
class _Argument
```

`_Argument` 类用于处理命令行参数，解析并存储参数值。

### 方法

#### `__init__(self, obj: CoreArgument, dest: str | None, nargs: int = 1)`

初始化 `_Argument` 对象。

- **Parameters**:
  - `obj` — `CoreArgument` — 命令行参数对象。
  - `dest` — `str | None` — 参数的存储目标，可选。
  - `nargs` — `int` — 需要的参数数量，默认为 1。

#### `process(self, value: str | cabc.Sequence[str | T_UNSET] | T_UNSET, state: _ParsingState) -> None`

处理传入的参数值。

- **Parameters**:
  - `value` — `str | cabc.Sequence[str | T_UNSET] | T_UNSET` — 传入的参数值。
  - `state` — `_ParsingState` — 解析状态对象。

- **Returns**:
  - `None`

*来源: `src/click/parser.py:185`*

---
<a id="sym-src_click_parser.py-186"></a>
### `_Argument.__init__` · method
```python
def __init__(self, obj: CoreArgument, dest: str | None, nargs: int = 1)
```

初始化一个 `_Argument` 对象。

**Parameters**:
- `obj` — `CoreArgument` — 基础参数对象。
- `dest` — `str | None` — 目标参数名。
- `nargs` — `int` — 参数数量，默认为1。

**Returns**:
- 无返回值。

*来源: `src/click/parser.py:186`*

---
<a id="sym-src_click_parser.py-191"></a>
### `_Argument.process` · method
```python
def process(
        self,
        value: str | cabc.Sequence[str | T_UNSET] | T_UNSET,
        state: _ParsingState,
    ) -> None
```

处理命令行参数。

**Parameters**:
- `value` — `str | cabc.Sequence[str | T_UNSET] | T_UNSET` — 命令行参数值。
- `state` — `_ParsingState` — 解析状态。

**Returns**:
- `None`

**Raises**:
- `BadArgumentUsage` — 当参数值不符合预期时抛出。

**内部调用(库内):**
- [`BadArgumentUsage`](src_click.md#sym-src_click_exceptions.py-323) — `BadArgumentUsage` 类继承自 `UsageError`，用于表示在命令行参数使用中出现了错误。

*来源: `src/click/parser.py:191`*

---
<a id="sym-src_click_parser.py-216"></a>
### `_ParsingState` · class
```python
class _ParsingState
```

`_ParsingState` 类用于管理命令行参数的解析状态。

- **Parameters**:
  - `rargs` — `list[str]` — 命令行参数列表。

- **Returns**:
  - `None`

- **Raises**:
  - 无

*来源: `src/click/parser.py:216`*

---
<a id="sym-src_click_parser.py-217"></a>
### `_ParsingState.__init__` · method
```python
def __init__(self, rargs: list[str]) -> None
```

初始化解析状态。

**Parameters**:
- `rargs` — `list[str]` — 剩余的命令行参数列表。

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/parser.py:217`*

---
<a id="sym-src_click_parser.py-224"></a>
### `_OptionParser` · class
```python
class _OptionParser
```

`_OptionParser` 类用于解析命令行选项和参数，并将其转换为 Click 命令的上下文。

### 方法

- **`__init__(self, ctx: Context | None = None) -> None`**
  - **Parameters**:
    - `ctx` — `Context | None` — The Click context for this parser. Can be `None` for advanced use cases.
  - **Returns**:
    - `None`

- **`add_option(self, obj: CoreOption, opts: cabc.Sequence[str], dest: str | None, action: str | None = None, nargs: int = 1, const: t.Any | None = None) -> None`**
  - **Parameters**:
    - `obj` — `CoreOption` — The option object to add.
    - `opts` — `cabc.Sequence[str]` — The option names (e.g., `['-v', '--verbose']`).
    - `dest` — `str | None` — The destination attribute name for the parsed value.
    - `action` — `str | None` — The action to take when the option is encountered.
    - `nargs` — `int` — The number of arguments expected for the option.
    - `const` — `t.Any | None` — A constant value to use when the option is present.
  - **Returns**:
    - `None`

- **`add_argument(self, obj: CoreArgument, dest: str | None, nargs:

*来源: `src/click/parser.py:224`*

---
<a id="sym-src_click_parser.py-241"></a>
### `_OptionParser.__init__` · method
```python
def __init__(self, ctx: Context | None = None) -> None:
        #: The :class:`~click.Context` for this parser.  This might be
        #: `None` for some advanced use cases.
```

### `_OptionParser.__init__`

初始化一个 `_OptionParser` 对象，用于解析命令行选项。

**Parameters**:
- `ctx` — `Context | None` — 与该解析器关联的 `Context` 对象。在某些高级用例中可能为 `None`。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/parser.py:241`*

---
<a id="sym-src_click_parser.py-265"></a>
### `_OptionParser.add_option` · method
```python
def add_option(
        self,
        obj: CoreOption,
        opts: cabc.Sequence[str],
        dest: str | None,
        action: str | None = None,
        nargs: int = 1,
        const: t.Any | None = None,
    ) -> None
```

Adds a new option to the parser.

**Parameters**:
- `obj` — `CoreOption` — The option object used to identify the option in the order list.
- `opts` — `Sequence[str]` — The option strings, which can include both short and long options.
- `dest` — `str | None` — The destination name for the option value.
- `action` — `str | None` — The action to take when the option is encountered, such as 'store', 'store_const', etc. Defaults to 'store'.
- `nargs` — `int` — The number of arguments expected for the option. Defaults to 1.
- `const` — `Any | None` — The constant value to use with 'store_const' and 'append_const' actions.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`_normalize_opt`](src_click.md#sym-src_click_parser.py-120) — **用途**: Normalize an option string using the token normalization function from t
- [`_Option`](src_click.md#sym-src_click_parser.py-127) — `_Option` 类用于处理命令行选项，解析用户输入并将其转换为程序可使用的参数。

*来源: `src/click/parser.py:265`*

---
<a id="sym-src_click_parser.py-290"></a>
### `_OptionParser.add_argument` · method
```python
def add_argument(self, obj: CoreArgument, dest: str | None, nargs: int = 1) -> None
```

Adds a positional argument named `dest` to the parser.

**Parameters**:
- `obj` — `CoreArgument` — The object used to identify the option in the order list that is returned from the parser.
- `dest` — `str | None` — The name of the argument.
- `nargs` — `int` — The number of arguments that the option should consume. Default is 1.

**Returns**:
- `None`

**内部调用(库内):**
- [`_Argument`](src_click.md#sym-src_click_parser.py-185) — `_Argument` 类用于处理命令行参数，解析并存储参数值。

*来源: `src/click/parser.py:290`*

---
<a id="sym-src_click_parser.py-298"></a>
### `_OptionParser.parse_args` · method
```python
def parse_args(
        self, args: list[str]
    ) -> tuple[dict[str, t.Any], list[str], list[CoreParameter]]
```

Parses positional arguments and returns a tuple containing parsed options, leftover arguments, and the order of arguments as they appear on the command line.

**Parameters**:
- `args` — `list[str]` — The list of arguments to parse.

**Returns**:
- `tuple[dict[str, t.Any], list[str], list[CoreParameter]]` — A tuple containing the parsed options, leftover arguments, and the order of arguments.

**Raises**:
- `UsageError` — If there is an error in parsing the arguments and resilient parsing is not enabled.

**内部调用(库内):**
- [`_ParsingState`](src_click.md#sym-src_click_parser.py-216) — `_ParsingState` 类用于管理命令行参数的解析状态。
- [`_OptionParser._process_args_for_options`](src_click.md#sym-src_click_parser.py-327) — _OptionParser._process_args_for_options
- [`_OptionParser._process_args_for_args`](src_click.md#sym-src_click_parser.py-316) — `_OptionParser._process_args_for_args`

*来源: `src/click/parser.py:298`*

---
<a id="sym-src_click_parser.py-316"></a>
### `_OptionParser._process_args_for_args` · method
```python
def _process_args_for_args(self, state: _ParsingState) -> None
```

### `_OptionParser._process_args_for_args`

处理命令行参数，将参数值传递给相应的参数对象进行处理。

**Parameters:**
- `state` — `_ParsingState` — 解析状态对象，包含当前解析的参数。

**Returns:**
- `None`

**Raises:**
- 无

**内部调用(库内):**
- [`_unpack_args`](src_click.md#sym-src_click_parser.py-51) — Given an iterable of arguments and an iterable of nargs specifications, it retur
- [`_Option.process`](src_click.md#sym-src_click_parser.py-169) — 处理命令行选项的值并更新解析状态。

*来源: `src/click/parser.py:316`*

---
<a id="sym-src_click_parser.py-327"></a>
### `_OptionParser._process_args_for_options` · method
```python
def _process_args_for_options(self, state: _ParsingState) -> None
```

### _OptionParser._process_args_for_options

处理命令行参数中的选项。

**Parameters:**
- `state` — `_ParsingState` — 解析状态对象。

**Returns:**
- `None`

**Raises:**
- 无

**内部调用(库内):**
- [`_OptionParser._process_opts`](src_click.md#sym-src_click_parser.py-470) — _OptionParser._process_opts

*来源: `src/click/parser.py:327`*

---
<a id="sym-src_click_parser.py-363"></a>
### `_OptionParser._match_long_opt` · method
```python
def _match_long_opt(
        self, opt: str, explicit_value: str | None, state: _ParsingState
    ) -> None
```

### 用途
解析长选项并处理其值。

### Parameters
- `opt` — `str` — 长选项字符串。
- `explicit_value` — `str | None` — 隐式值或 `None`。
- `state` — `_ParsingState` — 解析状态对象。

### Returns
- `None`

### Raises
- `NoSuchOption` — 如果选项不存在。
- `BadOptionUsage` — 如果选项不接受值但提供了值。

**内部调用(库内):**
- [`NoSuchOption`](src_click.md#sym-src_click_exceptions.py-232) — `NoSuchOption` 类用于表示在命令行解析过程中遇到不存在的选项时抛出的异常。
- [`_OptionParser._get_value_from_state`](src_click.md#sym-src_click_parser.py-430) — `_OptionParser._get_value_from_state`
- [`BadOptionUsage`](src_click.md#sym-src_click_exceptions.py-304) — `BadOptionUsage` 类用于表示在使用命令行选项时出现错误的情况。
- [`_Option.process`](src_click.md#sym-src_click_parser.py-169) — 处理命令行选项的值并更新解析状态。

*来源: `src/click/parser.py:363`*

---
<a id="sym-src_click_parser.py-390"></a>
### `_OptionParser._match_short_opt` · method
```python
def _match_short_opt(self, arg: str, state: _ParsingState) -> None
```

### _OptionParser._match_short_opt

解析短选项并处理其值。

**Parameters**:
- `arg` — `str` — 当前处理的命令行参数。
- `state` — `_ParsingState` — 解析状态对象。

**Returns**:
- `None`

**Raises**:
- `NoSuchOption` — 当遇到未知选项时抛出。
- `BadOptionUsage` — 当选项使用方式不正确时抛出。

**内部调用(库内):**
- [`_normalize_opt`](src_click.md#sym-src_click_parser.py-120) — **用途**: Normalize an option string using the token normalization function from t
- [`NoSuchOption`](src_click.md#sym-src_click_exceptions.py-232) — `NoSuchOption` 类用于表示在命令行解析过程中遇到不存在的选项时抛出的异常。
- [`_OptionParser._get_value_from_state`](src_click.md#sym-src_click_parser.py-430) — `_OptionParser._get_value_from_state`
- [`_Option.process`](src_click.md#sym-src_click_parser.py-169) — 处理命令行选项的值并更新解析状态。

*来源: `src/click/parser.py:390`*

---
<a id="sym-src_click_parser.py-430"></a>
### `_OptionParser._get_value_from_state` · method
```python
def _get_value_from_state(
        self, option_name: str, option: _Option, state: _ParsingState
    ) -> str | cabc.Sequence[str] | T_UNSET | T_FLAG_NEEDS_VALUE
```

### `_OptionParser._get_value_from_state`

从解析状态中获取选项的值。

**Parameters**:
- `option_name` — `str` — 选项的名称。
- `option` — `_Option` — 选项对象。
- `state` — `_ParsingState` — 解析状态对象。

**Returns**:
- `str | cabc.Sequence[str] | T_UNSET | T_FLAG_NEEDS_VALUE` — 选项的值，可以是字符串、字符串序列、未设置或需要值的标志。

**Raises**:
- `BadOptionUsage` — 如果选项需要参数但未提供。

**内部调用(库内):**
- [`BadOptionUsage`](src_click.md#sym-src_click_exceptions.py-304) — `BadOptionUsage` 类用于表示在使用命令行选项时出现错误的情况。

*来源: `src/click/parser.py:430`*

---
<a id="sym-src_click_parser.py-470"></a>
### `_OptionParser._process_opts` · method
```python
def _process_opts(self, arg: str, state: _ParsingState) -> None
```

### _OptionParser._process_opts

处理命令行选项。

**Parameters:**
- `arg` — `str` — 命令行参数。
- `state` — `_ParsingState` — 解析状态。

**Returns:**
- `None`

**Raises:**
- `NoSuchOption` — 如果找不到选项。
- `BadOptionUsage` — 如果选项使用不正确。

**内部调用(库内):**
- [`_normalize_opt`](src_click.md#sym-src_click_parser.py-120) — **用途**: Normalize an option string using the token normalization function from t
- [`_OptionParser._match_long_opt`](src_click.md#sym-src_click_parser.py-363) — 用途
- [`_OptionParser._match_short_opt`](src_click.md#sym-src_click_parser.py-390) — _OptionParser._match_short_opt

*来源: `src/click/parser.py:470`*

---
<a id="sym-src_click_parser.py-503"></a>
### `__getattr__` · func
```python
def __getattr__(name: str) -> object
```

用途: 用于处理未定义的属性访问，提供向后兼容性警告。

**Parameters**:
- `name` — `str` — 要访问的属性名称。

**Returns**:
- `object` — 返回与属性名称对应的对象。

**Raises**:
- `AttributeError` — 如果属性名称未定义。

*来源: `src/click/parser.py:503`*

---

## `src/click/shell_completion.py`

<a id="sym-src_click_shell_completion.py-19"></a>
### `shell_complete` · func
```python
def shell_complete(
    cli: Command,
    ctx_args: cabc.MutableMapping[str, t.Any],
    prog_name: str,
    complete_var: str,
    instruction: str,
) -> int
```

**用途**: Perform shell completion for the given CLI program.

**Parameters**:
- `cli` — `Command` — Command being called.
- `ctx_args` — `MutableMapping[str, t.Any]` — Extra arguments to pass to `cli.make_context`.
- `prog_name` — `str` — Name of the executable in the shell.
- `complete_var` — `str` — Name of the environment variable that holds the completion instruction.
- `instruction` — `str` — Value of `complete_var` with the completion instruction and shell, in the form `instruction_shell`.

**Returns**:
- `int` — Status code to exit with.

**Raises**:
- None

**内部调用(库内):**
- [`get_completion_class`](src_click.md#sym-src_click_shell_completion.py-472) — Look up a registered :class:`ShellComplete` subclass by the name provided by the
- [`ShellComplete.source`](src_click.md#sym-src_click_shell_completion.py-262) — **用途**: 生成 shell 脚本，定义完成函数。
- [`ShellComplete.complete`](src_click.md#sym-src_click_shell_completion.py-297) — **用途**: 生成要发送回 shell 的自动补全数据。

*来源: `src/click/shell_completion.py:19`*

---
<a id="sym-src_click_shell_completion.py-58"></a>
### `CompletionItem` · class
```python
class CompletionItem
```

`CompletionItem` 类用于表示命令行工具中的自动补全项。

- **__init__**
  - **Parameters**:
    - `value` — `t.Any` — 自动补全项的值。
    - `type` — `str` — 自动补全项的类型，默认为 "plain"。
    - `help` — `str | None` — 自动补全项的帮助信息，默认为 `None`。
    - `**kwargs` — `t.Any` — 其他任意关键字参数。
  - **Returns**: `None`
  - **Raises**: 无

- **__getattr__**
  - **Parameters**:
    - `name` — `str` — 要获取的属性名。
  - **Returns**: `t.Any`
  - **Raises**: 无

*来源: `src/click/shell_completion.py:58`*

---
<a id="sym-src_click_shell_completion.py-79"></a>
### `CompletionItem.__init__` · method
```python
def __init__(
        self,
        value: t.Any,
        type: str = "plain",
        help: str | None = None,
        **kwargs: t.Any,
    ) -> None
```

**用途**: 初始化一个 `CompletionItem` 对象，用于表示命令行补全项。

**Parameters**:
- `value` — `t.Any` — 补全项的值。
- `type` — `str` — 补全项的类型，默认为 "plain"。
- `help` — `str | None` — 补全项的帮助信息，默认为 `None`。
- `**kwargs` — `t.Any` — 其他任意关键字参数，存储在 `_info` 属性中。

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/shell_completion.py:79`*

---
<a id="sym-src_click_shell_completion.py-91"></a>
### `CompletionItem.__getattr__` · method
```python
def __getattr__(self, name: str) -> t.Any
```

获取 `CompletionItem` 对象的属性值。

**Parameters**:
- `name` — `str` — 要获取的属性名称。

**Returns**:
- `t.Any` — 属性值。

**Raises**:
- 无

*来源: `src/click/shell_completion.py:91`*

---
<a id="sym-src_click_shell_completion.py-201"></a>
### `ShellComplete` · class
```python
class ShellComplete
```

`ShellComplete` 类用于生成 shell 自动补全脚本。它提供了一系列方法来处理自动补全逻辑，包括获取命令行参数、生成补全变量、格式化补全项等。

### 方法

- **`__init__(self, cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, complete_var: str) -> None`**
  - **Parameters**:
    - `cli` — `Command` — 要生成补全脚本的 Click 命令。
    - `ctx_args` — `cabc.MutableMapping[str, t.Any]` — 命令上下文参数。
    - `prog_name` — `str` — 程序名称。
    - `complete_var` — `str` — 补全变量名。
  - **Returns**: `None`

- **`func_name(self) -> str`**
  - **Returns**: `str` — 补全函数名。

- **`source_vars(self) -> dict[str, t.Any]`**
  - **Returns**: `dict[str, t.Any]` — 补全脚本中的变量。

- **`source(self) -> str`**
  - **Returns**: `str` — 生成的 shell 补全脚本。

- **`get_completion_args(self) -> tuple[list[str], str]`**
  - **Returns**: `tuple[list[str], str]` — 命令行参数和补全参数。

*来源: `src/click/shell_completion.py:201`*

---
<a id="sym-src_click_shell_completion.py-230"></a>
### `ShellComplete.__init__` · method
```python
def __init__(
        self,
        cli: Command,
        ctx_args: cabc.MutableMapping[str, t.Any],
        prog_name: str,
        complete_var: str,
    ) -> None
```

初始化 `ShellComplete` 对象。

**Parameters**:
- `cli` — `Command` — 要完成的命令对象。
- `ctx_args` — `MutableMapping[str, Any]` — 上下文参数的映射。
- `prog_name` — `str` — 程序名称。
- `complete_var` — `str` — 完成变量的名称。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/shell_completion.py:230`*

---
<a id="sym-src_click_shell_completion.py-243"></a>
### `ShellComplete.func_name` · method
装饰器: `@property`
```python
def func_name(self) -> str
```

### ShellComplete.func_name

Returns:
- `str`: The name of the shell function defined by the completion script.

Raises:
- (无)

*来源: `src/click/shell_completion.py:243`*

---
<a id="sym-src_click_shell_completion.py-250"></a>
### `ShellComplete.source_vars` · method
```python
def source_vars(self) -> dict[str, t.Any]
```

提供用于格式化 `source_template` 的变量。

**Parameters**:
- 无

**Returns**:
- `dict[str, t.Any]`: 包含 `complete_func`, `complete_var`, 和 `prog_name` 的字典。

**Raises**:
- 无

*来源: `src/click/shell_completion.py:250`*

---
<a id="sym-src_click_shell_completion.py-262"></a>
### `ShellComplete.source` · method
```python
def source(self) -> str
```

**用途**: 生成 shell 脚本，定义完成函数。

**Parameters**:
- 无

**Returns**:
- `str`: 生成的 shell 脚本，定义了完成函数。

**Raises**:
- 无

**内部调用(库内):**
- [`ShellComplete.source_vars`](src_click.md#sym-src_click_shell_completion.py-250) — 提供用于格式化 `source_template` 的变量。

*来源: `src/click/shell_completion.py:262`*

---
<a id="sym-src_click_shell_completion.py-270"></a>
### `ShellComplete.get_completion_args` · method
```python
def get_completion_args(self) -> tuple[list[str], str]
```

Use the env vars defined by the shell script to return a tuple of `args, incomplete`. This must be implemented by subclasses.

**Parameters**:
- 无

**Returns**:
- `tuple[list[str], str]`: A tuple containing a list of arguments and the incomplete argument.

**Raises**:
- `NotImplementedError`: If the method is not implemented by subclasses.

*来源: `src/click/shell_completion.py:270`*

---
<a id="sym-src_click_shell_completion.py-277"></a>
### `ShellComplete.get_completions` · method
```python
def get_completions(self, args: list[str], incomplete: str) -> list[CompletionItem]
```

### ShellComplete.get_completions

Determine the context and last complete command or parameter from the complete args. Call that object's ``shell_complete`` method to get the completions for the incomplete value.

**Parameters**:
- `args` — `list[str]` — List of complete args before the incomplete value.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns**:
- `list[CompletionItem]` — Completions for the incomplete value.

**Raises**:
- None

**内部调用(库内):**
- [`_resolve_context`](src_click.md#sym-src_click_shell_completion.py-576) — **用途**: 生成以命令为起点的上下文层次结构，并遍历完整参数。此过程仅跟随命令，不触发输入提示或回调。
- [`_resolve_incomplete`](src_click.md#sym-src_click_shell_completion.py-637) — **用途**: Find the Click object that will handle the completion of the incomplete 
- [`shell_complete`](src_click.md#sym-src_click_shell_completion.py-19) — **用途**: Perform shell completion for the given CLI program.

*来源: `src/click/shell_completion.py:277`*

---
<a id="sym-src_click_shell_completion.py-289"></a>
### `ShellComplete.format_completion` · method
```python
def format_completion(self, item: CompletionItem) -> str
```

Format a completion item into the form recognized by the shell script. This method must be implemented by subclasses.

- **Parameters**:
  - `item` — `CompletionItem` — Completion item to format.
- **Returns**:
  - `str` — Formatted completion item.
- **Raises**:
  - `NotImplementedError`

*来源: `src/click/shell_completion.py:289`*

---
<a id="sym-src_click_shell_completion.py-297"></a>
### `ShellComplete.complete` · method
```python
def complete(self) -> str
```

**用途**: 生成要发送回 shell 的自动补全数据。

**Parameters**:
- `self` — ShellComplete — 自动补全实例。

**Returns**:
- `str` — 格式化后的自动补全数据，每行一个补全项。

**Raises**:
- 无

**内部调用(库内):**
- [`ShellComplete.get_completion_args`](src_click.md#sym-src_click_shell_completion.py-270) — Use the env vars defined by the shell script to return a tuple of `args, incompl
- [`ShellComplete.get_completions`](src_click.md#sym-src_click_shell_completion.py-277) — ShellComplete.get_completions
- [`ShellComplete.format_completion`](src_click.md#sym-src_click_shell_completion.py-289) — Format a completion item into the form recognized by the shell script. This meth

*来源: `src/click/shell_completion.py:297`*

---
<a id="sym-src_click_shell_completion.py-310"></a>
### `BashComplete` · class
```python
class BashComplete(ShellComplete)
```

BashComplete 类用于生成 Bash shell 的自动补全脚本。

- `_check_version() -> None`: 检查 Bash 版本是否支持所需的自动补全功能。
- `source(self) -> str`: 生成 Bash 自动补全脚本的字符串。
- `get_completion_args(self) -> tuple[list[str], str]`: 获取用于生成自动补全脚本的参数。
- `format_completion(self, item: CompletionItem) -> str`: 格式化单个自动补全项为 Bash 脚本中的字符串。

*来源: `src/click/shell_completion.py:310`*

---
<a id="sym-src_click_shell_completion.py-317"></a>
### `BashComplete._check_version` · method
装饰器: `@staticmethod`
```python
def _check_version() -> None
```

检查 Bash 版本是否支持 shell 完成。

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/shell_completion.py:317`*

---
<a id="sym-src_click_shell_completion.py-349"></a>
### `BashComplete.source` · method
```python
def source(self) -> str
```

### BashComplete.source

Returns the source code for the Bash completion script. This method ensures the script is up-to-date by checking the version before returning the source.

**Parameters**:
- None

**Returns**:
- `str`: The source code for the Bash completion script.

**Raises**:
- None

**内部调用(库内):**
- [`BashComplete._check_version`](src_click.md#sym-src_click_shell_completion.py-317) — 检查 Bash 版本是否支持 shell 完成。

*来源: `src/click/shell_completion.py:349`*

---
<a id="sym-src_click_shell_completion.py-353"></a>
### `BashComplete.get_completion_args` · method
```python
def get_completion_args(self) -> tuple[list[str], str]
```

获取 Bash 完成命令的参数。

**Parameters**:
- `self` — `BashComplete` — BashComplete 类的实例。

**Returns**:
- `tuple[list[str], str]` — 一个包含两个元素的元组，第一个元素是命令的参数列表，第二个元素是当前未完成的参数。

**Raises**:
- `IndexError` — 如果 `COMP_CWORD` 超出 `COMP_WORDS` 的范围。

**内部调用(库内):**
- [`split_arg_string`](src_click.md#sym-src_click_shell_completion.py-482) — Split an argument string as with :func:`shlex.split`, but don't fail if the stri

*来源: `src/click/shell_completion.py:353`*

---
<a id="sym-src_click_shell_completion.py-365"></a>
### `BashComplete.format_completion` · method
```python
def format_completion(self, item: CompletionItem) -> str
```

格式化完成项为字符串。

**Parameters**:
- `item` — `CompletionItem` — 完成项。

**Returns**:
- `str` — 格式化后的完成项字符串。

*来源: `src/click/shell_completion.py:365`*

---
<a id="sym-src_click_shell_completion.py-369"></a>
### `ZshComplete` · class
```python
class ZshComplete(ShellComplete)
```

ZshComplete 类用于处理 Zsh shell 的自动补全功能。

### 方法

- **get_completion_args(self) -> tuple[list[str], str]**
  - **Parameters**:
    - 无
  - **Returns**:
    - `tuple[list[str], str]`: 返回一个包含补全选项列表和当前输入字符串的元组。
  - **Raises**:
    - 无

- **format_completion(self, item: CompletionItem) -> str**
  - **Parameters**:
    - `item: CompletionItem`: 补全项对象。
  - **Returns**:
    - `str`: 格式化后的补全字符串。
  - **Raises**:
    - 无

*来源: `src/click/shell_completion.py:369`*

---
<a id="sym-src_click_shell_completion.py-375"></a>
### `ZshComplete.get_completion_args` · method
```python
def get_completion_args(self) -> tuple[list[str], str]
```

获取 Zsh 完成命令的参数和不完整部分。

**Parameters:**
- 无

**Returns:**
- `tuple[list[str], str]`: 一个包含命令参数列表和不完整部分的元组。

**Raises:**
- `IndexError`: 如果 `COMP_CWORD` 超出 `COMP_WORDS` 的范围。

**内部调用(库内):**
- [`split_arg_string`](src_click.md#sym-src_click_shell_completion.py-482) — Split an argument string as with :func:`shlex.split`, but don't fail if the stri

*来源: `src/click/shell_completion.py:375`*

---
<a id="sym-src_click_shell_completion.py-387"></a>
### `ZshComplete.format_completion` · method
```python
def format_completion(self, item: CompletionItem) -> str
```

格式化 Zsh 完成项。

**Parameters**:
- `item` — `CompletionItem` — 要格式化的完成项。

**Returns**:
- `str` — 格式化后的 Zsh 完成项字符串。

**Raises**:
- 无

*来源: `src/click/shell_completion.py:387`*

---
<a id="sym-src_click_shell_completion.py-405"></a>
### `FishComplete` · class
```python
class FishComplete(ShellComplete)
```

FishComplete 类用于处理 Fish shell 的命令补全。它继承自 ShellComplete 类，并提供了特定于 Fish shell 的补全逻辑。

### 方法

#### get_completion_args(self) -> tuple[list[str], str]

获取用于 Fish shell 补全的参数。

- **Parameters**:
  - 无

- **Returns**:
  - `tuple[list[str], str]`: 一个包含补全选项列表和当前输入字符串的元组。

#### format_completion(self, item: CompletionItem) -> str

格式化一个补全项，使其适合 Fish shell 的补全格式。

- **Parameters**:
  - `item` — `CompletionItem`: 要格式化的补全项。

- **Returns**:
  - `str`: 格式化后的补全项字符串。

*来源: `src/click/shell_completion.py:405`*

---
<a id="sym-src_click_shell_completion.py-411"></a>
### `FishComplete.get_completion_args` · method
```python
def get_completion_args(self) -> tuple[list[str], str]
```

获取 Fish shell 完成命令的参数。

**Parameters:**
- `self` — `FishComplete` — `FishComplete` 类的实例。

**Returns:**
- `tuple[list[str], str]` — 一个包含两个元素的元组，第一个元素是命令参数列表，第二个元素是不完整的单词。

**Raises:**
- 无

**内部调用(库内):**
- [`split_arg_string`](src_click.md#sym-src_click_shell_completion.py-482) — Split an argument string as with :func:`shlex.split`, but don't fail if the stri

*来源: `src/click/shell_completion.py:411`*

---
<a id="sym-src_click_shell_completion.py-425"></a>
### `FishComplete.format_completion` · method
```python
def format_completion(self, item: CompletionItem) -> str
```

### FishComplete.format_completion

格式化一个 `CompletionItem` 对象为鱼 shell 完成字符串。

**Parameters:**
- `item` — `CompletionItem` — 要格式化的完成项。

**Returns:**
- `str` — 格式化后的鱼 shell 完成字符串。

**Raises:**
- 无

*来源: `src/click/shell_completion.py:425`*

---
<a id="sym-src_click_shell_completion.py-452"></a>
### `add_completion_class` · func
```python
def add_completion_class(
    cls: ShellCompleteType, name: str | None = None
) -> ShellCompleteType
```

注册一个 `ShellComplete` 子类，并在指定名称下进行处理。

**Parameters**:
- `cls` — ShellCompleteType — 要处理 shell 自动补全的类。
- `name` — str | None — 注册类的名称。默认为类的 `name` 属性。

**Returns**:
- ShellCompleteType — 返回传入的类。

**Raises**:
- 无

*来源: `src/click/shell_completion.py:452`*

---
<a id="sym-src_click_shell_completion.py-472"></a>
### `get_completion_class` · func
```python
def get_completion_class(shell: str) -> type[ShellComplete] | None
```

Look up a registered :class:`ShellComplete` subclass by the name provided by the completion instruction environment variable. If the name isn't registered, returns ``None``.

**Parameters**:
- shell — str — Name the class is registered under.

**Returns**:
- type[ShellComplete] | None — The registered :class:`ShellComplete` subclass or ``None`` if not found.

*来源: `src/click/shell_completion.py:472`*

---
<a id="sym-src_click_shell_completion.py-482"></a>
### `split_arg_string` · func
```python
def split_arg_string(string: str) -> list[str]
```

Split an argument string as with :func:`shlex.split`, but don't fail if the string is incomplete. Ignores a missing closing quote or incomplete escape sequence and uses the partial token as-is.

**Parameters**:
- `string` — `str` — String to split.

**Returns**:
- `list[str]` — List of tokens.

**Raises**:
- None

*来源: `src/click/shell_completion.py:482`*

---
<a id="sym-src_click_shell_completion.py-519"></a>
### `_is_incomplete_argument` · func
```python
def _is_incomplete_argument(ctx: Context, param: Parameter) -> bool
```

Determine if the given parameter is an argument that can still accept values.

**Parameters**:
- `ctx` — `Context` — Invocation context for the command represented by the parsed complete args.
- `param` — `Parameter` — Argument object being checked.

**Returns**:
- `bool` — True if the parameter is an argument that can still accept values, False otherwise.

**内部调用(库内):**
- [`Context.get_parameter_source`](src_click.md#sym-src_click_core.py-937) — 获取参数的来源。这表明参数值是从哪里获得的。

*来源: `src/click/shell_completion.py:519`*

---
<a id="sym-src_click_shell_completion.py-542"></a>
### `_start_of_option` · func
```python
def _start_of_option(ctx: Context, value: str) -> bool
```

检查值是否看起来像一个选项的开始。

**Parameters**:
- `ctx` — `Context` — 上下文对象。
- `value` — `str` — 要检查的值。

**Returns**:
- `bool` — 如果值看起来像一个选项的开始则返回 `True`，否则返回 `False`。

*来源: `src/click/shell_completion.py:542`*

---
<a id="sym-src_click_shell_completion.py-551"></a>
### `_is_incomplete_option` · func
```python
def _is_incomplete_option(ctx: Context, args: list[str], param: Parameter) -> bool
```

Determine if the given parameter is an option that needs a value.

**Parameters**:
- `ctx` — `Context` — The context object.
- `args` — `list[str]` — List of complete args before the incomplete value.
- `param` — `Parameter` — Option object being checked.

**Returns**:
- `bool` — True if the parameter is an option that needs a value, False otherwise.

**Raises**:
- None

**内部调用(库内):**
- [`_start_of_option`](src_click.md#sym-src_click_shell_completion.py-542) — 检查值是否看起来像一个选项的开始。

*来源: `src/click/shell_completion.py:551`*

---
<a id="sym-src_click_shell_completion.py-576"></a>
### `_resolve_context` · func
```python
def _resolve_context(
    cli: Command,
    ctx_args: cabc.MutableMapping[str, t.Any],
    prog_name: str,
    args: list[str],
) -> Context
```

**用途**: 生成以命令为起点的上下文层次结构，并遍历完整参数。此过程仅跟随命令，不触发输入提示或回调。

**Parameters**:
- `cli` — `Command` — 正在调用的命令。
- `ctx_args` — `MutableMapping[str, Any]` — 传递给上下文的参数。
- `prog_name` — `str` — 在 shell 中的可执行文件名。
- `args` — `list[str]` — 在不完整值之前的完整参数列表。

**Returns**:
- `Context` — 生成的上下文层次结构。

**Raises**:
- 无

**内部调用(库内):**
- [`Command.make_context`](src_click.md#sym-src_click_core.py-1280) — `Command.make_context`

*来源: `src/click/shell_completion.py:576`*

---
<a id="sym-src_click_shell_completion.py-637"></a>
### `_resolve_incomplete` · func
```python
def _resolve_incomplete(
    ctx: Context, args: list[str], incomplete: str
) -> tuple[Command | Parameter, str]
```

**用途**: Find the Click object that will handle the completion of the incomplete value. Return the object and the incomplete value.

**Parameters**:
- `ctx` — `Context` — Invocation context for the command represented by the parsed complete args.
- `args` — `list[str]` — List of complete args before the incomplete value.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns**:
- `tuple[Command | Parameter, str]` — The Click object that will handle the completion and the incomplete value.

**Raises**:
- None

**内部调用(库内):**
- [`_start_of_option`](src_click.md#sym-src_click_shell_completion.py-542) — 检查值是否看起来像一个选项的开始。
- [`Command.get_params`](src_click.md#sym-src_click_core.py-1099) — 获取命令的所有参数，包括帮助选项。
- [`_is_incomplete_option`](src_click.md#sym-src_click_shell_completion.py-551) — Determine if the given parameter is an option that needs a value.
- [`_is_incomplete_argument`](src_click.md#sym-src_click_shell_completion.py-519) — Determine if the given parameter is an argument that can still accept values.

*来源: `src/click/shell_completion.py:637`*

---

## `src/click/termui.py`

<a id="sym-src_click_termui.py-59"></a>
### `_mask_hidden_input` · func
```python
def _mask_hidden_input(message: str, value: str) -> str
```

Replace occurrences of `value` in `message` with a fixed mask.

**Parameters**:
- `message` — `str` — The input message where the value will be replaced.
- `value` — `str` — The value to be replaced in the message.

**Returns**:
- `str` — The message with occurrences of `value` replaced by `_HIDDEN_INPUT_MASK`.

**Raises**:
- (No exceptions raised)

*来源: `src/click/termui.py:59`*

---
<a id="sym-src_click_termui.py-77"></a>
### `hidden_prompt_func` · func
```python
def hidden_prompt_func(prompt: str) -> str
```

**用途**: 提示用户输入密码，输入时不会显示在屏幕上。

**Parameters**:
- `prompt` — `str` — 提示信息，用于指导用户输入密码。

**Returns**:
- `str` — 用户输入的密码。

**Raises**:
- 无

*来源: `src/click/termui.py:77`*

---
<a id="sym-src_click_termui.py-83"></a>
### `_readline_prompt` · func
```python
def _readline_prompt(func: t.Callable[[str], str], text: str, err: bool) -> str
```

调用一个提示函数，传递完整的提示文本，以便在非 Windows 系统上 readline 可以正确处理行编辑和光标定位。

**Parameters**:
- `func` — `t.Callable[[str], str]` — 提示函数。
- `text` — `str` — 完整的提示文本。
- `err` — `bool` — 是否将输出重定向到标准错误。

**Returns**:
- `str` — 提示函数的返回值。

**Raises**:
- 无

**内部调用(库内):**
- [`func`](src_click.md#sym-src_click__compat.py-549) — func

*来源: `src/click/termui.py:83`*

---
<a id="sym-src_click_termui.py-93"></a>
### `_build_prompt` · func
```python
def _build_prompt(
    text: str,
    suffix: str,
    show_default: bool | str = False,
    default: t.Any | None = None,
    show_choices: bool = True,
    type: ParamType[t.Any] | None = None,
) -> str
```

构建命令行提示符。

**Parameters**:
- `text` — `str` — 提示文本。
- `suffix` — `str` — 提示的后缀。
- `show_default` — `bool | str` — 是否显示默认值，或自定义默认值的显示方式。
- `default` — `t.Any | None` — 默认值。
- `show_choices` — `bool` — 是否显示选项。
- `type` — `ParamType[t.Any] | None` — 参数类型。

**Returns**:
- `str` — 完整的提示符字符串。

**Raises**:
- 无

**内部调用(库内):**
- [`_format_default`](src_click.md#sym-src_click_termui.py-111) — 格式化默认值，如果默认值是文件对象，则返回文件名。

*来源: `src/click/termui.py:93`*

---
<a id="sym-src_click_termui.py-111"></a>
### `_format_default` · func
```python
def _format_default(default: t.Any) -> t.Any
```

格式化默认值，如果默认值是文件对象，则返回文件名。

**Parameters**:
- `default` — `t.Any` — 要格式化的默认值。

**Returns**:
- `t.Any` — 格式化后的默认值，如果是文件对象则返回文件名，否则返回原值。

**Raises**:
- 无

*来源: `src/click/termui.py:111`*

---
<a id="sym-src_click_termui.py-118"></a>
### `prompt` · func
```python
def prompt(
    text: str,
    default: t.Any | None = None,
    hide_input: bool = False,
    confirmation_prompt: bool | str = False,
    type: ParamType[t.Any] | t.Any | None = None,
    value_proc: t.Callable[[str], t.Any] | None = None,
    prompt_suffix: str = ": ",
    show_default: bool | str = True,
    err: bool = False,
    show_choices: bool = True,
) -> t.Any
```

**用途**: 提示用户输入，并根据参数进行类型检查和确认。

**Parameters**:
- `text` — `str` — 提示用户输入的文本。
- `default` — `t.Any | None` — 输入为空时的默认值。
- `hide_input` — `bool` — 是否隐藏输入值。
- `confirmation_prompt` — `bool | str` — 是否二次确认输入值，可以是字符串自定义消息。
- `type` — `ParamType[t.Any] | t.Any | None` — 用于检查值的类型。
- `value_proc` — `t.Callable[[str], t.Any] | None` — 用于转换值的函数。
- `prompt_suffix` — `str` — 提示文本的后缀。
- `show_default` — `bool | str` — 是否在提示中显示默认值，可以是字符串显示自定义文本。
- `err` — `bool` — 是否将文件默认设置为 `stderr`。
- `show_choices` — `bool` — 如果传递的类型是 Choice，是否显示选项。

**Returns**:
- `t.Any` — 用户输入并经过处理后的值。

**Raises**:
- `Abort` — 如果用户通过发送中断信号中止输入。

**内部调用(库内):**
- [`_readline_prompt`](src_click.md#sym-src_click_termui.py-83) — 调用一个提示函数，传递完整的提示文本，以便在非 Windows 系统上 readline 可以正确处理行编辑和光标定位。
- [`Abort`](src_click.md#sym-src_click_exceptions.py-362) — `Abort` 类继承自 `RuntimeError`，用于表示命令执行过程中发生了中止操作。
- [`_build_prompt`](src_click.md#sym-src_click_termui.py-93) — 构建命令行提示符。
- [`prompt_func`](src_click.md#sym-src_click_termui.py-180) — **用途**: 提示用户输入并返回输入的字符串。
- [`_mask_hidden_input`](src_click.md#sym-src_click_termui.py-59) — Replace occurrences of `value` in `message` with a fixed mask.

*来源: `src/click/termui.py:118`*

---
<a id="sym-src_click_termui.py-180"></a>
### `prompt_func` · func
```python
def prompt_func(text: str) -> str
```

**用途**: 提示用户输入并返回输入的字符串。

**Parameters**:
- `text` — `str` — 提示信息。

**Returns**:
- `str` — 用户输入的字符串。

**Raises**:
- `Abort` — 如果用户通过 `^C` 中断输入。

**内部调用(库内):**
- [`_readline_prompt`](src_click.md#sym-src_click_termui.py-83) — 调用一个提示函数，传递完整的提示文本，以便在非 Windows 系统上 readline 可以正确处理行编辑和光标定位。
- [`Abort`](src_click.md#sym-src_click_exceptions.py-362) — `Abort` 类继承自 `RuntimeError`，用于表示命令执行过程中发生了中止操作。

*来源: `src/click/termui.py:180`*

---
<a id="sym-src_click_termui.py-231"></a>
### `confirm` · func
```python
def confirm(
    text: str,
    default: bool | None = False,
    abort: bool = False,
    prompt_suffix: str = ": ",
    show_default: bool = True,
    err: bool = False,
) -> bool
```

**用途**: Prompts the user for confirmation with a yes/no question.

**Parameters**:
- `text` — `str` — The question to ask.
- `default` — `bool | None` — The default value to use when no input is given. If `None`, repeat until input is given.
- `abort` — `bool` — If this is set to `True`, a negative answer aborts the exception by raising :exc:`Abort`.
- `prompt_suffix` — `str` — A suffix that should be added to the prompt.
- `show_default` — `bool` — Shows or hides the default value in the prompt.
- `err` — `bool` — If set to true, the file defaults to ``stderr`` instead of ``stdout``, the same as with echo.

**Returns**:
- `bool` — The user's response to the confirmation question.

**Raises**:
- :exc:`Abort` — If the user aborts the input by sending an interrupt signal and `abort` is set to `True`.

**内部调用(库内):**
- [`_build_prompt`](src_click.md#sym-src_click_termui.py-93) — 构建命令行提示符。
- [`_readline_prompt`](src_click.md#sym-src_click_termui.py-83) — 调用一个提示函数，传递完整的提示文本，以便在非 Windows 系统上 readline 可以正确处理行编辑和光标定位。
- [`Abort`](src_click.md#sym-src_click_exceptions.py-362) — `Abort` 类继承自 `RuntimeError`，用于表示命令执行过程中发生了中止操作。

*来源: `src/click/termui.py:231`*

---
<a id="sym-src_click_termui.py-290"></a>
### `get_pager_file` · func
```python
def get_pager_file(
    color: bool | None = None,
) -> t.ContextManager[t.TextIO]
```

Context manager that yields a writable file-like object which can be used as an output pager.

**Parameters**:
- color — bool | None — Controls if the pager supports ANSI colors or not. The default is autodetection.

**Returns**:
- t.ContextManager[t.TextIO] — A context manager that yields a writable file-like object for use as an output pager.

**Raises**:
- None

**内部调用(库内):**
- [`resolve_color_default`](src_click.md#sym-src_click_globals.py-54) — 获取颜色标志的默认值。如果传递了一个值，则返回该值；否则，从当前上下文中查找。

*来源: `src/click/termui.py:290`*

---
<a id="sym-src_click_termui.py-309"></a>
### `echo_via_pager` · func
```python
def echo_via_pager(
    text_or_generator: cabc.Iterable[str] | t.Callable[[], cabc.Iterable[str]] | str,
    color: bool | None = None,
) -> None
```

This function takes a text or a generator of text and displays it via an environment-specific pager on stdout.

**Parameters**:
- `text_or_generator` — `cabc.Iterable[str] | t.Callable[[], cabc.Iterable[str]] | str` — The text to page, or a generator emitting the text to page.
- `color` — `bool | None` — Controls if the pager supports ANSI colors or not. The default is autodetection.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`get_pager_file`](src_click.md#sym-src_click_termui.py-290) — Context manager that yields a writable file-like object which can be used as an 

*来源: `src/click/termui.py:309`*

---
<a id="sym-src_click_termui.py-345"></a>
### `progressbar` · func
装饰器: `@t.overload`
```python
def progressbar(
    *,
    length: int,
    label: str | None = None,
    hidden: bool = False,
    show_eta: bool = True,
    show_percent: bool | None = None,
    show_pos: bool = False,
    fill_char: str = "#",
    empty_char: str = "-",
    bar_template: str = "%(label)s  [%(bar)s]  %(info)s",
    info_sep: str = "  ",
    width: int = 36,
    file: t.TextIO | None = None,
    color: bool | None = None,
    update_min_steps: int = 1,
) -> ProgressBar[int]
```

创建一个进度条对象，用于显示任务的进度。

**Parameters**:
- `length` — `int` — 进度条的总长度。
- `label` — `str | None` — 进度条的标签，默认为 `None`。
- `hidden` — `bool` — 是否隐藏进度条，默认为 `False`。
- `show_eta` — `bool` — 是否显示预计完成时间，默认为 `True`。
- `show_percent` — `bool | None` — 是否显示百分比，默认为 `None`。
- `show_pos` — `bool` — 是否显示当前位置，默认为 `False`。
- `fill_char` — `str` — 进度条填充字符，默认为 `#`。
- `empty_char` — `str` — 进度条空闲字符，默认为 `-`。
- `bar_template` — `str` — 进度条的模板字符串，默认为 `%(label)s  [%(bar)s]  %(info)s`。
- `info_sep` — `str` — 信息之间的分隔符，默认为 `  `。
- `width` — `int` — 进度条的宽度，默认为 `36`。
- `file` — `t.TextIO | None` — 输出文件，默认为 `None`。
- `color` — `bool | None` — 是否启用颜色，默认为 `None`。
- `update_min_steps` — `int` — 更新进度条的最小步数，默认

*来源: `src/click/termui.py:345`*

---
<a id="sym-src_click_termui.py-365"></a>
### `progressbar` · func
装饰器: `@t.overload`
```python
def progressbar(
    iterable: cabc.Iterable[V] | None = None,
    length: int | None = None,
    label: str | None = None,
    hidden: bool = False,
    show_eta: bool = True,
    show_percent: bool | None = None,
    show_pos: bool = False,
    item_show_func: t.Callable[[V | None], str | None] | None = None,
    fill_char: str = "#",
    empty_char: str = "-",
    bar_template: str = "%(label)s  [%(bar)s]  %(info)s",
    info_sep: str = "  ",
    width: int = 36,
    file: t.TextIO | None = None,
    color: bool | None = None,
    update_min_steps: int = 1,
) -> ProgressBar[V]
```

### `progressbar` 函数

创建并返回一个 `ProgressBar` 对象，用于显示进度条。

#### Parameters
- `iterable` (`cabc.Iterable[V] | None`): 要迭代的对象，用于计算进度。如果为 `None`，则需要手动调用 `update` 方法。
- `length` (`int | None`): 进度条的总长度。如果为 `None`，则从 `iterable` 中推断。
- `label` (`str | None`): 进度条的标签。
- `hidden` (`bool`): 是否隐藏进度条。
- `show_eta` (`bool`): 是否显示估计的剩余时间。
- `show_percent` (`bool | None`): 是否显示百分比。如果为 `None`，则根据 `show_eta` 和 `show_pos` 自动决定。
- `show_pos` (`bool`): 是否显示当前位置。
- `item_show_func` (`t.Callable[[V | None], str | None] | None`): 用于显示每个项目的函数。
- `fill_char` (`str`): 进度条填充字符。
- `empty_char` (`str`): 进度条空闲字符。
- `bar_template` (`str`): 进度条的模板字符串。
- `info_sep` (`str`): 信息部分的分隔符。
- `width` (`int`): 进度条的宽度。
- `file` (`t.TextIO | None`

*来源: `src/click/termui.py:365`*

---
<a id="sym-src_click_termui.py-385"></a>
### `progressbar` · func
```python
def progressbar(
    iterable: cabc.Iterable[V] | None = None,
    length: int | None = None,
    label: str | None = None,
    hidden: bool = False,
    show_eta: bool = True,
    show_percent: bool | None = None,
    show_pos: bool = False,
    item_show_func: t.Callable[[V | None], str | None] | None = None,
    fill_char: str = "#",
    empty_char: str = "-",
    bar_template: str = "%(label)s  [%(bar)s]  %(info)s",
    info_sep: str = "  ",
    width: int = 36,
    file: t.TextIO | None = None,
    color: bool | None = None,
    update_min_steps: int = 1,
) -> ProgressBar[V]
```

**用途**: 创建一个可迭代的上下文管理器，用于在迭代过程中显示进度条。

**Parameters**:
- `iterable` — `cabc.Iterable[V] | None` — 要迭代的可迭代对象，如果提供，则使用该可迭代对象的长度。
- `length` — `int | None` — 要迭代的项目数量，如果提供，则使用该长度。
- `label` — `str | None` — 进度条的标签。
- `hidden` — `bool` — 是否隐藏进度条，默认为 `False`。
- `show_eta` — `bool` — 是否显示剩余时间，默认为 `True`。
- `show_percent` — `bool | None` — 是否显示百分比，默认为 `None`。
- `show_pos` — `bool` — 是否显示当前位置，默认为 `False`。
- `item_show_func` — `t.Callable[[V | None], str | None] | None` — 用于显示每个项目的函数，默认为 `None`。
- `fill_char` — `str` — 进度条填充字符，默认为 `#`。
- `empty_char` — `str` — 进度条空字符，默认为 `-`。
- `bar_template` — `str` — 进度条模板，默认为 `%(label)s  [%(bar)s]  %(info)s`。
- `info_sep` — `str` — 信息分隔符，默认为 `  `。
-

**内部调用(库内):**
- [`resolve_color_default`](src_click.md#sym-src_click_globals.py-54) — 获取颜色标志的默认值。如果传递了一个值，则返回该值；否则，从当前上下文中查找。
- [`ProgressBar`](src_click.md#sym-src_click__termui_impl.py-57) — `ProgressBar` 类用于创建和管理进度条，提供进度更新、渲染和格式化等功能。

*来源: `src/click/termui.py:385`*

---
<a id="sym-src_click_termui.py-544"></a>
### `clear` · func
```python
def clear() -> None
```

Clears the terminal screen. This will have the effect of clearing the whole visible space of the terminal and moving the cursor to the top left. This does not do anything if not connected to a terminal.

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/termui.py:544`*

---
<a id="sym-src_click_termui.py-558"></a>
### `_interpret_color` · func
```python
def _interpret_color(color: int | tuple[int, int, int] | str, offset: int = 0) -> str
```

Interpret a color value and return its ANSI escape sequence.

**Parameters**:
- `color` — `int | tuple[int, int, int] | str` — The color value to interpret.
- `offset` — `int` — The offset to apply to the color code (default is 0).

**Returns**:
- `str` — The ANSI escape sequence for the color.

**Raises**:
- None

*来源: `src/click/termui.py:558`*

---
<a id="sym-src_click_termui.py-569"></a>
### `style` · func
```python
def style(
    text: t.Any,
    fg: int | tuple[int, int, int] | str | None = None,
    bg: int | tuple[int, int, int] | str | None = None,
    bold: bool | None = None,
    dim: bool | None = None,
    underline: bool | None = None,
    overline: bool | None = None,
    italic: bool | None = None,
    blink: bool | None = None,
    reverse: bool | None = None,
    strikethrough: bool | None = None,
    reset: bool = True,
) -> str
```

**用途**: Styles a text with ANSI styles and returns the new string.

**Parameters**:
- `text` — `t.Any` — The text to be styled.
- `fg` — `int | tuple[int, int, int] | str | None` — The foreground color, can be a color name or RGB tuple.
- `bg` — `int | tuple[int, int, int] | str | None` — The background color, can be a color name or RGB tuple.
- `bold` — `bool | None` — Whether to apply bold style.
- `dim` — `bool | None` — Whether to apply dim style.
- `underline` — `bool | None` — Whether to apply underline style.
- `overline` — `bool | None` — Whether to apply overline style.
- `italic` — `bool | None` — Whether to apply italic style.
- `blink` — `bool | None` — Whether to apply blink style.
- `reverse` — `bool | None` — Whether to apply reverse style.
- `strikethrough` — `bool | None` — Whether to apply strikethrough style.
- `reset` — `bool` — Whether to reset the styling at the end of the string.

**Returns**:
- `str` — The styled text.

**Raises**:
- None

**内部调用(库内):**
- [`_interpret_color`](src_click.md#sym-src_click_termui.py-558) — Interpret a color value and return its ANSI escape sequence.

*来源: `src/click/termui.py:569`*

---
<a id="sym-src_click_termui.py-698"></a>
### `unstyle` · func
```python
def unstyle(text: str) -> str
```

**用途**: Removes ANSI styling information from a string.

**Parameters**:
- `text` — `str` — The text to remove style information from.

**Returns**:
- `str` — The text with ANSI styling information removed.

**Raises**:
- None

**内部调用(库内):**
- [`strip_ansi`](src_click.md#sym-src_click__compat.py-487) — **用途**: 移除字符串中的 ANSI 转义码。

*来源: `src/click/termui.py:698`*

---
<a id="sym-src_click_termui.py-710"></a>
### `secho` · func
```python
def secho(
    message: t.Any | None = None,
    file: t.IO[t.AnyStr] | None = None,
    nl: bool = True,
    err: bool = False,
    color: bool | None = None,
    **styles: t.Any,
) -> None
```

`secho` 函数用于在终端中输出带有样式的文本。

**Parameters**:
- `message` — `t.Any | None` — 要输出的消息，可以是任何类型，但非字符串类型会被转换为字符串。
- `file` — `t.IO[t.AnyStr] | None` — 输出的目标文件，默认为标准输出。
- `nl` — `bool` — 是否在消息末尾添加换行符，默认为 `True`。
- `err` — `bool` — 是否将输出重定向到标准错误，默认为 `False`。
- `color` — `bool | None` — 是否应用颜色样式，默认为 `None`。
- `**styles` — `t.Any` — 传递给 `style` 函数的样式参数。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`style`](src_click.md#sym-src_click_termui.py-569) — **用途**: Styles a text with ANSI styles and returns the new string.

*来源: `src/click/termui.py:710`*

---
<a id="sym-src_click_termui.py-745"></a>
### `edit` · func
装饰器: `@t.overload`
```python
def edit(
    text: bytes | bytearray,
    editor: str | None = None,
    env: cabc.Mapping[str, str] | None = None,
    require_save: bool = False,
    extension: str = ".txt",
) -> bytes | None
```

编辑给定的文本内容。

**Parameters**:
- `text` — `bytes | bytearray` — 要编辑的文本内容。
- `editor` — `str | None` — 用于编辑文本的编辑器名称，如果为 `None`，则使用系统默认编辑器。
- `env` — `cabc.Mapping[str, str] | None` — 传递给编辑器的环境变量。
- `require_save` — `bool` — 是否要求编辑器保存更改。
- `extension` — `str` — 保存文件的扩展名。

**Returns**:
- `bytes | None` — 编辑后的文本内容，如果未保存更改则返回 `None`。

*来源: `src/click/termui.py:745`*

---
<a id="sym-src_click_termui.py-755"></a>
### `edit` · func
装饰器: `@t.overload`
```python
def edit(
    text: str,
    editor: str | None = None,
    env: cabc.Mapping[str, str] | None = None,
    require_save: bool = True,
    extension: str = ".txt",
) -> str | None
```

编辑给定的文本并返回编辑后的文本。

**Parameters:**
- `text` — `str` — 要编辑的文本。
- `editor` — `str | None` — 用于编辑文本的编辑器。如果未指定，则使用默认编辑器。
- `env` — `cabc.Mapping[str, str] | None` — 传递给编辑器的环境变量。
- `require_save` — `bool` — 是否要求编辑器保存更改。
- `extension` — `str` — 保存文件的扩展名。

**Returns:**
- `str | None` — 编辑后的文本，如果未保存更改则返回 `None`。

*来源: `src/click/termui.py:755`*

---
<a id="sym-src_click_termui.py-765"></a>
### `edit` · func
装饰器: `@t.overload`
```python
def edit(
    text: None = None,
    editor: str | None = None,
    env: cabc.Mapping[str, str] | None = None,
    require_save: bool = True,
    extension: str = ".txt",
    filename: str | cabc.Iterable[str] | None = None,
) -> None
```

**用途**: 打开一个文本编辑器来编辑文本或文件。

**Parameters**:
- `text` — `None` — 要编辑的文本内容。
- `editor` — `str | None` — 用于编辑文本的编辑器名称。
- `env` — `cabc.Mapping[str, str] | None` — 传递给编辑器的环境变量。
- `require_save` — `bool` — 是否要求编辑器保存更改。
- `extension` — `str` — 文件的扩展名。
- `filename` — `str | cabc.Iterable[str] | None` — 要编辑的文件名或文件名列表。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/termui.py:765`*

---
<a id="sym-src_click_termui.py-775"></a>
### `edit` · func
```python
def edit(
    text: str | bytes | bytearray | None = None,
    editor: str | None = None,
    env: cabc.Mapping[str, str] | None = None,
    require_save: bool = True,
    extension: str = ".txt",
    filename: str | cabc.Iterable[str] | None = None,
) -> str | bytes | bytearray | None
```

**用途**: 编辑给定的文本或文件，并返回编辑后的文本或文件内容。

**Parameters**:
- `text` — `str | bytes | bytearray | None` — 要编辑的文本。如果提供文件名，则忽略此参数。
- `editor` — `str | None` — 用于编辑文本的编辑器路径。如果未提供，则自动检测。
- `env` — `cabc.Mapping[str, str] | None` — 传递给编辑器的环境变量。
- `require_save` — `bool` — 如果为 `True`，则未保存在编辑器中将使返回值变为 `None`。
- `extension` — `str` — 传递给编辑器的文件扩展名。默认为 `.txt`。
- `filename` — `str | cabc.Iterable[str] | None` — 要编辑的文件名。如果提供，则忽略 `text` 参数。如果编辑器支持一次编辑多个文件，可以传递一个文件名序列。

**Returns**:
- `str | bytes | bytearray | None` — 编辑后的文本或文件内容。如果编辑器未保存更改，则返回 `None`。

**Raises**:
- `UsageError` — 如果无法打开编辑器。

**内部调用(库内):**
- [`Editor`](src_click.md#sym-src_click__termui_impl.py-656) — `Editor` 类用于管理文本编辑器的配置和操作，提供编辑文件和文本的功能。
- [`edit`](src_click.md#sym-src_click_termui.py-745) — 编辑给定的文本内容。
- [`Editor.edit_files`](src_click.md#sym-src_click__termui_impl.py-686) — Open files in the user's editor.

*来源: `src/click/termui.py:775`*

---
<a id="sym-src_click_termui.py-833"></a>
### `launch` · func
```python
def launch(url: str, wait: bool = False, locate: bool = False) -> int
```

This function launches the given URL (or filename) in the default viewer application for this file type. If this is an executable, it might launch the executable in a new session. The return value is the exit code of the launched application. Usually, ``0`` indicates success.

**Parameters**:
- `url` — `str` — URL or filename of the thing to launch.
- `wait` — `bool` — Wait for the program to exit before returning. This only works if the launched program blocks. In particular, ``xdg-open`` on Linux does not block.
- `locate` — `bool` — If this is set to `True` then instead of launching the application associated with the URL it will attempt to launch a file manager with the file located. This might have weird effects if the URL does not point to the filesystem.

**Returns**:
- `int` — The exit code of the launched application.

**内部调用(库内):**
- [`open_url`](src_click.md#sym-src_click__termui_impl.py-772) — 用途: 打开指定 URL 并根据需要等待或定位。

*来源: `src/click/termui.py:833`*

---
<a id="sym-src_click_termui.py-867"></a>
### `getchar` · func
```python
def getchar(echo: bool = False) -> str
```

Fetches a single character from the terminal and returns it.

**Parameters**:
- `echo` — `bool` — if set to `True`, the character read will also show up on the terminal. The default is to not show it.

**Returns**:
- `str` — the character read from the terminal.

**Raises**:
- None

*来源: `src/click/termui.py:867`*

---
<a id="sym-src_click_termui.py-897"></a>
### `raw_terminal` · func
```python
def raw_terminal() -> AbstractContextManager[int]
```

提供一个上下文管理器，用于在终端中以原始模式运行。

**Parameters**:
- 无

**Returns**:
- `AbstractContextManager[int]`: 一个上下文管理器，用于在终端中以原始模式运行。

**Raises**:
- 无

*来源: `src/click/termui.py:897`*

---
<a id="sym-src_click_termui.py-903"></a>
### `pause` · func
```python
def pause(info: str | None = None, err: bool = False) -> None
```

暂停执行并等待用户按下任意键继续。如果程序未通过终端运行，则此命令将不会执行任何操作。

**Parameters**:
- `info` — `str | None` — 在暂停前打印的消息，默认为 `"Press any key to continue..."`。
- `err` — `bool` — 如果设置为 `True`，消息将输出到 `stderr` 而不是 `stdout`，类似于 `echo`。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`getchar`](src_click.md#sym-src_click_termui.py-867) — Fetches a single character from the terminal and returns it.

*来源: `src/click/termui.py:903`*

---

## `src/click/types.py`

<a id="sym-src_click_types.py-37"></a>
### `ParamTypeInfoDict` · class
```python
class ParamTypeInfoDict(t.TypedDict)
```

`ParamTypeInfoDict` 是一个类型字典，用于存储参数类型信息。

| **参数** | **类型** | **含义** |
| --- | --- | --- |
| 无 | 无 | 无 |

**Returns**: 无

**Raises**: 无

*来源: `src/click/types.py:37`*

---
<a id="sym-src_click_types.py-42"></a>
### `ParamType` · class
```python
class ParamType(t.Generic[_ValueT_co], abc.ABC)
```

`ParamType` 是一个抽象基类，用于定义命令行参数的类型。它提供了一系列方法来处理参数的转换、验证和提示信息。

### 方法

- **to_info_dict(self) -> ParamTypeInfoDict**
  - **返回**: `ParamTypeInfoDict` — 参数类型的信息字典。
  - **用途**: 返回一个包含参数类型信息的字典，用于生成帮助信息。

- **__call__(self, value: t.Any, param: Parameter | None = None, ctx: Context | None = None) -> _ValueT_co | None**
  - **参数**:
    - `value` — `t.Any` — 传入的参数值。
    - `param` — `Parameter | None` — 参数对象，可选。
    - `ctx` — `Context | None` — 上下文对象，可选。
  - **返回**: `_ValueT_co | None` — 转换后的参数值，如果转换失败则返回 `None`。
  - **用途**: 将传入的参数值转换为指定类型，如果转换失败则返回 `None`。

- **get_metavar(self, param: Parameter, ctx: Context) -> str | None**
  - **参数**:
    - `param` — `Parameter` — 参数对象。
    - `ctx` — `Context` — 上下文对象。
  - **返回**: `str | None` — 参数的元变量字符串，用于显示在帮助信息中。
  - **

*来源: `src/click/types.py:42`*

---
<a id="sym-src_click_types.py-80"></a>
### `ParamType.to_info_dict` · method
```python
def to_info_dict(self) -> ParamTypeInfoDict
```

Gather information that could be useful for a tool generating user-facing documentation.

**Parameters**:
- `self` — `ParamType` — The instance of the parameter type.

**Returns**:
- `ParamTypeInfoDict` — A dictionary containing information about the parameter type, including its type and name.

**Raises**:
- None

*来源: `src/click/types.py:80`*

---
<a id="sym-src_click_types.py-101"></a>
### `ParamType.__call__` · method
```python
def __call__(
        self,
        value: t.Any,
        param: Parameter | None = None,
        ctx: Context | None = None,
    ) -> _ValueT_co | None
```

### 用途
`ParamType.__call__` 方法用于将输入值转换为特定类型，并在转换失败时返回 `None`。

### Parameters
- `value` — `t.Any` — 输入值，需要转换为特定类型。
- `param` — `Parameter | None` — 与输入值相关的参数对象，可选。
- `ctx` — `Context | None` — 当前命令上下文对象，可选。

### Returns
- `_ValueT_co | None` — 转换后的值，如果转换失败则返回 `None`。

### Raises
- 无

**内部调用(库内):**
- [`ParamType.convert`](src_click.md#sym-src_click_types.py-121) — Converts the value to the correct type. This method is not called if the value i

*来源: `src/click/types.py:101`*

---
<a id="sym-src_click_types.py-111"></a>
### `ParamType.get_metavar` · method
```python
def get_metavar(self, param: Parameter, ctx: Context) -> str | None
```

Returns the metavar default for a parameter if it provides one.

**Parameters**:
- param — Parameter — The parameter to get the metavar for.
- ctx — Context — The context in which the parameter is being used.

**Returns**:
- str | None — The metavar default for the parameter, or None if it does not provide one.

*来源: `src/click/types.py:111`*

---
<a id="sym-src_click_types.py-114"></a>
### `ParamType.get_missing_message` · method
```python
def get_missing_message(self, param: Parameter, ctx: Context | None) -> str | None
```

Optionally returns extra information about a missing parameter.

**Parameters**:
- `param` — `Parameter` — The parameter that is missing.
- `ctx` — `Context | None` — The context in which the parameter is missing.

**Returns**:
- `str | None` — Extra information about the missing parameter, or `None` if no extra information is available.

*来源: `src/click/types.py:114`*

---
<a id="sym-src_click_types.py-121"></a>
### `ParamType.convert` · method
```python
def convert(
        self, value: t.Any, param: Parameter | None, ctx: Context | None
    ) -> _ValueT_co
```

Converts the value to the correct type. This method is not called if the value is `None` (the missing value).

**Parameters**:
- `value` — `t.Any` — The value to convert.
- `param` — `Parameter | None` — The parameter that is using this type to convert its value. May be `None`.
- `ctx` — `Context | None` — The current context that arrived at this value. May be `None`.

**Returns**:
- `_ValueT_co` — The converted value.

**Raises**:
- None

*来源: `src/click/types.py:121`*

---
<a id="sym-src_click_types.py-147"></a>
### `ParamType.split_envvar_value` · method
```python
def split_envvar_value(self, rv: str) -> cabc.Sequence[str]
```

Given a value from an environment variable, this method splits it into small chunks based on the defined envvar list splitter.

**Parameters**:
- `rv` — `str` — The value from an environment variable.

**Returns**:
- `cabc.Sequence[str]` — The value split into chunks.

**Raises**:
- None

*来源: `src/click/types.py:147`*

---
<a id="sym-src_click_types.py-157"></a>
### `ParamType.fail` · method
```python
def fail(
        self,
        message: str,
        param: Parameter | None = None,
        ctx: Context | None = None,
    ) -> t.NoReturn
```

**用途**: Helper method to fail with an invalid value message.

**Parameters**:
- `message` — `str` — The error message to display.
- `param` — `Parameter | None` — The parameter that caused the failure (optional).
- `ctx` — `Context | None` — The context in which the failure occurred (optional).

**Returns**:
- `t.NoReturn` — This method does not return.

**Raises**:
- `BadParameter` — Raises a `BadParameter` exception with the provided message, context, and parameter.

**内部调用(库内):**
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `src/click/types.py:157`*

---
<a id="sym-src_click_types.py-166"></a>
### `ParamType.shell_complete` · method
```python
def shell_complete(
        self, ctx: Context, param: Parameter, incomplete: str
    ) -> list[CompletionItem]
```

**用途**: Return a list of `click.shell_completion.CompletionItem` objects for the incomplete value.

**Parameters**:
- `ctx` — `Context` — Invocation context for this command.
- `param` — `Parameter` — The parameter that is requesting completion.
- `incomplete` — `str` — Value being completed. May be empty.

**Returns**:
- `list[CompletionItem]` — A list of completion items.

**Raises**:
- None

*来源: `src/click/types.py:166`*

---
<a id="sym-src_click_types.py-184"></a>
### `CompositeParamType` · class
```python
class CompositeParamType(ParamType[_ValueT_co])
```

`CompositeParamType` 类用于表示由多个参数类型组合而成的参数类型。

- **arity(self) -> int**
  - **Parameters**:
    - `self` — `CompositeParamType` — 实例本身。
  - **Returns**:
    - `int` — 组合参数类型的数量。
  - **Raises**:
    - 无

*来源: `src/click/types.py:184`*

---
<a id="sym-src_click_types.py-189"></a>
### `CompositeParamType.arity` · method
装饰器: `@property` `@abc.abstractmethod`
```python
def arity(self) -> int
```

用途: 返回参数类型的元组长度。

**Parameters**:
- 无

**Returns**:
- `int`: 参数类型的元组长度。

**Raises**:
- 无

*来源: `src/click/types.py:189`*

---
<a id="sym-src_click_types.py-195"></a>
### `FuncParamTypeInfoDict` · class
```python
class FuncParamTypeInfoDict(
        ParamTypeInfoDict,
        t.Generic[_ValueT_contra, _ValueT_co],
    )
```

`FuncParamTypeInfoDict` 是一个泛型类，用于存储和管理函数参数类型信息。

| 参数名 | 类型 | 含义 |
| --- | --- | --- |
| _ValueT_contra | 类型 | 逆变类型参数 |
| _ValueT_co | 类型 | 协变类型参数 |

这个类继承自 `ParamTypeInfoDict`，并使用泛型来处理不同类型的参数信息。

*来源: `src/click/types.py:195`*

---
<a id="sym-src_click_types.py-202"></a>
### `FuncParamTypeInfoDict` · class
```python
class FuncParamTypeInfoDict(ParamTypeInfoDict)
```

`FuncParamTypeInfoDict` 是一个用于存储函数参数类型信息的字典类，继承自 `ParamTypeInfoDict`。

| **Parameters** | **Type** | **Meaning** |
| --- | --- | --- |
| 无 | 无 | 无 |

| **Returns** | **Meaning** |
| --- | --- |
| 无 | 无 |

| **Raises** | **Meaning** |
| --- | --- |
| 无 | 无 |

这个类主要用于存储和管理函数参数的类型信息，可以用于在命令行工具中处理参数类型。

*来源: `src/click/types.py:202`*

---
<a id="sym-src_click_types.py-206"></a>
### `FuncParamType` · class
```python
class FuncParamType(ParamType[_ValueT_co], t.Generic[_ValueT_contra, _ValueT_co])
```

`FuncParamType` 类用于将一个函数转换为参数类型，以便在命令行参数中使用。

- **Parameters**:
  - `func` — `Callable[[_ValueT_contra], _ValueT_co]` — 一个函数，该函数接受一个参数并返回一个值。
- **Returns**:
  - `FuncParamTypeInfoDict[_ValueT_contra, _ValueT_co]` — 一个字典，包含函数参数类型的信息。
- **Raises**:
  - 无

*来源: `src/click/types.py:206`*

---
<a id="sym-src_click_types.py-210"></a>
### `FuncParamType.__init__` · method
```python
def __init__(self, func: t.Callable[[_ValueT_contra], _ValueT_co]) -> None
```

### `FuncParamType.__init__`

初始化一个 `FuncParamType` 对象，用于包装一个函数。

**Parameters:**
- `func` — `t.Callable[[_ValueT_contra], _ValueT_co]` — 要包装的函数。

**Returns:**
- `None`

*来源: `src/click/types.py:210`*

---
<a id="sym-src_click_types.py-214"></a>
### `FuncParamType.to_info_dict` · method
```python
def to_info_dict(self) -> FuncParamTypeInfoDict[_ValueT_contra, _ValueT_co]
```

将参数类型转换为信息字典。

**Parameters**:
- `self` — `FuncParamType` — 当前实例。

**Returns**:
- `FuncParamTypeInfoDict[_ValueT_contra, _ValueT_co]` — 包含函数和父类信息的字典。

**Raises**:
- 无

*来源: `src/click/types.py:214`*

---
<a id="sym-src_click_types.py-217"></a>
### `FuncParamType.convert` · method
```python
def convert(
        self, value: _ValueT_contra, param: Parameter | None, ctx: Context | None
    ) -> _ValueT_co
```

Converts the value using the provided function.

**Parameters**:
- `value` — `_ValueT_contra` — The value to convert.
- `param` — `Parameter | None` — The parameter being converted.
- `ctx` — `Context | None` — The context in which the conversion is taking place.

**Returns**:
- `_ValueT_co` — The converted value.

**Raises**:
- `BadParameter` — If the conversion fails.

**内部调用(库内):**
- [`func`](src_click.md#sym-src_click__compat.py-549) — func
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.

*来源: `src/click/types.py:217`*

---
<a id="sym-src_click_types.py-234"></a>
### `UnprocessedParamType` · class
```python
class UnprocessedParamType(ParamType[t.Any])
```

`UnprocessedParamType` 是一个 Click 参数类型，用于表示未处理的参数值，直接返回传入的值。

- **Parameters**:
  - `value` — `_ValueT` — 传入的参数值。
  - `param` — `Parameter | None` — 当前参数对象，可选。
  - `ctx` — `Context | None` — 当前上下文对象，可选。

- **Returns**:
  - `_ValueT` — 返回传入的参数值。

- **Raises**:
  - 无

*来源: `src/click/types.py:234`*

---
<a id="sym-src_click_types.py-237"></a>
### `UnprocessedParamType.convert` · method
```python
def convert(
        self, value: _ValueT, param: Parameter | None, ctx: Context | None
    ) -> _ValueT
```

###用途
UnprocessedParamType 类的 convert 方法用于将传入的值进行转换，但在此实现中直接返回原始值。

###Parameters
- value — _ValueT — 需要转换的值。
- param — Parameter | None — 当前参数对象，可选。
- ctx — Context | None — 当前上下文对象，可选。

###Returns
- _ValueT — 返回原始传入的值。

*来源: `src/click/types.py:237`*

---
<a id="sym-src_click_types.py-242"></a>
### `UnprocessedParamType.__repr__` · method
```python
def __repr__(self) -> str
```

返回一个表示未处理参数类型的字符串。

**Returns**:
- `str`: 表示未处理参数类型的字符串 "UNPROCESSED"。

*来源: `src/click/types.py:242`*

---
<a id="sym-src_click_types.py-246"></a>
### `StringParamType` · class
```python
class StringParamType(ParamType[str])
```

`StringParamType` 是一个 Click 参数类型，用于将输入值转换为字符串。

- **Parameters**:
  - `value` — `t.Any` — 用户提供的输入值。
  - `param` — `Parameter | None` — 当前参数对象，如果有的话。
  - `ctx` — `Context | None` — 当前上下文对象，如果有的话。

- **Returns**:
  - `str` — 转换后的字符串值。

- **Raises**:
  - `UsageError` — 如果输入值无法转换为字符串。

*来源: `src/click/types.py:246`*

---
<a id="sym-src_click_types.py-249"></a>
### `StringParamType.convert` · method
```python
def convert(
        self, value: t.Any, param: Parameter | None, ctx: Context | None
    ) -> str
```

将输入值转换为字符串。

**Parameters**:
- `value` — `t.Any` — 要转换的值。
- `param` — `Parameter | None` — 相关的参数对象，如果有的话。
- `ctx` — `Context | None` — 相关的上下文对象，如果有的话。

**Returns**:
- `str` — 转换后的字符串。

**Raises**:
- `UnicodeError` — 如果解码过程中发生 Unicode 错误。

*来源: `src/click/types.py:249`*

---
<a id="sym-src_click_types.py-267"></a>
### `StringParamType.__repr__` · method
```python
def __repr__(self) -> str
```

返回字符串 "STRING"。

**Returns**:
- `str`: 字符串 "STRING"

*来源: `src/click/types.py:267`*

---
<a id="sym-src_click_types.py-274"></a>
### `ChoiceInfoDict` · class
```python
class ChoiceInfoDict(ParamTypeInfoDict, t.Generic[_ValueT_co])
```

`ChoiceInfoDict` 类是一个泛型字典类型，用于存储和管理命令行参数的选项信息。

### Parameters
- `_ValueT_co` — `t.Generic` — 表示泛型类型参数 `_ValueT_co`，表示值的类型。

### Returns
- `ParamTypeInfoDict` — 表示该类继承自 `ParamTypeInfoDict`，用于存储参数类型信息。

### Raises
- 无

*来源: `src/click/types.py:274`*

---
<a id="sym-src_click_types.py-279"></a>
### `ChoiceInfoDict` · class
```python
class ChoiceInfoDict(ParamTypeInfoDict)
```

`ChoiceInfoDict` 是一个用于存储和管理选项信息的字典类，通常用于 Click 命令行工具中定义选项的可能值及其描述。

**Parameters**:
- 无

**Returns**:
- `ChoiceInfoDict` — 一个字典，键为选项值，值为选项的描述信息。

**Raises**:
- 无

*来源: `src/click/types.py:279`*

---
<a id="sym-src_click_types.py-284"></a>
### `Choice` · class
```python
class Choice(ParamType[_ValueT_co], t.Generic[_ValueT_co])
```

`Choice` 类用于定义一个参数类型，该参数类型只能接受预定义的选项之一。

### 方法

- **__init__(self, choices: cabc.Iterable[_ValueT_co], case_sensitive: bool = True) -> None**
  - **Parameters**:
    - `choices` — `cabc.Iterable[_ValueT_co]` — 预定义选项的集合。
    - `case_sensitive` — `bool` — 是否区分大小写，默认为 `True`。
  - **Returns**: `None`

- **to_info_dict(self) -> ChoiceInfoDict[_ValueT_co]**
  - **Returns**:
    - `ChoiceInfoDict[_ValueT_co]` — 包含选项信息的字典。

- **_normalized_mapping(self, ctx: Context | None = None) -> cabc.Mapping[_ValueT_co, str]**
  - **Parameters**:
    - `ctx` — `Context | None` — 上下文对象，可选。
  - **Returns**:
    - `cabc.Mapping[_ValueT_co, str]` — 归一化后的选项映射。

- **normalize_choice(self, choice: object, ctx: Context | None) -> str**
  - **Parameters**:
    - `choice` — `object` — 选项值。
    - `ctx` — `Context | None` — 上下文对象，可选。
  - **Returns**:
    - `str` — 归一化后的选项字符串。

*来源: `src/click/types.py:284`*

---
<a id="sym-src_click_types.py-317"></a>
### `Choice.__init__` · method
```python
def __init__(
        self, choices: cabc.Iterable[_ValueT_co], case_sensitive: bool = True
    ) -> None
```

### Choice.__init__
初始化一个 `Choice` 对象，用于验证输入是否在给定的选项列表中。

**Parameters:**
- `choices` — `cabc.Iterable[_ValueT_co]` — 可迭代对象，包含允许的选项。
- `case_sensitive` — `bool` — 是否区分大小写，默认为 `True`。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/types.py:317`*

---
<a id="sym-src_click_types.py-323"></a>
### `Choice.to_info_dict` · method
```python
def to_info_dict(self) -> ChoiceInfoDict[_ValueT_co]
```

将 Choice 对象转换为信息字典。

**Parameters**:
- 无

**Returns**:
- `ChoiceInfoDict[_ValueT_co]`: 包含 Choice 对象信息的字典。

**Raises**:
- 无

*来源: `src/click/types.py:323`*

---
<a id="sym-src_click_types.py-330"></a>
### `Choice._normalized_mapping` · method
```python
def _normalized_mapping(
        self, ctx: Context | None = None
    ) -> cabc.Mapping[_ValueT_co, str]
```

Returns a mapping where keys are the original choices and the values are the normalized values that are accepted via the command line.

**Parameters**:
- `ctx` — `Context | None` — The context object for the command, or `None` if not available.

**Returns**:
- `Mapping[_ValueT_co, str]` — A dictionary mapping original choices to their normalized values.

**Raises**:
- None

**内部调用(库内):**
- [`Choice.normalize_choice`](src_click.md#sym-src_click_types.py-348) — **用途**: Normalize a choice value, used to map a passed string to a choice. Each 

*来源: `src/click/types.py:330`*

---
<a id="sym-src_click_types.py-348"></a>
### `Choice.normalize_choice` · method
```python
def normalize_choice(self, choice: object, ctx: Context | None) -> str
```

**用途**: Normalize a choice value, used to map a passed string to a choice. Each choice must have a unique normalized value.

**Parameters**:
- `choice` — `object` — The choice value to be normalized.
- `ctx` — `Context | None` — The context object, which may contain a normalization function.

**Returns**:
- `str` — The normalized choice value.

**Raises**:
- None

*来源: `src/click/types.py:348`*

---
<a id="sym-src_click_types.py-368"></a>
### `Choice.get_metavar` · method
```python
def get_metavar(self, param: Parameter, ctx: Context) -> str | None
```

### `Choice.get_metavar`

Returns a string representing the metavar for the given parameter, formatted with choices from the `Choice` object. If the parameter is required and of type "argument", it is enclosed in curly braces; otherwise, in square braces.

**Parameters:**

- `param` — `Parameter` — The parameter for which to get the metavar.
- `ctx` — `Context` — The context in which the parameter is being processed.

**Returns:**

- `str | None` — The formatted metavar string or `None` if no choices are available.

**内部调用(库内):**
- [`convert_type`](src_click.md#sym-src_click_types.py-1284) — Converts a type to a `StringParamType`.
- [`Choice._normalized_mapping`](src_click.md#sym-src_click_types.py-330) — Returns a mapping where keys are the original choices and the values are the nor

*来源: `src/click/types.py:368`*

---
<a id="sym-src_click_types.py-386"></a>
### `Choice.get_missing_message` · method
```python
def get_missing_message(self, param: Parameter, ctx: Context | None) -> str
```

**用途**: 返回当没有选择传递时显示的消息。

**Parameters**:
- `param` — `Parameter` — 传递的参数。
- `ctx` — `Context | None` — 上下文对象，可选。

**Returns**:
- `str` — 显示的消息。

**Raises**:
- 无

**内部调用(库内):**
- [`Choice._normalized_mapping`](src_click.md#sym-src_click_types.py-330) — Returns a mapping where keys are the original choices and the values are the nor

*来源: `src/click/types.py:386`*

---
<a id="sym-src_click_types.py-396"></a>
### `Choice.convert` · method
```python
def convert(
        self, value: t.Any, param: Parameter | None, ctx: Context | None
    ) -> _ValueT_co
```

### Choice.convert

Converts a given value from the parser to its corresponding normalized value in the list of choices. If the value does not match any choice, raises a `BadParameter` exception.

**Parameters**:
- `value` — `t.Any` — The value to convert.
- `param` — `Parameter | None` — The parameter object.
- `ctx` — `Context | None` — The context object.

**Returns**:
- `_ValueT_co` — The corresponding "original" choice.

**Raises**:
- `BadParameter` — If the value does not match any choice.

**内部调用(库内):**
- [`Choice.normalize_choice`](src_click.md#sym-src_click_types.py-348) — **用途**: Normalize a choice value, used to map a passed string to a choice. Each 
- [`Choice._normalized_mapping`](src_click.md#sym-src_click_types.py-330) — Returns a mapping where keys are the original choices and the values are the nor
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.
- [`Choice.get_invalid_choice_message`](src_click.md#sym-src_click_types.py-420) — 用途

*来源: `src/click/types.py:396`*

---
<a id="sym-src_click_types.py-420"></a>
### `Choice.get_invalid_choice_message` · method
```python
def get_invalid_choice_message(self, value: t.Any, ctx: Context | None) -> str
```

### 用途
获取给定值无效时的错误消息。

### Parameters
- `value` — `t.Any` — 无效的值。
- `ctx` — `Context | None` — 上下文对象，可选。

### Returns
- `str` — 错误消息。

### Raises
- 无

**内部调用(库内):**
- [`Choice._normalized_mapping`](src_click.md#sym-src_click_types.py-330) — Returns a mapping where keys are the original choices and the values are the nor

*来源: `src/click/types.py:420`*

---
<a id="sym-src_click_types.py-434"></a>
### `Choice.__repr__` · method
```python
def __repr__(self) -> str
```

用途: 返回 Choice 对象的字符串表示。

**Parameters**:
- 无

**Returns**:
- `str`: Choice 对象的字符串表示，格式为 "Choice([choices])"，其中 choices 是一个包含所有选项的列表。

**Raises**:
- 无

*来源: `src/click/types.py:434`*

---
<a id="sym-src_click_types.py-437"></a>
### `Choice.shell_complete` · method
```python
def shell_complete(
        self, ctx: Context, param: Parameter, incomplete: str
    ) -> list[CompletionItem]
```

**用途**: 提供命令行 shell 自动补全功能，根据当前输入的不完整值匹配并返回可能的补全项。

**Parameters**:
- `ctx` — `Context` — 命令的调用上下文。
- `param` — `Parameter` — 请求补全的参数。
- `incomplete` — `str` — 正在补全的值，可能为空。

**Returns**:
- `list[CompletionItem]` — 匹配的补全项列表。

**Raises**:
- 无

**内部调用(库内):**
- [`Choice.normalize_choice`](src_click.md#sym-src_click_types.py-348) — **用途**: Normalize a choice value, used to map a passed string to a choice. Each 
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。

*来源: `src/click/types.py:437`*

---
<a id="sym-src_click_types.py-460"></a>
### `DateTimeInfoDict` · class
```python
class DateTimeInfoDict(ParamTypeInfoDict)
```

`DateTimeInfoDict` 类继承自 `ParamTypeInfoDict`，用于处理日期时间类型的参数信息。

- **Parameters**:
  - 无参数。

- **Returns**:
  - `ParamTypeInfoDict` — 一个字典，用于存储日期时间类型的参数信息。

- **Raises**:
  - 无异常。

*来源: `src/click/types.py:460`*

---
<a id="sym-src_click_types.py-464"></a>
### `DateTime` · class
```python
class DateTime(ParamType[datetime])
```

`DateTime` 类用于处理日期时间参数，支持多种日期时间格式。

### Parameters
- `formats` — `cabc.Sequence[str] | None` — 日期时间格式列表，可选。

### Returns
- `DateTimeInfoDict` — 日期时间信息字典。

### Raises
- `ValueError` — 如果无法将输入值转换为日期时间。

### Methods
- `__init__(self, formats: cabc.Sequence[str] | None = None)` — 初始化 `DateTime` 对象，设置支持的日期时间格式。
- `to_info_dict(self) -> DateTimeInfoDict` — 返回日期时间信息字典。
- `get_metavar(self, param: Parameter, ctx: Context) -> str` — 获取参数的元变量字符串。
- `_try_to_convert_date(self, value: t.Any, format: str) -> datetime | None` — 尝试将输入值转换为日期时间，返回转换后的日期时间对象或 `None`。
- `convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> datetime` — 将输入值转换为日期时间，如果转换失败则抛出 `ValueError`。
- `__repr__(self) -> str` — 返回对象的字符串表示。

*来源: `src/click/types.py:464`*

---
<a id="sym-src_click_types.py-489"></a>
### `DateTime.__init__` · method
```python
def __init__(self, formats: cabc.Sequence[str] | None = None)
```

初始化 `DateTime` 对象，设置日期时间格式。

**Parameters**:
- formats — `cabc.Sequence[str] | None` — 日期时间格式字符串序列，可选。默认值为 `["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]`。

**Returns**:
- `None` — 无返回值。

**Raises**:
- 无

*来源: `src/click/types.py:489`*

---
<a id="sym-src_click_types.py-496"></a>
### `DateTime.to_info_dict` · method
```python
def to_info_dict(self) -> DateTimeInfoDict
```

将 `DateTime` 对象转换为包含格式信息的字典。

**Parameters**:
- 无

**Returns**:
- `DateTimeInfoDict` — 包含格式信息的字典。

**Raises**:
- 无

*来源: `src/click/types.py:496`*

---
<a id="sym-src_click_types.py-499"></a>
### `DateTime.get_metavar` · method
```python
def get_metavar(self, param: Parameter, ctx: Context) -> str
```

### `DateTime.get_metavar`

Returns a string representing the metavar for the given parameter, formatted according to the specified formats.

*来源: `src/click/types.py:499`*

---
<a id="sym-src_click_types.py-502"></a>
### `DateTime._try_to_convert_date` · method
```python
def _try_to_convert_date(self, value: t.Any, format: str) -> datetime | None
```

尝试将给定的值按指定格式转换为日期时间对象。

**Parameters**:
- `value` — `t.Any` — 要转换的值。
- `format` — `str` — 日期时间格式字符串。

**Returns**:
- `datetime | None` — 成功转换的日期时间对象，否则返回 `None`。

**Raises**:
- 无

*来源: `src/click/types.py:502`*

---
<a id="sym-src_click_types.py-508"></a>
### `DateTime.convert` · method
```python
def convert(
        self, value: t.Any, param: Parameter | None, ctx: Context | None
    ) -> datetime
```

将输入值转换为 `datetime` 对象。

**Parameters**:
- `value` — `t.Any` — 要转换的值。
- `param` — `Parameter | None` — 当前参数。
- `ctx` — `Context | None` — 当前上下文。

**Returns**:
- `datetime` — 转换后的 `datetime` 对象。

**Raises**:
- `BadParameter` — 如果值不匹配任何格式。

**内部调用(库内):**
- [`DateTime._try_to_convert_date`](src_click.md#sym-src_click_types.py-502) — 尝试将给定的值按指定格式转换为日期时间对象。
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.

*来源: `src/click/types.py:508`*

---
<a id="sym-src_click_types.py-531"></a>
### `DateTime.__repr__` · method
```python
def __repr__(self) -> str
```

用途: 返回一个表示 `DateTime` 类的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 返回字符串 "DateTime"。

**Raises**:
- 无

*来源: `src/click/types.py:531`*

---
<a id="sym-src_click_types.py-535"></a>
### `_NumberParamTypeBase` · class
```python
class _NumberParamTypeBase(
    ParamType[_ValueT_co], t.Generic[_ValueT_contra, _ValueT_co]
)
```

`_NumberParamTypeBase` 是一个基类，用于处理数字类型的参数转换。

- **Parameters**:
  - `value` — `_ValueT_contra` — 要转换的值。
  - `param` — `Parameter | None` — 相关的参数对象。
  - `ctx` — `Context | None` — 当前的上下文对象。

- **Returns**:
  - `_ValueT_co` — 转换后的值。

- **Raises**:
  - `ValueError` — 如果值无法转换为数字类型。

*来源: `src/click/types.py:535`*

---
<a id="sym-src_click_types.py-540"></a>
### `_NumberParamTypeBase.convert` · method
```python
def convert(
        self, value: _ValueT_contra, param: Parameter | None, ctx: Context | None
    ) -> _ValueT_co
```

Converts the input value to a number of a specific type.

**Parameters**:
- `value` — `_ValueT_contra` — The value to convert.
- `param` — `Parameter | None` — The parameter object, if available.
- `ctx` — `Context | None` — The context object, if available.

**Returns**:
- `_ValueT_co` — The converted value.

**Raises**:
- `BadParameter` — If the value cannot be converted to the specified number type.

**内部调用(库内):**
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.

*来源: `src/click/types.py:540`*

---
<a id="sym-src_click_types.py-558"></a>
### `NumberRangeInfoDict` · class
```python
class NumberRangeInfoDict(ParamTypeInfoDict, t.Generic[_FloatValueT_co])
```

`NumberRangeInfoDict` 是一个泛型类，用于存储和管理数值范围信息。它继承自 `ParamTypeInfoDict`，并使用泛型参数 `_FloatValueT_co` 来表示数值类型。

### Parameters
- `_FloatValueT_co` — `t.Generic` — 表示数值类型，通常是浮点数类型。

### Returns
- 无返回值。

### Raises
- 无异常抛出。

*来源: `src/click/types.py:558`*

---
<a id="sym-src_click_types.py-566"></a>
### `NumberRangeInfoDict` · class
```python
class NumberRangeInfoDict(ParamTypeInfoDict)
```

`NumberRangeInfoDict` 是 Click 库中用于存储和处理数字范围参数信息的字典类。

**Parameters:**
- 无

**Returns:**
- `NumberRangeInfoDict` — 一个字典对象，用于存储和处理数字范围参数信息。

**Raises:**
- 无

*来源: `src/click/types.py:566`*

---
<a id="sym-src_click_types.py-574"></a>
### `_NumberRangeBase` · class
```python
class _NumberRangeBase(
    _NumberParamTypeBase[_ValueT_contra, _FloatValueT_co],
    t.Generic[_ValueT_contra, _FloatValueT_co],
)
```

`_NumberRangeBase` 是一个基类，用于定义数值范围的参数类型，支持最小值、最大值以及开区间和闭区间的选择。

### 方法

- **__init__**
  - **Parameters**:
    - `min` — `_FloatValueT_co | None` — 范围的最小值，如果为 `None`，则没有最小值限制。
    - `max` — `_FloatValueT_co | None` — 范围的最大值，如果为 `None`，则没有最大值限制。
    - `min_open` — `bool` — 是否允许最小值（默认为 `False`）。
    - `max_open` — `bool` — 是否允许最大值（默认为 `False`）。
    - `clamp` — `bool` — 是否将值限制在范围内（默认为 `False`）。
  - **Returns**: `None`

- **to_info_dict**
  - **Returns**: `NumberRangeInfoDict[_FloatValueT_co]` — 返回一个包含范围信息的字典。

- **convert**
  - **Parameters**:
    - `value` — `_ValueT_contra` — 要转换的值。
    - `param` — `Parameter | None` — 参数对象，如果为 `None`，则没有参数上下文。
    - `ctx` — `Context | None` — 上下文对象，如果为 `None`，则没有上下文信息。
  - **Returns**: `_

*来源: `src/click/types.py:574`*

---
<a id="sym-src_click_types.py-584"></a>
### `_NumberRangeBase.__init__` · method
```python
def __init__(
        self,
        min: _FloatValueT_co | None = None,
        max: _FloatValueT_co | None = None,
        min_open: bool = False,
        max_open: bool = False,
        clamp: bool = False,
    ) -> None
```

初始化一个数值范围对象。

**Parameters**:
- `min` — `_FloatValueT_co | None` — 范围的最小值，如果为 `None`，则没有最小值限制。
- `max` — `_FloatValueT_co | None` — 范围的最大值，如果为 `None`，则没有最大值限制。
- `min_open` — `bool` — 是否允许最小值在范围内（开区间）。
- `max_open` — `bool` — 是否允许最大值在范围内（开区间）。
- `clamp` — `bool` — 是否将输入值限制在范围内。

**Returns**:
- `None`

*来源: `src/click/types.py:584`*

---
<a id="sym-src_click_types.py-598"></a>
### `_NumberRangeBase.to_info_dict` · method
```python
def to_info_dict(self) -> NumberRangeInfoDict[_FloatValueT_co]
```

将数字范围参数转换为信息字典。

**Parameters**:
- 无

**Returns**:
- `NumberRangeInfoDict[_FloatValueT_co]`: 包含数字范围参数信息的字典。

**Raises**:
- 无

*来源: `src/click/types.py:598`*

---
<a id="sym-src_click_types.py-608"></a>
### `_NumberRangeBase.convert` · method
```python
def convert(
        self, value: _ValueT_contra, param: Parameter | None, ctx: Context | None
    ) -> _FloatValueT_co
```

Converts the value to a float and checks if it falls within the specified range.

**Parameters**:
- `value` — `_ValueT_contra` — The value to convert.
- `param` — `Parameter | None` — The parameter object.
- `ctx` — `Context | None` — The context object.

**Returns**:
- `_FloatValueT_co` — The converted value.

**Raises**:
- `BadParameter` — If the value is not within the specified range.

**内部调用(库内):**
- [`_NumberRangeBase._clamp`](src_click.md#sym-src_click_types.py-642) — 用途: 找到在给定方向上将要被 clamped 的有效值。
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.
- [`_NumberRangeBase._describe_range`](src_click.md#sym-src_click_types.py-659) — **用途**: 生成用于帮助文本的范围描述。

*来源: `src/click/types.py:608`*

---
<a id="sym-src_click_types.py-642"></a>
### `_NumberRangeBase._clamp` · method
装饰器: `@abc.abstractmethod`
```python
def _clamp(
        # Covariant type variables cannot be used in input positions, so we use a
        # separate method-scoped type variable instead.
        self: _NumberRangeBase[t.Any, _FloatValueT],
        bound: _FloatValueT,
        dir: t.Literal[1, -1],
        open: bool,
    ) -> _FloatValueT
```

用途: 找到在给定方向上将要被 clamped 的有效值。

**Parameters**:
- `bound` — `_FloatValueT` — 边界值。
- `dir` — `t.Literal[1, -1]` — 1 或 -1，表示移动的方向。
- `open` — `bool` — 如果为真，范围不包括边界。

**Returns**:
- `_FloatValueT` — 在给定方向上将要被 clamped 的有效值。

*来源: `src/click/types.py:642`*

---
<a id="sym-src_click_types.py-659"></a>
### `_NumberRangeBase._describe_range` · method
```python
def _describe_range(self) -> str
```

**用途**: 生成用于帮助文本的范围描述。

**Parameters**:
- 无

**Returns**:
- `str`: 用于帮助文本的范围描述。

**Raises**:
- 无

*来源: `src/click/types.py:659`*

---
<a id="sym-src_click_types.py-673"></a>
### `_NumberRangeBase.__repr__` · method
```python
def __repr__(self) -> str
```

**用途**: 返回一个描述当前 `_NumberRangeBase` 实例的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 描述当前 `_NumberRangeBase` 实例的字符串。

**Raises**:
- 无

**内部调用(库内):**
- [`_NumberRangeBase._describe_range`](src_click.md#sym-src_click_types.py-659) — **用途**: 生成用于帮助文本的范围描述。

*来源: `src/click/types.py:673`*

---
<a id="sym-src_click_types.py-678"></a>
### `IntParamType` · class
```python
class IntParamType(_NumberParamTypeBase[t.SupportsInt | t.SupportsIndex, int])
```

`IntParamType` 类用于处理整数类型的参数。

- **Parameters**:
  - `self` — `IntParamType` — 实例本身。

- **Returns**:
  - `str` — 返回类的字符串表示。

- **Raises**:
  - 无

*来源: `src/click/types.py:678`*

---
<a id="sym-src_click_types.py-682"></a>
### `IntParamType.__repr__` · method
```python
def __repr__(self) -> str
```

返回表示整数参数类型的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 表示整数参数类型的字符串 "INT"。

**Raises**:
- 无

*来源: `src/click/types.py:682`*

---
<a id="sym-src_click_types.py-686"></a>
### `IntRange` · class
```python
class IntRange(_NumberRangeBase[int, int], IntParamType)
```

`IntRange` 类用于定义一个整数范围参数类型，限制输入值在指定的整数范围内。

### 方法

- **_clamp(self, bound: int, dir: t.Literal[1, -1], open: bool) -> int**
  - **Parameters**:
    - `bound` — `int` — 边界值。
    - `dir` — `t.Literal[1, -1]` — 方向，1 表示向上，-1 表示向下。
    - `open` — `bool` — 是否开放边界。
  - **Returns**:
    - `int` — 调整后的值。
  - **Raises**:
    - 无

*来源: `src/click/types.py:686`*

---
<a id="sym-src_click_types.py-703"></a>
### `IntRange._clamp` · method
```python
def _clamp(self, bound: int, dir: t.Literal[1, -1], open: bool) -> int
```

Clamp a value within a range based on a direction and whether the range is open.

**Parameters**:
- `bound` — `int` — The boundary value.
- `dir` — `t.Literal[1, -1]` — The direction to clamp towards (1 for up, -1 for down).
- `open` — `bool` — Whether the range is open.

**Returns**:
- `int` — The clamped value.

*来源: `src/click/types.py:703`*

---
<a id="sym-src_click_types.py-710"></a>
### `FloatParamType` · class
```python
class FloatParamType(_NumberParamTypeBase[t.SupportsFloat | t.SupportsIndex, float])
```

`FloatParamType` 类用于处理浮点数参数，确保输入值可以被转换为浮点数。

- **Parameters**:
  - `self` — `FloatParamType` — 实例本身。

- **Returns**:
  - `str` — 类的字符串表示。

- **Raises**:
  - 无

*来源: `src/click/types.py:710`*

---
<a id="sym-src_click_types.py-714"></a>
### `FloatParamType.__repr__` · method
```python
def __repr__(self) -> str
```

返回一个表示 `FloatParamType` 类型的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 表示 `FloatParamType` 类型的字符串 "FLOAT"

*来源: `src/click/types.py:714`*

---
<a id="sym-src_click_types.py-718"></a>
### `FloatRange` · class
```python
class FloatRange(_NumberRangeBase[float, float], FloatParamType)
```

`FloatRange` 类用于定义一个浮点数范围，可以用于命令行参数的类型检查和验证。

### 方法

#### `__init__`

初始化一个 `FloatRange` 对象。

**Parameters:**
- `min` — `float | None` — 范围的最小值，如果为 `None`，则没有最小值限制。
- `max` — `float | None` — 范围的最大值，如果为 `None`，则没有最大值限制。
- `min_open` — `bool` — 是否允许最小值（`True` 表示不包括最小值，`False` 表示包括最小值）。
- `max_open` — `bool` — 是否允许最大值（`True` 表示不包括最大值，`False` 表示包括最大值）。
- `clamp` — `bool` — 是否对超出范围的值进行裁剪（`True` 表示裁剪，`False` 表示不裁剪）。

#### `_clamp`

对一个浮点数进行裁剪。

**Parameters:**
- `bound` — `float` — 需要裁剪的浮点数。
- `dir` — `t.Literal[1, -1]` — 裁剪方向，`1` 表示向上裁剪，`-1` 表示向下裁剪。
- `open` — `bool` — 是否允许边界值（`True` 表

*来源: `src/click/types.py:718`*

---
<a id="sym-src_click_types.py-736"></a>
### `FloatRange.__init__` · method
```python
def __init__(
        self,
        min: float | None = None,
        max: float | None = None,
        min_open: bool = False,
        max_open: bool = False,
        clamp: bool = False,
    ) -> None
```

### FloatRange.__init__

初始化一个 `FloatRange` 对象，用于限制浮点数的范围。

**Parameters:**
- `min` — `float | None` — 范围的最小值，如果为 `None`，则没有最小限制。
- `max` — `float | None` — 范围的最大值，如果为 `None`，则没有最大限制。
- `min_open` — `bool` — 是否允许最小值（`True` 表示允许，`False` 表示不允许）。
- `max_open` — `bool` — 是否允许最大值（`True` 表示允许，`False` 表示不允许）。
- `clamp` — `bool` — 是否将值限制在范围内（`True` 表示限制，`False` 表示不限制）。

**Raises:**
- `TypeError` — 如果同时设置了 `min_open` 或 `max_open` 且 `clamp` 为 `True`。

*来源: `src/click/types.py:736`*

---
<a id="sym-src_click_types.py-751"></a>
### `FloatRange._clamp` · method
```python
def _clamp(self, bound: float, dir: t.Literal[1, -1], open: bool) -> float
```

Clamps a float value based on the given bound, direction, and whether the bound is open.

**Parameters**:
- `bound` — `float` — The bound value to clamp against.
- `dir` — `t.Literal[1, -1]` — The direction to clamp towards (1 for upper, -1 for lower).
- `open` — `bool` — Whether the bound is open.

**Returns**:
- `float` — The clamped value.

**Raises**:
- `RuntimeError` — If the bound is open and clamping is not supported.

*来源: `src/click/types.py:751`*

---
<a id="sym-src_click_types.py-761"></a>
### `BoolParamType` · class
```python
class BoolParamType(ParamType[bool])
```

`BoolParamType` 类用于处理布尔类型的参数，提供将字符串或布尔值转换为布尔值的方法。

- **Parameters**:
  - `value` — `str | bool` — 要转换的值，可以是字符串或布尔值。
  - `param` — `Parameter | None` — 相关的参数对象，可选。
  - `ctx` — `Context | None` — 相关的上下文对象，可选。

- **Returns**:
  - `bool` — 转换后的布尔值。

- **Raises**:
  - `UsageError` — 如果输入值无法转换为布尔值。

*来源: `src/click/types.py:761`*

---
<a id="sym-src_click_types.py-798"></a>
### `BoolParamType.str_to_bool` · method
装饰器: `@staticmethod`
```python
def str_to_bool(value: str | bool) -> bool | None
```

Convert a string to a boolean value.

**Parameters**:
- `value` — `str | bool` — The value to convert.

**Returns**:
- `bool | None` — The converted boolean value, or `None` if the value does not match any known boolean state.

*来源: `src/click/types.py:798`*

---
<a id="sym-src_click_types.py-812"></a>
### `BoolParamType.convert` · method
```python
def convert(
        self, value: t.Any, param: Parameter | None, ctx: Context | None
    ) -> bool
```

将输入值转换为布尔类型。

**Parameters**:
- value — t.Any — 输入值。
- param — Parameter | None — 相关参数。
- ctx — Context | None — 相关上下文。

**Returns**:
- bool — 转换后的布尔值。

**Raises**:
- BadParameter — 如果输入值不是有效的布尔值。

**内部调用(库内):**
- [`BoolParamType.str_to_bool`](src_click.md#sym-src_click_types.py-798) — Convert a string to a boolean value.
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.

*来源: `src/click/types.py:812`*

---
<a id="sym-src_click_types.py-826"></a>
### `BoolParamType.__repr__` · method
```python
def __repr__(self) -> str
```

**用途**: 返回表示布尔参数类型的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 表示布尔参数类型的字符串 "BOOL"。

**Raises**:
- 无

*来源: `src/click/types.py:826`*

---
<a id="sym-src_click_types.py-830"></a>
### `UUIDParameterType` · class
```python
class UUIDParameterType(ParamType[uuid.UUID])
```

`UUIDParameterType` 类用于处理 UUID 类型的参数，确保输入值是有效的 UUID。

- **Parameters**:
  - `value` — `uuid.UUID | str` — 要转换的值，可以是 UUID 对象或字符串表示的 UUID。
  - `param` — `Parameter | None` — 相关的参数对象，可选。
  - `ctx` — `Context | None` — 当前的上下文对象，可选。

- **Returns**:
  - `uuid.UUID` — 转换后的 UUID 对象。

- **Raises**:
  - `ValueError` — 如果输入值不是有效的 UUID。

*来源: `src/click/types.py:830`*

---
<a id="sym-src_click_types.py-833"></a>
### `UUIDParameterType.convert` · method
```python
def convert(
        self, value: uuid.UUID | str, param: Parameter | None, ctx: Context | None
    ) -> uuid.UUID
```

Converts a value to a UUID.

**Parameters**:
- value — uuid.UUID | str — The value to convert.
- param — Parameter | None — The parameter being processed.
- ctx — Context | None — The context in which the parameter is being processed.

**Returns**:
- uuid.UUID — The converted UUID.

**Raises**:
- BadParameter — If the value is not a valid UUID.

**内部调用(库内):**
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.

*来源: `src/click/types.py:833`*

---
<a id="sym-src_click_types.py-848"></a>
### `UUIDParameterType.__repr__` · method
```python
def __repr__(self) -> str
```

返回表示 UUID 类型的字符串。

**Parameters**:
- 无

**Returns**:
- `str`: 表示 UUID 类型的字符串 "UUID"

*来源: `src/click/types.py:848`*

---
<a id="sym-src_click_types.py-852"></a>
### `FileInfoDict` · class
```python
class FileInfoDict(ParamTypeInfoDict)
```

`FileInfoDict` 类继承自 `ParamTypeInfoDict`，用于存储和管理文件信息的字典。

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| 无 | 无 | 该类无参数 |

| 返回 | 含义 |
| --- | --- |
| 无 | 该类无返回值 |

| 异常 | 含义 |
| --- | --- |
| 无 | 该类无异常抛出 |

`FileInfoDict` 类用于存储和管理文件信息，通常在命令行工具中用于处理文件相关的参数。

*来源: `src/click/types.py:852`*

---
<a id="sym-src_click_types.py-857"></a>
### `File` · class
```python
class File(ParamType[t.IO[t.Any]])
```

`File` 类是一个 Click 参数类型，用于处理文件路径和文件对象的转换和解析。

### Parameters
- `mode` — `str` — 文件打开模式，如 "r"（读取）、"w"（写入）等。
- `encoding` — `str | None` — 文件的编码格式，如 "utf-8"。
- `errors` — `str | None` — 处理编码错误的方式，如 "strict"、"ignore" 等。
- `lazy` — `bool | None` — 是否延迟加载文件。
- `atomic` — `bool` — 是否以原子方式处理文件。

### Returns
- `FileInfoDict` — 文件信息字典。

### Raises
- `FileNotFoundError` — 如果文件不存在。
- `PermissionError` — 如果没有权限访问文件。

### Methods
- `to_info_dict(self) -> FileInfoDict` — 将文件信息转换为字典。
- `resolve_lazy_flag(self, value: str | os.PathLike[str]) -> bool` — 解析延迟加载标志。
- `convert(self, value: str | os.PathLike[str] | t.IO[t.Any], param: Parameter | None, ctx: Context | None) -> t.IO[t.Any]` — 将文件路径或文件对象转换为文件对象。
- `shell_complete(self, ctx: Context, param: Parameter, incomplete: str) -> list[CompletionItem]` — 提供 shell 自动补全功能。

*来源: `src/click/types.py:857`*

---
<a id="sym-src_click_types.py-896"></a>
### `File.__init__` · method
```python
def __init__(
        self,
        mode: str = "r",
        encoding: str | None = None,
        errors: str | None = "strict",
        lazy: bool | None = None,
        atomic: bool = False,
    ) -> None
```

初始化一个文件对象。

**Parameters:**
- `mode` — `str` — 文件打开模式，默认为 "r"（只读）。
- `encoding` — `str | None` — 文件编码，默认为 None。
- `errors` — `str | None` — 错误处理方式，默认为 "strict"。
- `lazy` — `bool | None` — 是否延迟加载，默认为 None。
- `atomic` — `bool` — 是否原子操作，默认为 False。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/types.py:896`*

---
<a id="sym-src_click_types.py-910"></a>
### `File.to_info_dict` · method
```python
def to_info_dict(self) -> FileInfoDict
```

将文件信息转换为字典。

**Parameters**:
- 无

**Returns**:
- `FileInfoDict` — 包含文件模式和编码的字典。

**Raises**:
- 无

*来源: `src/click/types.py:910`*

---
<a id="sym-src_click_types.py-917"></a>
### `File.resolve_lazy_flag` · method
```python
def resolve_lazy_flag(self, value: str | os.PathLike[str]) -> bool
```

**用途**: 解析文件的延迟标志。

**Parameters**:
- `value` — `str | os.PathLike[str]` — 文件路径或类似路径的对象。

**Returns**:
- `bool` — 文件的延迟标志。

**Raises**:
- 无

*来源: `src/click/types.py:917`*

---
<a id="sym-src_click_types.py-926"></a>
### `File.convert` · method
```python
def convert(
        self,
        value: str | os.PathLike[str] | t.IO[t.Any],
        param: Parameter | None,
        ctx: Context | None,
    ) -> t.IO[t.Any]
```

将输入值转换为文件对象。

**Parameters**:
- `value` — `str | os.PathLike[str] | t.IO[t.Any]` — 输入值，可以是文件路径、文件对象或类似文件的对象。
- `param` — `Parameter | None` — 参数对象，可选。
- `ctx` — `Context | None` — 上下文对象，可选。

**Returns**:
- `t.IO[t.Any]` — 文件对象。

**Raises**:
- `OSError` — 如果无法打开文件。

**内部调用(库内):**
- [`_is_file_like`](src_click.md#sym-src_click_types.py-988) — 检查给定的值是否为文件对象。
- [`File.resolve_lazy_flag`](src_click.md#sym-src_click_types.py-917) — **用途**: 解析文件的延迟标志。
- [`LazyFile`](src_click.md#sym-src_click_utils.py-112) — `LazyFile` 类提供了一个延迟打开文件的机制，只有在实际需要时才打开文件，从而节省资源。
- [`Context.call_on_close`](src_click.md#sym-src_click_core.py-673) — Register a function to be called when the context tears down.
- [`open_stream`](src_click.md#sym-src_click__compat.py-370) — `open_stream`
- [`safecall`](src_click.md#sym-src_click_utils.py-36) — Wraps a function to swallow exceptions, returning `None` if an exception occurs.
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.
- [`format_filename`](src_click.md#sym-src_click_utils.py-425) — Format a filename for display, ensuring it can be displayed by replacing any inv

*来源: `src/click/types.py:926`*

---
<a id="sym-src_click_types.py-971"></a>
### `File.shell_complete` · method
```python
def shell_complete(
        self, ctx: Context, param: Parameter, incomplete: str
    ) -> list[CompletionItem]
```

**用途**: 返回一个特殊的完成标记，告诉完成系统使用 shell 提供文件路径补全。

**Parameters**:
- `ctx` — `Context` — 调用此命令的上下文。
- `param` — `Parameter` — 正在请求补全的参数。
- `incomplete` — `str` — 正在补全的值，可能为空。

**Returns**:
- `list[CompletionItem]` — 返回一个包含特殊完成标记的列表，该标记告诉完成系统使用 shell 提供文件路径补全。

**Raises**:
- 无

**内部调用(库内):**
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。

*来源: `src/click/types.py:971`*

---
<a id="sym-src_click_types.py-988"></a>
### `_is_file_like` · func
```python
def _is_file_like(value: t.Any) -> te.TypeIs[t.IO[t.Any]]
```

检查给定的值是否为文件对象。

**Parameters**:
- value — `t.Any` — 要检查的值。

**Returns**:
- `te.TypeIs[t.IO[t.Any]]` — 如果值具有 `read` 或 `write` 方法，则返回 `True`，否则返回 `False`。

**Raises**:
- 无

*来源: `src/click/types.py:988`*

---
<a id="sym-src_click_types.py-992"></a>
### `PathInfoDict` · class
```python
class PathInfoDict(ParamTypeInfoDict)
```

`PathInfoDict` 类继承自 `ParamTypeInfoDict`，用于处理路径信息的类型检查和验证。

| **Parameters** | **Type** | **Meaning** |
| -------------- | -------- | ----------- |
| 无             | 无       | 无          |

| **Returns** | **Meaning** |
| ----------- | ----------- |
| 无          | 无          |

| **Raises** | **Meaning** |
| ---------- | ----------- |
| 无         | 无          |

这个类主要用于在 Click 命令行工具中对路径参数进行类型检查和验证。它继承了 `ParamTypeInfoDict` 的功能，并提供了特定的路径信息处理逻辑。

*来源: `src/click/types.py:992`*

---
<a id="sym-src_click_types.py-1001"></a>
### `Path` · class
```python
class Path(ParamType[str | bytes | os.PathLike[str]])
```

`Path` 类用于处理文件路径，提供验证和转换路径的功能。

### 方法

#### `__init__`
初始化 `Path` 对象。

**Parameters:**
- `exists` — `bool` — 指定路径必须存在。
- `file_okay` — `bool` — 允许路径是文件。
- `dir_okay` — `bool` — 允许路径是目录。
- `writable` — `bool` — 指定路径必须可写。
- `readable` — `bool` — 指定路径必须可读。
- `resolve_path` — `bool` — 是否解析路径。
- `allow_dash` — `bool` — 是否允许路径是短横线。
- `path_type` — `type | None` — 指定路径类型。
- `executable` — `bool` — 指定路径必须可执行。

#### `to_info_dict`
将路径信息转换为字典。

**Returns:**
- `PathInfoDict` — 路径信息字典。

#### `coerce_path_result`
将路径值转换为标准路径格式。

**Parameters:**
- `value` — `str | os.PathLike[str]` — 路径值。

**Returns:**
- `str | bytes | os.PathLike[str]` — 转换后的路径值。

#### `convert`
将路径值转换为标准路径格式，并进行验证。

**Parameters:**
- `value` —

*来源: `src/click/types.py:1001`*

---
<a id="sym-src_click_types.py-1046"></a>
### `Path.__init__` · method
```python
def __init__(
        self,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: type | None = None,
        executable: bool = False,
    ) -> None
```

### Path.__init__

初始化一个 `Path` 对象，用于检查文件或目录的属性。

**Parameters:**
- `exists` — `bool` — 检查路径是否存在。
- `file_okay` — `bool` — 是否允许路径是文件。
- `dir_okay` — `bool` — 是否允许路径是目录。
- `writable` — `bool` — 检查路径是否可写。
- `readable` — `bool` — 检查路径是否可读。
- `resolve_path` — `bool` — 是否解析路径。
- `allow_dash` — `bool` — 是否允许路径是短横线。
- `path_type` — `type | None` — 指定路径类型。
- `executable` — `bool` — 检查路径是否可执行。

**Returns:**
- `None`

**Raises:**
- 无

*来源: `src/click/types.py:1046`*

---
<a id="sym-src_click_types.py-1075"></a>
### `Path.to_info_dict` · method
```python
def to_info_dict(self) -> PathInfoDict
```

将 `Path` 对象转换为包含路径信息的字典。

**Parameters**:
- 无

**Returns**:
- `PathInfoDict`: 包含路径信息的字典，包括 `exists`, `file_okay`, `dir_okay`, `writable`, `readable`, `allow_dash` 等属性。

**Raises**:
- 无

*来源: `src/click/types.py:1075`*

---
<a id="sym-src_click_types.py-1086"></a>
### `Path.coerce_path_result` · method
```python
def coerce_path_result(
        self, value: str | os.PathLike[str]
    ) -> str | bytes | os.PathLike[str]
```

将输入值转换为指定的路径类型。

**Parameters**:
- `value` — `str | os.PathLike[str]` — 输入的路径值。

**Returns**:
- `str | bytes | os.PathLike[str]` — 转换后的路径值。

**Raises**:
- 无

*来源: `src/click/types.py:1086`*

---
<a id="sym-src_click_types.py-1099"></a>
### `Path.convert` · method
```python
def convert(
        self,
        value: str | os.PathLike[str],
        param: Parameter | None,
        ctx: Context | None,
    ) -> str | bytes | os.PathLike[str]
```

Converts a path string or path-like object to a normalized path string, bytes, or path-like object.

**Parameters**:
- `value` — `str | os.PathLike[str]` — The path string or path-like object to convert.
- `param` — `Parameter | None` — The parameter object associated with the value.
- `ctx` — `Context | None` — The context object associated with the value.

**Returns**:
- `str | bytes | os.PathLike[str]` — The normalized path string, bytes, or path-like object.

**Raises**:
- `BadParameter` — If the path does not exist or is not a file or directory as expected.

**内部调用(库内):**
- [`Path.coerce_path_result`](src_click.md#sym-src_click_types.py-1086) — 将输入值转换为指定的路径类型。
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.
- [`format_filename`](src_click.md#sym-src_click_utils.py-425) — Format a filename for display, ensuring it can be displayed by replacing any inv

*来源: `src/click/types.py:1099`*

---
<a id="sym-src_click_types.py-1172"></a>
### `Path.shell_complete` · method
```python
def shell_complete(
        self, ctx: Context, param: Parameter, incomplete: str
    ) -> list[CompletionItem]
```

**用途**: 返回一个特殊的完成标记，告诉完成系统使用 shell 提供路径补全，仅限目录或任何路径。

**Parameters**:
- `ctx` — `Context` — 调用此命令的上下文。
- `param` — `Parameter` — 正在请求补全的参数。
- `incomplete` — `str` — 正在补全的值，可能为空。

**Returns**:
- `list[CompletionItem]` — 一个包含特殊完成标记的列表，该标记告诉 shell 提供路径补全。

**Raises**:
- 无

**内部调用(库内):**
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。

*来源: `src/click/types.py:1172`*

---
<a id="sym-src_click_types.py-1191"></a>
### `TupleInfoDict` · class
```python
class TupleInfoDict(ParamTypeInfoDict)
```

`TupleInfoDict` 是 Click 库中用于处理元组类型参数的字典类，它继承自 `ParamTypeInfoDict`。

| **Parameters** | **Type** | **Meaning** |
| --- | --- | --- |
| 无 | 无 | 无 |

| **Returns** | **Meaning** |
| --- | --- |
| 无 | 无 |

| **Raises** | **Meaning** |
| --- | --- |
| 无 | 无 |

这个类主要用于定义和处理元组类型的参数信息。它继承自 `ParamTypeInfoDict`，可以用来存储和操作元组类型的参数信息。

*来源: `src/click/types.py:1191`*

---
<a id="sym-src_click_types.py-1195"></a>
### `Tuple` · class
```python
class Tuple(CompositeParamType[tuple[t.Any, ...]])
```

`Tuple` 类用于定义一个参数类型，该参数类型可以接受一个元组，并且每个元素可以是不同类型的值。

### 方法

#### `__init__(self, types: cabc.Sequence[type[t.Any] | ParamType[t.Any]]) -> None`
- **Parameters**:
  - `types` — `cabc.Sequence[type[t.Any] | ParamType[t.Any]]` — 一个包含类型或 `ParamType` 对象的序列，每个元素对应元组中相应位置的值的类型。
- **Returns**:
  - `None`

#### `to_info_dict(self) -> TupleInfoDict`
- **Returns**:
  - `TupleInfoDict` — 一个字典，包含有关 `Tuple` 类型的信息。

#### `name(self) -> str:  # type: ignore[override]`
- **Returns**:
  - `str` — 类型的名称。

#### `arity(self) -> int:  # type: ignore[override]`
- **Returns**:
  - `int` — 元组中元素的数量。

#### `convert(self, value: t.Any, param: Parameter | None, ctx: Context | None) -> tuple[t.Any, ...]`
- **Parameters**:
  - `value` — `t.Any` — 要转换的值。
  - `param` — `Parameter | None` — 相关的参数对象。
  - `ctx` — `Context | None` — 相关的上下文对象。
-

*来源: `src/click/types.py:1195`*

---
<a id="sym-src_click_types.py-1209"></a>
### `Tuple.__init__` · method
```python
def __init__(self, types: cabc.Sequence[type[t.Any] | ParamType[t.Any]]) -> None
```

初始化一个 `Tuple` 对象，用于存储多个参数类型。

**Parameters**:
- `types` — `cabc.Sequence[type[t.Any] | ParamType[t.Any]]` — 一个包含参数类型的序列，可以是 `type[t.Any]` 或 `ParamType[t.Any]`。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`convert_type`](src_click.md#sym-src_click_types.py-1284) — Converts a type to a `StringParamType`.

*来源: `src/click/types.py:1209`*

---
<a id="sym-src_click_types.py-1212"></a>
### `Tuple.to_info_dict` · method
```python
def to_info_dict(self) -> TupleInfoDict
```

将元组类型转换为信息字典。

**Parameters**:
- 无

**Returns**:
- `TupleInfoDict` — 包含元组类型信息的字典。

**Raises**:
- 无

*来源: `src/click/types.py:1212`*

---
<a id="sym-src_click_types.py-1219"></a>
### `Tuple.name` · method
装饰器: `@property`
```python
def name(self) -> str:  # type: ignore[override]
```

**用途**: 返回一个元组中所有类型名称的字符串表示。

**Parameters**:
- 无

**Returns**:
- `str`: 元组中所有类型名称的字符串表示，类型名称之间用空格分隔。

**Raises**:
- 无

*来源: `src/click/types.py:1219`*

---
<a id="sym-src_click_types.py-1223"></a>
### `Tuple.arity` · method
装饰器: `@property`
```python
def arity(self) -> int:  # type: ignore[override]
```

返回元组的类型数量。

**Parameters**:
- 无

**Returns**:
- `int`: 元组的类型数量

**Raises**:
- 无

*来源: `src/click/types.py:1223`*

---
<a id="sym-src_click_types.py-1226"></a>
### `Tuple.convert` · method
```python
def convert(
        self, value: t.Any, param: Parameter | None, ctx: Context | None
    ) -> tuple[t.Any, ...]
```

将单个值转换为元组。

**Parameters:**
- `value` — `t.Any` — 要转换的值。
- `param` — `Parameter | None` — 相关的参数对象。
- `ctx` — `Context | None` — 相关的上下文对象。

**Returns:**
- `tuple[t.Any, ...]` — 转换后的元组。

**Raises:**
- `BadParameter` — 如果提供的值数量与类型数量不匹配。

**内部调用(库内):**
- [`ParamType.fail`](src_click.md#sym-src_click_types.py-157) — **用途**: Helper method to fail with an invalid value message.

*来源: `src/click/types.py:1226`*

---
<a id="sym-src_click_types.py-1248"></a>
### `_guess_type` · func
```python
def _guess_type(
    ty: type[t.Any] | ParamType[t.Any] | None,
    default: t.Any | None,
) -> type[t.Any] | tuple[type[t.Any], ...] | ParamType[t.Any] | None
```

Infer a type from the provided type or default value.

**Parameters**:
- `ty` — `type[t.Any] | ParamType[t.Any] | None` — The type to infer.
- `default` — `t.Any | None` — The default value to inspect if `ty` is `None`.

**Returns**:
- `type[t.Any] | tuple[type[t.Any], ...] | ParamType[t.Any] | None` — The inferred type, a tuple of types, or `None`.

*来源: `src/click/types.py:1248`*

---
<a id="sym-src_click_types.py-1284"></a>
### `convert_type` · func
装饰器: `@t.overload`
```python
def convert_type(ty: None, default: None = None) -> StringParamType
```

Converts a type to a `StringParamType`.

**Parameters**:
- `ty` — `None` — The type to convert.
- `default` — `None` — The default value.

**Returns**:
- `StringParamType` — The converted type.

*来源: `src/click/types.py:1284`*

---
<a id="sym-src_click_types.py-1286"></a>
### `convert_type` · func
装饰器: `@t.overload`
```python
def convert_type(
    ty: type | ParamType[t.Any], default: t.Any | None = None
) -> ParamType[t.Any]
```

Converts a type to a Click parameter type.

**Parameters**:
- `ty` — `type | ParamType[t.Any]` — The type to convert.
- `default` — `t.Any | None` — The default value for the parameter.

**Returns**:
- `ParamType[t.Any]` — The converted Click parameter type.

*来源: `src/click/types.py:1286`*

---
<a id="sym-src_click_types.py-1290"></a>
### `convert_type` · func
装饰器: `@t.overload`
```python
def convert_type(
    ty: t.Any | None, default: t.Any | None = None
) -> ParamType[t.Any]
```

Converts a given type to a `ParamType`.

**Parameters**:
- `ty` — `t.Any | None` — The type to convert.
- `default` — `t.Any | None` — The default value to use if `ty` is `None`.

**Returns**:
- `ParamType[t.Any]` — The converted type.

*来源: `src/click/types.py:1290`*

---
<a id="sym-src_click_types.py-1293"></a>
### `convert_type` · func
```python
def convert_type(
    ty: t.Any | None = None, default: t.Any | None = None
) -> ParamType[t.Any]
```

Find the most appropriate :class:`ParamType` for the given Python type. If the type isn't provided, it can be inferred from a default value.

**Parameters**:
- `ty` — `t.Any | None` — The Python type to convert. If not provided, it will be inferred from the `default` value.
- `default` — `t.Any | None` — The default value to use for type inference if `ty` is not provided.

**Returns**:
- `ParamType[t.Any]` — The most appropriate :class:`ParamType` for the given Python type.

**Raises**:
- `AssertionError` — If an uninstantiated parameter type is used.

**内部调用(库内):**
- [`_guess_type`](src_click.md#sym-src_click_types.py-1248) — Infer a type from the provided type or default value.
- [`Tuple`](src_click.md#sym-src_click_types.py-1195) — `Tuple` 类用于定义一个参数类型，该参数类型可以接受一个元组，并且每个元素可以是不同类型的值。
- [`FuncParamType`](src_click.md#sym-src_click_types.py-206) — `FuncParamType` 类用于将一个函数转换为参数类型，以便在命令行参数中使用。

*来源: `src/click/types.py:1293`*

---
<a id="sym-src_click_types.py-1370"></a>
### `OptionHelpExtra` · class
```python
class OptionHelpExtra(t.TypedDict, total=False)
```

`OptionHelpExtra` 类是一个类型提示字典，用于扩展 Click 命令行工具中选项的帮助信息。

| 参数名 | 类型 | 含义 |
| --- | --- | --- |
| help | str | 选项的帮助文本 |
| show_default | bool | 是否显示选项的默认值 |
| prompt | str | 选项的提示文本 |
| confirmation_prompt | str | 确认选项的提示文本 |
| prompt_required | bool | 是否要求用户输入 |
| is_flag | bool | 是否是布尔标志选项 |
| flag_value | Any | 布尔标志选项的值 |
| multiple | bool | 是否允许多个值 |
| count | bool | 是否计数 |
| metavar | str | 选项的元变量名称 |
| nargs | int | 选项的参数数量 |
| type | ParamType | 选项的参数类型 |
| callback | Callable | 选项的回调函数 |
| expose_value | bool | 是否暴露选项的值 |
| is_eager | bool | 是否在解析其他选项之前解析该选项 |
| help_option_names | List[str] | 帮助选项的名称 |
| hidden | bool | 是否隐藏该选项 |
| show_envvar | bool | 是否显示环境变量 |
| envvar | str | 环境变量名称 |
| autocompletion | Callable | 自动补全函数 |
| is_group | bool | 是否是选项组 |
| is_subcommand | bool | 是否是子命令 |
| is_option | bool |

*来源: `src/click/types.py:1370`*

---

## `src/click/utils.py`

<a id="sym-src_click_utils.py-32"></a>
### `_posixify` · func
```python
def _posixify(name: str) -> str
```

将字符串转换为 POSIX 兼容的格式。

**Parameters**:
- `name` — `str` — 输入的字符串。

**Returns**:
- `str` — 转换后的 POSIX 兼容字符串。

*来源: `src/click/utils.py:32`*

---
<a id="sym-src_click_utils.py-36"></a>
### `safecall` · func
```python
def safecall(func: t.Callable[P, R]) -> t.Callable[P, R | None]
```

Wraps a function to swallow exceptions, returning `None` if an exception occurs.

**Parameters**:
- `func` — `t.Callable[P, R]` — The function to wrap.

**Returns**:
- `t.Callable[P, R | None]` — The wrapped function, which returns `None` if an exception occurs.

**Raises**:
- None

**内部调用(库内):**
- [`func`](src_click.md#sym-src_click__compat.py-549) — func

*来源: `src/click/utils.py:36`*

---
<a id="sym-src_click_utils.py-39"></a>
### `wrapper` · func
```python
def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | None
```

用途: 包装一个函数调用，捕获任何异常并返回 `None`。

**Parameters**:
- `*args` — `P.args` — 传递给被包装函数的参数。
- `**kwargs` — `P.kwargs` — 传递给被包装函数的关键字参数。

**Returns**:
- `R | None` — 被包装函数的返回值，如果发生异常则返回 `None`。

**Raises**:
- 无

**内部调用(库内):**
- [`func`](src_click.md#sym-src_click__compat.py-549) — func

*来源: `src/click/utils.py:39`*

---
<a id="sym-src_click_utils.py-49"></a>
### `make_str` · func
```python
def make_str(value: t.Any) -> str
```

Converts a value into a valid string.

**Parameters**:
- value — t.Any — The value to convert.

**Returns**:
- str — The converted string.

**Raises**:
- None

*来源: `src/click/utils.py:49`*

---
<a id="sym-src_click_utils.py-59"></a>
### `make_default_short_help` · func
```python
def make_default_short_help(help: str, max_length: int = 45) -> str
```

Returns a condensed version of the help string, ensuring it does not exceed the specified maximum length.

**Parameters**:
- `help` — `str` — The original help string.
- `max_length` — `int` — The maximum allowed length of the condensed help string (default is 45).

**Returns**:
- `str` — The condensed help string.

*来源: `src/click/utils.py:59`*

---
<a id="sym-src_click_utils.py-112"></a>
### `LazyFile` · class
```python
class LazyFile
```

`LazyFile` 类提供了一个延迟打开文件的机制，只有在实际需要时才打开文件，从而节省资源。

- **Parameters**:
  - `filename` — `str | os.PathLike[str]` — 文件路径。
  - `mode` — `str` — 文件打开模式，默认为 "r"。
  - `encoding` — `str | None` — 文件编码，默认为 None。
  - `errors` — `str | None` — 错误处理方式，默认为 "strict"。
  - `atomic` — `bool` — 是否以原子方式打开文件，默认为 False。

- **Returns**:
  - `t.IO[t.Any]` — 文件对象。

- **Raises**:
  - `FileNotFoundError` — 文件不存在时抛出。
  - `PermissionError` — 权限不足时抛出。

- **Methods**:
  - `open(self) -> t.IO[t.Any]` — 打开文件并返回文件对象。
  - `close(self) -> None` — 关闭文件。
  - `close_intelligently(self) -> None` — 智能关闭文件，确保在异常情况下也能正确关闭。
  - `__enter__(self) -> LazyFile` — 上下文管理器入口，返回当前对象。
  - `__exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` — 上下文管理器出口

*来源: `src/click/utils.py:112`*

---
<a id="sym-src_click_utils.py-127"></a>
### `LazyFile.__init__` · method
```python
def __init__(
        self,
        filename: str | os.PathLike[str],
        mode: str = "r",
        encoding: str | None = None,
        errors: str | None = "strict",
        atomic: bool = False,
    ) -> None
```

`LazyFile` 类用于延迟打开文件，直到实际需要读取或写入时才进行打开操作。

**Parameters**:
- `filename` — `str | os.PathLike[str]` — 文件路径或类似路径的对象。
- `mode` — `str` — 文件打开模式，默认为 "r"（读取模式）。
- `encoding` — `str | None` — 文件编码，默认为 None。
- `errors` — `str | None` — 错误处理方式，默认为 "strict"。
- `atomic` — `bool` — 是否以原子方式打开文件，默认为 False。

**Returns**:
- `None`

**Raises**:
- 无

**内部调用(库内):**
- [`open_stream`](src_click.md#sym-src_click__compat.py-370) — `open_stream`

*来源: `src/click/utils.py:127`*

---
<a id="sym-src_click_utils.py-152"></a>
### `LazyFile.__getattr__` · method
```python
def __getattr__(self, name: str) -> t.Any
```

用途: 代理对文件对象的属性访问。

**Parameters**:
- `name` — `str` — 要访问的属性名称。

**Returns**:
- `t.Any` — 文件对象上指定属性的值。

**Raises**:
- 无

*来源: `src/click/utils.py:152`*

---
<a id="sym-src_click_utils.py-155"></a>
### `LazyFile.__repr__` · method
```python
def __repr__(self) -> str
```

### `LazyFile.__repr__`

返回文件的字符串表示形式。

**Parameters**:
- 无

**Returns**:
- `str`: 文件的字符串表示形式。

**Raises**:
- 无

**内部调用(库内):**
- [`format_filename`](src_click.md#sym-src_click_utils.py-425) — Format a filename for display, ensuring it can be displayed by replacing any inv

*来源: `src/click/utils.py:155`*

---
<a id="sym-src_click_utils.py-160"></a>
### `LazyFile.open` · method
```python
def open(self) -> t.IO[t.Any]
```

LazyFile.open 方法用于打开文件。如果文件尚未打开，则会尝试打开文件。如果打开文件时发生错误，会抛出 FileError 异常。

- **Parameters**:
  - 无

- **Returns**:
  - `t.IO[t.Any]`: 文件对象

- **Raises**:
  - `FileError`: 如果打开文件时发生错误

**内部调用(库内):**
- [`open_stream`](src_click.md#sym-src_click__compat.py-370) — `open_stream`
- [`FileError`](src_click.md#sym-src_click_exceptions.py-342) — `FileError` 类继承自 `ClickException`，用于表示与文件操作相关的错误。

*来源: `src/click/utils.py:160`*

---
<a id="sym-src_click_utils.py-178"></a>
### `LazyFile.close` · method
```python
def close(self) -> None
```

Closes the underlying file, no matter what.

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/utils.py:178`*

---
<a id="sym-src_click_utils.py-183"></a>
### `LazyFile.close_intelligently` · method
```python
def close_intelligently(self) -> None
```

### close_intelligently

Closes the file if it was opened by the lazy file wrapper, ensuring that stdin is never closed.

**Parameters**:
- `self` — `LazyFile` — The instance of the `LazyFile` class.

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/utils.py:183`*

---
<a id="sym-src_click_utils.py-190"></a>
### `LazyFile.__enter__` · method
```python
def __enter__(self) -> LazyFile
```

用途: 返回当前的 `LazyFile` 实例。

**Parameters**:
- 无

**Returns**:
- `LazyFile`: 当前的 `LazyFile` 实例。

**Raises**:
- 无

*来源: `src/click/utils.py:190`*

---
<a id="sym-src_click_utils.py-193"></a>
### `LazyFile.__exit__` · method
```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None
```

关闭文件，如果文件是打开的。

**Parameters:**
- `exc_type` (type[BaseException] | None) — 异常类型，如果有的话。
- `exc_value` (BaseException | None) — 异常值，如果有的话。
- `tb` (TracebackType | None) — 异常回溯，如果有的话。

**Returns:**
- `None`

**Raises:**
- 无

**内部调用(库内):**
- [`LazyFile.close_intelligently`](src_click.md#sym-src_click_utils.py-183) — close_intelligently

*来源: `src/click/utils.py:193`*

---
<a id="sym-src_click_utils.py-201"></a>
### `LazyFile.__iter__` · method
```python
def __iter__(self) -> cabc.Iterator[t.AnyStr]
```

### `LazyFile.__iter__`

**用途**: 迭代文件内容。

**Parameters**:
- 无

**Returns**:
- `cabc.Iterator[t.AnyStr]`: 文件内容的迭代器。

**Raises**:
- 无

*来源: `src/click/utils.py:201`*

---
<a id="sym-src_click_utils.py-206"></a>
### `KeepOpenFile` · class
```python
class KeepOpenFile
```

`KeepOpenFile` 类用于包装一个文件对象，确保在上下文管理器中使用时文件保持打开状态，直到显式关闭。

- **Parameters**:
  - `file` — `t.IO[t.Any]` — 要包装的文件对象。

- **Returns**:
  - `None`

- **Raises**:
  - 无

### 关键方法

- **__init__(self, file: t.IO[t.Any]) -> None**
  - 初始化 `KeepOpenFile` 对象，接受一个文件对象作为参数。

- **__getattr__(self, name: str) -> t.Any**
  - 代理对文件对象的属性访问。

- **__enter__(self) -> KeepOpenFile**
  - 实现上下文管理器的 `__enter__` 方法，返回当前对象。

- **__exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None**
  - 实现上下文管理器的 `__exit__` 方法，确保文件在上下文退出时保持打开状态。

- **__repr__(self) -> str**
  - 返回对象的字符串表示。

- **__iter__(self) -> cabc.Iterator[t.AnyStr]**
  - 实现迭代器协议，返回文件对象的迭代器。

*来源: `src/click/utils.py:206`*

---
<a id="sym-src_click_utils.py-221"></a>
### `KeepOpenFile.__init__` · method
```python
def __init__(self, file: t.IO[t.Any]) -> None
```

用途: 用于包装一个文件对象，确保文件在对象被销毁时不会关闭。

**Parameters**:
- `file` — `t.IO[t.Any]` — 要包装的文件对象。

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `src/click/utils.py:221`*

---
<a id="sym-src_click_utils.py-224"></a>
### `KeepOpenFile.__getattr__` · method
```python
def __getattr__(self, name: str) -> t.Any
```

### 用途
递归地获取文件对象的属性。

### Parameters
- `name` — `str` — 要获取的属性名称。

### Returns
- `t.Any` — 文件对象的属性值。

### Raises
- 无

*来源: `src/click/utils.py:224`*

---
<a id="sym-src_click_utils.py-227"></a>
### `KeepOpenFile.__enter__` · method
```python
def __enter__(self) -> KeepOpenFile
```

用途: 返回当前的 `KeepOpenFile` 实例。

**Parameters**:
- 无

**Returns**:
- `KeepOpenFile`: 当前的 `KeepOpenFile` 实例。

**Raises**:
- 无

*来源: `src/click/utils.py:227`*

---
<a id="sym-src_click_utils.py-230"></a>
### `KeepOpenFile.__exit__` · method
```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None
```

### KeepOpenFile.__exit__

Closes the file handle without closing the underlying file descriptor.

**Parameters:**
- `exc_type` (`type[BaseException] | None`): The type of the exception that was raised, or `None` if no exception was raised.
- `exc_value` (`BaseException | None`): The exception instance that was raised, or `None` if no exception was raised.
- `tb` (`TracebackType | None`): The traceback object associated with the exception, or `None` if no exception was raised.

**Returns:**
- `None`

**Raises:**
- None

*来源: `src/click/utils.py:230`*

---
<a id="sym-src_click_utils.py-238"></a>
### `KeepOpenFile.__repr__` · method
```python
def __repr__(self) -> str
```

返回文件对象的字符串表示。

**Parameters**:
- 无

**Returns**:
- `str`: 文件对象的字符串表示。

**Raises**:
- 无

*来源: `src/click/utils.py:238`*

---
<a id="sym-src_click_utils.py-241"></a>
### `KeepOpenFile.__iter__` · method
```python
def __iter__(self) -> cabc.Iterator[t.AnyStr]
```

**用途**: 迭代 `KeepOpenFile` 对象中的文件内容。

**Parameters**:
- 无

**Returns**:
- `cabc.Iterator[t.AnyStr]`: 文件内容的迭代器。

**Raises**:
- 无

*来源: `src/click/utils.py:241`*

---
<a id="sym-src_click_utils.py-245"></a>
### `echo` · func
```python
def echo(
    message: object = None,
    file: t.IO[t.Any] | None = None,
    nl: bool = True,
    err: bool = False,
    color: bool | None = None,
) -> None
```

Print a message and newline to stdout or a file. This should be used instead of `print` because it provides better support for different data, files, and environments.

**Parameters**:
- `message` — `object` — The string or bytes to output. Other objects are converted to strings.
- `file` — `t.IO[t.Any] | None` — The file to write to. Defaults to `stdout`.
- `nl` — `bool` — Print a newline after the message. Enabled by default.
- `err` — `bool` — Write to `stderr` instead of `stdout`.
- `color` — `bool | None` — Force showing or hiding colors and other styles. By default Click will remove color if the output does not look like an interactive terminal.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`_find_binary_writer`](src_click.md#sym-src_click__compat.py-190) — _find_binary_writer
- [`resolve_color_default`](src_click.md#sym-src_click_globals.py-54) — 获取颜色标志的默认值。如果传递了一个值，则返回该值；否则，从当前上下文中查找。
- [`strip_ansi`](src_click.md#sym-src_click__compat.py-487) — **用途**: 移除字符串中的 ANSI 转义码。

*来源: `src/click/utils.py:245`*

---
<a id="sym-src_click_utils.py-343"></a>
### `get_binary_stream` · func
```python
def get_binary_stream(name: t.Literal["stdin", "stdout", "stderr"]) -> t.BinaryIO
```

Returns a system stream for byte processing.

- **Parameters**:
  - `name` — `t.Literal["stdin", "stdout", "stderr"]` — The name of the stream to open. Valid names are `'stdin'`, `'stdout'`, and `'stderr'`.
- **Returns**:
  - `t.BinaryIO` — The system stream for byte processing.
- **Raises**:
  - `TypeError` — If the provided `name` is not one of `'stdin'`, `'stdout'`, or `'stderr'`.

*来源: `src/click/utils.py:343`*

---
<a id="sym-src_click_utils.py-355"></a>
### `get_text_stream` · func
```python
def get_text_stream(
    name: t.Literal["stdin", "stdout", "stderr"],
    encoding: str | None = None,
    errors: str | None = "strict",
) -> t.TextIO
```

Returns a system stream for text processing. This usually returns a wrapped stream around a binary stream returned from `get_binary_stream` but it also can take shortcuts for already correctly configured streams.

- **Parameters**:
  - `name` — `t.Literal["stdin", "stdout", "stderr"]` — The name of the stream to open. Valid names are `stdin`, `stdout`, and `stderr`.
  - `encoding` — `str | None` — Overrides the detected default encoding.
  - `errors` — `str | None` — Overrides the default error mode.

- **Returns**:
  - `t.TextIO` — A text stream for text processing.

- **Raises**:
  - `TypeError` — If the unknown standard stream is provided.

*来源: `src/click/utils.py:355`*

---
<a id="sym-src_click_utils.py-376"></a>
### `open_file` · func
```python
def open_file(
    filename: str | os.PathLike[str],
    mode: str = "r",
    encoding: str | None = None,
    errors: str | None = "strict",
    lazy: bool = False,
    atomic: bool = False,
) -> t.IO[t.Any]
```

Open a file with additional behavior to handle special cases like opening standard streams, lazy opening on write, and atomic writing.

**Parameters**:
- `filename` — `str | os.PathLike[str]`: The name or Path of the file to open, or `'-'` for `stdin`/`stdout`.
- `mode` — `str`: The mode in which to open the file.
- `encoding` — `str | None`: The encoding to decode or encode a file opened in text mode.
- `errors` — `str | None`: The error handling mode.
- `lazy` — `bool`: Wait to open the file until it is accessed. For read mode, the file is temporarily opened to raise access errors early, then closed until it is read again.
- `atomic` — `bool`: Write to a temporary file and replace the given file on close.

**Returns**:
- `t.IO[t.Any]`: A file-like object.

**Raises**:
- None

**内部调用(库内):**
- [`LazyFile`](src_click.md#sym-src_click_utils.py-112) — `LazyFile` 类提供了一个延迟打开文件的机制，只有在实际需要时才打开文件，从而节省资源。
- [`open_stream`](src_click.md#sym-src_click__compat.py-370) — `open_stream`
- [`KeepOpenFile`](src_click.md#sym-src_click_utils.py-206) — `KeepOpenFile` 类用于包装一个文件对象，确保在上下文管理器中使用时文件保持打开状态，直到显式关闭。

*来源: `src/click/utils.py:376`*

---
<a id="sym-src_click_utils.py-425"></a>
### `format_filename` · func
```python
def format_filename(
    filename: str | bytes | os.PathLike[str] | os.PathLike[bytes],
    shorten: bool = False,
) -> str
```

Format a filename for display, ensuring it can be displayed by replacing any invalid bytes or surrogate escapes with the replacement character ``�``.

**Parameters**:
- `filename` — `str | bytes | os.PathLike[str] | os.PathLike[bytes]` — The filename to format.
- `shorten` — `bool` — Whether to shorten the filename by stripping the path.

**Returns**:
- `str` — The formatted filename.

**Raises**:
- None

*来源: `src/click/utils.py:425`*

---
<a id="sym-src_click_utils.py-467"></a>
### `get_app_dir` · func
```python
def get_app_dir(app_name: str, roaming: bool = True, force_posix: bool = False) -> str
```

Returns the configuration folder for the application based on the operating system.

**Parameters**:
- `app_name` — `str` — The application name, properly capitalized and can contain whitespace.
- `roaming` — `bool` — Controls if the folder should be roaming or not on Windows. Has no effect otherwise.
- `force_posix` — `bool` — If set to `True`, then on any POSIX system the folder will be stored in the home folder with a leading dot instead of the XDG config home or darwin's application support folder.

**Returns**:
- `str` — The path to the application's configuration folder.

**Raises**:
- None

**内部调用(库内):**
- [`_posixify`](src_click.md#sym-src_click_utils.py-32) — 将字符串转换为 POSIX 兼容的格式。

*来源: `src/click/utils.py:467`*

---
<a id="sym-src_click_utils.py-516"></a>
### `PacifyFlushWrapper` · class
```python
class PacifyFlushWrapper
```

`PacifyFlushWrapper` 是一个包装器类，用于在不立即刷新底层文件对象的情况下提供一个文件对象的接口。

- **Parameters**:
  - `wrapped` — `t.IO[t.Any]` — 要包装的底层文件对象。

- **Returns**:
  - `None`

- **Raises**:
  - 无

*来源: `src/click/utils.py:516`*

---
<a id="sym-src_click_utils.py-527"></a>
### `PacifyFlushWrapper.__init__` · method
```python
def __init__(self, wrapped: t.IO[t.Any]) -> None
```

### PacifyFlushWrapper.__init__

初始化 `PacifyFlushWrapper` 对象。

**Parameters**:
- `wrapped` — `t.IO[t.Any]` — 被包装的文件对象。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `src/click/utils.py:527`*

---
<a id="sym-src_click_utils.py-530"></a>
### `PacifyFlushWrapper.flush` · method
```python
def flush(self) -> None
```

### PacifyFlushWrapper.flush

Flushes the wrapped stream, ignoring `OSError` with `errno.EPIPE`.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- OSError: If an `OSError` occurs with an error number other than `errno.EPIPE`.

*来源: `src/click/utils.py:530`*

---
<a id="sym-src_click_utils.py-539"></a>
### `PacifyFlushWrapper.__getattr__` · method
```python
def __getattr__(self, attr: str) -> t.Any
```

### PacifyFlushWrapper.__getattr__

递归调用 `self.wrapped` 的 `__getattr__` 方法，获取指定属性。

**Parameters**:
- `attr` — `str` — 要获取的属性名称。

**Returns**:
- `t.Any` — `self.wrapped` 对应属性的值。

**Raises**:
- 无

*来源: `src/click/utils.py:539`*

---
<a id="sym-src_click_utils.py-543"></a>
### `_detect_program_name` · func
```python
def _detect_program_name(
    path: str | None = None, _main: ModuleType | None = None
) -> str
```

Determine the command used to run the program, for use in help text. If a file or entry point was executed, the file name is returned. If ``python -m`` was used to execute a module or package, ``python -m name`` is returned.

**Parameters**:
- `path` — `str | None` — The Python file being executed. Python puts this in `sys.argv[0]`, which is used by default.
- `_main` — `ModuleType | None` — The `__main__` module. This should only be passed during internal testing.

**Returns**:
- `str` — The command used to run the program.

**Raises**:
- None

*来源: `src/click/utils.py:543`*

---
<a id="sym-src_click_utils.py-598"></a>
### `_expand_args` · func
```python
def _expand_args(
    args: cabc.Iterable[str],
    *,
    user: bool = True,
    env: bool = True,
    glob_recursive: bool = True,
) -> list[str]
```

Simulate Unix shell expansion with Python functions.

**Parameters**:
- `args` — `cabc.Iterable[str]` — List of command line arguments to expand.
- `user` — `bool` — Expand user home directory. Default is `True`.
- `env` — `bool` — Expand environment variables. Default is `True`.
- `glob_recursive` — `bool` — ``**`` matches directories recursively. Default is `True`.

**Returns**:
- `list[str]` — Expanded list of command line arguments.

**Raises**:
- None

*来源: `src/click/utils.py:598`*

---