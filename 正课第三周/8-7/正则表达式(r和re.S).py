"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:正则表达式(r和re.S).PY
@ide:PyCharm
@time:2018-08-07 09:30:32
"""
import re
#r'':一般用在正则表达式中,称之为原始字符串,作用是将python语法中的反斜杠转义给取消,将其设置成一个普通的字符串,可以解决python中转义字符串产生的问题
print('a\nb')#python换行符\n,
print(r'a\nb')
print('123\b456')#python表示退格的作用
#\b正则表达式中表示的匹配边界位置
pattern_obj=re.compile(r'\bword\b')
res=re.search(pattern_obj,'abc word 123')
print(res[0])

#re.S:作用是将字符串中的换行符当做一个普通的字符来处理,让正则表达式匹配的时候不受到换行符的影响,把所有行的字符串都看成一个整体来处理
string='''my name is
heihei your name is
haha
'''
pattern_obj=re.compile(r'my(.*?)haha',re.S)
res=re.search(pattern_obj,string)
print(res)
print(res[0])
print('group',res.group(1))
#默认情况下,正则表达式在使用search和match匹配的时候,是按照整行内容进行匹配的,如果在当前行没有匹配成功,则切换到下一行继续进行匹配.
