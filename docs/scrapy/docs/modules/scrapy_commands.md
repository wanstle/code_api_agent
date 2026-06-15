# scrapy/commands

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
<td><code>ScrapyCommand</code></td>
<td>class</td>
<td>Scrapy 命令基类，定义通用命令属性和方法</td>
</tr>
<tr>
<td><code>BaseRunSpiderCommand</code></td>
<td>class</td>
<td>为 crawl、parse 和 runspider 等命令提供共享功能</td>
</tr>
<tr>
<td><code>ScrapyHelpFormatter</code></td>
<td>class</td>
<td>自定义命令行帮助信息的输出格式</td>
</tr>
<tr>
<td><code>Command</code></td>
<td>class</td>
<td>实现 parse 命令的接口与行为</td>
</tr>
<tr>
<td><code>sanitize_module_name</code></td>
<td>function</td>
<td>清理模块名，替换非法字符</td>
</tr>
<tr>
<td><code>extract_domain</code></td>
<td>function</td>
<td>从 URL 中提取域名</td>
</tr>
<tr>
<td><code>verify_url_scheme</code></td>
<td>function</td>
<td>验证 URL 的协议是否合法</td>
</tr>
<tr>
<td><code>_make_writable</code></td>
<td>function</td>
<td>设置文件权限为可写</td>
</tr>
<tr>
<td><code>TextTestResult</code></td>
<td>class</td>
<td>自定义测试结果输出格式</td>
</tr>
</tbody>
</table>
</div>

---

## 模块概述

<div class="api-module-meta"><strong>Package</strong>: `scrapy.commands` &nbsp;|&nbsp; <strong>Source</strong>: `scrapy/commands/__init__.py` (`237` lines)</div>

<div class="api-module-overview" markdown="1">
本模块涉及 Scrapy 命令行工具的实现机制，包含命令基类、命令行参数解析、帮助信息格式化等功能。它作为 Scrapy CLI 的一部分，负责处理各种命令的执行逻辑和上下文配置。该模块被 `scrapy.cmdline` 模块调用，用于构建命令行接口并执行具体命令。它依赖于 `argparse` 和 `scrapy.settings` 等模块来完成命令参数解析与设置管理。
</div>


---

## 类参考

### `ScrapyCommand`
<!-- api: class | visibility: public | source: scrapy/commands/__init__.py:27 -->
> **Summary**: Scrapy 命令基类，定义通用命令属性和方法
**Type**: `<class>` | **Module**: `scrapy.commands`
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
<td><code>requires_project</code></td>
<td><code>bool</code></td>
<td><code>False</code></td>
<td>是否需要项目配置</td>
</tr>
<tr>
<td><code>requires_crawler_process</code></td>
<td><code>bool</code></td>
<td><code>True</code></td>
<td>是否需要 CrawlerProcess</td>
</tr>
<tr>
<td><code>crawler_process</code></td>
<td>CrawlerProcessBase</td>
<td>None</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>default_settings</code></td>
<td><code>dict[str, Any]</code></td>
<td><code>{}</code></td>
<td>命令默认设置</td>
</tr>
<tr>
<td><code>exitcode</code></td>
<td><code>int</code></td>
<td><code>0</code></td>
<td>命令退出码</td>
</tr>
</tbody>
</table>
</div>
#### 构造方法
```python
ScrapyCommand()
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
<td><code>set_crawler(crawler: Crawler)</code></td>
<td><code>None</code></td>
<td>设置爬虫实例（已弃用）</td>
</tr>
</tbody>
</table>
</div>
##### `set_crawler`
```python
set_crawler(crawler: Crawler) -> None
```
<div class="api-table-container api-fields-table" markdown="0">
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>crawler</code></td>
<td><code>Crawler</code></td>
<td>爬虫实例</td>
</tr><tr class="api-returns-row"><td><strong>Returns</strong></td><td><code>None</code></td><td>设置爬虫实例</td></tr>
</tbody>
</table>
</div>
**Raises**: `RuntimeError` — 当调用此方法时抛出（已弃用警告）
**See Also**: `BaseRunSpiderCommand`, `Command`

---
### `BaseRunSpiderCommand`
<!-- api: class | visibility: public | source: scrapy/commands/__init__.py:149 -->
> **Summary**: 为 crawl、parse 和 runspider 等命令提供共享功能
**Type**: `<class>` | **Module**: `scrapy.commands`  
**Inheritance**: `BaseRunSpiderCommand` → `ScrapyCommand`
### `ScrapyHelpFormatter`
<!-- api: class | visibility: public | source: scrapy/commands/__init__.py:199 -->
> **Summary**: 自定义命令行帮助信息的输出格式
**Type**: `<class>` | **Module**: `scrapy.commands`


---
<span class="md-source-file">[:octicons-git-branch-24: Architecture](../architecture.md) &nbsp;|&nbsp; [:octicons-list-unordered-24: API Quick Ref](../api-index.md)</span>