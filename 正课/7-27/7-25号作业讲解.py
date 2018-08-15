"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:7-25号作业讲解.PY
@ide:PyCharm
@time:2018-07-27 09:23:58
"""
#1.利用map()和reduce()函数，实现类似于int()的功能。比如:'123'-123
from functools import reduce
#'123'转换成整数123
#两个步骤:
#1,先将字符串'123'中的每一个字符'1','2','3'转换成数字1,2,3,---使用map函数,
#2,将每一个数字进行相应的处理,使其成为123---使用reduce
def char_to_number(string):
    all_number_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    #以参数string为键,取出all_number_dict中的值
    return all_number_dict[string]
res=list(map(char_to_number,'132'))
print(res)

def result_number(x,y):
    res=x*10+y
    return res
result=reduce(result_number,res)
print('最终的结果:',result,'最终的类型',type(result))

#整体进行封装,使其使用起来和int一样函数一样方便
def INT(s):
    def char_to_number(string):
        all_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        # 以参数string为键,取出all_number_dict中的值
        return all_number_dict[string]
    def result_number(x, y):
        res = x * 10 + y
        return res
    return reduce(result_number,map(char_to_number,s))

res=INT('456')
print(type(res))
print(res)

#2.利用map()实现类似于字符串的lower()函数的功能。比如将AbCdEF全部转换成小写
def char_lower(string):
    all_char_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i','J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r','S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    #声明一个变量,记录下最终的转换结果
    result=''
    #遍历下string这个字符串,将其中的大写字符转化成小写
    for char_str in string :
        if char_str.isupper():
            #如果从string字符串中取出来的字母是大写,则从字典中取出对应的小写字母
            every_char_result=all_char_dict[char_str]
            #every_char_result:'a'
        else:
            every_char_result=char_str
            #'c'
        result+=every_char_result
        #result:ac
    return result

res=char_lower('AfdsfSSf')
print(res)
res1=list(map(char_lower,['AbcDdfG','dFGEFcdsd']))
print(res1)

def custom_lower(s):
    def char_lower(string):
        all_char_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i','J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r','S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
        # 声明一个变量,记录下最终的转换结果
        result = ''
        # 遍历下string这个字符串,将其中的大写字符转化成小写
        for char_str in string:
            if char_str.isupper():
                # 如果从string字符串中取出来的字母是大写,则从字典中取出对应的小写字母
                every_char_result = all_char_dict[char_str]
                # every_char_result:'a'
            else:
                every_char_result = char_str
                # 'c'
            result += every_char_result
            # result:ac
        return result
    if isinstance(s,list):
        #isinstance():判断某一变量是否属于某一个类型.如果是则返回True,否就返回False
        return list(map(char_lower,s))
    else:
        return char_lower(s)
res1=custom_lower(['KsdsSD'])
print(res1)