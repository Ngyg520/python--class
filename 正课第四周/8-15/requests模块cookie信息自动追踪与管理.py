"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:requests模块cookie信息自动追踪与管理.PY
@ide:PyCharm
@time:2018-08-15 10:46:29
"""
#requests这个模块,如果直接利用get()或者post等方法可以做到模拟网页的请求,但是每一次请求之间是没有关系的,相当于不同的会话,也就是相当于浏览器打开了两个不同的页面
#设想这样一个场景,第一次请求利用post()方法登录了某个网站,第二次向获取成功登录之后的个人信息,又用了一次get()方法请求个人信息页面,实际上相当于打开了两个浏览器,是完全不相关的两个会话,这样并不能成功获取个人信息
#解决方案:维持同一个会话,也就是相当于使用同一个浏览器打开不同的页面,而不是每次都有设置cookie,这时候就有了session对象
import requests
#请求http://httpbin.org/cookies/set/number/1234567890网址设置cookie信息,名称是number,内容是1234567890,接着请求http://httpbin.org/cookies.这个网址可以获取当前的cookies
requests.get("http://httpbin.org/cookies/set/number/1234567890")
r=requests.get("http://httpbin.org/cookies")
print(r)

session_obj=requests.Session()
session_obj.get(("http://httpbin.org/cookies/set/number/1234567890"))
r=session_obj.get("http://httpbin.org/cookies")
print(r.text)


