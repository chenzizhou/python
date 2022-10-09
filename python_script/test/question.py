# 接收执行脚本时提供的参数
from sys import argv
prompt='>'
# 给收到参数值赋予给变量
script,username,things=argv
print('do you like me,%s?'%username)
input(prompt)
print('do you want to make %s?'%things)
input(prompt)
"""chenziran"""