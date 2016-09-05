__author__ = 'shenyao'
#列表生成式(list comprehensions),是python内置的非常简单却可以用来创建list的生成式
print(list(range(1,11)))

L=[]
for x in range(1,11):
    L.append(x * x)
print(L)

print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0]) #筛选仅偶数的平方
print([m + n for m in 'abc' for n in 'xyz'])#两层循环,生成全排列

import os #导入os模块
print([d for d in os.listdir('.')]) #os.listdir可以列出文件和目录

d={'x':'a','y':'b','z':'c'}
print([k+'='+v for k,v in d.items()])

L=['Hello','World','Welcome']
print([s.lower() for s in L])#把一个list中的所有字符串变成小写

#通过列表生成式,可以快速生成list,可以通过一个list推导出里一个list.
