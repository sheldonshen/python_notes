'''
Created on Sep 7, 2016

@author: sheldonshen
'''
class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print("Running....")

class FlyableMixIn(object):
    def fly(self):
        print("Flying....")
        
#各种动物
class Dog(Mammal,RunnableMixIn):#通过多重继承，一个子类就可以同时获得多个父类的所有功能
    pass

class Bat(Mammal,FlyableMixIn):#通过多重继承，一个子类就可以同时获得多个父类的所有功能
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird,RunnableMixIn):
    pass
#让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn(混入)
