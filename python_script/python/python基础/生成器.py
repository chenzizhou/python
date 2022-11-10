# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/10 23:24
# 功能：
def myyield():
    yield 1
    yield 2
    print('over')
t=myyield()
l=[1,2,3]
l1=[4,5,6]
l2=zip(l)
print(l2)
print(list(l2))
print(enumerate(l))
print(list(enumerate(l)))