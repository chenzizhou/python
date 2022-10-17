# 作者
# NATURE
# 日期
# 2022/10/17 15:48
# 功能
#
import os
def get_new_file():
    l=os.listdir('../report')
    print(l)
    l.sort(key=lambda x:os.path.getmtime('../report/'+x))
    print(l)
    return '../report/'+l[-1]