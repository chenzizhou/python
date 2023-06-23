def debx(bj,ll,yf):
    return bj*(ll/100*((1+ll/100)**yf))/(((1+ll/100)**yf)-1)
print(debx(10000,2,2))

def debj(bj,ll,yf,yhyfs):
    if yf>=yhyfs:
        print('贷款已经换完')
        return 0
    else:
        return (bj/yf)+(bj-(yhyfs*(bj/yf)))*ll/100


print(debj(10000,2,2,2))