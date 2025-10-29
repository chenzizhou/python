# conftest.py
from datetime import datetime

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def abc():
    return []


@pytest.fixture()
def driver():
    print(datetime.now(), '用例开始执行')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver  # yield之前是前置，yield之后是后置。开始执行用例。可以传递数据。
    print(datetime.now(), '用例执行完毕')
    driver.quit()
