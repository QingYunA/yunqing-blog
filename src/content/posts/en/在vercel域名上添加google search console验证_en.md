---
title: How to verify Google Search Console for a domain purchased on Vercel
published: 2025-08-25
description: How to verify Google Search Console for a domain purchased on Vercel
tags: [vercel, google search console, domain]
category: Learning
draft: false
---

# How to verify Google Search Console for a domain purchased on Vercel

## Background
Recently, I purchased a domain on Vercel to use for my personal blog. To make it searchable on Google, I wanted to verify it on Google Search Console. However, Vercel might be a relatively niche domain provider, as I couldn't find the corresponding verification method for Vercel in Google Search Console's official documentation.

Vercel itself doesn't provide a quick way to import TXT DNS records, which made me spend quite some time figuring it out on my own.

## Verification Steps
1. Enter your domain in Google Search Console and start the verification process. Copy the TXT record value as shown in the image below.
![](https://s2.loli.net/2025/08/25/7RzoQ2trAkgcBwe.png)
2. Go to the `domain` section in `Vercel`. In the `name` field, enter your domain (for example, mine is `yunqing.org`). Then, paste the TXT record value obtained in step 1 into the `value` field and click the black ADD button.
![](https://s2.loli.net/2025/08/25/XG4PImKDBYwQ3EV.png)
3. Wait a few minutes, then return to Google Search Console and click verify to complete the verification. (In fact, I didn't even have to wait XD)