# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:48
 @Author  : Cristiano Ronalda
------------------------------
"""

import os
import shutil
import pytest

from utill.log import Mylog

REPORT_TMP_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result/reports/tmp/'))

if __name__ == '__main__':

    Mylog.info('======================================start======================================')
    if os.path.exists(REPORT_TMP_PATH):
        shutil.rmtree(REPORT_TMP_PATH)
    # args = ['-s', '-v','--reruns', '3', '-m=test', f'--alluredir={REPORT_TMP_PATH}']
    args = ['-s', '-v', f'--alluredir={REPORT_TMP_PATH}']
    Mylog.info(f'argsi为:{str(args)}')
    pytest.main(args)
    os.system("allure generate ./result/reports/tmp/ -o ./result/reports/html --clean")
    Mylog.info('=======================================end=======================================')