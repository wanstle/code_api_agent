# API 参考:`examples/inout`


## `examples/inout/inout.py`

<a id="sym-examples_inout_inout.py-7"></a>
### `cli` · func
装饰器: `@click.command()` `@click.argument("input", type=click.File("rb"), nargs=-1)` `@click.argument("output", type=click.File("wb"))`
```python
def cli(input, output)
```

This script works similar to the Unix `cat` command but it writes into a specific file (which could be the standard output as denoted by the ``-`` sign).

**Parameters**:
- `input` — list — A list of file-like objects to read from.
- `output` — file-like — The file-like object to write to.

**Returns**:
- None

**Raises**:
- None

*来源: `examples/inout/inout.py:7`*

---