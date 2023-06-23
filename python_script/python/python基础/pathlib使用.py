import os.path
from pathlib import Path
currentPath = Path.cwd()
homePath = Path.home()
print("文件当前所在目录:%s\n用户主目录:%s" %(currentPath, homePath))
currentPath = Path.cwd()#获取的是绝对路径
# currentPath =r'F:\work\python\python_script\python\python基础'
# currentPath = os.path.curdir#获取的值相对路径
print(type(currentPath))
newPath = currentPath/'python-100'#Path获取路径<class 'pathlib.WindowsPath'>可以和/进行直接拼接
print("新目录为:%s" %(newPath))
newPath.mkdir(exist_ok=True)
newPath.rmdir()
# 5 获取文件所在目录的不同部分字段
txtPath = Path('python-100.txt')
nowPath = txtPath.resolve()
print("文件的完整路径为:%s" % nowPath)
print("文件完整名称为(文件名+后缀名):%s" % nowPath.name)
print("文件名为:%s" % nowPath.stem)
print("文件后缀名为:%s" % nowPath.suffix)
print("文件所在的文件夹名为:%s" % nowPath.parent)
print("文件所在的盘符为:%s" % nowPath.anchor)

# 6 文件、路径是否存在判断
currentPath = Path.cwd() / 'python'
currentPath.rmdir()
print(currentPath)

print(currentPath.exists())  # 判断是否存在 python 文件夹，此时返回 False。
print(currentPath.is_dir())  # 判断是否存在 python 文件夹，此时返回 False。


currentPath.mkdir()  # 创建 python 文件夹。

print(currentPath.exists())  # 判断是否存在 python 文件夹，此时返回 True。
print(currentPath.is_dir())  # 判断是否存在 python 文件夹，此时返回 True。

currentPath = Path.cwd() / 'python-100.txt'

print(currentPath.exists())  # 判断是否存在 python-100.txt 文件，此时文件未创建返回 False。
print(currentPath.is_file())  # 判断是否存在 python-100.txt 文件，此时文件未创建返回 False。

f = open(currentPath,'w')  # 创建 python-100.txt 文件。
f.close()

print(currentPath.exists())  # 判断是否存在 python-100.txt 文件，此时返回 True。
print(currentPath.is_file())  # 判断是否存在 python-100.txt 文件，此时返回 True。

# 7.文件统计以及匹配查找
# 使用 Path.iterdir() 获取当前文件下的所有文件，并根据后缀名统计其个数。
import pathlib
from collections import Counter
currentPath = pathlib.Path.cwd()
gen = (i.suffix for i in currentPath.iterdir())
print(Counter(gen))

import pathlib
from collections import Counter
currentPath = pathlib.Path.cwd()
gen = (i.suffix for i in currentPath.glob('*.txt'))  # 获取当前文件下的所有 txt 文件，并统计其个数。
print(Counter(gen))
gen = (i.suffix for i in currentPath.rglob('*.txt'))  # 获取目录中子文件夹下的所有 txt 文件，并统计其个数。
print(Counter(gen))

