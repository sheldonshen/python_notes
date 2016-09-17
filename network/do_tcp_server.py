__author__ = 'shenyao'
import threading,time,socket
#服务器(创建一个基于IPV4和Tcp协议的socket)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1',9999))
s.listen(5)#开始监听,参数表示等待连接的最大数量
print("Wauting for connection...")

#连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。
# 如果客户端发送了exit字符串，就直接关闭连接
def tcplink(sock,addr):
    print("Accept new connection from %s:%s" % addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connection from %s:%s closed." % addr)

while True:
   #接受一个新的连接
   sock,addr=s.accept()
   #创建新线程来处理TCP连接,每个连接都必须创建新线程（或进程）来处理，
   # 否则，单线程在处理连接的过程中，无法接受其他客户端的连接
   t=threading.Thread(target=tcplink,args=(sock,addr))
   t.start()