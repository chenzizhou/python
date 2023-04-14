# coding=utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
import os
from time import sleep

import allure
import pytest


@allure.feature('pytest测试模块')  # 一级标题
class TestPytest:
    @allure.story("测试001")  # 二级标签（每个接口的标签）
    @allure.title("001")  # 标题，每个用例带个标题（报告体现在每个测试用例）(一个接口有几个用例，title用例的标签)
    @pytest.mark.skipif(1 == 0, reason='True')  # 满足条件跳过
    def test_pytest(self, mf2):  # 调用夹具的第一种方式
        sleep(3)
        print(f'{mf2}测试pytest')

    @pytest.mark.run(order=1)
    # 标记 冒烟测试用例
    @pytest.mark.smoke
    # 调用夹具的第二种方式
    @pytest.mark.usefixtures('mf2')
    # 跳过测试用例
    @pytest.mark.skip(reason='cool')
    def test_pytest_ini(self):
        sleep(3)
        print('测试pytest_ini')

    @pytest.mark.smoke
    def test_baidu(self, driver):
        driver.get('http://www.baidu.com')
        print('夹具生成浏览器驱动')


# https://github.com/allure-framework/allure2/releases
if __name__ == '__main__':
    # 1.主函数模式
    # (1)运行所有:
    pytest.main()
    # (2)指定模块: pytest.main(['-vs', 'test_login.py'])
    # (3)指定目录: pytest.main(['-vs" ,'. / interface_testcase'])
    # (4)通过nodeid指定用例运行:nodeid由模块名, 分隔符，类名，方法名，函数名组成。
    # pytest.main([-vs' ,'. / interface_testcaseltest_interface.py::test_04_func'])
    # pytest.main(['-vs', './interface_testcase/test_interface.py::TestInterface.test_03_zhiliao')
    # 2.命令行模式
    # (1)运行所有: pytest
    # (2)指定模块: pytest - vs
    # test_login.py
    # (3)指定目录: pytest - vs ./Jinterface_testcase
    # (4)指定目录: pytest - vs ./jinterface_testcase / test_interface.py.test_04_func
    # 参数详解∶
    # -s∶表示输出调试信息，包括print打印的信息
    # -v∶显示更详细的信息
    # -vs∶这两个参数一起用
    # -n: 支持多线程或者分布式运行测试用例。
    # 如: pytest -vs../testcase/test_login.py - n 2
    # --reruns NUM∶失败用例重跑
    # -x∶表示只要要一个用例报错，那么测试停止。
    # --maxfail = 2 出现两个用例失败就停止。
    # --k: 根据测试用例的部分字符串指定测试用例。如: pytest - vs. / testcase - k "ao"
    # --html./report report.html: 生成html的测试报告。
    # –strict选项，遇到拼写错误的标记或未注册的标记就会报错。并且在pytest.ini里注册了标记，但是没有函数使用该标记，也会报错。
    # --alluredir 文件夹

    # pytest.main(['-sv','test_pytest.py','-m','smoke'])
    # pytest.main(['-sv','test_pytest.py','-m','smoke'])
    # pytest.main(['-sv', 'test_pytest.py', '-n', '3', '--alluredir', '../report/temp'])
    # os.system(r'E:\allure-2.21.0\bin\allure.bat generate ../report/temp -o ../report/report --clean')
