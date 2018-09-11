# CentOS6.x 安装 Python2.7

## 痛点

* 源码编译python2.7麻烦
* 需要解决py2.6和py2.7共存的问题
* 装了py2.7还要解决pip2.7的安装问题

## 实践的centos版本
```
# cat /etc/centos-release
CentOS release 6.7 (Final)
```

## 安装方式

1. 源码编译安装python2.7和pip
2. 第三方yum源安装python2.7和pip
3. 使用虚拟环境或者conda去安装

下面介绍第二种方法：使用yum源安装python2.7

## 配置yum源
```
# vim /etc/yum.repos.d/sclo6-python27.repo
[sclo6-python27]
name=sclo6-python27
baseurl=https://cbs.centos.org/repos/sclo6-python27-rh-release/x86_64/os
enabled=1
gpgcheck=0
```

## 查看是否包含python2.7的rpm包
```
# yum repolist
# yum info python27
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
Available Packages
Name        : python27
Arch        : x86_64
Version     : 1.1
Release     : 25.el6
Size        : 4.6 k
Repo        : sclo6-python27
Summary     : Package that installs python27
License     : GPLv2+
Description : This is the main package for python27 Software Collection.
```

## 安装python2.7和pip包
```
# yum install python27 python27-python-pip
```

## 设置环境变量

包里的内容默认安装到 `/opt/rh/python27` 下面，该目录下有一个 `enable` 的文件，source一下就可以了：

```
# vim .bashrc
source /opt/rh/python27/enable

# source .bashrc
# python -V
Python 2.7.13
# pip -V
pip 8.1.2 from /opt/rh/python27/root/usr/lib/python2.7/site-packages (python 2.7)
```

> **[success] 恭喜**
> 
> 到这一步你已经成功地在CentOS6.x上安装Python2.7了。

