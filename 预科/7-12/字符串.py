#字符串也可以理解为一个容器,也存在着索引值.也存在索引值,默认不可变

#-----------------------字符串常用函数---------------------------------
string='德玛西亚'
#len():获取字符粗的长度
res1=len(string)
print(res1)
#字符串的取值
res2=string[0]
print(res2)
#切片查询
res3=string[0:3]
print(res3)
#倒数查询
res4=string[-1]
print(res4)
#count():统计某个字符出现的次数
res5=string.count('德')
print('统计某个字符出现的次数',res5)

#find():在匹配到合适的字符串之后,会直接返回该字符串所在位置的起始索引值
#用于查询某字符在字符串中出现的索引位置,会直接返回该字符串所在位置的起始索引值,如果查询不到,则返回-1,

find_str='西'
res6=string.find(find_str)
print('find',res6)
#不会显示亚的索引值
find_str='西亚'
res7=string.find(find_str)
print(res7)
#find():参数1:要找的字符串,参数2,从哪个位置开始找.参数3:找到哪个位置;(取头不取尾),如果不设置范围,则从整个字符串中找.
res7=string.find(find_str,0,1)
print('find',res7)

#index():在匹配到合适的字符串之后,会直接返回该字符串所在位置的起始索引值
res8=string.index(find_str)
print('index',res8)
# 如果查询不到合适的字串符,会报错
# res9=string.index(find_str,0,1)
# print(res9)

#upper():将小写的英文字母全部转换成大写.
string1='abcd'
res10=string1.upper()
print(res10)
#lower():将大写英文字母全部转换成小写
string2='EFGHIJ'
res11=string2.lower()
print('lower',res11)
#split():根据指定字符对一个字符串进行分割,返回值是一个list列表
string4='a;b;c;d'
res12=string4.split(';')
print(res12)
#replace():使用新的字符串替换旧的字符串
string5='a;b'
res13=string5.replace(';','-')
print(res13)

#strip():除去字符串首尾两端的自定字符
string3=';abcd;'
res14=string3.strip(';')
print(res14)

#startswith():判断一个字符串是否以某一个字符开头,返回的结果是True或者False
string6='abcd'
res15=string6.startswith('a')
print(res15)
#endswith():判断一个字符串是否以某一个字符串结尾,返回的结果是True或者False
res16=string.endswith('b')
print(res16)

#----------------字符串的添加和修改-----------------------
#修改
string7='你好'
new_string=string7.replace('你','')
print(new_string)
#1.现将字符串转化成列表
new_list=list(string7)
print(type(new_list))
print(new_list)
#2.向列表中添加字符
new_list.insert(2,'他')
new_list.insert(3,'王')
new_list.insert(4,'吧')
new_list.insert(5,'蛋')
print(new_list)
#3.再将列表转化成字符串
new_string1=''.join(new_list)
print(new_string1)