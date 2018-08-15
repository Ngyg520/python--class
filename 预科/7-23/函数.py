"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:预科
@author:Mr.Yang
@file:函数.PY
@ide:PyCharm
@time:2018-07-23 09:08:21
"""
# print('今天是周一')
# print('今天是周二')
# print('今天是周三')

#函数:为什么使用函数?没有函数的编程只是在单纯的写代码逻辑,如果想重写代码逻辑,只能copy一份代码.但是一旦使用函数,就可以将一些相同的代码逻辑封装起来,这样可以提高代码的重复使用率,提升开发效率.

#第一步:声明一个函数,在函数里面写逻辑代码
#第二步:调用函数,执行编写的逻辑代码

#怎么样声明一个函数?

#def 声明函数的关键字,shuchu,函数名(可以自定义的).()用于定义函数的参数,如果没用内容,就表示该函数没有参数.":"下面的东西,要封装的代码逻辑.

#1.声明一个无返回值,无参数的函数
def shuchu():
    print('今天是周一')
    print('今天是周二')
    print('今天是周三')
    #调用函数,函数名+括号
shuchu()
shuchu()

#2.声明一个有返回值,无参数的函数
#一个函数为什么要有返回值:因为你一个函数想要最终的执行结果,后面的程序才能根据这个执行结果进行其他的操作

def cheng():
    c = 10
    d = 20
    e = c*d
    return e
res=cheng()
print(res)

f= res*10
print(f)

#声明一个无返回值,有参数的函数

#ab叫做形式参数,简称形参
def chufa(a,b):
    c = a/b
    print(c)
#10,2.5称之为实际参数,简称实参.相当于给a,b两个形参赋值,a=10,b=2.5
chufa(10,2.5)
chufa(10,4)

#4.有返回值,有参数的函数
def jianfa(a,b):
    c=a-b
    return c
res=jianfa(8,5)
print(res)
res1=res+ 10
print(res1)

#return关键字的作用
#1用于返回函数的执行结果
#2,用于结束当前代码的执行,使用return关键结束代码执行的时候,return必须位于函数内部,区别break
def test():
    for x in range(1,11):
        if x == 3:
            return
        else:
            print('---',x)
test()

