'''
Created on Sep 9, 2016

@author: sheldonshen
'''
#StringIO的操作只能是str,
#BytesIO用来操作二进制数据
#BytesIO实现了在内存中读写bytes
from io import BytesIO
f=BytesIO()
print(f.write("中文".encode('utf-8')))#写入通过ｅｎｃｏｄｅ之后的bytes
print(f.getvalue())

with BytesIO(b'\xe4\xb8\xad\xe6\x96\x87') as f:
    print(f.read().decode("utf-8"))#输入decode之后的str

#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
