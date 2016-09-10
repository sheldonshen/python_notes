__author__ = 'shenyao'
#操作文件和目录的函数一部分在os模块中，一部分在os.path中
'''
Created on Sep 9, 2016
@author: sheldonshen
'''
#操作文件和目录

#python内置的os模块也可以直接调用操作系统提供的接口函数
import os
#import sys
print(os.name)#os类型
#print(os.uname()) #availability:recent flavors of unix
#print(sys.platform)

#环境变量
print(os.environ)#os中定义的环境变量
print(os.environ.get("PATH"))#获取某个环境变量的值
print(os.environ.get("x",'default'))

print(os.path.abspath('.'))

#操作文件和目录
#在某个目录下创建新目录
print(os.path.join('.','pydev'))
#创建目录
print(os.mkdir('C:/Users/shenyao/Desktop/testdev'))

#os.mkdir('C:/Users/shenyao/Desktop/testdev')
#删除目录
os.rmdir('C:/Users/shenyao/Desktop/testdev')
#拆分路径
print(os.path.split("‪C:/Users/shenyao/Desktop/test.py"))
#拆分文件扩扩展名
print(os.path.splitext("‪C:/Users/shenyao/Desktop/test.py"))
#os.rename("C:/Users/shenyao/Desktop/test.py",'C:/Users/shenyao/Desktop/testC.py')
os.remove("C:/Users/shenyao/Desktop/test.py")
#当前目录下的所有文件夹
print([x for x in os.listdir(".") if os.path.isdir(x)])
#当前目录下的所有python文件
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
