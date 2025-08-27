---
title: 在vercel上购买的域名如何验证google search console
published: 2025-08-25
description: 在vercel上购买的域名如何验证google search console
tags: ['vercel', 'google search console', '域名']
category: 学习
draft: False
slug: 在vercel上购买的域名如何验证google-search-console
---

# 在vercel上购买的域名如何验证google search console

## 背景
最近在vercel上购买了域名用来做自己博客，为了能被google搜索到，想着在google search console上进行验证。没想到vercel可能是比较小众的域名提供商，在google search console的官方文档里没有找到vercel对应的验证方法。

vercel自己也不提供快捷的TXT导入dns 记录方法，害得我自己摸索了半天

## 验证步骤
1. 在google search console上输入自己域名开始验证，复制下图的TXT记录值
![](https://s2.loli.net/2025/08/25/7RzoQ2trAkgcBwe.png)
2. 进入`vercel`的`domain`界面，在`name`栏输入自己的域名，比如我的就是`yunqing.org`,然后在`value`复制步骤1得到的TXT记录值，随后点击黑色按钮ADD即可
![](https://s2.loli.net/2025/08/25/XG4PImKDBYwQ3EV.png)
3. 等待几分钟，回到google search console点击验证即可验证成功 (事实上我根本没有等待XD)