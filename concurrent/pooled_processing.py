__author__ = 'shenyao'
#启动大量的子进程,可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print("Run task %s (%s)..." %(name,os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end   = time.time()
    print('Task %s runs %0.2f seconds.' %(name,(end-start)))

if __name__=="__main__":
    print("Parent process %s " % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("Waiting all subprocess done...")
    p.close()#调用close之后就不能继续添加新的Process了,
    p.join()#等待所有子进程完成,one must call close() or terminate() before using join()
    print("All subprocess done")


