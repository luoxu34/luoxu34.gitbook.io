# case一例和init脚本一例

Confluence的启动脚本，也可以作为case语句的例子

`cat /etc/init.d/confluence`

```bash
#!/bin/bash

# Confluence Linux service controller script
cd "/opt/atlassian/confluence/bin"

case "$1" in
    start)
        ./start-confluence.sh
        ;;
    stop)
        ./stop-confluence.sh
        ;;
    restart)
        ./stop-confluence.sh
        ./start-confluence.sh
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

