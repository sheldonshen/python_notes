'''
Created on Sep 19, 2016

@author: sheldonshen
'''
#收取邮件分2步
#1使用poplib把邮件的原始文本下载到本地
#2使用email解析原始文本,还原为邮件对象

#通过POP3下载邮件
import poplib
from email.parser import Parser

#输入邮件地址，口令和POP3服务器地址
email=input('Email:')
password=input("Paasword:")
pop3_server=input('POP3 server:')

#连接到POP3服务器
server=poplib.POP3(pop3_server)
#可以打开或者关闭调试信息
server.set_debuglevel(1)
#可选：打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

#身份认证
server.user(email)
server.pass_(password)

#stat()返回邮件数量和占用的空间
print('Message:%s.Size:%s' % server.stat())
#list()返回所有邮件的编号
resp,mails,octets = server.list()
#可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

#获取最新一份邮件，注意索引号是从1开始的
index=len(mails)
resp,lines,octets=server.retr(index)

#lines存储了邮件的原始文本的每一行
#可以获得整个邮件的原始内容
msg_content=b'\r\n'.join(lines).decode('utf-8')
#稍后解析出邮件
msg=Parser().parsestr(msg_content)

#可以根据邮件索引号直接从服务器删除邮件
#server.dele(index)
#关闭连接
server.quit()


#解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils  import parseaddr

import poplib

msg=Parser().parsestr(msg_content)

#递归地打印Message对象的层次结构
#indent用法语缩进展示
def print_info(msg,indent=0):
    if indent==0:
        for header in ['From','To','Subject']:
            value=msg.get(header,'')
            if value:
                if header=='Subject':
                    value=decode_str(value)
                else:
                    hdr,addr = parseaddr(value)
                    name=decode_str(hdr)
                    #value= u'%s <%s>' % (name, addr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('' * indent,header,value))
    if(msg.is_multipart()):
        parts = msg.get_payload()
        for n,part in enumerate(parts):
            print('%spart %s' % (' ' * indent,n))
            print('%s----------------' % (' ' * indent))
            print_info(part,indent+1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type='text/html':
            content=msg.get_payload(decode=True)
            charset=guess_charset(msg)
            if charset:
                content=content.decode(charset)
            print("%sText:%s" %('  ' * indent,content + '...'))
        else:
            print('%sAttachment:%s' %(" " * indent,content_type))


def decode_str(s):  
    value,charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type','').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset=content_type[pos + 8:].strip()
    return charset

#用Python的poplib模块收取邮件分两步：第一步是用POP3协议把邮件获取到本地，
#第二步是用email模块把原始邮件解析为Message对象，然后，用适当的形式把邮件内容展示给用户即可
