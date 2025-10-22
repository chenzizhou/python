import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 需要安装webdriver_manager库

from pageobject.login_page import LoginPage


class TestLogin():
    @pytest.mark.parametrize("username,password", [('c60068129', 'Czr1234567890/'), (1, 1), (2, 2)])
    def test_login(self, username, password):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        l = LoginPage(driver)
        l.login(username=username, password=password)
