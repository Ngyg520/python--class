"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:使用urllib和cookie模拟登陆智游教务管理系统.PY
@ide:PyCharm
@time:2018-08-14 14:13:19
"""
#1.分析智游教务管理系统的请求,找到登陆按钮请求得到的地址,分析发现,是一个post请求,请求的地址是:http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr;JSESSIONID=5a141316-ee51-4c21-8fb3-eb26255280e2请求携带两个参数:j_password,j_username
#2.编写代码模拟发送一个携带参数的post请求登陆网站,然后拿到登陆成功之后的cookie信息保存到本地,
#3.下次登陆的时候只需要携带上本地的cookie信息即可完成登陆
import urllib.request
import http.cookiejar
from urllib.parse import urlencode
#定义发起post请求的url地址
post_url="http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr"
#构造参数
post_data=urlencode({"j_username":"18738577851","j_password":"yyj19970711"})
#设置请求头
headers={
    "User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
}
#定义函数来获取cookie信息:
def get_cookie():
    #创建一个MollizaCookieJar的对象
    cookie_obj=http.cookiejar.MozillaCookieJar("stu_cookie.txt")
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
    cookie.load("stu_cookie.txt",ignore_expires=True,ignore_discard=True)
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(handler)
    request=urllib.request.Request("http://kaoshi.zhiyou900.com:8888/edustu/me/edu/meda.spr",headers=headers)
    response=opener.open(request).read().decode('utf-8')
    print(response)

load_cookie()