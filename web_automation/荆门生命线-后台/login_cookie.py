# 作者
# NATURE
# 日期
# 2023/1/6 17:41
# 功能
#
import base64
from time import sleep

import requests
from PIL import Image
import pytesseract

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
# driver.add_cookie({'name':'sidebarStatus',
#                    'value':'0'})
# driver.add_cookie({'name':'pai_token',
#                    'value':'51a2f50b-8146-3722-af2f-f5d42b833cfc'})
# driver.add_cookie({'name':'SSITGTOKEN',
#                    'value':
#                        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJhZG1pbiIsInNjb3BlIjpbInNlcnZlciJdLCJleHAiOjE2NzMyNjM5MDcsImRlcHRfaWQiOjEwMCwiYXV0aG9yaXRpZXMiOlsiKjoqOioiLCJhZG1pbiJdLCJqdGkiOiI5YTIyNzAyZS04ODAxLTQ2ZTktOTg3Yy1hNmM4ZmFlNzY4MTkiLCJjbGllbnRfaWQiOiJ3ZWIiLCJ1c2VybmFtZSI6ImFkbWluIn0.PpPHTBCfqO3UTiQGYlg8lb-POYVUjDV9esqlRkQeTxc'
#                    })
driver.get('https://lifelinetest.ssitg.com/index')

driver.find_element(By.XPATH,'//img/../input[@placeholder="用户名/账号/手机号"]').send_keys('admin')
driver.find_element(By.XPATH,'//img/../input[@placeholder="请输入您的密码"]').send_keys('admin')
element=driver.find_elements(By.XPATH,'//img[@class="code-img"]')[0]
print(element.rect)
# element.screenshot('./picture/yzm.png')
# image = Image.open('./picture/yzm.png')
# image.convert('L')
# image.show()
# content = pytesseract.image_to_string(image)   # 解析图片
# print(content)
sleep(10)





