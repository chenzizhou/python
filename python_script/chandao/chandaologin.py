from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
url='http://114.215.149.146:81/zentaopms/www/user-login.html'
driver.get(url)
##account 用户名
user='chenzizhou'
driver.find_element_by_id('account').send_keys(user)
sleep(1)
##passwod 密码
password='YSD@city'
driver.find_element_by_name('password').send_keys(password)
sleep(1)
##submit
driver.find_element_by_id('submit').click()
