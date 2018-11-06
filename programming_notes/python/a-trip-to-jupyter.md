# Jupyter之旅

Jupyter发音`/ˈdʒuːpɪtə(r)/`

## The Jupyter Notebook

> The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

## 安装

前提条件是已经存在python2.7或python3.3以上版本的环境，官方**墙裂推荐**通过`Anaconda`安装`Jupyter`。

```bash
# Anaconda方式安装
conda install jupyter

# Pip方式安装
python -m pip install --upgrade pip
python -m pip install jupyter
```

## 运行

```bash

# 默认方式，浏览器访问 http://localhost:8888
jupyter notebook

# 指定某个notebook启动
jupyter notebook notebook.ipynb

# 绑定ip、指定端口启动
jupyter notebook --ip '0.0.0.0' --port 9999

# 不自动打开浏览器启动
jupyter notebook --no-browser

# 集成matplotlib启动(也可启动后执行 %matplotlib 命令)
jupyter notebook --pylab

```

## 配置


## 快捷键

### 首先要知道模式切换

按 `Esc` 键，进入命令模式，cell状态变成deactivate，光标隐藏

按 `Enter` 键，进入编辑模式，cell被激活，光标显示并闪烁

### 最常用快捷键

快捷键 | 作用
---|---
Ctrl-Enter | 运行cell的代码
Shift-Enter | 运行cell的代码，然后跳到下一个cell
Alt-Enter | 运行cell的代码，然后新建cell并跳到该cell

### 命令模式下的快捷键

快捷键 | 作用
---|---
Enter | 切换到编辑模式
a |  上方新建cell
b | 下放新建cell
d,d | 删除选中的单元

### 编模式下的快捷键


快捷键 | 作用
---|---
Esc | 切换到命令模式
Tab | 代码补全或缩进
Shift-Tab | 显示Docstring

