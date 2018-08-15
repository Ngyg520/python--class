#大象装进冰箱三个步骤:1.打开冰箱,2.把大象塞进去,3.关闭冰箱
#文件读写的三个步骤:1.打开文件,2.读/写,3.关闭文件


#一些总结:一般的文件流操作都包含缓冲机制,write方法并不直接将数据写入文件,而是将先写入内存中特定的缓冲区.flush方法是用来刷新缓冲区的,即将缓冲区中的数据立即写入文件,同时清空缓冲区,再执行关闭操作,这样即使缓冲区数据未能保存也能保证数据的完整性,如果进程意外退出或者正常退出时而未执行文件的close方法,缓冲区中的内容将会丢失

#文件打开模式:
#r:只读
#w:只写
#a:追加写入模式,如果打开的不存在,则会自动创建,如果存在,则会自动打开,加入文件是空的,光标会在文件的开头位置,假如文件不为空,光标在文件的末尾位置,不论光标位置在哪,都会在文件末尾追加字符.
#w+:写读模式,能写也能读,覆盖写入,写入位置会根据光标的位置而定.
#r+:以读写模式打开文件 	光标在文件开头 	如果文件不存在，则出错。读写都可以移动光标。写入时，如果光标不在文件末尾，则会覆盖源文件.
#a+:追加读写,能写能读,如果文件不存在,则会自动创建,如果存在,则会打开,光标在文件的末尾位置,不论光标位置在哪,都会在文件末尾追加字符.
#rb:二进制读,但是不能设置编码,因为默认就是二进制格式.
#rw:二进制写,但是需要更改写入文件的编码格式.
#ab:二进制追加模式,

#1.创建文件操作的句柄
#open():第一个参数:文件名,第二个参数:文件的打开方式,第三个参数:编码格式.参数之间的位置不能调换
# f=open('ThatGirl.txt','r',encoding='utf-8')
#tell():光标的位置
# print(f.tell())
#read():读取文件,读取括号里可填写读取字符的个数,
# print(f.read(10))
# print(f.tell())
#将光标移到括号填写的相应的位置
# f.seek(0)
# print(f.tell())
# print(f.read(3))
#文件在读取的末实现不能写入数据,写入的模式下.无法读取数据,'w':写入模式,写进去的数据会覆盖原有的数据.
# f.write('hhh')
#不填参数默认读取文件的全部内容
# print(f.read())
# print(f.tell())
#文件的编码格式
# print(f.encoding)
#文件的名称
# print(f.name)


# f=open('ThatGirl.txt','a',encoding='utf-8')
# f.write('hello,')
#------------------------a+:追加读写模式-----------------------
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

# f=open('ThatGirl.txt','r',encoding='utf-8')
#readline():一次只读取一行数据
# print(f.readline())
#readlines():会读取所有航的数据,但是会将每一行的数据当成一个元素存放在列表当中
# print(f.readlines())
# print(f.truncate(3))

# f=open('ThatGirl.txt','w+',encoding='utf-8')
# f.write('hello')
# print(f.read(3))

# f=open('ThatGirl.txt','r+',encoding='utf-8')
# print(f.read(3))
# f.write('hhh')

# f=open('ThatGirl.txt','r+',encoding='utf-8')
# # f.write('world')
# # print(f.read(5))
# f.seek(4)
# f.write('')

#-----------------------------flush--------------------
#假如写入数据的时候,文件中没有写入的数据,需要用到flush刷新一下缓冲区,直接将文件写入到本地文件
f=open('test7.txt','w',encoding='utf=8')
