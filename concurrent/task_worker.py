__author__ = 'shenyao'
#分布式进程worker
#分布式多进程任务
# B 任务进程
import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只从网络上获取Queue,所以注册时只提供名字：
QueueManager.register('get_task_queue')
QueueManager.register("get_result_queue")

#连接到服务器,也就是运行task_master.py的机器
server_addr='127.0.0.1' #任务进程要通过网络连接到服务进程,所以要指定服务进程的IP
print("Connect to server %s..." % server_addr)
#端口和验证码注意保持与task_master.py设置的完全一样：
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接
m.connect()
#获取Queue的对象
task=m.get_task_queue()
result=m.get_result_queue()
#从task队列取任务,并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1) #取出任务
        print("run task %d  * %d " % (n, n))
        r = '%d * %d = %d' %(n,n,n * n)#执行任务
        time.sleep(1)
        result.put(r)#把结果写入result
    except queue.Empty:
        print("task queue is empty")
#处理结束
print("worker exit.")

#笔记
#计算密集型vsIO密集型

#web应用就是IO密集型
#对于计算密集型任务,最好用C语言编写
#对于IO密集型任务,脚本语言是首选,C语言最差

#异步IO
#如果充分利用操作系统提供的异步IO支持,就可以用单进程单线程模型来执行多任务,
#这种全新的模型称为事件驱动模型,Nginx就是支持异步IO的web服务器
#用异步IO编程模型来实现多任务是一个主要趋势
#对应到python语言,单进程的异步编程模型称为协程

#在Thread和Process中,应当优选Process,因为Process更稳定,而且,Process可以分布到多台机器上,
# 而Thread最多只能分布到同一台机器的多个CPU上










