# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/13 16:41
# 功能：
f = open('test.txt', 'wb')
b = '123\n陈自然'.encode(encoding='utf8')
f.write(b)
f.close()
f = open('test.txt', 'rt+',encoding='utf8')
# f = open('test.txt', 'rb')
# 只有文本格式打开时，才能设置encoding，且在python3中，中文编码utf8而不是utf-8
t = f.readline()
# f.seek(2,1)
# 只适合字节读取
t=f.read(2)#根据文本格式读取位数，t代表读取两个字符，b代表两个字节
f.write('123')
f.write('456')
f.seek(0,0)
print(f.read())
f.close()

f = open('test.txt', 'rb')
print(f.read())
f.close()


# f = open('test.txt', 'a+t',encoding='utf8')
f = open('test.txt', 'a+b')
f.seek(-8,1)
t=f.read(3)
# print(t)
print(t.decode('utf8','ignore'))#utf8编码中文字符占三个字节.读取时不能从中间去，否则解析时报错，如果避免报错，解析加上ignore，忽略不完整中文字符字节


