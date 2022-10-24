from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from wq_user import User
import unittest


class test_wq(unittest.TestCase):
    def setUp(self):
        pass

    def test_login(self):
        u = User()
        u.login('bhcs', '123456')
        sleep(2)
        # u.make_scheme( '081701', '巡检测试范围')
        # sleep(2)
        # u.make_plan(driver, '081701', '陈自然')
        u.make_ywpz()
        sleep(2)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
