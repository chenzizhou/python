# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/17 23:14
# 功能：
import time
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '11',  # 手机安卓版本
    'deviceName': 'mix fold',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.alibaba.android.rimet',  # 启动APP Package名称
    'appActivity': '.biz.LaunchHomeActivity',  # 启动Activity名称#
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
    driver.find_elements(By.ID, 'home_app_item')[2].click()
    driver.find_elements(By.XPATH, "//android.view.View[@text='考勤打卡']")[0].click()
    driver.find_element(By.XPATH, "//android.view.View[@text='" + dk_type + "']").click()


while True:
    h, m = time.ctime().split(' ')[3][:5].split(':')
    if h == '09' and m == '00':
        dddk('上班打卡')
        sleep(60 * 60 * 3 - 5)
    elif h == '12' and m == '00':
        dddk('下班打卡')
        sleep(60 * 60 * 6 - 5)
    elif h == '00' and m == '09':
        dddk('外勤打卡')
        sleep(60 * 60 * 15 - 5)
    else:
        continue
