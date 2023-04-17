import sys
# print(sys.modules)
# print(sys.stdin.readline())
print(sys.exec_prefix)
print(sys.executable)
print(sys.prefix)
print(sys.platform)
'''
此模块提供对由使用或维护的某些对象的访问。
解释器和与解释器强交互的函数。
动态对象：
argv--命令行参数；argv[0]是脚本路径名(如果已知。
path--模块搜索路径；path[0]为脚本目录，否则为‘’
module--已加载模块的词典。
displayhook--调用以在交互会话中显示结果。
exepthook--调用以处理除systemexit之外的任何未捕获的异常。
在交互式会话中自定义打印或安装自定义。
顶级异常处理程序，分配其他函数来替换这些函数。
stdin--标准输入文件对象；由int()使用。
stdout-标准输出文件对象；由print()使用。
stderr-标准错误对象；用于错误消息。
通过分配其他文件对象(或行为类似文件的对象)。
对于这些，有可能重定向所有解释器的i/o。
last_type--上次未捕获异常的类型。
last_value--上次未捕获异常的值。
last_tracceback--上次未捕获异常的回溯。
这三项仅在交互会话中可用。
追溯已打印出来。
静态对象：
builtin_module_names--该解释器中内置的模块名称的元组。
版权--与此翻译有关的版权声明。
exec_prefix--用于查找特定于计算机的python库的前缀。
executable--python解释器的可执行二进制文件的绝对路径。
float_info--包含有关float实现的信息的命名元组。
float_repr_style--指示浮点数的repr()输出样式的字符串。
hash_info--包含有关散列算法的信息的命名元组。
hexversion-编码为单个整数的版本信息。
实现(implementation)--python实现信息。
int_info--包含有关int实现的信息的命名元组。
maxsize--容器支持的最大长度。
maxunicode--最大unicode码位的值。
platform--平台标识符。
prefix --用于查找python库的前缀。
thread_info--包含有关线程实现的信息的命名元组。
version--该解释器的字符串版本。
version_info--命名元组形式的版本信息。
dllhandle--[仅限windows]python dll的整数句柄。
winver--[仅限windows]python dll的版本号。
_enableleacywindowsfsencoding--[仅限windows]。
__stdin__--原来的stdin；不要碰！
__stdout__--原来的stdout；不要碰！
__stderr__--原来的stderr；不要碰！
__displayhook__--原来的displayhook；不要碰！
__excepthook__--原来的excepthook；不要碰！
功能：
displayhook()--将对象打印到屏幕上，并将其保存在内置中。_。
exepthook()-打印异常及其对sys.stderr的回溯。
exception()--返回当前线程的活动异常。
exc_info()--返回有关当前线程的活动异常的信息。
exit()--通过引发systemexit退出解释器。
getdlopen标志()--返回要用于dlopen()调用的标志。
getprofile()--获取全局性能分析函数。
getrefcount()--返回对象的引用计数(加1：-)。
getrecursionlimit()--返回解释器的最大递归深度。
getsizeof()--返回对象的大小(以字节为单位。
gettrace()--获取全局调试跟踪函数。
setdlopen标志()--设置要用于dlopen()调用的标志。
setprofile()--设置全局性能分析函数。
set递归限制()--设置解释器的最大递归深度。
settrace()--设置全局调试跟踪函数
'''
# print(sys.path)
# print(sys.__doc__,file=open('sys使用文档.txt','w'))
# print(sys.displayhook )
print(sys.exception() )
print(sys.getrecursionlimit() )
print(sys.getsizeof(1))
