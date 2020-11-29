# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 类的组合

class Course(object):

    def __init__(self, subject, price):
        self.subject = subject
        self.price = price

class Birthday(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def surprice(self):
        print("你的生日是%d年%d月%d日"%(self.year, self.month, self.day))

class Student(object):

    def __init__(self, name, sex, age, birthday):
        self.name = name
        self.sex = sex
        self.age = age
        self.birthday = birthday
        self.course = Course("python", 2020)

s = Student('李某','男',20,Birthday(2000, 10, 1))
print("你所学的科目是%s"%s.course.subject)
s.birthday.surprice()
