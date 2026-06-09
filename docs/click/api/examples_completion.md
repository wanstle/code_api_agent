# API 参考:`examples/completion`


## `examples/completion/completion.py`

<a id="sym-examples_completion_completion.py-8"></a>
### `cli` · func
装饰器: `@click.group()`
```python
def cli()
```

用途: 定义主命令行接口。

**Parameters**:
- 无

**Returns**:
- 无

**Raises**:
- 无

*来源: `examples/completion/completion.py:8`*

---
<a id="sym-examples_completion_completion.py-14"></a>
### `ls` · func
装饰器: `@cli.command()` `@click.option("--dir", type=click.Path(file_okay=False))`
```python
def ls(dir)
```

**用途**: 列出指定目录中的文件和子目录。

**Parameters**:
- `dir` — `str` — 要列出内容的目录路径。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `examples/completion/completion.py:14`*

---
<a id="sym-examples_completion_completion.py-18"></a>
### `get_env_vars` · func
```python
def get_env_vars(ctx, param, incomplete):
    # Returning a list of values is a shortcut to returning a list of
    # CompletionItem(value).
```

### get_env_vars

Returns a list of environment variable names that contain the specified incomplete string.

**Parameters:**
- `ctx` — `Context` — The current context.
- `param` — `Parameter` — The parameter being processed.
- `incomplete` — `str` — The incomplete string to filter environment variable names.

**Returns:**
- `list` — A list of environment variable names that contain the specified incomplete string.

*来源: `examples/completion/completion.py:18`*

---
<a id="sym-examples_completion_completion.py-26"></a>
### `show_env` · func
装饰器: `@cli.command(help="A command to print environment variables")` `@click.argument("envvar", shell_complete=get_env_vars)`
```python
def show_env(envvar)
```

显示指定环境变量的值。

**Parameters**:
- `envvar` — `str` — 要显示的环境变量名称。

**Returns**:
- `None`

**Raises**:
- `KeyError` — 如果指定的环境变量不存在。

*来源: `examples/completion/completion.py:26`*

---
<a id="sym-examples_completion_completion.py-32"></a>
### `group` · func
装饰器: `@cli.group(help="A group that holds a subcommand")`
```python
def group()
```

用途: 定义一个命令组。

**Parameters**:
- 无

**Returns**:
- `Group` — 命令组对象

**Raises**:
- 无

*来源: `examples/completion/completion.py:32`*

---
<a id="sym-examples_completion_completion.py-36"></a>
### `list_users` · func
```python
def list_users(ctx, param, incomplete):
    # You can generate completions with help strings by returning a list
    # of CompletionItem. You can match on whatever you want, including
    # the help.
```

### list_users

生成用户列表的自动补全项。

**Parameters**:
- `ctx` — `Context` — 上下文对象。
- `param` — `Parameter` — 当前参数对象。
- `incomplete` — `str` — 当前输入的不完整字符串。

**Returns**:
- `list[CompletionItem]` — 匹配的自动补全项列表。

**Raises**:
- 无

**内部调用(库内):**
- [`CompletionItem`](src_click.md#sym-src_click_shell_completion.py-58) — `CompletionItem` 类用于表示命令行工具中的自动补全项。

*来源: `examples/completion/completion.py:36`*

---
<a id="sym-examples_completion_completion.py-52"></a>
### `select_user` · func
装饰器: `@group.command(help="Choose a user")` `@click.argument("user", shell_complete=list_users)`
```python
def select_user(user)
```

选择并显示用户。

**Parameters**:
- user — str — 用户名

**Returns**:
- 无

**Raises**:
- 无

*来源: `examples/completion/completion.py:52`*

---