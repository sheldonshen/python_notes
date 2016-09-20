'''
Created on Sep 20, 2016

@author: sheldonshen
'''
#协程，又称微线程，纤程。英文名Coroutine。
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行
#Python对协程的支持是通过generator实现的。


#注意到consumer函数是一个generator
def consumer():
    r=""
    while True:
        n = yield r#consumer通过yield拿到消息n,又通过yield把结果返回
        if not n:
            return 
        print("[CONSUMER]Consuming %s..." % n)
        r='200 OK'

#把一个consumer传入produce
def produce(c):
    c.send(None)#启动生成器
    n=0
    while n < 5:
        n = n + 1
        print("[PRODUCER]Producing %s..." % n)
        r = c.send(n)#切换到consumer
        print('[PRODUCER]Consumer return: %s' % r)#produce拿到consumer处理的结果，继续生产下一条消息
    c.close()#produce决定不生产了,通过c.close()关闭关闭consumer,整个过程结束

c = consumer()
produce(c)

#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
#子程序就是协程的一种特例。
#协程:单线程执行并发程序
