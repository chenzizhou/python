# 作者
# NATURE
# 日期
# 2022/10/18 14:35
# 功能
#
from time import sleep

from selenium import webdriver
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
sleep(2)
driver.find_element_by_id("kw").send_keys("remote")
sleep(2)
driver.find_element_by_id("su").click()
sleep(5)
driver.quit()