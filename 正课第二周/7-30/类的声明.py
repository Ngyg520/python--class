"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:类的声明.PY
@ide:PyCharm
@time:2018-07-30 10:52:26
"""
class People(object):
    #__init__:这个初始化函数,会在对象被创建的时候,自动执行函数的调用,不需要手动打点调用
    #__init__:在类中并不是必须要定义的,但是当声明属性的时候,必须通过__init__函数声明
    def __init__(self,name,age,sex):
        self.name =name
        self.age =age
        self.sex =sex
        print('我是在对象被创建出来的时候自动调用执行的')
    #类中定义的函数,第一个参数必须是self,self也相当于一个形参,但是它是由解释器自动传值,self后面可以定义我们需要的参数
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('睡觉')
    def work(self):
        print('工作')

#创建一个对象,1自动执行了对象的初始换函数__init__( ),与此同时给初始化函数传递了参数.传递参数的时候,参数中实际上隐含了一个实参,这个参数会赋值给__init__( )函数中的形参self
p1=People('p1','20','男')
#当对象操作类中的属性的时候,对象名.属性名,操作类中函数的时候,对象名.函数名( )
print(p1.name)
p1.work()

#关于对象的创建过程(对象内存):
#每次通过people类创建对象的时候,python解释器都会给对象分配一个单独的内存空间,会将people类中定义的属性复制一份存放到对象的内存中,同时,内存具有唯一性的特征,创建出来的每一个对象都是唯一的,独立的,不允许重复
#虽然所有people类的对象都是name,age,sex这些属性,但是复制出来的每一个对象的属性名都是存在各自内存中的,并不是共用一个属性名,互不相干
p2=People('p2','30','女')
print(id(p1))
print(id(p2))