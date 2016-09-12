__author__ = 'shenyao'
#multiprocessing模块就是跨平台版本的多进程模块
#Process类来代表一个进程对象
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print("Run  process %s (%s)..." %(name,os.getpid()))

if __name__=="__main__":
    print("Parent process %s." %(os.getpid()))
    #target:target is the callable object to be invoked by the run() method
    #args:args is the argument tuple for the target invocation
    p=Process(target=run_proc,args=('test',))
    print("Child process will start")
    p.start()
    p.join()#等待子进程结束后在继续往下运行,同常用于进程间的同步
    print("Child process end")
