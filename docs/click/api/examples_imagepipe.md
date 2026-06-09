# API 参考:`examples/imagepipe`


## `examples/imagepipe/imagepipe.py`

<a id="sym-examples_imagepipe_imagepipe.py-11"></a>
### `cli` · func
装饰器: `@click.group(chain=True)`
```python
def cli()
```

This script processes a bunch of images through pillow in a unix pipe. One commands feeds into the next.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None

*来源: `examples/imagepipe/imagepipe.py:11`*

---
<a id="sym-examples_imagepipe_imagepipe.py-24"></a>
### `process_commands` · func
装饰器: `@cli.result_callback()`
```python
def process_commands(processors)
```

This function processes a sequence of commands by chaining them together.

**Parameters**:
- processors — list — An iterable of processor functions that will be applied sequentially to a stream of commands.

**Returns**:
- None

**Raises**:
- None

**内部调用(库内):**
- [`processor`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-42) — Helper decorator to rewrite a function so that it returns another function from 

*来源: `examples/imagepipe/imagepipe.py:24`*

---
<a id="sym-examples_imagepipe_imagepipe.py-42"></a>
### `processor` · func
```python
def processor(f)
```

Helper decorator to rewrite a function so that it returns another function from it.

**Parameters**:
- `f` — function — The function to be decorated.

**Returns**:
- function — A new function that returns another function.

**Raises**:
- None

*来源: `examples/imagepipe/imagepipe.py:42`*

---
<a id="sym-examples_imagepipe_imagepipe.py-47"></a>
### `new_func` · func
```python
def new_func(*args, **kwargs)
```

**用途**: 创建一个处理器函数，该处理器函数接受一个流并返回处理后的流。

**Parameters**:
- `*args` — `tuple` — 传递给处理器函数的额外参数。
- `**kwargs` — `dict` — 传递给处理器函数的额外关键字参数。

**Returns**:
- `function` — 返回一个处理器函数，该函数接受一个流并返回处理后的流。

*来源: `examples/imagepipe/imagepipe.py:47`*

---
<a id="sym-examples_imagepipe_imagepipe.py-48"></a>
### `processor` · func
```python
def processor(stream)
```

用途: 处理输入流。

**Parameters**:
- `stream` — `any` — 输入流。

**Returns**:
- `any` — 处理后的结果。

**Raises**:
- 无

*来源: `examples/imagepipe/imagepipe.py:48`*

---
<a id="sym-examples_imagepipe_imagepipe.py-56"></a>
### `generator` · func
```python
def generator(f)
```

**用途**: 创建一个生成器函数，该函数将旧值传递不变，并不将值作为参数传递。

**Parameters**:
- `f` — function — 要包装的函数。

**Returns**:
- function — 返回一个新的生成器函数。

**Raises**:
- 无

*来源: `examples/imagepipe/imagepipe.py:56`*

---
<a id="sym-examples_imagepipe_imagepipe.py-62"></a>
### `new_func` · func
装饰器: `@processor`
```python
def new_func(stream, *args, **kwargs)
```

用途: 递归地生成并返回 `stream` 和 `f(*args, **kwargs)` 的内容。

**Parameters**:
- `stream` — 生成器 — 用于生成内容的生成器。
- `*args` — 任意类型 — 传递给 `f` 的位置参数。
- `**kwargs` — 任意类型 — 传递给 `f` 的关键字参数。

**Returns**:
- 生成器 — 递归地生成 `stream` 和 `f(*args, **kwargs)` 的内容。

**Raises**:
- 无

*来源: `examples/imagepipe/imagepipe.py:62`*

---
<a id="sym-examples_imagepipe_imagepipe.py-69"></a>
### `copy_filename` · func
```python
def copy_filename(new, old)
```

用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

**Parameters**:
- `new` — object — 目标对象，其 `filename` 属性将被设置。
- `old` — object — 源对象，其 `filename` 属性将被复制。

**Returns**:
- object — 返回 `new` 对象，其 `filename` 属性已更新。

*来源: `examples/imagepipe/imagepipe.py:69`*

---
<a id="sym-examples_imagepipe_imagepipe.py-84"></a>
### `open_cmd` · func
装饰器: `@cli.command("open")` `@click.option(
    "-i",
    "--image",
    "images",
    type=click.Path(),
    multiple=True,
    help="The image file to open.",
)` `@generator`
```python
def open_cmd(images)
```

Loads one or multiple images for processing. The input parameter can be specified multiple times to load more than one image.

