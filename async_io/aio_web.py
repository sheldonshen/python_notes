'''
Created on Sep 20, 2016

@author: sheldonshen
'''
import asyncio
from aiohttp import web

#async/await

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv=await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print("Server started at http://127.0.0.1:8000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

#如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持
#asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架
