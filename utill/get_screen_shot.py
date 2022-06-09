# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:38
 @Author  : Cristiano Ronalda
------------------------------
"""
import os
import time
import allure

screenshot_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../result/screenshots/'))


def get_screen_file(driver, text):
    """
    获取屏幕截图
    :param driver:
    :param text:
    :return:
    """
    filename = '\\' + time.strftime('%Y%m%d%H%M') + text + '.png'
    driver.get_screenshot_as_file(screenshot_path + filename)
    return screenshot_path + filename


def del_png_files():
    """
    删除屏幕截图
    :return:
    """
    file_list = []
    for dir, path, files in os.walk(screenshot_path):
        if len(files) > 0:
            for file in files:
                if file.endswith('.png'):
                    file_list.append(os.path.join(dir, file))
    if len(file_list) > 0:
        for file in file_list:
            os.remove(file)


def allure_screen(driver, s):
    if s is not None:
        allure.attach(driver.get_screenshot_as_png(), s, allure.attachment_type.PNG)


if __name__ == '__main__':
    # print(sys._getframe().f_code.co_name)
    del_png_files()
