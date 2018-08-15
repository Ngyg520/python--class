"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:my_module.PY
@ide:PyCharm
@time:2018-07-25 16:40:09
"""
__all__=['say_hello','name']

name="张三"
age='20'

def say_hello():
    print('hello')
def say_hhh():
    print('哈哈哈')

print('my_module执行了')

if __name__ == '__main__':
    say_hhh()