# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/15 18:52
# 功能：
import unittest

discover=unittest.defaultTestLoader.discover('./','test*.py')
if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(discover)