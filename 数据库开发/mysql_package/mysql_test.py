# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月03日
"""

import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '521221',
    database = 'python_sql',
    charset = 'utf8'  # 编码千万不要加-
)  # 链接数据库
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 产生一个游标对象(就是用来帮你执行命令的)
"""
cursor=pymysql.cursors.DictCursor将查询结果以字典的形式返回
"""
sql = 'select * from emp;'
res = cursor.execute(sql)
# print(res)  # execute返回的是你当前sql语句所影响的行数  改返回值一般不用
# 获取命令执行的查询结果
# print(cursor.fetchone())  # 只拿一条
# print(cursor.fetchall())  # 拿所有
# print(cursor.fetchmany(2))  # 可以指定拿几条
print(cursor.fetchone())
print(cursor.fetchone())  # 读取数据类似于文件光标的移动
# cursor.scroll(1,'relative')  # 相对于光标所在的位置继续往后移动1位
cursor.scroll(10,'absolute')  # 相对于数据的开头往后继续移动1位        # 取第 n+1 条数据
print(cursor.fetchall())


