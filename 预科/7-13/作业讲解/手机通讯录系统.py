"""
座右铭:将来的你一定会感激现在拼命的自己
@project:${PROJECT_NAME}
@author:Mr.Zhang
@file:${NAME}.PY
@ide:${PRODUCT_NAME}
@time:${YEAR}-${MONTH}-${DAY} ${HOUR}:${MINUTE}:${SECOND}
"""
list_student=['郝超杰','李威','吕朝朝','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']
#思路,一个姓对应一个列表
#声明一个空字典
student_dict={}
#遍历所有联系人,给每个人的姓氏提取出来
for student in list_student :
    #从每个人的名字当中取出姓氏,联系人的分类就是以姓氏为键.
    first_char=student[0]
    #判断字典是否存在first_char这个键中
    if first_char in student_dict :
        #如果有这个键,通过键取出联系人列表,,result_list:['郝超杰']
        result_list=student_dict [first_char]
        #如果student不在result_list中,将student添加到result.
        result_list.append(student)
    else:
        #如果没有这个键
        #创建这个键,并且给这个键配置一个联系人列表
        result_list=[student]
        student_dict[first_char]=result_list#键对应值(值为一个表)
while True:
    print('''
    1-查询
    2-退出
    ''')
    select_number=int(input('请选择操作序号'))
    while select_number!=1 and select_number!=2:
        select_number=int(input('请重新选择操作序号'))
    if select_number==1:
        select_char=input('请输入姓氏:')
        #判断输入的联系人在不在字典当中
        if select_char in student_dict:
            #如果有联系人的信息,则以输入的姓氏为键取出对应的联系人列表,然后遍历联系人列表
            stu_list=student_dict[select_char]
            for index,result in enumerate(stu_list):
                print(index+1,'-',result)
        # 打印的是else的结果
        else:
            print('没有对应的联系人信息')
    else:
        break