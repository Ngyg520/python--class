"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-20
@author:Mr.Zhang
@file:文件读写操作.PY
@ide:PyCharm
@time:2018-07-20 10:47:17
"""
#大象装进冰箱的三个步骤：第一步：打开冰箱，第二步：把大象塞进去，第三步：关闭冰箱
#文件读写：1.打开文件。2.对文件进行读/写。3.关闭文件

#文件打开的几种模式:
#1.w:只写模式，如果要打开的文件不存在，则会自动创建。如果存在，则会自动打开。光标在文件的开头位置。会对文件进行覆盖写入。
#2.r:只读模式，如果打开的文件不存在，则会报错。如果存在，则会自动打开。光标在文件的开头位置。
#3.w+：写读模式，可读可写，如果文件不存在，则会自动创建。如果存在，则会自动打开。使用open函数打开文件的时候，会自动将文件里面的内容清空。光标在文件的开头位置。会对文件进行覆盖写入。
#4.r+：读写模式,如果文件不存在，则会报错。如果文件存在，则会自动打开。光标在文件的开头位置。区别于写读模式，打开文件的时候不会清空文件内容。如果光标不在文件的末尾位置，会覆盖源文件。会根据光标的写入位置进行覆盖。没有将会保留。（并不是完全覆盖覆盖的内容）
#5.a：追加只写模式，如果打开的不存在，则会自动创建。如果存在，则会自动打开。假如文件是空的，光标会在文件的开头位置，假如文件不为空，光标在文件的末尾位置。不论光标位置在哪里，都会在文件的末尾位置追加字符。
#6.a+:追加读写模式，如果文件不存在，则会自动创建。如果存在，则会自动打开。假如文件是空的，光标会在文件的开头位置，假如文件不为空，光标在文件的末尾位置。不论光标位置在哪里，都会在文件的末尾位置追加字符。

#一些总结：一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。正常情况下缓冲区满时，操作系统会自动将缓冲数据写入到文件中。至于close方法，原理是内部先调用flush方法来刷新缓冲区，再执行关闭操作，这样即使缓冲区数据未满也能保证数据的完整性。如果进程意外退出或正常退出时而未执行文件的close方法，缓冲区中的内容将会丢失。

#----------------------------------------w只写模式----------------------------------------------
#1.创建文件操作的句柄
# open():第一个参数：文件名；第二个参数：文件的打开方式；第三个参数：文件的编码格式。这几个参数之间的位置不能调换。
# f = open('test.txt','w',encoding='utf-8')
# #1.writable():判断文件是否可写，返回的结果是True或者False
# print(f.writable())
# # #2.readable():判断文件是否可读，返回的结果是True或者False
# print(f.readable())
# # #3.tell():返回当前的光标位置
# print(f.tell())
# f.write('123')
# print(f.tell())
# # #4.name():返回当前文件名称
# print(f.name)
# # #5.encoding:返回当前文件的编码格式
# print(f.encoding)
# # #6.seek():返回到指定的光标位置
# f.seek(0)
# print(f.tell())
# f.write('456')
# # #7.close():关闭文件。因为文件写入，首先是写入到计算机缓存当中，然后再写入到硬盘里。假如不对文件进行关闭，万一电脑出问题关机或者重启，则会导致文件丢失或者损坏。
# f.close()



#-----------------------------------r只读模式----------------------------------------------

# f=open('test1.txt','r',encoding='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writable())
# #read()读取文件，如果read()里面不填写参数，则默认会读取整个文件的内容。
# # print(f.read())
# # print(f.tell())
# # f.seek(0)
# # print(f.read(5))
# #readline():一次只会读取一行数据。
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# #readlines():会读取所有行的数据，但是会将每一行的数据当做一个元素存放在列表中。
# print(f.readlines())
# f.close()


#------------------------------------w+写读模式------------------------------------------
# f=open('test2.txt','w+',encoding='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writable())
# f.write('456')
# print(f.tell())
# f.seek(0)
# print(f.read(1))
# f.close()

#-----------------------------------r+读写模式------------------------------------------
# f=open('test3.txt','r+',encoding='utf-8')
# print(f.tell())
# print(f.writable())
# print(f.readable())
# print(f.read(3))
# print(f.tell())
# f.write('aaa')
# print(f.tell())
# f.seek(5)
# f.write('bbb')
# print(f.tell())
# f.close()

#---------------------------------------a：追加只写模式------------------------------------
# f=open('test4.txt','a',encoding='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writable())
# f.write('bbb')
# print(f.tell())
# f.seek(5)
# f.write('ccc')
# f.close()

#---------------------------------------a+:追加读写模式-----------------------------------
# f=open('test5.txt','a+',encoding='utf-8')
# print(f.tell())
# print(f.writable())
# print(f.readable())
# f.seek(0)
# print(f.read(5))
# print(f.tell())
# f.write('7887')
# print(f.tell())
# f.close()
#--------------------------------------trucate-----------------------------------------
# f=open('test6.txt','a+',encoding='utf-8')
# print(f.tell())
# f.seek(2)
# #trucate():指定长度的话，就从文件的开头开始截断指定长度，其余内容删除；不指定长度的话，就从文件开头开始截断到当前位置，其余内容删除。
# f.truncate(3)
# f.close()

#----------------------------------flush----------------------------------------------
# 假如写入数据的时候，文件中没有写入的数据，需要用到flush刷新一下缓冲区。直接将文件写入到本地文件中。
# f=open('test7.txt','w',encoding='utf-8')
# f.write('123456')
# f.flush()
# f.close()





















