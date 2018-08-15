"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:高阶函数之sorted函数.PY
@ide:PyCharm
@time:2018-07-25 10:51:40
"""
#sorted():用于对个序列进行升序排列,第一个参数:序列,第二个参数key:用于指定一个只接受一个参数的函数,这个函数用于从序列中的每一个元素中提取一个用于排序的关键字,默认值为None,第三个参数reverse:有两个值,一个为True,一个为False,如果reverse=True,则列表中的元素会被倒叙排列

#sorted默认按照ascll排序

from functools import  cmp_to_key

list1=[30,500,70,3,9]
list2=sorted(list1)
print('排列之后的结果',list2)

list4=['a','d','c','b']

list3=sorted(list1,reverse=True)
print('倒叙排序:',list3)

list5=[('b',4),('a',0),('c',2),('d',3)]
list6=sorted(list5,key=lambda x : x[0])
print(list6)

#如果使用sorted()函数实现对一个序列的降序排序

list7=[20,15,70,3,9]
list8=sorted(list7)
print('升序排列:',list8)
#如果x>y返回-1,x<y返回1,是按照降序排列的
#如果x>y返回1,x<y返回-1,则就是默认的升序排列
def reversed(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

result=sorted(list7,key=cmp_to_key(reversed))
print('降序排列:',result)

#面试中的常考题:sort和sorted的区别
#sort()排序将会改变原有的list,而sorted排序只是对列表进行排序,返回一个排序过后的新列表,并不会对原有列表进行改动
#sorted()用于对一个序列进行排序,而sort只能用于列表的排序



list9=[9,5,3,8,7,1]
list9.sort()
print(list9)

list10=[11,15,9,7,6]
list11=sorted(list10)
print('list10是',list10)
print('list11是',list11)

test=(1,2,5,9,8)
# test.sort()
print(sorted(test))
print(test)