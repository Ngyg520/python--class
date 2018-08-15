"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课
@author:Mr.Yang
@file:异常捕获.PY
@ide:PyCharm
@time:2018-07-23 15:43:34
"""

#try....except....:用于捕获代码异常,当一段程序出现异常的时候,会导致程序崩溃,整个程序会结束运行,后续的一些代码逻辑也不会再执行.,,,,,但是异常被捕获并进行处理,可以保证整个程序的正常进行,后续的代码也不会受到异常的影响

try:
    #写要捕获异常的代码
    pass
except Exception as e:
    #Exception:异常类,基本上都能捕获常见的异常情况,表示异常原因
    #e,用于接收错误原因的.
    pass
    #出现异常时,需要设置的代码逻辑
    #当try里面的代码执行成功的时候,则不会执行except Exception as e 里面的代码
else:
    pass
    #如果try里面的代码执行成功,则紧接着会执行else中的代码
    #如果try出现异常没有执行成功,则不会执行else里面的代码
finally:
    pass
    #不管try执行成功还是失败,最终都会执行finally语句里面的代码


#example:
list1=[]
try:
    print(list1[0])
except Exception as e:
    print('try里面的代码没有执行成功,需要执行我')
    print('错误的原因error:',e)
else:
    print('try里面的代码执行成功,则会接着执行我!try里面的代码没有执行成功,则不会执行我!')
finally:
    print('不管try执行成功还是失败,都会最终执行我!')


try:
    print(list1[0])
except IndexError as e:
    print('try里面的代码没有执行成功,需要执行我')
    print('错误的原因error:',e)
else:
    print('try里面的代码执行成功,则会接着执行我!try里面的代码没有执行成功,则不会执行我!')
finally:
    print('不管try执行成功还是失败,都会最终执行我!')

try:
    import  a
except Exception as e :
    print('错误原因error:',e)


#在函数内部自定义一个异常:当调用该韩式的时候,如果不符合函数内部定义的条件,则抛出这个异常!如果符合函数条件,就不抛出异常!
#raise:抛出异常原因的关键字
def is_outrange(age):
    if age <16:
        raise Exception('小于16周岁,不能谈恋爱!')
    else:
        return True
try:
    res= is_outrange(15)
except Exception as  e:
    print('错误原因error:',e)


#面试题中常问的问题:你遇到过的错误类有哪些?

#ImportError:导入错误
#indexError:索引错误
#NameError:尝试访问一个没有声明的变量
#SyntaxError:语法错误
#AttributeError:尝试访问未知的对象属性
#KeyError:请求一个不存在的字典关键字
#ValueError:传给函数的参数类型不正确
#.................

