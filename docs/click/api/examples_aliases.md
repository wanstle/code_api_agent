# API 参考:`examples/aliases`


## `examples/aliases/aliases.py`

<a id="sym-examples_aliases_aliases.py-7"></a>
### `Config` · class
```python
class Config
```

`Config` 类用于管理命令别名和配置文件的读写。

- **__init__(self)**
  - **Parameters**: None
  - **Returns**: None
  - **Raises**: None

- **add_alias(self, alias, cmd)**
  - **Parameters**: 
    - `alias` — `str` — 别名名称。
    - `cmd` — `str` — 命令名称。
  - **Returns**: None
  - **Raises**: None

- **read_config(self, filename)**
  - **Parameters**: 
    - `filename` — `str` — 配置文件路径。
  - **Returns**: None
  - **Raises**: None

- **write_config(self, filename)**
  - **Parameters**: 
    - `filename` — `str` — 配置文件路径。
  - **Returns**: None
  - **Raises**: None

*来源: `examples/aliases/aliases.py:7`*

---
<a id="sym-examples_aliases_aliases.py-10"></a>
### `Config.__init__` · method
```python
def __init__(self)
```

初始化一个 `Config` 对象，设置默认路径和空别名字典。

**Parameters**:
- 无

**Returns**:
- `None`

**Raises**:
- 无

*来源: `examples/aliases/aliases.py:10`*

---
<a id="sym-examples_aliases_aliases.py-14"></a>
### `Config.add_alias` · method
```python
def add_alias(self, alias, cmd)
```

用途: 添加一个别名到配置中。

**Parameters**:
- `alias` — `str` — 别名的名称。
- `cmd` — `str` — 别名对应的命令。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `examples/aliases/aliases.py:14`*

---
<a id="sym-examples_aliases_aliases.py-17"></a>
### `Config.read_config` · method
```python
def read_config(self, filename)
```

读取配置文件并更新别名。

**Parameters**:
- `filename` — `str` — 配置文件的路径。

**Returns**:
- `None`

**Raises**:
- `configparser.NoSectionError` — 如果配置文件中没有 "aliases" 部分。

*来源: `examples/aliases/aliases.py:17`*

---
<a id="sym-examples_aliases_aliases.py-25"></a>
### `Config.write_config` · method
```python
def write_config(self, filename)
```

用途: 将配置写入指定文件。

**Parameters**:
- `filename` — `str` — 配置文件的路径。

**Returns**:
- `None`

**Raises**:
- `None`

*来源: `examples/aliases/aliases.py:25`*

---
<a id="sym-examples_aliases_aliases.py-37"></a>
### `AliasedGroup` · class
```python
class AliasedGroup(click.Group)
```

`AliasedGroup` 类继承自 `click.Group`，用于处理命令别名，使得用户可以通过别名来调用命令。

### 方法

#### `get_command(self, ctx, cmd_name)`

- **Parameters**:
  - `ctx` — `click.Context` — 上下文对象。
  - `cmd_name` — `str` — 用户输入的命令名称或别名。

- **Returns**:
  - `click.Command` — 对应的命令对象，如果找不到命令则返回 `None`。

#### `resolve_command(self, ctx, args)`

- **Parameters**:
  - `ctx` — `click.Context` — 上下文对象。
  - `args` — `list` — 命令行参数列表。

- **Returns**:
  - `str` — 命令的名称，不包括别名。

- **Raises**:
  - `click.NoSuchCommand` — 如果找不到命令。

*来源: `examples/aliases/aliases.py:37`*

---
<a id="sym-examples_aliases_aliases.py-42"></a>
### `AliasedGroup.get_command` · method
```python
def get_command(self, ctx, cmd_name):
        # Step one: built-in commands as normal
```

### AliasedGroup.get_command

获取指定命令对象。如果命令名称在配置中存在别名，则返回别名对应的命令对象；如果不存在别名，则尝试自动缩写命令名称。如果匹配到多个命令，则抛出异常。

**Parameters**:
- `ctx` — `click.Context` — 上下文对象。
- `cmd_name` — `str` — 命令名称。

**Returns**:
- `click.Command` — 命令对象，如果找到匹配的命令；否则返回 `None`。

**Raises**:
- `click.UsageError` — 如果存在多个匹配的命令。

