from selenium import webdriver
from time import sleep
import os
dr=webdriver.Chrome()
url='http://www.youdao.com'
dr.get(url)
dr.add_cookie({'name':'name','value':'nature'})
try:
    for cookie in dr.get_cookies():
        print("%s>%s"%(cookie['name'],cookie['value']))
except Exception as e:
    print(e)
