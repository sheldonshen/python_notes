__author__ = 'shenyao'
#metaclass是类的模板,所以必须从type类型派生
class ListMetaclass(type):
    #参数解释: cls:当前准备创建的类的对象
    #          name:类的名字
    #          bases:类继承的父类集合
    #          attrs:类的方法集合
    def __new__(cls, name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

#metaclass=ListMetaclass 传入关键字参数metaclass,它指示python解释器在创建MyList时,要通过
#ListMetaclass.__new__()来创建,在此,我们可以修改类的定义,比如,加上新的方法,然后,返回修改后的定义
class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
print(L)

#而普通的list方法没有add方法
L2=list()
L2.add(1)#list' object has no attribute 'add'




