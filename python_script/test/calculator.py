_a=123
b=123
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
c=Count(1,2)
c.test_add()



