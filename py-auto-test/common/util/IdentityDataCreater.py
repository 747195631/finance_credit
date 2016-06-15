# coding=utf-8
###########################################
# File: InterfaceDataProcessing.py
# Desc: 身份数据生成器
# Author: zhangyufeng
# History: 2015/11/21 zhangyufeng 新建
###########################################
import os
import random
from datetime import date
from datetime import timedelta

from common.util.logger import logger

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DC_PATH = BASE_DIR + "\districtcode.txt"


# 随机生成身份证号
def get_district_code():
    try:
        with open(DC_PATH) as file:
            data = file.read()
            district_list = data.split('\n')
        for node in district_list:
            # print node
            if node[10:11] != ' ':
                state = node[10:].strip()
            if node[10:11] == ' ' and node[12:13] != ' ':
                city = node[12:].strip()
            if node[10:11] == ' ' and node[12:13] == ' ':
                district = node[14:].strip()
                code = node[0:6]
                code_list.append({"state": state, "city": city, "district": district, "code": code})
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


def generator():
    try:
        global code_list
        code_list = []
        if not code_list:
            get_district_code()
        id = code_list[random.randint(0, len(code_list))]['code']  # 地区项
        id += str(random.randint(1930, 2013))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id += da.strftime('%m%d')
        id += str(random.randint(100, 300))  # ，顺序号简单处理
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5',
                      '9': '3', '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count += int(id[i]) * weight[i]
        id += check_code[str(count % 11)]  # 算出校验码
        return id
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


def generator_const(days_num):
    '''
    此方法生成的是110105开头的当前年月日减去参数天数的随机身份证
    :param days_num: 用来减的天数
    :return: 生成的身份证字符串
    '''
    id = str(110105)
    da = date.today() + timedelta(days=days_num)
    id += da.strftime('%Y%m%d')
    id += str(random.randint(100, 300))  # ，顺序号简单处理
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5',
                  '9': '3', '10': '2'}  # 校验码映射
    logger.debug(id)
    for i in range(0, len(id)):
        count += int(id[i]) * weight[i]
    id += check_code[str(count % 11)]  # 算出校验码
    return id
