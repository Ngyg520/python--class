#为什么使用函数?因为没有函数的编程只是单纯的写逻辑,如果想重用逻辑,唯一的方法就是copy一份源代码,但是使用函数就可以将一些逻辑相同的代码封装起来,这样做的好处可以提高代码逻辑的重复使用率,提升开发效率.
#1.声明函数,在函数里面编写逻辑代码
#2.调用函数,执行编写的逻辑代码.

#声明函数,def,声明函数的关键字,add是自定义的函数名称,():用于定于函数的参数,如果没有内容就表示该函数没有参数.


#1.无返回值,无参数的函数
def add():
    a =1
    b =2
    c = a+b
    print(c)
#调用函数
add()


#2.有返回值,无参数的函数
#一个函数为什么要有返回值:因为想要一个函数的最终执行结果,后面的程序才可以根据这个执行结果进行其他的操作
#return:是返回函数结果的关键字
def cheng():
    c=10
    d=20
    e=c*d
    return e
res=cheng()
print(res)
f=res*10
print(f)


#3.无返回值,有参数的函数
#a,b称之为形参,形式参数,形参是用于接受实参的值
def chu(a,b):
    c=a/b
    print(c)
#10,2.5称之为实参,实际参数,用于给形参赋值
chu(10,2.5)


#4.有返回值,有参数的函数
def jian(a,b):
    c=a-b
    return a,b,c
res=jian(10,1)
print(type(res))
print(res)
res1,res2,res3=jian(10,1)
print(res1,res2,res3)

#return关键字的作用:
#1,用于返回函数的结果
#2用于结束当前代码的执行,使用return关键字结束代码执行的时候,必须位于函数内部.
def test():
  for x in range(1,11):
     if x ==2:
         return
     else:
         print(x)
test()