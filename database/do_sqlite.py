__author__ = 'shenyao'
#python就内置了sqlite3,所以在python中可以直接使用sqlite3,不需要安装任何东西,直接使用
#导入SQLite驱动
import sqlite3
#连接到SQlite数据库
#数据库文件是test.db
#如果文件不存在,会自动在当前目录创建
conn=sqlite3.connect('test.db')
#创建一个Cursor
cursor=conn.cursor()
#执行一条SQL语句,创建user表\
print(cursor.execute('create table user(id varchar(20) primary key,name varchar(20))'))
#继续执行一条sql语句,插入一条记录
print(cursor.execute('insert into user(id,name) values(\'1\',\'Micheal\')'))
print(cursor.rowcount)
#关闭cursor
cursor.close()
#提交事务
conn.commit()
#关闭Connection
conn.close()

#查询记录
import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
#执行查询语句
cursor.execute("select * from user where id=?",('1',))
#获得查询结果
values=cursor.fetchall()
print(values)

#在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
#要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
#如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。


#official document sqlite3
import sqlite3
#Connection object that represents the database
conn=sqlite3.connect('example.db')
#create a Cursor object
cursor = conn.cursor()
#create table
cursor.execute('''create table stocks(data text,trans text,symbol text,qty real,price real)''')
#insert a row of data
cursor.execute("insert into stocks values('2006-01-05','BUY','RHAT',100,35.14)")
#save(commit)the changes
conn.commit()
# we can also close the connection if we are done with it.
#just be sure any changes have been committed or they will be lost
conn.close()

import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()

t=('RHAT',)
c.execute('select * from stocks where symbol=?',t)
print(c.fetchone())

purchases=[('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),]
c.executemany('insert into stocks values(?,?,?,?,?)',purchases)
for row in c.execute("select * from stocks order by price"):
    print(row)

# create a user-defined function
import sqlite3
import hashlib

def md5sum(t):
    return hashlib.md5(t).hexdigest()

con = sqlite3.connect(":memory:")
con.create_function("md5",1,md5sum)
cur=con.cursor()
cur.execute('select md5(?)',(b"foo",))
print(cur.fetchone()[0])

#  create a user-defined aggregate function
import sqlite3
class MySum:
    def __init__(self):
        self.count=0
    def step(self,value):
        self.count += value

    def finalize(self):
        return self.count

con=sqlite3.connect(":memory:")
con.create_aggregate('mysum',1,MySum)
cur=con.cursor()
cur.execute('create table test(i)')
cur.execute('insert into test(i) values(1)')
cur.execute('insert into test(i) values(2)')
cur.execute('select mysum(i) from test')
print(cur.fetchone()[0])

# Cursor Objects
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table people(name_last,age)")

who='simon'
age=18
#this is the qmark style
cur.execute('insert into people values(?,?)',(who,age))
#and this is the named style
cur.execute('select * from people where name_last=:who and age=:age',{'who':who,'age':age})
print(cur.fetchone())

# executemany()
import sqlite3

class IterChars:
    def __init__(self):
        self.count = ord('a')
    def __iter__(self):
        return self
    def __next__(self):
        if self.count > ord('z'):
            raise StopIteration
        self.count+=1
        return (chr(self.count-1),) #this is a 1-tuple

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute('create table characters(c)')

theIter = IterChars()
cur.executemany("insert into characters(c) values(?)",theIter)
cur.execute('select c from characters')
print(cur.fetchall())

# using generator
import sqlite3
import string
def char_generator():
    for c in string.ascii_lowercase:
        yield(c,)

con=sqlite3.connect(':memory:')
cur=con.cursor()
cur.execute('create table characters(c)')
cur.executemany('insert into characters(c) values(?)',char_generator())
cur.execute("select c from characters")
print(cur.fetchall())

# executescript(sql_script)
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript("""
create table person(
        firstname,
        lastname,
        age
    );

    create table book(
        title,
        author,
        published
    );

    insert into book(title, author, published)
    values (
        'Dirk Gently''s Holistic Detective Agency',
        'Douglas Adams',
        1987
    );
""")

# Row Objects
import sqlite3
conn=sqlite3.connect(":memory:")
c=conn.cursor()
c.execute('''create table stocks
(date text, trans text, symbol text,
qty real, price real)''')

c.execute('''insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)
''')

conn.commit()
c.close()

conn.row_factory=sqlite3.Row
c=conn.cursor()
c.execute('select * from stocks')
r=c.fetchone()
print(type(r))
print(tuple(r))
print(len(r))
print(r[2])
print(r.keys())
print(r['qty'])
for member in r:
    print(member)
