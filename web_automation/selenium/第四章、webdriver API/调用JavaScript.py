import time
from selenium import webdriver

from time import sleep

from selenium.webdriver.common.by import By

#访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
#搜索
driver.find_element(By.ID,"kw").send_keys("selenium")
driver.find_element(By.ID,"su").click()
sleep(2)
#通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,1000);"
driver.execute_script(js)
sleep (3)
