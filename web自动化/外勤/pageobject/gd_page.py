# 作者
# NATURE
# 日期
# 2022/10/26 10:40
# 功能
#
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from web自动化.外勤.pageobject.login_page import LoginPage


class WxgdPage(LoginPage):
    # 元素定位
    gdgl_loc=(By.XPATH,r"//span[text()='工单管理']")
    wxgd_loc=(By.XPATH,r"//span[text()='维修工单']")

    wxgd_iframe_loc=(By.XPATH,r"//iframe[@src='/hbp/d/gdzsjmb.htm']")
    xjgd_loc=(By.XPATH,r"//a[text()='新建工单']")

    wxsb_iframe_loc=(By.XPATH,r"//div[@class='layui-laydialog-content']/iframe")
    dzms_loc=(By.XPATH,"//label[contains(text(),'地址描述')]/../div//input")
    lxr_loc=(By.XPATH,"//label[contains(text(),'联系人')]/../div//input")
    lxdh_loc=(By.XPATH,"//label[contains(text(),'联系电话')]/../div//input")
    fylb_loc=(By.XPATH,"//label[contains(text(),'反映类别')]/../div//input")
    fyqy_loc=(By.XPATH,"//label[contains(text(),'反映区域')]/../div//input")
    jjd_loc=(By.XPATH,"//label[contains(text(),'紧急度')]/../div//input")
    yqwgsj_loc=(By.XPATH,"//label[contains(text(),'要求完工时间')]/../div//input")
    yxsb_loc=(By.XPATH,"//label[contains(text(),'影响设备')]/../div//input")
    bz_loc=(By.XPATH,"//label[contains(text(),'备注')]/../div//input")
    xczp_loc=(By.XPATH,"//label[contains(text(),'现场照片')]/..//div[@class='select-text']")
    fj_loc=(By.XPATH,"//label[contains(text(),'附件')]/..//div[@class='select-text']")
    close_loc=(By.XPATH,"//span[text()='关闭']")
    save_loc=(By.XPATH,"//span[text()='保存']")

    def save_wxsb(self,username='admin',password='123456'):
        # 登录
        print('登录')
        self.login(username,password)
        sleep(4)
        # 进入维修工单
        self.move_to_element(self.gdgl_loc)
        sleep(2)
        self.move_to_element(self.wxgd_loc)
        sleep(1)
        print('点击维修工单')
        self.click(self.wxgd_loc)
        # 点击新建工单
        sleep(1)
        self.in_frame(self.wxgd_iframe_loc)
        print('点击新建工单')
        self.click(self.xjgd_loc)
        self.out_frame()
        self.in_frame(self.wxsb_iframe_loc)
        sleep(1)
        self.click(self.dzms_loc)
        ActionChains(self.driver).move_by_offset(500, 200).click()
        sleep(5)
    def close_wxsb(self):
        pass