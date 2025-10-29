# coding=utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
from datetime import datetime

import allure
import pytest


# pip install allure-pytest
# 下载allure https://www.allure-framework.org/
# 添加到系统变量中，重启pycharm
# pytest -sv --alluerdir=temps --clean-alluredir .\testcase\test_pytest_插件_allure.py
# allure generate -o report -c temps


class TestPytest:
    def test_use_allure001(self):
        print('使用test_use_allure001')

    # allure支持对用例进行分组和关联。使用相同装饰器的用例，自动并入一组
    @allure.epic('我的项目/史诗')
    @allure.feature('我的模块/主题')
    @allure.story('我的功能/故事')
    @allure.title('我的用例/标题')
    def test_use_allure002(self):
        print('使用test_use_allure002')


# https://github.com/allure-framework/allure2/releases
if __name__ == '__main__':
    # 1.主函数模式
    # (1)运行所有:
    # pytest.main()
    # (2)指定模块:
    # pytest.main(['-vs', 'test_login.py'])
    # (3)指定目录: pytest.main(['-vs" ,'. /interface_testcase'])
    # (4)通过nodeid指定用例运行:nodeid由模块名, 分隔符，类名，方法名，函数名组成。
    pytest.main(['-vs', 'test_pytest.py::TestPytest::test_parametrize_single'])
    # pytest.main(['-vs', './interface_testcase/test_interface.py::TestInterface.test_03_zhiliao')
    # 2.命令行模式
    # (1)运行所有: pytest
    # (2)指定模块: pytest - vs
    # test_login.py
    # (3)指定目录: pytest - vs ./Jinterface_testcase
    # (4)指定目录: pytest - vs ./jinterface_testcase/test_interface.py.test_04_func
    # 参数详解∶
    # -s∶表示输出调试信息，包括print打印的信息
    # -v∶显示更详细的信息
    # -vs∶这两个参数一起用
    # -n: 支持多线程或者分布式运行测试用例。
    # 如: pytest -vs../testcase/test_login.py - n 2
    # --reruns NUM∶失败用例重跑
    # -x∶表示只要要一个用例报错，那么测试停止。
    # --maxfail = 2 出现两个用例失败就停止。
    # --k: 根据测试用例的部分字符串指定测试用例。如: pytest - vs ./testcase - k "ao"
    # --html./report report.html: 生成html的测试报告。
    # –strict选项，遇到拼写错误的标记或未注册的标记就会报错。并且在pytest.ini里注册了标记，但是没有函数使用该标记，也会报错。
    # --alluredir 文件夹

    # pytest.main(['-sv','test_pytest.py','-m','smoke'])
    # pytest.main(['-sv','test_pytest.py','-m','smoke'])
    # pytest.main(['-sv', 'test_pytest.py', '-n', '3', '--alluredir', '../report/temp'])
    # os.system(r'E:\allure-2.21.0\bin\allure.bat generate ../report/temp -o ../report/report --clean')
