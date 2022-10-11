# 作者
# NATURE
# 日期
# 2022/10/11 10:56
# 功能
#
class Person():
    def method(self):
        print('abc')
p=Person()
m=getattr(p,'method')
m()

