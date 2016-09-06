'''
Created on Sep 6, 2016

@author: sheldonshen
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    #return t[0] #按姓名排序
    return t[1]  #按成绩排序

L2 = sorted(L, key=by_name,reverse=True)
print(L2)

#sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
