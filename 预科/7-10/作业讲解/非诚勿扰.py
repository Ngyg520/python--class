man_age=int(input('请输入男生的年龄:'))
man_height=int(input('请输入男生的身高:'))
man_weight=int(input('请输入男生的体重(公斤):'))
man_income=int(input('请输入男生的收入:'))

woman_age=int(input('请输入女生的年龄:'))
woman_height=int(input('请输入女生的身高:'))
woman_weight=int(input('请输入女生的体重(公斤):'))
woman_income=int(input('请输入女生的收入:'))

if (20<=woman_age<=30) and (160<=woman_height <=170) and (50<=woman_weight <=60)and (2000<=woman_income <=3000):
    #再判断女生符合男生的要求下,判断男生是否符合女生的要求
    if (22<=man_age<=25) and (170<=man_height <=180) and (70<=man_weight <=80) and (10000<=man_income ):
        print('配对成功')
    else:
        print('男生不符合女生的要求')
else:
    print('女生不符合男生的要求')