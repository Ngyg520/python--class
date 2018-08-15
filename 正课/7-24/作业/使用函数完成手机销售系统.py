"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:使用函数完成手机销售系统.PY
@ide:PyCharm
@time:2018-07-24 09:03:54
"""

phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]


#查看品牌的函数
#设置一个形参is_detail,如果is_detail的值为True,查询手机信息,如果为false,查询简要信息
def select_all_phone(is_detail):
    for x in range (0,len(phone_info)):
        # 取出每一个字典
        phone_dict=phone_info[x]
        #is_detail是True,则查询详细信息(手机品牌,价格,库存)
        if is_detail==True:
            print('{0}-品牌{1},价格{2},库存{3}'.format(x+1,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        # 如果is_detail不是True,那么就是False,查询简要信息(手机品牌)
        else:
            print('{0}-品牌{1}'.format(x+1,phone_dict['name']))

#定义产看某个品牌的详细信息或者返回的函数
def detail_info_or_back():
    print('1-根据产品序号查看手机详细信息')
    print('2-返回')
    #根据控制台输入的数字,来进行判断运行那个选项
    select_operation=int(input('请输入你要操作的序号'))
    while select_operation!=1 and select_operation!=2:
        select_operation = int(input('输入错误,请重新输入你要操作的序号:'))
    #如果用户选择的是序号1,则运行第一个功能选项
    if select_operation==1:
        select_all_phone(False)
        select_number=int(input('请输入要查询的手机详细信息的手机品牌序号:'))
        #循环检测用户输入的手机品牌是否正确
        while select_number <1 or select_number>len(phone_info):
            select_number=int(input('输入的序号有误,请重新输入要查询的手机详细信息的手机品牌序号'))
        phone_dict=phone_info[select_number-1]
        print('{0}:品牌{1},价格{2},库存{3}'.format(select_number,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        #函数里面嵌套函数,因为用户选择序号1的时候,下面还有购买或者返回的操作,把购买和返回的操作单独进行函数封装,最后当用户选择1的时候,之前在序号1这个选择中,调用个buy_or_back()函数
        buy_or_back(phone_dict)
    #如果选择的不是序号1,那么就是序号2,返回
    else:
        return

#定义一个购买或者返回的函数,设置一个参数接受手机的字典信息
def buy_or_back(phone_dict):
    print('1-购买')
    print('2-返回')
    select_number=int(input('请输入要操作的编号:'))
    while select_number !=1 and select_number!=2:
        select_number=int(input('请输入要操作的编号'))
    if select_number==1:
        #在输入购买数量之前,先提示手机库存有多少.
        total_count=int(phone_dict['count'])
        print('当前库存%s台'%total_count)
        #当用户知道数量之后,让用户输入要购买的数量
        buy_count=int(input('请输入要购买的数量:'))
        while buy_count<=0 or buy_count>total_count:
            buy_count = int(input('输入错误,请输入要购买的数量'))
        #根据购买的数量,计算剩余库存并修改原有库存
        surplus_count=total_count - buy_count
        #将剩余库存存入到原有的字典中
        phone_dict['count']=str(surplus_count)
        #假如用户给手机全部买完,库存为0,将该手机品牌从列表中删除
        if int(phone_dict['count'])==0:
            phone_info.remove(phone_dict)
        print('购买成功!')
    #如果用户选择的不是序号1,那就是序号2,返回
    else:
        return

#定义添加产品或修改产品的函数
def add_or_update_phone_info():
    print('1-添加新产品')
    print('2-修改原有产品')
    select_number=int(input('请输入要选择的序号:'))
    while select_number!=1 and select_number!=2:
        select_number=int(input('输入错误,请重新输入序号'))
    #如果选择的是序号1,则添加新产品
    if select_number==1:
        new_phone_name=input('请输入新产品名称:')
        new_phone_price=input('请输入新产品价格:')
        new_phone_count = input('请输入新产品库存:')
        new_phone_dict={'name':new_phone_name,'price':new_phone_price,'count':new_phone_count}
        #再将新的字典加入到列表之中
        phone_info.append(new_phone_dict)
        print('新产品添加成功!')
    #用户不是选择1就是2修改原有产品
    else:
        #调用select_all_phone函数,参数设置为True,将所有的随机手机详细信息全部打印出来.用户再根据编号选择要对那个手机进行修改操作
        select_all_phone(True)
        print('1-根据序号修改产品信息')
        print('2-返回')
        select_number=int(input('请输入你要操作的序号:'))
        while select_number!=1 and select_number!=2:
            select_number=int(input('输入错误,请重新输入要操作的序号:'))
        #如果用户选择的是序号1,则根据产品序号修改产品信息
        if select_number ==1 :
            phone_num=int(input('请输入要修改的手机的序号:'))
            while phone_num<1 or phone_num>len (phone_info):
                phone_num = int(input('输入错误,请重新输入要修改的手机的序号:'))
            #取出对应的手机字典信息
            update_dict=phone_info[phone_num-1]
            #让用户输入修改的数据
            update_name=input('请输入修改的名称')
            update_price = input('请输入修改的价格')
            update_count= input('请输入修改的库存')
            update_dict['name']=update_name
            update_dict['price']=update_price
            update_dict['count']=update_count
            print('修改成功')
        else:
            return
#定义一个删除产品或者返回的函数
def delete_phone_or_back():
    print('1-根据产品序号删除产品')
    print('2-删除所有产品')
    print('3-返回')
    select_number=int(input('请输入要操作的编号:'))
    while select_number!=1 and select_number!=2 and select_number !=3:
        select_number=int(input('输入错误,请重新输入'))
    #用户选择1,要根据产品序号删除
    if select_number==1:
        select_all_phone(True)
        number=input('请输入要删除的产品编号')
        while number<1 or number >len(phone_info):
            number = int (input('请重新输入'))
        del phone_info[number-1]
    elif select_number==2:
        while len(phone_info):
            del  phone_info[0]
    #用户选择3,返回
    elif select_number==3:
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
            detail_info_or_back()
        else:
            break
    elif select_number==2:
        if len(phone_info):
            add_or_update_phone_info()
        else:
            break
    elif select_number==3:
        if len(phone_info):
            delete_phone_or_back()
        else:
            break
    elif select_number==4:
        break