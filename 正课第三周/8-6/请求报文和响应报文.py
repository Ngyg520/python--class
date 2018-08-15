"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:请求报文和响应报文'.PY
@ide:PyCharm
@time:2018-08-06 09:45:53
"""
#http有两类报文:请求报文和响应报文


#--------------------------------------------请求报文------------------------------
#1.请求报文的组成结构(必须会):
#请求行+请求头+空行+请求数据
#请求行的组成:请求行由请求方法URL字段和HTTP协议版本3个字段组成,这三个字段之间用空格分隔,例如:GET/index.html HTTP/1.1

#请求头:请求头由键值对组成每一行有一个键值对,请求头用来通知服务器关于的客户端信息的.
'''
User-Agent:请求表示(浏览器标识)
HOST:请求的主机地址
Connection:客户端和服务器之间的连接状态
Accept:能识别的数据类型
Cookie:服务端给客户端返回的连接状态的标识
'''

#请求数据(请求体):客户端向服务器传递的一些数据

#-----------------------------------------响应报文-------------------------------
#响应报文的组成结构(必会):
#状态行+响应头+空行+响应数据
#1.状态行:HTTP版本+状态码+状态码解释短语.例:HTTP/1.1 302 Moved Teporaily
#2.响应头:响应头由键值对组成,每行一对,响应头包含着向客户端反馈的信息
'''
Set-Cookie:服务器向客户端返回的一个随机字符串,标记着服务器和客户端之间的连接状态
Content-Type:服务器返回的数据类型
Content-length:服务器返回的数据长度
Server:服务类型
Expires:过期时间
'''

#3.响应数据(响应体):存放的服务器向客户端返回的数据


#常用的请求方法(至少说出5中方法,熟练掌握GET/POST)
#1.GET;请求指定的页面信息,并返回实体主体.
#2.post:向指定资源提交数据进行处理,数据被包含在请求体中
#3.HEAD:类似于get请求,只不过返回的响应中没有具体内容,用户获取报头,
#4.PUT:从客户端向服务器传输的数据取代指定的文档内容
#5.Delete:请求服务器删除指定的页面
#6.Trace:回显服务器收到的请求,主要用于测试或者诊断.

#常用的状态码:
#1.100-199:表示服务器成功接收部分请求,要求客户端继续提交其余的请求才能完成处理过程
#200-299:表示服务器成功接收请求,并且已经完成整个过程的处理,常用的状态码200(请求成功)
#300-399:为完成请求,客户端进一步细化请求,例如:请求的资源已经移动到一个新的网址,常见的302(所请求的页面已经临时转移到新的地址)
#4,400-409:客户端的请求有错误,常见的404(服务器无法找到被请求的页面),403(服务器拒绝被访问)
#5.500-599:服务器出现错误,常见500(请求未完成,服务器遇到不可预知的错误)

