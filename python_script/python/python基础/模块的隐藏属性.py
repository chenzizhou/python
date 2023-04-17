__all__ = ['name']  # 其他模块引用时，只导入该列表属性
name = 1
age = 22
_name = 2  # 导入其他模块时 看不见该属性
print(name, age)
