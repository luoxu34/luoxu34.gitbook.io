# Python陷阱

## py2.6和2.7的除法

遇到同一个项目，但是一个运行再`python2.6`上，一个运行再`python2.7`上，第一个陷阱就出现了：

py2.7中，499 / 100.0 = 4.99

```python
Python 2.7.5 (default, Aug 31 2016, 17:13:33)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 4.99 / 100.0
0.0499
>>>
>>> 499 / 100.0
4.99
```

py2.6中，**499 / 100.0 = 4.9900000000000002**

```python
Python 2.6.6 (r266:84292, Aug 18 2016, 15:13:37)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 4.99 / 100.0
0.0499
>>>
>>> 499 / 100.0
4.9900000000000002
>>>
>>> float(499) / 100.0
4.9900000000000002
>>>
>>>
>>> 499.0 / 100.0
4.9900000000000002
```

这个问题留意一下就好，迁移到py3是最好的建议。

