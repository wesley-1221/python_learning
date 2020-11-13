# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

def stu_register(name,age):
    print(age)
    if age>20:
        return False
    else:
        return True
stu_register("wesley", 20)

if stu_register:
    print("年龄合格")
else:
    print("不合格")