"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:作业巩固.PY
@ide:PyCharm
@time:2018-07-24 15:57:13
"""
phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]

#遍历列表的函数
def all_list(decide):
    for x in range(0,len(phone_info)):
        phone_dict=phone_info[x]
        if decide==1:
            print('{0},品牌{1},价格{2},库存{3}'.format(x + 1,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        elif decide==0:
            print('{0},品牌{1}'.format(x+1,phone_dict['name']))

#查看产品的详细信息或返回
def find_list():
    print('''
    1-根据产品序号查看产品信息
    2-返回
    ''')
    select_num=int(input('请输入操作序号'))
    while select_num!=1 and select_num !=2:
        select_num=int(input('请重新输入操作序号'))
    if select_num==1:
        all_list(0)
        select_number=int(input('请输入要查看详细信息的手机序号'))
        while select_number-1<=0 or select_number-1>len(phone_info):
            select_number=int(input('请重新输入要查看的详细信息的手机序号'))
        phone_dict=phone_info[select_number-1]
        print('品牌{0},价格{1},库存{2}'.format(phone_dict['name'],phone_dict['price'],phone_dict['count']))
        buy_phone(phone_dict)
    else:
        return
#购买函数
def buy_phone(phone_dict):
    print('''
    1-购买
    2-返回
    ''')
    select_num=int(input('请输入操作的序号'))
    while select_num!=1 and select_num !=2:
        select_num=int(input('请重新输入操作序号'))
    if select_num==1:
        count_num=int(phone_dict['count'])
        print('剩余库存:'.format(count_num))
        buy_phone_num=int(input('请输入购买的数量'))
        new_phone_count=count_num - buy_phone_num
        phone_dict['count']=new_phone_count
        print('购买成功')
        while count_num==0:
            phone_info.remove(phone_dict)
    else:
        return
#更改产品信息
def gengai_phone_info():
    print('''
    1-添加新产品
    2-修改原有产品
    ''')
    select_num=int(input('请输入操作序号'))
    while select_num!=1 and select_num !=2:
        select_num=int(input('请重新输入操作序号'))
    if select_num == 1:
        new_name=input('新产品名称:')
        new_price=input('新产品价格:')
        new_count=input('新产品库存')
        new_phone_dict={'name':new_name,'price':new_price,'count':new_count}
        phone_info.append(new_phone_dict)
        print('添加成功')
    elif select_num==2:
        all_list(1)
        print('''
        1-根据序号进行修改
        2-返回
        ''')
        select_number=int(input('请输入操作序号'))
        while select_num != 1 and select_num != 2:
            select_num = int(input('请重新输入操作序号'))
        if select_number==1:
            phone_num=int(input('请输入需要修改手机信息的序号'))
            while phone_num<=0 or phone_num>len(phone_info):
                phone_num=int(input('请重新输入'))
            update_dict=phone_info[phone_num-1]
            update_name=input('请输入需要修改的手机品牌')
            update_price=input('请输入手机品牌价格')
            update_count=input('请输入手机库存')
            update_dict['name']=update_name
            update_dict['price']=update_price
            update_dict['count']=update_count
            print('修改成功')
        else:
            return
#删除库存信息
def shanchu_phone():
    print('''
    1-查看所有产品,按照序号删除
    2-全部删除
    ''')
    select_num = int(input('请输入操作序号'))
    while select_num != 1 and select_num != 2:
        select_num = int(input('请重新输入操作序号'))
    if select_num == 1:
        all_list(1)
        shanchu_num=int(input('请输入你需要删除的编号'))
        while shanchu_num <= 0 or shanchu_num > len(phone_info):
            shanchu_num = int(input('请重新输入'))
        phone_info.pop(shanchu_num-1)
    elif select_num==2:
        while len(phone_info):
            del phone_info[0]
    elif select_num==3:
        return

while True:
    print('''
    欢迎使用手机销售系统
    1-查看所有手机品牌
    2-添加或修改手机信息
    3-删除手机信息
    4-退出程序
    ''')
    select_number=int(input('请输入操作的序号'))
    while select_number<=0 or select_number>4:
        select_number=int(input('输入错误,请重新输入要操作的序号:'))
    if select_number==1:
        if len(phone_info):#判断列表是否为
            find_list()
        else:
            break
    elif select_number==2:
        if len(phone_info):
            gengai_phone_info()
        else:
            break
    elif select_number==3:
        if len(phone_info):
            shanchu_phone()
        else:
            break
    elif select_number==4:
        break
