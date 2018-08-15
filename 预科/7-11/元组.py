#元组,和列表一样是一个容器类型的数据.元组只能在创建的时候添加数据,创建完成之后可以查询数据,但是元组的一级元素不能够被修改和删除,一般创建的元组的时候,在最后一个元素的后面要加上逗号
#创建一个元组
tuple1=(20,9.88,'亚洲捆绑',True,)
#------------------查询数据----------------
#序号查询
a = tuple1 [0]
print(a)
b=tuple1[3]
print(type(b))
print(b)


#切片查询,返回的是一个元组
#列表查询时,返回的是一个列表
c = tuple1[0:3]
print(c)
#通过索引进行遍历
for x in range(0,len(tuple1)):
    print(tuple1[x])
#直接遍历里面的元素
for y in tuple1:
    print(y)
#通过枚举查询
for index,value in enumerate(tuple1):
    print(index,value)
#--------------修改元素---------------------------------------
#一级元素不能被修改和删除,二级元素可以
tuple2=(20,30,'meiko',[(40,50)],'hhh')
res=tuple2[3][0]
print('---',res)
tuple2[3][0]=(60,70)
print(tuple2)

#----------------------------常用函数-----------------------------
#count():用于统计元素出现的次数
tuple3=(20,20,30,True,'hhh')
res=tuple3 .count(20)
print('===',res)
#index():用于返回元素的索引值,如果列表中存在多个相同的元素,则默认返回第一个符合条件的元素的索引
res=tuple3.index('hhh')
print(res)
