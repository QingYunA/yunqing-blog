---
title: PicGo+SMMS搭建稳定图床
published: 2025-08-11
description: PicGo+SMMS搭建稳定图床
tags: ['PicGo', 'SMMS', '图床']
category: 工具
draft: False
slug: picgosmms搭建稳定图床
---

# 前言

本人之前也折腾过Picgo+Github等图床，但是换了新设备又要重来一遍。本身图床就是生产力工具，所以越简单越快速的配置越好~

smms本身免费，而且不折腾，免费版本的5GB也能满足大多数人的需要，因此选择smms。当然有更多需求可以付费升级。

# 下载安装PicGo

- Github上下载[PicGo Github官方下载](https://github.com/Molunerfinn/PicGo/releases)

Windows用户选择红框软件下载并安装即可。

![](https://pic1.zhimg.com/v2-31c01e6b949f331ac8d8dc3d2b4b8bc6_r.jpg)

- 山东大学镜像站下载（如果你上不了Github）[PicGo-山东大学镜像站](https://mirrors.sdu.edu.cn/github-release/1713403144/github-release/Molunerfinn_PicGo/v2.3.1/)

Windows用户选择红框的下载安装即可。

![](https://pic2.zhimg.com/v2-21372e0552d4089985cbd582ae695f6b_r.jpg)

# smms注册并获取Token

## smms注册

访问[smms.app](http://smms.app)，这是sm.ms在中国大陆的专用域名，保证了网络通信顺畅。在smms.app上注册账号。

![](https://picx.zhimg.com/v2-8c5cefdf9878fd514385c383f09edd4f_r.jpg)

## 获取个人Token

登录后，在页面右上角User中进入Dashboard。

![](https://picx.zhimg.com/v2-3c59a4b24bbe88e641a91fa348fcba2f_r.jpg)

进入Dashboard后选择ApI Token。正常来说你需要再Generate 一个Token（笔者已经生成过了），复制你的Secret Token。

![](https://pica.zhimg.com/v2-4f01a6322b7043f19420f76a9d2f19f0_r.jpg)

# 在PicGo中使用SMMS

进入安装好的PicGo，点击左侧**图床设置**的**SM.MS**，点击加号按钮，新增配置。

![](https://pic1.zhimg.com/v2-1815bb6f4b0f7c5d415bf3b8f019d39e_r.jpg)

需要设置的配置有三个，第一个是配置名称，根据你的喜好命名，笔者命名为smms。第二个是 **设定Token，**将刚才生成的Token复制进来。第三个是**备用上传域名**，使用这个域名 **smms.app**。最后确定即可。

![](https://pica.zhimg.com/v2-de08ba7669f1b1303881d1ec24a174d0_r.jpg)

# 使用smms图床

在正确配置后，我们就可以在PicGo的上传区上传图片了，支持拖拽文件，选择文件，剪切板图片上传。剪切板图片上传应该是最实用的。

上传成功后，会自动复制Marddown语法的图片链接格式，非常方便~。当然也可以在左下角调整你需要的链接格式。

![](https://pic3.zhimg.com/v2-2c57b4fc7e510fae32e927f38995f2d6_r.jpg)

## 相册

在PicGo左侧的相册可以查看曾经上传过的图片，左下角的标识可以重新复制Markdown链接~

