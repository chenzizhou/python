# 作者
# NATURE
# 日期
# 2022/10/18 14:35
# 功能
#
import threading
from time import sleep

from selenium import webdriver
def dxc_baidu(browser):
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
threads=[]
for b in browser:
    t=threading.Thread(target=dxc_baidu,args=(b,))
    threads.append(t)
if __name__=='__main__':
    #启动线程
    for t in threads:
        t.start()
    for t in threads:
        t.join()
