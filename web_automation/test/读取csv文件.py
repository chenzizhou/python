# 作者
# NATURE
# 日期
# 2022/10/14 11:38
# 功能
#
import csv
import os
# print(dir(os.path))
print(__file__)
print(__name__)
print(os.path.dirname(__file__).split('test')[0]+'common\info.csv')
print(list(csv.reader(open(os.path.dirname(__file__).split('test')[0]+'common\info.csv','r'))))

for i in csv.reader(open(os.path.dirname(__file__).split('test')[0]+'common\info.csv','r')):
    print(i)
