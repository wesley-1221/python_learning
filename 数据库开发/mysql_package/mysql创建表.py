# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import pymysql

con = pymysql.connect("localhost", "root", "521221", "python_sql", 3306)

# print(con)
cur = con.cursor()

sql = """
    create table student
    (
    sno int primary key auto_increment ,
    sname varchar (30) not null ,
    age int(2) ,
    score float(3, 1)                         # 三位 整数两位，小数一位
    )
    """

try:
    cur.execute(sql)
    print("创建表成功")
    con.commit()
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    cur.close()
    con.close()



