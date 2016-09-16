'''
Created on Sep 16, 2016

@author: sheldonshen
'''
import base64
encoded = base64.b64encode(b'data to be encoded')
print(encoded)
data=base64.b64decode(encoded)
print(data)
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
#所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))

#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据
