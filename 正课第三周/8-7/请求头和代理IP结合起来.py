"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:请求头和代理IP结合起来.PY
@ide:PyCharm
@time:2018-08-07 15:19:00
"""
import urllib.request
import random
from urllib.request import ProxyHandler,build_opener
url='http://httpbin.org/get'
#设置一个浏览器标识的列表
user_agent_list=['Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11']
ip_list=[{'http':'http://111.155.116.200:8123'},{'http':'http://139.129.166.68:3128'},{'http':'http://118.190.95.35:9001'}]

#设置一个请求头choice随机选择一个
headers={
    'User-Agent':random.choice(user_agent_list)
}
#创建request时,添加headers(请求头)
request=urllib.request.Request(url,headers=headers,method='GET')

#创建一个IP代理对象
proxy_handler=ProxyHandler(random.choice(ip_list))
#根据IP代理对象,创建用于发送请求的opener对象
opener=build_opener(proxy_handler)


#使用install_openner方法之后,会将程序中默认的urlopen方法替换掉,也就是说使用install_openner之后,在该文件中,再次调用urlopern会使用以及创建好的operner对象,
# 如果不想替换,只是想临时用一下,可以使用openner.open()这样就不会对程序默认的urlopen有影响
# urllib.request.install_opener(opener)
# response=urllib.request.urlopen()
#在使用opener这个对象发起请求
response=opener.open(request)
print(response.read().decode('utf-8'))
