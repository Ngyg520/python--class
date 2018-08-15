"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:单例类.PY
@ide:PyCharm
@time:2018-08-01 14:12:03
"""
#单例类:就某一个类只能生成一个对象
class Singleton(object):
    __instance=None#私有的全局变量为空
    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance=object.__new__(cls)
            return cls.__instance

a=Singleton()
a1=Singleton()
print(a)
print(a1)