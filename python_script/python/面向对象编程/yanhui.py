def next_line(lst):
    L=[1]
    if len(lst)==1:
        L.append(1)
        return L
    for i in range(len(lst)-1):
        L.append(lst[i]+lst[i+1])
    L.append(1)
    return L
def print_l(n):
    L=[1]
    if n==1:
        return L
    for i in range(1,n):
        L=next_line(L)
    return L

# 生成器生成杨辉三角
def triangle(n):
    L=[1]
    yield L
    L.append(1)
    yield L
    while True:
        l=[1]
        for i in range(len(L)-1):
            l.append(L[i]+L[i+1])
        l.append(1)
        L=l
        yield L
        if len(L)==n:
            break
for i in triangle(10):
    print(i)
# L = list(filter(lambda n:n % 2 == 1, range(1, 20)))
# print(L)