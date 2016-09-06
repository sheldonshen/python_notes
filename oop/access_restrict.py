'''
Created on Sep 6, 2016

@author: sheldonshen
'''
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
bart = Student("sheldon",24)
print(bart.age)
bart.age=56
print(bart.age)#外部代码还是可以自由的修改实例的属性值


#将属性变成private的.
class Student_V2(object):
    def __init__(self,name,age):
        self.__name=name #在属性名的前面加__propertyName,属性就成为私有属性了
        self.__age=age
    def get_name(self):
        return self.__name 
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<=age<=100: #做参数的合法性检查
            self.__age=age
        else:
            raise ValueError("bad score")

bart = Student_V2("sheldon",24)
#print(bart.__age) #'Student_V2' object has no attribute '__age'
print(bart.get_age())
bart.set_age(100)
print(bart.get_age())
print(bart._Student_V2__age)
bart.__age=102#新增了一个属性__age,与内部的__age属性不是同一个
print(bart.get_age)
print(bart.__age)
