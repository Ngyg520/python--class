while True:
    #input接受的是个字符串,想要与整数比较需要int转换
    score = int(input('请输入你的成绩'))
    if score >=0 and score <60:
        print('你的成绩不及格')
    elif score>=60 and score<70:
        print('你的成绩是D')
    elif score>=70 and score<80:
        print('你的成绩是c')
    elif score >=80 and score<90:
        print('你的成绩是B')
    elif score>=90 and score<=100:
        print('你的成绩是A')

