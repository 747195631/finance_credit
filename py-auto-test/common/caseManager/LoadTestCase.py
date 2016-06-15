# coding=utf-8
###########################################
# File: loadTestCase.py
# Desc: 测试用例处理
# Author: zhangyufeng
# History: 2015/07/24 zhangyufeng 新建
###########################################
import xlrd


class LoadTestCase(object):
    class ReadExcelCase:
        def __init__(self, caseFile, readStyle=0, sheetNum=0):
            u'''
                caseFile->测试用例
                sheetNum->sheet游标，从0开始,存在的sheet页中必须有数据
                readStyle->0时以行读取测试用例,1时以列读取测试用例
                e.g.
                    readExcel("c:\login.xls",1,1)
            '''
            xls = xlrd.open_workbook(caseFile)
            self.table = xls.sheets()[sheetNum]
            self.__readStyle = readStyle
            self.rowLinesNum = self.table.nrows
            self.colLinesNum = self.table.ncols

        def getXlsData(self, num=1):
            u'''
                num为当前行号或列号
            '''
            if self.__readStyle == 0:
                return self.table.row_values(num - 1)
            elif self.__readStyle == 1:
                return self.table.col_values(num - 1)

    class ReadXmlCase:
        def __init__(self):
            pass

        def readXmlCase(self):
            pass
