from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from wq_user import User
import unittest


class test_wq(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def test_login(self):
        u = User()
        u.login(self.driver, 'admin', 'YSD@city')
        sleep(2)

        # u.make_scheme(driver, '081701', '巡检测试范围')
        # sleep(2)
        # u.make_plan(driver, '081701', '陈自然')
        u.make_ywpz(self.driver)
        sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
