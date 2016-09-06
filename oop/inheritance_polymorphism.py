'''
Created on Sep 6, 2016

@author: sheldonshen
'''

class Animal(object):
    def run(self):
        print("Animal is running")

class Dog(Animal):
    def run(self):
        print("Dog is running")
    def eat(self):
        print("Eating meat....")

class Cat(Animal):
    def run(self):
        print("Cat is running")

dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

#开闭原则
#1对扩展开放: 可以新增Animal子类
#2对修改关闭：  不需要修改依赖Animal类型的run_twice等函数

class Timer(object):
    def run(self):#对于python这种动态语言来说,不一定需要传入Animal类型，
                  #我们只需要确保传入的对象有一个run方法就可以了,这就是动态语言的鸭子类型
                  #它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
        print("start...")

run_twice(Timer())


#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
#但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
#你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象

