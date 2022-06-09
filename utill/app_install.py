# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:30
 @Author  : Cristiano Ronalda
------------------------------
"""
import sys
import time
import os
from threading import Thread
from utill.log import Mylog
from utill.getYamlData import get_config_yaml

mylog = Mylog()
capsbilities_data = get_config_yaml()
app_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_list = []
for abs1, dir, files in os.walk(app_path):
    if abs1 == app_path:
        for file in files:
            if file.endswith('.apk') and capsbilities_data['runtest']['enviroment'] in file.lower():
                app_file2 = os.path.join(abs1, file)
                file_list.append(app_file2)
if len(file_list) == 1:
    app_file = file_list[0]
    mylog.info("============>>>已找到待安装的apk:【%s】..." % app_file)
else:
    mylog.info(
        "============>>>未找到待安装的apk，请确保apk放在正确路径下:【%s】,且正确命名，测试包命名需包含test或TEST，生产包命名需包含release或RELEASE..." % app_path)
    sys.exit(-1)


def installApp():
    """
    安装app命令
    :return:
    """
    os.popen("adb install %s" % app_file)


def inputEvent1():
    """
    点击屏幕某个固定位置1
    :return:
    """
    time.sleep(3)
    os.popen("adb shell input tap 793 2211")


def inputEvent2():
    """
    点击屏幕某个固定位置2
    :return:
    """
    time.sleep(5)
    os.popen("adb shell input tap 540 2029")


def start_adb():
    """
    查看所有连接设备信息
    :return:
    """
    os.popen('adb devices')


def adb_pm_list():
    """
    查看所有包
    :return:
    """
    result = os.popen('adb shell pm list packages | find "appPackage"').read()
    return result


def check_out():
    """
    检查app是否运行
    :return:
    """
    start_adb()
    time.sleep(3)
    result = adb_pm_list()
    return result


def uninstall_app():
    """
    卸载app
    :return:
    """
    os.popen('adb uninstall "com.iflytek.medicalassistant"')


def install():
    """
    安装app
    :return:
    """
    t1 = Thread(target=installApp)
    t2 = Thread(target=inputEvent1)
    t3 = Thread(target=inputEvent2)
    t1.start()
    time.sleep(3)
    t2.start()
    time.sleep(3)
    t3.start()


if __name__ == '__main__':
    pass
