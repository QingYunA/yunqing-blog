---
title: Configuring Ruff Formatter in Nvim (Python)
published: 2024-04-22
description: Configuring Ruff Formatter in Nvim (Python)
tags: [Nvim, Ruff, Formatter, Python]
category: Learning
draft: false
---

# Configuring Ruff Formatter in Nvim (Python)

## Preface

The author uses `Lazyvim`, which utilizes `Mason` to manage formatters. The main issue encountered is that in Python files, the author does not want formatting that breaks lines for code with a width less than 125 (i.e., splitting a single line of code into multiple lines to avoid excessive length).

Creating a `pyproject.toml` in every project seems a bit cumbersome, so the goal is to set up a global configuration.

## Global Configuration for Ruff Formatter

Create a new folder named `ruff` in the `~/.config/` directory. Then, inside the `ruff` folder, create a file named `pyproject.toml` and enter the following content:

```toml
[tool.ruff]
line-length = 125
# Other configurations can also be placed here
```

After saving, your Ruff formatter should work correctly.