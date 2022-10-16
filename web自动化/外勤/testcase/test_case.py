# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/11 22:30
# 功能：
import HTMLTestRunner
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from time import sleep
from web自动化.外勤.pageobject.login_page import LoginPage


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('准备')

    @data(('admin', '123456'), ('nature', '123456'))
    @unpack
    def test_01_login(self, username, password):
        l = LoginPage()
        l.login(username,password)
        self.assertTrue(l.get_expect_element())
        l.close()

    @unittest.skip
    def test_02_login(self):
        print(111222)

    def tearDown(self):
        print('结束')


if __name__ == '__main__':  # 并没有执行
    print('运行')
    # suite = unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover('../testcase','test*.py')
    discover.addTest()
    # suite.addTest(TestLogin("test_01_login_1"))
    # runner = unittest.TextTestRunner()
    f=open('../report/result.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='外勤登录',description='用例执行情况：')
    runner.run(discover)
    f.close()
    # unittest.main()
