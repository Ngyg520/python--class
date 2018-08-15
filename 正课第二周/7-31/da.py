"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:da.PY
@ide:PyCharm
@time:2018-07-31 15:19:24
"""
class Student(object ):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def open_file(self):
        file_test = open('student.txt','w',encoding='utf-8')
        return file_test
    def save_data(self,file_test):
        file_test.write(self.name+' '+self.score)
        print('数据写入成功')
    def close_file(self,file_test):
        file_test.close()
        print('文件关闭成功')

# f = Student.open_file()
# student_one = Student('张三','180')
# student_one.save_data(f)
# student_one.close_file(f)
a = Student('张三','20')
f = a.open_file()
a.save_data(f)
a.close_file(f)
