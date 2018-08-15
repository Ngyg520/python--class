"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:property装饰器.PY
@ide:PyCharm
@time:2018-07-31 10:07:48
"""
#装饰器是以@开头,@结构也称为语法糖,装饰器主要是给现有的函数添加一些额外的功能
#@property
#@classmethod
#@staticmethod

#把一个函数变成一个属性

#property负责装饰一个实例方法,让其生成对应的getter和setter方法,调用时可以直接使用对象名.函数名的这种类似于属性调用的方法
class People(object):
    def __init__(self,name):
        self.__name=name
    #@property是将work函数声明为一个getter函数,getter用于取值的操作
    @property
    def work(self):
        return self.__name
    #声明一个work函数对应的setter函数,setter函数进行属性的赋值操作
    #@work中的这个work这个名称,必须要和上面的work函数名保持一致
    @work.setter
    def work(self,name):
        if isinstance(name,str):
            self.__name=name

        else:
            raise  ValueError('name is not "str" type!')
    #给work函数绑定一个deleter函数,用来删除属性
    @work.deleter
    def work(self):
        if hasattr(self,'_People__name'):
            del self.__name
            print('__name属性删除成功')
        else:
            raise  ValueError('__name atteribute不存在')


p1=People('张三')
#调用getter函数,对属性进行取值操作
res=p1.work
print(res)
#对象名.函数名如果在=号的左侧,这是在调用setter方法,给属性赋值,
# 等号右边的赋值就是实参,将会赋值给属性(形参name)
p1.work='李四'
print(p1.work)

del p1.work
