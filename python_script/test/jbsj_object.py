from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
url='http://www.baidu.com'
driver.get(url)

driver.find_element_by_id('kw').send_keys('哈登酱')

sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.SPACE)

sleep(2)

driver.find_element_by_id('kw').send_keys('吸毒')

sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')

driver.find_element_by_id('kw').send_keys(Keys.ENTER)

sleep(5)

driver.quit()
