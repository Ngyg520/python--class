"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-20
@author:Mr.Zhang
@file:文件修改.PY
@ide:PyCharm
@time:2018-07-20 14:41:07
"""
#以读的方式打开ThatGirl.txt这个文件
f = open('ThatGirl.txt','r',encoding='utf-8')
#以写入的方式打开文件，如果文件不存在则自动创建
f_new=open('ThatGirl.bak','w',encoding='utf-8')

for line in f:
    # print(line)
    if '别让他错过' in line:
        line=line.replace('别让他错过','错过就错过')
        f_new.write(line)
    else:
        f_new.write(line)
f.close()
f_new.close()


