# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""
# 不同变量的作用域不同就是由这个变量所在的命名空间觉得的、

"""
三种：
locals:    是函数的名称空间，包括局部变量和形参
globals:   全局变量，函数定义所在模块的名字空间
builtins:  内置模块的名字空间
"""
level = 'L0'
n = 20

def func():
    level = 'L1'
    n = 30
    print(locals())

    def outer():
        level = 'L2'
        n = 40
        print(locals(), n)

        def inner():
            level = 'L3'
            print(locals(), n)

        inner()

    outer()

func()

"""
{'level': 'L1', 'n': 30}
{'level': 'L2', 'n': 40} 40
{'level': 'L3', 'n': 40} 40             #因为inner也是outer的内部
"""

# name = 'wesley'
# age = '20'
# def change_name(a, b, address='广西'):
#     global age
#     name = 'leo'
#     print(locals())
#     print(globals())
#     #print(__builtins__)
# change_name(age, name)


