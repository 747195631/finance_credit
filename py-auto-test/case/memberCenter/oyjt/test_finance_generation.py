# encoding=utf-8
import pytest
from common.caseManager.LoadTestCase import LoadTestCase
from common.util.logger import console
from common.dbHandles.MysqlHandler import MysqlHandler
from common.util.TimeStamp import TimeStamp
from common.util.IdentityDataCreater import generator_const
import uuid
import random
from data.base import Financecenter
from data.base import Commcenter
from data.base import Membercenter


def get_userCreditdate(caseFile):
    temp_list = []
    user_info_sheet = LoadTestCase().ReadExcelCase(caseFile, 0, 0)
    user_appinfo_sheet = LoadTestCase().ReadExcelCase(caseFile, 0, 1)
    card_no_sheet = LoadTestCase().ReadExcelCase(caseFile, 0, 2)
    user_info_rowNum = user_info_sheet.rowLinesNum

    for i in range(0, user_info_rowNum):

        if i is not 0:
            temp_list.append(list())
            get_userInfo_data = user_info_sheet.getXlsData(i + 1)
            temp_list[i - 1].append(get_userInfo_data)

            get_userAppInfo_data = user_appinfo_sheet.getXlsData(i + 1)
            temp_list[i - 1].append(get_userAppInfo_data)

            get_cardNo_data = card_no_sheet.getXlsData(i + 1)

            temp_list[i - 1].append(get_cardNo_data)
            temp_list[i - 1] = tuple(temp_list[i - 1])

    return temp_list


caseFile = "data/getdata1.xlsx"
user_credit_result = get_userCreditdate(caseFile)


@pytest.mark.parametrize("tb_userInfo,tb_userAppInfo,card_no", user_credit_result)
def test_finance_generation(tb_userInfo, tb_userAppInfo, card_no):
    userid = str(16) + TimeStamp.time_stamp() + str(int(uuid.uuid1()))[:10]
    member_data = get_member_data(card_no[0])
    wxin_data = get_wxin_data(card_no[0])
    ##############################################################
    # 从getdata.xlsx获取到所有的数据，以此传给相应的字段
    # 通过装饰器实现多个表传参取值
    # 实现自动向tb_user_info表插入数据
    ##############################################################

    card_phone = member_data[0][1]
    card_idno = generator_const(0 - random.random() * (10955 - 10225) - 10225)
    open_id = member_data[0][3]
    wx_nickname = wxin_data[0][0]
    create_time = TimeStamp.time_stamp()
    update_time = TimeStamp.time_stamp()
    integral = tb_userInfo[0]
    delete_flag = tb_userInfo[1]
    finance_com_id = tb_userInfo[2]
    ###################################################################
    # tb_user_appl_info的相应字段
    ###################################################################
    company_detail_address = tb_userAppInfo[0]
    bank_card_name = tb_userAppInfo[1]
    bank_card_no = tb_userAppInfo[2]
    contact_name = tb_userAppInfo[3]
    contact_mobile = tb_userAppInfo[4]
    contact_relation = tb_userAppInfo[5]
    delete_flag = tb_userAppInfo[6]
    pic_front = tb_userAppInfo[7]
    pic_compress_front = tb_userAppInfo[8]
    pic_back = tb_userAppInfo[9]
    pic_compress_back = tb_userAppInfo[10]
    pic_full = tb_userAppInfo[11]
    pic_compress_full = tb_userAppInfo[12]
    province = tb_userAppInfo[13]
    city = tb_userAppInfo[14]
    area = tb_userAppInfo[15]
    company_name = tb_userAppInfo[16]
    contact_address_type = tb_userAppInfo[17]
    user_education = tb_userAppInfo[18]
    marital_status = tb_userAppInfo[19]
    company_size = tb_userAppInfo[20]
    census_reg_address = tb_userAppInfo[21]
    month_income = tb_userAppInfo[22]
    company_work_years = tb_userAppInfo[23]
    card_name = tb_userAppInfo[24]

    mysql_object_financecenter = MysqlHandler(mysql_user=Financecenter.MYSQL_USER.value,
                                              mysql_host=Financecenter.MYSQL_HOST.value,
                                              mysql_password=Financecenter.MYSQL_PASSWORD.value,
                                              mysql_db=Financecenter.MYSQL_DB.value)
    tb_user_info_dict = dict()
    tb_user_info_dict['user_id'] = userid
    tb_user_info_dict['user_name'] = card_name
    tb_user_info_dict['user_mobile'] = card_phone
    tb_user_info_dict['identity_card_no'] = card_idno
    tb_user_info_dict['weixin_open_id'] = open_id
    tb_user_info_dict['weixin_nick'] = wx_nickname
    tb_user_info_dict['create_time'] = create_time
    tb_user_info_dict['update_time'] = update_time
    tb_user_info_dict['integral'] = integral
    tb_user_info_dict['delete_flag'] = delete_flag
    tb_user_info_dict['finance_com_id'] = finance_com_id
    tb_user_info_table = "tb_user_info"
    tb_user_info_sql = mysql_object_financecenter.insert_str_generation(tb_user_info_table, tb_user_info_dict).encode(
        "utf-8")
    console.debug(tb_user_info_sql)
    try:
        mysql_object_financecenter.insert_mysql_data(tb_user_info_sql)
    except:
        console.exception("tb_user_info_sql插入错误！")

    #################################################################################################
    # 自动向tb_user_appl_info表插入数据
    #
    #
    #################################################################################################
    tb_user_appl_info_dict = dict()
    tb_user_appl_info_dict['user_appl_id'] = userid
    tb_user_appl_info_dict['user_id'] = tb_user_info_dict['user_id']
    tb_user_appl_info_dict['user_name'] = card_name
    tb_user_appl_info_dict['user_mobile'] = card_phone
    tb_user_appl_info_dict['identity_card_no'] = card_idno
    tb_user_appl_info_dict['company_detail_address'] = company_detail_address
    tb_user_appl_info_dict['bank_card_name'] = bank_card_name
    tb_user_appl_info_dict['bank_card_no'] = bank_card_no
    tb_user_appl_info_dict['contact_name'] = contact_name
    tb_user_appl_info_dict['contact_mobile'] = contact_mobile
    tb_user_appl_info_dict['contact_relation'] = contact_relation
    tb_user_appl_info_dict['delete_flag'] = delete_flag
    tb_user_appl_info_dict['create_time'] = create_time
    tb_user_appl_info_dict['update_time'] = update_time
    tb_user_appl_info_dict['pic_front'] = pic_front
    tb_user_appl_info_dict['pic_compress_front'] = pic_compress_front
    tb_user_appl_info_dict['pic_back'] = pic_back
    tb_user_appl_info_dict['pic_compress_back'] = pic_compress_back
    tb_user_appl_info_dict['pic_full'] = pic_full
    tb_user_appl_info_dict['pic_compress_full'] = pic_compress_full
    tb_user_appl_info_dict['province'] = province
    tb_user_appl_info_dict['city'] = city
    tb_user_appl_info_dict['area'] = area
    tb_user_appl_info_dict['company_name'] = company_name
    tb_user_appl_info_dict['contact_address_type'] = contact_address_type
    tb_user_appl_info_dict['user_education'] = user_education
    tb_user_appl_info_dict['marital_status'] = marital_status
    tb_user_appl_info_dict['company_size'] = company_size
    tb_user_appl_info_dict['census_reg_address'] = census_reg_address
    tb_user_appl_info_dict['month_income'] = month_income
    tb_user_appl_info_dict['company_work_years'] = company_work_years
    tb_user_appl_info_dict['bank_ref_mobile'] = card_phone
    tb_user_appl_info_table = "tb_user_appl_info"
    tb_user_appl_info_sql = mysql_object_financecenter.insert_str_generation(tb_user_appl_info_table,
                                                                             tb_user_appl_info_dict).encode("utf-8")
    console.debug(tb_user_appl_info_sql)
    mysql_object_financecenter.insert_mysql_data(tb_user_appl_info_sql)

    #########################################################################
    # 自动更新tb_cardno_openid表(其中只需要更新身份证号、userid)
    ########################################################################

    tb_cardno_openid_dict = dict()
    tb_cardno_openid_dict['id_no'] = card_idno
    tb_cardno_openid_dict['user_id'] = tb_user_info_dict['user_id']
    tb_cardno_openid_table = "tb_cardno_openid"
    condition_dict = {'card_no': card_no[0]}
    condition = MysqlHandler.condition_function(condition_dict)
    tb_cardno_openid_sql = mysql_object_financecenter.update_str_generation(tb_cardno_openid_table,
                                                                            tb_cardno_openid_dict, condition).encode(
        "utf-8")
    console.debug(tb_cardno_openid_sql)
    mysql_object_financecenter.update_mysql_data(tb_cardno_openid_sql)


