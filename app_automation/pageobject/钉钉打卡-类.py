# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/17 23:14
# 功能：
import time
from time import sleep

import pymysql as pymysql
import xlrd2
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from appium import webdriver
from selenium.webdriver.common.by import By
import datetime
from chinese_calendar import is_workday
pymysql.install_as_MySQLdb()

# 配置所控制手机
# desired_caps = {
#     'platformName': 'Android',  # 被测手机是安卓
#     'platformVersion': '10',  # 手机安卓版本
#     'deviceName': 'xiaomi',  # 设备名，安卓手机可以随意填写
#     'appPackage': 'com.alibaba.android.rimet',  # 启动APP Package名称
#     'appActivity': '.biz.LaunchHomeActivity',  # 启动Activity名称
#     'unicodeKeyboard ': True,  # 使用自带输入法，输入中文时填True
#     'resetKeyboard': True,  # 执行完程序恢复原来输入法
#     'noReset': True,  # 不要重置App
#     'newCommandTimeout': 6000,
#     'automationName': 'UiAutomator2',
#     'ignoreHiddenApiPolicyError': True,
#     'skipServerInstallation': True,
#     'skipDeviceInitialization': True
#     # 'app' : r'd:\apk\bili.apk'
# }
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
        print(f'{username}-登录成功')
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
        print('退出登录')

    def dd_dk(self, dk_type,username):
        # 工作台
        driver.find_element(By.XPATH, '//android.widget.TextView[@text="工作台"]').click()
        sleep(3)
        print(dk_type)
        # 进入考勤打卡按钮
        driver.find_elements(By.XPATH, "//android.view.View[@text='考勤打卡']")[0].click()
        sleep(3)
        try:
            # 打卡
            driver.find_element(By.XPATH, "//android.view.View[@text='" + dk_type + "']").click()
            print(f'{username}-打卡成功')
            sleep(3)
            if driver.find_element(By.XPATH, "//android.widget.TextView[@text='工作通知']"):
                print('进入打卡通知界面')
                driver.find_element(By.ID, "back_icon").click()
                sleep(2)
        except Exception:
            print('未开启打卡通知！')
        finally:
            # 关闭，回到主界面
            sleep(1)
            driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@content-desc="关闭"]').click()
            sleep(2)

    def dddk(self, dk_type, username, password):
        try:
            self.dd_login(username, password)
        except Exception:
            print('未在登录界面')
            self.dd_logout()
            self.dd_login(username, password)
        self.dd_dk(dk_type,username)
        self.dd_logout()

    def get_dd_user(self):
        x = xlrd2.open_workbook('./data/dd_user_info.xlxs')
        s = x.sheet_by_index(0)
        for i in range(1, s.rows):
            name, password = s.row_values(i)
            print(name, password)

    @classmethod
    def get_dd_user_by_mysql(cls):
        db_info={'host':'localhost',
                 'user':'root',
                 'password':'nature',
                 'db':'dd',
                 'charset':'utf8'
                }
        # 连接数据库
        dd=pymysql.connect(**db_info)
        # 获取游标
        cursor=dd.cursor()
        sql='select * from user_info;'
        # 执行SQL，获取值为行记录int
        cursor.execute(sql)
        # 获取执行SQL返回数据，返回类型为元组
        data=cursor.fetchall()
        peoples = []
        for i in data:
            p = {}
            p['username'], p['password'] = i[0],i[1]
            peoples.append(p)
        # 提交执行结果
        dd.commit()
        # 关闭游标
        cursor.close()
        #关闭所连数据库
        dd.close()
        return peoples
    @classmethod
    def get_dd_user(cls):
        x = xlrd2.open_workbook('../data/dd_user_info.xlsx')
        s = x.sheet_by_index(0)
        peoples = []
        for i in range(1, s.nrows):
            p = {}
            p['username'], p['password'] = name, password = s.row_values(i)
            peoples.append(p)
        # print(peoples)
        return peoples

    @classmethod
    def get_dd_control_phone_config(cls):
        x = xlrd2.open_workbook('../data/dd_control_phone_config.xlsx')
        s = x.sheet_by_index(0)
        desired_caps = {}
        for i in range(1, s.nrows):
            name, password, comment = s.row_values(i)
            if password == '1':
                desired_caps[name] = True
            elif password == '0':
                desired_caps[name] = False
            else:
                desired_caps[name] = password
        # print(desired_caps)
        return desired_caps


if __name__ == '__main__':
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '启动程序')
    desired_caps = Dd.get_dd_control_phone_config()
    # print(desired_caps)
    dk_types = ['上班打卡', '下班打卡', '外勤打卡']
    # print(dk_types)
    peoples = Dd.get_dd_user()
    # print(peoples)
    while True:
        date = datetime.datetime.now()
        h, m = date.time().strftime('%H:%M:%S').split(':')[:2]
        if is_workday(date):
            if h == '08' and m == '40':
                dd = Dd()
                for p in peoples:
                    dd.dddk(dk_types[0], p['username'], p['password'])
                sleep(60 * 60 * 3)
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
            # elif h:
            #     dd = Dd()
            #     for p in peoples:
            #         dd.dddk(dk_types[1], p['username'], p['password'])
            #     sleep(60 * 3)

            elif h == '20' and m == '30':
                dd = Dd()
                for p in peoples:
                    dd.dddk(dk_types[1], p['username'], p['password'])
                sleep(60 * 60 * 11)
            else:
                continue
        else:
            continue
