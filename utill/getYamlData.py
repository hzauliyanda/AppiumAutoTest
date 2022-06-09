# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:14
 @Author  : Cristiano Ronalda
------------------------------
"""
import os
import yaml


def get_config_yaml():
    """
    获取yaml文件数据
    :return:
    """
    yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/config.yaml"))
    with open(yaml_path, "r", encoding="utf-8") as fp:
        data = yaml.load(fp, Loader=yaml.Loader)
    return data


if __name__ == '__main__':
    pass
