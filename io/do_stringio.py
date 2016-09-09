'''
Created on Sep 9, 2016

@author: sheldonshen
'''
#StringIO就是在内存中读写str
from io import StringIO
f=StringIO()
print(f.write('hello'))
print(f.write(" "))
print(f.write("world！"))
print(f.getvalue())#getvalue用于获得写入后的str

#读
f=StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s=f.readline()
    if s == '':
        break
    print(s.strip())

