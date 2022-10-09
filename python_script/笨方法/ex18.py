# coding=utf-8
# 函数接收多个参数*args
def function(*args):
    # 将接收到的参数赋给变量
    username,password=args
    print(username,password)
function('nature',123456)