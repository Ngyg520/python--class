"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:7-26
@author:Mr.Yang
@file:json解析.PY
@ide:PyCharm
@time:2018-07-26 16:06:10
"""
#第三方的用于发送网络请求的一个模块,经常被用于爬虫

import requests
import json
response=requests.get('http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
).text
print(type(response))
print(response)

res_result=json.loads(response)
print(type(res_result))
print(res_result)

#取error的值
error1=res_result['error']
print(error1)
#取status的值
status1=res_result['status']
print(status1)
#取data的值
date1=res_result['date']
print(date1)
#取result的值,取出来的结果是一个列表,列表里面包含一个字典
result1=res_result['results']
print(result1)

#从result1这个列表中取出来这个字典
dict_1=result1[0]
print(type(dict_1))
print(dict_1)
#从dict_1这个字典当中,通过键取值
currentCity=dict_1['currentCity']
print(currentCity)
pm_25=dict_1['pm25']
print(pm_25)
#从dict_1这个字典当中取出键是index的值,对应的是一个列表
index=dict_1['index']
print(index)

#使用for循环遍历index这个列表
for dex in index:
    #取出来的dex都是一个字典
    des=dex['des']
    tipt=dex['tipt']
    title=dex['title']
    zs=dex['zs']
    print(des,tipt,title,zs)


weather_data1=dict_1['weather_data']
for xf in weather_data1:
    data=xf['date']
    dayPictureUrl=xf['dayPictureUrl']
    nightPictureUrl=xf['nightPictureUrl']
    weather=xf['weather']
    wind=xf['wind']
    temperature=xf['temperature']
    print(data,dayPictureUrl,nightPictureUrl,weather,wind,temperature)

