phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]
phone_dict={}
while True:
    print('欢迎使用1.0版本手机销售系统')
    print('''
        1-查看所有手机品牌
        2-更改产品库存信息
        3-移除产品库存信息
        4-退出程序
        ''')
    select1 = int(input('请输入操作序号查看手机信息'))
    if select1!=1 and select1!=2 and select1!=3 and select1!=4:
        select1=int(input('请输入正确的1~4操作编号'))
    if select1 == 1:
            for index,dict1 in enumerate(phone_info):#value是一个字典
                model_number = dict1.get('name')#提取字典键对应的值--手机品牌
                print(index+1,model_number)
            print('''    
            1-选择产品序号查看详情
            2-返回
            ''')
            select2= int(input('请输入需要操作的编号1或2'))
            if select2!=1 and select2!=2:
                select2=int(input('请输入1和2进行操作'))
            if select2==1:
                serial_number = int(input('请输入你需要查询的手机详情的编号'))
                serial_number1=int(serial_number-1)#输入的手机号-1等于索引
                cpxx=phone_info[serial_number-1]
                print(cpxx)
                #第三步购买手机
                print('''
                1-我确认购买该款手机
                2-返回
                ''')
                select3=int(input('请输入操作的编号以确认购买手机'))
                if select3 != 1 and select3 != 2:
                    select3 = int(input('请输入1和2进行操作'))
                if select3==1:
                    for index,dict1 in enumerate(phone_info):  # value=dict1
                        # 提取字典键对应的值--手机数量
                        number1=dict1.get('count')
                        new_num=int(number1)
                        if index == serial_number - 1:
                            def jian (a, b):
                                c = a - b
                                return c
                            new_num1 =jian(new_num,1)
                            print(new_num1)
                            dict1['count'] =new_num1#将减少后的库存new_num1赋值给count
                if select2 == 2:
                    def test():
                        return
                    test()
    if select1 == 2:
        print('''
        1-添加新产品
        2-修改原有产品
        ''')
        select2=int(input('输入操作序号'))
        if select2 != 1 and select2 != 2:
            select2 = int(input('请输入1和2进行操作'))
        if select2==1:
            new_name=input('输入新产品名称')
            new_price=input('新产品价格')
            new_count=input('新产品库存')
            phone_dict['name']=new_name
            phone_dict['price']=new_price
            phone_dict['count']=new_count
            phone_info.append(phone_dict)
            print('产品信息',phone_dict)
            print('产品信息添加成功')
        if select2==2:
            print('''
            1-选择序号进行信息修改
            2-返回
            ''')
            for index, dict1 in enumerate(phone_info):  # value是一个字典
                print(index + 1, dict1)
                num1=index-1
            czsz=int(input('需要修改的手机-序号'))
            if czsz!=1 and czsz!=2:
                czsz=int(input('请输入1和2进行操作'))
            dict2=phone_info[czsz-1]
            print(dict2)
            new_name1 = input('产品名称修改为:')
            new_price1 = input('产品价格修改为:')
            new_count1 = input('产品库存修改为:')
            dict2['name'] = new_name1
            dict2['price'] = new_price1
            dict2['count'] = new_count1
            print(dict2)
            print('产品信息修改成功')
            if czsz== 2:
                def test():
                    return
                test()
    if select1==3:
        print('''
        1-查看所有产品
        2-移除所有产品
        3-返回
        ''')
        select2=int(input('操作序号'))
        if select2 != 1 and select2 != 2 and select2!=3:
            select2 = int(input('请输入1和2进行操作'))
        if select2 == 1:
            for index, dict1 in enumerate(phone_info):  # value是一个字典
                print(index + 1, dict1)
            czsz=int(input('删除手机信息-序号'))
            phone_info.pop(czsz-1)
            print(phone_info)
            print('删除成功')
        if select2==2:
            while len(phone_info):
                del phone_info[0]
            print('移除所有产品成功')
        if select1 == 4:
            def test():
                return
            test()
    if select1==4:
        print('退出程序')
        break