# API 参考:`examples/complex`


## `examples/complex/complex/cli.py`

<a id="sym-examples_complex_complex_cli.py-10"></a>
### `Environment` · class
```python
class Environment
```

`Environment` 类代表一个应用程序的运行环境，负责日志记录和调试信息的输出。

- **__init__(self)**
  - **Parameters**: 无
  - **Returns**: 无
  - **Raises**: 无

- **log(self, msg, *args)**
  - **Parameters**: 
    - `msg` — `str` — 要记录的日志消息。
    - `*args` — `tuple` — 可选参数，用于格式化日志消息。
  - **Returns**: 无
  - **Raises**: 无

- **vlog(self, msg, *args)**
  - **Parameters**: 
    - `msg` — `str` — 要记录的调试信息。
    - `*args` — `tuple` — 可选参数，用于格式化调试信息。
  - **Returns**: 无
  - **Raises**: 无

*来源: `examples/complex/complex/cli.py:10`*

---
<a id="sym-examples_complex_complex_cli.py-11"></a>
### `Environment.__init__` · method
```python
def __init__(self)
```

初始化一个 `Environment` 对象。

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `examples/complex/complex/cli.py:11`*

---
<a id="sym-examples_complex_complex_cli.py-15"></a>
### `Environment.log` · method
```python
def log(self, msg, *args)
```

用途: Logs a message to stderr.

**Parameters**:
- `msg` — `str` — The message to log.
- `*args` — `tuple` — Additional arguments to format the message.

**Returns**:
- `None`

**Raises**:
- `None`

*来源: `examples/complex/complex/cli.py:15`*

---
<a id="sym-examples_complex_complex_cli.py-21"></a>
### `Environment.vlog` · method
```python
def vlog(self, msg, *args)
```

### Environment.vlog

Logs a message to stderr only if verbose is enabled.

**Parameters**:
- `msg` — `str` — The message to log.
- `*args` — `tuple` — Additional arguments to pass to the log function.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Environment.log`](examples_complex.md#sym-examples_complex_complex_cli.py-15) — 用途: Logs a message to stderr.

*来源: `examples/complex/complex/cli.py:21`*

---
<a id="sym-examples_complex_complex_cli.py-31"></a>
### `ComplexCLI` · class
```python
class ComplexCLI(click.Group)
```

`ComplexCLI` 是一个自定义的 Click 组命令类，用于管理复杂的命令集合。

### 方法

#### list_commands(self, ctx)

- **Parameters**:
  - `ctx` — `click.Context` — 上下文对象，包含命令的上下文信息。
- **Returns**:
  - `list` — 返回一个包含所有命令名称的列表。
- **Raises**:
  - 无

#### get_command(self, ctx, name)

- **Parameters**:
  - `ctx` — `click.Context` — 上下文对象，包含命令的上下文信息。
  - `name` — `str` — 要获取的命令名称。
- **Returns**:
  - `click.Command` — 返回指定名称的命令对象。
- **Raises**:
  - 无

*来源: `examples/complex/complex/cli.py:31`*

---
<a id="sym-examples_complex_complex_cli.py-32"></a>
### `ComplexCLI.list_commands` · method
```python
def list_commands(self, ctx)
```

### 用途
列出指定文件夹中所有以 `cmd_` 开头并以 `.py` 结尾的文件名，不包括文件扩展名。

### Parameters
- `ctx` — `Context` — 上下文对象。

### Returns
- `list` — 排序后的命令列表。

### Raises
- 无

*来源: `examples/complex/complex/cli.py:32`*

---
<a id="sym-examples_complex_complex_cli.py-40"></a>
### `ComplexCLI.get_command` · method
```python
def get_command(self, ctx, name)
```

### 用途
获取指定名称的命令对象。

### Parameters
- `ctx` — `Context` — 上下文对象。
- `name` — `str` — 命令名称。

### Returns
- `cli` — `Command` — 命令对象，如果找到；否则返回 `None`。

### Raises
- `ImportError` — 如果指定的命令模块无法导入。

*来源: `examples/complex/complex/cli.py:40`*

---
<a id="sym-examples_complex_complex_cli.py-56"></a>
### `cli` · func
装饰器: `@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)` `@click.option(
    "--home",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    help="Changes the folder to operate on.",
)` `@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")` `@pass_environment`
```python
def cli(ctx, verbose, home)
```

A complex command line interface.

**Parameters**:
- `ctx` — `Context` — The context object for the command.
- `verbose` — `bool` — Whether the command should operate in verbose mode.
- `home` — `str` — The home directory to use for the command.

**Returns**:
- `None`

**Raises**:
- None

*来源: `examples/complex/complex/cli.py:56`*

---

## `examples/complex/complex/commands/cmd_init.py`

<a id="sym-examples_complex_complex_commands_cmd_init.py-9"></a>
### `cli` · func
装饰器: `@click.command("init", short_help="Initializes a repo.")` `@click.argument("path", required=False, type=click.Path(resolve_path=True))` `@pass_environment`
```python
def cli(ctx, path)
```

**用途**: Initializes a repository.

**Parameters**:
- `ctx` — `Environment` — The context object.
- `path` — `str | bytes | os.PathLike[str] | os.PathLike[bytes]` — The path to the repository. If `None`, it defaults to the home directory.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Environment.log`](examples_complex.md#sym-examples_complex_complex_cli.py-15) — 用途: Logs a message to stderr.
- [`format_filename`](src_click.md#sym-src_click_utils.py-425) — Format a filename for display, ensuring it can be displayed by replacing any inv

*来源: `examples/complex/complex/commands/cmd_init.py:9`*

---

## `examples/complex/complex/commands/cmd_status.py`

<a id="sym-examples_complex_complex_commands_cmd_status.py-8"></a>
### `cli` · func
装饰器: `@click.command("status", short_help="Shows file changes.")` `@pass_environment`
```python
def cli(ctx)
```

### 用途
显示当前工作目录中的文件更改。

### Parameters
- `ctx` — `Environment` — 上下文对象，包含日志和调试信息的方法。

### Returns
- `None`

### Raises
- 无

**内部调用(库内):**
- [`Environment.log`](examples_complex.md#sym-examples_complex_complex_cli.py-15) — 用途: Logs a message to stderr.
- [`Environment.vlog`](examples_complex.md#sym-examples_complex_complex_cli.py-21) — Environment.vlog

*来源: `examples/complex/complex/commands/cmd_status.py:8`*

---