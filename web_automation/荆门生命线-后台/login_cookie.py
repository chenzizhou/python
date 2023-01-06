# 作者
# NATURE
# 日期
# 2023/1/6 17:41
# 功能
#
from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
# driver.add_cookie({'name':'pai_token',
#                    'value':'fbc8948d-1043-3e22-9110-58d5a9d8d972'})
# driver.add_cookie({'name':'SSITGTOKEN',
#                    'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJhZG1pbiIsInNjb3BlIjpbInNlcnZlciJdLCJleHAiOjE2NzMwODIyNjgsImRlcHRfaWQiOjEwMCwiYXV0aG9yaXRpZXMiOlsiKjoqOioiLCJhZG1pbiJdLCJqdGkiOiI5YmExNzFlNi1kZDNjLTQ4Y2QtYmNlNC1hNmY2ZWM3YmZjYWIiLCJjbGllbnRfaWQiOiJ3ZWIiLCJ1c2VybmFtZSI6ImFkbWluIn0.Hol_T-mqYx7K8eYeuqg08n6HbuuZRJBGTz_BFsQ2nJ4'
#                    })
driver.get('https://lifelinetest.ssitg.com/index')
sleep(10)