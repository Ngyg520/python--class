"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:calssmethod和staticmetho装饰器.PY
@ide:PyCharm
@time:2018-07-31 11:00:24
"""
class People(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#work  eat叫做实例方法,只能通过对象才能调用
    def eat(self):
        print('吃饭',self)
#classsmethod.将一个实例方法,转换成一个类方法
#类方法的调用:即可以通过类名调用,也可以通过对象调用,
# 类方法的一个参数需要修改成cls,因为当实例方法转换成类方法的时候,cls接受的是当前类People而不是对象
#类方法并不能调用属性
    @classmethod
    def work(cls):
        print('工作',cls)


#@staticmethod将实例方法转化成了静态方法,
# 静态方法中的第一个参数可以不用设置,已经失去了在实例方法中self的特殊含义,变成了一个普通的函数
    @staticmethod
    def smoke():
        print('整天西雾霾')

p1=People('张三','29')
#eat叫做实例方法,只能通过对象才能调用
p1.eat()
#类方法的调用:即可以通过对象调用,也可以通过类名调用,
p1.work()
People.work()
#静态方法:可以不设置任何参数,而且它可以类名调用,也可以通过对象调用
p1.smoke()
People.smoke()


#例子:
#由于类方法不能调用属性,所以不涉及到属性使用的地方都可以使用@classmethod来给一个函数声明为类方法,使用到属性的地方可以声明为实例方法
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    @classmethod
    def open_file(cls):
        file_test=open('student.txt','w',encoding='utf-8')
        return file_test
    #定义一个实例方法,用于保存数据
    def save_data(self,file_test):
        file_test.write(self.name+''+self.score)
        print('写入成功')
    #关闭文件的类方法
    @classmethod
    def close_file(cls,file_test):
        file_test.close()
        print('关闭成功')
#1.通过调用类方法open_file()的执行,可以获取open_file函数里面返回的file_test文件操作句柄,并把它赋值给f这个变量
f=Student.open_file()
student_one=Student('张三','180')
#2.将f变量里面保存着的文件操作句柄,继续传值给save_data()函数,用于调用write()函数写入数据
student_one.save_data(f)
#3.将f变量里面保存着的文件操作句柄,继续传值给close_file这个类方法,用于调用close()函数关闭文件
Student.close_file(f)