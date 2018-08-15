"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-20
@author:Mr.Zhang
@file:列表生成器.PY
@ide:PyCharm
@time:2018-07-20 15:54:17
"""
fast_list=(x*x for x in range(1,3))
print(fast_list)
#next():一次只从生成器中取出来一个值，如果元素被取完之后接着取会报错。StopIteration
print(next(fast_list))
print(next(fast_list))
# print(next(fast_list))
for x in fast_list:
    print(x)

# fast_list_1=[x*x for x in range(1,100000)]
# print(fast_list_1)
# fast_list_2=(x*x for x in range(1,1000000000))
# print(fast_list_2)

#列表生成式和列表生成器的区别：
#通过列表生成式，会一次性将所有的值都计算出来存放到列表当中。这样就会占用很大的内存，导致程序卡顿。另外由于计算机内存的限制，列表的容量也是有限的。如果一个列表的数据十分庞大，但是我们只需要访问前几个元素，那么就会导致后面其他的元素占用的内存空间浪费了。
#通过列表生成器，并不会一次性将所有的计算结果存放到内容当中，而是在使用某一下值的时候，才会去动态计算结果并返回，而没有使用的值是不会计算的。





