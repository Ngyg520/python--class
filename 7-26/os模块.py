"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:7-26
@author:Mr.Yang
@file:os模块.PY
@ide:PyCharm
@time:2018-07-26 09:26:35
"""
#os操作系统,全称(OperationSystem)
#os:用于操作文件/文件夹等等

import os
#1.cpu_count():获取cpu的个数
#根据cpu的个数可以决定创建几个进程更合适,cpu个数=最好开启的进程数
count = os.cpu_count()
print('cpu的个数为{}'.format(count))

#2.getcwd()返回当前文件所在文件夹的绝对路径(重点)
cwd=os.getcwd()
print('当前项目的绝对路径是{}'.format(cwd))

#name
name=os.name
print('操作系统的名称:',name)

#4.os.path.abspth():返回自身所在路径的绝对路径
result=os.path.abspath('os模块.py')
print('绝对路径是{}'.format(result))

#5.os.path.basename:取路径的最后一部分
result_1=os.path.basename('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('取路径的最后一部分:',format(result_1))

#6.os.path.dirname:返回当前文件/文件夹所在的父集文件夹
result_2=os.path.dirname('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('当前文件所在的上一级目录是:',format(result_2))

#7.判断路径下的文件/文件夹是否存在---True存在,False不存在(重点)
result_3=os.path.exists('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('该路径对应的文件是否存在:',format(result_3))

#8.os.path.isfile():判断是否为文件--True存在,False不存在
result_4=os.path.isfile('C:/Users/Administrator/Desktop/7-26')
print('是不是一个文件:',format(result_4))

#9.os.path.isdir():判断是否为文件夹--True存在,False不存在
result_5=os.path.isdir('C:/Users/Administrator/Desktop/7-26')
print('是否为文件夹:',result_5)

#10.os.path.join():拼接路径(小重点)
result_6=os.path.join('C:/Users/Administrator/Desktop/7-26','os模块.py')
print('拼接之后的路径:',format(result_6))

#11.mkdir()创建文件夹(重点)
#如果要在dir_1下面继续创建文件夹,需要切换到dir_1这个文件夹中

# os.mkdir('dir_1')
# print(os.getcwd())

#12.chdir()切换文件夹(重点)
# os.chdir('dir_1')
# os.mkdir('dir_2')
# os.chdir('dir_2')
# os.mkdir('dir_3')
# print(os.getcwd())

#13.makedirs():递归创建文件夹exist_ok=True如果存在也不会报错
# os.makedirs('a/b/c/d',exist_ok=True)
#14.removedirs:递归删除文件夹
# os.removedirs('a/b/c/d')
#补充:renames(递归更名)
# os.renames('a/b/c/d','e/f/g/h')

#15.mknod创建文件,但是windows上面的python不支持这样创建
#os.mknod('test.txt')

#(16.17.18都是重点)
#16.rename():文件更名-----字符串的replace(更换,替换)
# os.rename('test.txt','test1.txt')

#17.remove:文件删除
# os.remove('test1.txt')

#18.os.path.pardir:返回当前文件或者文件夹所在的父集目录
#..父集目录
#.当前目录
#cudir()当前目录
# print('当前文件/文件夹所在的父集目录:{}'.format(os.path.pardir))