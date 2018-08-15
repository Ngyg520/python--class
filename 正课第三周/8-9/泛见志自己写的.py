"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:泛见志自己写的.PY
@ide:PyCharm
@time:2018-08-09 14:19:23
"""
import re
import urllib.request
import random
from urllib.request import ProxyHandler,build_opener
#http://www.fanjian.net/huati
# http://www.fanjian.net/duanzi
# http://www.fanjian.net/duanzi-2
# http://www.fanjian.net/duanzi-3
class FJZSpider (object):
    user_agent_list = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    ip_list = [{'http': 'http://121.31.100.29:8123'}, {'http': 'http://219.141.153.41:80'},{'http': 'http://121.31.100.29:8123'}]
    def __init__(self,fjz_id):
        self.duanzi_id=fjz_id
        self.base_url='http://www.fanjian.net/{}'.format(self.duanzi_id)
        self.headers={'User-Agent':random.choice(self.user_agent_list)}
        self.ip=random.choice(self.ip_list)
    #获取总页数
    def get_total_page(self):
        request=urllib.request.Request(url=self.base_url,headers=self.headers)
        ip_proxyhandler=ProxyHandler(self.ip)
        opener=build_opener(ip_proxyhandler)
        reponse = opener.open(request).read().decode('utf-8')

        patter_obj=re.compile(r'共(.*?)页')#总页数
        total_page=int(re.search(patter_obj,reponse)[1])
        self.get_user_and_comment(total_page)
    #获取每一页的源代码
    def get_user_and_comment(self,total_page):
        for page_num in range(1,total_page+1):
            print('正在爬取第{}页'.format(page_num))
            abs_url=self.base_url+"-"+str(page_num)
            request=urllib.request.Request(url=abs_url,headers=self.headers)
            ip_pro_handler=ProxyHandler(self.ip)
            opener=build_opener(ip_pro_handler)
            reponse = opener.open(request).read().decode('utf-8')
            # response=urllib.request.urlopen(self.base_url).read().decode('utf-8')

            pattern_obj=re.compile(r'<a href=.*?target="_blank" title="(.*?)" class=".*?<p>(.*?)</p>.*?<div class=".*?吐槽</em> (.*?) </a>.*?<span class=.*?title=.*?</span> (.*?)<span class=.*?title=.*?</span> (.*?)<span class=',re.S)
            result_list=re.findall(pattern_obj,reponse)
            self.save_data(result_list)
    def save_data(self,result_list):
        file_test=open("{}.txt".format(self.duanzi_id),'a+',encoding='utf-8')
        for x in result_list:
            file_test.write('用户名字:{}'.format(x[0]))
            file_test.write("\n")
            file_test.write("内容:{}".format(x[1]))
            file_test.write("\n")
            file_test.write("吐槽:{}".format(x[2]))
            file_test.write("\n")
            file_test.write("访问量:{}".format(x[3]))
            file_test.write("\n")
            file_test.write("时间:{}".format(x[4]))
            file_test.write("\n")
            file_test.write("----------------")
    def start_spider(self):
        print('爬虫以启动')
        self.get_total_page()
if __name__ == '__main__':
    Spider=FJZSpider('huati')
    Spider.start_spider()