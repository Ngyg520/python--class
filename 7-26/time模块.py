"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:7-26
@author:Mr.Yang
@file:time模块.PY
@ide:PyCharm
@time:2018-07-26 10:51:58
"""
import time
#一.获取时间戳
#1.获取时间戳--单位为秒,从1970年1月1日00:00到现在一共经历的时间是多少秒.
#2.时间戳一般验证登录是否是否过期
timetamp=time.time()
print(timetamp)
#二.localtime():用于获取本地时间的函数,返回值是一个元组
localtime=time.localtime()
print(localtime)
print(localtime.tm_year)#打印年份
print(localtime.tm_mon)#打印月份
print(localtime.tm_mday)#打印今天日期

#三.asctime():获取格式化的本地时间
local_time=time.asctime(time.localtime())
print(local_time)

#四,将本地时间元组格式化成2018-7-26 11:01:xx的形式
#strftime:将时间元组转化成格式化的时间字符串
print(time.asctime())#打印出本地时间

time_1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(time_1)#打印出本地时间,可以添加格式


#五.strptime:将格式化的字符串转换成时间元组
string='Thu Jul 26 14:07 2018'
time_2=time.strptime(string,'%a %b %d %H:%M %Y')
print(time_2)

string1='2018-07-26 14:20:55'
time_3=time.strptime(string1,'%Y-%m-%d %H:%M:%S')
print(time_3)

#2018-7-26 14 Thu Jul
string2='2018-7-26 14:04 Thu Jul'
time_4=time.strptime(string2,'%Y-%m-%d %H:%M %a %b')
print(time_4)

#将时间元组格式化成字符串:14:05:30 7-26-18
time_5=time.strftime('%H:%M:%S %m-%d-%y',time.localtime())
print(time_5)