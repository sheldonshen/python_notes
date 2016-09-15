__author__ = 'shenyao'
#基本知识
#\d可以匹配一个数字
#\w可以匹配一个字母或者数字
# . 可以匹配任意字符
#匹配变长的字符,用*表示任意个字符(包括0个),用+表示至少一个字符,用?表示0个或1个字符,用{n}表示n个字符
#用{n,m}表示n-m个字符
#用[]表示范围
#A|B可以匹配A或B
#^表示行的开头,^\d表示必须以数字开头
#$表示行的结束,\d$表示必须以数字结束
#^py$只能变成整行匹配,只能匹配py
import re
print(re.match(r'^\d{3}\-\d{3,8}$','012-12345')) #使用r前缀,就不用考虑转义的问题
#匹配成功返回Match对象,否则返回None

#切分字符串
print('a b   c'.split(' ')) #无法识别连续的空格
print(re.split(r'\s+','a b   c'))
print(re.split(r'[\s\,]+','a,b, c  d'))
print(re.split(r'[\s\,\;]+','a,b;; c  d'))

#分组
#用()表示的就是要提取的分组(Group)
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m)
#如果在正则表达式中定义了组,就可以在Match对象上用group方法提取出子串来
print(m.group(0))#group(0)永远是原始字符串
print(m.group(1))#第1个子串
print(m.group(2))#第2个子串

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#贪婪匹配
#正则默认就是贪婪匹配,也就是匹配尽可能多的字符串
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups()) #使用?就可以让\d+采用非贪婪匹配

#编译
import re
#编译
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
print(type(re_telephone))
#使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
