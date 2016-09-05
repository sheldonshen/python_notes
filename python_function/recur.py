#递归形式
# def fact(n):
#     if n == 1:
#         return 1 
#     return n * fact(n-1)
# 
# print(fact(1))
# print(fact(5))
# print(fact(100))
# print(fact(1000))

#尾递归:在函数返回的时候,调用自身本身,并且return语句不能包含表达式，这样，编译器或者解释器就可以把尾递归做优化
#使递归本身无论调用多少次,都只占用一个帧栈,不会出现栈溢出的情况

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    else:
        return fact_iter(num-1,num * product) #仅返回递归函数本身
    #num-1和num * product在函数调用之前就会被计算


print(fact(1000))

#遗憾的是,大多数编程语言没有针对尾递归做优化,python解释器也没有做也没有做优化,所有
#即使把上面的函数fact(s)改成尾递归的形式,也会导致栈溢出


#小结
#1 使用递归函数的优点是逻辑简单清晰,缺点是过深得调用会导致栈溢出
#2 python标准的解释器没有针对尾递归做优化,任何函数都会存在栈溢出的问题

    
    