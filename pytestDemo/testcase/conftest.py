# coding: utf-8
# 作者：NATURE
# 开发时间：2022/12/2 21:58
# 功能：是本地的插件库，其中的hook函数和fixture将作用于该文件所在的目录以及所有子目录。
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# pytest前置条件+后置条件的两种写法
# 　　　　1：使用yield关键字来是实现　　推荐使用这种，因为yield关键字能返回函数的值
#        2：使用finc()函数来实现　　　　这种就不能返回返回值了
# (1)scope表示的是被@pytest.fixture标记的方法的作用域。function(默认)，class , module ,package，session.
# (2)params:参数化(支持列表[]，元祖()，字典列表[{},{}]，字典元祖({},{})
# (3)autouse=True :自动使用，默认False
# (4)ids:当使用params参数化时，给每一个值设置一个变量名。意义不大。
# (5)name :给表示的是被@pytest.fixture标记的方法取一个别名。
@pytest.fixture(scope='class', params=['nature', 'czr'], autouse=False, ids=['n', 'c'], name='mf1')
def my_fixture1(request):
    print('前置')
    # 返回值给调用夹具者，需接收
    yield request.param
    print('后置')


@pytest.fixture(scope='class', params=['nature', 'czr'], autouse=False, ids=['n', 'c'], name='mf2')
def my_fixture2(request):
    print('xxxxxxxxxxxxx测试用例的初始化xxxxxxxxxxxxxxxx')

    def fin():  # 尾部这是后置条件，测试用例执行后就会调用这个函数
        print('zzzzzzzzzzzz测试用例的清除zzzzzzzzzzz')

    request.addfinalizer(fin)  # 回调，当我整个包运行完了后回调fin这个方法
    return request.param


@pytest.fixture()  # 夹具，没有设定范围，就代表function范围  url='https://npm.taobao.org/mirrors/chromedriver/113.0.5672.24/chromedriver_win32.zip'
def driver():  # 函数
    # _path = ChromeDriverManager(url='https://chromedriver.storage.googleapis.com',version='113.0.5672.24').install()  # 自动安装 webdriver
    _path = ChromeDriverManager(url='https://chromedriver.storage.googleapis.com').install()  # 自动安装指定版本 webdriver
    return webdriver.Chrome(service=Service(_path))  # 启动浏览器


# 范围共享
@pytest.fixture(autouse=True, scope="session")
def f3():
    print(datetime.now(), '用例开始执行003')
    yield 'f3传递的数据'  # yield之前是前置，yield之后是后置。开始执行用例。可以传递数据。
    print(datetime.now(), '用例执行完毕003')


# pytest_generate_tests 是 pytest 框架中的一个钩子函数，用于动态生成测试用例。这个钩子允许你根据特定的条件或参数组合来生成多个测试实例，从而实现参数化测试。
# 基本用法
# 在pytest中，你可以通过实现pytest_generate_tests钩子来动态生成测试用例。这个钩子通常在conftest.py文件中定义，以便在多个测试文件中共享。

def pytest_generate_tests(metafunc):
    if 'data' in metafunc.fixturenames:
        data_values = [1, 2, 3]
        metafunc.parametrize('data', data_values)
