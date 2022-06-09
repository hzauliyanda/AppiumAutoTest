# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:19
 @Author  : Cristiano Ronalda
------------------------------
"""
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from utill.getText import is_Chinese


class BasePage:
    """
    基础方法封装
    """
    Toast_windows = "//*[@class='android.widget.Toast']"

    def __init__(self, driver):
        self.driver = driver

    # 元素定位方式封装，根据输入的信息判断
    def by_text(self, text):
        """
        根据输入的文本确定定位方式
        :param text:
        :return:
        """
        if '//*' in text:
            loc = (By.XPATH, text)
            return loc
        elif 'com.iflytek.medicalassistant:id/' in text:
            loc = (By.ID, text)
            return loc
        elif 'android.' in text and '//*' not in text:
            loc = (By.CLASS_NAME, text)
            return loc
        elif is_Chinese(text):
            loc = (By.XPATH, '//*[@text="%s"]' % text)
            return loc

    def find(self, loc, timeout=5):
        """
        定位单个元素
        :param loc:
        :param timeout:
        :return:
        """
        return self.driver.find_element(*loc)

    def finds(self, loc, timeout=5):
        """
        定位多个元素，返回列表
        :param loc:
        :param timeout:
        :return:
        """
        return self.driver.find_elements(*loc)

    def click(self, text):
        """
        单击元素
        :param text:
        :return:
        """
        self.find(self.by_text(text)).click()

    def click_lower_half(self, text):
        """
        点击元素范围的下半部分
        :param text:
        :return:
        """
        select_location = self.get_element_location(text)
        select_size = self.get_element_size(text)
        x = int((select_location['x'] + select_size['width']) / 2)
        y = int((select_location['y'] + select_size['height']) * 3 / 4)
        time.sleep(1)
        TouchAction(self.driver).tap(self.find(self.by_text(text)), x, y).perform()
        time.sleep(2)

    def clear(self, text):
        """
        清空输入框
        :param text:
        :return:
        """
        self.find(self.by_text(text)).clear()

    def send_keys(self, text, content):
        """
        输入文本信息
        :param text:
        :param content:
        :return:
        """
        self.find(self.by_text(text)).send_keys(content)

    def get_element_size(self, text):
        """
        返回元素的size
        :param text:
        :return:
        """
        return self.find(self.by_text(text)).size

    def get_element_location(self, text):
        """
        返回元素的位置坐标
        :param text:
        :return:
        """
        return self.find(self.by_text(text)).location

    def exists(self, text):
        """
        找到多个元素，返回list
        :param text:
        :return:
        """
        return self.finds(self.by_text(text))

    def get_text(self, text):
        """
        获取文本信息
        :param text:
        :return:
        """
        return self.find(self.by_text(text)).text

    def get_toast_text(self):
        """
        获取系统弹窗的文字
        :return:
        """
        return self.get_text(self.Toast_windows)

    def get_text_list(self, text):
        """
        获取多个元素的文字，返回列表
        :param text:
        :return:
        """
        return [i.text for i in self.finds(self.by_text(text))]

    def get_application_text_list(self, text):
        """
        获取主页的应用模块的文字，返回列表
        :param text:
        :return:
        """
        app_page_list = []
        while True:
            middle_list = self.get_text_list(text)
            try:
                last_one = app_page_list[-1]
            except IndexError:
                last_one = "随便取值"
            try:
                last_two = middle_list[-1]
            except IndexError:
                break
            if last_one != last_two:
                app_page_list.extend(middle_list)
            elif last_one == last_two:
                break
            self.application_swipe_left()
            middle_list.clear()
        return app_page_list

    def swipe_back(self):
        """
        左滑退出，从屏幕边缘滑到另一侧边缘
        :return:
        """
        time.sleep(0.5)
        TouchAction(self.driver).press(x=41, y=1187).move_to(x=942, y=1182).release().perform()
        time.sleep(0.5)

    def application_swipe_left(self):
        """
        滑动应用模块
        :return:
        """
        time.sleep(0.5)
        # 页面下滑后的位置
        self.driver.swipe(941, 619, 142, 619)
        # TouchAction(driver).press(x=892, y=619).move_to(x=208, y=624).release().perform()      # 原来位置
        time.sleep(1)

    def tab_swipe_left(self):
        """
        详情页的顶部tab左滑
        :return:
        """
        time.sleep(0.5)
        self.driver.swipe(986, 283, 180, 281)
        time.sleep(1)

    def tab_swipe_right(self):
        """
        详情页的顶部tab右滑
        :return:
        """
        time.sleep(0.5)
        self.driver.swipe(73, 283, 984, 283)
        time.sleep(1)

    def swipe_up(self):
        """
        详情页的顶部tab上滑
        :return:
        """
        time.sleep(0.5)
        self.driver.swipe(492, 2074, 497, 545)
        time.sleep(0.5)

    def swipe_down(self):
        """
        详情页的顶部tab下滑
        :return:
        """
        time.sleep(0.5)
        self.driver.swipe(497, 545, 492, 2074)
        time.sleep(0.5)

    def get_size(self):
        """
        获取手机屏幕尺寸
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y


if __name__ == '__main__':
    pass
