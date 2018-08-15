"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:requests.PY
@ide:PyCharm
@time:2018-08-15 10:08:58
"""
import requests
#使用requests发起一个get请求
response=requests.get('http://www.baidu.com')
print(response)
print(type(response))
#打印此次请求的地址
print(response.url)
#打印此次请求的请求头
print(response.headers)
#打印此次请求的cookie信息
print(response.cookies)
for key,value in response.cookies.items():
    print(key,'=',value)
#打印此次请求的状态码
print(response.status_code)
#获取网页内容
print(response.text)#字符串
print(response.content)#二进制数据

#------------------使用requests构造一个携带参数的get请求-----------------------
test_url_get="http://httpbin.org/get"
params={
    "username":"zhangsan",
    "password":"123456"
}
#使用requests,如果不设置请求头,则默认的请求头是python-requests/requests号
response=requests.get(test_url_get,params=params)
print(response.text)
#当访问一个网址得到的json字符串,则可以直接调用json()函数,直接将返回的结果转换成字典可以直接解析json就不需要导入json模块,再使用json.load()来进行转化了
print(response.json())
print(type(response.json()))

#--------------------使用requests构造一个携带参数的post请求---------------
test_url_post="http://httpbin.org/post"
data={
    "name":"list",
    "mima":"678910"
}
response=requests.post(test_url_post,data=data)
print(response.text)

#-----------------使用requests设置随机请求头和代理IP--------------------
test_url="http://httpbin.org/get"
proxy={"http":"https://106.58.150.29:80"}
headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
response=requests.get(test_url,proxies=proxy,headers=headers)
print(response.text)
