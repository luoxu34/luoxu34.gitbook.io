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

# 挂后台运行
nohup jupyter notebook > /var/log/jupyter.log 2>&1 &
```

## 配置

### 生成配置文件

```
$ jupyter notebook --generate-config
Writing default config to: /home/duni/.jupyter/jupyter_notebook_config.py
```

### 生成密码

```
$ jupyter notebook password
Enter password:
Verify password:
[NotebookPasswordApp] Wrote hashed password to /home/duni/.jupyter/jupyter_notebook_config.json
```

### 配置jupyter

```
$ vim ~/.jupyter/jupyter_notebook_config.py
```

我的配置如下：

    c.NotebookApp.ip = '0.0.0.0'
    c.NotebookApp.port = 8080
    c.NotebookApp.open_browser = False
    c.NotebookApp.notebook_dir = '/home/luoxu/notebook_dir'

注意点：
1. `c.NotebookApp.ip`以前是可以赋值`*`的，但是对于最新版本会绑定不了ip

### 使用SSL加密(可选)

#### 生成证书

```
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem
```

#### 指定证书

```
# 启动时指定证书
$ jupyter notebook --certfile=mycert.pem --keyfile mykey.key

# 写入配置文件
$ vim ~/.jupyter/jupyter_notebook_config.py

参数如下：
c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'
```

### 浏览器访问

http://127.0.0.1:8888

如果使用SSL加密则将http改成https

## 其他设置

### 定制notebook的url

访问jupyter，默认URL是`http://localhost:8888/`，但是可以定制前缀，例如想设置成`http://localhost:8888/ipython/`，需要这样设置：

`c.NotebookApp.base_url = '/ipython/'`

### 结合web服务使用

`pass`

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

## 魔术命令

`pass`

## 完整的jupyter_notebook_config.py

```python
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8080
c.NotebookApp.password = u'sha1:bcd259ccf...<your hashed password here>'
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/home/luoxu/notebook_dir'
c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'
c.NotebookApp.base_url = '/ipython/'
```

## 参考

1. http://jupyter-notebook.readthedocs.io/en/latest/public_server.html

