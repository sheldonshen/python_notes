__author__ = 'shenyao'
age=3
if age>=18:
    print("your age is %d" % age)
    print("adult")
else:
    print("your age is ", age)
    print("teenager")

age=3
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("id")

x = []
if x :#只要x是非零数值，非空字符串,非空list等,就判断为True,否则就是False
    print("true")
else:
    print("false")

s = input("birth:")
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print("00后")
