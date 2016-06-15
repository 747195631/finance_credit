# -*- coding:utf-8 -*-

from fixtures.mobileFixture import ytdyc_mobile_fixture_selenium
import pytest
from data.base import *
from lib.MemberSignUp import MemberSignUp


# @pytest.mark.parametrize("test_data,result",
#                          [([15120160320, '测试一', -10590], '余额'), ([15220160310, '测试一', -10590], '余额')])
@pytest.mark.parametrize("test_data,result",
                         [([15120160369, '福利八', -10590], '余额')])
def test_ytdycmember_sign_up(ytdyc_mobile_fixture_selenium, test_data, result):
    result_dict = MemberSignUp.member_sign_up(ytdyc_mobile_fixture_selenium, Ytdyc.YTDYC_MEMBER_URL.value, test_data)
    veri_point1 = result_dict['veri_point']
    assert veri_point1 == result
    # assert veri_point1 == "余额"
