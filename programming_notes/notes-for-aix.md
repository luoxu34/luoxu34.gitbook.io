# AIX使用笔记

## 重要的网址

* [AIX命令参考大全](http://www.kuqin.com/aixcmds/)
* [AIX Open Source Packages](http://www.perzl.org/aix/index.php)
* [Large Open Source Software Archive for AIX](http://www.bullfreeware.com/toolbox.php)

## 查看内存使用

相当于linux的free命令

```
# svmon -O unit=KB
Unit: KB
-------------------------------------------------------------------------------
               size       inuse        free         pin     virtual  available
memory     16777216    15984372      792844     4020140     7369640    6009568
```

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

#### netstat查看端口信息

```
# netstat -Aan|grep  6666 
f10005000037cbb0 tcp4       0      0  172.17.252.214.501 172.17.252.8.6666  ESTABLISHED
f1000500002bc3b0 tcp4       0      0  172.17.252.214.508 172.17.252.5.6666  ESTABLISHED
f10005000bb70bb0 tcp4       0      0  172.17.252.214.525 172.17.252.8.6666  ESTABLISHED
```

#### 查看pid

如果是TCP连接，则使用 ```rmsock f10005000037cbb0 tcpcb```
 
如果是UDP连接，则使用 ```rmsock f10005000037cbb0 inpcb```
 
输出结果：```The socket 0x37c808 is being held by proccess 11796492 (flow).```
 
#### 根据PID查询进程信息

```# ps -ef|grep 11796492```

## ls时类似Linux的time-style时间格式

https://blog.csdn.net/hbs2011/article/details/17027485

## chfs扩展文件系统

### 查看文件系统使用情况
```
bash-4.2# df
Filesystem    512-blocks      Free %Used    Iused %Iused Mounted on
/dev/hd4        31981568         0  100%    75073    97% /
/dev/hd2         7864320   4356344   45%    41542     8% /usr
/dev/hd9var      7077888   6489648    9%     8710     2% /var
/dev/hd3        12845056   5517688   58%     4498     1% /tmp
/dev/hd1        10747904   7470832   31%     4296     1% /home
/proc                  -         -    -         -     -  /proc
/dev/hd10opt    25952256  25509048    2%     8622     1% /opt
```

根目录已经使用了100%

### 查看物理卷(PV)
```
bash-4.2# lspv
hdisk0          00f90f47264e4f13                    rootvg          active
```

只有一个硬盘 hdisk0， 并且划到了 `rootvg` 的卷组里了。

### 查看卷组(VG)
```
bash-4.2# lsvg
rootvg

bash-4.2# lsvg -l rootvg
rootvg:
LV NAME             TYPE       LPs     PPs     PVs  LV STATE      MOUNT POINT
hd5                 boot       1       1       1    closed/syncd  N/A
hd6                 paging     128     128     1    open/syncd    N/A
hd8                 jfs2log    1       1       1    open/syncd    N/A
hd4                 jfs2       122     122     1    open/syncd    /
hd2                 jfs2       30      30      1    open/syncd    /usr
hd9var              jfs2       27      27      1    open/syncd    /var
hd3                 jfs2       49      49      1    open/syncd    /tmp
hd1                 jfs2       41      41      1    open/syncd    /home
hd10opt             jfs2       99      99      1    open/syncd    /opt
lg_dumplv           sysdump    16      16      1    open/syncd    N/A
lv_ifmduni          raw        10      10      1    closed/syncd  N/A

bash-4.2# lsvg rootvg
VOLUME GROUP:       rootvg            VG IDENTIFIER:  00f90f4700004c000000015b2663a42b
VG STATE:           active            PP SIZE:        128 megabyte(s)
VG PERMISSION:      read/write        TOTAL PPs:      799 (102272 megabytes)
MAX LVs:            256               FREE PPs:       275 (35200 megabytes)
LVs:                11                USED PPs:       524 (67072 megabytes)
OPEN LVs:           9                 QUORUM:         2 (Enabled)
TOTAL PVs:          1                 VG DESCRIPTORS: 2
STALE PVs:          0                 STALE PPs:      0
ACTIVE PVs:         1                 AUTO ON:        no
MAX PPs per VG:     32512
MAX PPs per PV:     1016              MAX PVs:        32
LTG size (Dynamic): 256 kilobyte(s)   AUTO SYNC:      no
HOT SPARE:          no                BB POLICY:      relocatable
```

可以看到文件系统格式是`jfs2`，还剩 35200MB 的空间是可用。

### 给根目录扩展文件系统
```
bash-4.2# chfs -a size=+10G /
Filesystem size changed to 52953088
```

### 确认根目录空间已经增加
```
bash-4.2# df
Filesystem    512-blocks      Free %Used    Iused %Iused Mounted on
/dev/hd4        52953088  20877544   61%    75085     4% /
/dev/hd2         7864320   4356344   45%    41542     8% /usr
/dev/hd9var      7077888   6489648    9%     8710     2% /var
/dev/hd3        12845056   5517688   58%     4498     1% /tmp
/dev/hd1        10747904   7470832   31%     4296     1% /home
/proc                  -         -    -         -     -  /proc
/dev/hd10opt    25952256  25509048    2%     8622     1% /opt
```

