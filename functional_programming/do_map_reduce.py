__author__ = 'shenyao'
def f(x):
    return x * x

#map作为高阶函数,事实上他把运算规则抽象了
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce
def add(x,y):
    return x + y

print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return 10 * x + y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(reduce(fn,map(char2num,'13579'))) #字符串'13579'变成整数13579


#整理成一个函数
def str2int(s):
    def fn(x,y):
        return 10 * x + y

    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

#利用lambda函数进一步简化
def str2int(s):
    def fn(x,y):
        return 10 * x + y

    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:10 * x + y,map(char2num,s))


def prod(L):
    return reduce(lambda x,y:x * y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7]))

def normalize(name):
    return name.title()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# def str2float(s):
#     pass
#
# print('str2float(\'123.456\') =', str2float('123.456'))
