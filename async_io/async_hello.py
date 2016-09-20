'''
Created on Sep 20, 2016

@author: sheldonshen
'''
import asyncio
 
@asyncio.coroutine
def hello():
    print("Hello,world")
    #异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello,again!")
 
#获取EventLoop:
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()



#用Task封装两个coroutine
import threading
import asyncio

@asyncio.coroutine
def hello_task():
    print("Hello,world! (%s)" % threading.currentThread())
    yield from asyncio.sleep(1)
    print("Hello,again! (%s)" % threading.currentThread())

loop=asyncio.get_event_loop()
tasks=[hello_task(),hello_task()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()