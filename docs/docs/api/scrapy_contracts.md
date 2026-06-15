# API 参考:`scrapy/contracts`

## `scrapy/contracts/__init__.py`

<a id="sym-scrapy_contracts___init__.py-24"></a>

### `Contract` · class
```python
class Contract
```

*来源: `scrapy/contracts/__init__.py:24` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-30"></a>

### `Contract.__init__` · method
```python
def __init__(self, method: Callable[..., Any], *args: Any)
```

**内部调用(库内):**
- [`_create_testcase`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-200)

*来源: `scrapy/contracts/__init__.py:30` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-35"></a>

### `Contract.add_pre_hook` · method
```python
def add_pre_hook(self, request: Request, results: TestResult) -> Request
```

*来源: `scrapy/contracts/__init__.py:35` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-41"></a>

### `Contract.wrapper` · method
装饰器: `@wraps(cb)`
```python
def wrapper(response: Response, **cb_kwargs: Any) -> list[Any]
```

*来源: `scrapy/contracts/__init__.py:41` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-61"></a>

### `Contract.add_post_hook` · method
```python
def add_post_hook(self, request: Request, results: TestResult) -> Request
```

*来源: `scrapy/contracts/__init__.py:61` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-67"></a>

### `Contract.wrapper` · method
装饰器: `@wraps(cb)`
```python
def wrapper(response: Response, **cb_kwargs: Any) -> list[Any]
```

*来源: `scrapy/contracts/__init__.py:67` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-88"></a>

### `Contract.adjust_request_args` · method
```python
def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]
```

*来源: `scrapy/contracts/__init__.py:88` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-92"></a>

### `ContractsManager` · class
```python
class ContractsManager
```

*来源: `scrapy/contracts/__init__.py:92` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-95"></a>

### `ContractsManager.__init__` · method
```python
def __init__(self, contracts: Iterable[type[Contract]])
```

*来源: `scrapy/contracts/__init__.py:95` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-99"></a>

### `ContractsManager.tested_methods_from_spidercls` · method
```python
def tested_methods_from_spidercls(self, spidercls: type[Spider]) -> list[str]
```

*来源: `scrapy/contracts/__init__.py:99` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-108"></a>

### `ContractsManager.extract_contracts` · method
```python
def extract_contracts(self, method: Callable[..., Any]) -> list[Contract]
```

*来源: `scrapy/contracts/__init__.py:108` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-125"></a>

### `ContractsManager.from_spider` · method
```python
def from_spider(self, spider: Spider, results: TestResult) -> list[Request | None]
```

**内部调用(库内):**
- [`ContractsManager.tested_methods_from_spidercls`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-99)
- [`ContractsManager.from_method`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-137)
- [`_create_testcase`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-200)

*来源: `scrapy/contracts/__init__.py:125` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-137"></a>

### `ContractsManager.from_method` · method
```python
def from_method(
        self, method: Callable[..., Any], results: TestResult
    ) -> Request | None
```

**内部调用(库内):**
- [`ContractsManager.extract_contracts`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-108)
- [`get_spec`](scrapy_utils.md#sym-scrapy_utils_python.py-215)
- [`Contract.adjust_request_args`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-88)
- [`Contract.add_pre_hook`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-35)
- [`Contract.add_post_hook`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-61)
- [`ContractsManager._clean_req`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-174)

*来源: `scrapy/contracts/__init__.py:137` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-174"></a>

### `ContractsManager._clean_req` · method
```python
def _clean_req(
        self, request: Request, method: Callable[..., Any], results: TestResult
    ) -> None
```

**内部调用(库内):**
- [`_create_testcase`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-200)

*来源: `scrapy/contracts/__init__.py:174` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-183"></a>

### `ContractsManager.cb_wrapper` · method
装饰器: `@wraps(cb)`
```python
def cb_wrapper(response: Response, **cb_kwargs: Any) -> None
```

**内部调用(库内):**
- [`_create_testcase`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-200)

*来源: `scrapy/contracts/__init__.py:183` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-191"></a>

### `ContractsManager.eb_wrapper` · method
```python
def eb_wrapper(failure: Failure) -> None
```

**内部调用(库内):**
- [`_create_testcase`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-200)

*来源: `scrapy/contracts/__init__.py:191` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-200"></a>

### `_create_testcase` · func
```python
def _create_testcase(method: Callable[..., Any], desc: str) -> TestCase
```

**内部调用(库内):**
- [`ContractTestCase`](scrapy_contracts.md#sym-scrapy_contracts___init__.py-203)

*来源: `scrapy/contracts/__init__.py:200` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-203"></a>

### `ContractTestCase` · class
```python
class ContractTestCase(TestCase)
```

*来源: `scrapy/contracts/__init__.py:203` · 待生成*

---
<a id="sym-scrapy_contracts___init__.py-204"></a>

### `ContractTestCase.__str__` · method
```python
def __str__(_self) -> str
```

*来源: `scrapy/contracts/__init__.py:204` · 待生成*

---

## `scrapy/contracts/default.py`

<a id="sym-scrapy_contracts_default.py-17"></a>

### `UrlContract` · class
```python
class UrlContract(Contract)
```

*来源: `scrapy/contracts/default.py:17` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-24"></a>

### `UrlContract.adjust_request_args` · method
```python
def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]
```

*来源: `scrapy/contracts/default.py:24` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-29"></a>

### `CallbackKeywordArgumentsContract` · class
```python
class CallbackKeywordArgumentsContract(Contract)
```

*来源: `scrapy/contracts/default.py:29` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-38"></a>

### `CallbackKeywordArgumentsContract.adjust_request_args` · method
```python
def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]
```

*来源: `scrapy/contracts/default.py:38` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-43"></a>

### `MetadataContract` · class
```python
class MetadataContract(Contract)
```

*来源: `scrapy/contracts/default.py:43` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-52"></a>

### `MetadataContract.adjust_request_args` · method
```python
def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]
```

*来源: `scrapy/contracts/default.py:52` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-57"></a>

### `ReturnsContract` · class
```python
class ReturnsContract(Contract)
```

*来源: `scrapy/contracts/default.py:57` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-78"></a>

### `ReturnsContract.__init__` · method
```python
def __init__(self, *args: Any, **kwargs: Any)
```

*来源: `scrapy/contracts/default.py:78` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-98"></a>

### `ReturnsContract.post_process` · method
```python
def post_process(self, output: list[Any]) -> None
```

**内部调用(库内):**
- [`ContractFail`](scrapy.md#sym-scrapy_exceptions.py-122) — `ContractFail` 类代表一个契约失败的异常，继承自 `AssertionError`，用于在契约检查失败时抛出。

*来源: `scrapy/contracts/default.py:98` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-117"></a>

### `ScrapesContract` · class
```python
class ScrapesContract(Contract)
```

*来源: `scrapy/contracts/default.py:117` · 待生成*

---
<a id="sym-scrapy_contracts_default.py-124"></a>

### `ScrapesContract.post_process` · method
```python
def post_process(self, output: list[Any]) -> None
```

**内部调用(库内):**
- [`ContractFail`](scrapy.md#sym-scrapy_exceptions.py-122) — `ContractFail` 类代表一个契约失败的异常，继承自 `AssertionError`，用于在契约检查失败时抛出。

*来源: `scrapy/contracts/default.py:124` · 待生成*

---