# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
from time import sleep

import pytest


class TestPytest:
    def test_pytest(self):
        sleep(3)
        print('测试pytest')

    def test_pytest01(self):
        sleep(3)
        print('测试pytest001')

    def test_pytest02(self):
        sleep(3)
        print('测试pytest002')

    def test_pytest03(self):
        sleep(3)
        print('测试pytest003')

    def test_pytest04(self):
        sleep(3)
        print('测试pytest004')


if __name__ == '__main__':
    pytest.main(['-vs', '../testcase/test_pytest001.py', '--reruns=3'])
