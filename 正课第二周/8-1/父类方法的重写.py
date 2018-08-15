
"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:父类方法的重写.PY
@ide:PyCharm
@time:2018-08-01 09:13:20
"""
#子类重写父类方法:
#1.完全重写,子类不继承父类所有函数的功能,直接将父类的函数的功能进行覆盖
#2.部分重写,父类函数中的功能符合子类的需求,但是需要添加一些功能

#注意点:
#1.子类重写父类方法的时候,子类定义的函数名必须和父类的函数名保持一致
#2.使用super( ) 函数是部分重写,不使用super()函数是完全重写

class People(object):
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def work(self):
        print('我是父类的work函数')
class Man(People):
    def __init__(self,name,age,height,sex,weight):
        #super函数:是让Man类对象self,调用父类的初始化函数__init__()
        super(Man,self).__init__(name,age,height)
        # self.name = name
        # self.age = age
        # self.height = height
        self.sex=sex
        self.weight=weight
    def work(self):#覆盖父类的work函数,
        print('我就说两句,不多说')
        print('好开森')

p1=People('张三','20','180')
m1=Man('李四','20','190','男','56')
m1.work()#调用父类的函数


#例子:
class Student(object):
    file_test=open('student.txt','w',encoding='utf-8')
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def save_data(self):
        Student.file_test.write(self.name+' '+self.score)#类变量,可以直接调用

    def close_file(self):
        Student.file_test.close()

# s1=Student('张三','180')
# s1.save_data()
# s1.close_file()

class ReadStudent(Student):
    #部分重写父类的save_data方法
    def save_data(self):
        super(ReadStudent,self).save_data()
        ReadStudent.file_test.close()
        #添加读取的新功能
        f=open('student.txt','r',encoding='utf-8')
        res=f.readlines()
        print('读取的结果是:',res)

r1=ReadStudent('李四','20')
r1.save_data()#使用需要注释55--57行