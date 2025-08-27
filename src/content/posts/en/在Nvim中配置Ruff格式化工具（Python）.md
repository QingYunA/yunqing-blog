---
title: 在Nvim中配置Ruff格式化工具（Python）
published: 2024-04-22
description: 在Nvim中配置Ruff格式化工具（Python）
tags: [Nvim, Ruff, 格式化工具, Python]
category: 学习
draft: false
---

# 在Nvim中配置Ruff格式化工具（Python）

## 前言

作者使用 `Lazyvim`，它使用 `Mason` 来管理格式化工具。遇到的主要问题是，在Python文件中，作者不希望格式化宽度小于125的代码行（即，将单行代码分割成多行以避免过长）。

在每个项目中都创建一个 `pyproject.toml` 似乎有点低效，因此目标是设置一个全局配置。

## Ruff格式化工具的全局配置

在 `~/.config/` 目录下创建一个名为 `ruff` 的新文件夹。然后，在 `ruff` 文件夹内创建一个名为 `pyproject.toml` 的文件，并输入以下内容：

```toml
[tool.ruff]
line-length = 125
# 其他配置也可以放在这里
```

保存后，你的Ruff格式化工具应该能正常工作。