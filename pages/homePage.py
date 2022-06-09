# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/9 下午3:24
 @Author  : Cristiano Ronalda
------------------------------
"""
import time
from pages.basePage import BasePage
from pages.home_patient_flow_page import HomePatientFlowPage
from pages.home_record_page import HomeCaseRecordPage
from pages.patient_center_page import PatientCenterPage
from pages.search_medical import SearchMedicalPage


class HomePage(BasePage):
    """
    主页内所有元素和操作
    """
    search_medical = '//*[@text="搜索疾病/药品/症状/文章"]'
    my_application = '***'
    patient_center = '****'

    @property
    def text_home_dict(self):
        """
        获取所有文案信息
        :return:
        """
        home_text_dict = {}
        # 向下滑动
        self.swipe_up()
        time.sleep(1)
        # 主页搜索框
        home_text_dict['元素1'] = self.get_text(self.search_medical)
        home_text_dict["元素2"] = self.get_application_text_list("*****")
        home_text_dict['元素3'] = self.get_text('*****')
        return home_text_dict

    @property
    def enter_home_case_record(self):
        """
        点击按钮进入下一个页面
        :return:
        """
        return HomeCaseRecordPage(self.driver)

    def enter_which_department(self, department_name):
        """
        选择页面
        :return:
        """
        department_list = self.get_departments_list
        num = department_list.index(department_name)
        self.click(department_list[num])

    def reselect_department(self, department_name):
        """
        选择后返回当前页面，所以return self
        :return:
        """
        self.enter_department_select()
        self.enter_which_department(department_name)
        return self


if __name__ == '__main__':
    k = HomePage('qwe')
    print(HomePage('qwe').__class__.__name__)

    # print(os.path.abspath(__file__))
