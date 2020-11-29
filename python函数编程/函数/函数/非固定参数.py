# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

# def stu_register(name, age, *args):               #*args会把多传入的参数变成一个元组的形式
#     print(name, age, args)
#
# stu_register("wesley", 20)                        #wesley 20 ()
# stu_register("wesley", 20, "java", "python")      #wesley 20 ('java', 'python')

def stu_register(name, age, *args, **kwargs):      #会把多传入的参数变成一个dict形式
    print(name, age, args, kwargs)

stu_register("wesley",20)                          #wesley 20 () {}
stu_register("wesley", 20, 'java', 'python', sex='male', address='guangxi')            #wesley 20 ('java', 'python') {'sex': 'male', 'address': 'guangxi'}