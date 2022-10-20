# 作者
# NATURE
# 日期
# 2022/10/19 17:23
# 功能
#
import multiprocessing

p=multiprocessing.Pipe(duplex=False)
print(p[0].send('123'))
print(p[0].recv())
