# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("wesley", 18)                 # <class '__main__.Student'>
print(type(s))
print(type(Student))                       # <class 'type'>所有类的类型都是type

# 动态创建一个类
# name是类属性
Teacher_class = type("Teacher", (object,), {"name": "leo"})          # Teacher类名

t = Teacher_class()
print(type(t))
print(t.name)                             # leo

# 创建实例属性
def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

def tell_info(self):
    print(self.year)


Birthday = type("Birthday", (object,), {"__init__": __init__, "tell_info": tell_info})
# Birthday 第一参数是类名
# (object,) 是这个类要继承的类
# {"__init__":__init__}是这个类的方法
b = Birthday(2020, 10, 1)
print(type(b))
print(b.year, b.month, b.day)
b.tell_info()                           # 2020









