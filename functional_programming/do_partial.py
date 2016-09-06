'''
Created on Sep 6, 2016

@author: sheldonshen
'''
#偏函数(partial function)
print(int("12345"))
print(int("12345",base=8))
print(int("12345",16))

def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))
print(int2('1010101'))
#functools.partial就是帮我们创建一个偏函数,不需要我们自己定义int2()
#functools.partial的作用就是把一个函数的某些参数给固定住(也就是默认值)，
#返回一个新函数,调用这个新函数会更简单
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000',base=10))

max2=functools.partial(max,10)
#args = (10, 5, 6, 7)
#max(*args)
print(max2(5,6,7))

#使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
