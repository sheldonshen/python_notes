__author__ = 'shenyao'
d={'a':1,'b':2,'c':3}
for key in d:#iter the dict
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

for ch in "simon":#iter the str
    print(ch)

#判断一个对象是否可迭代
from collections import Iterable
print(isinstance('abc',Iterable))#str是否可迭代
print(isinstance([1,2,3],Iterable))#list是否可迭代
print(isinstance((1,2,3),Iterable))#tuple是否可迭代
print(isinstance({'a':1,'b':2},Iterable))#dict是否可迭代
print(isinstance(123,Iterable))#整数是否可迭代(False)

#list实现类似java的下标循环
for i,value in enumerate(['a','b','c']):
    print(i,value)

#for循环里,同时引用2个变量
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
