import unittest

from web自动化.外勤.pageobject.gd_page import WxgdPage


class TestGdgl(unittest.TestCase):
    def test_wxgd(self):
        try:
            username = 'bhcs'
            password = '123456'
            g = WxgdPage()
            g.save_wxsb(username, password)
        except Exception as e:
            print(e)
        finally:
            pass
            # g.close()


if __name__ == '__main__':
    unittest.main()
