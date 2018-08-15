"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:__str__.PY
@ide:PyCharm
@time:2018-08-01 10:51:20
"""
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #__str__:当使用print输出对象的时候,只要定义了__str__(self)这个方法,就会打印出这个方法中return出来的数据
    def __str__(self):
        return'现在是%s这个对象'%self.name

s=Student('张三','20')
print(s)
s1=Student('李四','21')
print(s1)

#在python中如果一个方法名是__**__()的,那么这个函数就有特殊的功能,因此都称作魔法方法