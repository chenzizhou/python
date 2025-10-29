import pytest

from pageobject.register_page import RegisterPage


# # 要参数化模块中的所有测试，你可以给全局变量pytestmark赋值
# pytestmark = pytest.mark.parametrize("username,password", [('c60068129', 'Czr1234567890/'),
#                                                            (1, 1), ])  # username和password是变量名，后面是他们的值，多组数据用逗号隔开


class TestRegister:
    # 2组
    # 参数化，多组数据进行测试
    # username和password是变量名，后面是他们的值，多组数据用逗号隔开
    @pytest.mark.parametrize("username,password,pwd1", [('12345', '12345', '12345')])
    def test_register(self, username, password, pwd1, driver):
        rg = RegisterPage(driver)
        rg.register(username=username, password=password, pwd1=pwd1)
        # 检查是否登录成功
        assert "请登录" in driver.page_source, '两次密码不一致'
