age = int(input('请输入您的年龄：'))
if age >= 18:
    price = 10
elif age >= 4:
    price = 5
else:
    price = 0
print('您的年龄为{age}需要收费{price}美元')