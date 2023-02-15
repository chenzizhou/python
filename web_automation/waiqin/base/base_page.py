# 作者
# NATURE
# 日期
# 2022/10/11 21:12
# 功能
# 基础层：封装selenium原生方法
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    jm_loc=(By.XPATH,"//button[text()='登录']")
    def __init__(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        # 设置窗口大小
        driver.set_window_size(1550, 848)
        sleep(1)
        driver.maximize_window()
    def get(self,url):
        driver.get(url)
        # 显示等待
        WebDriverWait(driver, 3, 20).until(EC.visibility_of_element_located(self.jm_loc))
        # 刷新当前界面，清除历史数据
        driver.refresh()
        WebDriverWait(driver, 3, 20).until(EC.visibility_of_element_located(self.jm_loc))
    def loc_element(self, loc):
        return driver.find_element(*loc)

    def loc_elements(self, loc):
        return driver.find_elements(*loc)

    def move_to_element(self, loc):
        return ActionChains(driver).move_to_element(self.loc_element(loc)).perform()

    def send_keys(self, loc, value):
        return driver.find_element(*loc).send_keys(value)

    def click(self, loc):
        return driver.find_element(*loc).click()

    def get_driver(self):
        return driver

    def in_frame(self, loc):
        return driver.switch_to.frame(self.loc_element(loc))

    def in_frame1(self, element):
        return driver.switch_to.frame(element)

    def out_frame(self):
        return driver.switch_to.default_content()

    def execute_script(self, scripts, loc):
        return driver.execute_script(scripts, self.loc_element(loc))

    def move_by_offset(self, x, y):
        return ActionChains(driver).move_by_offset(x, y).perform()

    def close(self):
        return driver.close()

    def quit(self):
        return driver.quit()

    def find_element_by_xlsx(self, xlsx_data_dwmc):
        dwfs = xlsx_data_dwmc[0]
        dwz = xlsx_data_dwmc[1]
        if dwfs == 'XPATH':
            element = driver.find_element(By.XPATH, dwz)
        elif dwfs == 'ID':
            element = driver.find_element(By.ID, dwz)
        elif dwfs == 'NAME':
            element = driver.find_element(By.NAME, dwz)
        elif dwfs == 'CLASS_NAME':
            element = driver.find_element(By.CLASS_NAME, dwz)
        elif dwfs == 'TEXT':
            element = driver.find_element(By.PARTIAL_LINK_TEXT, dwz)
        return element
