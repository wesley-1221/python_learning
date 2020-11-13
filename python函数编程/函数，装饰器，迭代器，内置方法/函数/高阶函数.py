# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""
"""
高阶函数满足其一：
接收一个或者多个函数作为输入
return 返回另外一个函数
"""
def add(x, y, f):               #f是abs函数
    return f(x) + f(y)

res = add(3, -6, abs)            #abs绝对值
print(res)