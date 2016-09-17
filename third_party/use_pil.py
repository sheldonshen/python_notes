__author__ = 'shenyao'
from PIL import Image
#图像缩放
#打开一个jpg图像文件，注意是当前路径
im=Image.open('test.jpg')
#获得图像尺寸
w,h=im.size
print("Original image size:%sx%s" % (w,h))
#缩放到50%
im.thumbnail((w//2,h//2))
print("Resize image to %sx%s" %(w//2,h//2))
#把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg','jpeg')

#模糊效果
from PIL import Image,ImageFilter
#打开一个jpg文件,注意是当前文件
im=Image.open('test.jpg')
#应用模糊滤镜
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')

#PIL的ImageDraw提供了一系列绘图的方法,让我们直接绘图,比如要生成字母验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240 * 60
width=4*60
height=60
#创建Image对象
image=Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
font=ImageFont.truetype('E:\\toshiba\\PortableApps.com\\PortableApps\\OpenOfficePortable\\App\Fonts\\Arimo-Bold.ttf',36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

#PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理
#https://pillow.readthedocs.org/,PIL官方文档
