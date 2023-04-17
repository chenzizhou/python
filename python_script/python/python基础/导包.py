import 模块的隐藏属性 #dir查看时，只导入该模块名的变量名
# from 模块的隐藏属性 import * #dir查看时，默认导入该模块下所有变量，当模块有__all__列表时，只导入列表中的属性
print(dir())