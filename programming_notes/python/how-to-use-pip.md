# 优雅使用pip命令

pip命令用于安装各种第三方python库，但是在国内直接使用pip命令，显然下载速度就是一个问题，那如何优雅使用pip命令呢？

注意：下文仅针对 Linux/Uinx 平台。

## 国内 pypi 镜像源

国内主要有清华大学和阿里的 pypi 镜像源，下面是相关链接：

* [清华tuna](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
* [阿里开源镜像站](https://opsx.alibaba.com/mirror)

## 临时指定包的镜像源

不想使用默认的 pypi 源，可以使用 `-i` 选项指定来源，例如：

* pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
* pip install -i https://mirrors.aliyun.com/pypi/simple/ some-package

## 设置默认

pip源配置文件可以放置的位置(针对Linux/Uinx)： 

* /etc/pip.conf
* ~/.pip/pip.conf
* ~/.config/pip/pip.conf

如果 pip 版本 < 10.0.0，这样配置：

```
# vim /etc/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

如果 pip 版本 >= 10.0.0，可以这样配置：

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 显示已经安装的第三方包

命令：`pip list`

10.x 以前
```
# pip list
altgraph (0.15)
ansible (2.4.3.0)
```

10.x 以后
```
# pip list
Package                            Version
---------------------------------- -----------
altgraph                           0.15
ansible                            2.4.3.0
```

## 常用命令

## 其他技巧

