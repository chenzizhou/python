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
    'deviceName': 'mix fold',  # 设备名，安卓手机可以随意填写
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


def dddk(dk_type):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    # driver.find_element(By.ID, 'btn_agree')
    driver.find_element(By.XPATH, '//android.widget.FrameLayout').click()
    element = driver.find_element(By.ID, 'et_phone_input')
    element.clear()
    element.click()
    element.send_keys('15587621809')
    sleep(1)
    mmgl = driver.find_element(By.XPATH, '//android.widget.FrameLayout')
    if mmgl:
        mmgl.click()
        sleep(1)
        driver.find_element(By.ID, 'et_password').clear()
        driver.find_element(By.ID, 'et_password').send_keys('czr19970604')
        sleep(1)
    else:
        driver.find_element(By.ID, 'et_password').clear()
        sleep(1)
        driver.find_element(By.ID, 'et_password').click()
        sleep(1)
        driver.find_element(By.ID, 'et_password').send_keys('czr19970604')
    sleep(1)
    driver.find_element(By.ID, 'cb_privacy').click()
    sleep(1)
    driver.find_element(By.ID, 'tv').click()
    sleep(1)
    driver.find_elements(By.ID, 'home_app_item')[2].click()
    driver.find_elements(By.XPATH, "//android.view.View[@text='考勤打卡']")[0].click()
    # sleep(1)
    # driver.find_element(By.XPATH, "//android.view.View[@text='" + dk_type + "']").click()
    driver.find_element(By.XPATH,'//android.widget.RelativeLayout[@content-desc="关闭"]').click()
    driver.find_elements(By.ID, 'home_bottom_tab_text')[3].click()
    driver.swipe(0,1000,0,500)
    sz=driver.find_element(By.XPATH, '//android.widget.TextView[@text = "设置"]')
    sz.click()
    driver.swipe(0, 1000, 0, 500)
    driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]').click()

    driver.find_element(By.XPATH, '//android.widget.Button[@text="确认"]').click()

# print(time.ctime())
# print(time.ctime().split(' ')[3][:5])
# print(time.ctime().split(' ')[4][:5])
# h, m = time.ctime().split(' ')[4][:5].split(':')

while True:
    h, m = time.ctime().split(' ')[3][:5].split(':')
    if h == '08' and m == '45':
        dddk('上班打卡')
        sleep(60 * 60 * 3 - 5)
    elif h == '12' and m == '01':
        dddk('下班打卡')
        sleep(60 * 60 * 6 - 60)
    elif h == '18' and m == '32':
        dddk('下班打卡')
        sleep(60 * 60 * 2.4)
    elif h == '20' and m == '55':
        dddk('下班打卡')
        sleep(60 * 60 * 2.4)
    else:
        continue
