# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:35
 @Author  : Cristiano Ronalda
------------------------------
"""
import os
import xlrd


class OperationExcel:
    """
    读取excel数据
    """
    def get_data(self, filename, sheet_name):
        """
        获取指定文件和sheet的数据
        :param filename:
        :param sheet_name:
        :return:
        """
        self.book = xlrd.open_workbook(filename)
        self.sheet = self.book.sheet_by_name(sheet_name)
        self.nrows = self.sheet.nrows
        self.ncols = self.sheet.ncols
        nrows_list = []
        for row in range(self.nrows):
            ncols_list = []
            for col in range(self.ncols):
                # 0 是空   1是str  2是数字
                ctype = self.sheet.cell(row, col).ctype
                col_data = self.sheet.cell_value(row, col)
                if ctype == 0:
                    ncols_list.append(col_data)
                elif ctype == 1:
                    ncols_list.append(col_data)
                elif ctype == 2:
                    ncols_list.append(str(int(col_data)))
                # elif ctype ==3:
            nrows_list.append(tuple(ncols_list))
        return nrows_list

    def get_case_data(self, text):
        """
        获取某个sheet下的数据
        :param text:
        :return:
        """
        user_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/alldata.xlsx'))
        user_data = self.get_data(user_path, text)
        user_data.remove(user_data[0])
        return user_data


if __name__ == '__main__':
    print(OperationExcel().get_case_data('登录'))
