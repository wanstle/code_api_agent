# API 参考:`examples/naval`


## `examples/naval/naval.py`

<a id="sym-examples_naval_naval.py-6"></a>
### `cli` · func
装饰器: `@click.group()` `@click.version_option()`
```python
def cli()
```

Naval Fate.

- **Returns**: `None`
- **Raises**: `None`

*来源: `examples/naval/naval.py:6`*

---
<a id="sym-examples_naval_naval.py-16"></a>
### `ship` · func
装饰器: `@cli.group()`
```python
def ship()
```

用途: 管理船只。

**Parameters**:
- 无

**Returns**:
- 无

**Raises**:
- 无

*来源: `examples/naval/naval.py:16`*

---
<a id="sym-examples_naval_naval.py-22"></a>
### `ship_new` · func
装饰器: `@ship.command("new")` `@click.argument("name")`
```python
def ship_new(name)
```

**用途**: 创建一艘新船。

**Parameters**:
- `name` — `str` — 船的名称。

**Returns**:
- `None`

**Raises**:
- 无

*来源: `examples/naval/naval.py:22`*

---
<a id="sym-examples_naval_naval.py-32"></a>
### `ship_move` · func
装饰器: `@ship.command("move")` `@click.argument("ship")` `@click.argument("x", type=float)` `@click.argument("y", type=float)` `@click.option("--speed", metavar="KN", default=10, help="Speed in knots.")`
```python
def ship_move(ship, x, y, speed)
```

Moves a ship to a new location.

**Parameters**:
- ship — str — The name of the ship.
- x — int — The new X coordinate.
- y — int — The new Y coordinate.
- speed — int — The speed of the ship.

**Returns**:
- None

**Raises**:
- None

*来源: `examples/naval/naval.py:32`*

---
<a id="sym-examples_naval_naval.py-41"></a>
### `ship_shoot` · func
装饰器: `@ship.command("shoot")` `@click.argument("ship")` `@click.argument("x", type=float)` `@click.argument("y", type=float)`
```python
def ship_shoot(ship, x, y)
```

**用途**: Makes a ship fire at specified coordinates.

**Parameters**:
- `ship` — str — The name of the ship.
- `x` — int — The X coordinate.
- `y` — int — The Y coordinate.

**Returns**:
- None

**Raises**:
- None

*来源: `examples/naval/naval.py:41`*

---
<a id="sym-examples_naval_naval.py-47"></a>
### `mine` · func
装饰器: `@cli.group("mine")`
```python
def mine()
```

Manages mines.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `examples/naval/naval.py:47`*

---
<a id="sym-examples_naval_naval.py-62"></a>
### `mine_set` · func
装饰器: `@mine.command("set")` `@click.argument("x", type=float)` `@click.argument("y", type=float)` `@click.option(
    "ty",
    "--moored",
    flag_value="moored",
    default=True,
    help="Moored (anchored) mine. Default.",
)` `@click.option("ty", "--drifting", flag_value="drifting", help="Drifting mine.")`
```python
def mine_set(x, y, ty)
```

Sets a mine at a specific coordinate.

**Parameters**:
- x — int — The x-coordinate of the mine.
- y — int — The y-coordinate of the mine.
- ty — str — The type of mine.

**Returns**:
- None

**Raises**:
- None

*来源: `examples/naval/naval.py:62`*

---
<a id="sym-examples_naval_naval.py-70"></a>
### `mine_remove` · func
装饰器: `@mine.command("remove")` `@click.argument("x", type=float)` `@click.argument("y", type=float)`
```python
def mine_remove(x, y)
```

**用途**: Removes a mine at a specific coordinate.

**Parameters**:
- `x` — `int` — The x-coordinate of the mine.
- `y` — `int` — The y-coordinate of the mine.

**Returns**:
- `None`

**Raises**:
- (无)

*来源: `examples/naval/naval.py:70`*

---