"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:使用urllib库发送get和post请求.PY
@ide:PyCharm
@time:2018-08-07 10:08:02
"""
#urllib是python中内置的发送网络请求的一个库,在python2中由urllib和urllib2两个库来实现请求的发送,但是在python中 已经不存在urllib2这个库,已经合并为urllib
import urllib.request
#urllib是一个库,resquest是ullib库里面用于发送网络请求的一个模块

#发起一个不携带参数的get请求
response=urllib.request.urlopen('http://www.baidu.com')
#response调用属性
print(response.reason)
print(response.status)#得到此时响应的状态码
print(response.url)#可以获得此次请求的地址
print(response.headers)
#由于使用read方法拿到的响应的数据是二进制数据,所以需要使用decode解码成utf-8
# print(response.read().decode('utf-8'))

#--------------------构造一个get请求----------------------------------
import urllib.parse
#http://www.yundama.com/index/login?username=4554654654654&password=dasdwa+&utype=1&vcode=74456

#定义出基础网址(字符串)
# base_url='http://yundama.com/index/login'
# #构造一个参数字典
# data_dict={
#     "username":"131313121",
#     "password":"21431421",
#     "utype":"1",
#     "vcode":"321213"
# }
# #使用parse中urlencode这个方法将字典序列化成字符串,最后和基础网址进行拼接
# data_string=urllib.parse.urlencode(data_dict)
# print(data_string)
# new_url=base_url+"?"+data_string
# response=urllib.request.urlopen(new_url)
# print(response.read().decode('utf-8'))
#----------------------------------------测试------------------------------------
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
#注意事项:::
#如果直接将中文传入URL中请求,会导致编码错误,我们需要使用.quote(),对该中文关键字进行URL编码
# city=urllib.request.quote('郑州市'.encode('utf-8'))
# response=urllib.request.urlopen('http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city))
# print(response.read().decode('utf-8'))
#-------------------------构造一个携带参数的post请求-------------------
#测试网址:http://httpbin.org/post
data_dict={"username":"zhangsan","password":"123456"}
#使用parse中的urlencode将字典序列化成字符串
data_string=urllib.parse.urlencode(data_dict)
#将序列化后的字符串转化成二进制,因为post请求携带的是二进制参数
last_data=bytes(data_string,encoding='utf-8')
#如果给urlopen这个函数传递了data这个参数,那么它的请求方式则不是get请求,而是post请求
response=urllib.request.urlopen("http://httpbin.org/post",data=last_data)
#我们的参数出现在from表单中,这表明是模拟了表单的提交方式,以post方式传输数据
print(response.read().decode('utf-8'))

#timeout设置响应时间
response=urllib.request.urlopen('https://www.baidu.com',timeout=2)
print(response.read().decode('utf-8'))

