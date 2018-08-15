"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:对象属性的保护.PY
@ide:PyCharm
@time:2018-07-31 09:26:31
"""
#如果有一个对象,当需要对其属性进行修改的时候,有两种方法:
#1.对象名.属性名=属性值------------------>直接修改(不安全)
#2.对象名.方法名( )--------------------->间接修改

#为了更好的保护属性的安全,也就是不让属性被随意的修改,一般的处理方式:
#1,将属性定义为私有属性
#2.添加一个可以调用的方法(函数),通过调用方法来修改属性(还可以在方法中设置一些属性的条件)

class People(object):
    #私有属性
    def __init__(self,name,age,weight):
        #python设置私有属性,需要在属性前加两个_
        self.__name=name
        self.__age=age
        self._weight=weight
        #由于私有属性只能在类的内部使用,想要在外部获取私有属性的值,可以通过定义函数来完成
    def get_name(self):
        return self.__name
#添加修改属性
    def set_name(self,name):
        if isinstance(name,str):#(属性,限制)
            self.__name=name
        else:
            raise ValueError('name is not"str"type!')

p1=People('张三','20','180')
name=p1.get_name()
print(name)#打印出私有属性
# print(p1.__name)#私有属性无法直接调用
p1.set_name('李四')
print(p1.get_name())#对私有属性进行修改,并且要满足限制"str"
#一般也将_weight这种视为私有属性,不会再类的外部进行访问
print(p1._weight)


#面试题:
#python单_和双_的区别?
#1.__方法名__:内建方法,用户不能这样定义.例如:__init__
#2.__变量名(属性名):全私有属性(变量)/全保护属性(变量).只有类对象自己能访问,子类并不能访问这个属性
#3._变量名(属性名):半保护属性(变量),只有类对象和子类对象能访问到这些变量

#虽然从意义上讲单下划线和双下划线的变量(属性)都属于私有变量(属性),理论上外界不能访问的,但是Python并没有那么严格,仍然是可以强制访问的,因此python的私有仅仅是意义上的私有,只是种规范,可以不遵守
print('强制访问:',p1._People__name)