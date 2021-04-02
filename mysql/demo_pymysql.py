# 此文件只为讲解pymusql包的使用，不属于此项目框架
# 作用：连接数据库
# 操作流程：
'''
1、连接数据库，创建数据库对象
2、创建游标对象
3、对数据进行增删改查，都是使用的游标对象
4、关闭游标对象
5、关闭数据库连接
'''
# 导包
import  pymysql
# 连接数据库
conn = pymysql.connect(host='localhost',user='root',passwd='root',database='school',charset='UTF-8')
#创建游标对象
cursor = conn.cursor()
#对数据进行增删改查，都是使用的游标对象
sql = ''
cursor.execute(sql)
# 关闭游标对象
cursor.close()
# 关闭数据库
conn.close()