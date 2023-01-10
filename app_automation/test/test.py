# 作者
# NATURE
# 日期
# 2023/1/9 17:56
# 功能
#
import time

import xlrd2


def get_dd_user():
    x = xlrd2.open_workbook('../data/dd_user_info.xlsx')
    s = x.sheet_by_index(0)
    peoples=[]
    for i in range(1, s.nrows):
        p={}
        p['name'],p['password']=name, password = s.row_values(i)
        peoples.append(p)
    print(peoples)
    return peoples
get_dd_user()
print(time.ctime())
import datetime
from chinese_calendar import is_workday
date = datetime.datetime.now().date()
print(date)
date = datetime.datetime(2022, 9, 4)
print(date)
if is_workday(date):
  print("是工作日")
else:
  print("是休息日")