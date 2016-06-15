# -*- coding:utf8 -*-
###########################################
# File: GetSms.py
# Desc: 获取短信验证码
# Author: zhangyufeng
# History: 2016/3/7 zhangyufeng 新建
###########################################
from common.dbHandles.MysqlHandler import MysqlHandler
from common.dbHandles.RedisHandler import RedisHandler
from conf.mysqlConf import *
from conf.redisConf import *


class GetSms(object):
    def __init__(self, redis_host=REDIS_HOST, redis_port=REDIS_PORT, redis_password=REDIS_PASSWORD,
                 mysql_user=MYSQL_USER, mysql_host=MYSQL_HOST,
                 mysql_port=MYSQL_PORT, mysql_password=MYSQL_PASSWORD, mysql_db=MYSQL_DB):
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__redis_password = redis_password
        self.__mysql_user = mysql_user
        self.__mysql_host = mysql_host
        self.__mysql_port = mysql_port
        self.__mysql_password = mysql_password
        self.__mysql_db = mysql_db

    def get_sms_num_from_redis(self, redis_key_phone_number):
        redis_object = RedisHandler(redis_host=self.__redis_host, redis_port=self.__redis_port,
                                    redis_password=self.__redis_password)
        redis_key = str(redis_key_phone_number) + "authUserSendCode"
        # 由于取验证码时获取的是二进制数据，所以字符串化以后切片取值
        redis_value = str(redis_object.get_redis_data(redis_key))
        sms_num = "无对应手机号的短信验证码"
        if redis_object.get_redis_data(redis_key) is not None:
            sms_num = redis_value[-5:-1]
        return sms_num

    def get_sms_num_from_db(self, phone_number):
        select_sql = "select sms_content from member_sms_log where sms_phone=" + str(
            phone_number) + " order by log_id desc"
        mysql_object = MysqlHandler(mysql_user=self.__mysql_user, mysql_password=self.__mysql_password,
                                    mysql_host=self.__mysql_host,
                                    mysql_port=self.__mysql_port, mysql_db=self.__mysql_db)
        data_list = mysql_object.get_mysql_data(select_sql)
        sms_num = "无对应手机号的短信验证码"
        if data_list:
            sms_num = data_list[0][0]
        return sms_num
