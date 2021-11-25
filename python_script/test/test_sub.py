import unittest
from calculator import Count
class test_sub(unittest.TestCase):
    def test_sub(self):
        i=Count(4,2).sub()
        print(i)
if __name__=='__main__':
    unittest.main()
