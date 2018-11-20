# Python timestamp和datetime相互转换

首先说明，Python生成的Unix时间戳是秒级的，小数点前有10位，Java生成的时间戳毫秒级的，小数点前有13位，所以通讯时要注意一下。

## 生成Unix时间戳

```python
# 生成Unix时间戳
ts = time.time()

print(ts)
print(int(ts))                # 转成10位的时间戳格式
print(int(round(ts * 1000)))  # 转成13位的时间戳格式

# 1542621530.7437315
# 1542621530
# 1542621530744
```

## timestamp转datetime

```python
ts = time.time()
dt = datetime.datetime.fromtimestamp(int(ts))  # 参数是int，字符串是不可以的
dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')

print('timestamp:', ts)
print(' datetime:', dt)
print(' datetime: ' + dt_str)

# timestamp: 1542621452.9544733
#  datetime: 2018-11-19 17:57:32.954473
#  datetime: 2018-11-19 17:57:32
```

## datetime转timestamp

```python
dt = '2018-11-19 17:57:32'

#转换成时间数组
time_array = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(time_array)

print(timestamp)
# 1542621452.0
```

## 使用Arrow库处理时间

```python
import arrow, time

# 当前时间戳
ts = time.time()
# ts = arrow.utcnow().timestamp

# 构造Arrow对象
t1 = arrow.get(ts)

# datetime对象转成timestamp
t2 = arrow.get(t1.datetime)
t2.timestamp

# Arrow转成字符串的datetime
dt_str = t1.format('YYYY-MM-DD HH:mm:ss')

# 字符串的datetime转成timestamp
t3 = arrow.get(dt_str)
t3.timestamp
```

可见，arrow处理时间更优雅，也不用去记各种类型和方法，像我每次都记不得`strptime`和`strftime`是哪种类型转哪种。

## 最后说一句

不带时区的时间，不够规范。

