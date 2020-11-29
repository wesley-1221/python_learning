# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

# name = 'wesley'                 #不会调用最内层函数
# def change_name():
#     name = 'leo'
#     def chage_name2():
#         name = 'linda'
#         print(name)
#     print(name)
# change_name()
# print(name)

name = 'wesley'
def change_name():
    name = 'leo'
    def chage_name2():
        name = 'linda'
        print(name)
    chage_name2()                 #函数中调用函数
    print(name)
change_name()
print(name)

