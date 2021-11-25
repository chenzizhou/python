from selenium import webdriver
# 时间
from time import sleep
##键盘事件
from selenium.webdriver.common.keys import Keys
# 鼠标事件
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from read_ini import ReadIni
from chandao_pakage import chandao
import random
from PIL import Image
import pytesseract
# 获取随机数
# for i in range(5):
#     user_code=''.join(random.sample("1234567890abcdefghijk",4))
#     print(user_code)
driver=webdriver.Chrome()
cd=chandao(driver=driver)
url='http://114.215.149.146:81/zentaopms/www/user-login.html'
username='chenzizhou'
password='YSD@city'
part='login'
cd.login(url,username,password,part)
project_name='内部规划-外勤2.X'
task_name='回归bug，提价bug'
ssign_name='陈自洲'
expected_time='3.5'
cd.write_task(project_name,task_name,ssign_name,expected_time,'write_task')
consumed='3.5'
cd.start_task(consumed,node='start_task')
cd.finish_task(node='finish_task')
driver.close()