# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 如何反射一个文件下指定的字符串对应的属性
import sys
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, 'walking........')

# def talk(self):                                  # 给类绑定方法
#     print(self.name, "is speaking")

p = Person("wesley", 18)
# print(sys.modules[__name__])
mod = sys.modules[__name__]
if hasattr(mod, "p"):
    o = getattr(mod, "p")
    print(o)                      # <__main__.Person object at 0x0000019FC71D2D88>
    o.walk()
print(p)                          # <__main__.Person object at 0x0000019FC71D2D88>
p.walk()

