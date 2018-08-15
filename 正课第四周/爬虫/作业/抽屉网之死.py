"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:抽屉网之死.PY
@ide:PyCharm
@time:2018-08-14 15:07:59
"""
import urllib.request
import http.cookiejar
from urllib.parse import urlencode
#定义发起post请求的url地址
post_url="https://dig.chouti.com/login"
#构造参数
post_data=urlencode({"phone":"8618538606559","password":"sjh666"})
#设置请求头
headers={
    "User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
}
#定义函数来获取cookie信息:
def get_cookie():
    #创建一个MollizaCookieJar的对象
    cookie_obj=http.cookiejar.MozillaCookieJar("ctw_cookie.txt")
    #根据cookie_obj对象创建一个用于管理cookie信息操作对象的handler
    cookie_handler=urllib.request.HTTPCookieProcessor(cookie_obj)
    #根据cookie_handler创建一个opener对象
    opener=urllib.request.build_opener(cookie_handler)
    #对post_url发起请求(转二进制数据)
    data_bytes=bytes(post_data,encoding='utf-8')
    #创建一个request对象
    request=urllib.request.Request(post_url,data_bytes,headers)
    #根据opener对象来发起请求
    response=opener.open(request).read().decode('utf-8')
    # print(response)
    #登录成功之后,将服务器返回的cookie信息保存到本地
    cookie_obj.save(ignore_discard=True,ignore_expires=True)

get_cookie()

def load_cookie():
    cookie=http.cookiejar.MozillaCookieJar()
    cookie.load("ctw_cookie.txt",ignore_expires=True,ignore_discard=True)
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(handler)
    request=urllib.request.Request("https://dig.chouti.com/user/link/saved/1",headers=headers)
    # response=urllib.request.Request("https://dig.chouti.com/link/vote?linksId=21462511",headers=headers,data=data_bytes)
    response=opener.open(request).read().decode('utf-8')
    print(response)

load_cookie()

