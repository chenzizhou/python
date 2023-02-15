# 作者
# NATURE
# 日期
# 2023/2/10 16:56
# 功能
#
import datetime
import sys
import os
# 将当前工作目录下的文件夹都加入系统模块搜索路径
path=os.getcwd().split('\\')[0]
for i in range(0,len(os.getcwd().split('\\'))-1):
    if i==0:
        path = path
        sys.path.append(path)
    else:
        path=path+'/'+os.getcwd().split('\\')[i]
        sys.path.append(path)
from app_automation.pageobject.dddk_class import Dd
i=sys.argv[1]
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '启动程序')
dk_types = ['上班打卡', '下班打卡', '外勤打卡']
peoples=Dd.get_dd_user()
dd = Dd()
for p in peoples:
    dd.dddk(dk_types[int(i)], p['username'], p['password'])
input("please input any key to exit!")