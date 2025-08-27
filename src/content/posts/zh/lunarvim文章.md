---
title: LunarVim安装
published: 2024-04-23
description: LunarVim安装
tags: ['LunarVim', '安装']
category: 学习
draft: False
slug: lunarvim安装
---

使用LunarVim已经有一段时间了，在过去的时间我使用了nvim，spacevim等一系列开箱即用的vim软件，综合体验下来，lunarvim使用丝滑，添加插件也极为方便。
但是LunarVim的安装着实有一些麻烦，因此写了本篇文章帮助大家安装。

## LunarVim所需插件

- Nvim v0.9.0+

- git

- make

- pip

- python

- npm,node

- cargo

- nerd font

- 可选 lazygit
  下面一步步进行安装
  
  ## Nvim v0.9.0+
  
  nvim在大多数的ubuntu 系统中，apt-get install 都无法获取到最新的nvim版本。因此这里采用github上官方推荐的方法直接安装。
  下载AppImage
  
  ```bash
  curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
  chmod u+x nvim.appimage
  ./nvim.appimage
  ```
  
  上面的命令大概率会失败，**如果失败，在运行完上面命令的基础上**，在运行下面的命令：
  
  ```bash
  ./nvim.appimage --appimage-extract
  ./squashfs-root/AppRun --version
  ```
  
  软链接nvim,执行完下述代码后，就会出现经典的Nvim界面，此时Nvim已经安装好了。
  
  ```bash
  sudo mv squashfs-root /
  sudo ln -s /squashfs-root/AppRun /usr/bin/nvim
  nvim
  ```
  
  ![](https://s2.loli.net/2023/10/25/1PzAyZLQs8teqrX.png)
  
  ## git
  
  大多数ubuntu安装好后会自带，如果没有安装好用下面的代码安装
  
  ```bash
  sudo apt-get install git
  ```
  
  ## pip + python
  
  pip基本与python 捆绑，因此通过安装anaconda可以同时安装好pip 和 python
  
  ```bash
  cd ~
  wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
  bash Anaconda3-2023.09-0-Linux-x86_64.sh
  ```
  
  ![](https://s2.loli.net/2023/10/25/fy5WD476Uvhkrnz.png)
  敲击回车
  ![](https://s2.loli.net/2023/10/25/KjQqSP5LZnYOrGX.png)
  在该界面按两下 方向键下↓
  询问你是否接受license terms 输入`yes`
  ![](https://s2.loli.net/2023/10/25/mTw2VXSJ9RypKYx.png)
  这里询问你是否更换Anaconda3的安装路径，如果不更改直接回车下一步即可安装完成。
  
  ## npm + node
  
  npm与node也是绑定安装，这里我选择最省事的nvm安装方法
  
  ```bash
  wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
  ```
  
  安装好后，通过`nvm ls-remote`可以安装的版本，选择一个最新的。这里我选的是18.18版本
  
  ```bash
  nvm install v18.18.0
  ```
  
  执行好后npm+node就安装完毕了。
  
  ## cargo
  
  cargo 可以通过该自动化脚本直接安装
  
  ```bash
  curl https://sh.rustup.rs -sSf | sh
  ```

## Nerd font

Nerd Font是lunarvim中各种图标能否正常显示的关键
如果你是Windows用户，可以直接去[Nerd Font](https://www.nerdfonts.com/font-downloads)官网下载需要的Nerd font字体并安装。建议选择`FiraCode`。安装好后通过windows terminal ssh连接服务器，在设置中将字体改为想使用的Nerd Font
![](https://s2.loli.net/2023/10/25/baEMcTGzYk2VyLI.png)
如果你是Ubuntu用户，参考LunarVim给出的[建议安装方法](https://github.com/ronniedroid/getnf)

## lazygit

安装好lazygit后可以在lunarvim终端，通过快捷键<space><g><g>快速打开lazygit。
如果你不知道什么是lazygit，请参考作者的[github链接](https://github.com/jesseduffield/lazygit)

```bash
安装lazygit 注意 只适用于ubuntu系统
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin
```

## 正式安装Lunarvim

直接使用官方提供的安装方法

```bash
LV_BRANCH='release-1.3/neovim-0.9' bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.sh)
```

中途遇到询问，全部输入`yes`即可

好了！到目前为止你已经安装好了lunarvim，可以使用它了。
如果不能直接在bash中通过`lvim`命令启动lunarvim，那么应该是你的没有配置好环境变量，参考以下我的配置(在安装好lvim后会有提示)。
注意将`user`改为你的实际用户名。

```bash
export PATH="/home/user/.local/bin/:$PATH"
```

同时为了避免输入lvim太麻烦，可以在bashrc或者zshrc中加入

```bash
alias vim=lvim
```

将vim映射到lvim。记得`source`更新

## 我的配置文件

由于`Lunarvim`已经将开箱即用做到了极致，因此我的个人配置更改不多，主要是将ESCAPE设置为了`jj`，增加了一些常用的插件。
有兴趣的朋友可以fork尝试~
https://github.com/QingYunA/lvim-conifg
