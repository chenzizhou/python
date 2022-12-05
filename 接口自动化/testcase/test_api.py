# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/4 20:47
# 功能：
import pytest


class TestApi:
    @pytest.mark.parametrize('name1,name2', [['nature', 'simple']])
    def test_api(self, name1,name2):
        print(name1,name2)


if __name__ == '__main__':
    pytest.main(['-vs', './test_api.py'])
