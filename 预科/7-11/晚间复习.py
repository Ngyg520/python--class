#列表,元组,字典
list=[]
tuple=(20,1,3,5)
dict={}
set1=set()
#-----------添加数据-------------
list.append('李四')
print(list)
list.insert(0,'张三')
print(list)

dict['A']='阿罗多姿'
print(dict)
set1.add(1)
print(set1)
#---------查询数据------------
name=list[0:2]
print(name)
name1=list[:]
print(name1)
name2=list[-1]
print(name2)
for x in list:
    print('---',x)
for y in range (0,len(list)):
    print('==',list[y])
for y in range (0,len(list)):
    print('==',y)
#枚举函数
for index,value in enumerate(list):
    print(index,value)

a = tuple[0]#按索引查询
print(a)

b= tuple [0:1]
print(b)

for z in range(0,len(tuple)):#按索引值列举所有
    print(tuple[z])
for e in tuple:#直接列举所有
    print(e)
for index,value in enumerate(tuple):#枚举列举
    print(index,value)

name= dict['A']#按键查询
print(name)

#-------------------------修改数据------------------
list[0]='王五'#根据索引修改列表的值
print(list)

dict[1]='wangbadan'#字典添加键值对
print(dict)
res2=dict.pop('A')#根据键删除数据
print('---',dict)

tuple1=('多','来','米','发',[('锁','拉')],'西')#元组无法对一级值进行修改添加,可对二级进行
res=tuple1[4][0]
print(res)

tuple1[4][0]=('王八蛋')#对元组进行修改
print(tuple1)
#-----------------------常用函数-------------------
num=list.count('李四')#统计值出现的次数
print(num)
num1=list.index('王五')#显示值的索引
print(num1)
list.reverse()#将列表进行反转
print(list)
list1=['武器','安妮']
list.extend(list1)#合并列表
print(list)
list.clear()#清空列表所有值
print(list)
while len(list):#使用循环删除列表中所有的元素
    del list[0]
print('---',list)
list2=['剑圣','剑姬','巨人','剑魔']
del list2[0]#根据索引值删除值
print(list2)
list2.pop(1)#根据索引值删除值
print(list2)
list2.pop()#默认删除最后的值
print(list2)
list2.remove('剑姬')#直接删除填写的元素,如果存在多个,则默认删除第一个符合条件的
print(list2)

sex=tuple.count(20)#统计次数
print(sex)
sex1=tuple.index(20)#打印列表元素的索引值,存在多个,则默认打印第一个元素的索引值
print(sex1)

dict2={'name':"张三",'age':20,'sex':'男'}
#get():根据键获取对应的值,如果字典中不存在这个键,则默认采用后面的默认值.如果存在该键,则直接取字典中的值
sex2=dict2.get('name','李四')
print(sex2)
sex3=dict2.get('height',150)
print(sex3)
#items():将字典中的每一个键值对设置成元组的形式,并且存储在列表之中
sex4=dict.items()
print(sex4)
#字典第一种遍历
for key, value in dict2.items():
    print(key,value)
#第二种遍历
for key ,value in enumerate(dict2):
    print(key,value)
#打印出来的是删除的键对应的值
sex5=dict2.pop('name')
print(sex5)
#setdefault():根据键获取对应的值,如果存在该键,则直接获取字典中的值.如果字典中不存在这个键,则采取后面默认的值.并且将该键与值加入到原始字典中.
sex6=dict2.setdefault('age','19')
print(sex6)
#fromkeys():生成一个字典,第一个函数是键,第二个参数是值
dict3=dict.fromkeys('1',[3])
print(dict3)
print(dict2)
#update():用于将一个字典添加到另一个字典中
dict2.update(dict3)
