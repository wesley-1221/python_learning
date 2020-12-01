# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月01日
"""

import sqlite3

con = sqlite3.connect("sqlite3_demo/demo.db")

cur = con.cursor()

sql = """update person set pname=? where pno=?"""

try:
    cur.execute(sql,("叶宝宝",1))
    # 提交事务
    print("修改成功")
    con.commit()
    print("提交成功")
except Exception as e:
    print(e)
    print("插入失败")
finally:
    cur.close()
    con.close()