from sys import argv
import os
path=os.path
print(path)
print(os.path.exists('1.txt'))
script,filename=argv
# 打开文件
f=open(filename,)
# 打印读取文件内容
# f.write('chenziran')
print(f.read())
print(f.read())
# 将读取文件的指针移动文件开头
f.seek(0)
print(f.read())
filename_again=input('输入文件名》')
f=open(filename_again)
# 打印读取文件内容
print(f.read())
f.close()