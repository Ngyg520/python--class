"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:__new__.PY
@ide:PyCharm
@time:2018-08-01 14:03:53
"""
#依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass

#依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass

#__new__至少要有一个参数cls,代表要实例化的类,cls这个参数是在实例化时,有python解释器自动提供的
#__init__有一个参数self,就是这个__new__返回出来的实例,__init__函数就可以在__new__的基础上完成一些初始化的操作
#我们可以把类当做制造商,__new__方法就是前期的原材料购买环节,__init__方法就可以在原材料的基础上进行加工.初始化商品

class A(object):
    def __init__(self):
        print('这是__init__方法')
    def __new__(cls):
        print('这是__new__方法')
        return object.__new__(cls)#__new__必须要有返回值,返回实例化出来的实例

a=A()