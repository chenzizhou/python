# 作者
# NATURE
# 日期
# 2022/10/19 16:24
# 功能
#
import multiprocessing
from time import sleep
from selenium.webdriver import Remote


def djc_grid_baidu(host,browser):
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser,
                                           'version': '',
                                          'javascriptEnabled': True})
    sleep(2)
    driver.get('http://www.baidu.com')
    sleep(2)
    driver.find_element_by_id("kw").send_keys("remote")
    sleep(2)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()


lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
         'http://127.0.0.1:5555/wd/hub': 'firefox',
         'http://192.168.10.196:6666/wd/hub': 'chrome'}
processes = []
for host, browser in lists.items():
    p = multiprocessing.Process(target=djc_grid_baidu, args=(host,browser))
    processes.append(p)
if __name__ == '__main__':
    # 启动线程
    for p in processes:
        p.start()
        print(dir(p))
    for p in processes:
        p.join()

