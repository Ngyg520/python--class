"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:练习.PY
@ide:PyCharm
@time:2018-08-02 21:54:15
"""
import sqlite3
connect=sqlite3.connect('Grades.db')
cursor=connect.cursor()
create_table="CREATE TABLE Grades (num INTEGER PRIMARY KEY,name TEXT,grade INTEGER,rank INTEGER)"

insert_sql="INSERT INTO Grades (num,name,grade,rank) VALUES (1,’zhangsan’,398,20)"


