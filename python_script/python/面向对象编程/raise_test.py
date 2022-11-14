def print_test():
    w=int(input('put a word:'))
    # raise ValueError("请输入整数")
    if w<0:
     raise ValueError("请输入整数")
    print(w)
try:
    print_test()
except ValueError as e:
    print(e)