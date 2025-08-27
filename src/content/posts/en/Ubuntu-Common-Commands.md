---
title: Ubuntu Common Commands
published: 2022-10-11
description: Ubuntu Common Commands
tags: [Ubuntu, Commands]
category: Learning
draft: false
---
### Network Training Commands 
``` bash
# Training
torchrun --nproc_per_node 1 --master_port 12364 train.py --gpus 1 -o ./logs/test-unet/ --conf_path ./conf/conf.yml

# Prediction
torchrun --nproc_per_node 1 --master_port 12365 predict.py --gpus 0 -o ./results/unet_still_work/ --conf_path ./conf/unet.yml  -k ./logs/unet_still_work/
tar xvf work.tar # Extract tar file
tar -cvf FileName.tar DirName # Package DirName and all its files (folders)
```
### Ubuntu System Commands

```bash
tar xvf work.tar # Extract tar file
tar -cvf FileName.tar DirName # Package DirName and all its files (folders)


watch -n 2 --color gpustat --c  #Monitor GPU
sudo chmod 0750 /home/username  #Set other users unable to access
ubuntu-drivers devices  #View available drivers
uname -a  #View system information
uncompyle6 -o DataManage.py .\DataManage.pyc #Decompile pyc -> py
lspci -vnn | grep VGA #Check system model
df -h #Check hard drive capacity
chomd -R 700 dir # Make the path accessible only to the user themselves


curl 'http://202.204.48.66' --data "DDDDD=41824276&upass=08173039&0MKKey="
unset http_proxy
unset https_proxy
x-www-browser http://some-url.org

sudo /usr/local/sunlogin/bin/sunloginclient

#Delete within one day
sudo find /tmp -type f -atime +1 -delete 
# Delete pip cached packages
pip cache purge

#Check hard drive status
df -h
#Find top 50 largest files under a path
sudo du -hd 1 /home/user/ | sort -hr | head -50

#Server transfer command
sudo scp -r -P 10091 /data/cc/TOF_private/resample/label+/ cyq@frp.visual3d.cn:/external_disk/cc_data/

# Clean up GPU zombie processes, this command will kill all processes
fuser -v /dev/nvidia2 | awk '{print $0}' |  xargs kill -9
Where nvidia2 represents killing the nvidia card with index 2 (generally the order is card 0, card 1, card 2....)

# Install missing packages for a program
pip install pipreqs
pipreqs ./ # Will generate a requirements txt

# Make a file readable, writable, and executable
chmod 777 xxx.file 
4 (read) 2 (write) 1 (execute)

# Change file owner
chown cc:cc cyq.txt
# Find frp process and run frp in background
ps -aux|grep frp| grep -v grep

# Clash for Windows usage
Path ./config/clash4linux
# Run
./clash_linux
# Set terminal to use proxy
export http_proxy="http://127.0.0.1:10809"
export https_proxy="http://127.0.0.1:10808"
# Git proxy
git config --global http.proxy 'http://127.0.0.1:10809'
git config --global https.proxy 'http://127.0.0.1:10808'

# Cancel proxy
unset http_proxy
unset https_proxy

# Git cancel proxy
git config --global --unset http.proxy
git config --global --unset https.proxy

To delete none images, you must first delete the containers in the images. To delete containers in images, you must stop the containers first.
docker images
$ docker stop $(docker ps -a | grep "Exited" | awk '{print $1 }') //Stop containers
$ docker rm $(docker ps -a | grep "Exited" | awk '{print $1 }') //Delete containers
$ docker rmi $(docker images | grep "none" | awk '{print $3}') //Delete images

#Specify visible GPUs for program
CUDA_VISIBLE_DEVICES=0,1,2,3 python xxx.py
```
