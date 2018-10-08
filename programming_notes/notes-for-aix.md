# AIX使用笔记

## SSH服务

* 查看ssh服务状态
```
# lssrc -s sshd
Subsystem   Group       PID         Status 
 sshd       ssh         3866742     active
```

* 停止和启动 ssh 服务
```
# stopsrc -t sshd
# startsrc -t sshd
```

## SFTP服务

* SSH能登录但SFTP连接不上

可能为了安全禁用了sftp，常见手段就是修改`Subsystem`参数

sshd配置文件：`/etc/ssh/sshd_config`

查看sshd_config配置文件，可能影响sftp登录的参数包括：

```
PermitRootLogin
Subsystem       sftp    /usr/sbin/sftp-server
ChrootDirectory
```

1. 如果允许root登录，PermitRootLogin应当为yes
2. Subsystem应当未被注释，或者指定的sftp server存在
3. ChrootDirectory应当为none

## 解压失败

### 现象
```
$ gunzip -c libobk.tar.gz |tar -mxf -
tar: 0511-188 Cannot create libobk.so: Cannot open or remove a file containing a running program.
```

### 解释
解压的时候，提示libobk.so在运行，其实是内核已经加载了该模块，虽然没有进程使用改so文件了，但是并没有被释放


### 解决
`root` 权限下执行 `slibclean` 命令

## 拷贝大文件

### 现象
1. scp超过1g的文件提示 `File too large`
2. `gunzip: 10gr2_aix5l64_database.cpio: File too large`

### 解决办法
修改 `/etc/security/limits` 文件，去掉文件size限制

```
default:
    fsize = -1 
    core = -1 
    cpu = -1
    data = 491519
    rss = -1
    stack = 65536
    nofiles = 2000
```

也有人说执行下面的命令就可以，执行了没用，可能需要重启机器

```
# ulimit -f unlimited
# ulimit -Hf unlimited
```

## nfs mount

### 现象
```
$ sudo mount -o cio,rw,bg,hard,rsize=32768,wsize=32768,vers=3,intr,timeo=600,proto=tcp,nosuid,noacl  192.168.101.23:/dept/output_dir  /tmp/aix5duni_mask

mount: 1831-008 giving up on:
192.168.101.23:/dept/output_dir
vmount: Operation not permitted.
```

### 解决
```
5.2版本下执行：
# nfso -o nfs_use_reserved_ports=1

5.2（含）以上执行：
# nfso -p -o nfs_use_reserved_ports=1
```

### 参考

http://blog.sina.com.cn/s/blog_623630d50101pvto.html

## 查看某个端口被哪个进程占用

1. netstat查看端口信息

```
# netstat -Aan|grep  6666 
f10005000037cbb0 tcp4       0      0  172.17.252.214.501 172.17.252.8.6666  ESTABLISHED
f1000500002bc3b0 tcp4       0      0  172.17.252.214.508 172.17.252.5.6666  ESTABLISHED
f10005000bb70bb0 tcp4       0      0  172.17.252.214.525 172.17.252.8.6666  ESTABLISHED
```

2. 查看pid

如果是TCP连接，则使用 ```rmsock f10005000037cbb0 tcpcb```
 
如果是UDP连接，则使用 ```rmsock f10005000037cbb0 inpcb```
 
输出结果：```The socket 0x37c808 is being held by proccess 11796492 (flow).```
 
3. 根据PID查询详细信息

```# ps -ef|grep 11796492```

