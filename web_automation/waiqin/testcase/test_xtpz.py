# 作者
# NATURE
# 日期
# 2023/2/9 11:26
# 功能
#
import pytest

from web_automation.waiqin.pageobject.xtsz_page import XtpzPage

@pytest.fixture()
def my_fixture():
    print('测试开始！')

class TestXtpz:
    @pytest.mark.usefixtures('my_fixture')
    def test_xtpz(self):
        url = 'http://10.41.16.20:32091/?ecode=FCG&init=FCG'
        username = 'admin'
        password = '123456'
        file = '../data/ywpz_info.xlsx'
        ywlxs = XtpzPage.get_ywpz_info_by_xlsx(file)
        print(ywlxs)
        x = XtpzPage()
        x.add_ywxf(ywlxs, username=username, password=password)


if __name__=='__main__':
    pytest.main(['-vs','test_xtpz.py'])