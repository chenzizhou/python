from selenium import webdriver
import unittest
import time
class MyTest(unittest.TestCase) :
    '''测试有道搜索'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window ()
        self.driver .implicitly_wait(10)
        self.base_url="http://www.youdao.com"
    def test_youdao(self):
        '''关键字搜索'''
        driver=self.driver
        driver.get (self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("webdriver")
        driver.find_element_by_css_selector("#form > button").click()
        
        time.sleep (2)
        title = driver.title
        self.assertEqual(title,"webdriver -有道搜索")
    def tearDown(self) :
        self.driver.close()
if __name__=="__main__":
    unittest.main()
