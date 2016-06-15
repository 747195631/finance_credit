# coding=utf-8
###########################################
# File: InterfaceDataProcessing.py
# Desc: http接口处理工具类
# Author: zhangyufeng
# History: 2015/11/20 zhangyufeng 新建
###########################################
from util.Md5 import Md5
from util.TimeStamp import TimeStamp

from common.util.logger import logger


class InterfaceDataProcessing(object):
    def __init__(self, interface_code, data_dict, secretkey_value):
        try:
            # 生成时间戳
            self.__time_stamp = TimeStamp.time_stamp()
            self.__data_dict = data_dict
            self.__secretkey_value = secretkey_value
            self.__interface_code = interface_code
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 接口数据处理方法，key为interface_code
    def processing(self):
        try:
            processing_dict = dict()
            # 字典生成key和value的对应关系，value为方法对象而不是执行方法
            processing_dict["ytdyccrmcancel"] = self.ytdyccrm_cancel_func
            if self.__interface_code.decode("utf-8") in processing_dict:
                return processing_dict[self.__interface_code.decode("utf-8")]()
            else:
                return 0
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 烟台大悦城会员卡解绑接口数据处理方法
    def ytdyccrm_cancel_func(self):
        try:
            self.__data_dict["dt"] = self.__time_stamp
            sign_str = str(self.__data_dict["dt"]) + self.__data_dict["method"] + str(2.0) + self.__secretkey_value
            sign = Md5.md5(sign_str)
            self.__data_dict["sign"] = sign
            return self.__data_dict
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 处理application/x-www-form-urlencoded数据（a=1&b=1）为字典
    @classmethod
    def urldecoded(self, data):
        try:
            data_list_first = data.split("&")
            data_list_second = list()
            for tmp in data_list_first:
                data_list_second.append(tmp.split("="))
                result = dict()
            for i in data_list_second:
                result[i[0]] = i[1]
            return result
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")
