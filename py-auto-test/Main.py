# coding=utf-8
import pytest
from common.util.GetSms import GetSms
from common.util.IdentityDataCreater import *
from common.util.IdentityDataCreater import generator_const
import random
from common.util.logger import logger, console
from common.dbHandles.MysqlHandler import MysqlHandler
from common.util.TimeStamp import TimeStamp
import uuid
from data.base import Financecenter
from data.base import Commcenter
from data.base import Membercenter


# pytest.main("-s -v 'case/memberCenter/test_memberSignUp.py' --html=./logs/report.html")
# pytest.main("-s -v 'case/test_mysqlHandler.py' --html=./logs/report.html")
# pytest.main("-s -v 'case/memberCenter/ytdyc/test_memberSignUp.py'")
pytest.main("-s -v 'case/memberCenter/ytdyc/test_finance_generation.py' --html=./logs/report.html")
# pytest.main("-s -v 'case/memberCenter/oyjt/test_finance_generation.py' --html=./logs/report.html")

# shift = 1
# cellphone_num1 = 13120160425
# cellphone_num2 = 14120160323
# identify = gennerator_const(0 - random.random() * (10955 - 10225) - 10225)
# logger.info("短信获取开始!\n")
# print("短信获取开始!\n")
# if shift == 1:
#     logger.info(str(cellphone_num1)+"的会员卡短信验证码为:" + GetSms().get_sms_num_from_db(cellphone_num1))
#     logger.info(str(cellphone_num1)+"的消费金融短信验证码为:" + GetSms().get_sms_num_from_redis(cellphone_num1))
#     console.info(str(cellphone_num1)+"的会员卡短信验证码为:" + GetSms().get_sms_num_from_db(cellphone_num1))
#     console.info(str(cellphone_num1)+"的消费金融短信验证码为:" + GetSms().get_sms_num_from_redis(cellphone_num1))
# else:
#     logger.info(str(cellphone_num1)+"的会员卡短信验证码为:" + GetSms().get_sms_num_from_db(cellphone_num1))
#     logger.info(str(cellphone_num2)+"的消费金融短信验证码为:" + GetSms().get_sms_num_from_redis(cellphone_num2))
#     console.info(str(cellphone_num1)+"的会员卡短信验证码为:" + GetSms().get_sms_num_from_db(cellphone_num1))
#     console.info(str(cellphone_num2)+"的消费金融短信验证码为:" + GetSms().get_sms_num_from_redis(cellphone_num2))
# logger.info("身份证号为：" + identify + "\n")
# logger.info("短信获取结束!")
# console.info("身份证号为：" + identify + "\n")
# console.info("短信获取结束!")
