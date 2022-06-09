# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:30
 @Author  : Cristiano Ronalda
------------------------------
"""
import traceback
import allure
import pytest
from hamcrest import assert_that, has_item, equal_to
import sys
from pages.init_start import InitStartApp
from utill.getScreenShot import get_screen_file


@pytest.mark.test
@allure.feature("发现页")
class TestHome:

    @pytest.mark.text
    @allure.title("页面文本检查")
    def test_home_texts(self):
        self.log.info("============>>>【%s】-【%s】用例开始执行:" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        try:
            self.log.info("============>>>正在启动app并登录")
            text_dict = InitStartApp(self.driver).type_skipwelcome.submit_login().reselect_department(
                self.department).text_home_dict
            self.log.info("============>>>已获取科室【%s】主页的所有文案：%s" % (self.department, text_dict))
            allure.attach(str(text_dict), "所有文本")
            assert_that(text_dict['流动情况'], equal_to("本月出院"))
            self.log.info("============>>>【%s】-【%s】用例执行结束:" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        except Exception as e:
            file_path = get_screen_file(self.driver, self.__class__.__name__ + '-' + sys._getframe().f_code.co_name)
            self.log.error(
                "============>>>【%s】-【%s】用例执行失败，截图已保存至【%s】，报错日志：【%s】" % (
                    self.__class__.__name__, sys._getframe().f_code.co_name, file_path, str(e)))
            allure.attach(str(e), "失败原因")
            with open(file_path, 'rb') as p:
                file = p.read()
                allure.attach(file, "失败截图", allure.attachment_type.PNG)
            traceback.print_exc(e)

if __name__ == '__main__':
    pass
