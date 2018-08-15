"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:7-26
@author:Mr.Yang
@file:json&pickle模块.PY
@ide:PyCharm
@time:2018-07-26 15:41:38
"""
import json
import pickle

#json:是采取键值对的结构组成的一组数据,是一种比较轻量级的数据交换格式,主要用在服务器和前端之间的数据传递
#json数据相对于其他格式的数据,数据量小,传输速度快,解析效率高,格式较为统一,解析起来比较方便.

#--------------------------------json-------------------------------------
dict1={"name":"maria",'age':'20','is_male':True}
#将字典转换成字符串
#json中bool值:true/false
#python值:True/False
#json.dumps会将字典中所有的单引号改变成json中标准的双引号

#-----------------序列化:将python中的对象写入到文件当中----------------------
# data = json.dumps(dict1)
# print(type(data))
# print(data)
# f=open('test.txt','w',encoding='utf-8')
# f.write(data)
# f.close()

#--------------------反序列化:将文件中的字符串转化成python对象----------------
f_read=open('test.txt','r',encoding='utf-8')
res=f_read.read()
print(type(res))
print('读',res)
data_2=json.loads(res)
print(type(data_2))
print(data_2)
print(data_2['name'])
print(data_2['age'])

#------------------------------------pickle------------------------------------
# pickle模块和json用法一样.(基本上使用json足够)
# pickle和json的区别:
# 1.json只能处理基本的数据类型,pickle能够处理所有的python类型
# 2.json用于各种语言之间的字符转换,pickle只能用于python对象的持久化或者python程序之间对象的网络传输

