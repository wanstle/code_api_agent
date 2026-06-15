# Architecture: scrapy

<span class="md-source-file">[:octicons-list-unordered-24: API Quick Ref](api-index.md)</span>

---

## 阅读指南

如果你是初次接触本项目，建议按以下顺序阅读文档：

**1. 先读本页** — 了解项目整体结构、模块职责划分和典型调用链。

**2. 基础设施层** — [scrapy](modules/scrapy.md)、[scrapy/utils](modules/scrapy_utils.md)、[scrapy/downloadermiddlewares](modules/scrapy_downloadermiddlewares.md)、[tests/test_settings](modules/tests_test_settings.md)、[tests/AsyncCrawlerProcess](modules/tests_AsyncCrawlerProcess.md)

这些模块提供项目的基础能力（配置、LLM 推理、仓库解析），被其他模块广泛依赖。先理解它们，后续模块更容易读懂。

**3. 核心业务层** — [scrapy/core](modules/scrapy_core.md)、[scrapy/extensions](modules/scrapy_extensions.md)、[scrapy/http](modules/scrapy_http.md)、[scrapy/pipelines](modules/scrapy_pipelines.md)

这些模块实现项目的核心功能（索引构建、技能系统、问答代理、文档生成），是项目的主体逻辑所在。

**4. 入口层** — [scrapy/commands](modules/scrapy_commands.md)

这些模块是用户交互的入口，它们编排调用核心业务层和基础设施层来完成具体任务。阅读时可以对照调用链理解模块间的协作关系。

**5. 辅助工具** — [tests](modules/tests.md)、[tests/mockserver](modules/tests_mockserver.md)

这些模块提供评估、测试和实用脚本，通常在了解核心功能后按需查阅。

---

## 项目概述

# 项目概述

## 1. 项目概述

Scrapy 是一个用 Python 编写的开源网络爬虫框架，用于高效地抓取网页并提取结构化数据。它具有高度可扩展性、模块化设计和丰富的中间件系统，适用于大规模数据采集任务。项目包含 423 个文件，共计 6520 个符号（函数、类、变量等），主要使用 Python 编写。

项目采用分层架构设计，分为三层：

- **入口/CLI 层**：负责命令行接口、用户交互和配置解析，如 `scrapy.commands`、`scrapy.cmdline`。
- **核心业务逻辑层**：包含爬虫引擎、调度器、下载器、中间件、管道等模块，如
