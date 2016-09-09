'''
Created on Sep 9, 2016

@author: sheldonshen
'''
#操作文件和目录

#python内置的os模块也可以直接调用操作系统提供的接口函数
import os
import sys
print(os.name)#os类型
#print(os.uname()) #availability:recent flavors of unix
print(sys.platform)

#环境变量
print(os.environ)#os中定义的环境变量
print(os.environ.get("PATH"))#获取某个环境变量的值
print(os.environ.get("x",'default'))

#操作文件和目录

