# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/13 15:30
# 功能：
b = '陈自然'.encode(encoding='utf-8')
print(b)
print(b.decode())

ba = bytearray('abcd',encoding='utf-8')
ba[0]=0xe9
print(ba)
ba[1:2]=b'BDP'
print(len(ba))
print(ba[0])
