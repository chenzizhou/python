from socket import * 
import os,sys
# 确定用哪个文件进行通信
server_address='./python/wlbc/test'
if os.path.exists(server_address):
    os.unlink(server_address)
# 创建本地套接字
s=socket(AF_UNIX,SOCK_STREAM)
# 绑定本地套接字文件
s.bind(server_address)
s.listen(5)
s.accept()
