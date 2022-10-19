# 作者
# NATURE
# 日期
# 2022/10/19 16:24
# 功能
#
import multiprocessing
import threading
from time import sleep

from selenium import webdriver
def djc_baidu(browser):
    driver='webdriver.'+browser+'()'
    driver=eval(driver)
    sleep(2)
    driver.get('http://www.baidu.com')
    sleep(2)
    driver.find_element_by_id("kw").send_keys("remote")
    sleep(2)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()
browser=['Chrome', 'Firefox','Edge']
processes=[]
for b in browser:
    p=multiprocessing.Process(target=djc_baidu,args=(b,))
    processes.append(p)
if __name__=='__main__':
    #启动线程
    for p in processes:
        p.start()
    for p in processes:
        p.join()