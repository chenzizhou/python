from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',8888))
while True:
    msg=input('发消息》》')
    s.send(msg.encode())
    # s.send(msg.encode())
    if not msg:
        break
    data=s.recv(1024)
    print(data.decode())
s.close()