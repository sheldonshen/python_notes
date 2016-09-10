__author__ = 'shenyao'
#pickling,serialization,marshalling,flattening
#把变量从内存中变成可存储或传输的过程称之为序列化,pickling
#把变量内容从序列化的对象重新读到内存里称之为反序列化,unpickling
import pickle
d=dict(name="Bob",age=20,score=88)
print(pickle.dumps(d)) #dumps将对象序列化bytes

with open("dump.txt",'wb') as f:
    pickle.dump(d,f) #dump将一个对象序列化并写入文件(file-like Object)

with open("dump.txt",'rb') as f:
    d=pickle.load(f)#从一个file-like Object对象直接反序列化出对象
    print(d)

#pickle只能用于python,使用pickle只能保存那些不重要的数据,不能成功的反序列化也没有关系
