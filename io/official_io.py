__author__ = 'shenyao'
#official input and output

#1 fancier output formatting
s='Hello,World'
print(str(s))
print(repr(s))
hello="hello,world\n"
print(repr(hello))
#The repr() of the string adds string quotes and backslashes:
print(hello)
#the arguments to repr() may be any python object
print(repr((1,2,('spam','eggs'))))

#write a table of squares and  cubes in two ways
for x in  range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    #notice use of the 'end' on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('12'.zfill(5))
print("-3.14".zfill(7))
print("3.14159126".zfill(5))
print("we are the {} who say '{}'!".format('knight','Ni'))
print('{0} and {1}'.format('spam','eggs'))
print("{1} and {0}".format("spam",'eggs'))
print("this {food} is {adjective}.".format(food="banana",adjective="delicious"))
print("the story of {0},{1},and {other}.".format('bill','manfred',other="test"))
#'!a'(apply ascii()),'!s'(apply str()) and '!r'(apply repr()) can be used to convert the value
# before it is formatted
contents="eels"
print('my hovercraft is full of {}.'.format(contents))
print('my hovercraft is full of {!r}.'.format(contents))
import math
print('the value if PI is approximately {0:.3f}.'.format(math.pi))
table={'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,phone in table.items():
    print("{0:10}  ==> {1:10d}".format(name,phone))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#printf-style string format
print("the value of pi is %5.3f." % math.pi)

f=open("end.txt",'r')
print(f.read().strip())
print(repr(f.read()))
f.close()

f=open("end.txt",'r')
for line in f:
    print(line,end="")
f.close()

f=open("end.txt",'w')
value=('the answer',42)
s=str(value)
print(f.write(s))
