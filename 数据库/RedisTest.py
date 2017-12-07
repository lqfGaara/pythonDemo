# coding:utf8
import redis

class RedisHelper:
    # 建立连接
    def __init__(self, host, port):
        self.redis = redis.Redis(host=host, port=port)

    # 存储数据
    def setValue(self, key, value):
        self.redis.set(key, value)

    # 取数据
    def getValue(self, key):
        try:
            return self.redis.get(key)
        except Exception as e:
            return None
