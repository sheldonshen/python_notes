'''
Created on Sep 7, 2016

@author: sheldonshen
'''
class Student(object):
    def get_score(self):
        return self._score
    
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must be 0~100")
        self._score=score
        
    @property #装饰器property
    def score(self):#get_score
        print("@property")
        return self._score
    
    @score.setter #装饰器score.setter
    def score(self,score):#set_score
        print("@score.setter")
        if not isinstance(score,int):
            raise ValueError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must be 0~100")
        self._score=score

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self,birth):
        self._birth=birth
    
    @property #age只有@propety为只读属性
    def age(self):
        return 2016-self._birth
    
    

s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(9999)

sp = Student()
s.score=99 #OK,实际转化为s.set_score(99)
print(s.score) #OK,实际转化为s.get_score()
#s.score=9999

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width=value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height=value
    
    @property
    def resolution(self):
        return self._width * self._height
    
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
