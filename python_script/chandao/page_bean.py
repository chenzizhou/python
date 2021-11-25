from selenium import webdriver
driver=webdriver.Chrome()
url='http://114.215.149.146:81/zentaopms/www/user-login.html'
def get_element_by_id(id):        
        element=driver.find_element_by_id(id)
        return element
def get_element_by_xpath(xpath):
        # driver=self.driver
        element=driver.find_element_by_xpath(xpath)
        return element
def get_element_by_link_text(text):
        # driver=self.driver
        element=driver.find_element_by_link_text(text)
        return element
def get_element_by_name(text):
        # driver=self.driver
        element=driver.find_element_by_name(text)
        return element
def get_element_by_class_name(text):
        # driver=self.driver
        element=driver.find_element_by_class_name(text)
        return element
def location(element):
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







