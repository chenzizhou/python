# 作者
# NATURE
# 日期
# 2022/10/26 10:40
# 功能
#
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from web自动化.外勤.pageobject.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

class WxgdPage(LoginPage):
    bd_loc=(By.XPATH,r"// div[ @ title = '百度']")
    # 元素定位
    gdgl_loc=(By.XPATH,r"//span[text()='工单管理']")
    wxgd_loc=(By.XPATH,r"//span[text()='维修工单']")
    wxgdjm_loc=(By.XPATH,r"// div[contains(text(), '工单编号') and @class ='ui-th-div ui-jqgrid-sortable']")

    wxgd_iframe_loc=(By.XPATH,r"//iframe[@src='/hbp/d/gdzsjmb.htm']")
    xjgd_loc=(By.XPATH,r"//a[text()='新建工单']")

    wxsb_iframe_loc=(By.XPATH,r"//div[@class='layui-laydialog-content']/iframe")
    gs_loc=(By.XPATH,"//label[contains(text(),'供水或排水')]/../div//input")
    gs_xx_loc=(By.XPATH,"//a[@title='供水']")

    dzms_loc=(By.XPATH,"//label[contains(text(),'地址描述')]/../div//input")
    dt_loc=(By.CSS_SELECTOR,"#map_gc")
    qr_loc=(By.XPATH,"//input[@value='确认']")

    lxr_loc=(By.XPATH,"//label[contains(text(),'联系人')]/../div//input")
    lxdh_loc=(By.XPATH,"//label[contains(text(),'联系电话')]/../div//input")

    fylb_loc=(By.XPATH,"//label[contains(text(),'反映类别')]/../div//input")
    fylb_xx_loc=(By.XPATH,"//a[@title='阀门维修']")

    fyqy_loc=(By.XPATH,"//label[contains(text(),'反映区域')]/../div//input")
    fyqy_xx_loc=(By.XPATH,"//a[@title='工业园区']")

    jjd_loc=(By.XPATH,"//label[contains(text(),'紧急度')]/../div//input")
    yqwgsj_loc=(By.XPATH,"//label[contains(text(),'要求完工时间')]/../div//input")
    yxsb_loc=(By.XPATH,"//label[contains(text(),'影响设备')]/../div//input")
    bz_loc=(By.XPATH,"//label[contains(text(),'备注')]/../div//input")
    xczp_loc=(By.XPATH,"//label[contains(text(),'现场照片')]/..//div[@class='select-text']")
    fj_loc=(By.XPATH,"//label[contains(text(),'附件')]/..//div[@class='select-text']")
    close_loc=(By.XPATH,"//span[text()='关闭']")
    save_loc=(By.XPATH,"//span[text()='保存']")
    qd_loc=(By.XPATH,"//span[text()='启动']")

    def save_wxsb(self,username='admin',password='123456'):
        # 登录
        driver=self.get_driver()
        print('登录')
        self.login(username,password)

        # 显示等待
        WebDriverWait(driver, 5, 20).until(EC.visibility_of_element_located(self.bd_loc))
        # 进入维修工单
        self.move_to_element(self.gdgl_loc)
        sleep(2)
        element=WebDriverWait(driver,5,20).until(EC.visibility_of_element_located(self.wxgd_loc))
        print(self.wxgd_loc)
        self.move_to_element(self.wxgd_loc)
        # sleep(1)
        print('点击维修工单')
        element.click()
        # 点击新建工单
        sleep(1)
        self.in_frame(self.wxgd_iframe_loc)
        WebDriverWait(driver, 1, 20).until(EC.visibility_of_element_located(self.wxgdjm_loc))
        print('点击新建工单')
        self.click(self.xjgd_loc)
        sleep(1)
        self.out_frame()
        self.in_frame(self.wxsb_iframe_loc)
        sleep(1)
        self.click(self.gs_loc)
        sleep(1)
        self.click(self.gs_xx_loc)
        sleep(1)
        self.click(self.dzms_loc)
        self.out_frame()
        print('地图选址界面')
        f=self.loc_elements(self.wxsb_iframe_loc)
        self.in_frame1(f[1])
        sleep(1)
        dt=self.loc_element(self.dt_loc)
        self.move_by_offset(500, 200)
        sleep(2)
        print('选择地址')
        dt.click()
        sleep(2)
        print('点击确定')
        self.click(self.qr_loc)
        sleep(2)
        self.out_frame()
        self.in_frame(self.wxsb_iframe_loc)
        self.send_keys(self.lxr_loc,'测试-nature')
        sleep(1)
        self.send_keys(self.lxdh_loc,'15587621808')
        sleep(1)
        self.click(self.fylb_loc)
        self.loc_element(self.fylb_xx_loc).click()
        self.click(self.fyqy_loc)
        sleep(1)
        self.loc_element(self.fyqy_xx_loc).click()
        self.send_keys(self.jjd_loc,'一般')
        sleep(1)
        # self.click(self.yxsb_loc)
        self.click(self.qd_loc)
        sleep(5)
    def close_wxsb(self):
        pass