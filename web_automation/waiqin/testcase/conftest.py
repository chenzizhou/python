# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/2 21:58
# 功能：配置当前包下所用夹具
import pytest
@pytest.fixture(scope='class',params=['nature', 'czr', 'simple'])
def my_fixture(request):
    print('前置')
    yield request.param
    print('后置')
