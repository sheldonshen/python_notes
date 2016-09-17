__author__ = 'shenyao'
#第一个GUI程序
from tkinter import *
class Application(Frame):#Frame是可以容纳其他Widget的父容器(Widget)
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel=Label(self,text="Hello,world!")
        self.helloLabel.pack()#把widget加入到父容器中
        self.quitButton=Button(self,text="Quit",command=self.quit)#当Button被点击时,触发self.quit()使程序退出
        self.quitButton.pack()

app=Application()#实例化Application
# 设置窗口标题
app.master.title("Hello,World")
# 主消息循环
app.mainloop()

#输入文本
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text="Hello",command=self.hello)#当Button被点击时,触发self.hello()使程序退出
        self.alertButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'defaultInput'#default input
        messagebox.showinfo('Message','Hello,%s' % name)

app=Application()
#设置窗口标题
app.master.title="Hello,World"
#主消息循环
app.mainloop()

#Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写
