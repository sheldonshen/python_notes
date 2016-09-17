__author__ = 'shenyao'
import socket
#编写客户端程序
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Micheal',b'Tracy',b'Srash']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
