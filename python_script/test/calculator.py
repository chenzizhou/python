class Count():
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
    def test_add(self):
        i=self.a+self.b  
        print(i) 
        return i 
    def sub(self):
        print(self.a-self.b)
    # def test_add(self):
        # print('加法') 
    # @unittest.skip('不想执行这一条')
    # def test_sub(self):
        # print('减法')    



