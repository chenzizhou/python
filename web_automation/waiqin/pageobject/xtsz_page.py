# 作者
# NATURE
# 日期
# 2022/12/21 16:23
# 功能
#业务配置
from time import sleep

import xlrd2
import yaml
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from web_automation.waiqin.pageobject.login_page import LoginPage
class XtpzPage(LoginPage):
    def add_ywxf(self,ywlxs,gs='',username='admin',password='123456'):
        '''
        :param ywlxs:业务类型
        :param gws: 管网类型
        :param gs: 公司
        :param username: 账号
        :param password: 登录密码
        :return:
        '''
        self.login(username,password)
        driver=self.get_driver()
        xtpz = driver.find_elements(By.XPATH,'//span[@title="系统设置" and text()="系统设置"]')[0]
        # 将业务配置元素滑动到可见位置
        driver.execute_script('arguments[0].scrollIntoView()', xtpz)
        sleep(3)
        ActionChains(driver).move_to_element(xtpz).perform()
        sleep(3)
        elements = driver.find_elements(By.TAG_NAME,'span')
        sleep(1)
        for element in elements:
            if element.text == '业务配置':
                print("点击业务配置")
                ActionChains(driver).click(element).perform()
                break
        sleep(2)
        print('进入业务配置')
        for ywlx,ywxfs in ywlxs.items():
            # 业务配置-查看
            driver.find_element(By.XPATH,r"//td[text()='"+ywlx+"']/../td[3]/div/button[1]").click()
            sleep(1)
            print("进入业务配置列表")
            driver.find_element(By.XPATH,'//div[text()="+ 添加类型"]').click()
            sleep(2)
            for ywxf,gws in ywxfs.items():
                if gs:
                    driver.find_element(By.ID,'name').send_keys(gs+'-'+ywxf)
                    sleep(1)
                    driver.find_element(By.ID,'code').send_keys(gs+'-'+ywxf)
                else:
                    driver.find_element(By.ID,'name').send_keys(ywxf)
                    sleep(1)
                    driver.find_element(By.ID,'code').send_keys(ywxf)
                for gw in gws.keys():
                    for sbxx in gws[gw]:
                        sb,zyls,sfdw,dwfs,dwbj,sffk,sfdwfk,fklc=sbxx
                        # 添加作业对象
                        driver.find_element(By.XPATH,"//label[text()='作业对象']/../button[1]").click()
                        sleep(1)
                        # 点击设备类型
                        driver.find_element(By.XPATH,'//span[@class="ant-select-selection__rendered"]').click()
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
                        driver.find_element(By.XPATH, "//ul[ @role='listbox']/li[text()='"+zyls+"']").click()
                        sleep(1)
                        # 到位
                        if sfdw=='是':
                            driver.find_element(By.XPATH, "//span[text()='到位']").click()
                            sleep(1)
                            # 到位方式
                            driver.find_element(By.XPATH, "//span[text()='"+dwfs+"']").click()
                            # 到位半径
                            dwbj_ele=driver.find_element(By.XPATH, "//input[@role='spinbutton']")
                            dwbj_ele.send_keys(Keys.CONTROL,'a')
                            sleep(1)
                            dwbj_ele.send_keys(dwbj)
                            sleep(1)
                        if sffk=='是':
                            # 是否反馈
                            driver.find_element(By.XPATH, "//span[text()='反馈']").click()
                            if sfdwfk=='是':
                                driver.find_element(By.XPATH, "//span[text()='到位后反馈']").click()
                            # 设备反馈
                            driver.find_element(By.XPATH,"//div[@id='equipFeedbackBpm']/div/div[@class='ant-select-selection__rendered']").click()
                            sleep(2)
                            # 设备流程
                            driver.find_element(By.XPATH, "//ul[@role='listbox']/li[text()='"+fklc+"']").click()
                            sleep(1)
                        # 保存
                        driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                        try:
                            n = 1
                            while driver.find_element(By.XPATH,"//span[text()='作业对象重复,请重新输入']"):
                                driver.find_element(By.XPATH,"//*[@id='objectName']").send_keys(n)
                                sleep(1)
                                n+=1
                                driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                                sleep(1)
                        except Exception as e:
                            pass
                        finally:
                            print(f'{ywlx}-{gw}-{sb}已添加！')
                            # continue
                    print(ywlx+'-'+gw+' 所有设备已添加完毕！')
                # self.add_zydx(ywlx,ywxf,gws)
                driver.find_element(By.XPATH,'//span/button[1]').click()
                sleep(1)
                driver.find_element(By.XPATH,'//div[text()="业务配置"]').click()
                sleep(1)

    def add_zydx(self,ywlx,ywxf,gws):
        driver = self.get_driver()
        for gw in gws.keys():
            for sbxx in gws[gw]:
                sb, zyls, sfdw, dwfs, dwbj, sffk, sfdwfk, fklc = sbxx
                # 添加作业对象
                driver.find_element(By.XPATH, "//label[text()='作业对象']/../button[1]").click()
                sleep(1)
                # 点击设备类型
                driver.find_element(By.XPATH, '//span[@class="ant-select-selection__rendered"]').click()
                sleep(1)
                try:
                    # 选择设备
                    driver.find_element(By.CSS_SELECTOR, "span[title='" + gw + "']+ul span[title='" + sb + "']").click()
                except Exception as e:
                    print('------------------无' + gw + '-' + sb + '-----------------------')
                    sleep(1)
                    driver.find_element(By.XPATH, "//span/div/button[@type='submit']/../button[@type='button']").click()
                    sleep(1)
                    continue
                sleep(1)
                # 作业历史选择
                driver.find_element(By.XPATH,
                                    "//div[@id='historyRecords']/div/div[@class='ant-select-selection__rendered']").click()
                sleep(1)
                driver.find_element(By.XPATH, "//ul[ @role='listbox']/li[text()='" + zyls + "']").click()
                sleep(1)
                # 到位
                if sfdw == '是':
                    driver.find_element(By.XPATH, "//span[text()='到位']").click()
                    sleep(1)
                    # 到位方式
                    driver.find_element(By.XPATH, "//span[text()='" + dwfs + "']").click()
                    # 到位半径
                    dwbj_ele = driver.find_element(By.XPATH, "//input[@role='spinbutton']")
                    dwbj_ele.send_keys(Keys.CONTROL, 'a')
                    sleep(1)
                    dwbj_ele.send_keys(dwbj)
                    sleep(1)
                if sffk == '是':
                    # 是否反馈
                    driver.find_element(By.XPATH, "//span[text()='反馈']").click()
                    if sfdwfk == '是':
                        driver.find_element(By.XPATH, "//span[text()='到位后反馈']").click()
                    # 设备反馈
                    driver.find_element(By.XPATH,
                                        "//div[@id='equipFeedbackBpm']/div/div[@class='ant-select-selection__rendered']").click()
                    sleep(2)
                    # 设备流程
                    driver.find_element(By.XPATH, "//ul[@role='listbox']/li[text()='" + fklc + "']").click()
                    sleep(1)
                # 保存
                driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                try:
                    n = 1
                    while driver.find_element(By.XPATH, "//span[text()='作业对象重复,请重新输入']"):
                        driver.find_element(By.XPATH, "//*[@id='objectName']").send_keys(n)
                        sleep(1)
                        n += 1
                        driver.find_element(By.XPATH, "//span/div/button[@type='submit']").click()
                        sleep(1)
                except Exception as e:
                    pass
                finally:
                    print(f'{ywlx}-{ywxf}{gw}-{sb}已添加！')
                    # continue
            print(f'{ywlx} -{ywxf}-{gw} 所有设备已添加完毕！')

    @staticmethod
    def get_ywpz_info_by_xlsx():
        x = xlrd2.open_workbook('../data/ywpz_info.xlsx')
        ywlxs={}
        s=x.sheet_by_index(0)
        for row in range(1,s.nrows):
            ywlx,ywxf,gw,sb,zyls,sfdw,dwfs,dwbj,sffk,sfdwfk,fklc=s.row_values(row)
            n=row
            while n>0:
                if ywlx:
                    break
                else:
                    ywlx=s.cell_value(n-1,0)
                    # print(ywlx)
                    n=n-1
            n = row
            while n>0:
                if ywxf:
                    break
                else:
                    ywxf=s.cell_value(n-1,1)
                    # print(ywlx)
                    n=n-1
            n = row
            while n>0:
                if gw:
                    break
                else:
                    gw=s.cell_value(n-1,2)
                    # print(ywlx)
                    n=n-1
            print(ywlx, ywxf, gw, sb, zyls, sfdw, dwfs, dwbj, sffk, sfdwfk, fklc)
            if ywlx in ywlxs.keys():
                if ywxf in ywlxs[ywlx].keys():
                    if gw in ywlxs[ywlx][ywxf].keys():
                        ywlxs[ywlx][ywxf][gw].append([sb,zyls,sfdw,dwfs,dwbj,sffk,sfdwfk,fklc])
                    else:
                        ywlxs[ywlx][ywxf][gw]=[[sb,zyls,sfdw,dwfs,dwbj,sffk,sfdwfk,fklc]]
                else:
                    ywlxs[ywlx][ywxf]={gw:[[sb,zyls,sfdw,dwfs,dwbj,sffk,sfdwfk,fklc]]}
            else:
                ywlxs[ywlx]={ywxf:{gw:[[sb,zyls,sfdw,dwfs,dwbj,sffk,sfdwfk,fklc]]}}
        return ywlxs
    @staticmethod
    def get_ywpz_info_by_yaml():
        with open('../data/xtpz.yaml', 'r',encoding="utf-8") as f:
            ywlxs=yaml.load(f,Loader=yaml.FullLoader)
        return ywlxs
if __name__=='__main__':
    ywlxs=XtpzPage.get_ywpz_info_by_xlsx()
    print(ywlxs)
    print(type(ywlxs))
    x = XtpzPage()
    x.add_ywxf(ywlxs)

