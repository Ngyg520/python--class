"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:8-7.PY
@ide:PyCharm
@time:2018-08-07 19:17:03
"""
import urllib.request
import requests
import random
from urllib.request import ProxyHandler,build_opener
from bs4 import BeautifulSoup
import re
import os
#https://www.sxtp.net/meinv/xinggan/index_2.html
#/meinv/201801/45129.html
#https://www.sxtp.net/meinv/201801/45129.html
#https://www.sxtp.net/meinv/201801/45115_3.html
#主站
tuple_1=()

for x in range (10,30):
    print('正在下载第%s页'%x)
    url="https://www.sxtp.net/meinv/xinggan/index_"+str(x)+".html"
    user_agent_list=['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # ip_list=[{'http':'http://111.155.116.200:8123'},{'http':'http://139.129.166.68:3128'},{'http':'http://118.190.95.35:9001'}]
    ip_list = [{'http': 'http://121.31.100.29:8123'}, {'http': 'http://219.141.153.41:80'},{'http': 'http://121.31.100.29:8123'}]
    headers={ 'User-Agent':random.choice(user_agent_list)}
    request=urllib.request.Request(url,headers=headers,method='GET')
    proxy_handler=ProxyHandler(random.choice(ip_list))
    opener=build_opener(proxy_handler)
    response=opener.open(request).read().decode('utf-8')
    pattern_obj=re.compile(r'<a title=".*?" href="(.*?).html" target=',re.S)
    result_list=re.findall(pattern_obj,response)
    # print(result_list)
    for min_url in result_list:
        url_1 = "https://www.sxtp.net" +str(min_url)
        url_1_1=url_1+".html"
        # print(url_1)
        #主站的每一个美女
        headers = {'User-Agent': random.choice(user_agent_list)}
        request = urllib.request.Request(url_1_1, headers=headers, method='GET')
        proxy_handler = ProxyHandler(random.choice(ip_list))
        opener = build_opener(proxy_handler)
        response = opener.open(request).read().decode('utf-8')
        pattern_obj = re.compile(r'<em>.*?共(.*?)张.*?<img  alt="点击大图看下一张：(.*?)" src="(.*?)"  />', re.S)
        result_list_1 = re.findall(pattern_obj, response)
        # print(result_list_1)
        for list_sort in result_list_1:
            for  min_girl_num,min_girl_url in enumerate(list_sort):
                # print(min_girl_url)
                 #获取美女的所有网页
                if min_girl_num==0:
                    pages=min_girl_url
                    pages_1=int(pages)
                    for x in range(2,pages_1+1):
                        url_3=url_1+"_"+str(x)+".html"
                        headers = {'User-Agent': random.choice(user_agent_list)}
                        request = urllib.request.Request(url_3, headers=headers, method='GET')
                        proxy_handler = ProxyHandler(random.choice(ip_list))
                        opener = build_opener(proxy_handler)
                        response = opener.open(request).read().decode('utf-8')
                        pattern_obj = re.compile(r'<dt><h1>(.*?)<em>.*?<img  alt=".*?" src="(.*?)"  />',re.S)
                        result_list_2 = re.findall(pattern_obj, response)
                        # print(result_list_2)
                        for tuple_1 in result_list_2:
                            name=tuple_1[0]
                            url_jpg=tuple_1[1]
                            urllib.request.urlretrieve(url_jpg,'./image/{}.jpg'.format(name))
                            print('正在下载-{}'.format(name))

