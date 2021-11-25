from read_ini import ReadIni
class FindElement():
    def __init__(self,driver,node):
        self.driver=driver
        self.read_ini=ReadIni(node=node)
    def get_element(self,key):
        driver=self.driver
        data=self.read_ini.get_value(key)
        by=data.split('>')[0]
        value=data.split('>')[1]
        if by=='id':
            return driver.find_element_by_id(value)
        elif by=='name':
           element=driver.find_element_by_name(value)
        elif by=='class':
            element=driver.find_element_by_class_name(value)
        elif by=='xpath':
            element=driver.find_element_by_xpath(value)
        elif by=='text':
            element=driver.find_element_by_link_text(value)
            print(element)
        return element
    def send_keys(self,key,value):
        self.get_element(key).send_keys(value)