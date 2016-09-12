__author__ = 'shenyao'
import time,threading

#假定这是你的银行存款
balance=0
lock=threading.Lock()


def change_it(n):
    #先存后取,结果应该为0
    global balance
    balance=balance + n
    balance=balance - n

def run_thread(n):
    for i in range(100000):
        #先要获取锁
        lock.acquire()
        try:
            #放心的改吧
            change_it(n)
        finally:
            #改完了一定要释放锁
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
#balance = balance + n
#也分两步：
#计算balance + n，存入临时变量中；
#将临时变量的值赋给balance。

import multiprocessing

def loop():
    x = 0
    while True:
        x = x  ^ 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()


#Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
#Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响
