__author__ = 'shenyao'
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    print("Data:",data.decode('utf-8'))

print("------模拟浏览器发送GET请求---------")
#模拟浏览器发送GET请求
#需要使用Request对象,通过往Request对象添加HTTP头,我们就可以把请求伪装成浏览器
#模拟Iphone6去请求豆瓣首页
req=request.Request("http://www.douban.com/")
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status',f.status,f.reason)
    for k,v in f.getheaders():
        print("%s:%s" %(k,v))
    print("Data:",f.read().decode("utf-8"))

#Post请求
#如果以POST发送一个请求,只需要把参数data以bytes形式传入
from urllib import request,parse
print("login to weibo.cn")
email=input("Email:")
passwd=input("Password:")
login_data=parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
print("login_data:",login_data)
req=request.Request("https://passport.weibo.cn/sso/login")
req.add_header('Origin','https://passport.weibo.cn/sso/login')
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header("Referer",'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print("%s:%s" %(k,v))
    print("Data:",f.read().decode('utf-8'))

print("---------------handler------------------")
#handler
#通过proxy去访问网站
proxy_handler=request.ProxyHandler({'http':'http://www.m1905.com'})
proxy_auth_handler=request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm','host','username','password')
opener=request.build_opener(proxy_handler,proxy_auth_handler)
with opener.open("http://www.1905.com/news/20160915/1088265.shtml?fr=home_lbt_02") as  f:
     print(f.read())

#urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
# 伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的

