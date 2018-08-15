#author:yang
#----使用双重for循环实现一个99乘法表----
for x in range (1,10):
    # 最外层for循环取值1-9
    # x=1,for y in range(1,2) y=1
    # x=2,for y in range(1,3) y=2
    for y in range (1,x+1):
        # print()语句默认有换行符,使用end=''替换掉换行符
        print('%d*%d=%d'%(y,x,x*y),end=' ')
    print('')
#猜数字
#random:python中的随机模块
import random
#首先生成一个随机数
random_number=random.randint(0,100)
#作弊手段
print('猜数字游戏')
#错误次数
error_count=0
#开始猜
while True:
    #因为控制台输入的数字是字符串类型没有办法和整数进行比较,所以使用int转换类型
    input_number=int(input('请输入要猜的数字(0-100):'))
    #不断检测输入的数字是否符合要求,不符合规则从新输入,符合要求则进行判断
    while input_number<0 or input_number>100:
        input_number=int(input('输入的数字不在范围之内,请从新输入'))
    if input_number>random_number:
        print('不好意思,你猜大了!')
        error_count+=1     #错误次数+1
    if input_number<random_number:
        print('你猜小了')
        error_count+=1
    if input_number==random_number:
        print('''恭喜你,猜对了
        1-继续猜
        2-退出
        ''')
        error_count=0
        select_number=int(input('请选择您要操作的序号:'))
        while select_number<1 or select_number>2:
            select_number=int(input('1,2不分?从新选'))
        if select_number == 1:
            random_number=random.randint(0,100)
            # 作弊代码print('随机数',random_number)
        else:
            break
    if error_count>=10:
        #错误次数大于规定次数,运行结束
        print('错误次数已达10次')
        num1=int(input('a'))
        break