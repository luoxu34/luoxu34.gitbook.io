# Command Lines

Record the common commands and usage on Linux.

## tree

用作：显示目录树结构

例子：`tree -L 2 -P "*.md|*.py" -I "_book|node_*" -FC`

> **[info] 说明**
>
> -L 就是level显示目录层级
>
> -P 匹配某些文件或目录
>
> -I 忽略某些文件或目录
>
> -F 自动在目录名后加/，可执行文件加*，socket文件加=
>
> -C 显示配色效果

## awk

### 变量

* NF  表示当前记录的字段数
* NR  表示AWK读入的行数
* FNR 表示读入行所在文件中的行数

注：当只有一个输入流时，NR等价于FNR

### 交换域

最近遇到个情况，需要互换一行数据中第1和第15个字段的内容，数据格式如下：

> 1969-12-31 19:00:00|Setup|e64b2af8-68aa-1e1a-ab24-f8420e5e82ad|cm999||1|0|||||e64b2af8-68aa-1e1a-ab24-f8420e5e82ad_1553124830416_1||1|2019-03-20 19:33:50|LayaBox(iPhone; CPU iPhone OS Mac OS X)|||||||||||||||||||||true|true

解决方法：`awk -F '|' -v OFS='|' '{tmp=$1;$1=$15;$15=tmp;}'1 txt > txt2`

### 按照某列划分文本

需求是这样：文件一行为一笔订单，每列间隔符是TAB键，每行第15列是时间戳格式的付费时间，需要根据不同日期，把订单分类到不同文件中。

数据格式如下：

>tlzr_vn	CN1001	49游	vietnam_androidgp	vietnam_androidgp	googleplay	null	STARED	vietnam_1016_16419385	4F9581D3A7C3480591314ACE5D20A364	C58563F4BCD37773	50000.0	RMB	500	1447137754	0   null

解决方法：`awk '{print $0 >> strftime("orders/%Y%m%d_orders.log",$15) }' orders.txt`

## uniq

```bash
# 去除重复行
sort file |uniq

# 查找非重复行
sort file |uniq -u

# 查找重复行
sort file |uniq -d
```

## 匹配TAB键

```bash
grep '\t' test_txt
grep '	' test_txt  # 单引号内的空白是组合键生成的：ctl+v,tab

awk -F '/t' '{print}' test_txt
awk -F '\t' '{print}' test_txt
awk -F '	' '{print}' test_txt  # 同样是组合键生成的TAB隐藏字符
```

## 显示不可见字符

```
cat -A file1

# vim中
:set invlist
:set nolist

```

