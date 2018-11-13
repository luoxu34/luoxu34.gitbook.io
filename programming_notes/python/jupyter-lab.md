# Jupyter Lab

这里是[Jupyter Lab的官方文档](https://jupyterlab.readthedocs.io/)。

上一篇介绍了 [Jupyter Notebook](a-trip-to-jupyter.md)，这回介绍 `Jupyter Lab`。

`Jupyter Lab`是`Jupyter`的下一代产品，炫酷多了。

如果说 `Jupyter` 是火车，那 `Jupyter Lab` 就是高铁了。

## 安装

```bash
$ conda install jupyterlab
```

## 运行

```bash
# 直接运行
$ jupyter-lab

# 后台运行
$ nohup jupyter-lab > /var/log/jupyter-lab.log 2>&1 &
```

不用重新配置参数，默认和 `Jupyter` 是同一套配置。

## 效率

使用快捷键才能提高效率，快捷键查看[上一篇文章](a-trip-to-jupyter.md)。

## 编写启动脚本

```bash
#!/usr/bin/env sh
# filename: jupyter_server.sh
# author  : luoxu34<luoxu34@outlook.com>
# date    : 2018-11-07

LOG_FILE="/var/log/jupyter-lab.log"
PID_FILE="/var/run/jupyter-lab.pid"

echo_url(){
  echo "https://your_ip_or_url:your_port"
}

get_pid(){
  lab_pid=`ps x | grep jupyter-lab | grep -v grep | awk '{print $1}'`
  echo $lab_pid
}

start(){
  # lab_pid=`get_pid`
  lab_pid=`cat ${PID_FILE}`

  test ${lab_pid}  && ps -p ${lab_pid} > /dev/null && \
    echo "Jupyter is running, enjoy!" && exit

  # 激活环境，并启动jupyter-lab，最后打印浏览器访问的URL
  source activate jupyter
  nohup jupyter-lab > $LOG_FILE 2>&1 &

  lab_pid=`get_pid`
  echo "${lab_pid}" > $PID_FILE

  echo "PID is ${lab_pid}, hurry up!"
  echo_url
}

stop(){
  lab_pid=`cat ${PID_FILE}`

  if [ -z "${lab_pid}" ]; then
    echo "No running"
  else
    echo "kill ${lab_pid}, goodbye..."
    kill ${lab_pid}
    echo > ${PID_FILE}
  fi
}

status(){
  lab_pid=`cat ${PID_FILE}`

  test ${lab_pid} && ps -p ${lab_pid} > /dev/null && \
    echo "[${lab_pid}] Jupyter Lab is running, enjoy!" && \
    echo_url || \
  echo "Jupyter Lab is not running, sad!"
}

restart(){
  stop
  # sleep 1
  start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
    status
    ;;
  restart)
    restart
    ;;
  url)
    echo_url
    ;;
  *)
    echo $"Usage: $0 {start|stop|status|restart|url}"
    exit 2
esac

exit $?
```

## 最后

我已经开始使用`Jupyter Lab`，你还在等什么！

