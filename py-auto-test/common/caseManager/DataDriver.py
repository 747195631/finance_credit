# coding=utf-8
###########################################
# File: DataDriver.py
# Desc: 数据驱动
# Author: 张羽锋
# History: 2015/07/24 张羽锋 新建
###########################################
from pyAuto.caseManage.LoadTestCase import LoadTestCase
import uniout


class DataDriver(uniout):
    def __init__(self):
        pass

    def setRunOnAllRows(self, caseFile, sheetNum=0, readStyle=0):
        u'''
        caseFile->测试用例
        sheetNum->sheet游标，从0开始,存在的sheet页中必须有数据
        readStyle->0时以行读取测试用例,1时以列读取测试用例
        e.g.
            readExcel("c:\login.xls",1,1)
        '''
        xlsCase = LoadTestCase.ReadExcelCase(caseFile)
        for i in range(xlsCase.rowLinesNum):
            print(xlsCase.getXlsData(i))

    def setRunFromTo(self):
        pass
