#集合是一个无序的,元素不可重复的数据组合.标识符号{}
#它有两个主要作用:
#1,去重,把一个容器变成集合,可以实现去重的功能
#2,关系测试,测试两组数据之间的交集,差集,并集等等.
list1=[1,2,3,4,5,2,2,1,1]
set_1=set(list1)
print(type(set_1))
print(set_1)
tuple1=(5,7,6,9,9,9,9,8)
set_2=set(tuple1)
print(type(set_2 ))
print(set_2)
string='hhhhheih'
set_3=set(string)
print(type(set_3))
print(set_3)

#------------------------------常用函数----------------------------
#声明一个空的集合,不要和声明一个空字典混淆.
# 空字典:dict={}
myset=set()
#add():往集合里面添加数据,整体不会分开,如果添加的数据重复,则自动去重.
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(4)
myset.add(5)
myset.add('6')
myset.add('7')
myset.add('8')
myset.add('9')

#2.remove:删除集合中的元素,括号中直接添加要删除的元素的值,
myset.remove(1)
print(myset)
#如果删除的元素不存在集合中,则会报错
# myset.remove(1)
# print(myset)
#discard():删除集合中的元素,括号中直接添加要删除的元素的值,
myset.discard(2)
print(myset)
##如果删除的元素不存在集合中,却不会报错
myset.discard(2)
print('---',myset)
#pop():随机删除集合中的元素
myset.pop()
print(myset)
myset.pop()
print(myset)

#5.updeat():会将传入的可迭代的数据的每一个元素分别传入到集合当中变成集合中的一个元素,
myset.update('grzggzr')
print(myset)
# 区别于add():add默认会将要传入的数据整体当成一个元素传入到set集合当中.
myset.add('不好意思')
print(myset)
#clear():清空集合
myset.clear()
print(myset)

#------------------------------关系测试运算-----------------------------------
list2=[1,2,3,4,5,6]
set1=set(list2)
print(set1)
list3=[4,5,6,7,8]
set2=set(list3)
print(set2)


#issubset():判断***是不是***的子集,返回的结果是True或者False
res5=set1.issubset(set2)
print(res5)
#issuperset():判断***是不是***的父集,返回的结果是True或者False
res6=set1.issuperset(set2)
print(res6)
#isdisjoint():判断***和***是否没有交集,返回的结果是True或者False
res7=set1.isdisjoint(set2)
print(res7)

#intersection:求两个集合之间的交集
res=set1.intersection(set2)
print('交集',res)
#union:求两个集合之间的并集
res2=set1.union(set2)
print('并集',res2)
#difference:求两个集合之间的差集
res3=set1.difference(set2)
print('差集',res3)

#------------------------------通过运算符的形式进行关系测试--------------------------
#&:交集符号
res8=set1 & set2
print('交集',res8)
# |:并集
res9=set1|set2
print('并集',res9)
# -:差集
res10=set1 - set2
print('差集',res10)
set3={7,8,9}
#运算先后顺序可以加小括号来改变
res11=set1&((set2|set3)-set3)
print(set1)
print(set2)
print(set3)
print(res11)

