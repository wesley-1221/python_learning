# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月14日
"""


def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


doSomethingBeforeHi(hi)
# outputs:I am doing some boring work before executing hi()
#         hi yasoob!