from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager  # 需要安装webdriver_manager库

# 设置 WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
login_url = 'http://127.0.0.1:8000/user/login/'
# 打开登录页面
driver.get(login_url)

# 找到用户名和密码输入框
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# 输入用户名和密码
username_field.send_keys("c60068129")
password_field.send_keys("Czr1234567890/")

# 提交登录表单
password_field.send_keys(Keys.RETURN)

# 等待页面加载
time.sleep(5)
print(driver.page_source)  # 打印页面源码，方便调试




