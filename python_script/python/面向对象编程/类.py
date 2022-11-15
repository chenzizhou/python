class Student(object):
    """学生类"""
    __slots__ = ['name', 'age','__p']

    def __init__(self):
        self.__p = 1

    def __p_m(self):
        return self.__p

    def o_m(self):
        return '实例方法被调用' + '私有变量，私有方法' + str(self.__p_m())

    @classmethod
    def c_m(cls):
        return '类方法被调用！'

    @staticmethod
    def s_m():
        return '静态方法被调用!'


def out_print(lst):
    for i in lst:
        print(i.name, i.age)
        print(getattr(i, 'o_m')())
        print(i.__class__.c_m())
        print(i.s_m())
        print(i.__doc__)
        # print(i.__dict__)#类中存在__slots__属性时，__dict__不可用

        print(i.__class__)
        print(i.__class__.__bases__)
        print(i.__class__.__base__)
        print(i.__class__.__slots__)
        print(i.__class__.__mro__)
        print(isinstance(i, Student))
        print(type(i))


l = []
while True:
    name = input('姓名:')
    if not name:
        break
    age = input('年龄:')
    stu = Student()
    stu.name = name
    stu.age = age
    l.append(stu)
out_print(l)
