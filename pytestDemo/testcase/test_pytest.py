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


if __name__ == '__main__':
    pytest.main(['-sv'])