**Parameters**:
- images — list — A list of image file paths or a single file path to be opened.

**Returns**:
- generator — Yields an image object for each image file path provided.

**Raises**:
- Exception — If an error occurs while opening an image, an error message is printed to the standard error stream.

**内部调用(库内):**
- [`get_binary_stdin`](src_click.md#sym-src_click__compat.py-315) — 获取二进制标准输入流。

*来源: `examples/imagepipe/imagepipe.py:84`*

---
<a id="sym-examples_imagepipe_imagepipe.py-110"></a>
### `save_cmd` · func
装饰器: `@cli.command("save")` `@click.option(
    "--filename",
    default="processed-{:04}.png",
    type=click.Path(),
    help="The format for the filename.",
    show_default=True,
)` `@processor`
```python
def save_cmd(images, filename)
```

Saves all processed images to a series of files.

**Parameters**:
- images — list — A list of images to be saved.
- filename — str — The filename template for the saved images.

**Returns**:
- None

**Raises**:
- None

*来源: `examples/imagepipe/imagepipe.py:110`*

---
<a id="sym-examples_imagepipe_imagepipe.py-123"></a>
### `display_cmd` · func
装饰器: `@cli.command("display")` `@processor`
```python
def display_cmd(images)
```

**用途**: Opens all images in an image viewer.

**Parameters**:
- `images` — `list` — A list of image objects to be displayed.

**Returns**:
- `generator` — Yields each image object after displaying it.

**Raises**:
- None

*来源: `examples/imagepipe/imagepipe.py:123`*

---
<a id="sym-examples_imagepipe_imagepipe.py-135"></a>
### `resize_cmd` · func
装饰器: `@cli.command("resize")` `@click.option("-w", "--width", type=int, help="The new width of the image.")` `@click.option("-h", "--height", type=int, help="The new height of the image.")` `@processor`
```python
def resize_cmd(images, width, height)
```

Resizes an image by fitting it into the box without changing the aspect ratio.

**Parameters**:
- images — list — A list of images to resize.
- width — int — The new width of the image. If None, the original width is used.
- height — int — The new height of the image. If None, the original height is used.

**Returns**:
- generator — A generator that yields the resized images.

**Raises**:
- None

*来源: `examples/imagepipe/imagepipe.py:135`*

---
<a id="sym-examples_imagepipe_imagepipe.py-151"></a>
### `crop_cmd` · func
装饰器: `@cli.command("crop")` `@click.option(
    "-b", "--border", type=int, help="Crop the image from all sides by this amount."
)` `@processor`
```python
def crop_cmd(images, border)
```

Crops an image from all edges by a specified border.

**Parameters**:
- images — list — A list of images to be cropped.
- border — int — The number of pixels to crop from each edge of the image.

**Returns**:
- list — A list of cropped images.

**Raises**:
- None

**内部调用(库内):**
- [`copy_filename`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-69) — 用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

*来源: `examples/imagepipe/imagepipe.py:151`*

---
<a id="sym-examples_imagepipe_imagepipe.py-165"></a>
### `convert_rotation` · func
```python
def convert_rotation(ctx, param, value)
```

Converts a rotation value to a tuple representing the rotation method and degrees.

**Parameters**:
- `ctx` — `Context` — The context object.
- `param` — `Parameter` — The parameter object.
- `value` — `str` — The rotation value to convert.

**Returns**:
- `tuple` — A tuple containing the rotation method and degrees.

**Raises**:
- `BadParameter` — If the rotation value is invalid.

**内部调用(库内):**
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `examples/imagepipe/imagepipe.py:165`*

---
<a id="sym-examples_imagepipe_imagepipe.py-178"></a>
### `convert_flip` · func
```python
def convert_flip(ctx, param, value)
```

Converts a string value representing a flip direction into a tuple containing the corresponding Image.FLIP constant and a description.

**Parameters**:
- `ctx` — `Context` — The context object.
- `param` — `Parameter` — The parameter object.
- `value` — `str` — The value to convert.

**Returns**:
- `tuple` — A tuple containing the corresponding Image.FLIP constant and a description.

**Raises**:
- `BadParameter` — If the value is invalid.

**内部调用(库内):**
- [`BadParameter`](src_click.md#sym-src_click_exceptions.py-114) — `BadParameter` 类继承自 `UsageError`，用于表示在命令行参数解析过程中遇到无效参数的情况。

*来源: `examples/imagepipe/imagepipe.py:178`*

---
<a id="sym-examples_imagepipe_imagepipe.py-195"></a>
### `transpose_cmd` · func
装饰器: `@cli.command("transpose")` `@click.option(
    "-r", "--rotate", callback=convert_rotation, help="Rotates the image (in degrees)"
)` `@click.option("-f", "--flip", callback=convert_flip, help="Flips the image  [LR / TB]")` `@processor`
```python
def transpose_cmd(images, rotate, flip)
```

Transposes an image by either rotating or flipping it.

**Parameters**:
- images — list — A list of image objects to be transposed.
- rotate — tuple — A tuple containing the rotation mode and degrees.
- flip — tuple — A tuple containing the flip mode and direction.

**Returns**:
- generator — A generator that yields the transposed image objects.

**Raises**:
- None

**内部调用(库内):**
- [`copy_filename`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-69) — 用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

*来源: `examples/imagepipe/imagepipe.py:195`*

---
<a id="sym-examples_imagepipe_imagepipe.py-212"></a>
### `blur_cmd` · func
装饰器: `@cli.command("blur")` `@click.option("-r", "--radius", default=2, show_default=True, help="The blur radius.")` `@processor`
```python
def blur_cmd(images, radius)
```

Applies gaussian blur to a list of images.

**Parameters**:
- images — list — A list of images to be blurred.
- radius — int — The radius of the gaussian blur.

**Returns**:
- generator — A generator that yields the blurred images.

**Raises**:
- None

**内部调用(库内):**
- [`copy_filename`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-69) — 用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

*来源: `examples/imagepipe/imagepipe.py:212`*

---
<a id="sym-examples_imagepipe_imagepipe.py-229"></a>
### `smoothen_cmd` · func
装饰器: `@cli.command("smoothen")` `@click.option(
    "-i",
    "--iterations",
    default=1,
    show_default=True,
    help="How many iterations of the smoothen filter to run.",
)` `@processor`
```python
def smoothen_cmd(images, iterations)
```

Applies a smoothening filter to each image in the given list for a specified number of iterations.

**Parameters**:
- images — list — A list of image objects to be smoothened.
- iterations — int — The number of times the smoothening filter should be applied to each image.

**Returns**:
- generator — A generator that yields the smoothened image objects.

**Raises**:
- None

**内部调用(库内):**
- [`copy_filename`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-69) — 用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

*来源: `examples/imagepipe/imagepipe.py:229`*

---
<a id="sym-examples_imagepipe_imagepipe.py-243"></a>
### `emboss_cmd` · func
装饰器: `@cli.command("emboss")` `@processor`
```python
def emboss_cmd(images)
```

Embosses an image.

**Parameters**:
- images — list — A list of image objects to be embossed.

**Returns**:
- generator — A generator that yields the embossed image objects.

**Raises**:
- None

**内部调用(库内):**
- [`copy_filename`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-69) — 用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

*来源: `examples/imagepipe/imagepipe.py:243`*

---
<a id="sym-examples_imagepipe_imagepipe.py-255"></a>
### `sharpen_cmd` · func
装饰器: `@cli.command("sharpen")` `@click.option(
    "-f", "--factor", default=2.0, help="Sharpens the image.", show_default=True
)` `@processor`
```python
def sharpen_cmd(images, factor)
```

Sharpens an image by a specified factor.

**Parameters**:
- images — list — A list of images to be sharpened.
- factor — float — The factor by which the image sharpness is increased.

**Returns**:
- generator — A generator that yields the sharpened images.

**Raises**:
- None

**内部调用(库内):**
- [`copy_filename`](examples_imagepipe.md#sym-examples_imagepipe_imagepipe.py-69) — 用途: 将 `old` 对象的 `filename` 属性复制到 `new` 对象中，并返回 `new` 对象。

*来源: `examples/imagepipe/imagepipe.py:255`*

---
<a id="sym-examples_imagepipe_imagepipe.py-267"></a>
### `paste_cmd` · func
装饰器: `@cli.command("paste")` `@click.option("-l", "--left", default=0, help="Offset from left.")` `@click.option("-r", "--right", default=0, help="Offset from right.")` `@processor`
```python
def paste_cmd(images, left, right)
```

Pastes the second image on the first image and leaves the rest unchanged.

**Parameters**:
- images — list — A list of images to process.
- left — int — The x-coordinate where the second image should be pasted.
- right — int — The y-coordinate where the second image should be pasted.

**Returns**:
- generator — Yields the processed images.

**Raises**:
- None

*来源: `examples/imagepipe/imagepipe.py:267`*

---