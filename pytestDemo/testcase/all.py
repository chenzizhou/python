# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:30
# 功能：
import pytest

if __name__ == '__main__':
    # -s: 表示输出调试信息，包括print打印的信息
    # -v: 显示更详细的信息
    # pytest.main(['指点参数', '指点模块/指点目录/（指点目录/模块）/（指点目录/指点模块::类名::方法名）','多线程[-n=2]'])
    # pytest.main(['-vs', '../../web自动化/外勤/testcase/test_pytest002.py::test_func'])
    pytest.main(['-n = 2', '../testcase/test_pytest.py'])
