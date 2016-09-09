'''
Created on Sep 9, 2016

@author: sheldonshen
'''
#自定义Dict类，这个类的行为和dict一致,但是可以通过属性来访问
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except:
            raise AttributeError(r"r'Dict' object has no attribute '%s' " % key)
    
    def __setattr__(self,key,value):
        self[key]=value

#引入python的unittest模块
#编写一个测试类，从unittest.TestCase继承
#以test开头的方法就是测试方法
import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b="test")
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,"test")
        self.assertTrue(isinstance(d,Dict))
    
    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,"value")
    
    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],"value")
    
    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']
    
    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty

    def setUp(self):
        print("setUp...")
    
    def tearDown(self):
        print("tearDown...")

if __name__=="__main__":
    unittest.main()
