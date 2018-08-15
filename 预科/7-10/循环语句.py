#循环打印1-10的数字
#for循环
#while循环

#for循环..................
#range():python的内置函数,用于设置范围.range()函数:取头不取尾.range(1,11)取值1-10 range(1-12)取值1-11
for x in range (1,11):
    print(x)

string='恭喜lpl获得洲际赛冠军'
for s in string :
    print(s)
#一般来说,能使用for循环遍历的,都可以称之为可迭代对象.
#循环中的两个关键字:
#continue:用于中断for/while循环中的某一次循环,剩下的循环还会执行完毕
#break:用于中断整个for/while循环

for y in range(1,6):
    if y==2 :
        break
    else:
        print('===',y)


for y in range(1,6):
    if y==2 :
        continue
    else:
        print(y)

for f in range(0,3000):
    if f >500:
        print('nizhongjiangle ')
    else:
        break
#-----------------------------------------while----循环----------------------------------------------
#while循环,执行的依据是判断while后面跟的条件是否成立,一般用于在不知道循环次数的情况下,使用while循环
#当while后面跟的条件一直为真时,就会成为死循环
# while True:
#     print('这是一个死循环')

num = 1
while num<=520:
    print('521')
    num+=1





