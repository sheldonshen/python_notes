'''
Created on Sep 6, 2016

@author: sheldonshen
'''
class Student(object):
    pass

bart = Student()
print(bart)
bart.name='tommy'#给实例变量绑定属性
print(bart.name)


class Person(object):
    def __init__(self,name,age):#self表示创建的实例本身
        self.name = name
        self.age = age
    def print_age(self):#数据封装
        print("%s : %s" %(self.name,self.age))
    
    def get_grade(self):#数据封装
        if self.age>=18:
            return "adult"
        else:
            return "child"        
bart = Person('simon',24)
bart.print_age()
print(bart.get_grade())

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
#除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
