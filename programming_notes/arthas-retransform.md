# Arthas热更代码实践

## 启动

```shell
java -jar arthas-boot.jar <pid>
java -jar arthas-boot.jar --select arthas-demo
```

### 注意

* arthas和目标进程需要具有相同的权限
* arthas和目标进程最好运行的JDK版本要一致

## 退出

`quit`和`exit`命令：只退出当前连接，其他 Arthas 客户端不受影响。Attach到目标进程上的arthas还会继续运行，端口会保持开放，下次连接时可以直接连接上。

`stop`和`shutdown`命令：完全退出arthas，所有 Arthas 客户端全部退出。退出前会自动重置所有增强过的类。

## 热更代码

### 参考文档

[Arthas retransform 命令](https://arthas.gitee.io/retransform.html)

### 限制

* 不允许新增加field/method，enum是无法增强的
* 正在跑的函数，没有退出不能生效

### 热更步骤

```shell
# 启动arthas并attach到目标进程
java -jar arthas-boot.jar <pid>
# retransform jvm
retransform /tmp/MathGame.class /tmp/MathGame2.class
# 退出arthas
stop
```

### 撤销热更

方法一：再热更一次新的class文件

方法二：删除 retransform entry
1. 删除类对应的 retransform entry
2. 重新触发 retransform

```shell
# 查看 retransform entry
retransform -l
# 删除指定 retransform entry
retransform -d <id>
# 删除所有 retransform entry
retransform --deleteAll
# 显式触发 retransform
retransform --classPattern *MathCalssNamePath
```

