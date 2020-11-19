# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月19日
"""

class Person(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('我的名字：%s,年龄：%d,性别：%s'%(self.name,self.age,self.sex))

class Teacher(Person):

    def __init__(self,name, age, sex, T_id):
        super().__init__(name, age, sex)
        self.T_id = T_id

    def tell_info(self):
        print('我的教职工id是%d, 名字：%s'%(self.T_id, self.name))

class Student(Person):

    def __init__(self,name, age, sex, S_id):
        Person.__init__(self, name, age, sex)
        self.S_id = S_id

    def tell_info(self):
        print('我的学号id是%d, 名字：%s'%(self.S_id, self.name))

T = Teacher("吴某",21,"男", 2020108847)
T.tell_info()

S = Student("李某", 30, "女", 2018108888)
S.tell_info()