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


class Dd():
    def __init__(self):
        global driver
        driver = self.get_driver()

    def get_driver(self):
        # 连接appium服务端并告知要控制手机的版本及应用等配置并返回一个操作手机的驱动
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver

    def dd_login(self, username, password):
        print("进入登录界面")
        # 用户名
        driver.find_element(By.ID, 'et_phone_input').send_keys(username)
        sleep(2)
        # 密码
        driver.find_element(By.ID, 'et_password').send_keys(password)
        sleep(1)
        driver.find_element(By.ID, 'cb_privacy').click()
        sleep(1)
        # 登录
        driver.find_element(By.ID, 'tv').click()
        print('登录成功')
        sleep(3)

    def dd_logout(self):
        # 我的
        driver.find_element(By.XPATH, '//android.widget.TextView[@text="我的"]').click()
        sleep(2)
        # 滑动
        driver.swipe(0, 1000, 0, 500)
        # 点击设置
        driver.find_element(By.XPATH, '//android.widget.TextView[@text = "设置"]').click()
        sleep(2)
        driver.swipe(0, 1000, 0, 500)
        # 退出登录
        driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]').click()
        sleep(1)
        # 点击确定
        driver.find_element(By.XPATH, '//android.widget.Button[@text="确认"]').click()
        print('回到登录界面')
    def dd_dk(self, dk_type):
        # 工作台
        driver.find_element(By.XPATH, '//android.widget.TextView[@text="工作台"]').click()
        sleep(4)
        print(dk_type)
        # 进入考勤打卡按钮
        driver.find_elements(By.XPATH, "//android.view.View[@text='考勤打卡']")[0].click()
        sleep(4)
        # 打卡
        driver.find_element(By.XPATH, "//android.view.View[@text='" + dk_type + "']").click()
        print('打卡成功')
        sleep(4)
        # 关闭，回到主界面
        driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@content-desc="关闭"]').click()
        sleep(2)

    def dddk(self, dk_type, username, password):
        try:
            self.dd_login(username, password)
        except Exception:
            print('未在登录界面')
            self.dd_logout()
            self.dd_login(username, password)
        self.dd_dk(dk_type)
        self.dd_logout()


# 配置所控制手机
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

dk_types = ['上班打卡', '下班打卡', '外勤打卡']
print(str(time.ctime().split(' ')[4][:5])+'启动程序')
while True:
    # username='13277987082'
    # password='rz321324'
    peoples = [{"username": "18571708907", "password": "zy153580"},
               {"username": "15587621808", "password": "czr19970604"}]
    # username = '18571708907'
    # password = 'zy153580'
    h, m = time.ctime().split(' ')[4][:5].split(':')
    if h == '08' and m == '10':
        dd = Dd()
        for p in peoples:
            dd.dddk(dk_types[0], p['username'], p['password'])
        sleep(60 * 60 * 3 )
    elif h == '12' and m == '00':
        dd = Dd()
        for p in peoples:
            dd.dddk(dk_types[1], p['username'], p['password'])
        sleep(60 * 60 * 5.5)
    elif h == '18' and m == '00':
        dd = Dd()
        for p in peoples:
            dd.dddk(dk_types[1], p['username'], p['password'])
        sleep(60 * 60 * 2)

    # 调试代码段
    # elif h == '10':
    #     dd = Dd()
    #     for p in peoples:
    #         dd.dddk(dk_types[1], p['username'], p['password'])
    #     sleep(60*3)

    elif h == '20' and m == '31':
        dd = Dd()
        for p in peoples:
            dd.dddk(dk_types[1], p['username'], p['password'])
        sleep(60 * 60 * 11)
    else:
        continue
