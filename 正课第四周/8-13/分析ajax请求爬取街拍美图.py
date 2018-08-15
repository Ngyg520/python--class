"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:分析ajax请求爬取街拍美图.PY
@ide:PyCharm
@time:2018-08-13 15:01:04
"""
import urllib.request
from urllib.parse import urlencode
import json
import os
class JPMTSpider(object):
    def __init__(self,offest,keyword):
        self.base_url="https://www.toutiao.com/search_content/?"
        self.offset=offest

    def get_page(self):
        #构造请求
        params={
            "offset":self.offset,
            "format":"json",
            "keyword":"街拍美图",
            "autoload":"true",
            "count":"20",
            "cur_tab":"1",
            "from":"search_tab"
        }

        url=self.base_url+urlencode(params)
        try:
            respons=urllib.request.urlopen(url)
            if respons.status==200:
                html=respons.read().decode('utf-8')#json数据
                #调用解析json数据
                self.parse_json(html)

        except Exception as e:
            return None
    #定义一个函数来解析json数据
    def parse_json(self,html):
        #由于网页源代码是字符串,所以需要调用loads方法进行反序列化,得到一个字典对象
        json_data=json.loads(html)
        #先判断json_data这个字典当中有没有data这个键
        if json_data.get('data'):
            #如果有data这个键,则将这个键对应的列表取出来,并遍历json_data对应的列表,每一个item对应的都是一个字典
            for item in json_data.get('data'):
                #将item这个字典里面的键img_list取出来,对应的结果是一个列表
                image_list=item.get("image_list")
                #将item这个字典里面的键title对应的值取出来
                title=item.get('title')
                self.save_image(title,image_list)

    def save_image(self,title,image_list):
        #先判断是否存在title这个文件夹再创建
        if not os.path.exists(title):
            os.mkdir(title)
        #image_list对应的是一个列表.每一个url_dict是一个列表,将其遍历出来
        for url_dict in image_list:
            #从url_dict这个字典中获取url这个键对应的值是图片的地址
            url=url_dict.get("url")
            #拼接出来图片的完整地址
            image_list="http:"+url
            #给图片设置名称
            img_name=url.split('/')[-1]
            try:
                response=urllib.request.urlopen(image_list)
                if response.status==200:
                    #给每一张图片拼接一个完整的路径
                    file_path='{0}/{1}.{2}'.format(title,img_name,'jpg')
                    #判断title这个文件夹当中有没有img_name这个图片
                    if not os.path.exists(file_path):
                        #with open上下文管理器,使用它不需要手动关闭文件
                        with open(file_path,'wb') as f:
                            #resopense.read()拿到的数据本身就是图片的二进制数据,所以不需要使用decode转换编码,因为存储图片的时候存储的就是二进制数据
                            f.write(response.read())
                    else:
                        print('该图片已经存在')

            except Exception as e:
                print('保存图片失败,原因是',e)

if __name__ == '__main__':
    for x in range(1,40,20):
        spider=JPMTSpider(x,"街拍美图")
        spider.get_page()