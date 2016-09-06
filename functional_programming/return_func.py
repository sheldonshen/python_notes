'''
Created on Sep 6, 2016

@author: sheldonshen
'''
#1函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def mysum():
        ax = 0
        for n in args:
            ax=ax+n 
        return ax
    return mysum;

print(calc_sum(1,2,3,4))
f = lazy_sum(1,2,3,4)
print(f)
print(f())
f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1 == f2) #False

#2闭包
#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
#这种称为“闭包（Closure）”的程序结构拥有极大的威力

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i * i 
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1())#9
print(f2())#9
print(f3())#9

#返回闭包时牢记的一点是:返回函数不要引用任何循环变量后者后续会发生变化的变量
def count_refactor():
    def f(j):
        def g():
            return j * j 
        return g 
    fs=[]
    for i in range(1,4):
        fs.append(f(i))#f(i)立刻被执行,因此i的当前值被传入f()
    return fs

f1,f2,f3=count_refactor()
print(f1())#1
print(f2())#4
print(f3())#9

#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
