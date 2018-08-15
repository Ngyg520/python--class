"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:怎样使用urllib来设置代理IP和随机请求头.PY
@ide:PyCharm
@time:2018-08-07 14:14:35
"""
#为什么要设置代理IP和随机请求头?
#爬虫默认的User-Agent(python-urllib/python版本)
#1.服务器会判断一个频繁的请求是不是来自于同一个User-Agent标识,或者判断User-Agent是不是一python开头,如果是,则会限制访问
#解决方案:随机切换User-Agent的值

#2.服务器会判断一个频繁的请求是不是来自于同一个IP,如果是,则会对Ip进行限制访问
#解决方案:使用代理IP,随机切换IP地址,不使用真实的IP来发起请求
import urllib.request
import random
#--------------------使用urllib设置请求头-----------------------------------
#定义一个访问的网址:
url='http://httpbin.org/get'
#设置一个浏览器标识的列表
user_agent_list=['Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11']
#设置一个请求头choice随机选择一个
headers={
    'User-Agent':random.choice(user_agent_list)
}
#创建request时,添加headers(请求头)
request=urllib.request.Request(url,headers=headers,method='GET')
response=urllib.request.urlopen(request).read().decode('utf-8')
print(response)

#------------------------------------动态添加请求头-------------------------
#创建request时,没有添加headers,后面添加
result=urllib.request.Request(url,method='GET')
result.add_header('User-Agent','Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;')
response=urllib.request.urlopen(result)
print(response.read().decode('utf-8'))
#----------------------使用urllib设置代理ip--------------------------------------
from urllib.request import ProxyHandler,build_opener
#设置一个代理IP列表
ip_list=[{'http':'http://111.155.116.200:8123'},{'http':'http://139.129.166.68:3128'},{'http':'http://61.135.217.7:80'},{'http':'http://118.190.95.35:9001'}]

#创建一个IP代理对象
proxy_handler=ProxyHandler(random.choice(ip_list))
#根据IP代理对象,创建用于发送请求的opener对象
opener=build_opener(proxy_handler)
opener.addheaders=[('User-Argent','Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;')]
#在使用opener这个对象发起请求
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))