**内部调用(库内):**
- [`Context.ensure_object`](src_click.md#sym-src_click_core.py-748) — **用途**: 确保在当前上下文中存在指定类型的对象，如果不存在则创建一个新的实例。

*来源: `examples/aliases/aliases.py:42`*

---
<a id="sym-examples_aliases_aliases.py-70"></a>
### `AliasedGroup.resolve_command` · method
```python
def resolve_command(self, ctx, args):
        # always return the command's name, not the alias
```

### `AliasedGroup.resolve_command`

用途: 解析命令并返回命令的名称，而不是别名。

**Parameters**:
- `ctx` — `Context` — 上下文对象。
- `args` — `list` — 命令行参数列表。

**Returns**:
- `tuple` — 包含命令名称、命令对象和剩余参数。

**Raises**:
- 无

*来源: `examples/aliases/aliases.py:70`*

---
<a id="sym-examples_aliases_aliases.py-76"></a>
### `read_config` · func
```python
def read_config(ctx, param, value)
```

### 用途
处理 `--config` 选项的回调函数，确保在任何时候加载正确的配置文件，即使组本身从未执行。

### Parameters
- `ctx` — `Context` — 上下文对象，提供有关命令和参数的信息。
- `param` — `Parameter` — 当前处理的参数对象。
- `value` — `str | None` — 传递给 `--config` 选项的值，如果未提供则为 `None`。

### Returns
- `str` — 配置文件的路径。

### Raises
- 无

**内部调用(库内):**
- [`Context.ensure_object`](src_click.md#sym-src_click_core.py-748) — **用途**: 确保在当前上下文中存在指定类型的对象，如果不存在则创建一个新的实例。

*来源: `examples/aliases/aliases.py:76`*

---
<a id="sym-examples_aliases_aliases.py-97"></a>
### `cli` · func
装饰器: `@click.command(cls=AliasedGroup)` `@click.option(
    "--config",
    type=click.Path(exists=True, dir_okay=False),
    callback=read_config,
    expose_value=False,
    help="The config file to use instead of the default.",
)`
```python
def cli()
```

An example application that supports aliases.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `examples/aliases/aliases.py:97`*

---
<a id="sym-examples_aliases_aliases.py-102"></a>
### `push` · func
装饰器: `@cli.command()`
```python
def push()
```

Pushes changes.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `examples/aliases/aliases.py:102`*

---
<a id="sym-examples_aliases_aliases.py-108"></a>
### `pull` · func
装饰器: `@cli.command()`
```python
def pull()
```

用途: 拉取更改。

**Parameters**:
- 无

**Returns**:
- 无

**Raises**:
- 无

*来源: `examples/aliases/aliases.py:108`*

---
<a id="sym-examples_aliases_aliases.py-114"></a>
### `clone` · func
装饰器: `@cli.command()`
```python
def clone()
```

Clones a repository.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `examples/aliases/aliases.py:114`*

---
<a id="sym-examples_aliases_aliases.py-120"></a>
### `commit` · func
装饰器: `@cli.command()`
```python
def commit()
```

Commits pending changes.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `examples/aliases/aliases.py:120`*

---
<a id="sym-examples_aliases_aliases.py-127"></a>
### `status` · func
装饰器: `@cli.command()` `@pass_config`
```python
def status(config)
```

### 用途
显示配置的状态。

### Parameters
- `config` — `Config` — 配置对象。

### Returns
- `None`

### Raises
- 无

*来源: `examples/aliases/aliases.py:127`*

---
<a id="sym-examples_aliases_aliases.py-139"></a>
### `alias` · func
装饰器: `@cli.command()` `@pass_config` `@click.argument("alias_", metavar="ALIAS", type=click.STRING)` `@click.argument("cmd", type=click.STRING)` `@click.option(
    "--config_file", type=click.Path(exists=True, dir_okay=False), default="aliases.ini"
)`
```python
def alias(config, alias_, cmd, config_file)
```

Adds an alias to the specified configuration file.

**Parameters**:
- `config` — `Config` — The configuration object.
- `alias_` — `str` — The alias to be added.
- `cmd` — `str` — The command to which the alias is associated.
- `config_file` — `str` — The path to the configuration file.

**Returns**:
- `None`

**Raises**:
- None

**内部调用(库内):**
- [`Config.add_alias`](examples_aliases.md#sym-examples_aliases_aliases.py-14) — 用途: 添加一个别名到配置中。
- [`Config.write_config`](examples_aliases.md#sym-examples_aliases_aliases.py-25) — 用途: 将配置写入指定文件。

*来源: `examples/aliases/aliases.py:139`*

---