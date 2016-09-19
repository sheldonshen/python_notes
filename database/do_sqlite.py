__author__ = 'shenyao'
# #python就内置了sqlite3,所以在python中可以直接使用sqlite3,不需要安装任何东西,直接使用
# #导入SQLite驱动
# import sqlite3
# #连接到SQlite数据库
# #数据库文件是test.db
# #如果文件不存在,会自动在当前目录创建
# conn=sqlite3.connect('test.db')
# #创建一个Cursor
# cursor=conn.cursor()
# #执行一条SQL语句,创建user表\
# print(cursor.execute('create table user(id varchar(20) primary key,name varchar(20))'))
# #继续执行一条sql语句,插入一条记录
# print(cursor.execute('insert into user(id,name) values(\'1\',\'Micheal\')'))
# print(cursor.rowcount)
# #关闭cursor
# cursor.close()
# #提交事务
# conn.commit()
# #关闭Connection
# conn.close()

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
