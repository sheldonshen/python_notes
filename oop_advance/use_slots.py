'''
Created on Sep 7, 2016

@author: sheldonshen
'''
class Student(object):
    pass

s=Student()
s.name='congbird'
print(s.name)

def set_age(self,age):
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)#调用实例方法
print(s.age)
#给一个实例绑定的方法,对尼一个实例不起作用
s1=Student()#创建新的实例
#s1.set_age(22)#'Student' object has no attribute 'set_age'

#为了给所有实例都绑定方法,可以给class绑定方法
def set_score(self,score):
    self.score=score

Student.set_score=set_score

#给class绑定方法后,所有实例均可调用
s.set_score(123)
print(s.score)
s1.set_score(456)
print(s1.score)

#上面的set_score方法可以直接定义在class中,但是动态绑定允许我们在程序的运行
#过程中动态给class加上功能,这在静态语言中很难实现


#使用__slots__来限制class实例能添加的属性
class Person(object):
    __slots__=('name','age')#用tuple定义允许绑定的属性名称


p = Person()
p.name="congbire"
p.age=23
#p.gender="M" #'Person' object has no attribute 'gender'

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Man(Person):
    pass

m = Man()
m.gender="M"
