# 作者
# NATURE
# 日期
# 2023/3/3 15:25
# 功能
#
class A:
    __slots__ = ['name', 'age']
    V = 0

    # 类方法需要使用 @ classmethod装饰器定义
    # 类方法的第一个参数用来绑定类，约定写为cls
    # 类和对象实例都可以调用类方法
    # 类方法不能访问此类创建的对象的属性
    @classmethod
    def get_v(cls):  # 此方法不是实例方法， 是类方法
        return cls.V

    # 静态方法需要使用 @staitcmethod装饰器定义
    # 静态方法与普通函数的定义相同，不需要传入self和cls
    # 静态方法只能凭借该类和实例来调用
    # 静态方法不能访问类变量和实例变量
    @staticmethod
    def myadd(a, b):
        return a + b

    def work(self):
        print('父类')


class B(A):
    def work(self):
        print('子类')


# 类方法调用
print(A.get_v())  # 类直接访问类方法
a = A()
print(a.get_v())  # 类实例访问类方法
print(a.__class__.get_v())  # 获取该实例的类访问类方法
# 静态方法调用
print(A.myadd(100, 200))
print(a.myadd(300, 400))

print(a.__slots__)
a.name = 'nature'
# #类中定义__slots__变量后，类实例无该__dict__属性）
# a.school='123' #类中已定义固定属性，不能出现其他属性
# print(a.__dict__)

b=B()
print(B.__base__)
b.work()
super(B,b).work()


