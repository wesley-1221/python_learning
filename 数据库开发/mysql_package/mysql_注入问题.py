# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月03日
"""

# 结合数据库完成一个用户的登录功能？
import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '521221',
    database = 'python_sql',
    charset = 'utf8'  # 编码千万不要加-
)  # 链接数据库
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

username = input('>>>:')
password = input('>>>:')
sql = "select * from emp where name=%s and sex=%s"
# 不要手动拼接数据 先用%s占位 之后将需要拼接的数据直接交给execute方法即可
print(sql)
rows = cursor.execute(sql,(username,password))  # 自动识别sql里面的%s用后面元组里面的数据替换
if rows:
    print('登录成功')
    print(cursor.fetchall())
else:
    print('用户名密码错误')