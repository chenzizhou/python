from selenium import webdriver
import random   
# 时间
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException
##键盘事件
from selenium.webdriver.common.keys import Keys
# 鼠标事件
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class chandao(object):
    def __init__(self,driver):
        self.driver=driver
    def get_element_by_id(self,id):
        driver=self.driver
        element=driver.find_element_by_id(id)
        return element
    def get_element_by_xpath(self,xpath):
        driver=self.driver
        element=driver.find_element_by_xpath(xpath)
        return element
    def get_element_by_link_text(self,text):
        driver=self.driver
        element=driver.find_element_by_xpath(text)
        return element
    def login(self,url,username,password):
        driver=self.driver
        # url='http://114.215.149.146:81/zentaopms/www/user-login.html'
        driver.get(url)
        WebDriverWait(driver,5).until(ec.title_contains("用户登录"))
        driver.implicitly_wait(10)
        ##account 用户名
        # username='chenzizhou'
        locator=(By.ID,('account'))
        WebDriverWait(driver,5).until(ec.visibility_of_element_located(locator))
        # self.get_element_by_id('account').send_keys(username)
        driver.find_element_by_id('account').send_keys(username)
        sleep(1)
        ##passwod 密码
        # password='YSD@city'
        driver.find_element_by_name('password').send_keys(password)
        ##submit
        driver.find_element_by_id('submit').click()
        sleep(1)
    def write_task(self,project_name='内部规划-外勤2.X',task_name='执行案例',assign_name='陈自洲',expected_time='7.5'):
        driver=self.driver
        driver.find_element_by_link_text('项目').click()
        sleep(1)
        driver.find_element_by_link_text('任务').click()
        ##currentItem
        sleep(1)
        driver.find_element_by_id('currentItem').click()
        # project_name='内部规划-外勤2.X'
        ##  
        driver.find_element_by_class_name('form-control.search-input.empty').send_keys(project_name)
        sleep(1)
        driver.find_element_by_class_name('search-list-item.active').send_keys(Keys.ENTER)
        sleep(1)
        driver.maximize_window()
        sleep(1)
        driver.find_element_by_link_text('批量创建').click()
        sleep(1)
        # task_name='执行案例'
        driver.find_element_by_id('name[0]').send_keys(task_name)
        sleep(1)
        driver.find_element_by_id('type0').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="type0"]/option[@title="系统测试"]').click()
        sleep(2)
        # assign_name='陈自洲'
        driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/span').click()
        sleep(2)
        element=driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/div[2]/input')
        driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/div[2]/input').send_keys(assign_name)
        print(element.get_attribute("value")=="陈自洲")
        sleep(1) 
        element=driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/div/ul/li/em').click()
        element1=driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/span')
        print(element1.get_attribute('value'))
        sleep(1)
        ##预计 estimate[0]
        # expected_time='7.5'
        driver.find_element_by_id('estimate[0]').send_keys(expected_time)
        ##预计开始 estStarted[0]
        sleep(1)
        driver.find_element_by_id('estStarted[0]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tfoot/tr/th').click()
        sleep(1)
        driver.find_element_by_id('deadline[0]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tfoot/tr/th').click()
        sleep(1)
        ##driver.find_element_by_id(submit).click()