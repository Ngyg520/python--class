import sqlite3
#定义一个数据模型类,只包含属性,不包含操作函数
class StudentModel(object):
    def __init__(self,db_name,table_name,field_name,field_age,field_id):
        self.db_name=db_name
        self.table_name = table_name
        self.field_name = field_name
        self.field_age = field_age
        self.field_id = field_id

#定义一个操作类,不包含属性
class StudentManager(object):
    #创建库
    def create_connet_and_cursor(self,stu_obj):
        self.connet=sqlite3.connect(stu_obj.db_name)
        self.cursor=self.connet.cursor()
    #创建表
    def create_table(self,stu_obj):
        create_sql="create table if not exists"+stu_obj.table_name+"(%s INTEGER PRIMARY KEY UNIQUE,%s TEXT,%s TEXT )"%(stu_obj.field_id,stu_obj.field_name,stu_obj.field_age)
        self.cursor.execute(create_sql)
    #创建添加数据的函数
    def insert_student_info(self,stu_obj):
        name=input('姓名')
        age=int(input('年龄'))
        insert_sql="insert into"+stu_obj.table_name+"(%s,%s) value ('%s','%s')"%(stu_obj.field_name,stu_obj.field_age,name,age)
        self.cursor.execute(insert_sql)
    #创建一个查询数据库总量的函数
    def get_total_count(self,stu_obj):
        select_sql="select count(*) from %s"%(stu_obj.table_name)
        res=self.cursor.execute(select_sql)
        count=res.fetchone()[0]
        return count
    #定义一个能否查询到ID对应数据的函数
    def get_true_id_false(self,stu_obj,number):
        select_number="select * from %s where id=%d"%(stu_obj.table_nmae,number)
        res=self.cursor.execute(select_number)
        result=res.fetchall()
        return len(result)

    #定义一个查询的函数
    def select_student_info(self,stu_obj):
        count=self.get_total_count(stu_obj)
        if count!=0:
            select_sql="select * from "+stu_obj.table_name
            result=self.cursor.execute(select_sql)
            for id,name,age in result:
                print(id,name,age)
        elif count==0:
            print('学员信息为空,无法查询')
    #定义一个更改数据的函数
    def update_student_info(self,stu_obj):
        count=self.get_total_count(stu_obj)
        if count!=0:
            self.select_student_info(stu_obj)
            number=int(input('学员编号'))
            while self.get_true_id_false(stu_obj,number)==False:
                number=int(input('请冲输入'))
            name=input('xm')
            age=int(input('nl'))
            update_sql="update"+stu_obj.table_name+"set %s='%s',%s='%s' where %s=%s"%(stu_obj.field_name,name,stu_obj.field_age,age,id,number)
            self.cursor.execute(update_sql)
        else:
            print('空')
    #定义一个删除
    def delete_student_info(self,stu_obj):
        count=self.get_total_count(stu_obj)
        if count!=0:
            self.select_student_info(stu_obj)
            print('1')
            print('2')
            select_number=int(input('输入操作号'))
            while select_number!=1 and select_number!=2:
                select_number=int(input('从新'))
            if select_number==1:
                number = int(input('请输入要删除的学员的序号：'))
                while self.get_true_id_false(stu_obj, number) == False:
                    number = int(input('序号输入错误，请重新输入要删除的学员序号：'))
                delete_info="delete from %s where id=%d"%(stu_obj.table_name,number)
            else:
                delete_info="delete from %s "%(stu_obj.table_name)
            self.cursor.execute(delete_info)
        else:
            print('为空')
    def close_db_and_commit(self):
        self.connet.commit()
        self.cursor.close()
        self.connet.close()


if __name__ =="__main__":
    student=StudentModel('Student_plaus.db','Student','name','age','id')
    db_manager=StudentManager()
    db_manager.create_connet_and_cursor(student)
    db_manager.create_table(student)
    while True:
        print('''
        1-添加学员信息
        2-修改学员信息
        3-查询学员信息
        4-删除学员信息
        0-退出程序
        ''')
        select_number=int(input('请选择操作序号:'))
        while select_number<0 or select_number>4:
            select_number = int(input('输入错误,请重新选择操作序号:'))
        if select_number==1:
            db_manager.insert_student_info(student)
        elif select_number==2:
            db_manager.update_student_info(student)
        elif select_number==3:
            db_manager.select_student_info(student)
        elif select_number==4:
            db_manager.delete_student_info(student)
        else:
            break
    db_manager.close_db_and_commit()




