# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:30
# 功能：
import pytest

if __name__ == '__main__':
    # -s: 表示输出调试信息，包括print打印的信息
    # -v: 显示更详细的信息
    # -n: 支持多线程或者分布式运 行测试用例。
    # 如: pytest - vs.. / testcase / test_login.py - n
    # --reruns NUM∶失败用例重跑
    # -×∶表示只要要一个用例报错，那么测试停止。
    # --maxfail = 2:出现两个用例失败就停止。
    # -k: 根据测试用例的部分字符串指定测试用例。如: pytest - vs. / testcase - k "ao"
    # pytest.main(['指点参数', '指点模块/指点目录/（指点目录/模块）/（指点目录/指点模块::类名::方法名）','多线程[-n=2]'])
    # 指定用例执行
    # pytest.main(['-vs', '../../web自动化/外勤/testcase/test_pytest002.py::test_func'])
    # 失败用例重跑
    # pytest.main(['-vs', '../testcase/test_pytest001.py','-n=2','--reruns=2'])
    # 执行顺序默认从上到下
    pytest.main(['-s', '../testcase/test_pytest001.py','-m=smoke'])
