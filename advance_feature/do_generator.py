__author__ = 'shenyao'
#生成器(generator):如果列表元素可以按照某种算法推算出来,那我们就可以在循环的过程中不断推算出后续的元素
#这样就不必创建完整的list,从而可以节省大量的空间,在python中，这种一边循环一边计算的机制,称为生成器(generator)

#1 创建一个generator,把一个列表生成式的[]改成()
L=[x * x  for x in range(10)]
print(L) #list
g=(x * x  for x in range(10))
print(g)  #generator object <genexpr>

#通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#generator保存的是算法,每次调用next(g),就算出g的下一个元素的值
g=(x * x for x in range(10))
for n in g:#generator也是可迭代对象
    print(n)

def fib(max):#fib函数定义了斐波拉契数列的推算规则，这种逻辑其实非常类似generator
    n,a,b=0,0,1
    while n < max:
        #print(b) #要把函数变成generator,只需要把print(b)变成yield b 就可以了
        yield b  #2 这是定义generator的第2种方法
        a,b=b,a+b #相当于t=(b,a+b),t是一个tuple,a=t[0],b=t[1]
        n = n + 1
    return 'done'

#如果一个函数定义中包含yield关键字,那么这个函数就不再是一个普通函数,而是一个generator
print(fib(6)) #generator object fib

def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield(3)
    print("step 3")
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))


for n in fib(6):
    print(n) #拿不到函数的返回值


g=fib(6)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print("Generator return value:",e.value) #拿到函数的返回值
        break
    
    
#using generator(function) to print Pascal's Triangle(杨辉三角)
def triangles():
    #print("step 1")
    L=[1]
    yield L
    #print("step 2")
    L=[1,1]
    yield L
    while True:
        length = len(L)
        result=[1]
        for i in range(length-1):
            result.append(L[i]+L[i+1])
        result.append(1)
        #print("step ",(length+1))
        yield result
        L=result

n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
