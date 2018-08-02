# 弄懂 git diff

## 理解 git workflow

![Git Workflow](../images/git-workflow.png)

一个文件的局部生命周期：

1. 文件创建的时候存在工作区，状态是unstaged
2. 文件被修改，但是未追踪，这时存在工作区，状态依旧是unstaged
3. 被追踪之后存在暂存区staging，状态变成了staged
4. 提交commit之后存在本地仓库
5. 最后推送push到远程仓库

## git diff的作用

`show changes between commits, commit and working tree, etc.`

## 区别

| git commands      | distinctive       | explanation |
| ----------------- | ----------------- | ----------- |
| git diff          | staged ^ unstaged | 比较文件在工作区和暂存区的差异 |
| git diff --cached | staged ^ commited | 比较文件在暂存区和仓库的差异   |
| git diff HEAD     |(staged + unstaged) ^ commited | 比较文件在工作区+暂存区和仓库的差异 |

