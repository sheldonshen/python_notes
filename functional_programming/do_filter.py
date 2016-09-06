'''
Created on Sep 6, 2016

@author: sheldonshen
'''
def is_odd(n):#返回一个奇数序列(筛选函数)
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8])))

def not_empty(s):#删除序列中空字符串(筛选函数)
    return s and s.strip()

print(list(filter(not_empty,['A',' ','B',None,'C',' '])))


def _odd_iter():
    n =1
    while True:
        n = n + 2
        yield n 

def _not_divisiable(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n 
        it = filter(_not_divisiable(n),it) #构造新序列
        

#打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


def is_palindrome(n):#赛选回文数
    li = list(reversed(str(n)))
    rsn=""
    for s in li:
        rsn=rsn+s 
    rn = int(rsn)
    return rn == n

output = filter(is_palindrome,range(1,1000))
print(list(output))

#由于filter使用了惰性计算,所以只有在取filter结果的时候,才会真正选择返回下一个元素
