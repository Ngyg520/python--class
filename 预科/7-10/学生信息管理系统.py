student_list=[]
while True:
    print('welcome use 1.0 student student information management system')
    print('''
    1-添加学生姓名    
    2-修改学员姓名
    3-查询学员姓名
    4-删除学员姓名
    0-退出
    ''')
    select1=int(input('输入第一步的操作序号'))
    while select1<0 or select1>4:
        select1=int(input('请重新输入1~4'))
    if select1==1:
        name1=input('需要添加的学生姓名:')
        student_list.append(name1)
        print('添加学生姓名成功')
        print('信息系统现有:',student_list)
    if select1==2:
        for index,value in enumerate(student_list):
            print(index+1,value)
        print('修改学生姓名请选择学生学号')
        num1=int(input('修改学生的学号为:'))
        while num1>len(student_list):
            num1=int(input('请输入正确的学号'))
        name1=input('学生的姓名改为:')
        student_list[num1-1]=name1
        print('修改成功')
        print('信息系统现有:',student_list)
    if select1==3:
        print('''
        1-输入序号查询
        2-全部查询
        ''')
        select2=int(input('请输入1/2'))
        if select2 == 1:
            num2=int(input('输入学号'))
            name2=student_list[num2-1]
            print(name2)
        if select2 ==2:
            for index, value in enumerate(student_list):
                print(index+1,value)
    if select1==4:
        print('''
        1-输入学员序号删除
        2-输入学员姓名删除
        3-删除所有学生
        ''')
        select2=int(input('请输入你操作的序号'))
        while select2!=1 and select2 !=2 and select2 !=3:
            select2=int(input('请输入1-2-3进行操作'))
        if select2==1:
            num1=int(input('需要删除的学生学号'))
            student_list.pop(num1)
            print('删除成功')
        if select2==2:
            name1=input('请输入你需要删除的学生姓名')
            student_list.remove(name1)
            print('删除成功')
        if select2==3:
            student_list.clear()
            print('删除学生信息系统成功')
    if select1==0:
        break

