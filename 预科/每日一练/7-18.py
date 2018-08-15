#1.使用4,9,2,7四个数字，可以使用+ - * /，每个数字使用一次，使表达式的结果为24。请问表达式是什么____？
print(2*4+9+7)
list_num=[]
# dict1={'q':'4','w':'9','e':'2','r':'7'}
# for key,value in dict1 .items():
#     print(key,value)
#     list2.append(value)
#2.尽可能多的写出列表去重方案，另写出去重的同时保持顺序不变的方案。
list1=['a','b','c','d','a','b','c','a','b','c']
list1.reverse()
for y,value in enumerate(list1):
    num1=list1.count(value)
    if num1>1:
        list1.remove(value)
list1.reverse()
print(list1)
#只把重复的提取出来
list2=['a','b','c','d','a','b','c']
for x,value in enumerate(list2):
    num1=list2.count(value)
    if num1>1:
        list_num.append(value)
for c,value in enumerate(list_num):
    list_num.remove(value)
print(list_num)
list2=['d','s','g','d','g','s','e','f','s','g','g','s','d','s']
set_1=set(list2)
print(list2)










