# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
import pytest


class TestPytest:
    def test_pytest(self):
        print('测试pytest002')

    @pytest.mark.smoke
    def test_pytest_ini(self):
        print('测试pytest_ini')


@pytest.mark.skip
def test_func():
    print('指点函数')


if __name__ == '__main__':
    pytest.main(['-sv','-m=smoke','--html=../report/report.html'])
