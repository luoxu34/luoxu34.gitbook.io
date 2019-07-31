# Tmux 入门

## 安装

软件源里的Tmux一般是1.x的，版本比较低，有的功能还不支持，所有墙裂建议自己编译安装2.x或3.x的版本。

另外由于 `Tmux` 依赖 [`libevent 2.x`](https://github.com/libevent/libevent/releases/latest) 和 [`ncurses`](https://github.com/libevent/libevent/releases/latest)，所以要先编译安装这两个模块。

最后从Git仓库上下载最新的版本编译安装 [Tmux](https://github.com/tmux/tmux/releases) 就可以了。

## 常用命令

| 作用                       | 命令                           |
| -------------------------- | ------------------------------ |
| 创建默认会话，会以数字命名 | tmux                           |
| 创建会话时指定会话名称     | tmux new -s name               |
| 后台方式创建会话           | tmux new -s name -d            |
| 查看所有会话               | tmux ls                        |
| 登录某个会话               | tmux a -t name                 |
| 销毁会话                   | tmux kill-session -t name      |
| 重命名会话                 | tmux rename -t oldname newname |

## 三级关系

tmux的三级关系是：session : windows : panel

## 组合键

引用来源：https://www.cnblogs.com/kevingrace/p/6496899.html

| 操作符       | 作用                                                         |
| ------------ | ------------------------------------------------------------ |
| **系统操作** |                                                              |
| ?            | 列出所有快捷键；按q返回                                      |
| **d**        | 脱离当前会话，输入tmux attach能够重新进入之前的会话          |
| D            | 选择要脱离的会话；在同时开启了多个会话时使用                 |
| Ctrl+z       | 挂起当前会话                                                 |
| r            | 强制重绘未脱离的会话                                         |
| **s**        | 选择并切换会话；在同时开启了多个会话时使用                   |
| :            | 进入命令行模式；此时可以输入支持的命令，例如kill-server可以关闭服务器 |
| **[**        | 进入复制模式；此时的操作与vi/emacs相同，按q/Esc退出          |
| ~            | 列出提示信息缓存；其中包含了之前tmux返回的各种提示信息       |
|              |                                                              |
| **窗口操作** |                                                              |
| **c**        | 创建新窗口                                                   |
| **&**        | 关闭当前窗口                                                 |
| **数字键**   | 切换至指定窗口                                               |
| p            | 切换至上一窗口                                               |
| n            | 切换至下一窗口                                               |
| l            | 在前后两个窗口间互相切换                                     |
| **w**        | 通过窗口列表切换窗口                                         |
| **,**        | 重命名当前窗口；这样便于识别                                 |
| .            | 修改当前窗口编号；相当于窗口重新排序                         |
| **f**        | 在所有窗口中查找指定文本                                     |
|              |                                                              |
| **面板操作** |                                                              |
| **z**        | 最大化/还原面板                                              |
| ”            | 将当前面板平分为上下两块                                     |
| %            | 将当前面板平分为左右两块                                     |
| **x**        | 关闭当前面板                                                 |
| !            | 将当前面板置于新窗口；即新建一个窗口，其中仅包含当前面板     |
| Ctrl+方向键  | 以1个单元格为单位移动边缘以调整当前面板大小                  |
| Alt+方向键   | 以5个单元格为单位移动边缘以调整当前面板大小                  |
| **Space**    | 在预置的面板布局中循环切换                                   |
| **q**        | 显示面板编号                                                 |
| o            | 在当前窗口中选择下一面板                                     |
| 方向键       | 移动光标以选择面板                                           |
| {            | 向前置换当前面板                                             |
| }            | 向后置换当前面板                                             |
| Alt+o        | 逆时针旋转当前窗口的面板                                     |
| Ctrl+o       | 顺时针旋转当前窗口的面板                                     |

## 配置文件

https://github.com/gpakosz/.tmux

一些重要的配置

```
# 修改prefix键
set -gu prefix2
unbind C-a
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# 分屏快捷键
unbind '"'
bind - splitw -v
unbind %
bind \ splitw -h

# 使用Alt+方向键快速切换面板
bind -n    M-Up select-pane -U
bind -n  M-Down select-pane -D
bind -n  M-Left select-pane -L
bind -n M-Right select-pane -R

# 强制vi模式
set -g status-keys vi
set -g mode-keys vi

# 启用鼠标模式 tmux>2.1
set-option -g mouse on

# 启用鼠标模式 tmux<2.1
setw -g mouse-resize-pane on    # 鼠标拖动调节pane的大小
setw -g mouse-select-pane on    # 鼠标点击激活pane
setw -g mouse-select-window on  # 鼠标点击切换window
setw -g mode-mouse on           # 开启window/pane里面的鼠标支持
```

##  共享会话

不同用户如果想使用同一个tmux会话，需要通过linux上的socket访问：

```
# root用户创建socket连接
tmux -S /tmp/t_socket

# 赋予其他用户访问权限
chmod 777 /tmp/t_socket

# 普通用户通过socket登录root的tmux会话
tmux -S /tmp/t_socket attach

# 回收会话
rm -f /tmp/t_socket
```

