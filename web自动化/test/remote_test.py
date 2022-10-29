# 作者
# NATURE
# 日期
# 2022/10/18 10:22
# 功能
#
from time import sleep

from selenium.webdriver import Remote

# 定义主机与浏览器
lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
         'http://127.0.0.1:5555/wd/hub': 'firefox',
         'http://192.168.10.196:6666/wd/hub': 'chrome'}

# 调用 Remote方法
# 通过不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser, 'version': '',
                                          'javascriptEnabled': True})
    driver.get('http://www.baidu.com')
    sleep(2)
    driver.find_element_by_id("kw").send_keys("remote")
    sleep(2)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()
