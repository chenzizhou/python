import unittest
import os
class pl_exc(unittest.TestCase):
    def setUp(self):
        print("执行每个方法之前的前置条件")
    def tearDown(self):
        print("执行完每个方法后的操作")
    def test_pl(self):
        path=os.getcwd()+"\\test" 
        suite=unittest.defaultTestLoader.discover(path,'calcu*.py')
        unittest.TextTestRunner().run(suite)
if __name__=='__main__':
    unittest.main()
