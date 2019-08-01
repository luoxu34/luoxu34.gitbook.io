# Clone System Using Mondo

## Mondo介绍

[Mondo Rescue](http://www.mondorescue.org/) 主要由 `Mondo` 和 `Mindi` 两部分组成：

* Mondo 是主程序用来备份和还原
* Mindi 则类似一个迷你的Linux，用于引导和启动Mondo恢复程序，它包括核心，模块，函数库及一些做系统维护的重要工具

## 安装

### 下载 repo

文件都叫 `mondorescue.repo`，需要根据系统和发行版本，从 [ftp://ftp.mondorescue.org/ ](ftp://ftp.mondorescue.org/ ) 中找到相应的文件下载下来，例如 centos7：

> wget ftp://ftp.mondorescue.org/rhel/7/x86_64/mondorescue.repo -O /etc/yum.repos.d/mondorescue.repo

### 安装

> yum install mondo

## 备份恢复

参考这篇[文章](https://www.tecmint.com/how-to-clone-linux-systems/)

