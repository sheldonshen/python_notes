'''
Created on Sep 6, 2016

@author: sheldonshen
'''
#假设我们要增强now()函数的功能，比如在函数调用前后自动打印日志，但又不希望
#修改now函数的定义,这种在代码运行期间动态增加功能的方式,称之为"装饰器"(Decorator)
import functools
#本质上,decorator就是一个返回函数的高阶函数
def log(func):#能打印日志的decorator
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s()" % func.__name__)
        func(*args,**kw)
    return wrapper

def logWithParam(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s()" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


#@log  #相当与执行了now=log(now)
@logWithParam('execute')#now=logWithParam("execute")(now)
def now():
    print("2015-3-25")
    
f=now
f()
print(now.__name__)   #wrapper
# print(now.__name__) #now

#-----------------------
def logBA(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call")
        func(*args,**kw)
        print("end call")
    return wrapper

@logBA
def test():
    print("method is called")
    
test()

#功能类似于spring中AOP编程
