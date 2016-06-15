# coding=utf-8
###########################################
# File: TimeStamp.py
# Desc: 时间戳生成工具
# Author: zhangyufeng
# History: 2015/08/18 zhangyufeng 新建
###########################################
import time

from common.util.logger import logger


class TimeStamp(object):
    @classmethod
    def time_stamp(cls):
        try:
            # 格式化
            time_format1 = '%Y%m%d%H%M%S'
            return time.strftime(time_format1)
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")
