# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/9 23:15
# 功能：
import random

l = [1, 2, 4, 5]
print(random.sample(l, 2))
print(random.randint(1, 10))
print(random.uniform(1, 10))
try:
    if 1 == 2:
        raise AssertionError('123')
except Exception as e:
    print(e)

# assert 1 == 2, '不等于'
