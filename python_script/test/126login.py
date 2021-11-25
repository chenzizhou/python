##从selenium中获取浏览器驱动
from selenium import webdriver
from selenium.webdriver import ActionChains
##从time中获取sleep方法
from time import sleep

##获取谷歌的驱动
driver=webdriver.Chrome()
driver.implicitly_wait(10)
##设置浏览器窗口大小
##driver.set_window_size(900,400)

##获取浏览器窗口大小
##print(driver.get_window_size())
##定义变量，如不是数字类型，变量值需引号
url="http://www.126.com"
##url1='https://mail.163.com/register/index.htm?from=126mail&utm_source=126mail'
##浏览器地址栏输入
driver.get(url)
sleep(1)
driver.maximize_window()##设置最大窗口模式
login=driver.current_window_handle#获取当前页的句柄
name='nature_simple'
password='czr199764'
tel=15587621808

#登录
driver.switch_to.frame(0)

##跳出框架
##driver.switch_to.default_content()

driver.find_element_by_name("email").send_keys(name)
driver.find_element_by_id("pwdtext").send_keys(password)

try:
    driver.switch_to.default_content()
    count=driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
    driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='loginDiv']/iframe"))
    driver.find_element_by_xpath('//*[@id="dologin"]').click()
except Exception as e:
    print(e)
driver.switch_to.default_content()    
name=driver.find_element_by_id('spnUid').text
print(name)
