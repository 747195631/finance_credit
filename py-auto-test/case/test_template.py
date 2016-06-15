# -*- coding:utf-8 -*-

#########################################################
#
# 在文件目录下命令行执行py.test可直接执行所有带test开头的文件的测试,执行py.case -h可看帮助
# 执行py.case -k "first"只取params中的0,执行py.case -s则打印程序中的print()
# 如果需要打日志则直接配置logging进行日志输出即可
#
#########################################################
import sys
import pytest
from common.util.logger import logger

sys.path.append("../")
logger.debug("测试")


# 被测函数
def tmp_func1(param1):
    result = param1 + 1
    return result


#########################################################
#
# @pytest.fixture(scope=function,params=None,autouse=False,ids=None)装饰器
# scope是范围，有四个选项function  (default),  class ,  module ,  session，一般选择默认即可。
# params。参数，程序中通过“形参.param”获得并使用
# autouse是配置项，如果不打算把装饰后的函数放到测试用例函数的形参中，这个值设置为True，则所有的函数都会引用。实际使用中
# 大多需要把装饰后的函数放到测试用例函数的形参中，故一般使用默认值False。
# ids是params对应的key，命令行执行测试时可以指定执行，使用-k。
#
#########################################################
@pytest.fixture(params=[0, 1], ids=["first", "second"])
def tmp_fixture(request):
    return request.param


# 带teardown的fixture
@pytest.fixture()
def tmp_fixture_with_last(request):
    print("开始了！")

    # teardown方法
    def last_run():
        print("结束了！")

    # teardown
    request.addfinalizer(last_run)
    return 1


# 测试用例函数
def test_tmp_func1():
    logger.debug("测试1")
    print("测试2")
    assert tmp_func1(0) == 1


def test_tmp_func2(tmp_fixture):
    assert tmp_func1(tmp_fixture) == 1


def test_tmp_func3(tmp_fixture_with_last):
    print("进行中！")
    assert tmp_func1(tmp_fixture_with_last) == 1


@pytest.mark.parametrize("input_data,expected", [(1, 2), (2, 2)])
def test_tmp_func4(input_data, expected):
    assert tmp_func1(input_data) == expected

#########################################################
#
# 如何不想使用命令执行测试而是想在Run.py中直接执行
# 则在Run.py中添加可执行的pytest.lib()
# pytest.lib()中不添加参数则按默认配置运行项目中所有的符合条件的文件
# 建议使用pytest.lib("-s -v")
#
#########################################################
