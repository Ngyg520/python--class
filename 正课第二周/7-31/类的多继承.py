"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:类的多继承.PY
@ide:PyCharm
@time:2018-07-31 16:10:38
"""
#定义一个A类
class A(object):
    def print_test(self):
        print('A类')
class B(object):
    def print_test(self):
        print('B类')
class C(A,B):
    def print_test(self):
        print('C类')

#面试题:
#在上面多继承的例子中,如果父类A,B都有一个同名的方法,name通过子类调用的时候,会调用哪一个?
obj_c=C()
obj_c.print_test()
#先调用自己的类,再调用父类
print(C.__mro__)#可以查看C类的对象搜索方法时的先后顺序

