# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/11 21:41
# 功能：
from time import sleep

from selenium.webdriver.common.by import By

from web自动化.外勤.base.base_page import BasePage


class LoginPage(BasePage):
    # 页面元素
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, 'password')
    eye_loc = (By.XPATH, '//div[@class="ey-x-input-suffix"]')
    submit_loc = (By.XPATH, "//button[text()='登录']")
    info_loc=(By.XPATH,"//span[@class='arrow-icon']")

    def login(self, username='admin', password='123456'):
        self.send_keys(LoginPage.username_loc, username)
        sleep(1)
        self.send_keys(LoginPage.password_loc, password)
        sleep(2)
        self.click(LoginPage.eye_loc)
        sleep(1)
        self.click(LoginPage.submit_loc)
        sleep(2)

    def get_expect_element(self):
        return self.loc_element(LoginPage.info_loc)
        sleep(2)
