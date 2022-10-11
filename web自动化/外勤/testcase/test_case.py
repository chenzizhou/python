# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/11 22:30
# 功能：
import unittest
from selenium import webdriver
from time import sleep

from web自动化.外勤.pageobject.login_page import LoginPage


class TestCase(unittest.TestCase):
    def test_01_login(self):
        l = LoginPage()
        l.login()
        l.close()

    def test_02_login(self):
        print(111222)


if __name__ == '__main__':  # 并没有执行
    print('运行')
    unittest.main()
