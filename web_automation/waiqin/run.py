import os
import sys
import time
import unittest
import HTMLTestRunner
print(os.getcwd())
# 将当前工作目录下的文件夹都加入系统模块搜索路径
path = os.getcwd().split('\\')[0]
for i in range(0, len(os.getcwd().split('\\')) - 1):
    if i == 0:
        path = path
        sys.path.append(path)
    else:
        path = path + '/' + os.getcwd().split('\\')[i]
        sys.path.append(path)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./testcase', 'test_login.py')
    runner = unittest.TextTestRunner()
    # 添加时间生成唯一测试报告
    # file_url = './report/' + time.strftime("%Y-%m-%d %H_%M_%S") + ' result.html'
    file_url = './report/result.html'
    print(file_url)
    f = open(file_url, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='外勤登录', description='用例执行情况：')
    runner.run(suite)
    f.close()
