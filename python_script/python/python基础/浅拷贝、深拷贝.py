import copy

a = [1, 2, [3, 4], {'a': 1}]  # 原始对象
b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝
e = a[:]  # 能复制序列，浅拷贝

a.append('add1') # 修改对象a
a[2].append('add2') # 修改对象a中的[3,4]数组对象

a[3] = '666'
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('e:', e)
