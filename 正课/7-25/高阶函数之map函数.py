"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:高阶函数之map函数.PY
@ide:PyCharm
@time:2018-07-25 09:04:09
"""
#map()函数:接收两个参数,一个是参数,一个是序列,map函数将序列中的每一个元素都传入函数中进行运算,并把结果当做有个迭代器进行返回.

def calc(x):
    res=x*x
    return res

#计算列表中每个元素的平方
result = map(calc,[1,2,3,4,5,6])
print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# for res in  result:
#     print(res)
result=list(result)
print(result)

#将列表中的每一个元素转换成字符串
result=map(str,[1,2,3,4,5,6])
print(result)
# print(next(result))
for res in result:
    print(res,end='-')

#将列表中的每一个元素都转化成整数
result_2=map(int,['1','2','3','4','5','6'])
print(result_2)
print(next(result_2))
for res in result_2:
    print(res,end=',')

#将字符串中每一个元素都转化成整数
result_3=map(int,'1234567')
print(result_3)
for res in result_3:
    print(res,end='~')

