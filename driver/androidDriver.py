# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:13
 @Author  : Cristiano Ronalda
------------------------------
"""

# -*- coding:utf-8 "-*-
import os
from appium import webdriver
from utill.getYamlData import get_config_yaml


def androidDriver():
    """
    driver启动
    :return:
    """
    # 获取yaml文件中的数据
    capsbilities_data = get_config_yaml()
    caps = {}
    caps["platformName"] = capsbilities_data['capsbilities']["platformName"]
    caps["platformVersion"] = str(capsbilities_data['capsbilities']["platformVersion"])
    caps["deviceName"] = capsbilities_data['capsbilities']["deviceName"]
    caps["appPackage"] = capsbilities_data['capsbilities']["appPackage"]
    caps["appActivity"] = capsbilities_data['capsbilities']["appActivity"]
    caps['automationName'] = capsbilities_data['capsbilities']["automationName"]
    caps["skipServerInstallation"] = capsbilities_data['capsbilities']["skipServerInstallation"]
    caps["autoGrantPermissions"] = capsbilities_data['capsbilities']["autoGrantPermissions"]

    driver = webdriver.Remote(
        "http://" + capsbilities_data['appiumServer']["ip"] + ":" + str(
            capsbilities_data['appiumServer']["port"]) + "/wd/hub", caps)
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    # appium -a 127.0.0.1 -p 4723 --session-override
    # uiautomatorviewer
    # androidDriver()
    pass
