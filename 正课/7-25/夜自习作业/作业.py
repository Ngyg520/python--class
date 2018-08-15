"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:作业.PY
@ide:PyCharm
@time:2018-07-25 19:28:39
"""
from functools import reduce

# 1.利用map()和reduce()函数，实现类似于int()的功能。比如:'123'-123

# dict1={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}
# print(reduce(lambda x,y:x*10+y,map(lambda string:dict1[string],input('请输入数字'))))




#2.利用map()实现类似于字符串的lower()函数的功能。比如将AbCdEF全部转换成小写
def all_char():
    all_char_dict = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e','F':'f', 'G':'g', 'H':'h', 'I':'i','J':'j', 'K':'k', 'L':'l', 'M':'m','N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u','V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z'}

str1='fFGWEGJdfwaf'



