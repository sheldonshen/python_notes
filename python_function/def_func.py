__author__ = 'shenyao'
def my_abs(x):
    if not isinstance(x,(int,float)):#函数参数检查
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x

def return_None():
    pass
print(return_None()) #None

def nop(): #空函数
    pass

#print(my_abs('A'))
#print(abs('A'))

import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return  nx,ny #python的函数返回多值其实就是返回一个tuple

x,y=move(100,100,60,math.pi/6)
print(x,y)
r=move(100,100,60,math.pi/6)
print(r) #tuple

def quadratic(a,b,c):
    return (-b-math.sqrt(b*b-4*a*c))/2*a,(-b+math.sqrt(b*b-4*a*c))/2*a

print(quadratic(2,3,1))
