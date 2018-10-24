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

| 目的 | 命令 |
| --- | --- |
| 查看pip版本 | pip -V |
| 搜索包 | pip search pip |
| 查看某个已安装包信息 | pip show pip |
| 安装网上包 | pip install fabric |
| 安装本地包 | pip install pip-9.0.0.tar.gz |
| 指定pypi源安装包 | pip install -i https://mirrors.aliyun.com/pypi/simple/ fabric |
| 指定版本安装 | pip install fabric==2.4.0 |
| 列出已安装包 | pip list |
| 检查更新 |  pip list --outdated |
| 更新某个包 | pip install -U pip |
| 卸载某个包 | pip uninstall pip -y |

## 其他技巧

### 安装旧版本包

如果不想安装最新包，但是不知都有哪些版本：

`pip install pylibmc==`

[参考链接在这里](https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available)

### 下载源码包而不安装

下载默认是编译好的二进制包，离线部署时，最好下载源码包：

`pip download --no-binary :all: pip`

### 导出/导入环境

导出requirements.txt

`pip freeze > requirements.txt`

导入环境(网络版)

`pip install -r requirements.txt`

导入环境(本地版)

`pip install -r requirements.txt --no-index -f /path/to/your/packages-dir`

## 显示某包的依赖

请使用 [`pipdeptree`](https://github.com/naiquevin/pipdeptree)

