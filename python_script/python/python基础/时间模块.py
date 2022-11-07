# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/6 11:13
# 功能：
'''_STRUCT_TM_ITEMS
__doc__
__loader__
__name__
__package__
__spec__
altzone  1
asctime
ctime
daylight  2
get_clock_info
gmtime
localtime
mktime
monotonic
monotonic_ns
perf_counter
perf_counter_ns
process_time
process_time_ns
sleep
strftime
strptime
struct_time
thread_time
thread_time_ns
time
time_ns
timezone 3
tzname  4'''
import time

# for i in dir(time):
#     if i[0:2] == '__' or i[0:1] == '_' or i in ["altzone","daylight","timezone","tzname"]:
#         # t = 'time.' + i
#         # print(eval(t))
#         print(i)
#     elif i in['get_clock_info','mktime','sleep','strftime','_strptime_time']:
#         pass
#     else:
#         f='time.'+i+'()';
#         v=eval(f);
#         print(v);
print(time.time())
print(time.ctime())
print(time.localtime(1667748592.1274579))
print(time.gmtime())
print(time.asctime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))




