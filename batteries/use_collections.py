'''
Created on Sep 16, 2016

@author: sheldonshen
'''
#collections是python内建的一个集合模块,提供了许多有用的集合类
#可替换python内置的list,tuple.dict,set等类型

#1 namedtuple,一个点的二维坐标
from collections import namedtuple
Point=namedtuple("Point",['x','y'],verbose=True)
p=Point(1,2)
print(p.x)
print(p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))

#namedtuple('名称',[属性list])
Circle=namedtuple('Circle',['x','y','r'])
circle=Circle(2,1,1) #tuple-like objects
print(circle.x)
print(circle.y)
print(circle.r)
print(repr(circle))
print(Circle._source)
#namedtuple(typename,field_names):factory function for creating tuple subclasses with named fields

#official introducing about namedtuple
#basic example
Point=namedtuple('Point',['x','y'])
p=Point(11,y=22) #instantiate with positional or keyword arguments
print(p[0]+p[1]) #indexable like the plain tuple(11,22)
x,y=p #unpack like a regular tuple
print(x,y)
print(p.x+p.y) #fields also accessiable by by name
print(p) #readable __repr__ with a name=value style

#namedtuple interacts with csv,sqlite3

#method and attribute
t=[11,22]
print(Point._make(t))#makes a new instance from an existing sequence or iterable
print(p._asdict())
print(p)
print(p._replace(x=33))
print(p._fields) #view the field name

Color=namedtuple('Color','red green blue')
Pixel=namedtuple("Pixel",Point._fields + Color._fields)
print(Pixel._fields)
print(Pixel(11,22,128,255,0))
print(getattr(p,'x'))
d={'x':11,'y':22}
print(Point(**d))

class Point(namedtuple('Point','x y')):
    __slots__=() #This helps keep memory requirements low by preventing the creation of instance dictionaries.
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f y=%6.3f hypot=%6.3f ' % (self.x,self.y,self.hypot)

for p in Point(3,4),Point(14,5/7):
    print(p)

Point3D = namedtuple("Point3D",Point._fields+('z',))

Book = namedtuple("Book",['id','title','authors'])
Book.__doc__+= ': Hardcover book in active collection'
Book.id.__doc__="13-digit ISBN"
Book.title.__doc__="Title of first printing"
Book.authors.__doc__ = 'List of authors sorted by last name'
print(Book.__doc__)

Account=namedtuple("Account",'owner balance transaction_count')
default_account=Account('<owner name>',0.0,0)
johhns_account=default_account._replace(owner='John')
print(johhns_account)
janes_account = default_account._replace(owner='Jane')
print(janes_account)

#2 deque是为了高效实现插入和删除操作的双向列表，适用于队列和栈
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
q.extendleft([1,2,3]) 
print(q)

d=deque('ghi') #make a new deque with three items
for ele in d:
    print(ele.upper())

d.append('j') #add a new entry to the right side
d.appendleft('f')#add a new entry to the left side
print(d)
print(d.pop())#return and remove the rightmost item
print(d)
print(d.popleft())
print(d)
print(d[0]) #peek at leftmost item
print(d[-1])#peek at rightmost item
print(d)
print(list(reversed(d)))
print('h' in d)
d.extend('jkl')
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
print(deque(reversed(d)))
d.clear()
print(d)
# print(d.pop())
d.extendleft('abc') #extendleft() reverses the input order
print(d)

#deque recipes
def tail(filename,n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f,n)


#3 defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict 
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

#official example
# s=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# s=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d=defaultdict(list)
for k,v in s:
    d[k].append(v)
print(sorted(d.items()))


d={}
for k,v in s:
    d.setdefault(k,[]).append(v)
print(sorted(d.items()))


s="mississippi"
d=defaultdict(int)
for k in s:
    d[k]+=1

print(sorted(d.items()))

def constant_factory(value):
    return lambda:value
d=defaultdict(constant_factory('<missing>'))
d.update(name='john',action='ran')
print('%(name)s %(action)s to %(object)s' % d)

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k,v in s:
    d[k].add(v)
print(sorted(d.items()))

#4 OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序,如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)


od=OrderedDict()
od['z']=3
od['y']=2
od['x']=1
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
print(list(od.keys()))

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self.__capacity = capacity
    
    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self.__capacity:
            last = self.popitem(last=False)
            print("remove:",last)
        if containKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key, value)

#5 Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1

print(c)
    
#collections模块提供了一些有用的集合类，可以根据需要选用

#rapid tallies[计数]
#tally occurrences of words in a list
cnt=Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word]+=1

print(cnt)

#find the ten most common words in Hamlet
import re 
words=re.findall(r'\w+',open('hamlet.txt').read().lower())
print(Counter(words).most_common(10))

c=Counter() #a new,empty counter
c=Counter('gallahad') #a new counter from an iterable
c=Counter({'red':4,'blue':2})#a new counter from a mapping
c=Counter(cats=4,dogs=8) #a new counter from keyword args


c=Counter(['egg','ham'])
print(c['bacon'])#counting of a missing element is zero

c['sausage']=0
print(c['sausage']) #counter entry with a zero count
del c['sauage'] #del actually removes the entry

c=Counter(a=4,b=2,c=0,d=-2)
print(sorted(c.elements()))

print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2,e=2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)
# print(c)

# print(sum(c.values()))
# c.reset()
# print(c)

c=Counter(a=3,b=3)
d=Counter(a=1,b=2)
print(c+d) # add two counters together:c[x]+c[x]
print(c-d) # subtract (keeping only positive counts)
print(c & d)#intersection:min(c[x],d[x])
print(c | d)


c=Counter(a=2,b=-4)
print(+c)
print(-c)

#OrderedDict
d=OrderedDict.fromkeys('abcde')
print(d)
d.move_to_end('b',last=True)
print(d)
print('/'.join(d.keys()))
d.move_to_end('b',last=False)
print("/".join(d.keys()))

#examples and recipes
#regular unsorted dictionary
d={'banana':3,'apple':4,'pear':1,'orange':2}
#dictionary sorted by key
print(OrderedDict(sorted(d.items(),key=lambda t:t[0])))
#dictionary sorted by value
print(OrderedDict(sorted(d.items(),key=lambda t:t[1])))
# dictionary sorted by length of the key string
print(OrderedDict(sorted(d.items(),key=lambda t:len(t[0]))))
