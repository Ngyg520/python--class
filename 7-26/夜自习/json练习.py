"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:7-26
@author:Mr.Yang
@file:json练习.PY
@ide:PyCharm
@time:2018-07-26 19:16:17
"""

import requests
import json
response=requests.get('http://api.map.baidu.com/telematics/v3/travel_attractions?id=yiheyuan&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json').text
# print(type(response))
# print('1',response)

res_result=json.loads(response)
# print('2',res_result)
#第一层
error1=res_result['error']
print('1',error1)
status1=res_result['status']
print('2',status1)
date1=res_result['date']
print('3',date1)
result1=res_result['result']
# print('4',result1)
#第二层
name1=result1['name']
print('5',name1)
location1=result1['location']
print('6',location1)
telephone1=result1['telephone']
print('7',telephone1)
star1=result1['star']
print('8',star1)
url1=result1['url']
print('9',url1)
abstract1=result1['abstract']
print('10',abstract1)
description1=result1['description']
print('11',description1)
ticket_info1=result1['ticket_info']
# print('12',ticket_info1)

#第三层
price1=ticket_info1['price']
print('13',price1)
open_time1=ticket_info1['open_time']
print('14',open_time1)
attention1=ticket_info1['attention']
# print('15',attention1)
#第四层

for x in  attention1:
    name2=x['name']
    print('16',name2)
    description1=x['description']
    print('17',description1)























