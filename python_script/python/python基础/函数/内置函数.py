# 作者
# NATURE
# 日期
# 2022/10/11 10:56
# 功能
#
'''人'''
class Person():
    def method(self):
        '''打印'''
        print('abc')
p=Person()
setattr(p, 'name','nature')
print(p.name)
m=getattr(p,'method')
m()
print(dir(p))

print(Person.method.__doc__)

