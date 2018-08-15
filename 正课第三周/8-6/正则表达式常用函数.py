"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:正则表达式常用函数.PY
@ide:PyCharm
@time:2018-08-06 17:37:21
"""
import re
#match和search取值最好加.group
#findall直接索引取值

#match():是从目标字符串的开头位置开始匹配,仅限于开头位置,匹配成功则返回match对象,否则返回None
patten_obj=re.compile('(my)')
res=re.match(patten_obj,'myhjaad')
print(res.group(1))

#search();从目标字符串的任意位置开始匹配数据,仅匹配一次,如果目标字符串有多个符合要求的结果,也只能找到一个
patten_obj=re.compile('(my)')
res=re.search(patten_obj,'hahmyheiheimy')
print(res.group(1))
print(res[0])

#findall():搜索整个字符串,会将所有匹配成功的字符串都返回出来
patten_obj=re.compile('my')
res=re.findall(patten_obj,'hahshamyajsdbnsadnfiasdosmyabui')
print('==',res[0])
print('--',res[1])
for x in res:
    print('-',x)

#split():以匹配到的符合要求的字符串为分隔符,将目标字符串分割成有个列表
patten_obj=re.compile('my')
res=re.split(patten_obj,'hahsdhmyhbdmy')
print('+++',res)
#sub():使用一个新的字符来替换目标字符串中符合匹配要求的字符
patten_obj=re.compile('-')
res=re.sub(patten_obj,'+','a-b-c')
print(res)