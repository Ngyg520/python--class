"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:7-26
@author:Mr.Yang
@file:main_1.PY
@ide:PyCharm
@time:2018-07-26 09:21:13
"""
import sys
print(sys.path)

from package_test.package_test1 import my_module3#调用包里面的包
print(my_module3.weight)
my_module3.say_xixi()

#import my_module 直接导入