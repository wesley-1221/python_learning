# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import sqlite3

con = sqlite3.connect("sqlite3_demo/demo.db")

cur = con.cursor()

sql = """delete from person where pno=?"""
# 单元素元组要加逗号(3,)
try:
    cur.execute(sql, (3,))
    # 提交事务
    print("删除成功")
    con.commit()
except Exception as e:
    print(e)
    print("删除失败")
finally:
    cur.close()
    con.close()
