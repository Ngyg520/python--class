"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:aqlist3的基本用法.PY
@ide:PyCharm
@time:2018-08-02 09:10:35
"""
#什么是数据库:用于保存大量的,格式统一的数据,比如name,age,sex,score.数据库内部的结构是由多个表table构成,每一个表中由很多的字段构成
#数据库管理多张表,表管理多个字段,字段里面存着数据


#重要!!!!
#数据库分为:
#关系型数据库和非关系型数据库两种

#关系型数据库的
# 特点:
# 表和字段,数据和数据之间都存着关系
#优点:
#1.数据之间都存在着相互的联系,有利于数据之间的增删改查
#2.关系型数据库有事务操作,能过保证数据的完整性和一致性
#缺点:
#1.数据和数据之间存在着关系,它德底层运行了大量的算法,这样会降低系统的效率和性能
#2.面对海量的数据,增删改查和数据的维护显得无能为力

#常见的关系型数据库:sqlist3,MySQl,Oracle,SQLServer

#非关系型数据库
#特点:数据和数据之间不存在着联系,他们是单独存在的
#优点:
#1.对海量的数据进行增删改查
#2.对海量的数据进行维护和处理的效率很高

#缺点:
#1.数据库和表之间没有关系,所以也没有强大的事务关系,更没有办法保证数据的安全性和完整性
#2.虽然处理海量的数据效率很高.但是安全性很差

#常见的非关系型数据库:redis,MongoDB



#sqlist3是python内置的一种轻量级的数据库
import sqlite3

#数据库的操作的三个步骤:
#1.先连接数据库文件
#2.进行数据的写入和读取
#3.关闭数据库


#connect( ):负责数据库连接的一个函数,当要连接的数据库文件不存在的时候,会默认在当前目录下自动创建一个新的数据库文件
connect=sqlite3.connect('databace.db')

#2.要操作数据库,先要获取数据库游标,通过游标来操作表,接着对表进行增删改查
cursor=connect.cursor()

#3.创建表,对表里面的数据进行增删改查

#(通过SQL语句来创建一个表)
#student:表名
#id,name,age,score:表的字段
#INTEGER,TEXT,FLOAT:数据类型
#PRIMARY KEY:给id这个字段添加约束,将id这个字段作为主键
#主键:主键是唯一的,不允许重复,主要是给某一条数据设置一个唯一的标识,方便数据的查找和定位
create_table="create table student(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,score FLOAT)"
#通过游标执行创建表的sql语句
# cursor.execute(creat_table)


#向表中插入数据(sql语句)
insert_sql="insert into student(name,age,score)VALUES ('李四',20,98.8)"
# cursor.execute(insert_sql)

#更改表中的数据(sql语句)
#where后面跟的筛选条件
update_sql="update student set name='%s',age=%d,score=%.1f WHERE id=2"%('高翔',30,99.9)
# cursor.execute(update_sql)

#查询表中的数据(sql语句)
# * 查询所有数据
select_sql='select * from student'
result=cursor.execute(select_sql)
print(result)
print(result.fetchone())
#fetchone():获取结果集的一条数据,返回结果是一个由字段对应的数据组成的一个元组

#fetchall():获取结果集中的所有数据,一条数据对应着一个元组,然后再将这些元组嵌套在列表中进行返回
# print(result.fetchall())
# res=result.fetchall()
# for tuple_test in res:
#     print('id是:%s'%tuple_test[0])
#     print('name是:%s' % tuple_test[1])
#     print('age是:%s' % tuple_test[2])
#     print('score是:%s' % tuple_test[3])
#第二种遍历方式:注释上一个才可执行
for x in result:
    print(x)

#删除表中的数据(sql语句)
delete_sql="delete from student WHERE  id=1"
cursor.execute(delete_sql)

#执行提交的操作
connect.commit()
#关闭游标
cursor.close()
#关闭数据库
connect.close()

#小练习:
#1.创建一个数据库teacher
#创建一个表tea,字段(id(主键),name,age,sex)
#3.往tea表中插入数据(张,20,男)
#4.往tea表中插入数据(李四,30,女)
#修改(李四,30,女)这条数据为(王五,22,男)
#删除(张三,20,男)
#7.将表中所有的数据查询出来
