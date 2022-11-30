# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
from time import sleep

import pytest


class TestPytest:
    age = 18

    # @pytest.mark.run(order=3),需导入pytest-ordering
    # 作用：按照自定义顺序执行
    @pytest.mark.run(order=3)
    def test_pytest(self):
        print('测试pytest')
        assert 1 == 2

    @pytest.mark.run(order=1)
    def test_pytest01(self):
        print('测试pytest001')

    @pytest.mark.run(order=2)
    def test_pytest02(self):
        print('测试pytest002')

    @pytest.mark.run(order=4)
    def test_pytest04(self):
        print('测试pytest004')

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    def test_pytest03(self):
        print('测试pytest003')

    @pytest.mark.smoke
    @pytest.mark.skipif(age >= 19, reason='已成年')
    @pytest.mark.run(order=6)
    def test_pytest_ini(self):
        print('测试pytest_ini')


if __name__ == '__main__':
    pytest.main(['-vs', '../testcase/test_pytest001.py', '--reruns=2'])
