"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:对象的内存管理.PY
@ide:PyCharm
@time:2018-08-01 14:18:25
"""
#内存:操作系统的运行内存,一般用于启动一些程序,开启一些进程和线程,供程序调动使用
#计算机编程语言管理内存有两种方式:
#1,自动化管理内存,比如python
#2.手动管理内存,比如C

#自动与手动的区别
#自动:
#优点:开发效率更高,不用自己手动负责对象内存的释放
#缺点:可能出现对象在内存中释放不掉的情况,出现内存泄漏

#手动:指的是程序员来负责对象的内存释放.
#优点:对象的引用计算管理更加精准,不容易产生内存泄漏的现象(对象没有被释放,依然在内存中存在)
#缺点:消耗大量时间,开发效率低

#内存的分区;
#1.栈区:一般用于保存一些局部变量,指针等,这个区的内存有操作系统在程序运行结束的时候负责回收的
#2.堆区:创建的对象(list/tuple/dict/set/object)存储在堆区中,程序员主要管理的区就是堆区的内存
#3.全局区或者静态区:用于存放全局变量,全局变量占用的内存需要等待整个程序运行结束时,才能被回收,也是由操作系统进行回收,不受引用计数的限制
#4,常量区:用于存放一些字符串,整数,小数等常量,而常量所占用的内存是可以共享的,目的是为了节省内存空间,不受引用计数的限制,也是由操作系统统一回收常量区的内存
#5.代码编译器:由于存放经过解释器编译过后的二进制代码文件,由操作系统在程序运行结束后统一回收


#Python中的内存管理采用的是"引用计数"的方式,对一个对象的声明周期进行管理,如果一个的引用计数为0,则该对象会被解释器进行内存的回收,对象会在内存中随之消失,如果一个对象的引用计数不为0,则该对象会一直存放在内存中

#对象引用计数的变化:
#1.当对象被创建的时候,引用计数+1
#2.当对象被其他指针引用的时候,引用计数-1
#当对象被删除的时候,引用计数-1
#4.当程序结束的时候,引用计数为0
import time
class People(object):
    number=0
    def __init__(self):
        print('People对象被创建了')
        People.number+=1
        print('引用计数是:',People.number)
    def __del__(self):
        print('People生成的对象被删除了')
        People.number-=1
        print('引用计数是:',People.number)
p1=People()
p2=People()
p3=p2
time.sleep(1)#时间间隔
del p1
time.sleep(1)
del p2
time.sleep(1)