"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:2json.PY
@ide:PyCharm
@time:2018-08-10 10:29:56
"""
import json
f=open('泛见志.txt','r',encoding='utf-8')
res=json.loads(f.read())
print(res)