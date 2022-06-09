# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:33
 @Author  : Cristiano Ronalda
------------------------------
"""
import os
from appium.webdriver.appium_service import AppiumService
from utill.getYamlData import get_config_yaml
from utill.shell import sh


class AppServer:
    """
    封装appServer
    """
    def __init__(self):
        self.port_data = get_config_yaml()['appiumServer']['port']
        self.ip_data = get_config_yaml()['appiumServer']['ip']
        self.service = AppiumService()

    def start_appium(self):
        """
        启动appium
        :return:
        """
        log_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'result/logs/appium.log'))
        self.service.start(
            args=['--address', '{}'.format(self.ip_data), '-p', '{}'.format(self.port_data), '--session-override'],
            timeout_ms=2000)

    def check_appium_port(self, port):
        """
        检查端口是否被占用
        :param port:
        :return:
        """
        cmd = "netstat -ano | findstr %s" % port
        cmd_result = sh(cmd)
        if str(port) and "LISTENING" in cmd_result:
            i = cmd_result.index("LISTENING")
            start = i + len("LISTENING") + 7
            end = cmd_result.index('\n')
            pid = cmd_result[start:end]
            return pid
        else:
            return None

    def kill_server(self, pid):
        """
        杀掉进程
        :param pid:
        :return:
        """
        cmd_kill = "taskkill -f -pid %s" % pid
        sh(cmd_kill)

    def stop_appium(self):
        """
        停止appium
        :return:
        """
        self.service.stop()


if __name__ == '__main__':
    app = AppServer()
    # app.start_appium()
    print(app.check_appium_port(4723))
