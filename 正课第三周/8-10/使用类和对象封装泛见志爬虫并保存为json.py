"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:使用类和对象封装泛见志爬虫并保存为json文件.PY
@ide:PyCharm
@time:2018-08-10 09:28:42
"""
import urllib.request
import re
import random
from urllib.request import ProxyHandler,build_opener
import json
class FJZSpider(object):
    user_agent_list = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    ip_list = [{'http': 'http://123.139.56.238:9999'}, {'http': 'http://119.179.131.245:8060'},{'http': 'http://121.31.156.12:8123'}]

    def __init__(self):
        self.base_url="http://www.27270.com/tag/513.html"
        self.headers={'User-Agent':random.choice(self.user_agent_list)}
        self.ip=random.choice(self.ip_list)

    def get_detail_info(self,total_num):
        for page in range (1,total_num+1):
            print('正在第{}页'.format(page))
            abs_url=self.base_url+"list_16_"+str(page)+".html"
            request=urllib.request.Request(url=abs_url,headers=self.headers)
            ip_proxyhandler = ProxyHandler(self.ip)
            opener = build_opener(ip_proxyhandler)
            response = opener.open(request)

            pattern_obj=re.compile(r'<div class=.*?original="(.*?)"></a></div>',re.S)
            result_list=re.findall(pattern_obj,response)
            return result_list
    def start_spider(self):
        self.get_detail_info(3)

if __name__ == '__main__':
    fjz=FJZSpider()
    fjz.start_spider()
