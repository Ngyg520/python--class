"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:urllib中cookie的使用.PY
@ide:PyCharm
@time:2018-08-14 11:08:04
"""
#-------------------------如何获取cookie信息--------
import http.cookiejar,urllib.request
#第一步,声明一个cookiejar对象
cookie_obj=http.cookiejar.CookieJar()
#第二步,根据cookiejar对象创建cookie信息的管理对象handler
handler=urllib.request.HTTPCookieProcessor(cookie_obj)
#第三步,根据handler对象创建一个opener对象
opener=urllib.request.build_opener(handler)
#第四步,根据opener对象打开网址
response=opener.open("http://www.baidu.com")
#这样cookiejar对象cookie_obj就保存了该网址的cookie信息
for item in cookie_obj:
    print(item.name+"=",item.value)

#----------------------如何将cookie信息保存到本地---------------------
#                       cookieJar
#                            /
#                           FileCookieJar
#                          /          \
#                 MozillaCookieJar     LWPCookieJar
#MozillaCookieJar和LWPCookieJar都是用于将cookie信息保存在本地文件的一种形式,区别在于使用MozillaCookieJar生成的Cookie信息,会保存为Mozilla类型的Cookie格式,使用LWPCookieJAR会将cookie信息保存为libwww-pel格式的cookie文件

#声明一个MozillaCookieJar或者LwpCookieJar的一个对象
cookie_mozilla_obj=http.cookiejar.MozillaCookieJar(filename="cookie.txt")
#第二步:根据MozilaCookiejar生成的对象cookie_Mozilla_obj,来创建一个cookie信息的管理对象handler
hander=urllib.request.HTTPCookieProcessor(cookie_mozilla_obj)
#第三步:根据handler对象创建opener对象
opener=urllib.request.build_opener(handler)
#第四步:根据opener对象对网址发起请求
response_test=opener.open("http://www.baidu.com")
#第五步:将cookie信息保存在本地
#ignor_descard=True.即使cookie信息将要过期/作废,也仍要读取cookie信息
#ignor_expires=True,即使cookie信息在文件中已经存在,任然对其进行覆盖写入
cookie_mozilla_obj.save(ignore_expires=True,ignore_discard=True)

#------------------读取cookie信息对网站进行访问----------------------
#第一步:声明一个MozillaCookiejar对象
cookie_obj=http.cookiejar.MozillaCookieJar()
#第二步:假装本地cookie信息
cookie_obj.load(filename='cookie.txt',ignore_expires=True,ignore_discard=True)
#第三步:根据cookie_obj创建cookie信息的管理对象handler
handler=urllib.request.HTTPCookieProcessor(cookie_obj)
#第四步:根据handler创建一个opener对象
opener=urllib.request.build_opener(handler)
#第五步:根据opener对象调用open方法对网站发起请求
response_sex=opener.open("http://www.baidu.com")
print(response_sex.read().decode("utf-8"))
