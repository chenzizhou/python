from selenium import webdriver
import os
from time import sleep
co=webdriver.ChromeOptions()
prefs={"download.default_directory":r"E:\下载"}
co.add_experimental_option('prefs',prefs)
driver=webdriver.Chrome(options=co)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_css_selector('#files-tab').click()
sleep(2)
driver.find_element_by_css_selector('#files > table > tbody > tr:nth-child(1) > th > a').click()
sleep(30)
driver.quit()
