###coding=utf-8
##from selenium import webdriver
##from time import sleep
##driver=webdriver.Chrome()
###driver=webdriver.Firefox()
###driver=webdriver.Ie()
##driver.get("http://www.baidu.com")
##name="哈登"
##print("根据#选择器获取定位")
##driver.find_element_by_css_selector("input#kw").send_keys(name)
##
###driver.find_element_by_xpath("//input[@id='kw']").send_keys(name)
###driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input").send_keys(name)
###driver.find_element_by_class_name("s_ipt").send_keys(name)
###driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]").send_keys(name)
###点击
##sleep(5)
##driver.find_element_by_id("su").click()
##sleep(5)
##driver.quit()
###回退    
###driver.back()



##调用Javascript
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#设置浏览器窗口大小
driver.set_window_size(900,600)
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
#通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(700,450);"
driver.execute_script(js)
sleep(2)
ActionChains(driver).click(driver.find_element_by_xpath("//*[@id='su']")).perform()
##driver.quit()


