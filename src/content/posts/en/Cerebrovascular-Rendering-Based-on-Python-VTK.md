---
title: Cerebrovascular Rendering Based on Python VTK
published: 2025-08-11
description: Cerebrovascular Rendering Based on Python VTK
tags: [Python, VTK, Cerebrovascular Rendering, Scientific Visualization]
category: Tools
draft: false
---

## Preface

During the process of writing a paper, there was a need for vascular rendering. Based on existing C++ code, a Python VTK version of the rendering was developed. The rendering effect is decent and sufficient for scientific visualization purposes. The source code is open-sourced on GitHub. If you find it useful, please consider giving it a Star.

::github{repo="QingYunA/Cerebrovascular-Segmentation-Rendering-by-Python-VTK"}

## How to Use

Usage instructions are available on GitHub in both English and Chinese versions. Following the README should allow most users to get started directly.

Please note that only `.mhd` format rendering has been tested. Other file formats may encounter issues. Feel free to submit an issue if you encounter any problems.

## Rendering Results

1. Rendering prediction only

![](https://pic2.zhimg.com/v2-2a8578619c6b2df8288ded4ba5db48c5_r.jpg)

2. Rendering ft, fp, tp, etc. after calculating the confusion matrix between prediction and gt (label)

![](https://pic1.zhimg.com/v2-cfbd0bac52b33f468ecb75de490f56e8_r.jpg)

3. Adding colorbar on top of the rendering (currently not very aesthetically pleasing)

![](https://pic3.zhimg.com/v2-fac9ec2fd7c11e2d8c05801bb04e9756_r.jpg)