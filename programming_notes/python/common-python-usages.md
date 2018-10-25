# Common Python Usages

## 反转字符串

```python
s = 'test string'

# 1.使用字符串切片
s1 = s[::-1]

# 2.使用列表的reverse方法
l = list(s)
l.reverse()      # reverse方法返回值为None，该行必须这样写
s2 = ''.join(l)  # join的对象必须可迭代

# 3.使用reversed内置函数
s3 = ''.join(reversed(s))
```

## F-strings

新鲜事物，python3.6.2开始出现，PEP 498提出的一种新型字符串格式化机制

```python
name = 'luoxu34'
print(f'hello {name}')    # 'hello luoxu34'
```

## 漂亮的json格式

```python
import json
data = dict(name='广州', area_code='020')
print(json.dumps(data, indent=4, ensure_ascii=False))
```
Output:
```json
{
    "name": "广州",
    "area_code": "020"
}
```

## 判断文件是否可读写

```python
import os
os.access(path, mode)
```

参数 `mode` 有：
* os.F_OK 检查文件是否存在
* os.R_OK 检查文件是否可读
* os.W_OK 检查文件是否可以写入
* os.X_OK 检查文件是否可以执行

