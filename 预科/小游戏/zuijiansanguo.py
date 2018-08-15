#coding:utf-8
#三国刘备,曹操,孙权
liubei_list=[3000]
liubei_dict={'刘备':['益州','雍州']}
caocao_list=[8000]
caocao_dict={'曹操':['青州','徐州','幽州','兖州','并州']}
sunquan_list=[5000]
sunquan_dict={'孙权':['扬州','荆州']}
dict1={}
list1=[]
dict2={}
list2=[]
dict3={}
list3=[]
import random
random_num=random.randint(1000,10000)
random_num1=random.randint(1000,3000)

print('''
1-刘备
2-曹操
3-孙权
''')
shili1=int(input('请选择君主'))
while shili1!=1 and shili1!=2 and shili1!=3:
    shili1=int(input('皮?赶紧选1,2,3'))
if shili1==1:
    print('目前兵力',liubei_list)
    dipan = liubei_dict['刘备']
    print('你的地盘',dipan)
    dict1=liubei_dict#刘备
    list1=liubei_list
    dict2=caocao_dict#曹操
    list2=caocao_list
    dict3=sunquan_dict#孙权
    list3=sunquan_list
elif shili1==2:
    print('目前兵力',caocao_list)
    dipan = caocao_dict['曹操']
    print('你的地盘',dipan)
    dict1=caocao_dict#曹操
    list1=caocao_list
    dict2 = liubei_dict#刘备
    list2 = liubei_list
    dict3 = sunquan_dict
    list3 = sunquan_list#孙权
else :
    print('目前兵力',caocao_list)
    dipan = sunquan_dict['孙权']
    print('你的地盘',dipan)
    dict1=sunquan_dict#孙权
    list1=sunquan_list
    dict2 = caocao_dict#曹操
    list2 = caocao_list
    dict3 = liubei_dict#刘备
    list3 = liubei_list
res1=dict1.keys()
res2=dict2.keys()
res3=dict3.keys()
string1=''.join(res1)
string2=''.join(res2)
string3=''.join(res3)

while True:
    print('''
    1-征兵
    2-出征
    ''')
    caozuo1=int(input('输入1或2'))
    while caozuo1 != 1 and caozuo1 != 2 :
        caozuo1 = int(input('赶紧选1,2'))
    if caozuo1==1:
        # 征兵系统
        num1 = list1[0]
        num2 = list2[0]
        num3 = list3[0]
        num_one = num1 + random_num
        num_two = num2 + random_num1
        num_three = num3 + random_num1
        list1.pop(0)
        list1.insert(0,num_one)
        list2.pop(0)
        list2.insert(0, num_two)
        list3.pop(0)
        list3.insert(0, num_three)
        # 征兵获得随机兵力
        print('你的兵力:',num_one)
        print(string2,num_two)
        print(string3,num_three)

    if caozuo1==2:
        print('攻打',string2,'请选1')
        print('攻打',string3,'请选2')
        select=int(input('你的选择是:'))
        while select != 1 and select != 2:
            select = int(input('赶紧选1,2'))
        if select==1:
            def jian (a,b):
                c = a - b
                return c
            res4 = jian(num_one,num_two)
            if res4 > 0:
                print('打败了对方')
                res5=dict2.get(string2)
                res6=dict1.get(string1)
                res6.extend(res5)
                dict2.clear()
                print(list1)
                print('你的地盘扩大到:',dict1)
            else:
                print('你被杀了,游戏结束')
                break
        if select==2:
            def jian (a,b):
                c = a - b
                return c
            res1 = jian(num_one,num_three)
            print('剩余兵力',res1)
            if res1 > 0:
                print('打败了对方,游戏结束')
                res5 = dict3.get(string3)
                res6 = dict1.get(string1)
                res6.extend(res5)
                dict3.clear()
                print(list1)
                print('你的地盘扩大到:', dict1)
            else:
                print('你被杀了')
                break