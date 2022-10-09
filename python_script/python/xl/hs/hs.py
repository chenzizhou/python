# def is_palindrome(n):
#     s=''
#     for i in range(1,len(str(n))+1):
#         s+=str(n)[-i]
#     if n==int(s):
#         return s

# print(list(filter(is_palindrome,[1,2,3,4,5,12,12321])))



def is_palindrome(n):
    l=list(reversed(list(str(n))))
    r=''.join(l)
    if r==str(n):
        return r
    
print(list(filter(is_palindrome,[1,2,3,4,5,12,12321])))
 