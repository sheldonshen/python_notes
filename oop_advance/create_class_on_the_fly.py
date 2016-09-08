__author__ = 'shenyao'
class Hello(object):
    def hello(self,name="world"):
        print("Hello,%s" % name)

h = Hello()
print(type(Hello)) #type
print(type(h))
h.hello()

#我们说class的定义是运行时动态创建的,而创建class的方法就是type函数
def fn(self,name="world,welcome"):#先定义函数
    print("Hello,%s" % name)

#type方法参数解释
#1 class的名字
#2 继承的父类集合
#3 class的方法名与函数绑定，这里我们把函数fn绑定到方法名hello
Hello=type("Hello",(object,),dict(hello=fn)) #创建Hello class
he=Hello()
he.hello()
print(type(Hello))
print(type(he))




