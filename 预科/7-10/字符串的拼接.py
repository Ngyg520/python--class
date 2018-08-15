#author:张
#拼接字符串:就是讲不同的字符串或者变量拼接成一个完整的字符串内容.
#第一种:使用占位符拼接字符串
#%d:整数类型的占位符
age=20
score=100
result ='小明的年纪 是%d,成绩是%d'%( age, score)
print(result)

height=188
result='小刚的身高是%d'%height
print(result)
#拼接字符串的时候,如果只拼接一个变量,那么%后面不需要添加(),拼接两个或以上的变量需要添加()
#%f:小数类型的占位符,用于拼接小数类型的变量,默认情况下会取小数点后六位
weight=135.5
result2='小红的体重是%f'%(weight)
result3='小红的体重是%.1f'%weight
result4='小红的体重是%.2f'%weight
print(result2)
print(result3)
print(result4)

#%s:通用占位符,可以拼接任意类型的数据.
name='张三'
age=18
height=178.5
sex='male'
result5='他的名字是%s,年龄是%s,身高是%s,性别是%s'%(name,age,height,sex)
print(result5)

#第二种:使用+拼接,只能拼接字符串类型的数据
result6='今'+'晚'+'吃'+'鸡'+'吧'+'?'
print(result6)

#第三种:使用.format()对字符串进行拼接的时候,小括号中填写的要拼接的变量.{}中设置的拼接变量的顺序,顺序的编号默认是从0开始,依次向后+1

name='小白'
age=20
sex='famle'
weight=130.5
result7={'她的姓名是{0},年龄是{1},性别是{2},体重是{3}'.format(name,age,sex,weight)}
print(result7)
