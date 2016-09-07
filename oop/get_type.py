'''
Created on Sep 6, 2016

@author: sheldonshen
'''
#获取对象信息
#1使用type()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(123)==type(456))
print(type(123)==int)
print(type('str')==str)
print(type("str")==int(456))
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#2使用isinstance()
class Parent:
    pass
class Sub(Parent):
    pass
print(isinstance(Sub(),Parent))
print(isinstance(123,int))
print(isinstance(b'a',bytes))
print(isinstance((1,2,3),(list,tuple)))
print(isinstance([1,2,3],(list,tuple)))

#3使用dir
print(dir("ABC"))#dir获的str对象的属性和方法
print(len("ABC"))
print("ABC".__len__())

class MyDog(object):
    def __len__(self):
        return 100
    
dog=MyDog()
print(dog.__len__()) #100


class MyObject(object):
    def __init__(self):
        self.x=9 
    def power(self):
        return self.x * self.x

obj = MyObject()
#检测对象属性
print(hasattr(obj,'x')) #有属性'x'吗
print(obj.x)
print(hasattr(obj,'y')) #False
setattr(obj,'y',19) #设置属性
print(hasattr(obj,'y'))
print(obj.y)
print(getattr(obj,'y'))#获取属性
print(getattr(obj,'z',404))# 获取属性'z'，如果不存在，返回默认值404
#检测对象方法
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn = getattr(obj,'power')#fn指向obj.power
print(fn())# 调用fn()与调用obj.power()是一样的




