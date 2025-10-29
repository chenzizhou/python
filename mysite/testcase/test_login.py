import pytest
from pageobject.login_page import LoginPage





class TestLogin:
    # 2组
    # 参数化，多组数据进行测试
    # username和password是变量名，后面是他们的值，多组数据用逗号隔开
    @pytest.mark.parametrize("username,password", [('c60068129', 'Czr1234567890/'), ('1', '2'), ])
    def test_login(self, username, password, driver):
        lo = LoginPage(driver)
        lo.login(username=username, password=password)
        # 检查是否登录成功
        assert "欢迎" in driver.page_source

    # 1组
    # param1如果没有接受值，该方法会直接报error
    def test_login_again(self, param1):
        print('测试pytestmark')



