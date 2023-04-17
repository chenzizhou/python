class Person:
    a = 1
    b = 2

    def __init__(self):
        self.a = 3
        self.b = 4

    def per_test(self):
        print("per_test")


class Student(Person):
    c = 10
    d = 20

    def __init__(self):
        super(Student, self).__init__()

    def stu_test(self):
        print("stu_test func")

    def per_test(self):
        print("stu_per_test func")


p = Person()
s = Student()
print(Person.__dict__)
print(Student.__dict__)
print(p.__dict__)
print(s.__dict__)
