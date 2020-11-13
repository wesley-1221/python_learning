# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

def outer():
    name = "wesley"

    def inner():
        print("在inner里打印外层函数的变量", name)

    return inner                 # 重要，联系后面

f = outer()

f()                              # 重要

"""
意义：返回的函数对象， 不仅仅是一个函数的对象，在该函数外还包裹了一层作用域， 
使得无论在何处调用，优先使用自己外层的作用域
"""