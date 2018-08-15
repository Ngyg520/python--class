#author:yang
#字典:也是 python中内置的一种容器类型.字典是可变的,可以对字典进行增删改查的操作.
#字典有以下特点:
#1,字典是以"键-值"结构来存储数据的,字典照片那个没有索引这个概念,'键':相对于列表中的索引.可以通过键对一个数据进行增删改查.
#2,列表中的索引值是唯一的,键也是唯一的,都不允许重复.
#3,字典是无序的,'键-值'对的存储没有先后顺序,只需要一个键对应一个值.

#声明一个空字典
dict1={}
#声明一个非空字典
#键:adc,辅助,打野,中单,上单
#值:uzi,ming,mlxg,小虎,letme
dict2={'adc':'uzi','辅助':'ming','打野':'mlxg','中单':'xiaohu','上单':'letme'}

#计算内存中,True-1,False-0.1和True,0和False不能同时为字典中的键,同时存在会产生冲突
#列表和字典都不能当键,元组可以,是因为通常情况下,键不可变,而列表可变,元组不可变.
dict3={True:'true',(1,2,3):'(1,2,3)'}
print(dict3)
#------------------------------添加数据------------------------------
#数据的时候,要指定一个键,并且要给该键赋一个值.
dict2['替补']='karsa'
print(dict2)

#-----------------------------查询数据-------------------------------
name=dict2 ['adc']
print(name)
name1=dict2['辅助']
print(name1)

#------------------------------常用的函数-----------------------------------
dict4={'name':"张三",'age':20,'sex':'男'}
#P.get():根据键获取对应的值,如果字典中不存在这个键,则默认采用后面的默认值.如果存在该键,则直接取字典中的值
#get()函数:第一个参数:键  第二个参数:默认值
res=dict4 .get('name','李四')
print('----',res)
res1=dict4.get('height','170')
print(res1)
#2,items():将字典中的每一个键值对设置成元组的形式,并且存储在列表之中
res2=dict4.items()
print(res2)
#字典第一种遍历方式
for key,value in dict4 .items():
    print(key,value)
#字典第二种遍历方式,只取键,不取值.相当于遍历键(name,age,sex)
for key,value in enumerate(dict4):
    print('====',key,value)
#3.keys()取出字典中的所有的键并存放在列表中.
res3=dict4.keys()
print(res3)
#4.values:取出字典中所有的值并存放在列表中.
res4=dict4.values()
print(res4)
#5,pop():根据键删除字典中的值,返回的结果是删除的这个键对应的值
res5=dict4.pop('sex')
print(res5)
#6.setdefault():根据键获取对应的值,如果存在该键,则直接获取字典中的值.如果字典中不存在这个键,则采取后面默认的值.并且将该键与值加入到原始字典中.
dict5={'name':'麻子','age':21,'sex':'女'}
res6=dict5.setdefault('name','王二')
print('-----',res6)
res7=dict5.setdefault('height',180)
print('====',res7)
print(dict5)
#7.popitem():随机返回并删除字典中的一对键值对(一般会删除末尾的键值对),返回值是一个被删除的键值对组成的元组
res8=dict5.popitem()
print('被删除的',res8)
print(dict5)
#8.fromkeys():生成一个字典,第一个函数是键,第二个参数是值,如果第一个参数填写的是可迭代对象,则会将对象中的每一个元素拆分成一个元素当做键,并且对应的值都为第二个参数
dict6=dict.fromkeys('12',[1,2])
print(dict6)
dict7=dict.fromkeys('1','hhh')
print(dict7)#老师说10年用不上一次
#9.update():用于将一个字典添加到另一个字典中.
dict8={'射手':'iboy','辅助':'meiko'}
dict9={'打野':'7酱','中单':'scount','上单':'ray'}
dict8.update(dict9)
#10.判断一个键是否在一个字典中
if '射手' in dict8 :
    print('存在射手这个键')
#11.clear():清除所有键值对
dict8.clear()
print(dict8)
#12.del:根据键删除字典中的值
dict10={'name':'张三'}
del dict10 ['name']
print(dict10)

