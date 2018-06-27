# VirtualBox 安装 CentOS7-1611

## 安装CentOS7虚拟机

* 新建虚拟机

![](../images/centos7/image1.png)

* 配置内存

![](../images/centos7/image2.png)

* 配置磁盘1

![](../images/centos7/image3.png)

* 配置磁盘2

![](../images/centos7/image4.png)

* 配置磁盘3

![](../images/centos7/image5.png)

* 配置磁盘4

![](../images/centos7/image6.png)

* 创建完成虚拟机

![](../images/centos7/image7.png)

* ISO引导安装

![](../images/centos7/image8.png)

* 设置语言

![](../images/centos7/image9.png)

* 设置其他

![](../images/centos7/image10.png)

* 完成安装

![](../images/centos7/image11.png)

* 重启进入新系统

![](../images/centos7/image12.png)

> **[success] 温馨提示**
> 
> 创建虚拟机并安装好系统后，可以打一个虚拟机快照(snapshot)，并命名为clean system

----

## 无法创建64位虚拟机问题

只能新建32位的虚拟机系统，很可能是因为主板禁用了虚拟化的功能，开启后即可解决。

- 只能创建32位虚拟机系统

![](../images/centos7/image13.png)

- 重启进入BIOS，找到虚拟化选项

![](../images/centos7/image14.png)

- 修改为enable开启虚拟化功能

![](../images/centos7/image15.png)

- 已经可以创建32/64位虚拟机

![](../images/centos7/image16.png)

