# Command Lines

Record the common commands and usage on Linux.

## tree

用作： 显示目录树结构

例子： `tree -L 2 -P "*.md|*.py" -I "_book|node_*" -FC`

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

最近遇到个情况，需要互换一行数据中第1和第15个字段的内容，数据格式如下：

> 1969-12-31 19:00:00|Setup|e64b2af8-68aa-1e1a-ab24-f8420e5e82ad|cm999||1|0|||||e64b2af8-68aa-1e1a-ab24-f8420e5e82ad_1553124830416_1||1|2019-03-20 19:33:50|LayaBox(iPhone; CPU iPhone OS Mac OS X)|||||||||||||||||||||true|true

解决方法：`awk -F '|' -v OFS='|' '{tmp=$1;$1=$15;$15=tmp;}'1 txt > txt2`

