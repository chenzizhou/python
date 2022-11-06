# 作者
# NATURE
# 日期
# 2022/10/12 16:18
# 功能
#
v = 100
def outter( ):
    v = 200
    print( "outter里的V=", v) #在函数内创建一个函数并调用
    def inner():
        nonlocal v  #声明V为外部嵌套函数的作用域内的变量
        v += 1
        print( "innter里的V=", v)
    inner() #调用上面的函数
    print('调用inner后,outter里的V=', v)
outter( )
print("全局里的V的值是:",v)
