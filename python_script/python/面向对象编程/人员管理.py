# 
L=[
{
'name':'nature',
'age':'24'
},
{
'name':'simple',
'age':'25'
},
{
'name':'proud',
'age':'1'
}
]
def show(L):
    print(
'''
-----------------------   
|   name   |    age   | 
-----------------------''')
    if len(L):   
            for l in L:
                print('''|%10s|%10s|'''%(l['name'],l['age'])
                    )  
            print('''-----------------------   
            ''')
            input("Press on 'enter' going on!")
def delete_by_name(name):
    for l in L:
        if l['name']==name:
            L.remove(l)
def update_age(name,age):
    for l in L:
        if l['name']==name:
            l['age']=age
def sort_by_age_h_l():
    L1=L.copy()
    L1.sort(key=lambda x:x['age'],reverse=True)
    print(L1)
    show(L1)
def sort_by_age_l_h():
    L1=sorted(L,key=lambda x:x['age'],reverse=False)
    print(L1)
    show(L1)
while True:
    print("""
    +--------------------------------+
    | 1)添加学生信息                 |
    |                                |
    | 2)显示所有学生的信息           |
    |                                |
    | 3)删除学生信息                 |
    |                                |
    | 4)修改学生成绩                 |
    |                                |
    | 5)按学生成绩高-低显示学生信息  |
    |                                |
    | 6)按学生成绩低-高显示学生信息  |
    |                                |
    | 7)按学生年龄高-低显示学生信息  |
    |                                |
    | 8)按学生年龄低-高显示学生信息  |
    |                                |
    | 9)退出                         |
    +--------------------------------+""")
    choice=input("please your play choice?")
    if choice=='1':
        name=input('put name:')
        age=input('put age:')
        L.append({'name':name,'age':age})
    elif choice=='2':
        show(L)
    elif choice=='3':
        name=input('put your deleting people:')
        delete_by_name(name)
    elif choice=='4':
        name=input('put your update people:')
        age=input('put your update age:')
        update_age(name,age)
    elif choice=='5':
        sort_by_age_h_l()
    elif choice=='6':
        sort_by_age_l_h()
    elif choice=='q':
        break