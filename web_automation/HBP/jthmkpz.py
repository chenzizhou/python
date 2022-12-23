# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:09:02 2022
集团化模块配置
@author: Administrator
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from sys import argv
import os
ip=input('请输入ip:')
sleep(2)
if not ip:
  ip='192.168.10.196'  
url='http://'+ip+':7799/hbp'
driver=webdriver.Chrome()
if len(argv)>1:
    driver.get('http://'+argv[1]+':7799/hbp')
else:
    driver.get(url)
driver.maximize_window()
def login():
    driver.find_element_by_id('username').send_keys('admin')
    sleep(1)
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('login').click()
    sleep(1)
    if driver.find_element_by_class_name('subsystem-green2'):
        driver.find_element_by_class_name('subsystem-green2').click()
def make_sggd():  
    sleep(1)   
    driver.find_element_by_xpath('//a[@title="系统管理"]').click()
    # driver.find_element_by_id('menu_467002632272084992').click()
    sleep(1)
    # 定时计划界面
    driver.find_element_by_xpath('//*[@id="leftMenu"]/li[6]/a').click()
    sleep(1)
    # 需跳转到框架中
    dsjh=driver.find_element_by_xpath('//*[@id="content-main"]/iframe[@name="iframescheduler_list"]')
    print(dsjh)
    driver.switch_to.frame(dsjh)
    sleep(1)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@href="/hbp/platform/job/scheduler/jobEdit.htm"]').click()
    # driver.find_element_by_css_selector('body > div > div.toolbar-panel > div > div > div > a.btn.btn-primary.fa.fa-add').click()
    # ActionChains(driver).click(tj).perform()
    # driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/a[2]/span').click()
    # driver.find_element_by_class_name('fa-add').click()
    driver.find_element_by_id('jobName').send_keys('AreaSyncScheduler')
    driver.find_element_by_id('jobClass').send_keys('com.zzht.bp.biz.scheduler.AreaSyncScheduler')
    driver.find_element_by_id('description').send_keys('施工工地同步')
    sg=[('T_SGGD','T_SGGD','表名'),
    ('ID_','oid','gis关联hbp字段名'),
    ('ASSOC_ID','gid','hbp关联gis字段名'),
    ('AREA_ID','area_id','区域编号'),
    ('AREA_NAME','area_name','区域名称'),
    ('ADDRESS','address','发生位置'),
    ('START_TIME','start_time','开始时间'),
    ('END_TIME','end_time','结束时间'),
    ('PARTY_A_NAME','party_a_name','甲方单位名称'),
    ('PARTY_A_CONTACTS','party_a_contacts','甲方单位联系人'),
    ('PARTY_A_PHONE','party_a_phone','甲方联系电话'),
    ('COMPANY_NAME','company_name','施工单位名称'),
    ('COMPANY_CONTACTS','company_contacts','施工单位联系人'),
    ('COMPANY_PHONE','company_phone','施工联系电话'),
    ('DESCRIPTION','description','施工内容描述'),
    ('AREA_STATUS','area_status','区域状态'),
    ('REPORT_TIME','report_time','上报时间'),
    ('REPORT_STAFF','report_staff','上报人')]
    # 添加参数
    for i in (range(18)):    
        driver.find_element_by_id('addRow').click()
        driver.find_elements_by_id('paramName')[i].send_keys(sg[i][0])
        driver.find_elements_by_id('paramValue')[i].send_keys(sg[i][1])
        sleep(0.5)
    sleep(2)
    
    # 保存
    driver.find_element_by_css_selector('body > div > div.panel-toolbar > div > a.btn.btn-primary.fa.fa-save').click()
    driver.switch_to.default_content()
    
    # 取消
    driver.find_element_by_class_name('btn-default').click()
    driver.switch_to.frame(dsjh)
    sleep(1)
    # 鼠标虚浮框定位 F12+source+鼠标虚浮到定位位置+定位器（ctr+shift+c）
    gd=driver.find_element_by_xpath('//*[@id="2"]/td[6]/div/div[1]')
    ActionChains(driver).move_to_element(gd).perform()
    
    # 添加计划
    driver.find_element_by_xpath('//*[@id="2"]/td[6]/div/div[3]/ul/li[1]/a').click()
    driver.find_element_by_id('trigName').send_keys('test')
    driver.find_element_by_xpath('//*[@id="planType"]/option[2]').click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div/a[1]').click()
    driver.switch_to.default_content()
    driver.find_element_by_class_name('btn-default').click()
    sleep(1)
    driver.switch_to.frame(dsjh)
    driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[1]/a[3]/span').click()
    gd=driver.find_element_by_xpath('//*[@id="2"]/td[6]/div/div[1]')
    ActionChains(driver).move_to_element(gd).perform()
    driver.find_element_by_xpath('//*[@id="2"]/td[6]/div/div[3]/ul/li[3]/a').click()
def make_ecode():
    sleep(1)   
    tablenames=["t_csywdemo","t_early_warn_order","t_event_base",
                "t_gdzyw","t_patrol_scheme","t_sggd","t_valve_switch","t_xjwgsbzyw","t_ycsj"]
    driver.find_element_by_xpath('//a[@title="表单管理"]').click()
    sleep(0.5)
    driver.find_element_by_xpath('//span[@title="业务对象管理"]').click()
    driver.switch_to.frame('iframeywdxgl')
    for i in tablenames:
        try:
            driver.find_element_by_xpath('//td[@title="'+i+'"]').click()
        except Exception as e:
            continue
        driver.find_element_by_class_name('fa-edit').click()
        sleep(1)
        driver.switch_to.frame('listFrame')
        driver.find_element_by_xpath('//*[@id="boDefTabs"]/ul/li[2]/a').click()
        driver.find_element_by_id('addAttr').click()
        sleep(1)
        driver.switch_to.default_content()
        sleep(1)
        ecode_eidt=driver.find_element_by_xpath('/html/body/div[6]/div[2]/iframe')
        driver.switch_to.frame(ecode_eidt)
        driver.implicitly_wait(10)
        input_name=driver.find_element_by_id('name')
        input_name.clear()
        input_name.send_keys("公司编码")
        sleep(1)
        input_code=driver.find_element_by_id('code')
        sleep(1)
        input_code.click()
        sleep(1)
        input_code.clear()
        sleep(1)
        input_code.send_keys('ecode')
        sleep(0.5)
        driver.find_element_by_id('fieldName').clear()
        driver.find_element_by_id('fieldName').send_keys('ECODE_')
        sleep(0.5)
        driver.find_element_by_id('desc').send_keys('公司编码')
        driver.find_element_by_id('defValue').send_keys('0')
        sleep(0.5)
        driver.find_element_by_id('attrLength').clear()
        driver.find_element_by_id('attrLength').send_keys('64')
        sleep(0.5)
        driver.switch_to.default_content()
        driver.find_element_by_class_name('fa-ok').click()
        try:
            element=driver.find_element_by_class_name('layui-laydialog-title')
            print('又该元素！')
            element1=driver.find_element_by_xpath('/html/body/div[8]/div[3]/a')
            sleep(1)
            element1.click()
            print('又该元素！')
            driver.find_element_by_class_name('fa-cancel').click()
        except Exception:
            print('没有找到元素！')
        sleep(1)
        driver.switch_to.frame('iframeywdxgl')
        driver.find_element_by_class_name('fa-save').click()
        sleep(1)
login()
make_ecode()
        


