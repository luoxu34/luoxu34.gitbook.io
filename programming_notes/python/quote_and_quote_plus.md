# quote 和 quote_plus 的区别

## 导入模块

```python
try:
    from urllib import quote, quote_plus  # py2
except ImportError:
    from urllib.parse import quote, quote_plus  # py3
```

## 定义

````python
def quote(string, safe='/', encoding=None, errors=None)

def quote_plus(string, safe='', encoding=None, errors=None):
    if ((isinstance(string, str) and ' ' not in string) or
        (isinstance(string, bytes) and b' ' not in string)):
        return quote(string, safe, encoding, errors)
    if isinstance(safe, str):
        space = ' '
    else:
        space = b' '
    string = quote(string, safe + space, encoding, errors)
    return string.replace(' ', '+')
````

## 例子

```python
print(quote('ab'))   # ab
print(quote('/ab'))  # /ab
print(quote('a b'))  # a%20b

print(quote_plus('ab'))   # ab
print(quote_plus('/ab'))  # %2Fab
print(quote_plus('a b'))  # a+b
```

## 主要区别

1. `safe` 默认参数不同，quote默认会保留`/`不编码
2. 对于空格，`quote` 默认编码成 `%20`，而`quote_plus`是转成`+`号

## 参考

* [How to encode URLs in Python](https://www.urlencoder.io/python/)

