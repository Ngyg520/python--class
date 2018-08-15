"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:预科
@author:Mr.Yang
@file:函数的参数.PY
@ide:PyCharm
@time:2018-07-23 09:45:55
"""

#1,必备参数(位置参数),实参和形参数量上必须要保持一致

def sum(a,b):
    c=a+b
    print(c)
sum(1,6)

#2,命名关键字参数:通过定义关键字来获取实参的值,与形参的顺序无关.
def show(name,age):
    print('姓名是:%s-年龄是:%s'%(name,age))
show(age=20,name='张三')

#3.默认参数
#使用场景:数据库连接,地址和端口可以设置默认
#使用默认参数的时候,如果给形参传递了实参,则会接受实参的值.如果没有给这个形参传递实参,则形参会采用默认值

def show_one(user='zhangsan',password='123456789'):
    print('账号是%s'%user)
    print('密码是%s'%password)
show_one('李四','54554')

#4,可变参数(不定长参数)
#形参的数据会根据形参的数量的变换而变化
#*args:接收N个位置参数转化成元组的形式
def show_two(*args):
    print(type(args))
    print(args)
show_two(1)
show_two(1,2,3)
show_two('曹森')

#4-2:关键字参数
#**kwargs:把N个关键字参数,转化成了字典.
def show_three(**kwargs):
    print(type(kwargs))
    print(kwargs)
show_three(name='张三',age='20',sex='男')

#尝试写一个函数:把以上所有参数填写进去
def show_all(name,*args,age=20,mother,**kwargs):
    print('----',name)
    print('===',args)
    print('\\\\',age)
    print('---',mother)
    print('====',kwargs)
show_all('张三',*(10,20),age=34,mother='啊实打实',**{'sex':'女','father':'马云'})