num=input("输入一串数字：")
s=''
for i in range(1,len(num)+1):
    s+=str(num[-i])
print(s)
