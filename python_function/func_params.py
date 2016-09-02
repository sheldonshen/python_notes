__author__ = 'shenyao'
def power(x,n):#位置参数
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5,2))#位置参数
print(power(5,3))#位置参数


def power(x,n=2):#默认参数(必选参数在前,默认参数在后)
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5))
print(power(5,3))


def enroll(name,gender,age=6,city='beijing'):
    print("name",name)
    print("gender",gender)
    print("age",age)
    print("city",city)

enroll('Sarah','F')
enroll('Bob','M',7)
enroll('Sheldon','M',city="shenzhen")

#演示默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
#print(add_end())

#--------pitfall----------------
print(add_end())
print(add_end())
print(add_end())
#-------pitfall----------------

#-------solution---------------
#默认参数必须指向不变对象
def add_end(L=None):#利用None这个不变对象来实现
    if L is None:
        L=[]
    L.append('END')
    return L
#-------solution---------------
print(add_end())
print(add_end())
print(add_end())


def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#可变参数
def calc(*numbers):#把函数参数改为可变参数
    sum=0
    print(type(numbers)) #tuple
    for n in numbers:#numbers tuple
        sum=sum+n*n
    return sum
# print(calc([1,2,3]))
# print(calc((1,3,5,7)))
print( calc(1, 2, 3))
print(calc(1,3,5,7))
print(calc())
nums=[1,2,3]
print(calc(nums[0],nums[1],nums[2]))
print(calc(*nums))#*num表示把这个list的所有元素作为可变参数传进去,这种写法相当有用


#关键字参数
#可变参数在函数调用的时候自动组装为一个tuple,
#关键字参数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw) #kw {}

person('sheldon',24)
person('sheldon',24,city='beijing')
person('sheldon',24,gender='M',job="Engineer")
extra={'gender':'M','job':'softwar'}
person('sheldon','M',**extra)#kw将获得extra参数的一份拷贝


#关键字参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,"age:",age,"other:",kw)

person('jack',24,city='beijing',addr='chaoyang',zipcode=12345)


#命名关键字参数
#和关键字参数**kw不同,命名关键字参数需要一个特许的分隔符*,*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

person('jack',24,city="shenzhen",job="programmer")

def person(name,age,*args,city,job):
    print(name,age,city,job)

person('jack',24,city="shenzhen",job="programmer")

def person(name,age,*args,city='shenzhen',job):#命名关键字参数可以有默认值
    print(name,age,city,job)

person('jack',24,job="programmer")

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

#组合参数
#5中参数的定义顺序必须是必选参数,默认参数,可变参数,命名关键字参数,关键字参数
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a,b,c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
#所以,对于任意参数,都可以通过类似func(*args,**kw)的形式调用,无论他的参数是如何定义的

#小结
#1 默认参数一定要用不可变对象,如果是可变参数,程序运行时会有逻辑错误
#2 *args是可变参数,args接收的是一个tuple
#3 **kw是关键字参数,kw接收的是一个dict
#4 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
#5 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
#6 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
#7 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数













