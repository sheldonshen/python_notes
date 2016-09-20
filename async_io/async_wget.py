'''
Created on Sep 20, 2016

@author: sheldonshen
'''
#用asyncio的异步网络连接来获取sina、sohu和163的网站首页
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' %(host,line.decode('utf-8').rstrip()))
    #Ignore the body,close the socket
    writer.close()

loop=asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#asyncio提供了完善的异步IO支持；

#异步操作需要在coroutine中通过yield from完成；

#多个coroutine可以封装成一组Task然后并发执行。