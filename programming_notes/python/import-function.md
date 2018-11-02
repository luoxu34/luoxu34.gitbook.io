# 动态加载模块

## 知识要点

* `__import__`函数
* `getattr`函数

## 例子最明显

```python

目录结构如下时：
└── a.py

In [1]: a = __import__('a')

In [2]: a
Out[2]: <module 'a' from 'a.py'>

In [3]: dir(a)
Out[3]: ['B', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a']

In [4]: a.B
Out[4]: '123'

In [5]: a.a()
a

In [6]: getattr(a, 'B')
Out[6]: '123'

In [7]: getattr(a, 'a')()
a

目录结构如下时：
test
├── __init__.py
└── test1.py

In [1]: t = __import__('test')

In [2]: t
Out[2]: <module 'test' from 'test/__init__.pyc'>

In [3]: dir(t)
Out[3]: ['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__']

In [4]: tt = __import__('test.test1', fromlist=['test1'])

In [5]: tt
Out[5]: <module 'test.test1' from 'test/test1.pyc'>

In [6]: dir(tt)
Out[6]: ['A', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'b']

目录结构如下时：
├── test.py
└── test
    ├── __init__.py
    └── test1.py
    
In [1]: t = __import__('test')

In [2]: t
Out[2]: <module 'test' from 'test/__init__.pyc'>

```

