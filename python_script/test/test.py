from calculator import Count
import unittest
class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_add(self) :
        j= Count (2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j=Count(41,76)
        self.assertEqual(j.add(),117)
    def tearDown(self):
        print("test end")
    def add(self):
        print('可以吗？')
        
if __name__== '__main__':
## main方法只执行本模块以test开头的方法   
##    unittest.main()
##构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestCount('test_add'))
    ##    
    runner=unittest.TextTestRunner()
    runner.run(suite)
