"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:预科
@author:Mr.Yang
@file:全局变量与局部变量的作用域.PY
@ide:PyCharm
@time:2018-07-23 11:24:28
"""

#变量的作用域:是指一个变量所产生的作用范围,也就是说在哪一个范围内变量能够被解释器所识别
#变量分为:全局变量和局部变量
#全局变量:一般声明在函数的外部
#全局变量的作用域:整个.py文件内都可以使用,都可以被识别


#局部变量:一般声明在函数的内部.
#局部变量作用域:只能在函数的内部使用,超出范围,变量就不能再使用

#list1相当于全局变量,作用域是整个.py文件
list1=[]
def add_test():
    #a:局部变量,只能在函数内使用
    a = 1
    list1.append(a)
    print('局部变量:%s'%a)
    print(list1)
add_test()
list1.append(2)
print('全局变量:%s'%(list1))
print(list1)

name= '张三'

def show_name():
    #默认情况下,如果全局变量和局部变量名相同,在函数内部是无法识别到函数外部的全局变量的
    #local variable 'name' referenced before assignment:局部变量在声明之前被引用(先应用后声明的错误)
    #因为变量的引用的时候,会采取就近原则,会看最近的变量在哪,会发现最近的变量是name='李四',但是提取使用了name这个变量,然后再声明了name='李四,所以出现了先引用后声明的错误
    global name#global:将一个已经声明好的全局变量在函数内部重新声明,可以避免和同名的局部变量重名
    print('姓名:%s'%name)
    name='李四'
    print('姓名_1:%s'%name)

show_name()