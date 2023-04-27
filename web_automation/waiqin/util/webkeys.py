from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from toollib import autodriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


class WebKeys:

    def __init__(self, type_='chrome'):
        global driver
        driver = self.open_windows(type_)
        print(1)

    def open_windows(self, type_):
        if type_.lower() == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        elif type_.lower() == 'ie':
            service = Service(executable_path=IEDriverManager().install())
            driver = webdriver.Edge(service=service)
        elif type_.lower() == 'edge':
            service = Service(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
        else:
            driver_path = autodriver.chromedriver(platform='win64')  # 自动下载驱动（platform默认为win64）
            # 以下为selenium模拟操作
            driver = webdriver.Chrome(service=Service(driver_path))
        return driver

    def open(self, url):
        driver.get(url)

    def select(self, by=None, value=None):
        by = by.upper()
        if by == 'XPATH':
            element = driver.find_element(By.XPATH, value)
        elif by == 'ID':
            element = driver.find_element(By.ID, value)
        elif by == 'NAME':
            element = driver.find_element(By.NAME, value)
        elif by == 'CLASS_NAME':
            element = driver.find_element(By.CLASS_NAME, value)
        elif by == 'TEXT':
            element = driver.find_element(By.PARTIAL_LINK_TEXT, value)
        return element

    def click(self, by, value):
        self.select(by, value).click()

    def send_keys(self,by,value,txt):
        self.select(by,value).send_keys(txt)

    def select_frame(self,id=None,name=None,by=None,value=None):
        if id:
            driver.switch_to.frame(id)
        elif name:
            driver.switch_to.frame(name)
        else:
            driver.switch_to.frame(self.select(by,value))

    def default_frame(self):
        driver.switch_to.default_content()

    def parent_frame(self):
        driver.switch_to.parent_frame()

    def execute_script(self, scripts, by,value):
        driver.execute_script(scripts, self.select(by,value))

    def pause(self, time=1):
        sleep(time)

    def refresh(self):
        driver.refresh()

    def close(self):
        driver.close()
