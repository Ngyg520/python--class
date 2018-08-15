# #--------------------------------练习1----------------------
# while True:
#     input_grade=float(input('请输入你的成绩(0-100)'))
#     while input_grade<0 or input_grade>100:
#         input_grade=float(input('请输入正确的成绩范围'))
#     if input_grade>=0 and input_grade<60:
#             print('不及格')
#     elif input_grade>=60 and input_grade<70:
#             print('成绩D等')
#     elif input_grade>=70 and input_grade<80:
#             print('成绩C等')
#     elif input_grade>=80 and input_grade<90:
#             print('成绩B等')
#     elif input_grade>=90 and input_grade<=100:
#             print('成绩A等')
# #--------------------------练习2---------------------------------
# while True:
#   w=int(input('请输入你的体重(公斤)'))
#   h=int(input('请输入你的身高(厘米)'))
#   optimal_weight=h-105
#   if optimal_weight<w:
#      print('偏重')
#   if optimal_weight>w:
#      print('偏轻')
#   if optimal_weight== w :
#         print('刚刚好')
# #------------------------练习3---------------------------------
#
# #男生要求
# while True:
#     female_age=int(input('请输入女性年龄'))
#     if female_age<20 or female_age>=28:
#         print('年龄不符合')
#     female_height=int(input('请输入女性的身高'))
#     if female_height<150 or female_height>=180:
#         print('身高不符合')
#         female_weight=int(input('请输入女性的体重'))
#         if female_weight < 40 or female_weight >60:
#             print('体重不符合')
#             female_income=int(input('请输入女性的收入'))
#             if female_income < 2000 or female_income > 5000:
#                 print('收入不符合')
#                 female='她的年龄{0},身高{1},体重{2},收入{3}'.format(female_age,female_height,female_weight,female_income)
#                 print(female)
# #女性要求
# male_age=int(input('请输入男性年龄'))
# if male_age <22 or male_age>30:
#     print('男性年龄不符合')
# male_height=int(input('请输入男性身高'))
# if male_height <165 or male_height>190:
#     print('男性身高不符合')
# male_weight=int(input('请输入男性的体重'))
# if male_weight <50 or male_weight>70:
#     print('男性体重不符合')
# male_income=int(input('请输入男性的收入'))
# if male_income <20000 :
#     print('男性收入不符合')
# male='他的年龄{0},身高{1},体重{2},收入{3}'.format(male_age,male_height,male_weight,male_income)
# print(male)
# #--------------------------练习4-------------------------------
# while True:
#     km=int(input('请输入路程/公里'))
#     if km<=0:
#         print('请输入正确的公里数进行计算')
#         break
#     if km<=2:
#         money=(8)
#         print(money)
#     if km>2 and km<=12:
#         money=((km-2)*1.2+8)
#         print(money)
#     if km>12:
#         money=(20+(km-12)*1.5)
#         print(money)
# # -----------------------------------练习5----------------------
# # 表
# list=['多','少','春','秋']
# print('''
# 1.添加学员姓名
# 2.修改学员姓名
# 3.查询学员姓名
# 4.删除学员姓名
# 0.退出程序
# ''')
# select_number=int(input('请输入你的数字'))
# if select_number==1:
#     list.append(input('请输入姓名'))
# print(list)
# if select_number==2:#2成为必须的步骤
#     for index, value in enumerate(list):#枚举函数查询序号
#         print(index, value)
# list[int(input('输入序号'))]=input('请输入你确认的姓名')
# print(list)
# if select_number==3:
#     t_releter=print('''
#     5,输入序号查询
#     6,查询所有学员
#     ''')
#     t_releter=int(input('请输入你选择的序号'))
#     if t_releter == 5:
#         for index, value in enumerate(list):# 枚举函数查询序号
#             print(index, value)
#         list=list[int(input('输入序号'))]
#         print(list)
#     if t_releter == 6:
#         for index, value in enumerate(list):
#             print(index, value)
# if select_number==4:
#     a=int(input('输入序号'))
#     list.pop(a)#序号删除
#     print(list)
#     list.remove(input('删除的姓名'))#按容器内容删除
#     while len(list):#不知道错在哪里
#         del list[0]
#         print(list)
# else:
#
#
#
#
#
#
#
#
#
