---
title: How to Deploy a Blog on Vercel
published: 2025-08-27
description: How to Deploy a Blog on Vercel
tags: ['blog', 'vercel']
category: Blog
draft: False
slug: how-to-deploy-a-blog-on-vercel
---

## Find a Blog Template You Like
Vercel supports a wide range of blog templates from various frameworks, such as `nextjs`, `astro`, `express`, `hexo`, and more. You can choose a template you like on platforms like GitHub (99% of them can be directly deployed on Vercel).  
The template I use is as follows, which is a blog template built with the `astro` framework.  
::github{repo="saicaca/fuwari"}  
After selecting a template, remember to fork it to your own repository. This means your GitHub account should have the blog repository (Vercel will import it directly from your GitHub repository later).  

## Deploy the Blog on Vercel
Log in to Vercel. It is recommended to log in directly using your GitHub account.  
![](https://s2.loli.net/2025/08/27/AaPbMDBGLvd4Os9.png)  

After logging in, click `Add New` on the right and select `Project`.  
![](https://s2.loli.net/2025/08/27/z91rI45yXDsCV7n.png)  
Select the template you want to use from your repository and click `Import`.  
![](https://s2.loli.net/2025/08/27/p6rzOQuEmXZkfSP.png)  

Once you enter this interface, normally you only need to modify the `Project Name`. The framework used by the blog will be automatically recognized.  
> Note: If the repository involves some `Environment Variables`, you can configure them in the `Environment Variables` section at the bottom.  

![](https://s2.loli.net/2025/08/27/e1XZqStDKOJwARz.png)  

Wait for 2-3 minutes, and Vercel will successfully deploy your blog.  
![](https://s2.loli.net/2025/08/27/zZJQNO7DgjtW2TG.png)  
At this point, Vercel will provide you with a blog address ending with `vercel.app`, which can be directly accessed on the public network.  

## Add Your Own Domain (Optional)
Of course, we all want our blog to have a unique domain name. The process of purchasing a domain name will not be detailed here. Recommended domain name registrars are: `Vercel` (convenient and reasonably priced) and `Namecheap`.  
It is not recommended to purchase from domestic domain name registrars, as it may involve some filing issues and may not be easily indexed by Google later.  

After you have your own domain name, go to your Vercel project space, click `Domains`, then click `Add Existing`. Select the project to which you want to add the domain name and click `Select`.  
![](https://s2.loli.net/2025/08/27/Q2SyJ3zGlhjO8a9.png)  

Enter the domain name you purchased (without www).  
![](https://s2.loli.net/2025/08/27/g2rBlmN5Vpfs6z8.png)  

After adding the domain name, it cannot be resolved correctly yet because Vercel cannot verify whether you own the domain name.  
![](https://s2.loli.net/2025/08/27/6r9ycjSdCmlOFP7.png)  
The red box in the image shows the `DNS Records` you need to add. You need to go to your domain name provider and add a DNS record. Additionally, Vercel requires you to add two nameservers for proper resolution.  
![](https://s2.loli.net/2025/08/27/XJMySH7CsbZRLfv.png)  

After correctly adding the `DNS Records`, click `Refresh`. Once the domain ownership is verified, you can access your blog directly via the domain name.