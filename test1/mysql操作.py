# -*- coding:utf-8 -*-
import pymysql.cursors

#链接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='61638752115',
    db='school',
    charset='utf8'
)
#获取游标
cursor = connect.cursor()
#插入数据
mysql = "INSERT INTO p_name (姓名, 年龄, 性别) VALUES ( '%s', %s, '%s')"
# mysql1 = '''CREATE TABLE `p_name` (
# `姓名`  varchar(255) NOT NULL ,
# `年龄`  int(100) NULL ,
# `性别`  char(10) NULL )'''
data = ("中文4",10,"10")
# cursor.execute(mysql % data)
cursor.execute(mysql % data)
connect.commit()
print ("插入操作",cursor.rowcount,"条操作")
connect.close()


