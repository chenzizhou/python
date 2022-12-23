# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/11 22:30
# 功能：
import HTMLTestRunner
import time
import unittest
from ddt import ddt, data, unpack
from web_automation.外勤.pageobject.login_page001 import LoginPage
from web_automation.外勤.util.find_new_file import get_new_file
from web_automation.外勤.util.send_mail import send_mail


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('准备')

    @data(('bhcs', '123456'))
    @unpack
    def test_01_login(self, username, password):
        '''测试登录'''
        l = LoginPage()
        l.login(username,password)
        # self.assertTrue(l.get_expect_element())
        l.close()

    @unittest.skip #添加改装饰后，测试机也加不进去
    def test_02_login(self):
        print(111222)

    def tearDown(self):
        print('结束')


if __name__ == '__main__':  # 并没有执行
    print('运行')
    # suite = unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover('../testcase','test*.py')
    discover.addTest(TestLogin('test_02_login'))
    # suite.addTest(TestLogin("test_01_login_1"))
    # runner = unittest.TextTestRunner()
    file_url='../report/'+time.strftime("%Y-%m-%d %H_%M_%S")+' result.html'
    print(file_url)
    f=open(file_url,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='外勤登录',description='用例执行情况：')
    runner.run(discover)
    f.close()
    send_mail(get_new_file())
    # unittest.main()
