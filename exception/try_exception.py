__author__ = 'shenyao'
try:
    print("try...")
    r=10/2
    print('result:',r)
except ZeroDivisionError as e:
    print("except:",e)
finally:
    print("finally...")
print("END")


try:
    print("try....")
    r=10/int('2')
    print("result:",r)
except ValueError as e:
    print("ValueError:",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print("no error")
finally:
    print("finally")
print("END")


try:
    r=10/int("a")
except ValueError as e:
    print("ValueError:",e)
except UnicodeError as e:#第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类
    print("UnicodeError:",e)

import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e) #记录错误

main()
print("END END END")

#抛出错误
class FooError(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise FooError("invalid value: %s" %s) #抛出错误
    return 10 / n

foo('0')


def foo(s):
    n=int(s)
    if n==0:
        raise ValueError("invalid error: %s" %s)
    return 10 / n

def bar():
    try:
        foo("0")
    except ValueError as e:
        print("ValueError!")
        raise #抛出错误,raise语句不带参数,就会把当前错误原样抛出,

bar()

try:
    10/0
except ZeroDivisionError:
    raise ValueError("input error!")#还可以把一种类型的错误转化成另一种类型
