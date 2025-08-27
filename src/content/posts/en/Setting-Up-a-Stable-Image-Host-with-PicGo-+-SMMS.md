---
title: Setting Up a Stable Image Host with PicGo + SMMS
published: 2025-08-11
description: Setting Up a Stable Image Host with PicGo + SMMS
tags: [PicGo, SMMS, Image Hosting]
category: Tools
draft: false
---

# Preface

I have previously experimented with image hosting solutions like PicGo + GitHub, but setting it up again on a new device was a hassle. Since an image host is a productivity tool, the simpler and faster the configuration, the better.

SMMS is free, hassle-free, and its free tier of 5GB meets the needs of most users, which is why I chose SMMS. Of course, you can upgrade to a paid plan if you have more demands.

# Download and Install PicGo

- Download from GitHub: [PicGo Official GitHub Release](https://github.com/Molunerfinn/PicGo/releases)

Windows users can download and install the software indicated in the red box.

![](https://pic1.zhimg.com/v2-31c01e6b949f331ac8d8dc3d2b4b8bc6_r.jpg)

- Download from Shandong University Mirror Site (if you cannot access GitHub): [PicGo - Shandong University Mirror](https://mirrors.sdu.edu.cn/github-release/1713403144/github-release/Molunerfinn_PicGo/v2.3.1/)

Windows users can download and install the file indicated in the red box.

![](https://pic2.zhimg.com/v2-21372e0552d4089985cbd582ae695f6b_r.jpg)

# Register on SMMS and Obtain Token

## Register on SMMS

Visit [smms.app](http://smms.app), which is SMMS's dedicated domain for Mainland China, ensuring smooth network communication. Register an account on smms.app.

![](https://picx.zhimg.com/v2-8c5cefdf9878fd514385c383f09edd4f_r.jpg)

## Obtain Personal Token

After logging in, go to the top right corner, click on **User**, and enter the **Dashboard**.

![](https://picx.zhimg.com/v2-3c59a4b24bbe88e641a91fa348fcba2f_r.jpg)

In the Dashboard, select **API Token**. Normally, you will need to generate a new token (the author has already generated one). Copy your **Secret Token**.

![](https://pica.zhimg.com/v2-4f01a6322b7043f19420f76a9d2f19f0_r.jpg)

# Configure SMMS in PicGo

Open the installed PicGo, click on **Image Host Settings** on the left, then select **SM.MS**. Click the plus button to add a new configuration.

![](https://pic1.zhimg.com/v2-1815bb6f4b0f7c5d415bf3b8f019d39e_r.jpg)

There are three settings to configure:  
1. **Configuration Name**: Name it as you prefer (the author named it "smms").  
2. **Set Token**: Paste the token you just generated.  
3. **Backup Upload Domain**: Use this domain: **smms.app**.  
Finally, click **Confirm**.

![](https://pica.zhimg.com/v2-de08ba7669f1b1303881d1ec24a174d0_r.jpg)

# Using SMMS Image Host

After correct configuration, you can upload images in PicGo's upload area. It supports drag-and-drop, file selection, and clipboard image upload. Clipboard image upload is likely the most practical.

After a successful upload, the Markdown-formatted image link is automatically copied, which is very convenient. You can also adjust the link format in the bottom left corner if needed.

![](https://pic3.zhimg.com/v2-2c57b4fc7e510fae32e927f38995f2d6_r.jpg)

## Album

In the **Album** section on the left side of PicGo, you can view previously uploaded images. The icon in the bottom left corner allows you to copy the Markdown link again.