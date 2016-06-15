# coding=utf-8
###########################################
# File: Md5.py
# Desc: md5加密
# Author: zhangyufeng
# History: 2015/08/18 zhangyufeng 新建
###########################################
import hashlib

from common.util.logger import logger


class Md5(object):
    @classmethod
    def md5(cls, strVar):
        try:
            # md5加密并小写化
            md5_var = hashlib.md5()
            md5_var.update(strVar.encode("utf-8"))
            # md5_var.update(strVar)
            sign = md5_var.hexdigest().lower()
            return sign
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")