def get_member_data(card_no):
    mysql_object_membercenter = MysqlHandler(mysql_user=Membercenter.MYSQL_USER.value,
                                             mysql_host=Membercenter.MYSQL_HOST.value,
                                             mysql_password=Membercenter.MYSQL_PASSWORD.value,
                                             mysql_db=Membercenter.MYSQL_DB.value)

    talbe = 'member_user_card'
    field_list = []
    field_list.append("card_name")
    field_list.append("card_phone")
    field_list.append("card_idno")
    field_list.append("open_id")
    condition_dict = dict(card_vipno=card_no)
    condition = mysql_object_membercenter.condition_function(condition_dict)
    membercenter_data_sql = mysql_object_membercenter.select_str_generation(table=talbe, field_list=field_list,
                                                                            condition=condition)
    result = mysql_object_membercenter.get_mysql_data(membercenter_data_sql)
    return result


def get_wxin_data(card_no):
    mysql_object_commcenter = MysqlHandler(mysql_user=Commcenter.MYSQL_USER.value,
                                           mysql_host=Commcenter.MYSQL_HOST.value,
                                           mysql_password=Commcenter.MYSQL_PASSWORD.value,
                                           mysql_db=Commcenter.MYSQL_DB_1.value)
    table = "tb_wx_userinfo"
    field_list = []
    field_list.append("wx_nickname")
    condition_dict = dict(wx_openid=get_member_data(card_no)[0][3])
    condition = mysql_object_commcenter.condition_function(condition_dict)
    wxnickname_sql = mysql_object_commcenter.select_str_generation(table=table, field_list=field_list,
                                                                   condition=condition)
    result = mysql_object_commcenter.get_mysql_data(wxnickname_sql)
    return result
