# coding=utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：内置标记使用
import pytest


# pytest -vs .\testcase\test_pytest_内置标记.py


# # 要参数化模块中的所有测试，你可以给全局变量pytestmark赋值
# pytestmark = pytest.mark.parametrize("username,password", [('c60068129', 'Czr1234567890/'),
#                                                            (1, 1), ])  # username和password是变量名，后面是他们的值，多组数据用逗号隔开
# 测试def test_pytestmark_error
class TestPytest:
    @pytest.mark.xfail  # 内置xfail标记
    def test_inner_mark(self):
        assert 1 == 2
        print('测试内置标记xfail')

    @pytest.mark.parametrize('a', ['测试内置标记parametrize',
                                   pytest.param("测试内置标记xfail001", marks=pytest.mark.xfail)])  # 参数化内置标记
    def test_inner_mark_type(self, a):
        print(a)
        print('测试内置标记parametrize')

    # 4组
    # 多个参数化参数的所有组合
    @pytest.mark.parametrize("x", [0, 1])
    @pytest.mark.parametrize("y", [2, 3])
    def test_foo(self, x, y):
        print(x, y)

    # 1组
    # 全局pytestmark无法应用不到改测试方法上，且用例调用失败，因为参数对应不上
    # def test_pytestmark_error(self):
    #     pass


# https://github.com/allure-framework/allure2/releases
if __name__ == '__main__':
    # 1.主函数模式
    # (1)# 运行当前目录下的所有测试
    # pytest.main()
    # (2)指定模块:
    # pytest.main(['-vs', 'test_login.py'])
    # (3)指定目录: pytest.main(['-vs" ,'. /interface_testcase'])
    # (4)通过nodeid指定用例运行:nodeid由模块名, 分隔符，类名，方法名，函数名组成。
    pytest.main(['-vs', '.\\testcase\\test_pytest.py::TestPytest::test_parametrize_single'])
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
