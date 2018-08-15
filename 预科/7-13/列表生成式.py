#列表生成式:快速生成列表的一种方式
#列表生成式特点:会将所有的结果全部计算出来存放在列表中,这样会占用很大的内存空间,如果列表中的数据太多,会导致程序运行卡顿
my_list=[]
for x in range(1,11):
        res=x * x
        my_list.append(res)
print(my_list)

fast_list=[x*x for x in range(1,11)]
print(fast_list)

#if判断
fast_list_1=[x*x for x in range (1,11) if x!=2]
print(fast_list_1)
#遍历1-11的数字,让数字是奇数项的结果进行相乘的运算
fast_list_2=[x*x for x in range(1,11)  if x%2==1]
print(fast_list_2 )
#列表生成式还支持双重for循环
res2=[x*y for x in range(1,4) for y in range (1,4)]
print(res2)

#双重for循环
my_list_3=[]
for x in range(1,4):
    for y in range (1,4):
        res=x*y
        my_list_3.append(res)
print(my_list_3)

fast_list_3=[x*y for x in range(1,4) for y in range(1,4)]
print(fast_list_3)