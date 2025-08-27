---
title: Ubuntu常用命令
published: 2022-10-11
description: Ubuntu常用命令
tags: ['Ubuntu', '命令']
category: 学习
draft: False
slug: ubuntu常用命令
---
### 网络训练命令 
``` bash
# 训练
torchrun --nproc_per_node 1 --master_port 12364 train.py --gpus 1 -o ./logs/test-unet/ --conf_path ./conf/conf.yml

# 预测
torchrun --nproc_per_node 1 --master_port 12365 predict.py --gpus 0 -o ./results/unet_still_work/ --conf_path ./conf/unet.yml  -k ./logs/unet_still_work/
tar xvf work.tar # 解压tar文件
tar -cvf FileName.tar DirName # 将DirName和其下所有文件（夹）打包
```
### ubuntu 系统命令

```bash
tar xvf work.tar # 解压tar文件
tar -cvf FileName.tar DirName # 将DirName和其下所有文件（夹）打包


watch -n 2 --color gpustat --c  #监视GPU
sudo chmod 0750 /home/username  #设置其他用户无法访问
ubuntu-drivers devices  查看可用驱动
uname -a  查看系统信息
uncompyle6 -o DataManage.py .\DataManage.pyc #反编译pyc -> py
lspci -vnn | grep VGA 查看系统型号
df -h #查看硬盘容量
chomd -R 700 dir # 使得该路径仅用户自己可访问


curl 'http://202.204.48.66' --data "DDDDD=41824276&upass=08173039&0MKKey="
unset http_proxy
unset https_proxy
x-www-browser http://some-url.org

sudo /usr/local/sunlogin/bin/sunloginclient

#删除一天内的
sudo find /tmp -type f -atime +1 -delete 
# 删除 pip 缓存的包
pip cache purge

#查看硬盘情况
df -h
#查找路径下前50大的文件
sudo du -hd 1 /home/user/ | sort -hr | head -50

#服务器传输指令
sudo scp -r -P 10091 /data/cc/TOF_private/resample/label+/ cyq@frp.visual3d.cn:/external_disk/cc_data/

# 清理 gpu 僵尸进程，该指令会杀死所有进程
fuser -v /dev/nvidia2 | awk '{print $0}' |  xargs kill -9
其中 nvidia2 代表杀死序号 2 的nvidia 卡(一般顺序是 卡 0，卡 1，卡 2....)

# 安装一个程序缺失的包
pip install pipreqs
pipreqs ./ # 会生成一个 requirments txt

# 让一个文件可读可写可执行
chmod 777 xxx.file 
4 （read） 2 （write） 1 (execute)

# 修改文件所有者
chown cc:cc cyq.txt
# 找到frp进程与后台运行frp
ps -aux|grep frp| grep -v grep

# clash for windwos使用
路径 ./config/clash4linux
# 运行
./clash_linux
# 设置终端走代理
export http_proxy="http://127.0.0.1:10809"
export https_proxy="http://127.0.0.1:10808"
# git代理
git config --global http.proxy 'http://127.0.0.1:10809'
git config --global https.proxy 'http://127.0.0.1:10808'

# 取消代理
unset http_proxy
unset https_proxy

# git取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy

删除none的镜像，要先删除镜像中的容器。要删除镜像中的容器，必须先停止容器。
docker images
$ docker stop $(docker ps -a | grep "Exited" | awk '{print $1 }') //停止容器
$ docker rm $(docker ps -a | grep "Exited" | awk '{print $1 }') //删除容器
$ docker rmi $(docker images | grep "none" | awk '{print $3}') //删除镜像

#指定程序可见gpu
CUDA_VISIBLE_DEVICES=0,1,2,3 python xxx.py
```
```



