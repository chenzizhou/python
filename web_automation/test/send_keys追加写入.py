# 作者
# NATURE
# 日期
# 2022/10/13 11:52
# 功能
#
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://192.168.10.195:7799/")
username='admin'
password='123456'
driver.find_element_by_name("username").send_keys(username)
sleep(5)
driver.find_element_by_name('password').send_keys(password)
sleep(5)
# 追加添加值adminadmin
driver.find_element_by_name("username").send_keys(username)
sleep(5)