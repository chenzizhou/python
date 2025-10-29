from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class RegisterPage(BasePage):

    def register(self, username, password, pwd1):
        login_url = 'http://127.0.0.1:8000/user/login/'
        # 打开登录页面
        self.driver.get(login_url)
        self.click(loc=(By.LINK_TEXT, '前去注册'))
        # 找到用户名和密码输入框
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        pwd1_field = self.driver.find_element(By.NAME, "pwd1")

        # 输入用户名和密码
        username_field.send_keys(username)
        password_field.send_keys(password)
        pwd1_field.send_keys(password)

        # 提交登录表单
        password_field.send_keys(Keys.RETURN)

        # 等待页面加载
        sleep(5)
        print(self.driver.page_source)  # 打印页面源码，方便调试


