#if...if...
#if...else..
#if...elif...
name='张三'
#"==":比较运算符,用0于比较左右两边的值是否相等.结果返回的true和false
#python中对代码的缩进要求十分严格,因为python是通过缩进来判断代码之间的包含关系.如果某行代码的缩进比前面的缩进的多,说明该行代码是包含关系.如果代码之间的缩进一致,说明是同等级关系
if name =="李四":
    print('姓名是李四')
if name =="张三":
    print('姓名是张三')
if name =="王五":
    print('姓名是王五')

age=20
if age==20:
    print('年龄是二十岁')
else:
    print('年龄不是二十岁')

animal="小狗"
if animal=="小猫":
    print('这个动物是小猫')
elif animal=="小熊":
    print('这个动物是小熊')
elif animal=="小鹿":
    print('这个动物是小鹿')
elif animal=="小狗":
    print('这个动物是小狗')

age='2'
if age =='3':
    print('假的')
if age=='2':
    print('真的')