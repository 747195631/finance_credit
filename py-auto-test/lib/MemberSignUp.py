# -*- coding:utf-8 -*-
import time
from common.util.logger import logger
from common.util.GetSms import *
from common.util.IdentityDataCreater import *

sms_object = GetSms()


class MemberSignUp(object):
    def __init__(self):
        pass

    @staticmethod
    def member_sign_up(browser_param, url, test_data):
        try:
            result_dict = dict()
            browser = browser_param
            browser.get(url)
            try:
                time.sleep(1)
                browser.find_element_by_xpath("//span[@class='li-left']")
                time.sleep(1)
                browser.find_element_by_xpath("//li[@data-url='../dyc/member_perfect_info.html']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//img[@data-url='../dycnew/member-set.html']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//button[@class='log_out']").click()
                time.sleep(1)
            except:
                logger.debug("未绑卡")
            browser.find_element_by_id("memberPhone").send_keys(test_data[0])
            browser.find_element_by_xpath("//a[@class='btn btn_verify verify_code']").click()
            time.sleep(2)
            sms_num = sms_object.get_sms_num_from_db(test_data[0])
            browser.find_element_by_id("inp_verify_code").send_keys(sms_num)
            browser.find_element_by_id("btn_login_success").click()
            time.sleep(3)
            try:
                browser.find_element_by_xpath("//li[@onclick='closeErrorInfoThree()']").click()
            except:
                logger.debug("已注册")
                result_dict["veri_point"] = None
                result_dict["sms_num"] = None
                return result_dict
            time.sleep(2)
            browser.find_element_by_id("memberName").send_keys(test_data[1])
            # 默认当前时间大约推30年
            memberIdNo = generator_const(test_data[2])
            browser.find_element_by_id("memberIdNo").send_keys(memberIdNo)
            # 推荐人手机号，非必填项
            # browser.find_element_by_id("referrerPhone").send_keys("phone_num")
            browser.find_element_by_xpath("//a[@class='btn btn_register']").click()
            time.sleep(2)
            browser.find_element_by_xpath("//li/a[@id='confirmBtn']").click()
            time.sleep(3)
            veri_point = browser.find_element_by_xpath("//div[@class='Balance-left']").text
            result_dict["veri_point"] = veri_point
            result_dict["sms_num"] = sms_num
            return result_dict
        except:
            logger.exception("发现错误")

    def __call__(self, *args, **kwargs):
        pass
