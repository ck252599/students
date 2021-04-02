#需求：
'''
1、创建查询和修改的方法
2、把上面的创建的方法抽象一个类，专门做数据库的操作
'''
import  pymysql
from setting import DB_CONFIG
class Mysql():

         
    def  __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)

    # 实现查询方法
    def get_all(self,sql):
        try:
            # cursor = self.conn.cursor()
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    # 实现修改方法 ：需要增加一个提交功能
    def update(self,sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                # 手动提交方法
                self.conn.commit()
        except  Exception as e:
            self.conn.rollback() #回滚操作，回滚到上述代码未执行之前
            print(e)

        finally:
            if self.conn:
                self.conn.close()


if __name__ == '__main__':
    sql = 'select * from students where age = 30'
    sql1 = 'update students set age = 34 where studentNO = 4'
    m = Mysql()
    # print(m.get_all(sql))
    m.update(sql1)