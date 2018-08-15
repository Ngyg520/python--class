"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:json文件.PY
@ide:PyCharm
@time:2018-08-13 11:36:59
"""
import  json
f=open('pengpai.txt','r',encoding='utf-8')
res=json.loads(f.read())
for dict_test in res:
    print(dict_test['新闻标题'])
    print(dict_test['发布时间'])