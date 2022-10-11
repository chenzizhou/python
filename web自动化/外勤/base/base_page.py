# 作者
# NATURE
# 日期
# 2022/10/11 21:12
# 功能
# 基础层：封装selenium原生方法
from time import sleep

from selenium import webdriver


class BasePage:
    def __init__(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.get("http://192.168.10.195:7799/")
        # 刷新当前界面，清除历史数据
        driver.refresh()
        sleep(2)
        # 设置窗口大小
        driver.set_window_size(1550, 848)
        sleep(1)
        driver.maximize_window()
        driver.implicitly_wait(20)

    def loc_element(self, loc):
        return driver.find_element(*loc)

    def send_keys(self, loc, value):
        return driver.find_element(*loc).send_keys(value)

    def click(self, loc):
        return driver.find_element(*loc).click()
