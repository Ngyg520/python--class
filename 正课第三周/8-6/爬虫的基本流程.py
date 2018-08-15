"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:爬虫的基本流程.PY
@ide:PyCharm
@time:2018-08-06 15:41:44
"""
#一个爬虫程序通常分为三个部分:
#1.获取网页
#爬虫首先要做的就是获取网页,这里就是指网页的源代码,源代码里面包含着部分有用的信息,所以只要把源代码获取下来,就可以从中提取想要的信息(向服务器发起一个请求,返回的响应内容就是网页的源代码),所以最关键的部分就是构造一个请求并发送给服务器,然后就收到响应的源代码并将其解析出来.

#2.提取信息.
#获取网页源代码之后,就可以分析网页源代码,从中提取想要的数据,一个最通用的方法,正则表达式,它是一个万能的方法,但是构造一个正则表达式的时候,比较复杂而且容易出错.所以还可以使用xpath,BeautifulSoup等来进行网页的解释

#3.保存数据,
#提取到数据之后,一般会将提取到的数据保存起来以便后续的使用,既可以保存为TEXT文件,或者JSON文件,也可以保存为Excel文件,也可以保存到sqlite3,Mysql,MonogoDB等数据库之中