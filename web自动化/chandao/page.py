#coding=utf-8
from selenium import webdriver
from FindElement import FindElement
class page():
    def __init__(self,driver,node):
        self.driver=driver
        self.fd=FindElement(driver,node)
    def get_element(self,key):
        fd=self.fd
        element=fd.get_element(key)
        return element
    def get_elements(self,key):
        fd=self.fd
        element=fd.get_elements(key)
        return element   
    def send_keys(self,key,value):
        self.get_element(key).send_keys(value)
    def location(self,element):
        driver=self.driver
        # 1、定位的元素在当前页面看不见是无法执行点击操作的，需找到对应坐标，滑动到对应坐标处
        # location=driver.find_element_by_id('submit').rect
        # x=location['x']
        # y=location['y']
        # print(location['x'],location['y'])
        # driver.execute_script("window.scrollBy(x,y)")
        location=element.rect
        x=location['x']
        y=location['y']
        js_script='window.scrollBy('+str(x)+','+str(y)+')'
        driver.execute_script(js_script)