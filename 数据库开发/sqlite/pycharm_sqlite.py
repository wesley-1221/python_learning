# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月07日
"""
import sqlite3


def init_db(dbpath):
    sql = '''
        create table movie250 
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        )

    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
if __name__ == '__main__':
    dbpath = "movie.db"
    init_db(dbpath)