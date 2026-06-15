# scrapy/pipelines

<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>

---

## 快速概览

<div class="api-table-container api-simple-table" markdown="0">
<table>
<thead>
<tr>
<th>符号</th>
<th>类型</th>
<th>概述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ItemPipelineManager</code></td>
<td>class</td>
<td>管理项目管道组件的中间件管理器</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.pipelines` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/pipelines/__init__.py` (`142` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及文件存储、媒体处理及管道管理等能力，主要围绕文件下载与持久化逻辑展开。它提供了用于管理项目管道的中间件管理器，支持对管道组件的加载、初始化和调用。该模块与 `scrapy.core.downloader` 和 `scrapy.spiders` 等模块协作，负责处理下载后的媒体文件（如图片、文件）并将其持久化到指定存储后端。它通过 `MediaPipeline` 和 `FilesPipeline` 等基类提供通用的媒体处理逻辑，并通过 `FilesStoreProtocol` 定义了文件存储操作接口，支持多种存储后端如本地文件系统、S3、GCS 和 FTP。
本模块涉及文件存储、媒体处理及管道管理等能力，主要围绕文件下载与持久化逻辑展开。它提供了用于管理项目管道的中间件管理器，支持对管道组件的加载、初始化和调用。该模块与 `scrapy.core.downloader` 和 `scrapy.spiders` 等模块协作，负责处理下载后的媒体文件（如图片、文件）并将其持久化到指定存储后端。它通过 `MediaPipeline` 和 `FilesPipeline` 等基类提供通用的媒体处理逻辑，并通过 `FilesStoreProtocol` 定义了文件存储操作接口，支持多种存储后端如本地文件系统、S3、GCS 和 FTP。
</div>


---

## 类参考

### `ItemPipelineManager`
<!-- api: class | visibility: public | source: scrapy/pipelines/__init__.py:31 -->
> **Summary**: 管理项目管道组件的中间件管理器
**Type**: `<class>` | **Module**: `scrapy.pipelines`
**Inheritance**: `ItemPipelineManager` → `MiddlewareManager`
#### 构造方法
```python
ItemPipelineManager()
```
#### 方法
<div class="api-table-container api-methods-table" markdown="0">
<table>
<thead>
<tr>
<th>方法</th>
<th>返回值</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>_get_mwlist_from_settings(settings: Settings)</code></td>
<td><code>list[Any]</code></td>
<td>从设置中获取中间件列表</td>
</tr>
<tr>
<td><code>_add_middleware(mw: Any)</code></td>
<td><code>None</code></td>
<td>添加中间件到管理器</td>
</tr>
</tbody>
</table>
</div>

---
### `FileException`
<!-- api: class | visibility: public | source: scrapy/pipelines/files.py:78 -->
> **Summary**: 通用媒体错误异常类
**Type**: `<class>` | **Module**: `scrapy.pipelines.files`
**Inheritance**: `FileException` → `Exception`

---
### `StatInfo`
<!-- api: class | visibility: public | source: scrapy/pipelines/files.py:82 -->
> **Summary**: 文件状态信息类型定义
**Type**: `<class>` | **Module**: `scrapy.pipelines.files`
#### 字段
<div class="api-table-container api-fields-table" markdown="0">
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>默认值</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>checksum</code></td>
<td><code>str</code></td>
<td><code>None</code></td>
<td>文件校验和</td>
</tr>
<tr>
<td><code>last_modified</code></td>
<td><code>float</code></td>
<td><code>None</code></td>
<td>最后修改时间戳</td>
</tr>
</tbody>
</table>
</div>

---
### `FilesStoreProtocol`
<!-- api: class | visibility: public | source: scrapy/pipelines/files.py:87 -->
> **Summary**: 文件存储操作协议接口
**Type**: `<class>` | **Module**: `scrapy.pipelines.files`
### `FSFilesStore`
<!-- api: class | visibility: public | source: scrapy/pipelines/files.py:104 -->
> **Summary**: 本地文件系统文件存储实现
**Type**: `<class>` | **Module**: `scrapy.pipelines.files`
**Inheritance**: `FSFilesStore` → `FilesStoreProtocol`
### `S3FilesStore`
<!-- api: class | visibility: public | source: scrapy/pipelines/files.py:155 -->
> **Summary**: S3 文件


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>