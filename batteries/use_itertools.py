__author__ = 'shenyao'
#1 count()
import itertools
naturals=itertools.count(1) #count会创建无限的迭代器
# for n in naturals:
#     print(n)
#     pass

#2 cycle()
cs=itertools.cycle('ABC')
# for c in cs:
#     print(c)

#3 repeat()
ns=itertools.repeat('A',3)
for n in ns:
    print(n)

#takewhile()
naturals=itertools.count(1)
ns = itertools.takewhile(lambda x:x <= 20,naturals)
print(list(ns))

#chain()
for c in itertools.chain('ABC','XYZ'):
    print(c)

#groupby()
for key,group in itertools.groupby("AAABBBCCAAA"):
    print(key,list(group))
print("-----------------------")
for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
    print(key,list(group))
