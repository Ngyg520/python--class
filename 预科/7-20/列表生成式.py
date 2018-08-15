"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-20
@author:Mr.Zhang
@file:列表生成式.PY
@ide:PyCharm
@time:2018-07-20 15:41:31
"""
#列表生成式：快速生成列表的一种方式。
my_list=[]
for x in range(1,11):
    res=x**2
    my_list.append(res)
print(my_list)

fast_list=[x**2 for x in range(1,11)]
print(fast_list)

#加入if判断
my_list_1=[]
for x in range(1,11):
    if x!=2:
        res=x**2
        my_list_1.append(res)
print(my_list_1)


fast_list_1=[x**2 for x in range(1,11) if x!=2]
print(fast_list_1)


#遍历1-11之间的数字，让数字是奇数项的结果进行平方运算
my_list_2=[]
for x in range(1,11):
    if x%2==1:
        res=x**2
        my_list_2.append(res)
print(my_list_2)

fast_list_2=[x**2 for x in range(1,11) if x%2==1]
print(fast_list_2)

#双重for循环
my_list_3=[]
for x in range(1,4):
    for y in range(1,4):
        res=x*y
        my_list_3.append(res)
print(my_list_3)

fast_list_3=[x*y for x in range(1,4) for y in range(1,4)]
print(fast_list_3)
