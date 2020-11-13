# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""
# 这里只用global

name = 'wesley'
def change_name():
    global name                 # 参数不可以式name
    print(name)
change_name()
print(name)


