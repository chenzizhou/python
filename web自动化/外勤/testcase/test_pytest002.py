# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/27 16:19
# 功能：
import pytest

print('类之前')


class TestPytest:
    def test_pytest(self,my_fixture):
        print('测试pytest002')

    @pytest.mark.smoke
    def test_pytest_ini(self):
        print('测试pytest_ini')


class aaaaPytest:
    def test_pytest(self, my_fixture):
        print('测试pytest002', my_fixture)

    @pytest.mark.smoke
    def test_pytest_ini(self):
        print('测试pytest_ini')


@pytest.mark.skip
def test_func():
    print('指点函数')


if __name__ == '__main__':
    pytest.main(['-sv'])
