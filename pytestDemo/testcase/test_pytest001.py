# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
import os
from time import sleep

import allure
import pytest

@allure.feature('pytest测试模块')
class TestPytest:
    age = 18
    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("001") # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    # @pytest.mark.run(order=3),需导入pytest-ordering
    # 作用：按照自定义顺序执行
    @pytest.mark.run(order=3)
    def test_pytest(self):
        print('测试pytest')
        assert 1 == 2

    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("002")  # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    @pytest.mark.run(order=1)
    def test_pytest01(self):
        print('测试pytest001')

    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("002")  # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    @pytest.mark.run(order=2)
    def test_pytest02(self):
        print('测试pytest002')

    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("002")  # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    @pytest.mark.run(order=4)
    def test_pytest04(self):
        print('测试pytest004')

    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("002")  # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    def test_pytest03(self):
        print('测试pytest003')

    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("002")  # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    @pytest.mark.smoke
    # 满足条件，跳过用例
    @pytest.mark.skipif(age >= 19, reason='已成年')
    @pytest.mark.run(order=6)
    def test_pytest_ini(self):
        print('测试pytest_ini')


if __name__ == '__main__':
    pytest.main(['-vs', '../testcase/test_pytest001.py', '--reruns=2','--alluredir','../temp'])
    os.system(r'E:\allure-2.21.0\bin\allure.bat generate ../temp -o ../report --clean')
