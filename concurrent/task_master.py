__author__ = 'shenyao'
#分布式进程master
#分布式多进程任务

# A 服务进程
# 服务进程负责启动Queue,把Queue注册到网络上,然后往Queue里面写入任务

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列:
task_queue=queue.Queue() #原始的queue,在一台机器上写多进程程序时,可以直接拿来使用,但是,在分布式多进程环境下,
                         #添加任务到Queue不可以直接对原始的task_queue进行操作,那样就绕过了QueueManager的封装,
                         #必须通过manager.get_task_queue()获得的Queue接口添加
#接收结果的队列
result_queue=queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上,callable参数关联了Queue对象(),register是classmethod
# QueueManager.register('get_task_queue',callable=lambda:  task_queue)
# QueueManager.register('get_result_queue',callable=lambda: result_queue)
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

#绑定端口5000,设置验证码'abc'
manager=QueueManager(address=('',5000),authkey=b'abc')
#启动Queue
manager.start()
#获得通过网络访问的Queue对象
task = manager.get_task_queue() #在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
                                # 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
result=manager.get_result_queue()

#放几个任务进去
for i in  range(10):
    n = random.randint(0,10000)
    print("Put task %d..." % n)
    task.put(n)

#从result队列读取结果
print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result: %s" % r)

#关闭
manager.shutdown()
print("master exit.")