"""
PyMySQL连接数据库模块
"""
#1、导入库
import pymysql
#2、连接数据库
conn = pymysql.connect(host="192.168.3.151",
                       user="root",
                       password="Centos2026",
                       db="api_auto",
                       port=3306,
                       charset="utf8")
#3、创建游标
cursor = conn.cursor()
#4、增删改查
#准备SQL
sql = "SELECT * FROM login_user"
#执行SQL语句
cursor.execute(sql)
#获取结果
result = cursor.fetchall()
print(result)
#5、关闭游标
cursor.close()
#6、关闭连接
conn.close()
