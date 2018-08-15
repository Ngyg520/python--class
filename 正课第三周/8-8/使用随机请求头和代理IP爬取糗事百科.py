"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:使用随机请求头和代理IP爬取糗事百科.PY
@ide:PyCharm
@time:2018-08-08 09:26:45
"""
#分析要爬取网站的URL,找到其中的规律
#2.对网站发起请求,获取网站源代码
#3,根据源代码,使用正则表达式匹配出来我们想要的信息]
#4.把获取的信息存储出来

import urllib.request
from urllib.request import ProxyHandler,build_opener
import re
import random
import sqlite3

#设置爬取网址的基础网址
base_url="https://www.qiushibaike.com/hot/"
#设置一个请求头列表
user_agent_list=['Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11']
ip_list=[{'http':'http://111.155.116.200:8123'},{'http':'http://139.129.166.68:3128'},{'http':'http://118.190.95.35:9001'}]
#设置一个请求头
headers={
    'User-Agent':random.choice(user_agent_list)
}
#设置IP代理对象
proxy_handler=ProxyHandler(random.choice(ip_list))
#定义一个爬取糗事百科的函数,
def downlowd_qsbk(page):
    #设置详细的url地址
    abs_url=base_url+"page/"+str(page)+"/"
    request=urllib.request.Request(abs_url,headers=headers)
    #根据IP代理对象设置opener对象
    opener=build_opener(proxy_handler)
    #对网址发起访问,拿到源代码
    resoponse=opener.open(request).read().decode('utf-8')
    pattern_obj=re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender .*?Icon">(.*?)</div>.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
    #定义去掉换行符\n和<br/>和&quot:
    remove_n=re.compile(r'\n')
    remove_br=re.compile(r'<br/>')
    remove_quote=re.compile(r'&quote:')
    all_info_list=re.findall(pattern_obj,resoponse)
    # print(all_info_list)#获取网页
    for nick_name,age,content,smile_num,comment_num in all_info_list:
        nick_name=re.sub(remove_n,'',nick_name)
        content=re.sub(remove_n,'',content)
        content=re.sub(remove_br,'',content)
        inser_sql="insert into baike(nick_name,age,content,smile_num,comment_num)VALUES('%s','%s','%s','%s','%s')"%(nick_name,age,content,smile_num,comment_num)
        cursor.execute(inser_sql)
        # print('用户昵称:',nick_name)
        # print('用户年龄:',age)
        # print('内容:',content)
        # print('好笑数',smile_num)
        # print('评论数',comment_num)


if __name__=='__main__':
    connect=sqlite3.connect('qsbk.db')
    cursor=connect.cursor()
    create_table="create table if not EXISTS baike(id INTEGER PRIMARY KEY ,nick_name VARCHAR ,age VARCHAR ,content VARCHAR ,smile_num VARCHAR ,comment_num VARCHAR )"
    cursor.execute(create_table)
    for x in range(1,10):
        downlowd_qsbk(x)
    connect.commit()
    cursor.close()
    connect.close()



# downlowd_qsbk(1)















