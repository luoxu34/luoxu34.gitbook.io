# CentOS使用笔记

## 修改runlevel

最小化安装centos默认启动是字符界面。

如果已经安装了图形界面的组件，可以通过以下方式修改默认启动方式：

### 适用CentOS 6.x的方法

修改`/etc/inittab`文件，

`id:5:initdefault:` 表示图形界面

`id:3:initdefault:` 表示字符界面

界面切换，可以在终端中执行命令：

```bash
# init 5  进入图形界面
# init 3  进入字符界面
```

### 适用CentOS 7.x的方法

```bash
# systemctl set-default graphical.target   设置成图形界面
# systemctl set-default multi-user.target  设置成字符界面
```

