# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 不能访问类变量，也不可以访问实例变量
# 它与类唯一的关联就是需要通过类名来调用这个方法

class Student(object):

    role = "Stu"

    def __init__(self, name):
        self.name = name
    @staticmethod         # 和类没有任何关系了，
    def fly(self):
        print(self.name, 'is flying...')

    @staticmethod
    def walk():          # 实际没有参数， 没什么用
        print('student is flying...')

s = Student("wesley")
# s.fly()                          # TypeError: fly() missing 1 required positional argument: 'self'
# 静态方法没有指定帮忙传值（实例本身）
# 静态方法隔断了它和类或者实例的任何关系
s.fly(s)                          # 手动传值

