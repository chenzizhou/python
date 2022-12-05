import unittest

from ddt import ddt, data, unpack

from web自动化.外勤.pageobject.gd_page import WxgdPage
# @ddt,@data,@unpack
#装饰性函数，使用数据驱动，多次执行用例
# data里面装测试数据，unpack进行解包，针对列表、元组，解包元素对应测试用例参数也要有对应形参接收
@ddt
class TestGdgl(unittest.TestCase):
    @data(('bhcs','123456'))
    @unpack
    def test_wxgd(self,username,password):
        try:
            g = WxgdPage()
            g.save_wxsb(username, password)
        except Exception as e:
            print(e)
        finally:
            pass
            # g.close()


if __name__ == '__main__':
    unittest.main()
