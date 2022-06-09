# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:44
 @Author  : Cristiano Ronalda
------------------------------
"""
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_function():
    """
    yeild分割开始和结束
    在所有的用例开始前会执行yield前面的代码
    在所有的用例结束后会执行yield后面的代码
    :return:
    """
    print("执行conftest文件")
    yield
    print("执行conftest文件")


@pytest.fixture(scope="session", autouse=True)
def text_function(request):
    """
    # 测试用例模块test_home.py中
    class TestHome:
        def test_home1(self):
            self.data       ------注意看这里
    :param request:
    :return:
    """
    request.instance.data = '测试数据'  # 注意看这里
    request.instance.data[::-1]  # 注意看这里,该函数使用时需使用request.instance.data而不是直接data
