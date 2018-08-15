"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:预科
@author:Mr.Yang
@file:生成器函数.PY
@ide:PyCharm
@time:2018-07-23 14:34:00
"""

#生成器函数:当一个函数带有yieid关键字的时候,那么他将不再是一个普通的函数,而是一个生成器generator
#yieid和return;这俩个关键字十分的相似,yieid每次只返回一个值,而return则会把最终的结果一次返回
#每当代码执行到yieid的时候就会直接将yieid后面的值返回出,下一次迭代的时候,会从上一次遇到yieid之后的代码开始执行
def test():
    list1=[]
    for x in range (1,10):
        list1.append(x)
    return list1
res=test()
print(res)

def test_1():
    for x in range (1,10):
        yield x
generator=test_1()
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))

#生成器函数的例子:母鸡下蛋
#1,一次性把所有的鸡蛋全部下下来.
#如果一次把所有的鸡蛋全部下下来,一是十分占地方,而是容易坏掉.

def chicken_lay_eggs():
    #鸡蛋筐列表
    basket=[]
    for egg in range (1,101):
        basket.append(egg)
    return basket
eggs =chicken_lay_eggs()
print('一筐鸡蛋:',eggs)

#这样做的好处:第一是省地方,第二是下一个吃一个,不会坏掉
def chicken_lay_eggs_1():
    for egg in range(1,101):
        print('战斗母鸡正在下第{}个蛋'.format(egg))
        yield egg
        print('我把第{}个蛋给吃了!'.format(egg))
eggs_1=chicken_lay_eggs_1()
print(next(eggs_1))
print(next(eggs_1))
print(next(eggs_1))