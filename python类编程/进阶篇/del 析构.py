# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

class Student:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("程序结束执行")

# s = Student("wesley")
# print("+++++")
# print("-----")
#
# +++++
# -----
# 程序结束执行

s = Student("wesley")
print("+++++")
# 如果在这里删除s对象，会提前析构
del s
print("-----")

"""
+++++
程序结束执行
-----
"""