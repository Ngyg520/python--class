"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:小练习.PY
@ide:PyCharm
@time:2018-08-02 11:17:26
"""
#小练习:
#1.创建一个数据库teacher
#创建一个表tea,字段(id(主键),name,age,sex)
#3.往tea表中插入数据(张,20,男)
#4.往tea表中插入数据(李四,30,女)
#修改(李四,30,女)这条数据为(王五,22,男)
#删除(张三,20,男)
#7.将表中所有的数据查询出来

import sqlite3

connect=sqlite3.connect('teacher.db')#创建数据库-----数据库连接
cursor=connect.cursor()#获取数据库游标

tea_table="create table tea(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,sex TEXT)"
# cursor.execute(tea_table)#第二步

insert_sql="insert into tea(name,age,sex)VALUES ('张三',20,'男')"
insert_sql="insert into tea(name,age,sex)VALUES ('李四',30,'女')"
# cursor.execute(insert_sql)#第三,四步

update_sql="update tea set name='%s',age=%d,sex='%s' WHERE id=2"%('王五',22,'男')
# cursor.execute(update_sql)#第五步

delete_sql="delete from tea WHERE id=1"
# cursor.execute(delete_sql)#第六步

select_sql='select * from tea'
result=cursor.execute(select_sql)
for x in result:
    print(x)

connect.commit()#执行提交
cursor.close()#关闭游标
connect.close()#关闭数据库

