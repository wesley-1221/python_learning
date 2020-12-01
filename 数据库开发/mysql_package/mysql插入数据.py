# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import pymysql

con = pymysql.connect("localhost", "root", "521221", "python_sql", 3306)

cur = con.cursor()

sql = "insert into student(sname, age, score) values (%s, %s, %s)"

try:
    cur.execute(sql, ("wesley", 18, 99.5))
    print("插入数据成功")
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
    print("插入数据失败")
finally:
    cur.close()
    con.close()

