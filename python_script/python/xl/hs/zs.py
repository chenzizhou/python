'''装饰器'''
__author__='nature'
def log(func):
    def begin():
        print('begin')
        return func()
    return begin

@log
def begin():
    print('end')
begin()