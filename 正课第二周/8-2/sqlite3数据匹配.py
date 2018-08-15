"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:sqlite3数据匹配.PY
@ide:PyCharm
@time:2018-08-02 14:11:28
"""
import sqlite3
connect=sqlite3.connect('databace.db')
cursor=connect.cursor()
sql="select * from student where name like '张_'"
#like:主要是用于匹配数据库中的多条记录
#'张'匹配以'张'开头,并且只匹配'张'开头后一个字符串的数据

sql_1="select * from student where name like '%翔'"
#%a:匹配以a结尾的数据

sql_2="select * from student where name like '李%'"
#a%:以a开头的数据

sql_3="select * from student where name like '%五%'"
#%a%:匹配数据中包含a的数据
res=cursor.execute(sql)
for id,name,age,score in res:
    print(id,name,age,score)
connect.commit()
cursor.close()
connect.close()