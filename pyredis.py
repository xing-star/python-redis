#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

def redis_node():
    node = redis.StrictRedis(host='127.0.0.1',port=6379)
    node.set("name_test","superadmin")
    print node.get("name_test")


redis_node()

# 此处为本地运行，redis默认端口是6379
# 运行后在终端运行redis-cli进入redis命令行
# 127.0.0.1:6379> get name_test
# 得到superadmin说明交互成功
