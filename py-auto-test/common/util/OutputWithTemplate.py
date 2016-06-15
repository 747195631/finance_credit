# -*- coding:utf-8 -*-
import xlrd
import xlwt
from util.TimeStamp import TimeStamp

from common.util.logger import logger


class OutputWithTemplate(object):
    def output_with_excel(self, template_file, sheet_count, data_list):
        '''
        :param template_file: 模板文件路径
        :param sheet_count: 模板文件容sheet的个数，比如5个sheet页通过这个参数可以指定就用3个
        :param data_list: 数据list，其中包含sheet页list，表头list，数据list
        本方法中均使用list进行数据操作，由于模板中第一行为标题，故插入数据的行数索引从1开始
        '''
        try:
            data = xlrd.open_workbook(template_file)
            sheet_name = data.sheet_names()
            sheet_list = list()
            # 将模板文件sheet对象存入sheet_list列表
            for i in range(sheet_count):
                sheet_list.append(data.sheets()[i])
            template_data_list = list()
            # 将模板文件每个sheet的数据list存入tempLate_data_list列表
            for i_sheet in sheet_list:
                template_data_list.append(i_sheet.row_values(0))
            output_file = xlwt.Workbook()
            # 字体设定
            font = xlwt.Font()
            font.bold = True
            # 边框设定
            borders = xlwt.Borders()
            borders.left = 1
            borders.right = 1
            borders.top = 1
            borders.bottom = 1
            # 背景色设定
            backcolor = xlwt.Pattern()
            backcolor.pattern = xlwt.Pattern.SOLID_PATTERN
            backcolor.pattern_fore_colour = 5
            style = xlwt.XFStyle()
            style.font = font
            style.borders = borders
            style.pattern = backcolor
            output_file_sheet_list = list()
            # 输出文件添加sheet并给予标题,对象存入output_file_sheet_list列表
            for j in range(sheet_count):
                output_file_sheet_list.append(output_file.add_sheet(sheet_name[j], cell_overwrite_ok=True))
            # j_sheet_num为sheet页的索引
            for j_sheet_num in range(len(sheet_list)):
                # j_sheet_row_index为模板文件template_dataList的索引
                for j_sheet_row_index in range(len(template_data_list[j_sheet_num])):
                    output_file_sheet_list[j_sheet_num].write(0, j_sheet_row_index,
                                                              template_data_list[j_sheet_num][j_sheet_row_index], style)

            # 数据格式为{"sheet页数":{"列数":[当前添加的数据1,当前添加的数据2]}}
            filter_dict = dict()
            logger.debug("++++++++++++++++++++++++++++++")
            logger.debug(data_list)
            # 以追加方式添加数据
            for data_num in range(len(data_list[0])):
                logger.debug(data_num)
                logger.debug(data_list)
                # 当前sheet的索引
                data_sheet_num = int(data_list[0][data_num]) - 1
                data_row_num = 1
                data_col_num = int(data_list[1][data_num]) - 1
                logger.debug("===================================")
                logger.debug(data_sheet_num)
                logger.debug(data_col_num)
                # 判断当前sheet页数是否在filter_dict中，即当前sheet是否曾经出现过
                if str(data_sheet_num) not in filter_dict:
                    # 当前sheet页数不存在filter_dict,添加对应data_sheet_num字典
                    filter_dict[str(data_sheet_num)] = {}
                    # 增加对应列数的数据list
                    filter_dict[str(data_sheet_num)][str(data_col_num)] = list()
                    # 由于sheet页数第一次出现，故数据也一定第一次出现，所以之列列表中添加值
                    filter_dict[str(data_sheet_num)][str(data_col_num)].append(data_col_num)
                else:
                    # 当前sheet页数存在filter_dict中，判断当前列数是否在列数字典中，即当前列数是否出现过
                    if str(data_col_num) not in filter_dict[str(data_sheet_num)]:
                        # 当前列数未出现过,添加列表
                        filter_dict[str(data_sheet_num)][str(data_col_num)] = list()
                        # 向列数字典列表插数据，但插入数据的当前行数为初始值，即1
                        filter_dict[str(data_sheet_num)][str(data_col_num)].append(data_col_num)
                    else:
                        # 当前列数出现过。向列数字典列表插数据，插入数据的当前行数为总出现的次数
                        filter_dict[str(data_sheet_num)][str(data_col_num)].append(data_col_num)
                        data_row_num = len(filter_dict[str(data_sheet_num)][str(data_col_num)])
                logger.debug(filter_dict)
                data_preview_add = data_list[2][data_num]
                # 向excel中插入数据
                output_file_sheet_list[data_sheet_num].write(data_row_num, data_col_num, data_preview_add)

            output_file.save(str(TimeStamp.time_stamp()) + ".xls")


        except:
            logger.exception("发现错误")
