# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import sqlite3

con = sqlite3.connect("sqlite3_demo/demo.db")

cur = con.cursor()
# 自增长可不插入
sql = """
    insert into person(pname, age) values (?,?)
    """

try:
    cur.executemany(sql, [("leo", 21), ("linda", 22)])
    print("插入多条数据成功")
    con.commit()
    print("提交成功")
except Exception as e:
    print(e)
    con.rollback()
    print("插入多条数据失败")
finally:
    cur.close()
    con.close()