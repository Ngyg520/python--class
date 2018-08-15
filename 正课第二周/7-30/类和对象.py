"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:类和对象.PY
@ide:PyCharm
@time:2018-07-30 09:54:24
"""
#类和对象的基本定义:
#类:具有相同属性或者行为的事物通常为类.
#对象:从类中具体事例化出来的一个具体事物的存在.

#类和对象的关系:对象是类的实例,类是对象的模板.
#区分类和对象:
#1.车(类),王震宇的二手奥拓(对象)
#2.狗(类).曹向阳的藏獒(对象)
#3.水果(类),于胜阳啃那个榴莲(对象)

#面向对象编程中的类和对象:类在面向对象过程中,是一种抽象化的概念,类是不会占据内存空间的,类主要是为了辅助创建对象而存在的.对象才是面向对象编程的核心.所有函数的执行还有变量的调用都必须通过对象才能完成,对象在内存中是实际存在的,它会消耗内存空间,对象也称为实例化对象.

#面向过程中类的作用,通常情况下,会在类中指定一些属性和行为,当使用类实例化对象的时候,那么该对象就用于类指定的属性和行为

#类是由每一个对象共同抽象化出来的概念.至于类中需要指定哪些属性和行为,是由对象决定的,因为具体操作这些属性和行为的就是对象

#面向对象编程的时候,首先考虑如何设计一个类,类中的属性和行为是对象需要的属性和行为类决定的

#假如声明一个人类:
#人类需要的属性:姓名,年龄,性别(属性)
#人类需要的行为;吃饭睡觉工作( 行为:函数)

#calss:声明类的关键字
#people:自定义的一个类名,遵循大驼峰命名法.
#object:表示当前类people的父类,也称为基类或者根类,表示一种继承关系
class People(object):

    #__init__:对象的初始化函数,该函数就是用于指定对象属性的,
    #name/age/sex:叫做__init__函数的形参,等待着实参来传值
    def __init__(self,name,age,sex):
        #self.name,self.age,self.sex:人的属性
        self.name=name
        self.age=age
        self.sex=sex
    #eat/sleep/work:人的行为
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('睡觉')
    def work(self):
        print('工作')

#类已经声明完了,可以根据类来创建对象
#创建张三这个对象
zhangsan=People('张三','23','男')
print(zhangsan.name)
print(zhangsan.age)
print(zhangsan.sex)
zhangsan.eat()
zhangsan.sleep()
zhangsan.work()

#创建一个李四这个对象
lisi=People('李四','30','女')
print(lisi.name)
print(lisi.age)
print(lisi.sex)
lisi.eat()
lisi.sleep()
lisi.work()