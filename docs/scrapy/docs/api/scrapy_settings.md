# API 参考:`scrapy/settings`

## `scrapy/settings/__init__.py`

<a id="sym-scrapy_settings___init__.py-41"></a>

### `get_settings_priority` · func
```python
def get_settings_priority(priority: int | str) -> int
```

*来源: `scrapy/settings/__init__.py:41` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-52"></a>

### `SettingsAttribute` · class
```python
class SettingsAttribute
```

*来源: `scrapy/settings/__init__.py:52` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-59"></a>

### `SettingsAttribute.__init__` · method
```python
def __init__(self, value: Any, priority: int)
```

**内部调用(库内):**
- [`BaseSettings.maxpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-398)

*来源: `scrapy/settings/__init__.py:59` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-67"></a>

### `SettingsAttribute.set` · method
```python
def set(self, value: Any, priority: int) -> None
```

**内部调用(库内):**
- [`BaseSettings`](scrapy_settings.md#sym-scrapy_settings___init__.py-79)

*来源: `scrapy/settings/__init__.py:67` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-75"></a>

### `SettingsAttribute.__repr__` · method
```python
def __repr__(self) -> str
```

*来源: `scrapy/settings/__init__.py:75` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-79"></a>

### `BaseSettings` · class
```python
class BaseSettings(MutableMapping[str, Any])
```

*来源: `scrapy/settings/__init__.py:79` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-103"></a>

### `BaseSettings.__init__` · method
```python
def __init__(self, values: _SettingsInput = None, priority: int | str = "project")
```

*来源: `scrapy/settings/__init__.py:103` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-109"></a>

### `BaseSettings.__getitem__` · method
```python
def __getitem__(self, opt_name: str) -> Any
```

*来源: `scrapy/settings/__init__.py:109` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-114"></a>

### `BaseSettings.__contains__` · method
```python
def __contains__(self, name: Any) -> bool
```

*来源: `scrapy/settings/__init__.py:114` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-117"></a>

### `BaseSettings.add_to_list` · method
```python
def add_to_list(self, name: str, item: Any) -> None
```

**内部调用(库内):**
- [`BaseSettings.getlist`](scrapy_settings.md#sym-scrapy_settings___init__.py-225)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:117` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-128"></a>

### `BaseSettings.remove_from_list` · method
```python
def remove_from_list(self, name: str, item: Any) -> None
```

**内部调用(库内):**
- [`BaseSettings.getlist`](scrapy_settings.md#sym-scrapy_settings___init__.py-225)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:128` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-142"></a>

### `BaseSettings.get` · method
```python
def get(self, name: str, default: Any = None) -> Any
```

*来源: `scrapy/settings/__init__.py:142` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-171"></a>

### `BaseSettings.getbool` · method
```python
def getbool(self, name: str, default: bool = False) -> bool
```

*来源: `scrapy/settings/__init__.py:171` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-201"></a>

### `BaseSettings.getint` · method
```python
def getint(self, name: str, default: int = 0) -> int
```

*来源: `scrapy/settings/__init__.py:201` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-213"></a>

### `BaseSettings.getfloat` · method
```python
def getfloat(self, name: str, default: float = 0.0) -> float
```

*来源: `scrapy/settings/__init__.py:213` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-225"></a>

### `BaseSettings.getlist` · method
```python
def getlist(self, name: str, default: list[Any] | None = None) -> list[Any]
```

*来源: `scrapy/settings/__init__.py:225` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-247"></a>

### `BaseSettings.getdict` · method
```python
def getdict(
        self, name: str, default: dict[Any, Any] | None = None
    ) -> dict[Any, Any]
```

*来源: `scrapy/settings/__init__.py:247` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-270"></a>

### `BaseSettings.getdictorlist` · method
```python
def getdictorlist(
        self,
        name: str,
        default: dict[Any, Any] | list[Any] | tuple[Any] | None = None,
    ) -> dict[Any, Any] | list[Any]
```

**内部调用(库内):**
- [`Item.deepcopy`](scrapy.md#sym-scrapy_item.py-130) — 返回此 item 的深拷贝。

*来源: `scrapy/settings/__init__.py:270` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-319"></a>

### `BaseSettings.getwithbase` · method
```python
def getwithbase(self, name: str) -> BaseSettings
```

**内部调用(库内):**
- [`BaseSettings`](scrapy_settings.md#sym-scrapy_settings___init__.py-79)

*来源: `scrapy/settings/__init__.py:319` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-338"></a>

### `BaseSettings.get_component_priority_dict_with_base` · method
```python
def get_component_priority_dict_with_base(self, name: str) -> BaseSettings
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`BaseSettings.track_loaded_key`](scrapy_settings.md#sym-scrapy_settings___init__.py-354)
- [`BaseSettings.normalize_key`](scrapy_settings.md#sym-scrapy_settings___init__.py-364)
- [`BaseSettings`](scrapy_settings.md#sym-scrapy_settings___init__.py-79)
- [`BaseSettings.restore_key`](scrapy_settings.md#sym-scrapy_settings___init__.py-376)

*来源: `scrapy/settings/__init__.py:338` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-354"></a>

### `BaseSettings.track_loaded_key` · method
```python
def track_loaded_key(k: Any) -> None
```

**内部调用(库内):**
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)

*来源: `scrapy/settings/__init__.py:354` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-364"></a>

### `BaseSettings.normalize_key` · method
```python
def normalize_key(key: Any) -> Any
```

**内部调用(库内):**
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`global_object_name`](scrapy_utils.md#sym-scrapy_utils_python.py-274)
- [`BaseSettings.track_loaded_key`](scrapy_settings.md#sym-scrapy_settings___init__.py-354)

*来源: `scrapy/settings/__init__.py:364` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-376"></a>

### `BaseSettings.restore_key` · method
```python
def restore_key(k: str) -> Any
```

*来源: `scrapy/settings/__init__.py:376` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-386"></a>

### `BaseSettings.getpriority` · method
```python
def getpriority(self, name: str) -> int | None
```

*来源: `scrapy/settings/__init__.py:386` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-398"></a>

### `BaseSettings.maxpriority` · method
```python
def maxpriority(self) -> int
```

**内部调用(库内):**
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)
- [`get_settings_priority`](scrapy_settings.md#sym-scrapy_settings___init__.py-41)

*来源: `scrapy/settings/__init__.py:398` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-409"></a>

### `BaseSettings.replace_in_component_priority_dict` · method
```python
def replace_in_component_priority_dict(
        self,
        name: str,
        old_cls: type,
        new_cls: type,
        priority: int | None = None,
    ) -> None
```

**内部调用(库内):**
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:409` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-450"></a>

### `BaseSettings.__setitem__` · method
```python
def __setitem__(self, name: str, value: Any) -> None
```

*来源: `scrapy/settings/__init__.py:450` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-453"></a>

### `BaseSettings.set` · method
```python
def set(self, name: str, value: Any, priority: int | str = "project") -> None
```

**内部调用(库内):**
- [`BaseSettings._assert_mutability`](scrapy_settings.md#sym-scrapy_settings___init__.py-608)
- [`get_settings_priority`](scrapy_settings.md#sym-scrapy_settings___init__.py-41)
- [`SettingsAttribute`](scrapy_settings.md#sym-scrapy_settings___init__.py-52)

*来源: `scrapy/settings/__init__.py:453` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-481"></a>

### `BaseSettings.set_in_component_priority_dict` · method
```python
def set_in_component_priority_dict(
        self, name: str, cls: type, priority: int | None
    ) -> None
```

**内部调用(库内):**
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:481` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-505"></a>

### `BaseSettings.setdefault` · method
```python
def setdefault(  # pylint: disable=arguments-renamed
        self,
        name: str,
        default: Any = None,
        priority: int | str = "project",
    ) -> Any
```

*来源: `scrapy/settings/__init__.py:505` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-517"></a>

### `BaseSettings.setdefault_in_component_priority_dict` · method
```python
def setdefault_in_component_priority_dict(
        self, name: str, cls: type, priority: int | None
    ) -> None
```

**内部调用(库内):**
- [`BaseSettings.getdict`](scrapy_settings.md#sym-scrapy_settings___init__.py-247)
- [`load_object`](scrapy_utils.md#sym-scrapy_utils_misc.py-58)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:517` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-535"></a>

### `BaseSettings.setdict` · method
```python
def setdict(self, values: _SettingsInput, priority: int | str = "project") -> None
```

*来源: `scrapy/settings/__init__.py:535` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-538"></a>

### `BaseSettings.setmodule` · method
```python
def setmodule(
        self, module: ModuleType | str, priority: int | str = "project"
    ) -> None
```

**内部调用(库内):**
- [`BaseSettings._assert_mutability`](scrapy_settings.md#sym-scrapy_settings___init__.py-608)

*来源: `scrapy/settings/__init__.py:538` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-563"></a>

### `BaseSettings.update` · method
```python
def update(self, values: _SettingsInput, priority: int | str = "project") -> None
```

**内部调用(库内):**
- [`BaseSettings._assert_mutability`](scrapy_settings.md#sym-scrapy_settings___init__.py-608)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:563` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-596"></a>

### `BaseSettings.delete` · method
```python
def delete(self, name: str, priority: int | str = "project") -> None
```

**内部调用(库内):**
- [`BaseSettings._assert_mutability`](scrapy_settings.md#sym-scrapy_settings___init__.py-608)
- [`get_settings_priority`](scrapy_settings.md#sym-scrapy_settings___init__.py-41)
- [`BaseSettings.getpriority`](scrapy_settings.md#sym-scrapy_settings___init__.py-386)

*来源: `scrapy/settings/__init__.py:596` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-604"></a>

### `BaseSettings.__delitem__` · method
```python
def __delitem__(self, name: str) -> None
```

**内部调用(库内):**
- [`BaseSettings._assert_mutability`](scrapy_settings.md#sym-scrapy_settings___init__.py-608)

*来源: `scrapy/settings/__init__.py:604` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-608"></a>

### `BaseSettings._assert_mutability` · method
```python
def _assert_mutability(self) -> None
```

*来源: `scrapy/settings/__init__.py:608` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-612"></a>

### `BaseSettings.copy` · method
```python
def copy(self) -> Self
```

**内部调用(库内):**
- [`Item.deepcopy`](scrapy.md#sym-scrapy_item.py-130) — 返回此 item 的深拷贝。

*来源: `scrapy/settings/__init__.py:612` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-624"></a>

### `BaseSettings.freeze` · method
```python
def freeze(self) -> None
```

*来源: `scrapy/settings/__init__.py:624` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-634"></a>

### `BaseSettings.frozencopy` · method
```python
def frozencopy(self) -> Self
```

**内部调用(库内):**
- [`BaseSettings.freeze`](scrapy_settings.md#sym-scrapy_settings___init__.py-624)

*来源: `scrapy/settings/__init__.py:634` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-644"></a>

### `BaseSettings.__iter__` · method
```python
def __iter__(self) -> Iterator[str]
```

*来源: `scrapy/settings/__init__.py:644` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-647"></a>

### `BaseSettings.__len__` · method
```python
def __len__(self) -> int
```

*来源: `scrapy/settings/__init__.py:647` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-650"></a>

### `BaseSettings._to_dict` · method
```python
def _to_dict(self) -> dict[str, Any]
```

*来源: `scrapy/settings/__init__.py:650` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-656"></a>

### `BaseSettings.copy_to_dict` · method
```python
def copy_to_dict(self) -> dict[str, Any]
```

**内部调用(库内):**
- [`BaseSettings._to_dict`](scrapy_settings.md#sym-scrapy_settings___init__.py-650)

*来源: `scrapy/settings/__init__.py:656` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-673"></a>

### `BaseSettings._repr_pretty_` · method
```python
def _repr_pretty_(self, p: Any, cycle: bool) -> None
```

**内部调用(库内):**
- [`pformat`](scrapy_utils.md#sym-scrapy_utils_display.py-46)
- [`BaseSettings.copy_to_dict`](scrapy_settings.md#sym-scrapy_settings___init__.py-656)

*来源: `scrapy/settings/__init__.py:673` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-679"></a>

### `BaseSettings.pop` · method
```python
def pop(self, name: str, default: Any = __default) -> Any
```

*来源: `scrapy/settings/__init__.py:679` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-690"></a>

### `Settings` · class
```python
class Settings(BaseSettings)
```

*来源: `scrapy/settings/__init__.py:690` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-701"></a>

### `Settings.__init__` · method
```python
def __init__(self, values: _SettingsInput = None, priority: int | str = "project")
```

**内部调用(库内):**
- [`BaseSettings.setmodule`](scrapy_settings.md#sym-scrapy_settings___init__.py-538)
- [`BaseSettings`](scrapy_settings.md#sym-scrapy_settings___init__.py-79)

*来源: `scrapy/settings/__init__.py:701` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-715"></a>

### `iter_default_settings` · func
```python
def iter_default_settings() -> Iterable[tuple[str, Any]]
```

*来源: `scrapy/settings/__init__.py:715` · 待生成*

---
<a id="sym-scrapy_settings___init__.py-722"></a>

### `overridden_settings` · func
```python
def overridden_settings(
    settings: Mapping[str, Any],
) -> Iterable[tuple[str, Any]]
```

**内部调用(库内):**
- [`iter_default_settings`](scrapy_settings.md#sym-scrapy_settings___init__.py-715)

*来源: `scrapy/settings/__init__.py:722` · 待生成*

---

## `scrapy/settings/default_settings.py`

<a id="sym-scrapy_settings_default_settings.py-589"></a>

### `__getattr__` · func
```python
def __getattr__(name: str) -> Any
```

*来源: `scrapy/settings/default_settings.py:589` · 待生成*

---