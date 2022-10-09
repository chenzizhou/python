from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 一、启动谷歌
# driver=webdriver.Chrome()
# 二、启动火狐
# driver=webdriver.firefox()
# 三、启动edge
# 1、启动edge浏览器 win10版本 需修改该驱动名称为MicrosoftWebDriver.exe
# 2、启动edge驱动时（msedgedriver.exe），需要加上绝对路径
EDGE_PATH=r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\msedgedriver.exe'
driver=webdriver.Edge(EDGE_PATH)
# driver=webdriver.Edge()
# driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
locator=(By.ID,"su")
WebDriverWait(driver,5).until(ec.visibility_of_element_located(locator))
print(ec.title_contains('百度'))
sleep(2)
driver.close()