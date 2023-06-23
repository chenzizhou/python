# 即安装字符串式的路径自动导入模块，调用importlib.import_module()方法，但该方法的最小粒度只能达到.py文件名即模块
import importlib
#'类.A1'
path_str = input("请输入包-模块-类的字符串路径：")
module_path,class_name = path_str.rsplit('.',maxsplit=1)
# 1 利用字符串导入模块
module = importlib.import_module(module_path)  # from notify import email
# 2 利用反射获取类名
cls = getattr(module,class_name)  # Email、QQ、Wechat
# 3 生成类的对象
a = cls()
print(hasattr(a,'name'))#判断该对象是否有指定名字的属性或方法，返回值是bool类型
setattr(a,'high','175')#给指定的对象添加属性以及属性值
print(getattr(a,'high'))#获取对象指定名称的属性或方法，返回值是str类型
delattr(a,'high')#删除对象指定名称的属性或方法值，无返回值
print(a.__dict__)#过去对象属性