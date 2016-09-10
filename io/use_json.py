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

def dict2student(d):#定义unpickling的规则(custom decoder)
    return Student(d['name'],d['age'],d['score'])

s=Student('Bob',20,88)
print(json.dumps(s,default=student2dict))#定义pickling规则
print(json.dumps(s,default=lambda obj:obj.__dict__))#利用lambda将class的实例变成dict

json_str='{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))#定义unpickling的规则

#小结
#Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块

#append some content from the official document
import json
#encoding
print(json.dumps(['foo',{'bar':('baz',None,1.0,2)}]))
print(json.dumps('\"foo\bar'))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c":0,"b":0,"a":0},sort_keys=True))
from io import  StringIO
io=StringIO()
print(json.dumps(['streaming API'],io))
print(io.getvalue())
#compact encoding
print(json.dumps([1,2,3,{'4':5,'6':7}],separators=(',',':')))
#pretty printing
print(json.dumps({'4':5,'6':7},sort_keys=True,indent=4))

#decoding
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
print(json.loads('"\\"foo\\bar"'))
# io = StringIO('["streaming API"]')
# print(json.loads(io))

#specializing json object decoding
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'],dct['imag'])
    return dct

print(json.loads('{"__complex__":true,"real":1,"imag":2}',object_hook=as_complex))

import decimal
print(json.loads('1.1',parse_float=decimal.Decimal))

#extending JSONEncoder
class ComplexEncoder(json.JSONEncoder):
    #custom JSONEncoder subclass,override the default method
    def default(self,obj):
        if isinstance(obj,complex):
            return [obj.real,obj.imag]
        #Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self,obj)

print(json.dumps(2+1j,cls=ComplexEncoder))
print(ComplexEncoder().encode(2+1j))
print(list(ComplexEncoder().iterencode(2+1j)))

#Encoders and Decoders

#Infinite and NaN Number Values
# print(json.dumps(float("-inf")))
# print(json.dumps(float('-inf')))
# json.dumps(float('nan'))

#repeated names within an object
weird_json = weird_json = '{"x": 1, "x": 2, "x": 3}'
print(json.loads(weird_json))

#
