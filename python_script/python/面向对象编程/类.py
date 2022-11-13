class Student(object):
    '''学生类'''

    def s_m(self):
        print('学生methond')
        return '动态方法调用'


def out_print(lst):
    for i in lst:
        print(i.name, i.age)
        print(getattr(i, 's_m')())
        print(i.__doc__)
        print(i.__dict__)
        print(i.__class__)
        print(i.__class__.__bases__)
        print(i.__class__.__base__)
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
