# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:42
 @Author  : Cristiano Ronalda
------------------------------
"""
import logging
import os
import time
from utill.getYamlData import get_config_yaml

data = get_config_yaml()
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'debug'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.mkdir(path)
    if not os.path.isfile(filename):
        fd = open(filename, 'w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Mylog.err_handler)
        logger.addHandler(Mylog.console)
    logger.addHandler(Mylog.handler)
    logger.addHandler(Mylog.console)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Mylog.err_handler)
    logger.removeHandler(Mylog.handler)


def get_current_time():
    return time.strftime(Mylog.date, time.localtime(time.time()))


class Mylog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/result/logs/output.log'
    err_file = path + '/result/logs/error.log'
    if data['runtest']['log_clear']:
        open(log_file, 'w').close()
        open(err_file, 'w').close()
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'
    handler = logging.FileHandler(log_file, encoding='utf-8')
    console = logging.StreamHandler()
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(log_msg):
        set_handler('debug')
        logging.debug('[DEBUG' + get_current_time() + ']' + log_msg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')


if __name__ == '__main__':
    Mylog.debug("This is debug message")
    Mylog.info("This is info message")
    Mylog.warning("This is warning message")
    Mylog.error("This is error")
    Mylog.critical("This is critical message")
