#声明一个用于保存学员信息的空列表
member_list=['张三','李四','王五']
while True:
    print('''欢迎使用python-13期学生信息管理系统
    1-添加学员姓名
    2-修改学员姓名
    3-查询学员姓名
    4-删除学员姓名
    0-退出
    ''')
    select_number=int(input('选择你要操作的序号:'))
    #判断用户输入序号是否正确
    while select_number<0 or select_number>4:
        select_number=int(input('请重新输入正确序号'))
    #如果用户选择1,则添加学员姓名
    if select_number==1:
        name=input('请输入要添加的学员姓名:')
        member_list.append(name)
        print('学员信息添加成功')
    #添加学员信息
    if select_number==2:
        #判断是否有学员信息
        if len(member_list):
            #让用户选择学员序号,需要将列表中的学员信息展示出来
            for x in range(0,len(member_list)):
                # 索引+1等于序号
                print(x+1,member_list[x])
            student_num=int(input('请输入你要修改的学员序号:'))
            #判断输入序号是否满足容器长度
            while student_num<1 or student_num>len(member_list):
                student_num= int(input('请输入正确序号'))
            new_name= input('请输入修改的姓名')
            member_list[student_num-1]=new_name#减一使序号等于它的索引号
            print('学员信息修改成功')
        else:
            print('学员信息为空,无法修改')
    # 序号为3,说明想要查询学员信息
    if select_number == 3:
        if len (member_list):
            print('''
            1-输入序号查询
            2-查询所有学员
            ''')
            select_number=int(input('请输入你要操作的序号:'))
            #判断序号是否正确
            while select_number!=1 and select_number!=2:
                select_number=int(input('请输入正确的选择序号'))
            #选项1,输入序号查询学员信息
            if select_number==1:
                student_num = int(input('请输入要查询的学员序号'))
                #判断输入的序号是否正确
                while student_num<1 or student_num>len(member_list):
                    student_num = int(input('请输入正确的查询序号'))
                name=member_list[student_num-1]
                print('查询到的学员姓名:%s'%name)
            #选项2,展示所有学员信息
            if select_number==2:
                for x in range(0, len(member_list)):
                    # 索引+1等于序号
                    print(x + 1, member_list[x])
        # 首先判断列表中是否有学员信息
        else:
            print('学员信息为空,无法查询')
    #删除学员信息
    if select_number==4:
        if len(member_list):
            print('''
        1-输入序号删除
        2-输入学员姓名删除
        3-删除所有学员
        ''')
        for x in range(0, len(member_list)):
            # 索引+1等于序号
            print(x + 1, member_list[x])
        select_num=int(input('输入操作的序号'))
        while select_num!=1 and select_num !=2 and select_num!=3:
            select_num=int(input('请输入正确的操作序号'))
        if select_number == 1:
            select=int(input('请输入删除的学员序号'))
            while select<1 or select>len(member_list):
                select=int(input('编号不存在'))
            member_list.pop(select-1)
            print('删除学员成功')
        if select_num==2:
            name =input('请输入要删除的学员名称:')
            while name not in member_list:
                name=input('请重新输入要删除的学员姓名')
            member_list.remove(name)
            print('学员信息删除成功')
        if select_num==3:
            while len(member_list):
                del member_list[0]
            print('学员信息删除成功')
        else:
            print('学员信息为空')
    if select_number==0:
        break