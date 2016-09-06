'''
Created on Sep 6, 2016

@author: sheldonshen
'''
'a test module'
import sys

def test():
    args = sys.argv 
    if len(args)==1:
        print("hello world")
    elif len(args)==2:
        print("hello,%s" % args[1])
    else:
        print("too many arguments")

if __name__=='__main__':
    test()
    
#作用域
#1 __xxx__这样的变量是特殊变量，我们自己的变量一般不要用这种变量名
#2 类似_xxx或者__xxx这样的变量就是非公开的(private),不应该被直接使用

def _private_1(name):
    print("Hello,%s" % name)

def _private_2(name):
    print("Hi,%s" % name)

def greeting(name):
    if len(name):
        return _private_1(name)
    else:
        return _private_2(name)
    
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
