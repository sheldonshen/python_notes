__author__ = 'shenyao'
import json
d=dict(name="Bob",age=20,score=88)
print(json.dumps(d))#pickling
json_str='{"score": 88, "name": "Bob", "age": 20}'
print(json.loads(json_str))#unpickling


class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def student2dict(std):#定义pickling规则
    return {'name':std.name,'age':std.age,'score':std.score}

def dict2student(d):#定义unpickling的规则
    return Student(d['name'],d['age'],d['score'])

s=Student('Bob',20,88)
print(json.dumps(s,default=student2dict))#定义pickling规则
print(json.dumps(s,default=lambda obj:obj.__dict__))#利用lambda将class的实例变成dict

json_str='{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))#定义unpickling的规则

#小结
#Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块





