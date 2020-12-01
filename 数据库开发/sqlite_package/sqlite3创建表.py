# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import sqlite3
# 创建连接
con = sqlite3.connect("sqlite3_demo/demo.db")
# 创建游标
cur = con.cursor()
# 编写sql
sql = """create table person
        (
        pno INTEGER primary key autoincrement ,
        pname VARCHAR not null,
        age INTEGER 
        )
    """
# autoincrement自增长
# 执行sql
try:
    cur.execute(sql)
    print("创建表成功")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    # 关闭游标
    cur.close()
    con.close()

