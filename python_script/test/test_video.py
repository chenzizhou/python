#coding=utf-8

from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("http://videojs.com")

driver.implicitly_wait(10)

video=driver.find_element_by_xpath('//*[@id="vjs_video_3_html5_api"]')

url=driver.execute_script("return arguments[0].currentSrc;",video)

print(url)

print("start")

video.click()
##
##driver.execute_script("return arguments[0].play()",video)

sleep(15)

print("stop")

driver.execute_script("return arguments[0].pause()",video)

driver.quit()
