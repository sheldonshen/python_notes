__author__ = 'shenyao'
#可以直接作用于for循环的数据类型有
#一类是集合数据类型，list,tuple,dict,set,str等
#二类是generator，包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象:Iterable
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x  in range(10)),Iterable)) #list generator
print(isinstance(100,Iterable)) #False

#可以被next()函数调用并不断返回下一个值得对象称为迭代器:Iterator
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator)) #True
print(isinstance([],Iterator)) #False
print(isinstance({},Iterator)) #False
print(isinstance('abc',Iterator))#False
#生成器都是Iterator对象

#把list,dict,str等Iterable变成Iterator,可以使用iter函数
print(isinstance(iter([]),Iterator))

#你可能会问，为什么list、dict、str等数据类型不是Iterator？
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据
#可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
#所以Iterator的计算是惰性的,只有在需要返回下一个数据的时候才会计算

#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


#小结
#1凡是可以作用于for循环的对象都是Iterable类型
#2凡是可以作用于next()函数的对象都是Iterator类型,它们表示一个惰性计算的序列
#3集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
#4python的for循环本质上就是通过不断调用next()函数实现的.


