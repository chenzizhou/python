# 作者
# NATURE
# 日期
# 2022/10/13 16:12
# 功能
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://192.168.10.195:7799/")
username='admin'
password='123456'
driver.find_element_by_name("username").send_keys(username)
sleep(3)
driver.find_element_by_name('password').send_keys(password)
sleep(3)
driver.find_element_by_name('password').send_keys(Keys.ENTER)
sleep(3)
print(WebDriverWait(driver,10,1).until(expected_conditions.title_is('HopeMap外勤管理平台')))
sleep(3)
