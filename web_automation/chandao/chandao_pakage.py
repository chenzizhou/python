#coding=utf-8
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
from page import page
class chandao(object):
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def login(self,url,username='admin',password='123456',node='login'):
        driver=self.driver
        # url='http://114.215.149.146:81/zentaopms/www/user-login.html'
        driver.get(url)
        WebDriverWait(driver,5).until(ec.title_contains("用户登录"))
        ##account 用户名
        # username='chenzizhou'
        locator=(By.ID,('account'))
        WebDriverWait(driver,5).until(ec.visibility_of_element_located(locator))
        pg=page(driver,node)
        pg.send_keys('username',username)
        fd=FindElement(driver,node=node)
        sleep(1)
        ##passwod 密码
        # password='YSD@city'
        fd.send_keys('password',password)
        ##submit
        fd.get_element('submit').click()
        sleep(1)
    def write_task(self,project_name='内部规划-外勤2.X',task_name='执行案例',assigned_name='陈自洲',expected_time='7.5',node='write_task'):
        driver=self.driver
        pg=page(driver,node)
        fd=FindElement(driver,'write_task')
        pg.get_element('project').click()
        sleep(1)
        fd.get_element('task').click()
        ##currentItem
        sleep(1)
        fd.get_element('currentItem').click()
        # project_name='内部规划-外勤2.X'
        driver.find_element_by_class_name('form-control.search-input.empty').send_keys(project_name) 
        sleep(1)
        driver.find_element_by_class_name('search-list-item.active').send_keys(Keys.ENTER)
        sleep(1)
        fd.get_element('批量创建').click()
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
        fd.send_keys('assigned_name',assigned_name)
        print(element.get_attribute("value")=="陈自洲")
        sleep(1) 
        element=driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/div/ul/li/em').click()
        element1=driver.find_element_by_xpath('//*[@id="assignedTo0_chosen"]/a/span')
        print(element1.get_attribute('value'))
        sleep(1)
        ##预计 estimate[0]
        # expected_time='7.5'
        fd.send_keys('expected_time',expected_time)
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
        element=driver.find_element_by_id('submit')
        x=element.location['x']
        y=element.location['y']
        js_script='window.scrollBy('+str(x)+','+str(y)+')'
        print(x,y)
        driver.execute_script(js_script)
        fd.get_element('submit').click()
        sleep(2)
    def start_task(self,consumed='7.5',note='',node='start_task'):
        driver=self.driver
        pg=page(driver,node)
        fd=FindElement(driver,'start_task')
        fd.get_element('assigned').click()
        sleep(1)
        fd.get_element('start').click()
        driver.switch_to_frame('iframe-triggerModal')
        sleep(2)
        fd.send_keys('consumed',consumed)
        note_iframe=driver.find_element_by_class_name('ke-edit-iframe')
        driver.switch_to_frame(note_iframe)
        fd.send_keys('note',note)
        sleep(2)
        driver.switch_to.parent_frame()
        element=fd.get_element('submit')
        pg.location(element)
        element.click()
    def finish_task(self,note='',node='finish_task'):
        driver=self.driver
        pg=page(driver,node)
        fd=FindElement(driver,'finish_task')
        driver.switch_to.default_content()
        sleep(2)
        fd.get_element('assigned').click()
        fd.get_element('finish').click()
        sleep(2)
        driver.switch_to_frame('iframe-triggerModal')
        note_iframe=driver.find_element_by_class_name('ke-edit-iframe')
        driver.switch_to_frame(note_iframe)
        fd.send_keys('note',note)
        sleep(2)
        driver.switch_to.parent_frame()
        element=fd.get_element('submit')
        pg.location(element)
        element.click()
        sleep(2)
    def delete_task(self,project_name='内部规划-外勤2.X',node='delete_task'):
        driver=self.driver
        pg=page(driver,node)
        fd=FindElement(driver,'delete_task')
        sleep(1)
        pg.get_element('project').click()
        sleep(1)
        fd.get_element('task').click()
        ##currentItem
        sleep(1)
        pg.get_element('currentItem').click()
        # project_name='内部规划-外勤2.X'
        driver.find_element_by_class_name('form-control.search-input.empty').send_keys(project_name) 
        sleep(1)
        driver.find_element_by_class_name('search-list-item.active').send_keys(Keys.ENTER)
        pg.get_element('指派给我').click()
        sleep(2)
        pg.get_element('搜索').click()
        pg.get_element('筛选项').click()
        sleep(2)
        pg.get_element('筛选项').send_keys('由谁创建')
        driver.find_element_by_class_name('active-result').click()
        sleep(2)
        driver.find_element_by_class_name('chosen-single.chosen-default').click()
        driver.find_element_by_class_name('chosen-single.chosen-default').send_keys('陈自州')
        driver.find_element_by_class_name('active-result.highlighted').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="task-search"]/tbody/tr[2]/td/button[3]/i').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="field2_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="field2_chosen"]/a').send_keys('任务状态')
        driver.find_element_by_xpath('//*[@id="field2_chosen"]/div/ul/li').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="value2_chosen"]/a').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="value2_chosen"]/a').send_keys('已关闭')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="value2_chosen"]/div/ul/li').click()
        driver.find_element_by_id('submit').click()
        sleep(2)
        elements=pg.get_elements('任务名')
        print(len(elements))
        if len(elements)==0:
            pass
        else:
            # 不能直接用int进行迭代，而必须加个range
            for i in range(0,len(elements)):
                sleep(2)
                pg.get_element('任务名').click()
                sleep(2)
                pg.get_element('删除').click()
                sleep(2)
                # 浏览器弹框处理alert、confirm、Promt
                confirm=driver.switch_to.alert
                text=confirm.text
                print(text)
                confirm.accept()
                sleep(2)
        sleep(2)







