__author__ = 'shenyao'
L=['Micheal','Sarah','Tracy','Bob','Jack']
print(L[0],L[1],L[2])

r=[]
n=3
for i in range(n):
    r.append(L[i])
print(r)

print(L[:3])#slice
print(L[1:3])
print(L[-2:]) #include -1
print(L[-2:-1]) #exclude -1

L=list(range(100))
print(L)
print(L[:10])#前10个
print(L[-10:])#后10个
print(L[10:20])#前11-20个
print(L[:10:2])#前10个数,每2个取一个
print(L[::5])#所有的数,每5个数取一个
print(L[:])#原样复制一个list
print((0,1,2,3,4,5)[:3])#tuple切片操作
print('abcdefg'[:3])#string切片操作
