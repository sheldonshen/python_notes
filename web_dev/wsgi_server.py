'''
Created on Sep 20, 2016

@author: sheldonshen
'''
#WSGI:Web Server Gateway Interface
def application(environ,start_response):
    start_response("200 OK",[('Content-Type','text/html')])
    body = '<h1>Hello,%s!</h1>' %(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
#上面的application函数就是符合WSGI标准的一个HTTP处理函数
#environ:一个包含所有HTTP请求信息的dict对象
#start_response:一个发送HTTP响应的函数

#python内置了一个WSGI服务器，这个模块叫wsgiref
#运行WSGI服务器,加载application函数
#从wsgiref导入
from wsgiref.simple_server import make_server
#导入我们自己编写的application函数
#from hello import application

#创建一个服务器，IP地址为空,端口是8000，处理函数是application
httpd=make_server('',8000,application)
print("Serving HTTP on port 8000...")
#开始监听HTTP请求
httpd.serve_forever()

#无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，
#HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

#复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，
#我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发
