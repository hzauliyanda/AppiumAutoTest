# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:38
 @Author  : Cristiano Ronalda
------------------------------
"""
import re


def get_text(str):
    """
    匹配出全部汉字，返回匹配结果
    :param str:
    :return:
    """
    try:
        ch_list = re.findall('[\u4e00-\u9fa5]', str)
        return ''.join(ch_list)
    except Exception:
        print('未匹配到汉字')


def is_Chinese(str):
    """
    判断是否全部是汉字，或以汉字开头，或以汉字结尾
    :param str:
    :return:
    """
    try:
        str_list = re.findall('[\u4e00-\u9fa5]', str)
        if len(str_list) == len(str):
            return True
        elif len(str_list) < len(str) and re.match('^[\u4e00-\u9fa5]+', str):
            return True
        elif len(str_list) < len(str) and re.match('.+[\u4e00-\u9fa5]$', str):
            return True
        else:
            return False
    except Exception as e:
        print('未匹配到汉字')


def del_space(str):
    """
    删除文本中的所有空格
    :param str:
    :return:
    """
    try:
        for i in str:
            if i == " ":
                str = str.replace(i, '')
        return str
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(get_text('32     小李'))
