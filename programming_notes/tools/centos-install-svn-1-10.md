# CentOS安装svn1.10

## 设置软件源

```bash
$ cat wandisco-svn.repo
[WandiscoSVN]
name=Wandisco SVN Repo
baseurl=http://opensource.wandisco.com/centos/$releasever/svn-1.10/RPMS/$basearch/
enabled=1
gpgcheck=0
```

## 安装

```bash
$ sudo yum repolist
$ sudo yum install subversion -y
```

## 验证

```bash
$ svn --version
svn, version 1.10.0 (r1827917)
````

