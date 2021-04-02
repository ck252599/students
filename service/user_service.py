#实现业务逻辑层，对学生进行增删改查的业务逻辑



from mysql.base_mysql import Mysql
class UserService:

    def __init__(self):
        self.m = Mysql()


    # 添加
    # def add_stu(self,name,age,sex,classes,card,city):
    def add_stu(self,*args):
        #1、确定用户数据，最终组装成SQL语句
        lst = list(args)
        while len(lst) <= 6:
            lst.append('')
        sql = "insert into students(name,age,sex,class,card,city) values('{}','{}','{}','{}','{}','{}')".format(*lst)
        #2、调用update（）方法，实现插入操作
        # if isinstance(age,int):
        #     return '输入数据错误，年龄要求输入整数'
        # if age < 0 :
        #     return  '输入年龄不正确'
        result = self.m.update(sql)
        #3、给出用户提示
        if not result:
            print('添加记录成功')
        else:
            print('添加记录失败')
        # pass

    # 删除
    def del_stu(self,name):
        sql = "delete from students where name = '{}'".format(name)
        result = self.m.update(sql)
        if not result:
            print('删除成功')
        else:
            print('删除失败')
        # pass

    # 修改
    def mod_stu(self,column,value,name):
        if str(value).isdigit():
            sql = "update students set {} = {} where name like '%{}%'".format(column, value, name)
        #     注意代码中sql语句里面的标点和空格
        else:
            sql = "update students set {} = '{}' where name like '%{}%'".format(column, value, name)
        result = self.m.update(sql)
        if not result:
            print('修改成功')
        else:
            print('修改失败')
        # pass


    # 查询
    def get_stu(self,name):
        sql = "select * from students where name like '%{}%'".format(name)
        result = self.m.get_all(sql)
        return  result
        # pass
if __name__ == '__main__':
    # sql = "'张三','23','男','1班','123456789456123','北京'"
    use = UserService()
    # use.add_stu('张三','23','男','1班','123456789456123')
    # use.mod_stu('class','7班','刘邦')
    # print(use.get_stu('刘邦'))
    use.del_stu('张三')