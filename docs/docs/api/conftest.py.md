# API 参考:`conftest.py`

## `conftest.py`

<a id="sym-conftest.py-20"></a>

### `_py_files` · func
```python
def _py_files(folder)
```

递归地返回指定文件夹下所有 `.py` 文件的路径。

**Parameters**
- `folder`: 要搜索的文件夹路径。

**Returns**
- 生成器，产生指定文件夹中所有 `.py` 文件的字符串路径。

**Raises**
- (unknown)

*来源: `conftest.py:20`*

---
<a id="sym-conftest.py-59"></a>

### `pytest_addoption` · func
```python
def pytest_addoption(parser, pluginmanager)
```

为 pytest 添加一个 `--reactor` 选项以配置异步反应器。  
**Parameters**  
- `parser` – pytest 的命令行解析器对象  
- `pluginmanager` – pytest 的插件管理器对象  
**Returns**  
(unknown)  
**Raises**  
(unknown)

*来源: `conftest.py:59`*

---
<a id="sym-conftest.py-71"></a>

### `mockserver` · func
装饰器: `@pytest.fixture(scope="session")`
```python
def mockserver() -> Generator[MockServer]
```

创建一个 MockServer 实例并将其作为生成器返回。

**Returns**
  - `Generator[MockServer]`: 一个生成器，用于提供 MockServer 实例。

**Raises**
  - (unknown)

*来源: `conftest.py:71`*

---
<a id="sym-conftest.py-77"></a>

### `mitm_proxy_server` · func
装饰器: `@pytest.fixture  # function scope because it modifies os.environ`
```python
def mitm_proxy_server(monkeypatch: pytest.MonkeyPatch) -> Generator[MitmProxy]
```

启动并返回一个用于测试的 MITM 代理服务器，自动设置 HTTP 和 HTTPS 代理环境变量。

**Parameters**
- `monkeypatch`: pytest 的 monkeypatch 对象，用于临时设置环境变量。

**Returns**
- `Generator[MitmProxy]`: 一个生成器，yield 出一个 MitmProxy 实例。

**Raises**
- (unknown)

*来源: `conftest.py:77`*

---
<a id="sym-conftest.py-90"></a>

### `mitm_proxy_server_https` · func
装饰器: `@pytest.fixture  # function scope because it modifies os.environ`
```python
def mitm_proxy_server_https(monkeypatch: pytest.MonkeyPatch) -> Generator[MitmProxy]
```

启动并返回一个用于 HTTPS 的 MitmProxy 代理服务器生成器。

**Parameters**
- `monkeypatch`: pytest 的 monkeypatch 对象，用于设置环境变量。

**Returns**
- `Generator[MitmProxy]`: 一个生成器，产生 MitmProxy 实例。

**Raises**
- (unknown)

*来源: `conftest.py:90`*

---
<a id="sym-conftest.py-103"></a>

### `socks5_proxy_server` · func
装饰器: `@pytest.fixture  # function scope because it modifies os.environ`
```python
def socks5_proxy_server(monkeypatch: pytest.MonkeyPatch) -> Generator[MitmProxy]
```

启动一个 SOCKS5 代理服务器用于测试。

**Parameters**
- `monkeypatch`: pytest.MonkeyPatch - 用于设置环境变量的补丁对象。

**Returns**
- `Generator[MitmProxy]` - 一个生成器，产生 MitmProxy 实例。

**Raises**
- (unknown)

*来源: `conftest.py:103`*

---
<a id="sym-conftest.py-116"></a>

### `reactor_pytest` · func
装饰器: `@pytest.fixture(scope="session")`
```python
def reactor_pytest(request) -> str
```

从 pytest 配置中获取 reactor 选项的值。

**Parameters**
- `request`: pytest 的 request 对象，用于访问配置选项。

**Returns**
- `str`: 返回 `--reactor` 命令行选项的值。

*来源: `conftest.py:116`*

---
<a id="sym-conftest.py-120"></a>

### `pytest_configure` · func
```python
def pytest_configure(config)
```

配置 pytest 测试环境以选择合适的事件循环和反应器。

**Parameters**
- `config`: pytest 配置对象，用于获取命令行选项。

**Returns**
- (unknown)

**Raises**
- (unknown)

**内部调用(库内):**
- [`set_asyncio_event_loop_policy`](scrapy_utils.md#sym-scrapy_utils_reactor.py-98)
- [`install_reactor_import_hook`](scrapy_utils.md#sym-scrapy_utils_reactorless.py-50)

*来源: `conftest.py:120`*

---
<a id="sym-conftest.py-129"></a>

### `pytest_runtest_setup` · func
```python
def pytest_runtest_setup(item)
```

此函数用于根据测试标记和 Reactor 配置跳过不符合条件的测试。

**Parameters**
- `item`: pytest 测试项对象，用于检查标记和配置。

**Returns**
- (unknown)

**Raises**
- (unknown)

*来源: `conftest.py:129`*

---