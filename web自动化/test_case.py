# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/9 22:56
# 功能：
import unittest
from selenium import webdriver
from time import sleep


class TestCase(unittest.TestCase):
    def test_01_login(self):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        sleep(5)

    def test_02_login(self):
        print(111222)


if __name__ == '__main__':#并没有执行
    print('运行')
    unittest.main()
