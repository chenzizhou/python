from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
url='http://www.baidu.com'
driver.get(url) 
link=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(link).perform()
sleep(2)
driver.find_element_by_link_text('搜索设置').click()
sleep(2)
driver.find_element_by_class_name('prefpanelgo').click()
sleep(2)
##接受警告框
driver.switch_to_alert().accept()
driver.quit()
