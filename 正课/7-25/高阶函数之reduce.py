"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:高阶函数之reduce.PY
@ide:PyCharm
@time:2018-07-25 10:00:21
"""
from functools import reduce
#reduce():接受两个参数,第一个参数:函数,第二个参数,序列
#作用:将序列中的前两个元素进行一次运算,然后运算的结果再和第三个元素进行运算,依次往下执行

def add(x,y):
    res= x+y
    return res
result = reduce(add,['a','b','c','d'])
print(result)
#第一次运算结果:ab
#第一次运算结果:abc
# 第一次运算结果:abcd

result1=reduce(add,[1,2,3,4])
print(result1)

#使用lambda改造
result_1=reduce(lambda x,y:x+y ,[12,3,4])
print(result_1)