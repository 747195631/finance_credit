# coding=utf-8
###########################################
# File: readConfig.py
# Desc: 读取配置文件工具类
# Author: zhangyufeng
# History: 2015/10/13 zhangyufeng 新建
###########################################
import configparser
import os
import platform

from common.util.logger import logger

# 定义文件路径常量
BASE_CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = BASE_CURRENT_DIR
if platform.system() == "Windows":
    BASE_DIR = BASE_CURRENT_DIR.replace("\\", "/")


class ReadConfig:
    u'''
        conf.ini和config.conf配置文件路径不可更改
    '''

    def __init__(self):
        try:
            current_dir = os.getcwd()
            self.__ini_config_file = BASE_DIR + "/conf/" + "config.ini"
            self.__conf_config_file = BASE_DIR + "/conf/" + "config.conf"
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 读取windows ini配置文件
    # 配置文件格式
    #   [table]
    #   key=value
    def ini_data(self, label, key, configFile=None):
        try:
            config = configparser()
            if configFile is None:
                configFile = self.__ini_config_file
            config.read(configFile)
            return config.get(label, key)
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 读取linux配置文件
    # 配置文件格式
    #   key=value
    def conf_data(self, key, configFile=None):
        try:
            if configFile is None:
                configFile = self.__conf_config_file
            config_file = open(configFile, 'r')
            result = config_file.readlines()
            result_deal_list = []
            key_value_list = []
            for i in result:
                result_deal_list.append(i.strip('\n'))
            for j in result_deal_list:
                key_value_list.append(j.split('='))
            result_dict = dict(key_value_list)
            return result_dict[key]
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")
