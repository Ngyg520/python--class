"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:分析ajax请求爬取澎湃新闻.PY
@ide:PyCharm
@time:2018-08-13 10:11:27
"""
#1.访问澎湃新闻主页,在往下属性页面的时候,发现网址无任何变化,页面源代码中没有刷新出来的新闻内容,考虑是ajax请求的数据,可以使用火狐浏览器自带的抓包共工具进行,也可使用Charles进行抓包分析
#2.由于ajax请求多的数据类型是xhr的,所以点击火狐浏览器上面的xhr,发现刷新出来很多相似的请求,并且这些请求对应的响应内容就是动态刷新出来的新闻内容,于是便可以断定,刷新出来的内容就是这些请求得到的
#3.分析这些请求,发现这些请求只有papeidx这个地址的值,还有lastTime这个字段的值是变化着的,papeidx这个字段很容易构造的,但是lastTime这个字段不容易构造,经分析,发现这个字段的值和时间戳很相似,于是想到取时间戳值小数点后三位便和lastTime这个字段的值就可以保持一致,再经测算,发现结果就是如此
import urllib.request
from urllib.parse import urlencode
import re
import json
import time
class PengPaiSpider(object):
    big_list=[]
    def __init__(self):
        self.base_url="https://www.thepaper.cn/load_chosen.jsp?"

    #定义一个函数发起网络请求拿到网页的源代码
    def get_html(self):
        for x in range(1,4):
            params={
            "nodeids":"25949",
            "topCids":"2342071,2341667,2337706,2341786,",
            "pageidx":x,
            "lastTime":str(time.time())[0:14].replace('.',''),
            }
            url=self.base_url+urlencode(params)
            try:
                response=urllib.request.urlopen(url)
                if response.status==200:
                    #200说明请求成功
                    html=response.read().decode('utf-8')
                    #拿到源代码,调用get_detail_info对源代码进行解析
                    self.get_detail_info(html)
            except Exception as  e:
                print('连接失败的原因是:',e)
    #定义一个函数来解析网页源代码
    def get_detail_info(self,html):
        pattern_obj=re.compile(r'<h2>.*?">(.*?)</a>.*?<p>(.*?)</p>.*?<a href.*?target="_blank">(.*?)</a>.*?<span>(.*?)</span>', re.S)
        result_list=re.findall(pattern_obj,html)
        self.chang_to_dict(result_list)
    #定义一个函数用来讲数据转换为字典
    def chang_to_dict(self,result_list):
        #遍历列表中每一个元素的内容,并存放在字典当中
        for title,content,orgin,publish_time in result_list:
            dict_info={"新闻标题":title,"新闻内容":content,"新闻来源":orgin,"发布时间":publish_time}
            self.big_list.append(dict_info)
    #定义一个函数将字典存放在本地
    def save_to_json(self):
        json_data=json.dumps(self.big_list)
        f=open('pengpai.txt','w',encoding='utf-8')
        f.write(json_data)
        f.close()
if __name__ == '__main__':
    PengPai=PengPaiSpider()
    PengPai.get_html()
    PengPai.save_to_json()