__author__ = 'shenyao'
#python对smtp的支持有smtplib和email两个模块
#email负责构造邮件,smtplib负责发送邮件

#1 构造一个纯文本的邮件
#from email.mime.text import MIMEText
#from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils  import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#2 通过SMTP发出去
#输入Email地址和口令
from_addr=input('From:')
password=input('Password:')
#输入收件人的地址
to_addr=input('To:')
#输入SMTP服务器的地址
smtp_server=input('SMTP Server:')

# msg=MIMEText('hello,send by Python..,','plain','utf-8')
#发送HTML邮件
msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')

msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()

import smtplib
server=smtplib.SMTP(smtp_server,25)#SMTP协议默认的端口是25
server.set_debuglevel(1)#打印出所有与SMTP服务器交互的信息
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())#as_string是吧MIMEText对象变成str
server.quit()

#发送附件
#邮件对象
from email.mime.multipart import MIMEMultipart
from email.mime.base      import MIMEBase
msg=MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#邮件正文是MIMEText:
msg.attach(MIMEText('send with file...','plain','utf-8'))

#添加附件就是加上一个MIMEBase,从本地读取一个文件
with open('tuning.png','rb') as f:
    #设置附件的MIME和文件名,这里是png类型,
    mime=MIMEBase('image','png',filename='tuning.png')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart
    msg.attach(mime)

#发送图片
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

#同时支持HTML和Plain格式
msg=MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...

#加密SMTP
smtp_server='smtp.gmail.com'
smtp_port=587
server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
#剩下的代码和前面的一样
server.set_debuglevel(1)
