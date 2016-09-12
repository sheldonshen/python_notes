#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

print("process (%s) start...." % os.getpid())
#only works Unix/Linux/Mac
print("before fork")
pid=os.fork() #fork a child process
print("after fork") #但是fork()调用一次，返回两次
#return 0 in the child and the child's process id in the parent
if pid == 0:
    print("I'm the child process (%d) and my parent is (%d)" %(os.getpid(),os.getppid()))
else:
    print("I(%d) just created a child process (%d)" %(os.getpid(),pid))
