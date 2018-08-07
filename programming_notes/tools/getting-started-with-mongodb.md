# MongoDB入门

环境说明：
* CentOS Linux release 7.5.1804 (Core)
* MongoDB Community Edition 4.0

## Installation

### 配置yum源

```
# vim /etc/yum.repos.d/mongodb-org-4.0.repo
[mongodb-org-4.0]
name=MongoDB Repository
baseurl=http://mirrors.aliyun.com/mongodb/yum/redhat/$releasever/mongodb-org/4.0/$basearch/
#baseurl=http://mirrors.cloud.aliyuncs.com/mongodb/yum/redhat/$releasever/mongodb-org/4.0/$basearch/
gpgcheck=0
enabled=1
```

### 安装mongodb

```
# yum install -y mongodb-org
```

安装`mongodb-org`实际上找到下面几个相应的包进行安装：

* mongodb-org-server: 服务端，包含mongod守护进程、配置文件和初始化脚本
* mongodb-org-mongos: 包含mongos守护进程
* mongodb-org-shell: 数据库交互shell，本地和远程连接客户端
* mongodb-org-tools: 常用工具，主要是mongoimport bsondump, mongodump, mongoexport, mongofiles, mongorestore, mongostat, and mongotop

### 启动数据库

```
# systemctl start mongod
```

### 进入数据库

```
# mongo --host 127.0.0.1:27017
MongoDB shell version v4.0.0
connecting to: mongodb://127.0.0.1:27017/
MongoDB server version: 4.0.0
>
```

默认监听端口是27017，数据库配置文件位于`/etc/mongod.conf`

## Configuration

### 数据库认证authorization

#### 创建root用户

```
# mongo --host 127.0.0.1:27017
> use admin
> db.createUser( {
user: "用户名",
pwd: "密码",
roles: [ { role: "root", db: "admin" } ]
});
```

#### 开启数据库认证

```
# vim /etc/mongod.conf
security:
  authorization: enabled
```

#### 登陆

```
# mongo --host 127.0.0.1:27017
> use admin
> db.auth("用户名","密码"); 
```

或者

```
mongo --authenticationDatabase admin -u root -p xxxx
```

### 警告warning

如果进入mongo shell时见到一些类似下面的**warning**，那你应该做些改变了。

```
MongoDB server version: 4.0.0
Server has startup warnings:

** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
**          See http://dochub.mongodb.org/core/prodnotes-filesystem

** WARNING: Access control is not enabled for the database.
**          Read and write access to data and configuration is unrestricted.

** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
**        We suggest setting it to 'never'

** WARNING: /sys/kernel/mm/transparent_hugepage/defrag is 'always'.
**        We suggest setting it to 'never'

** WARNING: soft rlimits too low. rlimits set to 1024 processes, 65535 files.
            Number of processes should be at least 32767.5 : 0.5 times number of files.

```

下面是解决办法，修改后应该重启数据库。

* 问题一：文件系统更换成`XFS`，而不是ext4或者更老的文件系统

* 问题二：`/etc/mongod.conf`中开启数据库认证登陆`authorization: enabled`

* 问题三：关闭THP

    参考官方教程： https://docs.mongodb.com/manual/tutorial/transparent-huge-pages/

* 问题四：调整内核参数
    
    ```
    # vim /etc/security/limits.conf
    mongod  soft  nofile  64000
    mongod  hard  nofile  64000
    mongod  soft  nproc  32000
    mongod  hard  nproc  32000
    ```

## Connection

### python连接mongodb

首先要安装pymongo

```
# pip install pymongo
```

下面是简单的示例：

```
In [1]: import pymongo

In [2]: uri = "mongodb://root:password@127.0.0.1:27017"  # 不需要认证时可以省略root:password@

In [3]: db = pymongo.MongoClient(uri)

In [4]: db
Out[4]: MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True)

In [5]: db.list_database_names()
Out[5]: ['admin', 'config', 'local', 'test']
```

## reference

* 官方教程[Install MongoDB](https://docs.mongodb.com/manual/installation/)

