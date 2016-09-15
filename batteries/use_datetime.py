__author__ = 'shenyao'
#datetime是python处理日期和时间的标准库

#获取当前日期和时间
from datetime import datetime #datetime模块包含一个datetime类
now = datetime.now()#获取当前datetime
print(now)
print(type(now))

#获取指定日期和时间
from datetime import datetime
dt=datetime(2015,4,19,12,20)#用指定日期时间创建datetime
print(dt)

#datetime转换为timestamp
#timestamp的值与时区无关
from datetime import datetime
dt=datetime(2015,4,19,12,20)#用指定日期时间创建datetime
print(dt.timestamp())
#注意python的timestamp是一个浮点数

#timestamp转datetime
from datetime import datetime
t=1429417200.0
dt=datetime.fromtimestamp(t) #使用os时区
print(dt) #本地时间(北京时间)
dt=datetime.utcfromtimestamp(t)
print(dt) #UTC时间(格林威治标准时间与北京时间差了8小时)

#str转换为datetime
from datetime import datetime
cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday) #转换后的datetime是没有时区的信息

#datetime转换为str
from datetime import datetime
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

#datetime加减
from datetime import datetime,timedelta
now = datetime.now()
print(now)
print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=12))

#本地时间转换为UTC时间
from datetime import datetime,timedelta,timezone
tz_utc_8=timezone(timedelta(hours=8)) #创建时区(UTC+8:00)
now=datetime.now()
print(now)
dt=now.replace(tzinfo=tz_utc_8)
print(dt) #如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

#时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
