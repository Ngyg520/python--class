"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:main.PY
@ide:PyCharm
@time:2018-07-25 16:40:35
"""
#import本质相当于先把my_module这个模块中的所有代码先解释执行一遍,然后赋值给my_module这个变量,最后通过这个变量调用my_module里面的name,say_hello()
import my_module
my_module.say_hhh()
# print(my_module.name)
# my_module.say_hello()

#from....import....本质:相当于把my_module里面的age,say_hhh先放到main文件中执行一遍,所以就可以直接使用
# from my_module import age,say_hhh
# print(age)
# say_hhh()

# from my_module import *
# def say_hhh():
#     print('这是mian里面的say_hhh')
# print(age)
# print(name)
# say_hello()
# say_hhh()

# from my_module import  say_hhh as say_hhh_one
# say_hhh()
# say_hhh_one()

#当被导入模块中存在__all__=[],则使用from 模块名 import * 这种方式进行导入的时候,只能导入__all__=[]里面定义的变量或者函数

from my_module import *
say_hello()

