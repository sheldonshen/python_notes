__author__ = 'shenyao'
s = set([1,2,2,3,3])
print(s)
s.add(4) #add element
print(s)
s.remove(1)#remove element
print(s)

s1=set([1,2,3])
s2=set([2,3,4])
print(s1 & s2)
print(s1 | s2)
#s1.add([1,2,3]) #unhashable type:'list'
