---
title: 如何在Vercel上部署博客
published: 2025-08-27
description: 如何在Vercel上部署博客
tags: ['blog', 'vercel']
category: 博客
draft: False
slug: 如何在vercel上部署博客
---

## 找到喜欢的博客
Vercel支持大量框架的博客模板，比如`nextjs`、`astro`、`express`、`hexo`等。在github等方法上挑选喜欢的模板即可(99%可以在vercel上直接部署)
我使用的模板如下，是一个使用`astro`框架的博客模板。
::github{repo="saicaca/fuwari"}
在挑选好模板后，记得fork到自己的仓库下，相当于你自己的github账户下需要有博客仓库(后续vercel是直接从github仓库里进行导入)
## 在vercel上部署博客
登录vercel推荐直接使用github账号登录
![](https://s2.loli.net/2025/08/27/AaPbMDBGLvd4Os9.png)

登录后，点击右边的`Add New`，选择`Project`
![](https://s2.loli.net/2025/08/27/z91rI45yXDsCV7n.png)
选择仓库里准备使用的模板，点击`import`
![](https://s2.loli.net/2025/08/27/p6rzOQuEmXZkfSP.png)
进入该界面后，正常来说只需要修改`Project Name`，博客使用的框架会被直接识别出来。
> 注意：这里如果仓库涉及到一些`环境变量`,可以在底部的`EnvironmentVariables`里配置

![](https://s2.loli.net/2025/08/27/e1XZqStDKOJwARz.png)

等待2-3分钟后vercel就可以部署成功你的博客
![](https://s2.loli.net/2025/08/27/zZJQNO7DgjtW2TG.png)
这时vercel会给你一个以`vercel.app`结尾的博客地址，该地址可以直接在公网进行访问
## 添加自己的域名(可选)
当然，我们都希望自己的博客能有自己独特的域名。域名的购买不在这里赘述，推荐的域名购买商是：`vercel`(胜在方便，价格合理)，`namecheap`。
不推荐在国内域名商购买，会涉及到一些备案问题，后续可能也不方便被`google`搜索到。

在你拥有自己的域名后，进入vercel的project空间，点击`Domains`，点击`Add Existing`，选择你要添加域名的项目，点击`Select`
![](https://s2.loli.net/2025/08/27/Q2SyJ3zGlhjO8a9.png)

输入你所购买的域名，注意不带www
![](https://s2.loli.net/2025/08/27/g2rBlmN5Vpfs6z8.png)

添加好域名后，域名还无法正确解析，因为vercel无法验证域名所有权是否属于你
![](https://s2.loli.net/2025/08/27/6r9ycjSdCmlOFP7.png)
这里红框部分就是你需要添加的`DNS Records`，需要你去域名提供商那里添加一条DNS Records，另外vercel还需要你添加两个nameserver，才能正确解析。
![](https://s2.loli.net/2025/08/27/XJMySH7CsbZRLfv.png)
在正确添加完`DNS Records`后，点击`Refresh`，验证域名所属权后，就可以直接通过域名访问博客～