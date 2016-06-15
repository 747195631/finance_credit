# -*- coding:utf-8 -*-
###########################################
# File: mobileFixture.py
# Desc: 初始化方法
# Author: zhangyufeng
# History: 2016/03/02 zhangyufeng 新建
###########################################
import pytest
from data.base import *


@pytest.fixture()
def ytdyc_mobile_fixture_selenium():
    browser = ytdyc_mobile_get_auth_selenium()
    return browser


@pytest.fixture()
def ytdyc_mobile_fixture_protocol():
    opener = ytdyc_mobile_get_auth_protocol()
    return opener
