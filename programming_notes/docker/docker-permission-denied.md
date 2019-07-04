# docker 命令执行权限问题

## 错误信息

    Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.39/containers/json: dial unix /var/run/docker.sock: connect: permission denied

## 问题

docker命令默认只能root权限使用，其他用户如果要使用，每次都要在命令前加`sudo`，非常麻烦！

## 解决方法一

执行时每次都加上sudo，例如 `sudo docker ps`，这种方式繁琐！

## 解决方法二

给`docker.sock`文件加上权限：`sudo chmod 777 /var/run/docker.sock`

这样执行docker命令的时候就不需要加sudo，缺点是如果重启服务，就需要重新设置权限！

## 最有效的解决方法

安装docker时默认会创建docker组，只要把用户添加到`docker`组中，之后就可以愉快地使用docker命令了！

## 操作方法(root权限下执行)

```bash
# id luoxu
uid=1000(luoxu) gid=1000(luoxu) groups=1000(luoxu)
# groupmems -g docker -a luoxu
# id luoxu
uid=1000(luoxu) gid=1000(luoxu) groups=1000(luoxu),994(docker)
```

## 组相关命令

```bash
# 查看当前用户所在全部组
groups

# 创建组
groupadd groupname

# 删除组
groupdel groupname

更改查看组成员
groupmems -g groupname [action]
-a,--add username: 指定用户加入组
-d,--delete username: 从组中删除用户
-p,--purge :从组中清除所有成员
-l,--list: 显示组成员列表
```

