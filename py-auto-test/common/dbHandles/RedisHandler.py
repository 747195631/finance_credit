# -*- coding:utf-8 -*-
import redis


class RedisHandler(object):
    def __init__(self, redis_host=None, redis_port=6379, redis_password=None):
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__redis_password = redis_password

    def get_redis_data(self, redis_key):
        '''
        :param redis_key: redis的key
        :return: 直接返回redis的值
        '''
        redis_object = redis.StrictRedis(host=self.__redis_host, port=self.__redis_port, password=self.__redis_password)
        # 由于取验证码时获取的是二进制数据，所以字符串化以后切片取值
        redis_value = redis_object.get(redis_key)
        return redis_value

