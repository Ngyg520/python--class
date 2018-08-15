"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:test.PY
@ide:PyCharm
@time:2018-08-07 11:13:21
"""

#http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?
import urllib.parse
import urllib.request
# base_url='http://api.map.baidu.com/telematics/v3/weather'
# data_dict={
#     "location":"郑州市",
#     "output":"json",
#     "ak":"TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ",
#     "callback":"?"
# }
# data_string=urllib.parse.urlencode(data_dict)
# print(data_string)
# new_url=base_url+"?"+data_string
# response=urllib.request.urlopen(new_url)
# print(response.read().decode('utf-8'))
#urllib.urlopen不能带中文,
city=urllib.request.quote('郑州市'.encode('utf-8'))
response=urllib.request.urlopen('http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city))
print(response.read().decode('utf-8'))
