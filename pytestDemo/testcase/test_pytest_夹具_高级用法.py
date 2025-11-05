# coding=utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
from datetime import datetime

import pytest


# pytest -sv .\testcase\test_pytest_夹具.py
# 夹具：在用例执行之前、执行之后、自动运行代码
@pytest.fixture()  # 让所有用例都使用这个夹具
def f():
    print(datetime.now(), '用例开始执行')
    yield  # yield之前是前置，yield之后是后置。开始执行用例
    print(datetime.now(), '用例执行完毕')


@pytest.fixture(autouse=True)  # 让所有用例都使用这个夹具
def f2(f):  # 夹具中可以调用另一个夹具
    print(datetime.now(), '用例开始执行002')
    yield 'f2传递的数据'  # yield之前是前置，yield之后是后置。开始执行用例。可以传递数据。
    print(datetime.now(), '用例执行完毕002')


class TestPytest:
    def test_use_fixture(self, f):
        print(f)
        print('使用夹具')

    def test_use_fixture001(self, f2):
        print(f2)
        print('使用夹具的第001种方式')

    @pytest.mark.usefixtures('f2')
    def test_use_fixture002(self, f2):
        print(f2)
        print('使用夹具的第002种方式')

    # def test_use_fixture003(self, f3):
    #     print(f3)
    #     print('使用夹具的第003种方式')

    def test_transfer001(self, f, doctest_namespace):
        name = 'nature'
        doctest_namespace['name'] = name
        assert True

    def test_transfer002(self, f, doctest_namespace):
        print(doctest_namespace['name'])
        assert True


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
