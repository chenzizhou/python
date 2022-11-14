# name=input('请输入名字:')
# age=input('请输入年龄:')
# print('%s今年%s岁'%(name,age))
# 2
# a=input('put a word:')
# j=0
# for i in a:
#     if i==' ':
#         j+=1
# print(j)

# 3
# a=input('put a word:')
# j=0
# i=0
# while True:
#     if i<len(a):
#         if a[i]==' ':
#             j+=1
#             i+=1 
#         else:
#             i+=1 
#     else:
#         print(j)
#         break
# 4
# a=input('put a word:')
# j=0
# for i in a:
#     if i==' ':
#         j+=1
# print(j)

# 5
# i=65
# while i<91:
#     if i%2!=0:
#         print(chr(i),end=' ')
#         i+=1
#     else:
#         print(chr(i).lower(),end=' ')
#         i+=1

# 6
# c=n=int(input('put a number:'))
# i=1
# l=1
# while l<=c:
#     while i<=n:
#         print(i,end=' ') 
#         i+=1
#     else:
#         print()
#         i=l=l+1
#         n+=1

# 7
# sum=0
# for i in range(1,101):
#     if i%5!=0 and  i%7!=0 and i%11!=0:
#         sum+=i        
#     else:
#         continue        
# print(sum)


# n=int(input('put a number:'))
# i=1
# while n>0:
#     print(' '*(n-1)+'*'*i)
#     n-=1
#     i+=1


# n=int(input('put a number:'))
# # i=1
# i=1
# a=1
# while i<=n:
#     print(('*'*(2*i-1)).center(2*n-1))
#     i+=1
# else:
#     while a<=n:
#         print('*'.center(2*n-1))
#         a+=1


# weeks={'1': 'monday','2':'tuesday','3':'wednesday','4':'thursday','5':'friday','6':'saturday','7':'sunday'}
# day=input('put a number(1-7):')
# print(weeks[day]) 

# print(dict([[1,2],[3,4]]))


# l=['nature','chenziran','155887621808']
# L={x:len(x) for x in l}
# print(L)
# print(l)
   
# print(L)

# no=[1,2,3,4]
# names=['nature','simple','cute','love']
# l={x:y for x in no for y in names}
# print

#三角形打印
# n=int(input('put a number:'))
# def print_triangle(n):
#     l=list(range(1,n+1))
#     for i in l:
#         l1=list(range(1,i+1))
#         l2=list(reversed(l1))
#         del l2[0]
#         l1.extend(l2)
#         j=1
#         s=''
#         for x in l1:
#             if j!=0:
#                 s=s+str(x)
#                 j+=1
#         print(s.center(2*n-1))
# print_triangle(n)

# 菱形打印
# n=int(input('put a number:'))
# def print_diamond(n):
#     l=list(range(1,n+1))
#     L=list(reversed(list(range(1,n))))
#     l_sum=[l,L]
#     for I in l_sum:
#         for i in I:
#             l1=list(range(1,i+1))
#             l2=list(reversed(l1))
#             del l2[0]
#             l1.extend(l2)
#             j=1
#             s=''
#             for x in l1:
#                 if j!=0:
#                     s=s+str(x)
#                     j+=1
#             print(s.center(2*n-1))
# print_diamond(*[n])


# a=[]
# b=list()
# print(a,b)
# c=tuple()
# d=()
# print(c,d)
# e={}
# f=dict()
# print(e,f)
# g=set()
# print(g)
# d={'name':'nature','age':'24'}
# s=set(d)
# print(s)
# d1={'name','nature','24'}

# L1=[x for x in map(lambda x,y:x+y,[1,2,3,4],[5,6,8])]

# print(list(filter(lambda x:x%2!=0,L1)))


# D=[{" name": "Green" ,"age": 30},{"name":"11Bob","age":25}]
# print(sorted(D,key=lambda x:x["age"]))

# def myfac(x):
#     if x==1:
#         return 1
#     return x*myfac(x-1)
# def sumfac(n):
#     sum=0
#     for x in range(1,n+1):
#         sum=myfac(x)+sum
#     print(sum)

# print(sum(map(myfac,range(1,4))))



# L=[[3,5,8],10,[[13,14],15],18]

# print(type(L)==type(list()))
# l=[]**
# def print_list(lst):
#     for i in lst:
#         if type(i)!=type(list()):
#             l.append(i)
#             print(i)
#         elif type(i)==type(list()):
#             print_list(i)
#     return l
# # print_list(L)


# def sum_list(lst):
#     return sum(print_list(lst))

# print(sum_list(L))


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
},



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



