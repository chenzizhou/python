##从selenium中获取浏览器驱动
from selenium import webdriver
from selenium.webdriver import ActionChains
##从time中获取sleep方法
from time import sleep

##获取谷歌的驱动
driver=webdriver.Chrome()

##设置浏览器窗口大小
##driver.set_window_size(900,400)

##获取浏览器窗口大小
print(driver.get_window_size())
##定义变量，如不是数字类型，变量值需引号
url="http://www.126.com"
##url1='https://mail.163.com/register/index.htm?from=126mail&utm_source=126mail'
##浏览器地址栏输入
driver.get(url)
sleep(1)
driver.maximize_window()##设置最大窗口模式
login=driver.current_window_handle#获取当前页的句柄
name='nature_simple'
password='czr199764'
tel=15587621808

#登录
driver.switch_to.frame(0)

##跳出框架
##driver.switch_to.default_content()

driver.find_element_by_name("email").send_keys(name)
driver.find_element_by_id("pwdtext").send_keys(password)
driver.switch_to.default_content()
try:
    driver.find_element_by_xpath('//*[@id="dologin"]').click()
except Exception as e:
    print(e)
##driver.find_element_by_link_text("登  录").click()


sleep(1)##休眠

##driver.find_element_by_id("dologin").click()
#driver.find_element_by_id("idInput").send_keys("1096059759")
#driver.find_element_by_xpath("//*[@id='auto-id-1624978027420']").clear()
#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys("1096059759")
##sleep(5)
##driver.quit()

#跳转到注册页面，当实际未定位到当前页
driver.find_element_by_link_text("注册网易邮箱").click()

##只限于在一个网页中浏览过的网页进行切换（坑点）
##driver.back()

driver.refresh()##刷新当前页面

##关闭当前句柄
##driver.close()

##按照窗口索引定位到当前页
##login=driver.window_handles[0]

##获取列表中最后一个句柄
register=driver.window_handles.pop()

##定位到注册界面
driver.switch_to.window(register)

##圈定可能出现异常的地方，报错抛出异常，给与提示及解决方式，程序依照代码从下倒下按照逻辑执行
try:
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/input").send_keys(name)
##接受异常，子异常对象可以被父对象接受(BaseException是所有异常对象的基类)
except BaseException as e:
    print(e/n)
    print('重新编辑代码！')
finally:
##获取到当前浏览器所有页面的句柄
##all_handles=driver.window_handles

##依次取出所有句柄
##for handle in all_handles:
##    if handle!=login:
##        register=handle
##        driver.switch_to.window(register)
##        print('now register window!')
##        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/input").send_keys(name)

    
##sleep(3)
##driver.find_element_by_css_selector('#username').send_keys(name)
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/input").send_keys(name)
##driver.find_element_by_id("usrname").send_keys(name)
    print('程序还在进行吗？')
sleep(1)
driver.find_element_by_css_selector('input#password').send_keys(password)
sleep(1)
driver.find_element_by_id('phone').send_keys(tel)

##print('关闭当前定位界面')
##driver.close()
##try:
##    driver.switch_to.window(register)
##except Exception as e:
##    print(e)
##    print("你所切换的页面已经被你关闭啦，不好意思，请重新driver.get(url)")
##print('程序还在进行吗？')

##try:   
##    driver.close()
##except Exception as e:
##    print(e)
##    print('浏览器close关闭一个页面后，不会定位到下一个页面')
##finally:
##    print('但可以使用quit()关闭浏览器呀')
##    sleep(2)  
##关闭所有浏览器页面    
##driver.quit()
try:
    hk=driver.find_element_by_css_selector('.yidun_cover-frame')
    driver.switch_to.frame(hk)
    action=ActionChains(driver)
    action.click_and_hold(driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]')).perform()
    action.reset_actions()
    action.move_by_offset(180, 0).perform()  # 移动滑块
except Exception:
    print('请继续')
print('好的')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[4]/span').click()
sleep(30)

driver.find_element_by_link_text('立即注册').click()

