# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:15
 @Author  : Cristiano Ronalda
------------------------------
"""

import subprocess


def sh(command):
    """
    执行shell命令，output为命令行的结果
    :param command: 输入命令
    :return: 执行结果
    """
    output, errors = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT).communicate()
    output = output.decode("utf-8")
    return output


if __name__ == '__main__':
    sh("netstat -ano | findstr 4723")
