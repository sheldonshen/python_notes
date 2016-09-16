'''
Created on Sep 16, 2016

@author: sheldonshen
'''
import hashlib
#目的是为了发现原始数据是否被人篡改过。
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1=hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update("python hashlib?".encode("utf-8"))
print(sha1.hexdigest())

#由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

#def calc_md5(password):
#    return get_md5(password + 'the-Salt')

#经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令
