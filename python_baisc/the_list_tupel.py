'''
Created on Sep 1, 2016

@author: sheldonshen
#有序列表list(可变),tuple（不可变）
#因为tuple不可变,所以代码更安全，如果可能的话，能用tuple代替list就用tuple
#tuple所谓的'不变'是说，tuple每个元素的指向不变,即指向'a'不能改成指向'b',指向一个list，就不能
#就不能指向其他的对象。但指向的这个list本事是可变的,要创建一个内容也不变的tuple怎么做?
#那就必须保证tuple的每一个元素本身也不能变
'''

'''
The Python Tutorial 
https://docs.python.org/3/tutorial/introduction.html#lists
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
'''

classmates=['sheldon','simon','cong']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1]) #使用-1做索引,直接获取最后一个元素'cong'
print(classmates[-2])
print(classmates[-3])
classmates.append('sapphire')#追加元素到末尾
print(classmates)
classmates.insert(1, 'lin')
print(classmates)#插入元素到指定的位置
print(classmates.pop())#删除list末尾的元素
print(classmates)
print(classmates.pop(1))#删除指定位置的元素
print(classmates)
classmates[1]='jack'
print(classmates)

L=['Apple',123,True]
s=['python','java',['asp','php'],'scheme']
print(len(s))
print(s[2][1])

classmates=('sheldon','simon','cong')
print(classmates)
t=(1,)
print(t)

t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)
