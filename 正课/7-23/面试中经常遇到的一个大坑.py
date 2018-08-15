"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:预科
@author:Mr.Yang
@file:面试中经常遇到的一个大坑.PY
@ide:PyCharm
@time:2018-07-23 11:14:49
"""
def keng(i,result=[]):
    #id():显示对象的内存地址
    #一个对象对应的内存地址是唯一的
    print('没添加数据之前的列表的内存地址是:%s'%id(result))
    for x in range (i):
        result.append(x*x)
    print('添加数据之后的列表的内存地址是:%s' % id(result))
    return result

res = keng(3)
print(res)
res1=keng(3)
print(res1)
res2=keng(3,[1,2,3])
print(res2)
