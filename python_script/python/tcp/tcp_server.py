from socket import * 
s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(5)
print('waiting for connecting...')
s1,addr=s.accept()
print('connect from',addr)
while True:
    # input('先等等在接收')
    data=s1.recv(1024)
    # 客户端断开
    # print('++++',data)
    if not data:
        break
    print('++++'+data.decode())
    s1.send('确认下眼神'.encode())
s1.close()
s.close()