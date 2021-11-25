from selenium import webdriver
dr=webdriver.Chrome()
dr.maximize_window()
dr.get('http://www.baidu.com')
##屏幕截图
dr.get_screenshot_as_file('E:/python_script/1.png')
