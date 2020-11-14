# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月14日
"""


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet()               #注意加没加括号的区别
    else:
        return welcome


a = hi()
print(a)
# outputs: <function greet at 0x7f2143c01500>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# 现在试试这个

#print(a())
# outputs: now you are in the greet() function