# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 把一个方法变成 一个静态的属性（变量）

class Student(object):

    def __init__(self, name):
        self.name = name
    @property
    def fly(self):
        print(self.name, 'is flying...')

s = Student("wesley")
# s.fly()                                   # TypeError: 'NoneType' object is not callable
# 可以调用类方法，实例方法
s.fly                                       # wesley is flying...       不用加括号

# 有什么用？



