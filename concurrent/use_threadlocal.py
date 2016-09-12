#1 函数调用的时候,传递局部变量

# def process_student(name):
#     std = Student(name)
#     # std是局部变量，但是每个函数都要用它，因此必须传进去：
#     do_task_1(std)
#     do_task_2(std)
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)


#2 用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？

# global_dict = {}
#
# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
#
# def do_task_1():
#     # 不传入std，而是根据当前线程查找：
#     std = global_dict[threading.current_thread()]
#     ...
#
# def do_task_2():
#     # 任何函数都可以查找出当前线程的std变量：
#     std = global_dict[threading.current_thread()]
#     ...

#3 ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事
import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程相关的student:
   std=local_school.student
   print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=("Alice",),name="Thread-A")
t2=threading.Thread(target=process_thread,args=('Bob',),name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()

#Thread-local data is data whose value are thread specific.
#To manage thread-local data,just created an instance of local(or subclass) and store attributes on it:
#The instance's values will be different for separate threads

#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
