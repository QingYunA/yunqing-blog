---
title: 基于python vtk的脑血管渲染
published: 2025-08-11
description: 基于python vtk的脑血管渲染
tags: [Python, VTK, 脑血管渲染, 科研绘图]
category: 工具
draft: false
slug: python-vtk-cerebrovascular-rendering
---

## 前言

由于在论文写作过程对血管有渲染需要，在原有C++代码上制作了Python vtk版本的渲染。渲染效果一般，但是用于科研绘图已经足够。源码开源在了Github上，觉得有用的话烦请点个Star 

::github{repo="QingYunA/Cerebrovascular-Segmentation-Rendering-by-Python-VTK"}

## 如何使用

使用说明在Github上有英文版本与中文版本，看着readme大概率都可以直接上手使用。

需要注意的是我只测试了`.mhd`格式的渲染，其他文件可能会出问题，欢迎提issue。

## 渲染效果图

1. 仅渲染prediction


![](https://pic2.zhimg.com/v2-2a8578619c6b2df8288ded4ba5db48c5_r.jpg)

2. prediction与gt（label）计算混淆矩阵后渲染ft,fp,tp等

![](https://pic1.zhimg.com/v2-cfbd0bac52b33f468ecb75de490f56e8_r.jpg)

3. 在渲染基础上添加colorbar（目前做的很丑）

![](https://pic3.zhimg.com/v2-fac9ec2fd7c11e2d8c05801bb04e9756_r.jpg)

