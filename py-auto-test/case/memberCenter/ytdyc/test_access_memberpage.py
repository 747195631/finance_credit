# -*- coding:utf-8 -*-
from fixtures.mobileFixture import ytdyc_mobile_fixture_selenium
from fixtures.mobileFixture import ytdyc_mobile_fixture_protocol
from data.base import *
from common.util.logger import logger
import pytest
import time


# 使用selenium的方法
def test_access_success_selenium(ytdyc_mobile_fixture_selenium):
    browser = ytdyc_mobile_fixture_selenium
    browser.get(Ytdyc.TEST_URL.value)
    time.sleep(3)


# 使用请求的方法
def test_access_success_protocol(ytdyc_mobile_fixture_protocol):
    opener = ytdyc_mobile_fixture_protocol
    html = opener.open(Ytdyc.TEST_URL.value)
    logger.debug(html.read())
    time.sleep(3)
