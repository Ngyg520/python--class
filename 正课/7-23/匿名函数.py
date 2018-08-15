"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:预科
@author:Mr.Yang
@file:匿名函数.PY
@ide:PyCharm
@time:2018-07-23 14:05:28
"""
#lambda(匿名函数的关键字):python中使用匿名lambda创建匿名函数,不能给函数设置函数名,和普通的函数相比,lambda相当于生成的一个表达式,lambda语法相对简单,可以封装一些简单的逻辑

#为什么使用匿名函数
#1.不需要定义函数名,节省内存中的变量的定义的空间
#2.可以使代码更加简洁

#正常的使用函数来定义一个数字相加的函数
def add (x,y):
    return x + y
res= add(10,20)
print(res)

#使用 lambda来改造上面的数字相加的函数
#x,y相当于普通函数的参数,:分隔符,x+y相当于函数的返回值
res_lambda=lambda x,y:x+y
#通过res_lambda这个变量来执行lambda函数
res1=res_lambda(10,20)
print(res1)

#不添加参数的lambda函数
res2=lambda:print('这是一个没有参数的lambda函数!')
res2()

#lambda加上添加判断
def bijiao(x,y):
    if x>y:
        print('x和y中数字较大的是:%s'%x)
    else:
        print('x和y中数字较大的是:%s'%y)
bijiao(2,3)

res3=lambda x,y:print('x和y中数字较大的是:%s'%x) if x>y else print('x和y中数字较大的是:%s'%y)
res3(2,3)

#lambda设置默认函数
def panduan(name='张三'):
    if name=='张三':
        print('姓名是张三')
    else:
        print('姓名不是张三')
panduan(name='狗蛋')


res4=lambda name='张三':print('姓名是张三') if name=="张三" else print('姓名不是张三')
res4(name='李四')

#----------孟新科的提问-------------
def show_1():
    a=10
    b=10
    c=a+b
    print(c)
show_1()
#转为匿名函数
res_lambda=lambda a,b:a+b
res6=res_lambda(10,10)
print(res6)

result = lambda a,b:print('a,b的和是：%s'%(a+b))
result(10,10)