# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/11 21:41
# 功能：
from time import sleep

from selenium.webdriver.common.by import By

from web_automation.外勤.base.base_page import BasePage
from web_automation.外勤.util.xlsx_util import XlsxUtil


class LoginPage(BasePage):
    # 页面元素
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, 'password')
    eye_loc = (By.XPATH, '//div[@class="ey-x-input-suffix"]')
    submit_loc = (By.XPATH, "//button[text()='登录']")
    info_loc = (By.XPATH, "//span[@class='arrow-icon']")

    def login(self, username='admin', password='123456'):
        '''测试登录'''
        # self.send_keys(LoginPage.username_loc, username)
        # sleep(1)
        # self.send_keys(LoginPage.password_loc, password)
        # sleep(1)
        # self.click(LoginPage.eye_loc)
        # sleep(1)
        # self.click(LoginPage.submit_loc)
        # sleep(4)
        file = '../data/登录界面.xlsx'
        x=XlsxUtil()
        xlsx_data = x.read_xlsx(file)
        print(xlsx_data)
        self.find_element_by_xlsx(xlsx_data, 'username_loc').send_keys(username)
        sleep(1)
        self.find_element_by_xlsx(xlsx_data, 'password_loc').send_keys(password)
        sleep(1)
        self.find_element_by_xlsx(xlsx_data, 'eye_loc').click()
        sleep(1)
        self.find_element_by_xlsx(xlsx_data, 'submit_loc').click()
        sleep(3)

    def get_expect_element(self):
        return self.loc_element(LoginPage.info_loc)
        sleep(2)
