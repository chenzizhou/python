# 作者
# NATURE
# 日期
# 2022/11/7 16:41
# 功能
#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
ActionChains(driver).move_by_offset(500,200).click()