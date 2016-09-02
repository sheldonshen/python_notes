__author__ = 'shenyao'
names=['Micheal','Bob','Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
    sum = sum + x
print(sum)


print(type(range(5))) # class range
print(type(list(range(5)))) #class list

print(list(range(5)))

sum=0
for x in range(101):
    sum = sum + x
print(sum)