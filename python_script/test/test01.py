from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# EDGE_PATH=r'C:\Users\nature\AppData\Local\Programs\Python\Python39\msedgedriver.exe'
# driver=webdriver.Chrome()
# 启动edge浏览器 win10版本
##driver=webdriver.Edge(EDGE_PATH)
driver=webdriver.Edge()
# driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
locator=(By.CLASS_NAME,"submit")
WebDriverWait(driver,5).until(ec.visibility_of_element_located())
print(ec.title_contains('百度'))
sleep(2)
driver.close()