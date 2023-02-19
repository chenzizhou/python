# 作者
# NATURE
# 日期
# 2022/10/17 15:48
# 功能
#获取最新测试报告
import os
def get_new_file():
    l=os.listdir('../report')
    print(l)
    #按照文件的生成时间排序，从小到大
    l.sort(key=lambda x:os.path.getmtime('../report/'+x))
    print(l)
    return '../report/'+l[-1]