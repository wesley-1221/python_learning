# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import sqlite3

con = sqlite3.connect("sqlite3_demo/demo.db")

cur = con.cursor()

sql = """select * from person"""

try:
    cur.execute(sql)
    print("查询成功")
    person_one = cur.fetchone()
    print(person_one)
except Exception as e:
    print(e)
    print("查询失败")
finally:
    cur.close()
    con.close()