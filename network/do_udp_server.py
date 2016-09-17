__author__ = 'shenyao'
import socket
#SOCK_DGRAM指定了Socket的类型是UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
#不需要调用listen方法，而是直接接收任何来自客户端的请求
print("Bind UDP on 99999...")
while True:
    #接收数据
    data,addr=s.recvfrom(1024)
    print("Received from %s:%s" % addr)
    #s.sendto(b'Hello,%s!' % data,addr)
    reply='Hello, %s!' % (data.decode('utf-8'))
    s.sendto(reply.encode('utf-8'), addr)

