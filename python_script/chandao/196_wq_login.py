from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
url='http://192.168.10.196:7799/login'
driver.get(url)
username='admin'
password='123456'
##隐式等待
driver.implicitly_wait(10)
sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div[5]/div[1]/div/div/div/div/div[3]/div[1]/div[1]/input').send_keys(username)
sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div[5]/div[1]/div/div/div/div/div[3]/div[2]/div[1]/input').send_keys(password)
sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div[5]/div[1]/div/div/div/div/div[3]/div[5]/button').click()
sleep(2)
##巡检方案制定 /html/body/div[8]/div/div[1]/div/span[2]
xjgl=driver.find_element_by_xpath('//*[@id="main"]/div[5]/div[2]/div[1]/div/div/div/div[3]/div/span[2]')
ActionChains(driver).move_to_element(xjgl).perform()

##xjfazd=driver.find_element_by_css_selector('body > div:nth-child(9) > div > div:nth-child(1) > div > span.v-menu-item-text')
xjfazd=driver.find_element_by_css_selector('body > div.v-popup.v-menu-popup > div > div:nth-child(1) > div > span.v-menu-item-text')
ActionChains(driver).click(xjfazd).perform()
f=driver.find_element_by_css_selector('body > div.v-dialog.v-s-normal > div.v-dialog-body > div > div > iframe')
driver.switch_to.frame(f)
##创建方案
fa_name='20210728'
driver.find_element_by_css_selector('#scheme_name').send_keys(fa_name)
##筛选 #screenPageA > img
sleep(3)
sx=driver.find_element_by_css_selector('#screenPageA > img')
ActionChains(driver).click(sx).perform()
sleep(3)
##选择作业区域#workscope > xm-select > i   
zyqy=driver.find_element_by_css_selector('#workscope > xm-select > i')
ActionChains(driver).click(zyqy).perform()
sleep(3)
##伪元素解决用css定位
fw=driver.find_element_by_css_selector('#workscope > xm-select > div.xm-body.absolute > div > div.scroll-body > div:nth-child(1) > div > i.xm-option-icon.xm-iconfont.xm-icon-duox')
ActionChains(driver).click(fw).perform()
sleep(2)
driver.find_element_by_css_selector('#workscope > xm-select > div.xm-label.single-row > div > div').click()
sleep(1)
##搜索
driver.find_element_by_css_selector('#buttonPanel > input.button.base-button-query-style').click()
sleep(2)
##选择设备
driver.find_element_by_css_selector('#datagrid-row-r2-2-1 > td:nth-child(1) > div > input[type=checkbox]').click()
##点击确定，回到制定界面
driver.find_element_by_css_selector('#return-bt > input.button.retrieval-button.base-button-save-style').click()
##有效范围#workscope2 > xm-select > div.xm-label.single-row
driver.find_element_by_css_selector('#workscope2 > xm-select > div.xm-label.single-row').click()
##备注
driver.find_element_by_css_selector('#form-schemeRemark').send_keys('chenziran')
##上报#attachmentfile > div > div:nth-child(1) > div > a > img

##保存#saveBut
driver.find_element_by_css_selector('#saveBut').click()

##提示框处理
driver.switch_to_alert().accept()
