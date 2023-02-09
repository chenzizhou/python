#coding: utf8
# 作者：NATURE
# 开发时间：2022/10/11 21:41
# 功能：
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from web_automation.waiqin.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # 页面元素
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, 'password')
    eye_loc = (By.XPATH, '//div[@class="ey-x-input-suffix"]')
    submit_loc = (By.XPATH, "//button[text()='登录']")
    info_loc=(By.XPATH,"//span[@class='arrow-icon']")
    bd_loc = (By.XPATH, r"// div[ @ title = '百度']")
    def login(self, url,username='admin', password='123456'):
        '''测试登录'''
        print('进入登录界面')
        self.get(url)
        self.send_keys(LoginPage.username_loc, username)
        sleep(1)
        self.send_keys(LoginPage.password_loc, password)
        sleep(1)
        self.click(LoginPage.eye_loc)
        sleep(1)
        self.click(LoginPage.submit_loc)
        # 显示等待
        WebDriverWait(self.get_driver(), 5, 20).until(EC.visibility_of_element_located(self.bd_loc))

    def get_expect_element(self):
        return self.loc_element(LoginPage.info_loc)
        sleep(2)
