# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
import os

import pytest



class TestPytest:
    def test_pytest(self, my_fixture):
        print('测试pytest002')

    @pytest.mark.smoke
    def test_pytest_ini(self):
        print('测试pytest_ini')


def test_pytest(my_fixture):
    print('测试pytest002', my_fixture)


class aaaaPytest:

    @pytest.mark.smoke
    def test_pytest_ini(self):
        print('测试pytest_ini')


@pytest.mark.skip
def test_func():
    print('指点函数')


if __name__ == '__main__':
    pytest.main(['-sv', '--alluredir=./temp'])
    # 此处用的allure绝对路径，path不生效
    os.system(r'F:\allure-2.20.1\bin\allure.bat generate temp -o ./report --clean')
