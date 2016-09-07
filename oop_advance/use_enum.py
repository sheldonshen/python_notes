__author__ = 'shenyao'
from enum import Enum,unique
Month=Enum('Month',('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)


@unique#@unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun=0 #Sum的value被设定为0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1==Weekday.Mon)
print(day1==Weekday.Sun)
print(Weekday(1))
print(day1==Weekday(1))
#print(Weekday(7))
for name,member in Weekday.__members__.items():
    print(name,",",member)
#official document
#creating an enum
class Color(Enum):#class Color is an enumeration
    red=1 #enumeration member
    green=2 #enumeration member
    blue=3  #enumeration member has name and value(the name of Color.blue is blue,the value of Color.blue is 3)

print(Color.blue)
print(repr(Color.blue))
print(type(Color.blue))
print(isinstance(Color.blue,Color))
print(Color.blue.name)
#enum module
#1 module content
#  class enum.Enum
#  class enum.IntEnum
#  enum.unique

#enumerations support iteration,in definition order
class Shake(Enum):
    vanilla=7
    chocolate=4
    cookies=9
    mint=3

for shake in Shake:
    print(shake)

apples={}
#enumeration members are hashable
apples[Color.red]='red delicious'
apples[Color.green]='granny smith'
print(apples)
assert apples == {Color.red: 'red delicious', Color.green: 'granny smith'}


#programmatic access to enumeration members and their attributes
print(repr(Color(1)))
print(Color(3))
print(repr(Color['red']))
print(repr(Color['green']))
member=Color.blue
print(member.name)
print(member.value)

#duplicating enum members and values
class Shape(Enum):
    square=2
    diamond=1
    circle=3
    alias_for_square=2
    #square=3 #Attempted to reuse key: 'square'
print(repr(Shape.square))
print(repr(Shape.alias_for_square))
print(repr(Shape(2)))

#ensuring unique enumeration values
@unique
class Mistake(Enum):
    one=1
    two=2
    three=3
    #four=3#duplicate values found in <enum 'Mistake'>: four -> three

#print(Mistake.four)

#iteration
print(list(Mistake))
for name,member in Mistake.__members__.items():
    print(name,member)

for name,member in Shape.__members__.items():
    print(name,member)

print([name for name,member in Shape.__members__.items() if member.name != name])

#comparisons
print(Color.red is Color.red)
print(Color.red is Color.blue)
print(Color.red is not Color.blue)
#print(Color.red < Color.blue)
print(Color.blue == Color.red)
print(Color.blue != Color.red)
print(Color.blue == Color.blue)
print(Color.blue == 3)

#allowed  members and attributes of enumerations
class Mood(Enum):
    funky = 1
    happy = 3

    def describe(self):
        #self is the member here
        return self.name,self.value

    def __str__(self):
        return "my custom str! {0}".format(self.value)

    @classmethod
    def favorite_mod(cls):
        #cls here is the enumeration
        return cls.happy

print(Mood.favorite_mod())
print(Mood.happy.describe())
print(str(Mood.happy))

#restricted subclassing of enumerations
#class MoreColor(Color):
    #pink=17 #Cannot extend enumerations

class Foo(Enum):
    def some_behavior(self):
        pass

class Bar(Foo):
    happy=1
    sad=2

print(Bar.happy)

#picking
from test.test_enum import Fruit
from pickle import dumps,loads
print(Fruit.tomato is loads(dumps(Fruit.tomato)))


#Functional API
Animal = Enum('Animal','ant bee cat dog')
print(Animal)
print(repr(Animal.ant))
print(Animal.ant.value)
print(list(Animal))

#Derived Enumerations
from enum import IntEnum
class Shape(IntEnum):
    circle=1
    square=2

class Request(IntEnum):
    post=1
    get=2

print(Shape==1)
print(Shape.circle==1)
print(Shape.circle==Request.post) #True

class Color(Enum):
    red=1
    blue=2
print(Shape.circle==Color.red)   #False

print(int(Shape.circle))
print(['a','b','c'][Shape.circle])
print([i for i in range(Shape.square)])

#others
class IntEnum(int,Enum):
    pass

#interesting examples
class AutoNumber(Enum):
    def __new__(cls):
        value=len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_=value
        return obj

class Color(AutoNumber):
    red=()
    green=()
    blue=()

print(Color.green.value==2)

class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Grade(OrderedEnum):
    A=5
    B=4
    C=3
    D=2
    F=1

print(Grade.C < Grade.A)


class DuplicateFreeEnum(Enum):
    def __init__(self,*args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError("alias not allowed in DuplicateFreeEnum: %r-->%r" % (a,e))

class Color(DuplicateFreeEnum):
    red=1
    green=2
    blue=3
    #grene=2

#Planet
class Planet(Enum):
     MERCURY = (3.303e+23, 2.4397e6)
     VENUS   = (4.869e+24, 6.0518e6)
     EARTH   = (5.976e+24, 6.37814e6)
     MARS    = (6.421e+23, 3.3972e6)
     JUPITER = (1.9e+27,   7.1492e7)
     SATURN  = (5.688e+26, 6.0268e7)
     URANUS  = (8.686e+25, 2.5559e7)
     NEPTUNE = (1.024e+26, 2.4746e7)

     def __init__(self,mass,radius):
         self.mass=mass
         self.radius=radius

     @property
     def surface_gravity(self):
     # universal gravitational constant  (m3 kg-1 s-2)
          G = 6.67300E-11
          return G * self.mass / (self.radius * self.radius)

print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)

#how are enums different
class FieldTypes(Enum):
    name=0
    value=1
    size=2
print(FieldTypes.size.value)
#print(FieldTypes.value.size)
print(dir(Planet))
print(dir(Planet.EARTH))
