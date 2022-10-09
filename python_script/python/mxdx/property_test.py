class Screen(object):
    def __str__(self):
        return 'Screen object (name=%s)' % self.name
    # __repr__ = __str__
    # @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，
    # 只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
    # 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value<0:
            raise ValueError('值小于0')
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value<0:
            raise ValueError('值小于0')
        self._height = value

    @property
    def resolution(self):
        return 1
    # 只有在没有找到属性的情况下，才调用__getattr__，
    # 已有的属性，比如name，不会在__getattr__中查找。
    def __getattr__(self,attr):
        if attr=='name':
            return 'nature'
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    # def __getattr__(self, attr):
    #     if attr=='age':
    #         return lambda:25
c=Screen()
print(c.name) 
# print(c.age())
print(c)
c.width=1
print(c.width,c.resolution)