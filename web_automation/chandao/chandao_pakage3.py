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
from FindElement import FindElement
from selenium.webdriver.common.keys import Keys
from read_ini import *
from page_bean import *
class chandao(object):
    def __init__(self,driver=driver):
        self.driver=driver
    def login(self,url,username,password,node=None):
        driver=self.driver
        # url='http://114.215.149.146:81/zentaopms/www/user-login.html'
        driver.get(url)
        WebDriverWait(driver,5).until(ec.title_contains("用户登录"))
        driver.implicitly_wait(10)
        driver.maximize_window()
        ##account 用户名
        # username='chenzizhou'
        locator=(By.ID,('account'))
        WebDriverWait(driver,5).until(ec.visibility_of_element_located(locator))
        fd=FindElement(node=node)
        fd.send_keys('username',username)
        # get_element_by_id('account').send_keys(username)
        sleep(1)
        ##passwod 密码
        # password='YSD@city'
        fd.send_keys('password',password)
        # get_element_by_name('password').send_keys(password)
        ##submit
        fd.get_element('submit').click()
        # get_element_by_id('submit').click()
        sleep(1)
    def write_task(self,project_name='内部规划-外勤2.X',task_name='执行案例',assign_name='陈自洲',expected_time='7.5',node=None):
        driver=self.driver
        # read_ini=ReadIni(node='write_task')
        # read_ini.get_element('project').click()
        get_element_by_link_text('项目').click()
        sleep(1)
        # read_ini.get_element('task').click()
        get_element_by_link_text('任务').click()
        ##currentItem
        sleep(1)
        get_element_by_id('currentItem').click()
        # project_name='内部规划-外勤2.X'
        ## 
        get_element_by_class_name('form-control.search-input.empty').send_keys(project_name) 
        sleep(1)
        get_element_by_class_name('search-list-item.active').send_keys(Keys.ENTER)
        sleep(1)
        get_element_by_link_text('批量创建').click()
        sleep(1)
        # task_name='执行案例'
        get_element_by_id('name[0]').send_keys(task_name)
        sleep(1)
        get_element_by_id('type0').click()
        sleep(2)
        get_element_by_xpath('//*[@id="type0"]/option[@title="系统测试"]').click()
        sleep(2)
        # assign_name='陈自洲'
        get_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/span').click()
        sleep(2)
        element=get_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/div[2]/input')
        get_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/div[2]/input').send_keys(assign_name)
        print(element.get_attribute("value")=="陈自洲")
        sleep(1) 
        element=get_element_by_xpath('//*[@id="assignedTo0_chosen"]/div/ul/li/em').click()
        element1=get_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/span')
        print(element1.get_attribute('value'))
        sleep(1)
        ##预计 estimate[0]
        # expected_time='7.5'
        get_element_by_id('estimate[0]').send_keys(expected_time)
        ##预计开始 estStarted[0]
        sleep(1)
        get_element_by_id('estStarted[0]').click()
        sleep(1)
        get_element_by_xpath('/html/body/div[2]/div[3]/table/tfoot/tr/th').click()
        sleep(1)
        get_element_by_id('deadline[0]').click()
        sleep(1)
        get_element_by_xpath('/html/body/div[3]/div[3]/table/tfoot/tr/th').click()
        sleep(1)
        sleep(5)
        element=get_element_by_id('submit')
        x=element.location['x']
        y=element.location['y']
        js_script='window.scrollBy('+str(x)+','+str(y)+')'
        print(x,y)
        driver.execute_script(js_script)
        get_element_by_id('submit').click()
        sleep(2)
        get_element_by_id('assignedtome').click()
        sleep(2)
    def start_task(self,consumed,note=''):
        driver.find_element_by_xpath('//*[@id="assignedtome"]/span[1]').click()
        sleep(1)
        get_element_by_class_name('icon-task-start.icon-play').click()
        driver.switch_to_frame('iframe-triggerModal')
        sleep(2)
        get_element_by_xpath('//*[@id="consumed"]').send_keys(consumed)
        note_iframe=driver.find_element_by_class_name('ke-edit-iframe')
        driver.switch_to_frame(note_iframe)
        get_element_by_class_name('article-content').send_keys(note)
        sleep(2)
        driver.switch_to.parent_frame()
        element=get_element_by_id('submit')
        location(element)
        element.click()
    def finish_task(self,note=''):
        driver.switch_to.default_content()
        sleep(2)
        get_element_by_xpath('//*[@id="assignedtome"]/span[1]').click()
        get_element_by_class_name('icon-task-finish.icon-checked').click()
        sleep(2)
        driver.switch_to_frame('iframe-triggerModal')
        note_iframe=get_element_by_class_name('ke-edit-iframe')
        driver.switch_to_frame(note_iframe)
        get_element_by_class_name('article-content').send_keys(note)
        sleep(2)
        driver.switch_to.parent_frame()
        element=get_element_by_id('submit')
        location(element)
        element.click()
        sleep(2)



