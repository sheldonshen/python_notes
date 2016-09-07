'''
Created on Sep 7, 2016

@author: sheldonshen
'''
class Student(object):
    age=24 #类属性,归Student类所有
    def __init__(self,name):
        self.name = name

s=Student("Bob")
s.score=90#实例属性
print(s.score)
print(s.age)#类属性age,实例变量s可以访问到
print(Student.age)
# print(Student.name)
s.age=100#给实例绑定age属性
print(s.age)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的age属性
del s.age #删除实例的age属性
print(s.age)#再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

#千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性