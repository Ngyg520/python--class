#1.必备参数:实参和形参数量上必须要保持一致
def sum(a,b):
    c=a+b
    print(c)
sum(1,2)

#2.命名关键字参数,通过定义关键字来获取实参的值,与形参的顺序无关
def show(name,age):
    print('姓名是:%s-年龄是%s'%(name,age))
show(age=20,name='张三')

#3.默认参数
#一般可用于账号密码登录的函数,或者数据库连接的函数
def show1(name='mlxg',password='123456'):
    print('账号是:%s'%name)
    print('账号密码是:%s'%password)
#使用默认参数的时候,如果给形参传递了实参,则形参会接受实参的值.如果没有给这个形参传递实参,则形参会采用默认值
show1()
show1(password='678910')

#4.位置参数:形参的数量会根据实参的数量的变化而变化
#*args:接受N个位置参数,并且会把位置参数转换成元组的形式
def show2(*args):
    print(type(args))
    print(args)
show2(1)
show2(1,2)
show2(1,2,3)

#5.**kwargs:关键字参数
#**kwargs:把n个关键字参数,转换成字典的方式.
def show3(**kwargs):
    print(type(kwargs))
    print(kwargs)
show3(name='张三',age=8,sex='male')

#写一个函数,把以上所有参数全部填进去
def show4(name,*args,age=20,**kwargs):
    print('--',name)
    print('---',age)
    print('----',args)
    print('-----',kwargs)
show4(10,20,'zhang',age=34,sex='male',father='马云')

def show5(name,*args,age=20,**kwargs):
    print('--',name)
    print('---',age)
    print('----',args)
    print('-----',kwargs)
show5(10,'zhang',age=20,sex='male',father='马云')