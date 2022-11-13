class Student:
    pass

def out_print(lst):
    for i in lst:
        print(i.name,i.age)
l=[]
while True:
    name=input('姓名:')
    if not name:
        break
    age=input('年龄:')
    stu=Student()
    stu.name=name
    stu.age=age
    l.append(stu)
out_print(l)        
