# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/17 23:14
# 功能：
import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'deviceName': 'xiaomi',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.alibaba.android.rimet',  # 启动APP Package名称
    'appActivity': '.biz.LaunchHomeActivity',  # 启动Activity名称
    'unicodeKeyboard ': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2',
    'ignoreHiddenApiPolicyError': True,
    'skipServerInstallation': True,
    'skipDeviceInitialization': True
    # 'app' : r'd:\apk\bili.apk'
}


def dddk(dk_type,username,password):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    # driver.find_element(By.ID, 'btn_agree')
    # driver.find_element(By.XPATH, '//android.widget.FrameLayout').click()
    driver.find_element(By.ID, 'et_phone_input').send_keys(username)
    sleep(1)
    driver.find_element(By.ID, 'et_pwd_login').send_keys(password)
    sleep(1)
    driver.find_element(By.ID, 'cb_privacy').click()
    sleep(1)
    driver.find_element(By.ID, 'tv').click()
    sleep(1)
    driver.find_elements(By.ID, 'home_bottom_tab_icon')[1].click()
    driver.find_elements(By.XPATH, "//android.view.View[@text='考勤打卡']")[0].click()
    # sleep(1)
    driver.find_element(By.XPATH, "//android.view.View[@text='" + dk_type + "']").click()
    driver.find_element(By.XPATH,'//android.widget.RelativeLayout[@content-desc="关闭"]').click()
    driver.find_elements(By.ID, 'home_bottom_tab_text')[3].click()
    driver.swipe(0,1000,0,500)
    driver.find_element(By.XPATH, '//android.widget.TextView[@text = "设置"]').click()
    driver.swipe(0, 1000, 0, 500)
    driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]').click()
    driver.find_element(By.XPATH, '//android.widget.Button[@text="确认"]').click()





while True:
    username='13277987082'
    password='rz321324'
    h, m = time.ctime().split(' ')[4][:5].split(':')
    if h == '08' and m == '45':
        dddk('上班打卡',username,password)
        sleep(60 * 60 * 3 - 5)
    elif h == '12' and m == '01':
    # elif h == '12':
        dddk('下班打卡',username,password)
        sleep(60 * 60 * 6 - 60)
    elif h == '18' and m == '01':
        dddk('下班打卡',username,password)
        sleep(60 * 60 * 15 - 60 * 15 - 60)
    else:
        continue
