# Miniconda 介绍

Anaconda 是一个用于科学计算的 Python 发行版，支持 Linux, Mac, Windows, 包含了众多流行的科学计算、数据分析的 Python 包。

Miniconda 是一个 Anaconda 的轻量级替代，默认只包含了 python 和 conda，但是可以通过 pip 和 conda 来安装所需要的包。

可以借助 Miniconda 解决 python 发开中的包管理问题和环境管理问题（尤其是多版本Python并存问题），其他的方案有：

* virtualenv/venv
* vagrant
* docker

# 下载

Anaconda 下载 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

Miniconda 下载 https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/

# 安装

```
$ bash Miniconda3-latest-Linux-x86_64.sh

[/home/luoxu/miniconda3] >>>
PREFIX=/home/luoxu/miniconda3
installing: python-3.6.5-hc3d631a_2 ...
Python 3.6.5 :: Anaconda, Inc.
installing: ca-certificates-2018.03.07-0 ...
installing: conda-env-2.6.0-h36134e3_1 ...

......

installing: conda-4.5.4-py36_0 ...
installation finished.
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/luoxu/.bashrc ? [yes|no]
[no] >>> yes

Appending source /home/luoxu/miniconda3/bin/activate to /home/luoxu/.bashrc
A backup will be made to: /home/luoxu/.bashrc-miniconda3.bak


For this change to become active, you have to open a new terminal.

Thank you for installing Miniconda3!
```

如果安装时出错并提示 bunzip2: command not found

解决办法： `yum install bzip2`

source环境配置文件后，执行 `conda -V` 看到版本信息说明安装完成。

# 配置

## 配置 Anaconda 仓库的镜像

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

第一次运行 `conda config` 命令时，会在 `home` 目录自动创建 `.condarc` 配置文件。

## Conda 三方源

### Conda Forge

```
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```

当然，也可以临时指定安装源而不配置，如下：

```
$ conda install -c conda-forge wordcloud
```

# 使用

查看配置：conda config --show

查看环境：conda env list

创建环境：conda create --name=jupyter -y

删除环境：conda remove --name=jupyter --all -y

进入环境：source activate jupyter

退出环境：source deactivate

安装某个包：conda install *package_name*

指定channel安装某个包：conda install -c *channel_name* *pachage_name*

更新所有包：conda update --all

手册下载：[conda-cheatsheet.pdf](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)

# 参考

* [清华大学开源软件镜像站 - Anaconda 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
* [Anaconda使用总结](http://python.jobbole.com/86236/)

