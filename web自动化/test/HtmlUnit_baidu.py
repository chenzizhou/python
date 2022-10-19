# 作者
# NATURE
# 日期
# 2022/10/18 22:36
# 功能
#
from selenium.webdriver import Remote
from selenium.common.exceptions import WebDriverException

dc = {'browserName': 'htmlunit'}
driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=dc)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("htmlunit")
driver.find_element_by_id("su").click()
driver.get_screenshot_as_file("../common/run_ok.jpg")
driver.quit()
