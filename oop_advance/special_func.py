'''
Created on Sep 7, 2016

@author: sheldonshen
'''
#1定制类之__str__
class Student(object):
    def __init__(self,name):
        self._name=name
        
    def __str__(self):
        return 'Student object (name:%s)' % (self._name)
    
    __repr__=__str__
    
s = Student("simon")
print(s)


#2定制类之__iter__
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化2个计数器a,b 
    
    def __iter__(self):
        return self  #实例本身就是迭代对象,故返回自己
    
    def __next__(self):
        self.a,self.b=self.b,self.a + self.b #计算下一个值
        if self.a > 1000: #出口
            raise StopIteration()
        return self.a #返回下一个值
    
    def __getitem__(self,n):#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
        if isinstance(n,int):#n是索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b 
            return a
        if isinstance(n,slice):#n是切片
            start = n.start
            stop  = n.stop
            if start is None:
                start = 0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b=b,a+b 
            return L


for n in Fib():
    print(n)

#3定制类之__getitem__
print(Fib()[5])
print(Fib()[5:10])
print(Fib()[5:10:2])


#4定制类之__getattr__
class People(object):
    def __init__(self):
        self.name="micheal"
    
    def __getattr__(self,attr):#动态返回一个属性值
        if attr=='age':
            #return 250
            return lambda:25
        return AttributeError("'People' object has no attribute '%s'" % attr)
    
p = People()
print(p.name)
#print(p.age)
print(p.age())
print(p.abc) #None

#链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    
    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    
    def __str__(self):
        return self._path 

print(Chain().status.user.timeline.list)

#定制类之__call__
class Kid(object):
    def __init__(self,name):
        self.name=name
    
    def __call__(self):
        print("my name is %s" % (self.name))
    

k = Kid("simin")
k()#在实例本身上进行调用

#我们需要判断一个对象是否能被调用
print(callable(Kid('amy')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable("str"))
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
        










