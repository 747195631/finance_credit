# -*- coding:utf-8 -*-
from selenium import webdriver
from enum import Enum
from common.util.HttpUrlConnection import HttpUrlConnection

class Ytdyc(Enum):
    PROTOCOL = "http"
    HOST_ENVIRONMENT = "test2.ishop-city.com"
    PATH = "/mockPlatform/user/login"
    OPENID = "oU6MHj2xjqECLquKIxmL6rgZJ_6s"
    MCODE = "suolong"
    TEST_URL = r"http://test2.ishop-city.com/memc/center/dyc/login.do?mcode=suolong"
    YTDYC_MEMBER_URL = "http://test2.ishop-city.com/memc/center/dyc/login.do?mcode=suolong"

class Membercenter(Enum):
    MYSQL_USER = "demo"
    MYSQL_HOST = "192.168.1.29"
    MYSQL_PORT = 3306
    MYSQL_PASSWORD = "vSQF%bURaH64iwmw"
    # MYSQL_USER = "feng"
    # MYSQL_HOST = "localhost"
    # MYSQL_PORT = 3306
    # MYSQL_PASSWORD = "feng"
    MYSQL_DB = "memberCenter"


class Commcenter(Enum):
    MYSQL_USER = "demo"
    MYSQL_HOST = "192.168.1.29"
    MYSQL_PORT = 3306
    MYSQL_PASSWORD = "vSQF%bURaH64iwmw"
    # MYSQL_USER = "feng"
    # MYSQL_HOST = "localhost"
    # MYSQL_PORT = 3306
    # MYSQL_PASSWORD = "feng"
    MYSQL_DB_3 = "comm_center_sharding_3"
    MYSQL_DB_1 = "comm_center_sharding_1"


class Financecenter(Enum):
    MYSQL_USER = "demo"
    MYSQL_HOST = "192.168.1.29"
    MYSQL_PORT = 3306
    MYSQL_PASSWORD = "vSQF%bURaH64iwmw"
    # MYSQL_USER = "feng"
    # MYSQL_HOST = "localhost"
    # MYSQL_PORT = 3306
    # MYSQL_PASSWORD = "feng"
    MYSQL_DB = "financecenter"

# 使用selenium拿cookie
def ytdyc_mobile_get_auth_selenium():
    browser = webdriver.Chrome()
    url = Ytdyc.PROTOCOL.value + "://" + Ytdyc.HOST_ENVIRONMENT.value + Ytdyc.PATH.value + r"?openId=" + \
          Ytdyc.OPENID.value + r"&mcode=" + Ytdyc.MCODE.value
    browser.get(url)
    return browser

# 使用请求拿cookie
def ytdyc_mobile_get_auth_protocol():
    url = Ytdyc.PROTOCOL.value + "://" + Ytdyc.HOST_ENVIRONMENT.value + Ytdyc.PATH.value + r"?openId=" +\
          Ytdyc.OPENID.value + r"&mcode=" + Ytdyc.MCODE.value
    http_object = HttpUrlConnection(get_cookie_url=url)
    session_object = http_object.get_session_object()
    return session_object

