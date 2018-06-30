# 写作由来

自己常用 PuTTYTray 连接服务器，但是之前一直没有记录，一旦切换环境后总是不记得之前的配置是什么。好记性不如烂笔头，所以这里记录一下自己的常用配置，以免忘记。

[PuTTYTray](https://puttytray.goeswhere.com/)官网：https://puttytray.goeswhere.com/

在GitHub上的下载地址：https://github.com/FauxFaux/PuTTYTray/releases

# 配置笔记

## session保存到文件

![](../images/putty_tray/1_sessions.png)

> ** [info] 提示**
>
> 保存到文件方便修改和保留配置，但是保存到注册表方便其他工具使用session，例如WinSCP

## 禁止bell

![](../images/putty_tray/2_bell_disable.png)

## 设置窗口大小和行记录

![](../images/putty_tray/3_size_and_line.png)

## 设置字体类型和大小

![](../images/putty_tray/4_font.png)

## 开启全屏快捷键

![](../images/putty_tray/5_behaviour.png)

## Ctrl+Etner才打开超链接

![](../images/putty_tray/6_hyperlinks.png)

## 保持长连接

![](../images/putty_tray/7_keepalives.png)

## 设置登陆用户名

![](../images/putty_tray/8_login_username.png)

## 启动压缩

![](../images/putty_tray/9_compression.png)

## 使用SSH认证登陆

![](../images/putty_tray/10_pem.png)

## 配色 Color Scheme

我使用的是 [solarized dark](https://github.com/altercation/solarized/tree/master/putty-colors-solarized)，需要手动替换session文件中的内容。

# Solarized Dark

[solarized_dark_puttytray.txt](https://github.com/altercation/solarized/blob/master/putty-colors-solarized/solarized_dark_puttytray.txt) 

    Colour21\253,246,227\
    Colour20\238,232,213\
    Colour19\147,161,161\
    Colour18\42,161,152\
    Colour17\108,113,196\
    Colour16\211,54,130\
    Colour15\131,148,150\
    Colour14\38,139,210\
    Colour13\101,123,131\
    Colour12\181,137,0\
    Colour11\88,110,117\
    Colour10\133,153,0\
    Colour9\203,75,22\
    Colour8\220,50,47\
    Colour7\0,43,56\
    Colour6\7,54,66\
    Colour5\238,232,213\
    Colour4\0,43,54\
    Colour3\7,54,66\
    Colour2\0,43,54\
    Colour1\147,161,161\
    Colour0\131,148,150\
