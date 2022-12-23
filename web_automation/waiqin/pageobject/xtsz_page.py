# 作者
# NATURE
# 日期
# 2022/12/21 16:23
# 功能
#业务配置
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from web_automation.外勤.pageobject.login_page import LoginPage


class XtpzPage(LoginPage):
    def make_ywpz(self,ywlxs,gws,gs='',username='admin',password='123456'):
        self.login(username,password)
        driver=self.get_driver()
        xtpz = driver.find_elements_by_xpath('//span[@title="系统设置"]')[0]
        # 将业务配置元素滑动到可见位置
        driver.execute_script('arguments[0].scrollIntoView()', xtpz)
        sleep(3)
        ActionChains(driver).move_to_element(xtpz).perform()
        sleep(5)
        elements = driver.find_elements_by_tag_name('span')
        sleep(1)
        for element in elements:
            if element.text == '业务配置':
                print("点击业务配置")
                ActionChains(driver).click(element).perform()
                break
        sleep(2)
        print('进入业务配置')
        # ywlxs=['巡检','养护','检漏','排污稽查']
        for ywlx in ywlxs:
            # 业务配置-查看
            driver.find_element(By.XPATH,r"//td[text()='"+ywlx+"']/../td[3]/div/button[1]").click()
            print("进入业务配置列表")
            driver.find_element_by_xpath('//div[text()="+ 添加类型"]').click()
            sleep(2)
            if gs:
                driver.find_element_by_id('name').send_keys(gs+'-'+ywlx)
                sleep(1)
                driver.find_element_by_id('code').send_keys(gs+'-'+ywlx)
            else:
                driver.find_element_by_id('name').send_keys('测试-'+ ywlx)
                sleep(1)
                driver.find_element_by_id('code').send_keys('测试-'+ ywlx)
            # gws = {'北海供水': ['管段', '阀门', '控制阀门', '消防栓', '水表'],'北海原水': ['管段', '渠道', '阀门', '控制阀门', '消防栓'],}
            for gw in gws.keys():
                for sb in gws[gw]:
                    # 添加作业对象
                    driver.find_element_by_xpath("//label[text()='作业对象']/../button[1]").click()
                    sleep(1)
                    # 点击设备类型
                    driver.find_element_by_xpath('//span[@class="ant-select-selection__rendered"]').click()
                    sleep(1)
                    try:
                        # 选择设备
                        driver.find_element(By.CSS_SELECTOR, "span[title='" + gw + "']+ul span[title='" + sb + "']").click()
                    except Exception as e:
                        print('------------------无'+gw+'-'+sb+'-----------------------')
                        sleep(1)
                        driver.find_element(By.XPATH,"//span/div/button[@type='submit']/../button[@type='button']").click()
                        sleep(1)
                        continue
                    sleep(1)
                    # 作业历史选择
                    driver.find_element(By.XPATH,
                                        "//div[@id='historyRecords']/div/div[@class='ant-select-selection__rendered']").click()
                    sleep(1)
                    driver.find_element(By.XPATH, "//ul[ @role='listbox']/li[text()='设备作业历史']").click()
                    sleep(1)
                    # 到位
                    driver.find_element(By.XPATH, "//span[text()='到位']").click()
                    sleep(1)
                    # 到位半径
                    dwbj=driver.find_element(By.XPATH, "//input[@role='spinbutton']")
                    dwbj.send_keys(Keys.CONTROL,'a')
                    sleep(1)
                    dwbj.send_keys(100)
                    sleep(1)
                    # 是否反馈
                    # driver.find_element(By.XPATH, "//span[text()='反馈']").click()
                    # 设备反馈
                    # driver.find_element(By.XPATH,"//div[@id='equipFeedbackBpm']/div/div[@class='ant-select-selection__rendered']").click()
                    # sleep(2)
                    # 设备流程
                    # driver.find_element(By.XPATH, "//ul[@role='listbox']/li[text()='设备反馈']").click()
                    # sleep(1)
                    # 保存
                    driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                    try:
                        n = 1
                        while driver.find_element(By.XPATH,"//span[text()='作业对象重复,请重新输入']"):
                            driver.find_element(By.XPATH,"//*[@id='objectName']").send_keys(n)
                            n+=1
                            driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                    except Exception as e:
                        pass
                    finally:
                        print(f'{gw}-{sb}已添加！')
                        continue
                print(gw+' 所有设备已添加完毕！')
            driver.find_element_by_xpath('//span/button[1]').click()

