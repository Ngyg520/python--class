"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:__slots__的用法.PY
@ide:PyCharm
@time:2018-07-31 09:18:09
"""
#__slots__:主要是用于限制一个类的对象能添加的属性有哪些
class People(object):
    #以元组的形式,定义能添加的属性,除此之外的属性不能被添加,即对动态绑定属性发挥作用,也对__init__函数当中添加的属性发挥作用
    __slots__ = ('name','age','weight')
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        # self.height=height
p1=People('张三','20','180',)
# print(p1.height)
# p1.height='172'
# print(p1.height)