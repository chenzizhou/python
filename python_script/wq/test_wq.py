from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from wq_user import User
import unittest


class test_wq(unittest.TestCase):
    def setUp(self):
        pass

    def test_login(self):
        url = 'http://192.168.10.195:7799/login'
        u = User(url)
        username = 'admin'
        password = '123456'
        u.login(username, password)
        sleep(2)
        # u.make_scheme( '081701', '巡检测试范围')
        # sleep(2)
        # u.make_plan(driver, '081701', '陈自然')
        ywlxs = ['巡检', '养护', '检漏', '排污稽查']
        gws = {'供水管网': ['管段', '阀门', '控制阀门', '消防栓', '水表'], '高铁供水': ['管段', '渠道', '阀门', '控制阀门', '消防栓'], }
        gs=[]
        u.make_ywpz(ywlxs,gws,gs)
        sleep(2)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
