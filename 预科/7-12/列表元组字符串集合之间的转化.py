#列表:list
#元组:tuple
#字符串:str
#集合:set
#------------------------------------列表转换元组 字符串 集合------------
#列表转元组
print('列表')
list1=['a','b','c','d']
tup=tuple(list1)
print(type(tup))
print(tup)
#列表转字符串
string=''.join(list1)
print(type(string))
print(string)
#列表转集合
set1=set(list1)
print(type(set1 ),set1,sep='')#sep'去空格

#------------------------元组转 列表,字符串,集合------------------------------
#元组转列表
print('元组')
tuple1=('q','w','e','r')
list2=list(tuple1)
print(type(list2))
print(list2)
#元组转字符串
string1=''.join(tuple1)
print(type(string1))
print(string)
#元组转集合
set2=set(tuple1)
print(type(set2))
print(set2)
#---------------------------------字符串转  元组,列表,集合-----------------
print('字符串')
string2='wasd'
#字符串转列表
list3=list(string2)
print(type(list3))
print(list3)
#字符串转元组
tuple2=tuple(string2)
print(type(tuple2))
print(tuple2)
#字符串转集合
set3=set(string2)
print(type(set3))
print(set3)
#--------------------------------集合转  列表 元组  字符串---------------
#声明一个空集合
print('集合')
my_set1=set()
my_set={'z','x','c','v'}
#由于集合是无序的,所以转化列表,元组,字符串的结果也是无序的
#集合转字符串
string3=''.join(my_set)
print(type(string3))
print(string3)
#集合转化成列表
list4=list(my_set)
print(type(list4))
print(list4)
#集合转化成元组
tuple3=tuple(my_set)
print(type(tuple3))
print(tuple3)