class Primes:
    def __init__(self,b,n):
        self.data=[x for x in range(b,n+1) if x%2!=0]
    def __iter__(self):
        return self.data
    def __next__(self):
        for i in self.data:
            print(i)
for i in  Primes(2,8):
    print(i)