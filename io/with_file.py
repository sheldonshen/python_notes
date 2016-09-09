'''
Created on Sep 9, 2016

@author: sheldonshen
'''
#本章的IO编程都是同步模式，异步IO由于复杂度太高，后续涉及到服务器端程序开发时我们再讨论。

#读取文件
try:
    f=open("file.txt",'r')
    print(f.read())
finally:
    if f:
        f.close()

#每次都这么写,实在是太繁琐,python引入了with语句来帮我们自动调用close方法
with open("file.txt",'r') as f:
    print(f.read())


#read一次性读取文件的全部内容
#read(size)每次最多读取size个字节的内容
#readline每次读取一行
#readlines一次性读取所有内容并按行返回
with open("file.txt",'r') as f:
    for line in f.readlines():
        print(line.strip())#把末尾的'\n'去掉      

#file-like Object
#像open函数返回的这种有个read()方法的对象，在python中统称为file-like object,
#除了file外,还可以是内存的字节流,网络流,自定义流等，file-like object不要求从特定类继承,
#只要有个read()方法就行，StringIO就是在内存中创建的file-like Object,常用作临时缓冲

#二进制文件,用rb模式打开
with open("Base64.png",'rb') as f:
    print(f.read())  
    

#字符编码
with open("file.txt",'r',encoding='gbk',errors="ignore") as f:
    print(f.read())
    

#写文件
with open("file.txt",'w') as f:#r,rb
    print(f.write("hello,taiwan"))

#在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。 
