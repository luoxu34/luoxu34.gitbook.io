# ZFS on Linux Installation

## Mode

zfs的软件包有两种类型： `kABI-tracking kmod` 和 `DKMS`

选择哪一种的依据就是系统的内核：

1. 如果是系统自带的内核版本，使用 `kABI-tracking kmod`

2. 如果是自己构建的内核，需要使用 `DKMS`，并且一旦重新编译内核，就需要重建zfs

> **[info] Notices**
> 
> zfs软件源默认是 DKMS 类型的zfs包

## Installation

* 方法一： 从[ZFS on Linux官网](http://zfsonlinux.org/)下载spl和zfs源码包编译安装

* 方法二： 通过官方仓库安装

下面介绍的是在 `CentOS 7.5` 下通过 yum 源方式安装 `kABI-tracking kmod` 模式的 `zfs`

## Step

### 配置zfs源和公钥签名文件

```bash
$ sudo yum install http://download.zfsonlinux.org/epel/zfs-release.<dist>.noarch.rpm
$ gpg --quiet --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-zfsonlinux
pub  2048R/F14AB620 2013-03-21 ZFS on Linux <zfs@zfsonlinux.org>
    Key fingerprint = C93A FFFD 9F3F 7B03 C310  CEB6 A9D5 A1C0 F14A B620
    sub  2048R/99685629 2013-03-21
```

`<dist>` 替换成自己的版本，例如centos7.5对应是 `el7_5`

### 修改zfs.repo换成kmod模式

```
$ sudo vim /etc/yum.repos.d/zfs.repo
 [zfs]
 name=ZFS on Linux for EL 7 - dkms
 baseurl=http://download.zfsonlinux.org/epel/7/$basearch/
-enabled=1
+enabled=0
 metadata_expire=7d
 gpgcheck=1
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-zfsonlinux
@@ -9,7 +9,7 @@
 [zfs-kmod]
 name=ZFS on Linux for EL 7 - kmod
 baseurl=http://download.zfsonlinux.org/epel/7/kmod/$basearch/
-enabled=0
+enabled=1
 metadata_expire=7d
 gpgcheck=1
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-zfsonlinux
```

### 安装zfs

```bash
$ sudo yum install zfs
```

如果安装的是DKMS模式的zfs，请这样执行 `$ sudo yum install kernel-devel zfs`

### 验证安装完成

```bash
$ zpool list
no pools available
```

> **[success] 恭喜**
> 
> 到这一步已经成功安装了zfs了

### 如何移除zfs

销毁存储池、日志池，例如

`$ zpool destroy -f pool`

删除zfs包

`$ sudo yum remove zfs zfs-kmod spl spl-kmod libzfs2 libnvpair1 libuutil1 libzpool2 zfs-release`

## Problems

### 执行命令时发现zfs模块未加载到内核中

```bash
$ sudo zfs list
The ZFS modules are not loaded.
Try running '/sbin/modprobe zfs' as root to load them.
```

这种情况执行 `lsmod|grep zfs` 是没有内容的，按照提示手动加载就可以了： `/sbin/modprobe zfs`，加载后再查看内核是否加载了：

```bash
$ lsmod|grep zfs
zfs                  3559892  0
zunicode              331170  1 zfs
zavl                   15236  1 zfs
icp                   270187  1 zfs
zcommon                73440  1 zfs
znvpair                89131  2 zfs,zcommon
spl                   102412  4 icp,zfs,zcommon,znvpair
```

### 系统重启后没有自动加载zfs内核模块

没有自动加的原因是zfs-import-scan服务默认是disable的，开启就ok了

如果遇到重启存储池没有自动导入，就查看下zfs的哪些服务没有启动，设置为enable就好了

```bash
$ sudo systemctl list-unit-files | grep zfs
zfs-import-cache.service                      enabled 
zfs-import-scan.service                       disabled
zfs-mount.service                             enabled 
zfs-share.service                             enabled 
zfs-zed.service                               enabled 
zfs.target     

$ sudo systemctl enable zfs-import-scan.service
```

### 如何查看zfs的版本

```
$ dmesg | grep ZFS
[  447.184176] ZFS: Loaded module v0.7.9-1, ZFS pool version 5000, ZFS filesystem version 5
```

## Reference

[zfsonlinux wiki](https://github.com/zfsonlinux/zfs/wiki/RHEL-and-CentOS)

