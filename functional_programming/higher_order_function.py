__author__ = 'shenyao'
#高阶函数(Higher-order function)

#1变量指向函数
print(abs)
f=abs
print(f)
#函数本身也可以赋值给变量,即变量可以指向函数
print(f(-10))

#2函数名也是变量
#abs=10
#print(abs(-10))

#3传入函数
#一个函数可以接收里一个函数作为参数,这种函数就称之为高阶函数
def add(x,y,f):
    return f(x)+f(y)

print(add(5,-6,abs))
