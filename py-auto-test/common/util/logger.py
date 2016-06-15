# coding=utf-8
###########################################
# File: logger.py
# Desc: 日志工具类
# Author: zhangyufeng
# History: 2016/1/28 zhangyufeng 新建
###########################################
import os
import logging
import logging.config

# 定义文件路径常量
BASE_CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = BASE_CURRENT_DIR.replace("\\", "/")
LOGGING_CONF_DIR = os.path.join(BASE_DIR + "/conf/", "logging.conf")
LOGS_DIR = BASE_DIR + "/logs/"
LOGS_DEBUG_DIR = BASE_DIR + "/case/logs/"

if os.path.exists(BASE_DIR + "/logs") is False:
    os.makedirs(BASE_DIR + "/logs")
# if os.path.exists(BASE_DIR + "/case/logs") is False:
#     os.makedirs(BASE_DIR + "/case/logs")

ALL_DIR = LOGS_DIR + "all.log"
# ALL_DEBUG_DIR = LOGS_DEBUG_DIR + "all.log"
FILE_DIR = LOGS_DIR + "file.log"
# FILE_DEBUG_DIR = LOGS_DEBUG_DIR + "file.log"

# 判断文件是否存在，不存在则建立
if os.path.exists(ALL_DIR) is False:
    f = open(ALL_DIR, 'a')
    f.close()

# if os.path.exists(ALL_DEBUG_DIR) is False:
#     f = open(ALL_DEBUG_DIR, 'a')
#     f.close()

if os.path.exists(FILE_DIR) is False:
    f = open(FILE_DIR, 'a')
    f.close()

# if os.path.exists(FILE_DEBUG_DIR) is False:
#     f = open(FILE_DEBUG_DIR, 'a')
#     f.close()

# 读取配置文件并建立日志对象
logging.config.fileConfig(LOGGING_CONF_DIR)
logger = logging.getLogger("all")
console = logging.getLogger()
