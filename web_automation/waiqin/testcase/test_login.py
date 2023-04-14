# coding: utf8
# 作者：NATURE
# 开发时间：2022/10/11 22:30
# 功能：
import os
import sys
import unittest
from time import sleep

from ddt import ddt, data, unpack
import sys

path = os.getcwd().split('\\')[0]
for i in range(0, len(os.getcwd().split('\\')) - 1):
    if i == 0:
        path = path
        sys.path.append(path)
    else:
        path = path + '/' + os.getcwd().split('\\')[i]
        sys.path.append(path)
from web_automation.waiqin.pageobject.login_page import LoginPage
import warnings


@ddt  # 使用数据驱动类必须装饰
class TestLogin(unittest.TestCase):
    def setUp(self):  # 每个用例执行之前执行的方法
        # 解决框架自动关闭浏览器报错：ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter("ignore", ResourceWarning)
        print('准备')

    @data(('admin', '123456'), ('nature', '123456'))  # 使用命令执行时python test_01_login执行不了，因为测试用例名加了序列号和实参
    # ，test_01_login_1___admin___123456
    @unpack  # 数据是序列，需解包
    def test_01_login(self, username, password):
        '''测试登录'''
        url = 'http://192.168.10.195:7799/login'
        l = LoginPage()
        l.login(url, username, password)
        self.assertTrue(l.get_expect_element())
        sleep(1)
        # 解决框架自动关闭浏览器报错：ResourceWarning: Enable tracemalloc to get the object allocation traceback
        # l.quit()

    @unittest.skip  # 添加改装饰后，测试机也加不进去
    def test_02_login(self):
        print(111222)

    def tearDown(self):  # 每个用例执行之后执行的方法
        print('结束')


if __name__ == '__main__':  # 并没有执行
    # print(sys.path)
    # 获取测试集对象
    # suite = unittest.TestSuite()
    # 使用搜索加载制定路径模块下的用例集
    # suite=unittest.defaultTestLoader.discover('../testcase','test_login.py')
    # 添加用例集
    # discover.addTest(TestLogin('test_02_login'))
    # # suite.addTest(TestLogin("test_01_login_1"))
    # # runner = unittest.TextTestRunner()
    # 添加时间生成唯一测试报告
    # file_url='../report/'+time.strftime("%Y-%m-%d %H_%M_%S")+' result.html'
    # print(file_url)
    # f=open(file_url,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='外勤登录',description='用例执行情况：')
    # runner.run(discover)
    # f.close()
    # send_mail(get_new_file())
    # unittest.main()
    unittest.main(defaultTest=['TestLogin.test_02_login'],verbosity=2)
    # unittest.main(defaultTest=['TestLogin'], verbosity=2)
