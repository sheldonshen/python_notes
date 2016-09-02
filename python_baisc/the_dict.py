__author__ = 'shenyao'
names=['Micheal','Bob','Tracy']
scores=[95,97,96]

d={'Micheal':95,'Bob':97,'Tracy':96}
#这种key-value存储方式,在存放进入的时候，必须根据key算出value的存放位置,
#这样，取得时候才能根据根据key直接拿到value
print(d['Micheal'])

d['Adam']=23
print(d['Adam'])
#print(d['abc']) KeyError
print('abc' in d) #通过in判断key是否存在
print("Bob" in d)

print(d.get('Thomas')) #None
print(d.get('Thomas',-1)) #default value

print(d.pop('Tracy')) #删除
print(d)


#1 dict的key必须是不可变对象,这是因为dict根据key来计算value的位置
#如果每次计算相同的key得出的结果不同,那dict内部就完全混乱了
#这个通过key计算位置的算法称为哈希算法(Hash)
key=[1,2,3]
d[key]='a list' #TypeError:unhashable type:'list'


