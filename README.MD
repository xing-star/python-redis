### Ubuntu下使用python2.7操作Redis

- 前置条件

```
Ubuntu:16.04 内置Python2.7

apt-get install redis-server  # 安装redis

pip install redis  # 安装redis的python驱动

```

### 使用redis常用命令
```
redis-server  # 启动redis服务

redis-cli  # 进入redis客户端

redis-server -v  # 查看redis的版本

ps-ef | grep redis  # 检查后台进程的状态

netstat -| ntp |grep 6379  # 查看当前端口的监听状态
```

### redis设置命令(在redis命令行下)

```
set key value  # 设置key的value

get key # 获取key的value
```
