from selenium import webdriver
from selenium.webdriver import ActionChains
import os
driver=webdriver.Chrome()
driver.maximize_window()
file_path='file:///'+os.path.abspath('upfile.html')
print(file_path)
##file=r'E:\\python_script\upfile.html'
driver.get(file_path)
driver.implicitly_wait(10)
try:
    ActionChains(driver).click(driver.find_element_by_xpath("/html/body/div/div/input")).perform()
except Exception as e:
    print(e)
os.system(r'start E:\autoit_script\upfile.exe')


