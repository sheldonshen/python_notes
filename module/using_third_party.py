'''
Created on Sep 6, 2016

@author: sheldonshen
'''
from PIL import Image
im = Image.open('download.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100)) #缩放图片大小
im.save('thumb.jpg','JPEG')


#模块搜素路径
#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
#搜索路径存放在sys模块的path变量中
import sys
print(sys.path)#当前的搜索目录
sys.path.append("/search/dir")

#添加自己的搜索目录的2种方法
#1sys.path.append("/search/dir")
#2设置环境变量PYTHONPATH
